# The Same Change, Air-Gapped

The same fix, delivered into an enclave with no network path out. No DNS, no registry pull, no transparency log, no identity provider.

Read this as a diff against [the connected flow](connected.md). Most of the eleven steps happen on the low side much as before. The agent at step 3 breaks. Attestation discovery at step 9 breaks. From step 10 onward things survive the crossing, once the bundle carries its own verification material.

---

## Air gap and cross-domain are different problems

**Air gap** means no network path. Transfer happens by physical media, and nothing inspects the bytes.

**Cross-domain** means a guard or diode mediates the transfer, and **may refuse or rewrite what crosses**.

Most of the confusion I run into comes from treating these as one thing. Their answers have little in common, and only one of the two looks largely solved to me.

=== "Air gap -- largely solved"

    A standard OCI layout carries images, signatures, attestations, SBOMs and the referrers graph. One widely-used tool does this by default; another performs full offline verification with a trust root **embedded in its own binary**. Evidence crosses an air gap intact.

=== "Cross-domain -- still unsolved, as far as I can tell"

    A guard enforcing content policy may transform data to sanitise it. Transformation changes bytes; changed bytes break every signature over them.

    I haven't found a clean answer to that tension. It gets a page of its own: [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

---

## What breaks, and what holds

### Break 1 -- step 3, the agent, degrades with GPU count

With no managed frontier model available to it, the enclave fills the slot with a gateway in front of locally-hosted open-weight models.

The honest numbers, from the one contamination-controlled independent leaderboard I could find:

| Tier | Capability vs frontier |
|---|---|
| Hyperscale cloud, frontier model | baseline |
| Government cloud | near parity -- the penalty falls on operations |
| Enclave with ~8 high-end GPUs | **~95-100%** on contamination-controlled bug fixing |
| Enclave with 1-2 GPUs | **48-60%** |

!!! quote "The cliff is GPU count"
    An air-gapped enclave with a serious GPU estate gets a genuinely good agent, while a *connected* deployment with no GPUs and no model quota gets a worse one.

    On these numbers, hardware budget predicts agent quality and connectivity predicts operational pain.

The capability descriptor acts on this. In the GPU-poor tier it disables `autonomous-multi-file-change` and `long-horizon-task`, and **increases the review scrutiny tier** -- a policy consequence of the hardware, because weaker generation means more human attention per change.

The bit that took me longest to believe: **the enclave gets the better AI story on the things that matter.** What survives without frontier models looks like the set of patterns that have deterministic verifiers -- false-positive triage of scanner findings, validated test generation with a filter chain, mechanical refactoring from recipes. What dies -- agentic review as a gate, autonomous multi-file remediation, VEX justification selection -- is mostly what a factory shouldn't have trusted anyway. See [AI: Capability vs Provability](../tradeoffs/ai.md).

### Break 2 -- step 9, discovery by API becomes discovery by tag

The nasty part is how quietly this one fails: the bundle still carries its evidence, and the far side cannot find it.

Attestations are discovered by querying the registry: *what is attached to this digest?* That is a **live HTTP call**, and I know of no file-based equivalent.

!!! warning "The rule"
    **The registry must support the referrers API. The bundle must verify without it.**

    Bundle creation has to **materialise the referrers graph into the fallback tag scheme** and record the subject-to-referrer mapping in the manifest. Otherwise the far side holds the signature bytes and cannot find them.

Related things that also break, all of them network calls:

- revocation checking -- no offline mechanism I know of is both fresh and complete
- transparency-log lookup -- needs an inclusion proof and signed checkpoint carried *inside* the bundle
- package-manager metadata refresh, including module checksum databases that perform a live log lookup by default

### Break 3 -- step 10 onward, keyless signing survives the crossing

Keyless signing exchanges an identity token for a certificate valid for about ten minutes. Verification in a different trust domain six months later, by a far side with no path back to the issuer, is the exact case Sigstore was built for, and the ten-minute window survives it. The worry that it can't comes up a lot, and as far as I can tell it's a misreading.

!!! info "Payload lifetime is decoupled from certificate lifetime"
    The signer has the signature timestamped, and the verifier checks that the timestamp falls inside the certificate's validity window. The client specification states the design goal directly: *"we decouple the payload lifetime from the certificate lifetime."*

    The proof ships inside the bundle -- a transparency-log inclusion proof and signed checkpoint, or an RFC 3161 timestamp. No network call, and no long-lived key.

A package bundle whose leaf certificate was valid for ten minutes on 28 July 2026, carrying no RFC 3161 timestamps and no long-lived key, verified successfully offline **two months after that certificate expired**, with all egress forced through a dead proxy. Flipping one byte of the inclusion proof's root hash made it fail, so the Merkle proof is doing the work.

The usual rule of thumb -- *keyless within a trust domain, long-lived keys across* -- has the pairing backwards, I think. The narrower claims I'd stand behind:

- **Inside a trust domain, keyless is right and cheap.** A workload-identity system feeding your own certificate authority is a matter of configuration: the CA has a first-class SPIFFE issuer type, a validated trust-domain field, and config validation that rejects a SPIFFE issuer without one.
- **Across a boundary, keyless still works, provided the bundle carries its own verification material** -- the inclusion proof, the checkpoint, the trusted root. That obligation belongs to bundle construction, where it is cheap to discharge.
- **A long-lived key in a hardware module is a legitimate choice**, taken on accreditation grounds. Some regimes mandate it. Just don't justify it on the grounds that keyless can't cross -- that part doesn't hold.

Re-signing at a classification boundary is live practice anyway, at least in the one production defence pipeline I've seen up close, whose signing wrapper carries a parameter documented for use *"during re-signing or cross IL"*. That practice records who vouches for what crossed.

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
3. check `sequence` against a stored high-water mark -- the only defence I can see against rollback and omission when you cannot ask anything
4. for every blob, confirm `sha256(content) == name`

That is a complete integrity and authenticity check needing no understanding of OCI, Helm or ELF. Everything in `EVIDENCE/` is then additional verification at leisure, so provenance-rich checks **degrade gracefully** and deployment proceeds.

## What does not cross

**Upstream provenance, in practice.** Common tooling regenerates SBOMs locally during packaging, so the packager's assertion substitutes for the builder's. Build provenance, scan verdicts and control evidence often don't travel at all.

**Nothing is obliged to look.** This is the gap that worries me most. One widely-used tool's receiving-side load command has a single flag and no verification whatsoever; its global error-tolerance flag demotes a verification failure to a warning *"including storing images that failed verification"*. Another's deploy-time verification defaults to `if-possible`, so an unsigned package deploys quietly.

!!! danger "Where trust actually terminates"
    If a guard transformed anything, or the far side cannot reach the near side's signing infrastructure, **trust terminates at the importer.**

    The cryptographic chain ends there. Past that point you have a delegated, auditable, *named* link. Say so in the architecture document -- an assessor who works it out for themselves probably won't trust anything else you wrote.

## Step 11, the loop closing, barely exists

The feedback loop is the quiet casualty. Every design I've read leaves it alone until the far side has already been deployed to.

In a strictly one-way architecture, *did the deployment work* cannot come back. The only automatable exception I've found published is a **tiny fixed-schema receipt**: bundle manifest digest, an outcome from a closed enumeration, a component pass/fail bitmap, a monotonic counter, a timestamp, and a signature. Fixed length, no free text, no attacker-influenceable content.

That is enough to resynchronise the sender's delta bookkeeping and confirm deployment, at a covert-channel bandwidth of a few bits -- which is quantifiable, and therefore arguable in an accreditation conversation. Anything richer goes through human review on a slower cadence, or does not come back.

!!! quote "The uncomfortable conclusion"
    Plan for a factory that ships blind and a far side that operates autonomously. Continuous delivery stops at the boundary, and I haven't found a way round that which an accreditor would sign.

## And deltas, because a full bundle is tens of gigabytes

You can't ask the far side what it already has. **So keep the record yourself.**

Every one-way delta mechanism I've seen work is sender-side bookkeeping: the near side keeps an authoritative per-destination record of what it has transmitted and ships the difference. That turns an unanswerable question into accounting. The one acknowledged receipt above is what lets the record resynchronise if it is ever in doubt.

The best prior art I know of is twenty-five years old, and worth copying: a signed index over static deltas, where the index commits to content by hash and the payload inherits the signature transitively. Linux distribution package management has worked across air gaps for decades for exactly this reason.

Which leaves the questions I can't answer from this side of the boundary. What GPU estate does the enclave actually get (it sets the review scrutiny tier as much as it sets agent quality)? And what comes back across the boundary -- a few bits of signed receipt, or nothing at all?
