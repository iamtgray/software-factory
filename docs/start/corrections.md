# What We Got Wrong

Eight load-bearing claims were put through adversarial verification: three independent agents per claim, each instructed to *refute* it rather than confirm it, working from primary sources.

**Result: two refuted, five weakened, none survived intact.**

This page is the most useful on the site. Every correction below makes the position narrower and harder to knock down in front of someone who knows the field.

---

## 1. "No open-source project is a software factory" -- false

**Konflux-CI's own README** describes it as *"a cloud-native software factory"* that brings together *"best-in-class open source projects"*. Apache-2.0, self-hostable on any conformant Kubernetes.

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

## 5. Claims that were weakened rather than broken

**"Don't transform software, verify it"** survives in principle but was naive in detail. The flat *uncompressed* blob store doesn't survive contact, and the design needs an explicit **two-control-point split**: a low-side structural inspector that expands blobs under recursion limits, rejects path escapes, device nodes, setuid bits and capability attributes, and **emits only a verdict -- never modified bytes**. See [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

**"CDR delivers close to zero security benefit for software"** was rhetorical overreach. The defensible version: *no content-disarm engine has a sanitiser for compiled code, so transforming a software bundle changes every digest without touching the threat.* Cite the measured figure instead of the rhetoric: 13% soundness for binary reconstruction (USENIX Security 2024).

**"Three primitives suffice"** -- there are **five**. See [The Five Primitives](../how/primitives.md).

**"Review becomes the bottleneck"** was flagged as unmeasured; it turns out to be supported, with a correction. **Reviewer attention** is the scarce thing, not review itself, and build and test capacity *rise* in importance rather than falling. See [Gates vs Attention](../tradeoffs/gates-vs-attention.md).

---

## What this exercise is worth

Verification caught four factual errors, one architectural omission and two overclaims, in a position that had already been through six research streams. The errors weren't careless -- they were confident inferences from real evidence, which is the dangerous kind.

**A claim with nothing checking it drifts.** That applies to this project's own documents exactly as much as to Big Bang's OSCAL file.
