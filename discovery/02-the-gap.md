# The gap, restated precisely

Verified 2026-10-03 by direct inspection of source, not from a summary.

## Two clauses of the original premise don't survive contact

The premise in `00-premise.md` claimed no open-source project "integrates best-of-breed components into one coherent, deployable software factory, including SBOM production". Both halves are falsifiable in about ninety seconds:

- **Konflux-CI** (Apache-2.0, self-hostable on any conformant Kubernetes) describes itself as bringing together best-in-class open source projects into a single integrated software factory, and calls itself a cloud-native software factory in its strapline. The phrase is already taken.
- **SBOM production is commodity.** Konflux attaches them, Zarf generates them by default via Syft, Iron Bank emits four formats. Nobody will pay attention to a project whose pitch is that it makes SBOMs.

Stop claiming either. They make the whole thesis look unresearched, and the real gap is narrower and much more defensible.

## What is actually missing

> **CORRECTED 2026-10-04 — the claim that stood here, "the evidence does not cross the boundary with the artefact", was REFUTED by adversarial verification. See `00-index.md` 0.1 and 0.1a.** Evidence does cross, today, by default. Hauler carries cosign signatures, attestations, SBOMs *and* the OCI 1.1 referrers graph (`--exclude-extras` defaults to false) in a standard zstd-compressed OCI layout, and reconstructs the tags on the far side. `zarf package verify` performs full offline verification against a Sigstore trusted root **embedded in the binary**, with `--insecure-ignore-tlog` defaulting true "for air-gap" and RFC 3161 timestamps. The test set below — a high side independently establishing what it was given with zero network access — **is met today by an existing command.** Transport is solved and has been for a while.

**What is actually missing is a receiver that is obliged to look**, plus three narrower things:

1. **No fail-closed receiver-side gate.** Hauler's disconnected-side `load` has one flag and no verification; its `--ignore-errors` demotes a verification failure to a warning "including storing images that failed verification"; `zarf package deploy --verify` defaults to `if-possible`.
2. **No shipment-level evidence.** Nothing states what a transfer is supposed to contain, who authorised it, or what policy was in force, so omission and rollback are undetectable by construction.
3. **Upstream provenance does not cross.** Zarf regenerates SBOMs locally, so the packager's assertion substitutes for the builder's.
4. **The guard-mediated case is untouched** by any open-source project.

**And do not invent a bespoke transfer format for the sneakernet case.** A standard OCI layout already crosses and is read by five tools; a new format would be a one-implementation artefact needing its own accreditation, and the first question anyone asks is "why not OCI layout?"

## The evidence

`repo1.dso.mil/ironbank-tools/ironbank-pipeline` is publicly clonable with no CAC. Its stage 6, `pipeline1/6-post-publish/upload_to_cds.py`, is about 110 lines. In full, what it does:

1. `cosign verify` against the image — key-based (`use_key=True`), not keyless. Skipped entirely unless running on repo1, i.e. no verification in staging.
2. `skopeo copy docker://$REGISTRY/$IMAGE:$TAG oci:$ARTIFACT_DIR:$TAG` — into an OCI layout.
3. `tar -czvf tmp.tar.gz -C $ARTIFACT_DIR .`
4. `s3upload.upload_file(...)` to `containers/$IMAGE:$TAG.tar.gz` in `$CDS_SOURCE_BUCKET`.

That is the entire cross-domain story of the most mature hardened-container programme in defence.

Note what happens to the signature: it is **verified on the low side and then discarded**. What crosses the boundary is a gzipped OCI layout with no detached signature, no checksum file, no manifest, no SBOM, no scan results and no attestations — despite the same pipeline having just produced every one of those artefacts and uploaded them to a *different* S3 bucket for the web front end to display.

There is also no receiver-side counterpart anywhere in the repo, no chunking, and no handling of guard size limits.

And the repo has **no licence file anywhere**. Publicly readable, legally unusable. Source-available, not open source — so it is evidence, never a thing to copy.

> **The uniqueness quantifier that used to sit on this dissection is deleted, not downgraded to "appears to be" (`00-index.md` 0.2).** `hairgap`, `eurydice` and ANSSI's `lidi` are all one-way transfer implementations in open code, and they were found in minutes once someone ran a proper search. **Standing rule: no document in this project may assert a universal negative over open code.** The description above stands on its own as a dissection of the most mature hardened-container programme in defence; it never needed to be the only one.

## Why this is the right thing to attack

It reframes the project from "another platform" to one specific, hard, unglamorous problem: **a fail-closed receiver-side verification obligation over a signed shipment manifest** — not a transfer format. The format already exists and is a standard OCI layout. What does not exist is anything that refuses rather than warns, and anything that states what a shipment was supposed to contain so that omission and rollback become detectable.

That problem is:
- unoccupied in open source, as far as a proper search shows — stated as a search result, not as a universal negative
- the thing accreditors actually care about
- small enough to build
- useless to solve halfway, which is why nobody has

## The dependency that worries me

This applies to the **guard-mediated** case only — the sneakernet case is served by a standard OCI layout and needs no new format. The guard-mediated envelope is worthless if it guesses wrong about what real cross-domain guards accept and reject — filetypes, archive formats, whether content is rewritten in transit, size and throughput limits. That information is largely not in public code. Until we have it, the format is speculative.

Unresolved tension to carry forward: content-disarm-and-reconstruct guards *rewrite* files to sanitise them, which breaks every digest and signature they touch. An envelope that assumes byte-identical passage may be assuming the one thing the guard will not do.
