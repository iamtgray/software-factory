# Mandate vs adoption

On the measured evidence, platforms can make delivery worse, and mandating one looks like it makes it worse still.

## The numbers

From DORA's 2024 research:

| Measure | Effect of internal developer platform use |
|---|---|
| Individual productivity | **+8%** |
| Team performance | **+10%** |
| Organisational performance | **+6%** |
| **Throughput** | **−8%** |
| **Change stability** | **−14%** |

The report's own words: *"change failure rate and rate of rework are significantly increased when a platform is being used."*

More from the same report:

- Mandated exclusive use costs **a further 6% of throughput**.
- Platform use combined with instability **predicts burnout**.
- The one lever pulling the other way is **developer independence, +5%**.

!!! quote "DORA's own prescription"
    "A platform should provide methods for users... to **break out** of the tools and automations provided in the platform."

### The caveats

These findings are correlations, and the survey design cannot establish which way the causation runs. 89% of respondents reported using a platform, so the comparison group is small. The definition of "platform" is broad. DORA itself raises reverse causation (struggling organisations may adopt platforms). And platform engineering follows a **J-curve**: gains, then a dip, then recovery.

A mandated, air-gapped platform sits in the worst cell of that table -- mandated exclusive use, no escape hatch, nothing external to build thinly on top of.

## Why the usual remedy is unavailable

The consensus advice is "platform as a product": a named product manager, self-service, treat your developers as customers, earn adoption. Six independent sources agree on it, including a survey and a research programme.

The third step breaks in a mandated environment: *earn adoption through competition.* There's no exit, no internal market, and the mandate carries the force of law. One of the originators of the framing is explicit that "a little competition is a necessary ingredient".

Air-gapped, there are no "externally provided managed services" for a "thinnest viable platform" to sit on, so the platform team carries more load than the guidance assumes. That's a staffing and funding argument, and it needs making in year one.

## Developer experience as a security control

In a classified environment, shadow IT counts as a security incident. DORA's "ivory tower leads to shadow IT workarounds" pitfall therefore lands as a **security risk**, which makes developer experience a **security control**. That last step is my inference, though the two pieces it rests on are both documented.

It's also the mechanism in a national audit office finding:

> The organisation had *"a culture focused on the approvals process rather than outcomes"*, which *"incentivised [CIOs] to maintain or produce their own separate capabilities... rather than rely on shared ones."*

## Substitutes for the missing market pressure

If you can't have competition, you need something that does competition's job. None of these is a tested replacement:

**Preserve choice within the paved road.** The platform is the default, and teams keep a supported way to step off it.

**A fast, non-punitive exception route.**

**Independent satisfaction measurement, published alongside compliance metrics.** So that *"100% adoption, 30% satisfaction"* reads as failure.

**Publish the platform team's own delivery metrics.**

**Harvest capabilities from application teams.** The highest maturity level in the consensus model is "participatory", which doesn't need a market.

## Metrics to track

On the consensus model's own terms a mandated factory can't climb past adoption level 2 of 4, because the higher levels assume voluntary uptake. So ask the counterfactual -- **would** teams choose it?

**Track the workaround rate as the programme's headline health metric.** It's the air-gapped equivalent of churn, and hard to game under a mandate.

A second metric, from the reuse evidence: **track the modification rate of shared assets.** Reuse [only pays above 80% unchanged](../limits/history.md), so a slot every programme forks by 40% charges the coordination cost and returns nothing for it.

## The funding model

The failure mode is nearly fifty years old. The first organisation to trademark "The Software Factory" was starved of demand because nobody above it was required to use the thing ([the 1978 account](../limits/history.md)). The Japanese factories predate that trademark by six years.

RAND finds that modern defence software factories are mostly **customer-funded** -- a factory that must win each customer's budget can be starved of demand the same way.

!!! danger "Fund it as a product, or buy it -- never as a project with customer-recovered costs"
    The evidence is one well-documented case and one RAND finding.

## The measurement gap

The absence is [catalogued under what we cannot answer](../limits/unanswerable.md). I could not turn up a controlled study, a baseline, or a peer-reviewed evaluation of any named factory. One audit found only **6 of 36** programmes self-reporting agile methods delivered software to users in under three months. A metrics framework does exist -- published in October 2024, combining the four DORA measures with value and cyber-resilience measures including average time to achieve authorisation. I haven't found a single published value against it.

Per-tenant outcome measurement baselined *before* adoption is cheap next to everything else in the build.

Questions before betting the positioning on it:

1. Can the programme absorb a dip the size of −8% throughput in year one and still keep its funding?
2. Who owns the workaround rate, and is anyone senior willing to see it published?
3. Is the funding model negotiable now, or only after the first cancellation?
