# What Cannot Be Known

Some questions are hard. These are different -- the information is controlled or unmeasured, and no amount of effort from this side will produce it.

Knowing which is which decides what you do next, because the response to "hard" is more work and the response to "controlled" is a different conversation with different people.

## The one that blocks design

**What will a real cross-domain guard actually accept?**

Six of seven things you'd need to design a transfer format aren't publicly answerable:

| Question | Why it decides the design |
|---|---|
| Maximum single-file size | Decides whether chunking is mandatory |
| Maximum object count per transfer | Decides whether a flat blob store is viable at all |
| **Does an uncompressed tar of content-addressed files count as a "simple, verifiable type", or as an archive requiring recursive expansion?** | **This single answer determines the whole format.** One reading passes through; the other triggers the transformation that breaks every signature. |
| Is per-blob compression permitted? | Decides the size budget |
| Will a guard accept a hash-only validation policy in lieu of semantic inspection? | Decides whether the two-control-point design is acceptable at all |
| Sustained throughput and transfer-window cadence | Decides whether delta transfer is optional or essential |
| Is *any* acknowledgement in the return direction permissible? | Decides whether the feedback loop exists |

The relevant requirement sets, baseline lists and assessment methodologies are **controlled rather than merely obscure**. Vendor sites give marketing figures. Published guidance gives principles, not limits.

!!! danger "Stop designing the envelope format until someone cleared answers these"
    It's a conversation, not a research task.

    The two-control-point *structure* survives not knowing the limits; the specific encoding doesn't.

## The ones that are simply not published

**How software actually gets into classified cloud regions.** The regions exist, their accreditations are published, and the ingest mechanism is described nowhere reachable.

**Whether frontier model APIs exist in classified regions.** Service availability for those regions isn't publicly enumerable. There are public announcements about models built for national-security customers, but you can't look up availability for a specific region and model.

!!! tip "The design consequence, which doesn't depend on the answer"
    **Do not architect on the assumption that a managed frontier model exists on the high side.** Even where one does, it's region-specific, model-specific, quota-constrained and slower to receive new models.

    The self-hosted implementation of the inference slot is therefore **load-bearing, not a fallback**. And it earns its keep immediately even in a connected government deployment, because custom model import is unavailable there -- so the air-gap implementation is *also* the fine-tuning implementation.

**Alliance-level information exchange gateway specifications.** Not openly published.

## The ones that are not measured, by anyone

Different category. These are knowable in principle; nobody has done the work.

**Does any software factory improve delivery outcomes?** Four separate audit findings record the absence, and the precise version is: **nobody has published delivery or outcome metrics for a named software factory.** There is measured data -- a self-reported cultural survey of 36 practitioners across 19 organisations -- but every delivery figure in it is cited to earlier publications rather than measured, the correlation between maturity score and delivery speed is described as something that could "potentially correlate" and was never run, and one of its four factory categories had **no participants at all**.

DoD says the same thing about itself more bluntly than any auditor does. Its own modernisation plan carries, as **Carryover** items: *"Establish software factory criteria and metrics"*, *"Collect cost data on agile software programs"*, and *"Publish SBOM Implementation Guidance for DoD"*. And on continuous authorisation: *"Organizations don't have to provide metrics for cATO effectiveness, but we are interested in potential metrics to evaluate the effectiveness of the cATO process."* **Effectiveness is unmeasured by design, not by oversight.**

A metrics framework exists (published October 2024) and **nobody has published any values against it.** The word DORA appears zero times in 47 pages of DoD's own state-of-practice report.

**What is the real pre-factory baseline for authorisation timelines?** There's no agreed figure. One source says six months to two years; another says 18 to 24 months; neither cites anything. "Six months" circulates as a de facto baseline, converging independently across several vendors, with no documented origin.

**Does agent-generated volume actually overwhelm review in practice?** The claim that reviewer attention becomes the binding constraint is now supported, but whether the loop self-limits (reviewers rejecting low-quality change, so throughput plateaus rather than flooding) is unmeasured.

What to do with that absence is a positioning decision rather than a research task, and it sits on [Mandate vs Adoption](../tradeoffs/mandate-vs-adoption.md).

Every item above carries a confidence marker -- blocked, weak negative, or unverified -- and the marker decides whether you may say it to a customer. [What You Can Quote](../reference/status.md) holds the full catalogue.
