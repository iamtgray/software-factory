# Secure Software Factory

What a software factory actually is, what the evidence says it can deliver, and where I think the trade-offs land.

Everything here comes off the primary sources: specifications, source code, commit histories and published measurements. Where a thing is confirmed, I say so flatly. Where I'm reading between the lines, or working from an absence of evidence, I've tried to say that in the sentence itself.

---

??? question "I'm new to this -- where do I start?"

    In order:

    1. **[The Problem](start/the-problem.md)** -- what a software factory is for, and where I think the gap worth attacking is
    2. **[Scope](start/scope.md)** -- a platform, a product line, and one layer that stays out of bounds
    3. **[What Good Looks Like](how/what-good-looks-like.md)** -- the standards I'd hold a real factory against, and what a verdict needs to stand up
    4. **[A Worked Example](example/connected.md)** -- one bug fix traced from ticket to running container, and what gets signed at each step

    Then [Trade-offs](tradeoffs/index.md), which is where you decide whether any of it is worth having.

??? question "I'm an architect and I want the mechanism"

    Start with [The Five Primitives](how/primitives.md) -- a digest-bound statement, a delegated verdict, a capability descriptor, trust configuration, and freshness state. Fix those five and the tool choices start to look arbitrary, which is the bet [Slots and Outcomes](how/slots.md) runs on: a component position is defined by the outcome it owes, and the contract for it lives in a Kubernetes custom resource.

    [The Hand-offs](how/handoffs.md) is where the primitives get spent -- the transitions where the receiver has nothing to act on but a signature, because the sender's work leaves no other trace. Everything else is plumbing.

    Then the same change twice -- [end to end](example/connected.md), and [air-gapped](example/airgap.md).

??? question "I'm deciding whether to fund or buy one of these"

    The uncomfortable material first.

    | What someone will ask you | Where it's answered |
    |---|---|
    | Does a platform actually make delivery faster? | [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md) -- the measured numbers, including the ones that say platforms *reduce* throughput |
    | Has this been tried before? | [What Has Failed Before](limits/history.md) -- four times since 1968, and the diagnoses rhyme more than I was expecting |
    | What can't you tell me? | [What We Cannot Answer](limits/unanswerable.md) -- the questions I couldn't get at from public sources |
    | What happens when a dependency dies? | [Ecosystem Health](limits/ecosystem.md) -- twelve projects under 300 stars carry the stack, nine on the critical path |

??? question "I care about the air-gapped / cross-domain case"

    The distinction I see collapsed most often: an air gap is the absence of a network path, and cross-domain means a guard sits in the path and may refuse or rewrite what crosses. Sneakernet looks largely solved, which leaves the guard case, where rewriting the bytes breaks every signature over them.

    - [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md) -- sanitising content destroys the signatures that prove it is trustworthy, and I haven't found a published standard that reconciles the two
    - [The Same Change, Air-Gapped](example/airgap.md) -- what survives the crossing, what breaks on the way through, and the places where the connected flow had quietly assumed a network
    - [What We Cannot Answer](limits/unanswerable.md) -- six of seven questions about real guard behaviour that I couldn't answer from public sources

---

## The one-paragraph version

A software factory is a set of components that turn source code into a deployable artefact **together with machine-verifiable evidence about how it was made**. A dozen good open-source implementations already compile code and build containers, and producing evidence at all is commodity. The hard part is what happens to the evidence afterwards: keeping it current, binding it to the thing it describes, and getting something downstream to actually read it. None of that looks like standard practice yet. The failures I've looked at are mostly evidence failures -- evidence that drifted from reality, evidence discarded at a boundary, evidence whose validator got switched off because it kept failing.

## Worth knowing before anything else

**The term is contested and has failed before.** "Software factory" was rejected at the 1968 NATO conference, trademarked and abandoned by a US defence contractor in 1978, pursued in Japan for two decades without any study I've found showing it worked, and revived by Microsoft in 2003. Outside defence, the term that seems to have stuck is *platform engineering*. See [What Has Failed Before](limits/history.md).

**Most of what you need already exists.** Signed SBOMs, build provenance, policy gates, offline verification, air-gapped bundling -- all of it has working implementations under permissive licences, which left me with eight slots I couldn't find anything to fill (half of them collapsing into one work item once you look closely). [Build vs Adopt](tradeoffs/build-vs-adopt.md) covers which ones, and which features sit behind a paid licence.

**The measured evidence is unflattering.** Internal developer platforms correlate with **−8% throughput and −14% change stability**, and *mandating* one costs a further 6% of throughput. A factory that doesn't plan for this is planning to be cancelled during it. The numbers are in [Mandate vs Adoption](tradeoffs/mandate-vs-adoption.md), along with the question of whether you can absorb a dip that size and still keep your funding.

## Key concepts

Software factory
:   DoD defines it as *"a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users"* -- a definition which never mentions evidence, or provenance. The civilian equivalent term is *internal developer platform*.

Attestation
:   A small signed document that makes a claim about an artefact, bound to it by cryptographic digest. It's the closest thing a factory has to a common currency. See [The Five Primitives](how/primitives.md).

Delegated verdict
:   An accountable party performs an expensive verification once and signs a cheap assertion that everything downstream can check in its place. The same pattern covers the policy gate, the cross-domain importer and the human reviewer.

Slot
:   A component position defined by the **outcome it must produce** -- a signed SBOM, a reviewed diff, a scanned artefact. Any tool that delivers the outcome can occupy the position, which is what lets one architecture serve both a hyperscale cloud and a disconnected enclave (on paper, at least; I've not seen anyone run the same architecture in both). See [Slots and Outcomes](how/slots.md).

Air-gap
:   An environment with no network path to the outside. **Cross-domain** is the neighbouring case: a guard or diode mediates transfer and may *refuse or rewrite* what crosses. Conflating the two seems to be behind most of the confusion I run into.

Guard
:   A device enforcing content policy at a security boundary, which may transform data to sanitise it. Transformation changes bytes, and changed bytes break every signature over them. I don't have a clean answer to that, and as far as I can tell nobody's published one. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

cATO
:   Continuous Authorization to Operate. Real US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. **It governs how you hold on to an authorisation once you have one; the initial grant comes through the ordinary assessment and authorisation process.** A few pre-2022 programmes still operate one, though I've found no published count of how many.

!!! note "On confidence"
    Every claim on this site carries a provenance status -- verified against a primary source, reported, or explicitly unverified. The positive findings are the solid ones, because they come from reading specifications and source. Negative findings -- *nothing exists for this* -- are weaker by construction, since no amount of public reading proves an absence, and they're marked as such wherever they appear. Treat them as "I didn't find it", because that's all they are. See [What You Can Quote](reference/status.md).
