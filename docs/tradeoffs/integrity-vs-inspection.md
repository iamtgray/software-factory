# Integrity vs Inspection

The central unsolved tension.

## The two requirements

**Supply-chain integrity** says: bind evidence to bytes by cryptographic hash. Change one byte and every signature over it fails. That's the entire point -- the brittleness *is* the security property.

**Content inspection at a classified boundary** says: don't trust complex formats. Transform them into simple verifiable ones. UK guidance is explicit that complex data types "should be transformed into simple, verifiable data types", and that software-only verification of complex parsers "is usually unachievable... so is not recommended".

These requirements are incompatible. Transformation changes bytes. Changed bytes break signatures.

!!! quote "The tension, documented first-party by a mainstream tool"
    A widely-used container utility refuses to strip platforms from a multi-architecture image unless you also pass a flag removing the signatures, because doing so "**invalidates the manifest list signature and changes the manifest list digest**".

    It fails loudly rather than silently re-signing. That's the correct design choice, and it's the problem in miniature.

## What makes it genuinely hard

A diode and a guard are different devices and people conflate them constantly.

| | Enforces | Touches payload bytes? |
|---|---|---|
| **Diode** | Direction, physically | **No** -- its property is flow, not content |
| **Guard** | Content policy -- inspection, filtering, transformation | **Possibly yes** |

So a diode preserves digests. **A guard in front of it may not.** And published guidance puts transformation *before* the diode, on the low side, assuming outright that the transformation engine itself may be compromised.

## Four candidate resolutions, and why three of them fail

=== "The guard re-signs after transforming"

    **Wrong, and the guidance effectively says so.**

    Transformation is placed on the low side precisely because parsing untrusted content is inherently risky, with an explicit assumption that the transformer could be compromised. Design principles describe transformers as *lower assurance components* whose compromise can cause "loss of integrity of data within the flow".

    Giving that component a key the far side trusts converts an *expected* compromise into a total provenance bypass. Your effective trust root becomes the most attackable box in the architecture.

=== "Sign a canonical extract rather than the bytes"

    Works for documents. **Doesn't work for software**, because a compiled binary's bytes *are* its meaning. There is no semantic extract of an executable that survives rewriting.

    One adjacent idea is reusable though -- sign an *index* that commits to content by hash, so the payload inherits the signature transitively. That's what the bundle manifest does.

=== "Apply content-disarm-and-reconstruct to the bundle"

    **The strongest argument against this isn't the loud one.**

    The overclaim to avoid: "CDR delivers close to zero security benefit." That's rhetoric and a hostile reviewer will dismantle it -- CDR *can* strip unexpected file types, normalise archive structure and detect polyglot files.

    The defensible version: **no content-disarm engine has a sanitiser for compiled code.** So transforming a software bundle changes every digest without touching the actual threat. Cite the measured figure rather than the rhetorical one -- binary reconstruction achieves **13% soundness** (USENIX Security 2024).

    CDR protects document viewers from documents. It cannot protect a cluster from a backdoored binary, because the payload is executable by design.

=== "Don't transform software -- verify it"

    **The workable answer, with a correction.**

    Make the bundle a type the guard can *verify* rather than one it wants to *rewrite*: a flat content-addressed blob store plus one small strictly-schema'd signed manifest. The high-assurance check becomes schema validation plus confirming each blob's name equals its own hash -- a complete integrity check implementable in a few hundred lines, needing no understanding of OCI, ELF or Helm.

    Guidance explicitly permits this: transformation "may not be needed where the content format is simple enough to be verified directly".

    **The correction from verification:** the original formulation of this was naive. "Flat and uncompressed with no nesting to recurse into" doesn't survive contact -- the payload *is* nested, and claiming otherwise invites an easy rebuttal.

## The design that actually follows: two control points

!!! success "Split inspection from verification, and keep the high-assurance part single-function"
    **Control point 1 -- a low-side structural inspector.** Expands each blob in a scratch area under explicit recursion and expansion limits. Rejects path escapes, device nodes, FIFOs, sockets, setuid and setgid bits, and capability attributes. Multi-scans. **Emits only a verdict -- never modified bytes.**

    **Control point 2 -- the high-assurance check.** Schema validation plus per-blob hash equality. Nothing else. No parsing of application formats, no unbounded loops, no semantic understanding.

It works because it separates the *risky* operation (parsing untrusted content) from the *trusted* one (comparing hashes), and only the second needs to be high assurance. The first can be compromised without the far side losing integrity, because it never produces bytes that cross.

## What you are accepting

Be explicit about this, because an assessor will ask.

**Byte-identical pass-through means malicious content in a blob is not neutralised.** You've moved from *"the guard protects the far side from malicious bytes"* to *"the near side's attestations plus far-side runtime controls protect the far side"*.

For executable software that was always the truth. Don't argue that CDR is worthless. Argue that **it was never going to examine this payload meaningfully**, and that the control doing the work is the evidence chain plus runtime enforcement.

## The unknown that blocks the format

A format designed against a *guessed* guard specification is worthless, and six of the seven things you'd need to know aren't publicly answerable -- the questions, and what each one decides, are set out in [What We Cannot Answer](../limits/unanswerable.md). The relevant requirement sets are controlled rather than merely hard to find.

So stop designing the envelope format until someone cleared answers them. It's a conversation, not a research task, and the two-control-point *structure* survives not knowing the limits. The specific encoding doesn't.

## And the one nobody asks for

Across the DoD reference design and the DevSecOps Fundamentals, these terms occur **zero times**: `reproducible`, `OSCAL`, `admission`, `attestation`, `SLSA`, `in-toto`, `Sigstore`, `cosign`, `provenance`, `notary`, `checksum`, `digest`.

And the sharpest one: **the word "signed" appears zero times in DevSecOps Fundamentals v2.5.** In the reference design it appears twice, both describing a hardened-image registry's output. **Nobody is ever told to verify a signature** -- not at pull, not at build, not at admission, not at deploy. The security model is trust-by-source plus rescan, with two different scanners mandated "because scan results are too disparate".

**SBOM is the exception**, demanded once, in Fundamentals section 3.3.1.2 -- *"cATO includes the need for a Secure Software Supply Chain (SSSC) and requires a Software Bill of Materials (SBOM)."* A single occurrence in 44 pages, absent from both the acronym list and the glossary, with no format, depth, timing, consumer or consequence specified. Demanded, but barely.

That's not an argument against doing them. It's an argument for justifying them on merit rather than waving them through as compliance requirements -- because when budgets tighten, the things nobody asked for go first.
