# What the civilian evidence base says — and the first positioning problem

From `research/08-vendors-and-analysts.md`. Recorded 2026-10-03. Everything here is **Primary** (agent read the source) unless marked otherwise; I have not personally re-verified these, unlike the items in `04-regulatory-reset.md`.

## The terminology problem, and it is a real one

**The civilian world does not say "software factory."** Across the CNCF, DORA, Team Topologies and the ThoughtWorks Technology Radar, the settled vocabulary is **platform engineering / internal developer platform / internal developer portal**. Gartner's market category is "DevSecOps Platforms". Where "factory" appears it is either US-DoD lineage or the pejorative "feature factory".

This matters in two concrete ways:

1. **Searching for "software factory" surfaces defence material and vendor copy, not the evidence base.** The entire research programme so far has been looking under the wrong noun for the civilian half.
2. **The metaphors differ substantively.** *Factory* implies throughput and conformance. *Platform* implies adoption and experience. Several of the strongest findings below only make sense inside the platform framing — which suggests the project should be bilingual: say "software factory" to defence, "platform" to everyone else, and be clear with itself that the platform framing is where the evidence lives.

Also worth adopting as vocabulary: **golden path** (CNCF) or **paved road** (DORA, Netflix origin). CNCF usefully defines a golden path as a *bundle* — pipeline plus project template plus documentation, shipped as one unit — which is a more precise idea than the project has been using.

## Is there a dominant maturity model?

Yes, with a caveat worth repeating. The **CNCF Platform Engineering Maturity Model v1** (TAG App Delivery, in-repo at `github.com/cncf/tag-app-delivery`) is the vendor-neutral consensus artefact. But it is *practitioner consensus, not research* — openly derived from "patterns that have become apparent", and it quotes Fowler's criticism of maturity models approvingly. The research-backed material is **DORA**, which deliberately publishes no maturity model at all, offering a capability catalogue and performance clusters instead.

**Use CNCF's five aspects as the skeleton, DORA for anything causal, and invent nothing.**

Two structural findings from the CNCF model are more useful than its ladder:

- **Four of its five dimensions are sociotechnical, not technical** — Investment, Adoption, Operations, Measurement. Only Interfaces is technical. A project that is 100% an engineering effort is addressing one fifth of the model.
- **Level 4 is explicitly declared not to be the goal**, because each level costs more money and time.

### The best-designed model in the corpus is S2C2F, and it hands us an argument

**OpenSSF/Microsoft S2C2F** (`github.com/ossf/s2c2f`): 8 practices × 4 levels, roughly 27 individually testable requirements, each justified by a named real incident — left-pad for ING-2, colors v1.4.1 for ING-3, SaltStack CVE-2020-11651 for the L2 MTTR argument. L1 is defined as *industry parity*; L3 is the compliance bar; L4 is declared uneconomic except on your most critical dependencies.

**The argument to steal:** two of its L3-ish requirements — ING-2 (internal binary repository) and ING-4 (internal source mirror) — are things an air-gapped programme has to build anyway for connectivity reasons, and that most connected enterprises never get round to. **An air-gapped factory starts closer to S2C2F L3 than a typical internet-connected enterprise does.**

That inverts the usual framing where air-gap is purely a tax. Worth leading with in a defence conversation.

## Good-factory criteria, ranked by independence of agreement

Sixteen in the source; these are the ones where commercially unrelated parties agree, which is the strongest signal available. Note that Humanitec co-authored the CNCF model, so Humanitec and CNCF are **not** independent corroboration.

1. **Platform as a product, with a named product manager.** Six independent sources including a survey and a research programme. Settled; treat as given.
2. **Self-service without tickets.** CNCF, Bottcher, DORA, the Radar.
3. **Reduce cognitive load by "shifting down", not "shifting left"** — because shift-left *adds* load to developers. Team Topologies origin, adopted by both CNCF and DORA.
4. **Thinnest viable platform.** Skelton: "could be just a wiki page… don't make it any thicker than necessary."
5. **Automated, low-friction dependency updating with clear ownership.** The strongest security-side finding, agreed by Sonatype and S2C2F — unrelated parties.
6. **Clear, actionable feedback on task outcomes.** One source, but the best-evidenced single claim in the corpus: DORA 2025 found this is *the* platform attribute most correlated with positive user experience. It is nearly absent from every vendor maturity model.

Item 6 is the highest-leverage underexploited finding, and it converges exactly on `design/02` §2: it points at **explainable gate failures** rather than a red cross and a 4,000-line SARIF file. If review throughput is the scarce resource, feedback quality is the lever.

## Bad-factory criteria

DORA's five named pitfalls are the compact list, and all five corroborate elsewhere:

- **"Build it and they will come"** — no adoption strategy.
- **"Ivory tower"** — the platform team as gatekeeper rather than enabler, driving teams to shadow IT.
- **"Ticket-ops"** — a vending machine with a human behind it.
- **"Big bang"** release.
- **"One-size-fits-all"** — the golden path becomes a golden cage.

Plus: ThoughtWorks put **"layered platform teams" on Hold**, and warn in an Adopt entry that "we strongly caution against just renaming existing internal teams 'platform teams'". Bottcher names the **"superficial private cloud"** — self-service for a VM, tickets for everything that makes it useful. And CNCF places **mandate at Level 2 of 4** on its Adoption aspect, which is a problem the project has to confront directly (below).

## Hard numbers worth quoting

**DORA 2025** (n≈5,000, *n is `[SECONDARY]`*): 90% of organisations use an IDP; 76% have platform teams. The finding that matters most to us:

> "When platform quality is high, the effect of AI adoption on organizational performance becomes strong and positive… when platform quality is low, the effect is negligible."

That is direct empirical support for the central argument in `design/02` — that AI capability is gated by the quality of the platform it sits in, not the other way round. DORA also publishes honest negatives: platforms "can sometimes lead to a decrease in throughput and change stability if not carefully managed", and platform engineering follows a **J-curve** — gains, a dip, then recovery. Budget for the dip and say so in advance, because a programme that does not predict its own J-curve gets cancelled in it.

**Sonatype 2026** (registry telemetry, freely readable in full) — three numbers the project should use:

- **~95% of vulnerable component downloads had a fix already available.** Their conclusion: "the problem is not awareness. It is workflow inertia and unclear ownership." This reframes the vulnerability slot entirely: the factory's job is not *finding* the problem.
- **65% of OSS CVEs lack an NVD CVSS score**, and NVD versus independent severity buckets agree only **55.7%** of the time. Corroborates `research/03`'s finding that CPE-against-NVD matching is the thing that makes gates unusable.
- And the one I think is the most important single data point in the whole corpus: of **36,870** real upgrade recommendations, **27.76% referenced non-existent versions.** Hallucination was 1.69% at HIGH model confidence, but HIGH occurred in only 3.68% of cases.

That last figure is empirical support for `design/02` §3. An agent asked to propose an upgrade without grounded data invents versions more than a quarter of the time. **Give it the actual resolved dependency graph and the problem largely disappears** — which is precisely the "evidence graph as agent context substrate" claim, arrived at from telemetry rather than from reasoning.

**Thoughtworks:** tasks requiring another team were **10–12× slower in elapsed time** (hundreds of tasks, one Australian telco, method unpublished).

**Gartner is `[SECONDARY]` only** — gartner.com 403s and the Internet Archive was down throughout, so there is no primary analyst material in this corpus at all. Via community summary, one forecast is worth tracking: by 2027, **40% of companies will downgrade or disable autonomous AI agents due to governance gaps found only after production incidents**, root-caused to "binary treatment of agent governance". If that is even directionally right, the graded capability descriptor in `design/02` is addressing a real and imminent failure mode rather than a theoretical one.

## The problem the project has to confront: platform-as-a-product does not fully transfer

The platform-as-a-product argument has four steps, and in a mandated, air-gapped environment **step three breaks**: you cannot earn adoption through competition, because there is no exit, no internal market, and the mandate is a legal constraint. Bottcher is explicit that "a little competition is a necessary ingredient". Also broken: CNCF's advice to build the thinnest platform over externally-provided managed services — those are unavailable air-gapped, so the platform team carries more load than CNCF assumes. **The remaining remedy is staffing, which is a funding argument to make early rather than discover late.**

**The inversion to lead with:** in a classified environment, **shadow IT is a security incident, not merely a productivity loss.** DORA's "ivory tower → shadow IT workarounds" pitfall therefore becomes a *security* risk, which makes developer experience a security control rather than a nicety. That is the strongest available argument for taking the civilian platform findings seriously in a defence programme.

Candidate substitutes for the missing market pressure:

- Preserve choice *within* the paved road — enabling constraints, not a golden cage.
- A genuinely fast, non-punitive exception route.
- Independent satisfaction measurement reported alongside compliance metrics, so "100% adoption, 30% satisfaction" reads as failure rather than success.
- Publish the platform team's own delivery metrics.
- Harvest capabilities from application teams — CNCF's Adoption L4 "Participatory", which is achievable without a market.

And on scoring: a mandated factory is **stuck at CNCF Adoption Level 2 for ever**, so restate L3 counterfactually — *would* teams choose it? — and **treat the workaround rate as the programme's headline health metric.** It is the air-gapped equivalent of churn, and it is measurable.

## One find worth tracking

**CNCF TAG App Delivery has an air-gapped working group.** The README is a ~500-byte stub so there is no content yet, but the civilian cloud-native community has now formally recognised air-gapped delivery as its own problem domain. That is both a validation of the project's premise and a place it could contribute rather than compete.
