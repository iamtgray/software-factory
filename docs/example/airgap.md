# The Same Change, Air-Gapped

The same fix, delivered into an enclave with no network path out. No DNS, no registry pull, no transparency log, no identity provider.

Read this as a diff against [the connected flow](connected.md). Steps 1 to 9 happen on the low side much as before. After that, three steps break.

---

## Air gap and cross-domain are different problems

**Air gap** means no network path. Transfer happens by physical media, and nothing inspects the bytes.

**Cross-domain** means a guard or diode mediates the transfer, and **may refuse or rewrite what crosses**.

Almost all confusion in this field comes from treating these as one thing. They have completely different answers, and one of them is largely solved.

=== "Air gap -- largely solved"

    A standard OCI layout carries images, signatures, attestations, SBOMs and the referrers graph. One widely-used tool does this by default; another performs full offline verification with a trust root **embedded in its own binary**.

    The original premise of this project was that evidence does not cross. That was **wrong**, and the correction is on the [What We Got Wrong](../start/corrections.md) page.

=== "Cross-domain -- genuinely unsolved"

    A guard enforcing content policy may transform data to sanitise it. Transformation changes bytes; changed bytes break every signature over them.

    This is the tension that has no clean answer, and it has a page of its own: [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

---

## The three steps that break

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

### Break 3 -- step 10 onward, signing identity

Keyless signing exchanges an identity token for a short-lived certificate (valid for about ten minutes). Fine in connected CI. Useless for an artefact verified in a *different* trust domain six months later, because the far side can't reach the issuer to establish that the signature was made while the certificate was valid.

!!! success "The rule that resolves it"
    **Keyless within a trust domain. Long-lived hardware-held keys across trust domains.**

    A workload-identity system feeding a local certificate authority works *inside* the enclave, and inside the low-side factory, because each runs its own. But anything whose signature must be checked in a different trust domain than it was made in needs a long-lived key in a hardware security module, plus a timestamp as the transparency substitute.

A production defence pipeline already does exactly this -- its signing wrapper carries a parameter documented for use *"during re-signing or cross IL"*, meaning across impact levels. Re-signing at a classification boundary is live practice, not a theory.

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
