# Secure Software Factory

What a software factory actually is, what the evidence says it can deliver, and where the trade-offs are (the part most material skips).

This site is the readable version of a research programme that read the primary sources rather than the marketing. It includes the places where the research proved the original premise **wrong**, because those turned out to be the most useful findings.

---

??? question "I'm new to this -- where do I start?"

    In order:

    1. **[The Problem](start/the-problem.md)** -- what a software factory is for, and the gap worth attacking
    2. **[What We Got Wrong](start/corrections.md)** -- four confident claims the evidence demolished. Read this before repeating anything from the first page.
    3. **[Scope -- What This Is Not](start/scope.md)** -- the single most important decision, and why it's about scope rather than technology
    4. **[A Worked Example](example/connected.md)** -- one bug fix traced from ticket to running container, showing what gets signed at each step

    Then [Trade-offs](tradeoffs/index.md), which is the part you actually came for.

??? question "I'm an architect and I want the mechanism"

    1. **[The Five Primitives](how/primitives.md)** -- every hand-off in the factory is built from five things. Fix these and the tool choices become nearly arbitrary.
    2. **[The Hand-offs](how/handoffs.md)** -- five trust-domain transitions. Everything else is plumbing.
    3. **[Slots and Outcomes](how/slots.md)** -- how a component is defined by what it must produce rather than what it is
    4. **[A Change, End to End](example/connected.md)** and then **[The Same Change, Air-Gapped](example/airgap.md)**

??? question "I'm deciding whether to fund or buy one of these"

    Start with the uncomfortable material:

    1. **[Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md)** -- the measured numbers, including the ones that say platforms *reduce* throughput
    2. **[What Has Failed Before](limits/history.md)** -- the idea has failed four times since 1968, and the diagnoses are consistent
    3. **[What We Cannot Answer](limits/unanswerable.md)** -- what is genuinely unknowable from public sources
    4. **[Ecosystem Health](limits/ecosystem.md)** -- twelve projects under 300 stars sit on the critical path

??? question "I care about the air-gapped / cross-domain case"

    1. **[Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md)** -- the central tension: sanitising content destroys the signatures that prove it is trustworthy
    2. **[The Same Change, Air-Gapped](example/airgap.md)** -- what survives the crossing and what does not
    3. **[What We Cannot Answer](limits/unanswerable.md)** -- six of seven questions about real guard behaviour are not publicly answerable

---

## The one-paragraph version

A software factory is a set of components that turn source code into a deployable artefact **together with machine-verifiable evidence about how it was made**. The artefact was never the hard part. The evidence is. Producing it is commodity now; making it *current*, *bound to the thing it describes*, and *actually read by something* is not. Every documented failure here is a failure of evidence rather than of build automation: evidence that drifted from reality, evidence that was discarded at a boundary, evidence whose validator was switched off because it kept failing.

## Three things worth knowing before anything else

**The term is contested and has failed before.** "Software factory" was rejected at the 1968 NATO conference, trademarked and abandoned by a US defence contractor in 1978, pursued in Japan for two decades without ever being statistically validated, and revived by Microsoft in 2003. The civilian world has since settled on *platform engineering* instead. See [What Has Failed Before](limits/history.md).

**Most of what you need already exists.** Signed SBOMs, build provenance, policy gates, offline verification, air-gapped bundling -- all solved, by several projects, under permissive licences. The genuinely empty slots number about eight, and half of those collapse into one work item. See [Build vs Adopt](tradeoffs/build-vs-adopt.md).

**The measured evidence is not flattering.** Internal developer platforms correlate with **−8% throughput and −14% change stability**, and *mandating* one costs a further 6% of throughput. A factory that doesn't plan for this is planning to be cancelled during it. See [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md).

## Key concepts

Software factory
:   A set of components that produce a deployable artefact plus machine-verifiable evidence of its provenance. In US defence usage specifically, one that has adopted an approved DevSecOps reference design. The civilian equivalent term is *internal developer platform*.

Attestation
:   A small signed document that makes a claim about an artefact, bound to it by cryptographic digest. The universal currency of a factory. See [The Five Primitives](how/primitives.md).

Delegated verdict
:   An accountable party performs an expensive verification once and signs a cheap assertion that everything downstream trusts instead of repeating the work. The same pattern covers the policy gate, the cross-domain importer and the human reviewer.

Slot
:   A component position defined by the **outcome it must produce** -- a signed SBOM, a reviewed diff, a scanned artefact -- rather than by the tool that fills it. Lets one architecture serve a hyperscale cloud and a disconnected enclave. See [Slots and Outcomes](how/slots.md).

Air-gap
:   An environment with no network path to the outside. Distinct from **cross-domain**, where a guard or diode mediates transfer and may *refuse or rewrite* what crosses. Conflating the two causes most of the confusion in this field.

Guard
:   A device enforcing content policy at a security boundary, which may transform data to sanitise it. Transformation changes bytes, and changed bytes break every signature over them. This is the central tension of the whole design. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

cATO
:   Continuous Authorization to Operate. Real US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. **It modifies how you keep an authorisation; it is not a route to getting one.** Effectively nobody holds one.

!!! note "On confidence"
    Every claim on this site carries a provenance status -- verified against a primary source, reported by research, or explicitly unverified. The research ran **without a working search engine**, which makes positive findings unusually strong (they came from reading specs and source) and every negative finding weak. See [Evidence Status](reference/status.md).
