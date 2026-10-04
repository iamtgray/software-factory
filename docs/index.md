# Secure Software Factory

What a software factory is, what the evidence says it can deliver, and where the trade-offs land.

Everything here comes off primary sources: specifications, source code, commit histories and published measurements.

---

??? question "I'm new to this -- where do I start?"

    In order:

    1. **[The Problem](start/the-problem.md)** -- what a software factory is for, and where the gap worth attacking is
    2. **[Scope](start/scope.md)** -- a platform, a product line, and one layer that stays out of bounds
    3. **[What Good Looks Like](how/what-good-looks-like.md)** -- the standards a real factory gets held against, and what a verdict needs to stand up
    4. **[A Worked Example](example/connected.md)** -- one bug fix traced from ticket to running container, and what gets signed at each step

    Then [Trade-offs](tradeoffs/index.md), where you decide whether any of it is worth having.

??? question "I'm an architect and I want the mechanism"

    Start with [The Five Primitives](how/primitives.md) -- a digest-bound statement, a delegated verdict, a capability descriptor, trust configuration, and freshness state. Then [Slots and Outcomes](how/slots.md), where the contract for a component position lives in a Kubernetes custom resource.

    [The Hand-offs](how/handoffs.md) is where the primitives get spent -- the transitions where the receiver has nothing to act on but a signature, because the sender's work leaves no other trace.

    Then the same change twice -- [end to end](example/connected.md), and [air-gapped](example/airgap.md).

??? question "I'm deciding whether to fund or buy one of these"

    | What someone will ask you | Where it's answered |
    |---|---|
    | Does a platform actually make delivery faster? | [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md) -- the measured numbers, including the ones that say platforms *reduce* throughput |
    | Has this been tried before? | [What Has Failed Before](limits/history.md) -- four times since 1968 |
    | What can't you tell me? | [What We Cannot Answer](limits/unanswerable.md) -- the questions public sources don't answer |
    | What happens when a dependency dies? | [Ecosystem Health](limits/ecosystem.md) -- twelve projects under 300 stars carry the stack, nine on the critical path |

??? question "I care about the air-gapped / cross-domain case"

    Sneakernet looks largely solved, which leaves the guard case, where rewriting the bytes breaks every signature over them.

    - [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md) -- sanitising content destroys the signatures that prove it is trustworthy, and no standard reconciling the two turned up in public sources
    - [The Same Change, Air-Gapped](example/airgap.md) -- what survives the crossing, what breaks on the way through, and the places where the connected flow had quietly assumed a network
    - [What We Cannot Answer](limits/unanswerable.md) -- six of seven questions about real guard behaviour that public sources leave unanswered

---

## The one-paragraph version

A software factory is a set of components that turn source code into a deployable artefact **together with machine-verifiable evidence about how it was made**. A dozen open-source implementations already compile code and build containers, and producing evidence is commodity. The hard part is what happens to the evidence afterwards: keeping it current, binding it to the thing it describes, and getting something downstream to read it -- none of which is standard practice yet. The failures are mostly evidence failures: evidence that drifted from reality, evidence thrown away at a boundary, or a validator switched off because it kept failing.

## Worth knowing first

**The term is contested and has failed before.** "Software factory" was rejected at the 1968 NATO conference, trademarked and abandoned by a US defence contractor in 1978, pursued in Japan for two decades with no published study showing it worked, and revived by Microsoft in 2003. Outside defence, the term that stuck is *platform engineering*. See [What Has Failed Before](limits/history.md).

**Most of what you need already exists.** Signed SBOMs, build provenance, policy gates, offline verification, air-gapped bundling -- all of it has working implementations under permissive licences. That left eight slots with nothing available to fill them (half of those collapse into one work item). [Build vs Adopt](tradeoffs/build-vs-adopt.md) covers which ones, and which features sit behind a paid licence.

Internal developer platforms correlate with **−8% throughput and −14% change stability**, and *mandating* one costs a further 6% of throughput. The numbers are in [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md).

## Key concepts

Software factory
:   DoD defines it as *"a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users"* -- a definition that never mentions evidence or provenance. The civilian equivalent term is *internal developer platform*.

Attestation
:   A small signed document that makes a claim about an artefact, bound to it by cryptographic digest. See [The Five Primitives](how/primitives.md).

Delegated verdict
:   An accountable party performs an expensive verification once and signs a cheap assertion that everything downstream can check in its place. The same pattern covers the policy gate, the cross-domain importer and the human reviewer.

Slot
:   A component position defined by the **outcome it must produce** -- a signed SBOM, a reviewed diff, a scanned artefact. Any tool that delivers the outcome can occupy the position, which is how one architecture is meant to cover both a hyperscale cloud and a disconnected enclave. See [Slots and Outcomes](how/slots.md).

Air-gap
:   An environment with no network path to the outside. **Cross-domain** is the neighbouring case: a guard or diode mediates transfer and may *refuse or rewrite* what crosses.

Guard
:   A device enforcing content policy at a security boundary, which may transform data to sanitise it. Transformation changes bytes, and changed bytes break every signature over them. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

cATO
:   Continuous Authorization to Operate. Real US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. It governs how you hold on to an authorisation once you have one; the initial grant comes through the ordinary assessment and authorisation process. A few pre-2022 programmes still operate one.

!!! note "On confidence"
    Every claim on this site carries a provenance status -- verified against a primary source, reported, or explicitly unverified. Negative findings (*nothing exists for this*) mean only that public reading didn't turn it up, and they're marked as such -- see [What You Can Quote](reference/status.md).
