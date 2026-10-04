# Mandate vs Adoption

On the measured evidence, platforms can make delivery worse, and mandating one looks like it makes it worse still. The evidence is thinner than I'd like, and the caveats underneath it do real damage.

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

More from the same report:

- Mandated exclusive use costs **a further 6% of throughput**.
- Platform use combined with instability **predicts burnout**.
- The one lever I can see pulling the other way is **developer independence, +5%**.

!!! quote "DORA's own prescription"
    "A platform should provide methods for users... to **break out** of the tools and automations provided in the platform."

### The caveats

These findings are correlations, and the survey design cannot establish which way the causation runs. 89% of respondents reported using a platform, so the comparison group is small. The definition of "platform" is broad. DORA itself raises reverse causation (struggling organisations may adopt platforms). And platform engineering follows a **J-curve**: gains, then a dip, then recovery.

I read the numbers as a prediction to plan against, which may be more weight than a correlational survey can honestly carry.

A mandated, air-gapped platform sits in the worst cell of that table -- mandated exclusive use, no escape hatch, nothing external to build thinly on top of. So the mitigations below are carrying most of the weight here, and I can't tell you how much of the gap they actually close.

## Why the usual remedy is unavailable

The consensus advice is "platform as a product" -- a named product manager, self-service, treat your developers as customers, earn adoption. Six independent sources agree on it, including a survey and a research programme. It's about as settled as anything I've found in this field.

The third step breaks in a mandated environment: *earn adoption through competition.* There is no exit, no internal market, and the mandate carries the force of law. One of the originators of the framing is explicit that "a little competition is a necessary ingredient".

Another piece of the consensus advice breaks too. Air-gapped, there are no "externally provided managed services" for a "thinnest viable platform" to sit on, so the platform team carries more load than the guidance assumes (I haven't seen anyone put a figure on how much more). The argument is about staffing and funding, and it needs making in year one. Leave it and I'd expect year two to look like the familiar thing -- a team underwater, and a deployment path nobody can explain.

## The inversion that rescues it

In a classified environment, shadow IT counts as a security incident. DORA's "ivory tower leads to shadow IT workarounds" pitfall therefore lands as a **security risk**, which makes developer experience a **security control**. That last step is my inference, though the two pieces it rests on are both documented.

It's also the mechanism in the best-documented failure I've found -- a national audit office finding, with cause and effect in a single audited sentence:

> The organisation had *"a culture focused on the approvals process rather than outcomes"*, which *"incentivised [CIOs] to maintain or produce their own separate capabilities... rather than rely on shared ones."*

## Substitutes for the missing market pressure

If you can't have competition, you need something that does competition's job. None of these is a tested replacement as far as I know, and I'd welcome being told which of them has actually been tried:

**Preserve choice within the paved road.** Build enabling constraints. The platform is the default, and teams keep a supported way to step off it.

**A genuinely fast, non-punitive exception route.** If going around the platform requires an apology, people will do it quietly.

**Independent satisfaction measurement, published alongside compliance metrics.** So that *"100% adoption, 30% satisfaction"* reads as failure. Under a mandate I don't think the adoption number on its own tells you anything.

**Publish the platform team's own delivery metrics.** Accountability in both directions.

**Harvest capabilities from application teams.** The highest maturity level in the consensus model is "participatory", and that one looks reachable without a market.

## The metric to actually run the programme on

On the consensus model's own terms a mandated factory can't climb past adoption level 2 of 4, because the higher levels assume voluntary uptake. So ask the counterfactual -- **would** teams choose it? -- and measure the thing that answers it:

**Track the workaround rate as the programme's headline health metric.** It's the air-gapped equivalent of churn, it's measurable, and it's the one number I can't see a mandate gaming. Someone more motivated than me probably can.

A second metric, from the reuse evidence: **track the modification rate of shared assets.** Reuse [only pays above 80% unchanged](../limits/history.md), so a slot every programme forks by 40% charges the coordination cost and returns nothing for it.

## And the funding model, which is where I think this usually dies

The failure mode is nearly fifty years old. The first organisation to trademark "The Software Factory" was starved of demand because nobody above it was required to use the thing ([the 1978 account](../limits/history.md)). The Japanese factories predate that trademark by six years, and the trademarked factory is the one whose failure was written up.

RAND finds that modern defence software factories are mostly **customer-funded** -- which looks to me like that same failure written into the budget line. A factory that must win each customer's budget is a factory whose work flow can decline.

!!! danger "Fund it as a product, or buy it. Never fund it as a project with customer-recovered costs."
    That's the same mistake with a 2026 date on it. I'm reading one well-documented case and one RAND finding, so treat it as a warning I've grown confident about on thin evidence.

## I can't find anyone who's measured this properly

The absence is [catalogued under what we cannot answer](../limits/unanswerable.md). I could not turn up a controlled study, a baseline, or a peer-reviewed evaluation of any named factory. One audit found only **6 of 36** programmes self-reporting agile methods delivered software to users in under three months. A metrics framework does exist -- published in October 2024, combining the four DORA measures with value and cyber-resilience measures including average time to achieve authorisation. I haven't found a single published value against it.

Which looks like the opening to me. Most of the field seems to be running on claims, and per-tenant outcome measurement baselined *before* adoption is cheap next to everything else in the build. I haven't found another factory that can answer "did it work" at all, which isn't the same as there not being one.

So the questions I'd want answered before betting the positioning on it:

1. Can the programme absorb a dip the size of −8% throughput in year one and still keep its funding?
2. Who owns the workaround rate, and is anyone senior willing to see it published?
3. Is the funding model negotiable now, or only after the first cancellation?
