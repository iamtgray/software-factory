# What We Got Wrong

Eight load-bearing claims went through adversarial verification: three independent agents per claim, each instructed to *refute* it rather than confirm it, working from primary sources.

**Result: three refuted, five weakened, nothing survived intact.**

Sections 2, 3, 5 and 6 below come from that exercise. Sections 1 and 4 are errors caught elsewhere in the research, and they are here because they would embarrass you in the same room.

Every correction makes the position narrower and harder to knock down in front of someone who knows the field.

---

## 1. "No open-source project is a software factory" -- false

Konflux-CI's own README describes it as *"a cloud-native software factory"* that brings together *"best-in-class open source projects"*. Apache-2.0, self-hostable on any conformant Kubernetes.

**And SBOM generation is commodity.** Konflux attaches them, Zarf generates them by default via Syft, Iron Bank emits four formats.

!!! danger "Do not say"
    "There is no open-source software factory, and ours produces SBOMs." Both halves are falsifiable in ninety seconds and the claim makes the whole position look unresearched.

---

## 2. "The evidence does not cross the air-gap with the artefact" -- **refuted**

This was the central thesis. It's wrong for the ordinary media-gap case, and the refutation came from reading the source of the tools involved.

**Hauler** carries cosign signatures, attestations, SBOMs *and* the OCI 1.1 referrers graph **by default** -- the `--exclude-extras` flag defaults to false. It stores them in a plain zstd-compressed OCI layout, and on the far side reconstructs the `sha256-<digest>.sig` / `.att` / `.sbom` tags and re-pushes referrers by digest. Big Bang documents this as its production air-gap path and states that `cosign verify` works against the internal registry *"without reaching back to the source"*.

**Zarf goes further.** `zarf package verify` checks signature and checksum integrity entirely offline, with a Sigstore trusted root **embedded in the binary**, `--insecure-ignore-tlog` defaulting to true "for air-gap", and RFC 3161 timestamp verification.

The test originally set -- *a high side can independently establish what it was given with zero network access and no ability to ask the low side anything* -- **is met today by an existing command.**

### What is actually missing

Four things, and they're better problems than the original claim:

**1. The verification gate.** The evidence arrives; nothing is obliged to look at it. Hauler's disconnected-side `load` command has exactly one flag (`--filename`) and no verification of any kind. Its global `--ignore-errors` demotes a verification failure to a warning *"including storing images that failed verification"*. And `zarf package deploy --verify` defaults to `if-possible`, so an unsigned package deploys quietly.

**2. Shipment-level evidence.** What crosses is *per-image* signing evidence that rides along because the cosign tag convention happens to live inside the OCI layout. Nothing states what a transfer is *supposed* to contain, who authorised it, or what policy was in force -- so **omission and rollback are undetectable by construction**. Big Bang 3.34.0's haul tarball is authenticated by an unsigned checksums file whose entry for itself is `e3b0c442...b7852b855`: the SHA-256 of the empty string.

**3. Upstream provenance.** Zarf regenerates SBOMs locally with Syft, so the packager's assertion substitutes for the builder's. Build provenance, SLSA attestations, scan verdicts, VEX and control evidence do not cross at all.

**4. Guard-mediated crossing.** Everything above is sneakernet. No open-source project models a cross-domain guard.

!!! success "The corrected claim"
    **A standard OCI layout already crosses and already carries the evidence. What is missing is a fail-closed receiver-side gate over a signed shipment manifest.**

    This is a better position. Inventing a bespoke transfer format would produce a one-implementation artefact needing its own accreditation, and an accreditor's first question would be *"why not OCI layout?"* -- to which "we thought evidence didn't cross" is a factually wrong answer.

---

## 3. "Only one cross-domain implementation exists in open code" -- **refuted**

A universal negative asserted over all open source, by a project with **no working code search**. GitHub code search needs authentication; `grep.app` is bot-blocked; `searchcode` is dead.

The verifiers found counter-examples quickly -- including **`hairgap`**, **`eurydice`** and ANSSI's **`lidi`**, all one-way transfer implementations.

The *description* of Iron Bank's `upload_to_cds.py` is verified and sound. The *uniqueness quantifier* is deleted, not downgraded to "appears to be".

!!! warning "Standing rule"
    No finding may assert a universal negative over open code. Without code search at scale, "we found none" means "we did not find one", and the strength of that depends entirely on how we looked.

---

## 4. "The OSCAL file was untouched for three and a half years" -- wrong mechanism

Inferred from metadata without checking history. The real history is **six commits**, with the last substantive edit in April 2023 and later commits being a URL fix and a global departmental find-and-replace.

So the content *is* about three years stale, but the mechanism is more damning: **mechanical sweeps make it look maintained in the commit log** while nobody has reviewed its substance.

The better framing is the gate story: built Feb 2024, disabled Aug 2024, deleted Sep 2025. See [The Problem](the-problem.md).

---

## 5. "Keyless signing can't cross a trust boundary" -- **refuted, and backwards**

The rule asserted here was *keyless within a trust domain, long-lived hardware keys across trust domains*, on the reasoning that a ten-minute certificate can't be validated by a far side that can't reach the issuer.

That reasoning inverts the thing Sigstore exists to do. The signer has the signature timestamped; the verifier checks the timestamp falls inside the certificate's validity window. The client specification states the goal outright: *"we decouple the payload lifetime from the certificate lifetime."* The proof travels in the bundle as a transparency-log inclusion proof and signed checkpoint, or an RFC 3161 timestamp.

The verifier tested it rather than reasoning about it. A package bundle whose leaf certificate was valid for ten minutes on 28 July 2026, carrying no RFC 3161 timestamps and no long-lived key, verified offline **two months after expiry** with all egress forced through a dead proxy. Corrupting one byte of the inclusion proof's root hash made it fail, which confirms the Merkle proof is load-bearing rather than incidental.

What survives is narrower. Inside a trust domain, keyless is right and is configuration rather than code -- the certificate authority has a first-class SPIFFE issuer type with a validated trust-domain field. Across a boundary, keyless still works **provided the bundle carries its own verification material**, which is a bundle-construction requirement rather than a key-management one. A hardware-held long-lived key remains a legitimate choice for accreditation reasons, but don't claim you need one because keyless cannot cross.

This one was marked as blocking, because the wrong version was advice someone could have acted on.

---

## 6. Claims that were weakened rather than broken

**"Don't transform software, verify it"** survives in principle but was naive in detail. The flat *uncompressed* blob store doesn't survive contact, and the design needs an explicit **two-control-point split**: a low-side structural inspector that expands blobs under recursion limits, rejects path escapes, device nodes, setuid bits and capability attributes, and **emits only a verdict -- never modified bytes**. See [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

**"CDR delivers close to zero security benefit for software"** was rhetorical overreach. The defensible version: *no content-disarm engine has a sanitiser for compiled code, so transforming a software bundle changes every digest without touching the threat.* Cite the measured figure instead of the rhetoric: 13% soundness for binary reconstruction (USENIX Security 2024).

**"Three primitives suffice"** -- there are **five**. See [The Five Primitives](../how/primitives.md).

**"Review becomes the bottleneck"** was flagged as unmeasured; it turns out to be supported, with a correction. **Reviewer attention** is the scarce thing, not review itself, and build and test capacity *rise* in importance rather than falling. See [Gates vs Attention](../tradeoffs/gates-vs-attention.md).

**"Policy demands machine-verifiable evidence while implementations fail to deliver it"** -- the strong form does not survive the primaries, and this is the fifth weakened claim. The cATO memo's *"**all** security controls will need to be fed into a system level dashboard view"* became *"**which** security controls"* in the 2024 Evaluation Criteria; those criteria accept *"screen shots of control gate output as displayed in a dashboard"*, so a PNG meets the requirement; *"Automate security control configurations and validation"* is an **Objective**, not a threshold requirement; the memo itself licenses manual controls (*"Manual controls will have different timelines associated"*); and the Implementation Guide describes the method as a shift to *"a periodic assessment"*. **Corrected statement: policy demands continuous evidence and names the pipeline as its source, but specifies no machine-verifiable form — and that gap is where the stale document returns.** Weaker, and still a good argument. (This claim was omitted from an earlier version of this list, which is why the list read "five weakened" over four entries.) See [The Problem](the-problem.md).

---

## What this exercise is worth

Across the eight claims, verification caught four factual errors, one architectural omission and three overclaims, in a position that had already been through the research. The errors weren't careless -- they were confident inferences from real evidence, which is the dangerous kind.

**A claim with nothing checking it drifts.** That applies to this project's own documents exactly as much as to Big Bang's OSCAL file.
