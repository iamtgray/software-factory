# The Same Change, Air-Gapped

The same fix, delivered into an enclave with no network path out. No DNS, no registry pull, no transparency log, no identity provider.

Read this as a diff against [the connected flow](connected.md). Steps 1 to 9 happen on the low side much as before. After that, two steps break and a third only appears to.

---

## Air gap and cross-domain are different problems

**Air gap** means no network path. Transfer happens by physical media, and nothing inspects the bytes.

**Cross-domain** means a guard or diode mediates the transfer, and **may refuse or rewrite what crosses**.

Almost all confusion in this field comes from treating these as one thing. They have completely different answers, and one of them is largely solved.

=== "Air gap -- largely solved"

    A standard OCI layout carries images, signatures, attestations, SBOMs and the referrers graph. One widely-used tool does this by default; another performs full offline verification with a trust root **embedded in its own binary**. Evidence crosses an air gap intact.

=== "Cross-domain -- genuinely unsolved"

    A guard enforcing content policy may transform data to sanitise it. Transformation changes bytes; changed bytes break every signature over them.

    This is the tension that has no clean answer, and it has a page of its own: [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

---

## What breaks, and what only looks like it does

### Break 1 -- step 3, the agent, degrades by hardware rather than by classification

The enclave has no managed frontier model. The slot takes a different implementation: a gateway in front of locally-hosted open-weight models.

The honest numbers, from the one contamination-controlled independent leaderboard available:

| Tier | Capability vs frontier |
|---|---|
| Hyperscale cloud, frontier model | baseline |
| Government cloud | near parity -- the penalty is operational, not capability |
| Enclave with ~8 high-end GPUs | **~95-100%** on contamination-controlled bug fixing |
| Enclave with 1-2 GPUs | **48-60%** |

!!! quote "The cliff is GPU count, not classification"
    An air-gapped enclave with a serious GPU estate gets a genuinely good agent. A *connected* deployment with no GPUs and no model quota gets a worse one.

    This is the opposite of how the trade-off is usually described.

The capability descriptor acts on this. In the GPU-poor tier it disables `autonomous-multi-file-change` and `long-horizon-task`, and **increases the review scrutiny tier** -- because weaker generation means more human attention per change, which is a policy consequence rather than a feature flag.

And one genuine inversion: **the enclave gets the better AI story on the things that matter.** What survives without frontier models is exactly the set of patterns that have deterministic verifiers -- false-positive triage of scanner findings, validated test generation with a filter chain, mechanical refactoring from recipes. What dies -- agentic review as a gate, autonomous multi-file remediation, VEX justification selection -- is mostly what a factory shouldn't have trusted anyway. See [AI: Capability vs Provability](../tradeoffs/ai.md).

### Break 2 -- step 9, discovery by API becomes discovery by tag

This break silently produces a bundle whose evidence is present but unfindable.

Attestations are discovered by querying the registry: *what is attached to this digest?* That is a **live HTTP call**, and it has no file-based equivalent.

!!! warning "The rule"
    **The registry must support the referrers API. The bundle must not depend on it.**

    Bundle creation has to **materialise the referrers graph into the fallback tag scheme** and record the subject-to-referrer mapping in the manifest. Otherwise the far side holds the signature bytes and cannot find them.

Three related things that also break, all of them network calls with no offline equivalent:

- revocation checking -- no offline mechanism is both fresh and complete
- transparency-log lookup -- needs an inclusion proof and signed checkpoint carried *inside* the bundle
- package-manager metadata refresh, including module checksum databases that perform a live log lookup by default

### Break 3 -- step 10 onward, and this one is less broken than it looks

Keyless signing exchanges an identity token for a certificate valid for about ten minutes. The intuition is that this is useless for an artefact verified in a different trust domain six months later, because the far side can't reach the issuer to establish the signature was made while the certificate was valid.

That intuition is wrong, and it is the problem Sigstore was built to solve.

!!! info "Payload lifetime is decoupled from certificate lifetime"
    The signer has the signature timestamped, and the verifier checks that the timestamp falls inside the certificate's validity window. The client specification states the design goal directly: *"we decouple the payload lifetime from the certificate lifetime."*

    The proof ships inside the bundle -- a transparency-log inclusion proof and signed checkpoint, or an RFC 3161 timestamp. No network call, and no long-lived key.

A package bundle whose leaf certificate was valid for ten minutes on 28 July 2026, carrying no RFC 3161 timestamps and no long-lived key, verified successfully offline **two months after that certificate expired**, with all egress forced through a dead proxy. Flipping one byte of the inclusion proof's root hash made it fail, so the Merkle proof is doing the work.

The usual rule of thumb -- *keyless within a trust domain, long-lived keys across* -- has the pairing backwards. What is true is narrower:

- **Inside a trust domain, keyless is right and cheap.** A workload-identity system feeding your own certificate authority is configuration rather than code: the CA has a first-class SPIFFE issuer type, a validated trust-domain field, and config validation that rejects a SPIFFE issuer without one.
- **Across a boundary, keyless still works, provided the bundle carries its own verification material** -- the inclusion proof, the checkpoint, the trusted root. That is a bundle-construction requirement, not a key-management one.
- **A long-lived key in a hardware module is a legitimate choice**, but for accreditation reasons rather than cryptographic necessity. Some regimes mandate it. Do not claim you need one because keyless cannot cross.

Re-signing at a classification boundary remains live practice regardless -- a production defence pipeline's signing wrapper carries a parameter documented for use *"during re-signing or cross IL"*. But that is about who vouches for what crossed, not about whether a signature survives.

---

## What crosses, concretely

```
bundle.tar                      # sorted entries, fixed timestamps
├── MANIFEST.json               # the only semantically rich file; small; strictly schema'd
├── MANIFEST.sig                # two signatures: factory release key + release authority
├── TRUST/
│   ├── root.json               # current trust root
│   ├── root.history/           # every previous root, for offline chain-walking
│   ├── trusted_root.json       # verification material, cumulative
│   └── crl/                    # revocation set, with its issue time
├── EVIDENCE/
│   ├── attestations/*.dsse     # provenance, SBOM, tests, VEX
│   ├── scans/*.json            # with the vulnerability-DB version used
│   └── importer/*.dsse         # what the release authority verified
└── blobs/sha256/<64-hex>       # flat content-addressed payload
```

The manifest carries the things the [freshness primitive](../how/primitives.md#5-freshness-and-monotonicity-state) demands: `validNotBefore` / `validNotAfter`, a strictly monotonic `sequence` per producer-destination pair, `supersedes`, and the trust-root version and expiry.

**The far side's verification path**, in order:

1. validate the manifest against its schema
2. verify the manifest signature against the trust root **that travelled inside the bundle**
3. check `sequence` against a stored high-water mark -- the only defence against rollback and omission when you cannot ask anything
4. for every blob, confirm `sha256(content) == name`

That is a complete integrity and authenticity check needing no understanding of OCI, Helm or ELF. Everything in `EVIDENCE/` is then additional verification at leisure, so provenance-rich checks **degrade gracefully rather than blocking deployment**.

## What does not cross, and the honest admission

**Upstream provenance, in practice.** Common tooling regenerates SBOMs locally during packaging, so the packager's assertion substitutes for the builder's. Build provenance, scan verdicts and control evidence often do not travel at all.

**Nothing is obliged to look.** This is the real gap. One widely-used tool's receiving-side load command has a single flag and no verification whatsoever; its global error-tolerance flag demotes a verification failure to a warning *"including storing images that failed verification"*. Another's deploy-time verification defaults to `if-possible`, so an unsigned package deploys quietly.

!!! danger "Where trust actually terminates"
    If a guard transformed anything, or the far side cannot reach the near side's signing infrastructure, **trust terminates at the importer, not the original builder.**

    That is a delegated, auditable, *named* link rather than an unbroken cryptographic chain. Say so in the architecture document. An assessor who discovers it themselves will trust nothing else you wrote.

## Steps 11 and 12 barely exist

The feedback loop is the quiet casualty, and most designs forget it.

In a strictly one-way architecture, *did the deployment work* cannot come back. The only automatable exception published anywhere is a **tiny fixed-schema receipt**: bundle manifest digest, an outcome from a closed enumeration, a component pass/fail bitmap, a monotonic counter, a timestamp, and a signature. Fixed length, no free text, no attacker-influenceable content.

That is enough to resynchronise the sender's delta bookkeeping and confirm deployment, at a covert-channel bandwidth of a few bits -- which is quantifiable, and therefore arguable in an accreditation conversation. Anything richer goes through human review on a slower cadence, or does not come back.

!!! quote "The uncomfortable conclusion"
    Plan for a factory that ships blind and a far side that operates autonomously, rather than pretending continuous delivery extends across the boundary.

## And deltas, because a full bundle is tens of gigabytes

You can't ask the far side what it already has. **So don't ask -- remember.**

Every working one-way delta mechanism is sender-side bookkeeping: the near side keeps an authoritative per-destination record of what it has transmitted and ships the difference. That turns an unanswerable question into accounting. The one acknowledged receipt above is what lets the record resynchronise if it is ever in doubt.

The best prior art is twenty-five years old and worth copying rather than reinventing: a signed index over static deltas, where the index commits to content by hash and the payload inherits the signature transitively. Linux distribution package management has worked across air gaps for decades for exactly this reason.
