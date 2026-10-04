# Secure Software Factory

What a software factory actually is, what the evidence says it can deliver, and where the trade-offs are.

This site is the readable version of a research programme that read the primary sources instead of the marketing. Where the research proved the original premise **wrong**, the corrections are here too -- the central thesis was one of them.

---

??? question "I'm new to this -- where do I start?"

    In order:

    1. **[The Problem](start/the-problem.md)** -- what a software factory is for, and the gap worth attacking
    2. **[What We Got Wrong](start/corrections.md)** -- four confident claims the evidence demolished. Read this before repeating anything from the first page.
    3. **[Scope -- What This Is Not](start/scope.md)** -- three layers: a platform, a product line, and one that is out of bounds
    4. **[A Worked Example](example/connected.md)** -- one bug fix traced from ticket to running container, showing what gets signed at each step

    Then [Trade-offs](tradeoffs/index.md).

??? question "I'm an architect and I want the mechanism"

    Start with [The Five Primitives](how/primitives.md) -- a digest-bound statement, a delegated verdict, a capability descriptor, trust configuration, and freshness state. Fix those five and the tool choices become close to arbitrary, which is what [Slots and Outcomes](how/slots.md) then exploits: a component position is defined by the outcome it owes, and the contract for it lives in a Kubernetes custom resource.

    [The Hand-offs](how/handoffs.md) is where the primitives get spent. Five transitions where the receiver cannot verify what the sender did by inspection and has to rely on a signature; everything else is plumbing.

    Then the same change twice -- [end to end](example/connected.md), and [air-gapped](example/airgap.md).

??? question "I'm deciding whether to fund or buy one of these"

    The uncomfortable material first.

    | What someone will ask you | Where it's answered |
    |---|---|
    | Does a platform actually make delivery faster? | [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md) -- the measured numbers, including the ones that say platforms *reduce* throughput |
    | Has this been tried before? | [What Has Failed Before](limits/history.md) -- four times since 1968, and the diagnoses are consistent |
    | What can't you tell me? | [What We Cannot Answer](limits/unanswerable.md) -- what is genuinely unknowable from public sources |
    | What happens when a dependency dies? | [Ecosystem Health](limits/ecosystem.md) -- twelve projects under 300 stars sit on the critical path |

??? question "I care about the air-gapped / cross-domain case"

    The distinction the field muddles: an air gap is the absence of a network path, and cross-domain means a guard sits in the path and may refuse or rewrite what crosses. Sneakernet is largely solved. The guard case is not, because changed bytes break every signature over them.

    - [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md) -- sanitising content destroys the signatures that prove it is trustworthy, and no published standard reconciles the two
    - [The Same Change, Air-Gapped](example/airgap.md) -- what survives the crossing, what does not, and the three places the connected flow assumed a network
    - [What We Cannot Answer](limits/unanswerable.md) -- six of seven questions about real guard behaviour are not publicly answerable

---

## The one-paragraph version

A software factory is a set of components that turn source code into a deployable artefact **together with machine-verifiable evidence about how it was made**. The artefact was never the hard part. The evidence is. Producing it is commodity now; making it *current*, *bound to the thing it describes*, and *actually read by something* is not. Every documented failure here is a failure of evidence, not of build automation: evidence that drifted from reality, evidence that was discarded at a boundary, evidence whose validator was switched off because it kept failing.

## Three things worth knowing before anything else

**The term is contested and has failed before.** "Software factory" was rejected at the 1968 NATO conference, trademarked and abandoned by a US defence contractor in 1978, pursued in Japan for two decades without ever being statistically validated, and revived by Microsoft in 2003. The civilian world has since settled on *platform engineering* instead. See [What Has Failed Before](limits/history.md).

**Most of what you need already exists.** Signed SBOMs, build provenance, policy gates, offline verification, air-gapped bundling -- all solved, by several projects, under permissive licences. The genuinely empty slots number eight, and half of those collapse into one work item; [Build vs Adopt](tradeoffs/build-vs-adopt.md) covers which ones, and which features sit behind a paid licence.

**The measured evidence is not flattering.** Internal developer platforms correlate with **−8% throughput and −14% change stability**, and *mandating* one costs a further 6% of throughput. A factory that doesn't plan for this is planning to be cancelled during it. The numbers, and what to do about them, are in [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md).

## Key concepts

Software factory
:   A set of components that produce a deployable artefact plus machine-verifiable evidence of its provenance. In US defence usage specifically, one that has adopted an approved DevSecOps reference design. The civilian equivalent term is *internal developer platform*.

Attestation
:   A small signed document that makes a claim about an artefact, bound to it by cryptographic digest. The universal currency of a factory. See [The Five Primitives](how/primitives.md).

Delegated verdict
:   An accountable party performs an expensive verification once and signs a cheap assertion that everything downstream trusts instead of repeating the work. The same pattern covers the policy gate, the cross-domain importer and the human reviewer.

Slot
:   A component position defined by the **outcome it must produce** -- a signed SBOM, a reviewed diff, a scanned artefact -- and not by the tool that fills it. Lets one architecture serve a hyperscale cloud and a disconnected enclave. See [Slots and Outcomes](how/slots.md).

Air-gap
:   An environment with no network path to the outside. Distinct from **cross-domain**, where a guard or diode mediates transfer and may *refuse or rewrite* what crosses. Conflating the two causes most of the confusion in this field.

Guard
:   A device enforcing content policy at a security boundary, which may transform data to sanitise it. Transformation changes bytes, and changed bytes break every signature over them. This is the central tension of the whole design. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

cATO
:   Continuous Authorization to Operate. Real US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. **It modifies how you keep an authorisation; it is not a route to getting one.** Effectively nobody holds one.

!!! note "On confidence"
    Every claim on this site carries a provenance status -- verified against a primary source, reported by research, or explicitly unverified. The research ran **without a working search engine**, which makes positive findings unusually strong (they came from reading specs and source) and every negative finding weak. See [Evidence Status](reference/status.md).
