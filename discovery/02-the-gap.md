# The gap, restated precisely

Verified 2026-10-03 by direct inspection of source, not from a summary.

## Two clauses of the original premise don't survive contact

The premise in `00-premise.md` claimed no open-source project "integrates best-of-breed components into one coherent, deployable software factory, including SBOM production". Both halves are falsifiable in about ninety seconds:

- **Konflux-CI** (Apache-2.0, self-hostable on any conformant Kubernetes) describes itself as bringing together best-in-class open source projects into a single integrated software factory, and calls itself a cloud-native software factory in its strapline. The phrase is already taken.
- **SBOM production is commodity.** Konflux attaches them, Zarf generates them by default via Syft, Iron Bank emits four formats. Nobody will pay attention to a project whose pitch is that it makes SBOMs.

Stop claiming either. They make the whole thesis look unresearched, and the real gap is narrower and much more defensible.

## What is actually missing

**The evidence does not cross the boundary with the artefact.**

Everything upstream of the diode is solved, by multiple projects, well. The moment an artefact crosses into the high side it arrives as a bare tarball, and the receiving environment has no choice but to take it on trust.

## The evidence

`repo1.dso.mil/ironbank-tools/ironbank-pipeline` is publicly clonable with no CAC. Its stage 6, `pipeline1/6-post-publish/upload_to_cds.py`, is about 110 lines and appears to be the only cross-domain packaging implementation in open code anywhere. In full, what it does:

1. `cosign verify` against the image — key-based (`use_key=True`), not keyless. Skipped entirely unless running on repo1, i.e. no verification in staging.
2. `skopeo copy docker://$REGISTRY/$IMAGE:$TAG oci:$ARTIFACT_DIR:$TAG` — into an OCI layout.
3. `tar -czvf tmp.tar.gz -C $ARTIFACT_DIR .`
4. `s3upload.upload_file(...)` to `containers/$IMAGE:$TAG.tar.gz` in `$CDS_SOURCE_BUCKET`.

That is the entire cross-domain story of the most mature hardened-container programme in defence.

Note what happens to the signature: it is **verified on the low side and then discarded**. What crosses the boundary is a gzipped OCI layout with no detached signature, no checksum file, no manifest, no SBOM, no scan results and no attestations — despite the same pipeline having just produced every one of those artefacts and uploaded them to a *different* S3 bucket for the web front end to display.

There is also no receiver-side counterpart anywhere in the repo, no chunking, and no handling of guard size limits.

And the repo has **no licence file anywhere**. Publicly readable, legally unusable. Source-available, not open source — so it is evidence, never a thing to copy.

## Why this is the right thing to attack

It reframes the project from "another platform" to one specific, hard, unglamorous problem: a transfer envelope and its receiver-side verification path, such that a high-side environment can independently establish what it has been given with zero network access and no ability to ask the low side anything.

That problem is:
- genuinely unsolved in open source
- the thing accreditors actually care about
- small enough to build
- useless to solve halfway, which is why nobody has

## The dependency that worries me

The envelope design is worthless if it guesses wrong about what real cross-domain guards accept and reject — filetypes, archive formats, whether content is rewritten in transit, size and throughput limits. That information is largely not in public code. Until we have it, the format is speculative.

Unresolved tension to carry forward: content-disarm-and-reconstruct guards *rewrite* files to sanitise them, which breaks every digest and signature they touch. An envelope that assumes byte-identical passage may be assuming the one thing the guard will not do.
