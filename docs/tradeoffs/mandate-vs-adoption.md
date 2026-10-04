# Mandate vs Adoption

The measured evidence says platforms can make delivery worse, and that mandating one makes it worse still.

## The numbers

From DORA's 2024 research, with the caveats stated below:

| Measure | Effect of internal developer platform use |
|---|---|
| Individual productivity | **+8%** |
| Team performance | **+10%** |
| Organisational performance | **+6%** |
| **Throughput** | **−8%** |
| **Change stability** | **−14%** |

The report's own words: *"change failure rate and rate of rework are significantly increased when a platform is being used."*

Three further findings:

- Mandated exclusive use costs **a further 6% of throughput**.
- Platform use combined with instability **predicts burnout**.
- The lever that helps is **developer independence, +5%**.

!!! quote "DORA's own prescription"
    "A platform should provide methods for users... to **break out** of the tools and automations provided in the platform."

### The caveats

Correlational, not causal. 89% of respondents reported using a platform, so the comparison group is small. The definition of "platform" is broad. DORA itself raises reverse causation (struggling organisations may adopt platforms). And platform engineering follows a **J-curve**: gains, then a dip, then recovery.

None of that makes the numbers ignorable. It makes them a prediction to plan against.

A mandated, air-gapped platform sits in the worst cell of that table. Mandated exclusive use, no escape hatch, nothing external to build thinly on top of -- so the mitigations below aren't optional extras. They're the measured difference between a platform that helps and one that harms.

## Why the usual remedy is unavailable

The consensus advice is "platform as a product" -- a named product manager, self-service, treat your developers as customers, earn adoption. Six independent sources agree on it, including a survey and a research programme. It's as settled as anything in this field.

It has four steps, and **step three breaks** in a mandated environment: *earn adoption through competition.* There is no exit, no internal market, and the mandate is a legal constraint rather than a choice. One of the originators of the framing is explicit that "a little competition is a necessary ingredient".

A second piece of consensus advice also breaks. "Build the thinnest viable platform over externally provided managed services" assumes those services exist. Air-gapped, they don't -- so the platform team carries considerably more load than the guidance assumes. That's a staffing and funding argument, and it needs making early rather than in year two, when the team is underwater and the deployment path has become something nobody can explain.

## The inversion that rescues it

In a classified environment, shadow IT is a security incident rather than a productivity loss. DORA's "ivory tower leads to shadow IT workarounds" pitfall stops being an efficiency concern and becomes a **security risk** -- which makes developer experience a **security control**.

It is the mechanism in the best-documented failure anywhere in this research -- a national audit office finding, with cause and effect in a single audited sentence:

> The organisation had *"a culture focused on the approvals process rather than outcomes"*, which *"incentivised [CIOs] to maintain or produce their own separate capabilities... rather than rely on shared ones."*

## Substitutes for the missing market pressure

If you can't have competition, you need something that does competition's job:

**Preserve choice within the paved road.** Enabling constraints, not a golden cage. The platform is the default, not the boundary.

**A genuinely fast, non-punitive exception route.** If going around the platform requires an apology, people will do it quietly instead, which is the worst outcome.

**Independent satisfaction measurement, published alongside compliance metrics.** So that *"100% adoption, 30% satisfaction"* reads as failure rather than success. Without this, a mandate makes the adoption number meaningless as a signal.

**Publish the platform team's own delivery metrics.** Accountability in both directions.

**Harvest capabilities from application teams.** The highest maturity level in the consensus model is "participatory", and that's achievable without a market.

## The metric to actually run the programme on

A mandated factory is stuck at adoption level 2 of 4 for ever, because the model's higher levels assume voluntary uptake. So restate the question counterfactually -- **would** teams choose it? -- and measure the thing that answers it:

**Track the workaround rate as the programme's headline health metric.** It's the air-gapped equivalent of churn, it's measurable, and it's the only number a mandate can't game.

A second metric, from the reuse evidence: **track the modification rate of shared assets.** Reuse [only pays above 80% unchanged](../limits/history.md), so a slot every programme forks by 40% is worse than having no shared asset at all.

## And the funding model, which is where this usually dies

The documented failure mode is specific, recurring, and nearly fifty years old: the first organisation to trademark "The Software Factory" was starved of demand because nobody above it was required to use the thing ([the 1978 account](../limits/history.md)). It was not the first to build one -- the Japanese factories predate it by six years -- but it is the one whose failure was written up.

RAND finds that modern defence software factories are mostly **customer-funded** -- which writes that exact failure into the budget line. A factory that must win each customer's budget is a factory whose work flow can decline.

!!! danger "Fund it as a product, or buy it. Don't fund it as a project with customer-recovered costs."
    That's the same mistake with a 2026 date on it.

## Nobody has measured any of this properly

The absence is [catalogued under what we cannot answer](../limits/unanswerable.md) -- no controlled study, no baseline, no peer-reviewed evaluation of any named factory. One audit found only **6 of 36** programmes self-reporting agile methods delivered software to users in under three months. A metrics framework does exist -- published in October 2024, combining the four DORA measures with value and cyber-resilience measures including average time to achieve authorisation. **Nobody has published any values against it.**

Which is the opening. Position the work around the absence of measurement rather than around claimed benefit: everyone else is claiming; nobody is measuring. Shipping per-tenant outcome measurement, baselined *before* adoption, is cheap, and it would make this the first factory anywhere able to answer "did it work".
