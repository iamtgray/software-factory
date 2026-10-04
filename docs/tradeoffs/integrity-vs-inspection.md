# Integrity vs Inspection

The tension I keep coming back to, and the one I can't see a clean way through.

## The two requirements

**Supply-chain integrity** says: bind evidence to bytes by cryptographic hash. Change one byte and every signature over it fails. That's the entire point -- the brittleness *is* the security property.

**Content inspection at a classified boundary** says: treat complex formats as untrustworthy, and transform them into simple verifiable ones. UK guidance is explicit that complex data types "should be transformed into simple, verifiable data types", and that software-only verification of complex parsers "is usually unachievable... so is not recommended".

These requirements are incompatible. Transformation changes bytes. Changed bytes break signatures.

!!! quote "The tension, documented first-party by a mainstream tool"
    A widely-used container utility refuses to strip platforms from a multi-architecture image unless you also pass a flag removing the signatures, because doing so "**invalidates the manifest list signature and changes the manifest list digest**".

    It surfaces the conflict loudly and makes the operator choose. I think that's the right design choice, and it's the problem in miniature.

## What makes it genuinely hard

A diode and a guard are different devices, and in most of the conversations I've had they get treated as one.

| | Enforces | Touches payload bytes? |
|---|---|---|
| **Diode** | Direction, physically | **No** -- it governs flow direction only |
| **Guard** | Content policy -- inspection, filtering, transformation | **Possibly yes** |

A diode therefore preserves digests. **A guard in front of it may rewrite them** -- and published guidance puts transformation *before* the diode, on the low side, assuming outright that the transformation engine itself may be compromised.

## The ways out I can find, and where most of them break

=== "The guard re-signs after transforming"

    **Wrong, and as I read it the guidance says so.**

    Transformation is placed on the low side precisely because parsing untrusted content is inherently risky, with an explicit assumption that the transformer could be compromised. Design principles describe transformers as *lower assurance components* whose compromise can cause "loss of integrity of data within the flow".

    Giving that component a key the far side trusts converts an *expected* compromise into a total provenance bypass. Your effective trust root becomes the most attackable box in the architecture.

=== "Sign a canonical extract of the meaning"

    Works for documents, and **fails for software**, because a compiled binary's bytes *are* its meaning. I can't come up with a semantic extract of an executable that survives rewriting, and I'd be glad to be shown one.

    One adjacent idea is reusable though -- sign an *index* that commits to content by hash, so the payload inherits the signature transitively. That's what the bundle manifest does.

=== "Apply content-disarm-and-reconstruct to the bundle"

    **What I can defend here is narrow.**

    CDR *can* strip unexpected file types, normalise archive structure and detect polyglot files. So the sweeping version of the argument -- that CDR buys close to zero security here -- is too strong, and I'd expect a hostile reviewer to take it apart.

    Here it is: **I haven't found a content-disarm engine with a sanitiser for compiled code.** If that holds up, transforming a software bundle changes every digest without touching the actual threat. One measurement puts binary reconstruction at **13% soundness** (USENIX Security 2024).

    Because the payload is executable by design, a backdoored binary sails straight through an engine built to protect document viewers from documents.

=== "Make the software verifiable in place"

    **The one that looks workable to me.**

    Make the bundle a type the guard can *verify* as it stands: a flat content-addressed blob store plus one small strictly-schema'd signed manifest. The high-assurance check becomes schema validation plus confirming each blob's name equals its own hash -- a complete integrity check I'd expect to land in a few hundred lines, needing no understanding of OCI, ELF or Helm.

    Guidance explicitly permits this: transformation "may not be needed where the content format is simple enough to be verified directly".

    **Flatness is a property of the top level alone.** The blob store is content-addressed there, and the blobs themselves hold nested archives, which is why the recursion limits belong in the inspector and the hash check stays blind to what a blob contains.

## The design that seems to follow

!!! success "Split inspection from verification, and keep the high-assurance part single-function"
    **Control point 1 -- a low-side structural inspector.** Expands each blob in a scratch area under explicit recursion and expansion limits. Rejects path escapes, device nodes, FIFOs, sockets, setuid and setgid bits, and capability attributes. Multi-scans. **Emits a verdict and that alone; whatever bytes it produced stay in the scratch area and are destroyed there.**

    **Control point 2 -- the high-assurance check.** Schema validation plus per-blob hash equality. Nothing else. No parsing of application formats, no unbounded loops, no semantic understanding.

It holds up, as far as I can see, because it separates the *risky* operation (parsing untrusted content) from the *trusted* one (comparing hashes), and only the second needs to be high assurance. The first can be compromised without the far side losing integrity, because it never produces bytes that cross. That last clause carries most of the weight, and it took me a while to believe it -- it's also the sentence I'd expect an assessor to attack first.

## What you are accepting

I'd expect an assessor to go straight here, so it's worth being explicit.

**Byte-identical pass-through means malicious content in a blob is not neutralised.** You've moved from *"the guard protects the far side from malicious bytes"* to *"the near side's attestations plus far-side runtime controls protect the far side"*.

For executable software I'd argue that was always true. As far as I can tell CDR can't examine this payload meaningfully in the first place, which leaves the evidence chain plus runtime enforcement doing the work.

## The unknown that blocks the format

A format designed against a *guessed* guard specification is worthless. Of the things you'd need to know to stop guessing, six out of seven look to me like they aren't publicly answerable -- the questions, and what each one decides, are set out in [What We Cannot Answer](../limits/unanswerable.md). The relevant requirement sets are controlled, so access to them depends on clearance.

Which leaves the envelope format waiting. The two-control-point *structure* survives not knowing the limits; the specific encoding doesn't. So how much work on the encoding is worth doing before those answers arrive, and who do you have access to who could go and get them?

## And the one the documents don't ask for

Across the DoD reference design and the DevSecOps Fundamentals, these terms occur **zero times**: `reproducible`, `OSCAL`, `admission`, `attestation`, `SLSA`, `in-toto`, `Sigstore`, `cosign`, `provenance`, `notary`, `checksum`, `digest`.

And the sharpest one: **the word "signed" appears zero times in DevSecOps Fundamentals v2.5.** In the reference design it appears twice, both describing a hardened-image registry's output. **Neither document tells anyone to verify a signature** at any stage -- pull, build, admission, deploy. The security model on offer is trust-by-source plus rescan, with two different scanners mandated "because scan results are too disparate".

**SBOM is the exception**, demanded once, in Fundamentals section 3.3.1.2 -- *"cATO includes the need for a Secure Software Supply Chain (SSSC) and requires a Software Bill of Materials (SBOM)."* A single occurrence in 44 pages, absent from both the acronym list and the glossary, with no format, depth, timing, consumer or consequence specified. Demanded, but barely.

Signing, attestation and reproducible builds are still worth doing. The case has to rest on merit, because these documents give you nothing to point at -- and when budgets tighten, my experience is that the things nobody asked for go first. So whose budget carries them, and what happens to the evidence chain if the answer turns out to be nobody's?
