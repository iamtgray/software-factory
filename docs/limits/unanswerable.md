# What cannot be known

The information behind these questions is either controlled or was never measured, and more effort from this side won't produce it. Which of the two you're holding decides what you do next -- controlled means a different conversation with different people, not more research.

## The one that blocks design

**What will a real cross-domain guard actually accept?**

Designing a transfer format needs answers to all seven of these; only one has a public answer:

| Question | Why it decides the design |
|---|---|
| Maximum single-file size | Decides whether chunking is mandatory |
| Maximum object count per transfer | Decides whether a flat blob store is viable at all |
| **Does a tar of content-addressed files count as a "simple, verifiable type", or as an archive requiring recursive expansion?** | One reading passes through; the other triggers the transformation that breaks every signature. The payload *is* nested (container layers), so "nothing to recurse into" isn't available as an answer. |
| Is per-blob compression permitted? | Decides the size budget |
| Will a guard accept a hash-only validation policy where it expects semantic inspection? | Decides whether the two-control-point design is acceptable at all |
| Sustained throughput and transfer-window cadence | Decides whether delta transfer is optional or essential |
| Is *any* acknowledgement in the return direction permissible? | Decides whether the feedback loop exists |

The relevant requirement sets, baseline lists and assessment methodologies are **controlled**, and access takes a clearance and a need to know. Vendor sites give marketing figures; published guidance gives principles, not numbers.

!!! danger "The envelope format can't be settled until someone cleared answers these"
    The two-control-point *structure* survives without the limits; the specific encoding doesn't.

## The ones that aren't published

**How software actually gets into classified cloud regions.** The regions exist and their accreditations are published; the ingest mechanism isn't described anywhere reachable.

**Whether frontier model APIs exist in classified regions.** There's no public enumeration of service availability for those regions. Public announcements describe models built for national-security customers without stating availability for a specific region and model.

!!! note "Self-hosted inference"
    Where a managed frontier model does exist on the high side, it's region-specific, model-specific, quota-constrained and slower to receive new models. Custom model import is unavailable in connected government deployments, so the inference slot has to work self-hosted either way.

**Alliance-level information exchange gateway specifications.** Not published openly.

## The ones nobody has measured

**Does any software factory improve delivery outcomes?** Four separate audit findings record the absence, and **nobody has published delivery or outcome metrics for a named software factory**. One survey carries measured data -- self-reported culture, 36 practitioners across 19 organisations. Every delivery figure in it cites an earlier publication as its source. The correlation between maturity score and delivery speed is described as something that could "potentially correlate" and was never run. One of its four factory categories had **no participants**.

DoD says the same about itself. Its **Software Modernization Implementation Plan** still lists *"Establish software factory criteria and metrics"* and *"Collect cost data on agile software programs"* as *Carryover* items.

On continuous authorisation, from *The State of DevSecOps*: *"Organizations don't have to provide metrics for cATO effectiveness, but we are interested in potential metrics to evaluate the effectiveness of the cATO process from a DoD governance perspective."*

A metrics framework exists (published October 2024) with no published value against it anywhere I can find. The word DORA appears zero times in 47 pages of DoD's own state-of-practice report.

**What is the real pre-factory baseline for authorisation timelines?** There's no agreed figure. One source says six months to two years; another says 18 to 24 months; neither cites anything. "Six months" circulates as a de facto baseline, converging independently across several vendors, with no origin I could trace.

**Does agent-generated volume actually overwhelm review in practice?** Reviewer attention becoming the binding constraint is supported. What isn't measured is whether the loop self-limits, with reviewers rejecting low-quality change until throughput plateaus.

What to do with that absence is a positioning decision -- [Mandate vs Adoption](../tradeoffs/mandate-vs-adoption.md).

Every item above carries a confidence marker -- blocked, weak negative, or unverified -- and the marker decides whether you may say it to a customer. [What You Can Quote](../reference/status.md) has the full list.

The decisions this leaves open:

1. Who you know who's cleared enough to settle the guard limits
2. Whether the measurement gap is a reason to wait, or a reason to go and measure it yourselves
