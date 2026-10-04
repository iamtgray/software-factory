# Gates vs Attention

Attention is the factory's scarcest resource. The supply doesn't go up when you add checks, and every gate you add takes a bit more of it.

## The inverse relationship

"Fail the build on any high or critical finding" produces hundreds of findings on day one, and in the write-ups the gate is disabled or blanket-waived inside a quarter.

Peer-reviewed evidence (FSE 2025):

- suppressions grow **monotonically** -- they only ever accumulate
- **50.8% suppress nothing at all**
- dead suppressions **silently mask future findings**
- the top cause is **false positives**

A gate people have learned to click past provides false assurance *and* consumes attention.

## Where the false positives come from

Roughly in order of volume:

**Identifier matching.** Vendor-product identifiers are a curated vocabulary with no deterministic construction rule, so generators guess. Guess loosely and open-ended version ranges flood you; guess wrong and you get a false negative you probably never hear about. **65% of open-source CVEs lack a severity score** in the national database, and independent severity assessments agree with it only **55.7%** of the time.

**Base-image inheritance.** Operating-system findings the application team can't fix and the base owner has already triaged.

**Unreachable code.** The library is present; the vulnerable function is never called. Scanners don't work this out on their own.

**Scanner disagreement.** Two mainstream scanners draw on different advisory sources with different matching logic, so they won't always agree -- and often neither is wrong.

## What works, in rough order of effect

### 1. Remove findings at source

Most of the volume comes from the base image. A minimal, continuously rebuilt base **removes** findings outright.

### 2. Make recording a judgement cheap

!!! success "Signed VEX from one structured comment"
    An existing tool turns a maintainer typing one structured comment into a **Sigstore-signed in-toto VEX attestation**, authorised against a code-owners file. (It's at v0.0.1 with one maintainer, so I'd lift the design into our own implementation and keep the dependency out of the tree -- see [Build vs Adopt](build-vs-adopt.md).)

    Thirty seconds of human effort.

The gate survives if recording "the vulnerable code is not present" takes ten minutes and yields a signed artefact; make it cost a ticket and a security review and somebody will switch the gate off.

And a model shouldn't make this call -- the best measured performance on selecting the correct VEX justification is **under 70% macro-F1**.

### 3. Point AI at the work a deterministic check can confirm

**LLM triage of static-analysis false positives** is the strongest result in this area: F1 of 0.91-0.96, with one reported deployment eliminating 94-98% of false positives at under $0.12 per alarm against 10-20 minutes of human time.

AI code review *as a gate* has a much weaker record: 31,073 comments in the wild, a **56.3% rejection rate and 36.4% acceptance**, and no signed verdict for a policy engine to consume. I don't know whether that rejection rate is a property of the job or of the prompting, and I haven't found anyone who has separated the two. Until somebody does, it belongs in the comment thread where a human reads each suggestion and acts on the ones worth acting on.

### 4. Waivers that expire by construction

Every real gate needs break-glass. The better implementations make exclusions carry `effectiveOn` and `effectiveUntil` dates, a link to a tracking issue, and warnings before expiry.

That turns monotonic growth into self-pruning, if somebody acts on the warnings. I haven't found it measured either way.

### 5. Start in audit mode

Report-only for a quarter. Drive the count to zero. *Then* enforce. Most of the mature tools have an explicit audit level for this.

## Feedback quality, not breadth

!!! quote "DORA 2025"
    **Clear, actionable feedback on task outcomes** is *the* platform attribute most correlated with positive user experience.

A red cross and a 4,000-line SARIF file is a failure, even when the finding is correct. The gate's job is to **tell a human exactly what to do in as few words as possible**.

## Why this is getting more acute

Generation keeps getting cheaper. Review still costs a human the hour it has always cost. Measuring in human-attention-units per merged change *raises* the importance of build, test and CI capacity, because mechanical verification is how you spend less attention per change.

So the factory's highest-value output is the evidence that makes a change cheap to review: a passing test suite that genuinely covers the diff, a reachability verdict, a statement that this change touches nothing else, an explanation of a finding in one sentence.

## Where policy belongs

Rich policy belongs at the gate, where every attestation is to hand and failure is cheap and early. **Cheap policy belongs at admission**, where a one-second budget and an unbypassable position mean it must verify a signature and a verdict and nothing else.

Getting this backwards (evaluating "did this build prefetch hermetically" inside a mutating webhook against attestations fetched over the network) is how you take a cluster down.

Questions worth answering before anyone switches a gate to enforcing:

- after a quarter in audit mode, is zero findings actually reachable, or only nearly?
- who signs a "the vulnerable code is not present" judgement, and how many minutes does it cost them?
- what's the attention budget per merged change today, and what's being spent on it?
