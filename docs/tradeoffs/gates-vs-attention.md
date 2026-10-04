# Gates vs Attention

Attention is the factory's scarcest resource. The supply doesn't go up when you add checks, and every gate you add takes a bit more of it.

## The inverse relationship

Strictness and survival pull against each other. "Fail the build on any high or critical finding" produces hundreds of findings on day one, and in the write-ups I've found, the gate is disabled or blanket-waived inside a quarter.

There's peer-reviewed evidence for how this plays out (FSE 2025):

- suppressions grow **monotonically** -- they only ever accumulate
- **50.8% suppress nothing at all** -- dead weight, added defensively
- dead suppressions **silently mask future findings**, so the gate degrades invisibly
- the top cause is **false positives**

!!! warning "A gate that exhausts its reviewers is worth less than no gate"
    A gate people have learned to click past provides false assurance *and* consumes attention. An absent gate is at least honest about the risk. Given the choice I'd take the honest one.

## Where the false positives come from

Roughly in order of volume, going on impressions as much as counts:

**Identifier matching.** Vendor-product identifiers are a curated vocabulary with no deterministic construction rule, so generators guess. Guess loosely and open-ended version ranges flood you; guess wrong and you get a false negative you probably never hear about. **65% of open-source CVEs lack a severity score** in the national database, and independent severity assessments agree with it only **55.7%** of the time.

**Base-image inheritance.** Operating-system findings the application team can't fix and the base owner has already triaged.

**Unreachable code.** The library is present; the vulnerable function is never called. I haven't found a scanner that can work this out on its own.

**Scanner disagreement.** Two mainstream scanners draw on different advisory sources with different matching logic. They won't always agree, and often neither of them is wrong.

## What seems to work, roughly in order of effect

### 1. Remove findings at source

Most of the volume I've looked at comes from the base image. A minimal, continuously rebuilt base **removes** findings outright, and every finding it removes is a judgement nobody has to record.

Probably the highest-leverage thing on this list, and thoroughly unglamorous. The way to keep a gate switched on is to give it less to complain about.

### 2. Make recording a judgement cheap

!!! success "Already solved, and it contains no AI"
    An existing tool turns a maintainer typing one structured comment into a **Sigstore-signed in-toto VEX attestation**, authorised against a code-owners file. (It's at v0.0.1 with one maintainer, so I'd lift the design into our own implementation and keep the dependency out of the tree -- see [Build vs Adopt](build-vs-adopt.md).)

    Thirty seconds of human effort, producing a durable verifiable statement that travels with the artefact.

The economics decide this one. The gate survives if recording "the vulnerable code is not present" takes ten minutes and yields a signed artefact; make it cost a ticket and a security review and somebody will switch the gate off.

And a model shouldn't make this call -- the best measured performance on selecting the correct VEX justification is **under 70% macro-F1**. A wrongly signed justification is durable, verifiable, trusted and false.

### 3. Point AI at the work a deterministic check can confirm

**LLM triage of static-analysis false positives** is the strongest result I've found in this area: F1 of 0.91-0.96, with one reported deployment eliminating 94-98% of false positives at under $0.12 per alarm against 10-20 minutes of human time.

That works because the output is checkable. AI code review *as a gate* has a much weaker record: 31,073 comments in the wild, a **56.3% rejection rate and 36.4% acceptance**, and no signed verdict for a policy engine to consume. I don't know whether that rejection rate is a property of the job or of the prompting, and I haven't found anyone who has separated the two. Until somebody does, I'd put it in the comment thread, where a human reads each suggestion and acts on the ones worth acting on.

### 4. Waivers that expire by construction

Every real gate needs break-glass. The implementations I'd call good make exclusions carry `effectiveOn` and `effectiveUntil` dates, a link to a tracking issue, and warnings before expiry.

That should turn the monotonic-growth problem into a self-pruning one, assuming somebody acts on the warnings. I haven't found it measured either way.

### 5. Start in audit mode

Report-only for a quarter. Drive the count to zero. *Then* enforce. Most of the mature tools have an explicit audit level for this.

## The reframing I keep coming back to

One measured finding I haven't seen in a vendor maturity model:

!!! quote "DORA 2025"
    **Clear, actionable feedback on task outcomes** is *the* platform attribute most correlated with positive user experience.

Feedback quality is what carries the correlation, ahead of capability and breadth. That surprised me -- I would have put breadth first.

A red cross and a 4,000-line SARIF file is a failure, even when the finding is correct. The gate's job is to **tell a human exactly what to do in as few words as possible**. Spend the engineering effort on that sentence.

## Why this is getting more acute

Generation keeps getting cheaper. Review still costs a human the hour it has always cost, and I can't see anything in the generation stack that buys that hour back.

The scarce resource is **reviewer attention**. The unit I've ended up using is human-attention-units per merged change, and measuring it that way *raises* the importance of build, test and CI capacity, because mechanical verification is how you spend less attention per change.

!!! tip "What the factory is actually for"
    **The factory's highest-value output is the evidence that makes a change cheap to review.**

    A passing test suite that genuinely covers the diff. A reachability verdict. A statement that this change touches nothing else. An explanation of a finding in one sentence.

    Everything that reduces attention-per-change is worth more than another check that increases it.

## And one trade-off inside the trade-off

Rich policy belongs at the gate, where every attestation is to hand and failure is cheap and early. **Cheap policy belongs at admission**, where a one-second budget and an unbypassable position mean it must verify a signature and a verdict and nothing else.

Getting this backwards (evaluating "did this build prefetch hermetically" inside a mutating webhook against attestations fetched over the network) is how you take a cluster down. The delegated verdict exists so that the expensive reasoning happens once, somewhere it can afford to.

Which leaves the questions I'd want answered before anyone switches a gate to enforcing:

- after a quarter in audit mode, is zero findings actually reachable, or only nearly?
- who signs a "the vulnerable code is not present" judgement, and how many minutes does it cost them?
- what's the attention budget per merged change today, and what's being spent on it?

The third is where I'm least confident. I don't have a way to measure attention-per-change that doesn't come down to asking reviewers how a review felt, which may well be the weakest join in the whole argument above.
