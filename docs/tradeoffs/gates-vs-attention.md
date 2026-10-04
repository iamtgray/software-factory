# Gates vs Attention

Every gate consumes reviewer attention. Attention is the factory's scarcest resource, and it doesn't scale with the number of checks you add.

## The inverse relationship

Strictness and survival pull against each other. "Fail the build on any high or critical finding" produces hundreds of findings on day one, and within a quarter the gate is either disabled or blanket-waived.

There is peer-reviewed evidence for how this plays out (FSE 2025):

- suppressions grow **monotonically** -- they only ever accumulate
- **50.8% suppress nothing at all** -- they are dead weight, added defensively
- dead suppressions **silently mask future findings**, so the gate degrades invisibly
- the top cause is **false positives**

!!! warning "A gate that exhausts its reviewers is worth less than no gate"
    No gate at all is honest about the risk. A gate everyone has learned to click past provides false assurance *and* consumes attention. That's strictly worse.

## Where the false positives come from

Four sources, in rough order of volume:

**Identifier matching.** Vendor-product identifiers are a curated vocabulary with no deterministic construction rule, so generators guess. Guess loosely and open-ended version ranges flood you; guess wrong and you get a false negative you'll never see. **65% of open-source CVEs lack a severity score** in the national database, and independent severity assessments agree with it only **55.7%** of the time.

**Base-image inheritance.** Operating-system findings the application team cannot fix and the base owner has already triaged.

**Unreachable code.** The library is present; the vulnerable function is never called. No scanner can determine this on its own.

**Scanner disagreement.** Two mainstream scanners draw on different advisory sources with different matching logic. They won't agree, and neither is wrong.

## What actually works, in order of effect

### 1. Remove findings rather than suppressing them

Most volume comes from the base image. A minimal, continuously rebuilt base **removes** findings instead of requiring a judgement on each one.

It's the highest-leverage intervention available and it's thoroughly unglamorous: the way to keep a gate switched on is to give it less to complain about.

### 2. Make recording a judgement cost thirty seconds

!!! success "Already solved, and it contains no AI"
    An existing tool turns a maintainer typing one structured comment into a **Sigstore-signed in-toto VEX attestation**, authorised against a code-owners file.

    Thirty seconds of human effort, producing a durable verifiable statement that travels with the artefact.

The economics decide everything here. If recording "the vulnerable code is not present" takes ten minutes and yields a signed artefact, the gate survives. If it takes a ticket and a security review, the gate gets disabled.

And a model should *not* make this call -- the best measured performance on selecting the correct VEX justification is **under 70% macro-F1**. Signing the wrong justification is worse than signing none.

### 3. Use AI where it has a deterministic check, not where it has judgement

The strongest real result in this area, and it's genuinely good: **LLM triage of static-analysis false positives** achieves F1 of 0.91-0.96, with one reported deployment eliminating 94-98% of false positives at under $0.12 per alarm against 10-20 minutes of human time.

That works because the output is checkable. Compare AI code review *as a gate*: 31,073 comments in the wild, a **56.3% rejection rate and 36.4% acceptance**, and nothing emitting a signed verdict. It's advice, not a gate.

### 4. Waivers that expire by construction

Every real gate needs break-glass. The good implementations make exclusions carry `effectiveOn` and `effectiveUntil` dates, a link to a tracking issue, and warnings before expiry.

That turns the monotonic-growth problem into a self-pruning one. **Steal this design** -- it's the difference between a waiver list and a graveyard.

### 5. Start in audit mode

Report-only for a quarter. Drive the count to zero. *Then* enforce. The mature tools have an explicit audit level for exactly this.

## The reframing that matters

One measured finding is nearly absent from every vendor maturity model:

!!! quote "DORA 2025"
    **Clear, actionable feedback on task outcomes** is *the* platform attribute most correlated with positive user experience.

Not capability. Not breadth. Feedback quality.

Which points at something concrete: a red cross and a 4,000-line SARIF file is a failure, even when the finding is correct. The gate's job isn't to detect. It's to **tell a human exactly what to do in as few words as possible**.

## Why this is getting more acute

Generation is getting cheaper. Review is not.

So the scarce resource isn't review capacity in the abstract -- it's **reviewer attention**, measured in human-attention-units per merged change. And one correction follows from that: build, test and CI capacity *rise* in importance rather than falling, because mechanical verification is how you spend less attention per change.

!!! tip "The design instruction"
    **The highest-value output of the factory isn't the artefact. It's the evidence that makes a change cheap to review.**

    A passing test suite that genuinely covers the diff. A reachability verdict. A statement that this change touches nothing else. An explanation of a finding in one sentence.

    Everything that reduces attention-per-change is worth more than another check that increases it.

## And one trade-off inside the trade-off

Rich policy belongs at the gate, where every attestation is to hand and failure is cheap and early. **Cheap policy belongs at admission**, where a one-second budget and an unbypassable position mean it must verify a signature and a verdict and nothing else.

Getting this backwards (evaluating "did this build prefetch hermetically" inside a mutating webhook against attestations fetched over the network) is how you take a cluster down. The delegated verdict exists precisely so that the expensive reasoning happens once, somewhere it can afford to.
