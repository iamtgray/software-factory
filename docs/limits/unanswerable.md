# What Cannot Be Known

Some questions give way if you work at them for long enough. The ones on this page haven't given way for me, because the information behind them is either controlled or was never measured, and I don't think more effort from this side gets you there.

Knowing which kind you're holding decides what you do next -- the answer to "hard" is more work, and the answer to "controlled" is a different conversation with different people.

## The one that blocks design

**What will a real cross-domain guard actually accept?**

Designing a transfer format needs answers to all of these, and I could find a public answer for only one of them:

| Question | Why it decides the design |
|---|---|
| Maximum single-file size | Decides whether chunking is mandatory |
| Maximum object count per transfer | Decides whether a flat blob store is viable at all |
| **Does a tar of content-addressed files count as a "simple, verifiable type", or as an archive requiring recursive expansion?** | **I think this one answer decides the whole format.** One reading passes through; the other triggers the transformation that breaks every signature. The payload *is* nested -- it is container layers -- so "nothing to recurse into" isn't available as an answer. |
| Is per-blob compression permitted? | Decides the size budget |
| Will a guard accept a hash-only validation policy where it expects semantic inspection? | Decides whether the two-control-point design is acceptable at all |
| Sustained throughput and transfer-window cadence | Decides whether delta transfer is optional or essential |
| Is *any* acknowledgement in the return direction permissible? | Decides whether the feedback loop exists |

The relevant requirement sets, baseline lists and assessment methodologies are **controlled**. Reaching them takes a clearance and a need to know, so I don't think searching harder gets anywhere. The vendor sites I've been through give marketing figures, and the published guidance I've read stays at the level of principle, naming no numbers.

!!! danger "The envelope format can't be settled until someone cleared answers these"
    As far as I can see, the only route to the answers is a conversation with a cleared authority.

    The specific encoding seems to depend on those limits entirely, though the two-control-point *structure* survives without them.

## The ones I can't find published

**How software actually gets into classified cloud regions.** The regions exist and their accreditations are published; I haven't found the ingest mechanism described anywhere reachable.

**Whether frontier model APIs exist in classified regions.** I can't find a public enumeration of service availability for those regions. Public announcements describe models built for national-security customers, and I haven't seen availability stated publicly for a specific region and model.

!!! tip "The design consequence holds whichever way the answer falls"
    **I wouldn't architect on the assumption that a managed frontier model exists on the high side.** Even where one does, it's region-specific, model-specific, quota-constrained and slower to receive new models.

    The self-hosted implementation of the inference slot is therefore **load-bearing**. And it earns its keep immediately even in a connected government deployment, because custom model import is unavailable there -- so the air-gap implementation is *also* the fine-tuning implementation.

**Alliance-level information exchange gateway specifications.** I haven't found these published openly.

## The ones nobody seems to have measured

A different category. These look knowable in principle, and I can't find anyone who has done the work.

**Does any software factory improve delivery outcomes?** Four separate audit findings record the absence, and as far as I can tell **nobody has published delivery or outcome metrics for a named software factory**. One survey carries measured data -- self-reported culture, 36 practitioners across 19 organisations. Every delivery figure in it cites an earlier publication as its source. The correlation between maturity score and delivery speed is described as something that could "potentially correlate" and was never run. And one of its four factory categories had **no participants at all**.

DoD says the same thing about itself, more bluntly than the auditors I've read. Its **Software Modernization Implementation Plan** carries, as *Carryover* items, *"Establish software factory criteria and metrics"* and *"Collect cost data on agile software programs"* -- so there are no agreed criteria and no cost data, by the department's own accounting.

And on continuous authorisation, from *The State of DevSecOps*: *"Organizations don't have to provide metrics for cATO effectiveness, but we are interested in potential metrics to evaluate the effectiveness of the cATO process from a DoD governance perspective."* Reading that, effectiveness looks unmeasured by design -- the framework asks nobody for the number.

A metrics framework exists (published October 2024) and I haven't found a single published value against it. The word DORA appears zero times in 47 pages of DoD's own state-of-practice report.

**What is the real pre-factory baseline for authorisation timelines?** I can't find an agreed figure. One source says six months to two years; another says 18 to 24 months; neither cites anything. "Six months" circulates as a de facto baseline, converging independently across several vendors, with no origin I could trace.

**Does agent-generated volume actually overwhelm review in practice?** I'm fairly confident reviewer attention is what runs out first, though the argument for it is only a line long -- generation keeps getting cheaper and a review still costs a human the hour it always cost. What I can't find measured is whether the loop self-limits, with reviewers rejecting low-quality change until throughput plateaus. That's the part of this page I'm least sure of.

What to do with that absence is a positioning decision, and it sits on [Mandate vs Adoption](../tradeoffs/mandate-vs-adoption.md).

Every item above carries a confidence marker -- blocked, weak negative, or unverified -- and the marker decides whether you may say it to a customer. [What You Can Quote](../reference/status.md) holds the full catalogue.

Before anyone commits to an envelope format: can the design survive with the guard limits still unknown, and who do you know who's cleared enough to settle them? And on the measurement gap -- is that a reason to wait, or a reason to go and measure it yourselves?
