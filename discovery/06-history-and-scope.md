# The idea has failed four times, and the diagnoses tell us exactly what to scope

From `research/10-institutional-literature.md`. Recorded 2026-10-03. **Primary** throughout unless marked; I have not personally re-verified these.

This is the most decision-changing research in the programme so far, because it converts "what makes a bad software factory" from opinion into four documented post-mortems — and because the fix it implies is a scope decision we can take now.

## Four attempts, not one

| When | What | Outcome |
|---|---|---|
| **1968** | A Honeywell engineer proposes software factories at the NATO conference | **The conference rejects it as unworkable** on three grounds: reusable modules cannot be both general and efficient; machine dependence; no way to catalogue components |
| **1969→** | **Hitachi**, then NEC, Toshiba, Fujitsu 1976–77 | Ran two decades, then faded |
| **1975–78** | **SDC** — a US defence contractor, first to build and trademark "The Software Factory", ~200 programmers centralised in Santa Monica | Abandoned after ~10 projects |
| **1986–93** | **Eureka Software Factory** — publicly funded European platform programme | Forgotten |
| **2003–08** | **Microsoft Software Factories** (Greenfield & Short) — model-driven, DSLs | Faded |

Note the ordering: **Hitachi predates SDC.** The Japanese movement was not a response to American practice.

## The irony to own before someone else raises it

Cusumano states that SDC's model **"was an important influence on the software standards later developed by the U.S. Department of Defense"** — i.e. the DOD-STD-2167 lineage of heavyweight documentation-driven standards. And SEI's director sat on the **2018 Defense Science Board** task force that put "software factory" into modern DoD policy.

So: **the DoD coined the term, built the heavyweight standards regime out of it, and then re-adopted the same word to escape that regime.** Say this first, with amusement, in any defence conversation. It is a much better position than being caught by it.

Also worth knowing: after 1978 the term "became an anathema to both managers and programmers", and no US firm claimed a software factory for roughly twenty years.

## Diagnosis 1 — SDC, and it was not technology

In the order Cusumano gives:

1. **Too much product variety** for a centralised, standardised facility.
2. **Middle management refused to cede delivery control**, and were **"not required by top management to use the Software Factory, leading to a decline in the flow of work."** Demand starvation.
3. Infrastructure imposed **"without adequate analysis or anticipation of the work flow and the reactions of its personnel."**

Two things to extract. First, Cusumano explicitly **downgrades developer resistance to secondary** — the usual "engineers hated it" story is not the finding. Second, and this matters: **schedule and budget accuracy "improved dramatically".** SDC's factory was partly working when it lost a political contest. It was not killed by failing to deliver; it was killed by optional adoption and a management structure that could route around it.

### The strongest positioning argument available to us

The compromise SDC retreated to was to **"maintain the factory procedures and some of the tools, but decentralize the factory workers."**

That *is* modern platform engineering. The surviving half of the 1978 failure is the thing the industry independently reinvented forty years later. So the honest framing is not "this time it will work" but **"the part that survived is the part we are building, and we are deliberately not building the part that died."**

## Diagnosis 2 — Japan faded rather than collapsed

1. The advantage was **never statistically demonstrated.**
2. The enabling conditions were local: captive customers, lifetime employment, high volumes of similar mainframe software.
3. The product mix changed underneath it.

Toshiba Fuchu's own productivity data is the cautionary curve: **+22% in year one, +70% by year five, then +8% across the next four** — because they hit a **practical reuse ceiling of about 50%.**

## What has actually been measured

Thin, and we should say so rather than imply otherwise.

- **Cusumano & Kemerer, *Management Science* 1990, n=40: no statistically significant difference between US and Japanese organisations on productivity, quality *or* reuse.** The headline claim of the entire Japanese factory movement does not survive its own best study. Reused code costs **~64%** of new.
- **Toshiba's reuse step function**, and this is the most prescriptive finding in the corpus: reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.** Not a gradient — a step. **Therefore: measure the modification rate of our shared assets, because a slot implementation that every programme forks by 40% is worse than no shared asset at all.**
- **SEI's Product Line Technical Probe: of 9 adoptions, roughly one third were not succeeding.** The only base rate anyone has published.
- **Rajapakse et al. systematic literature review, 54 studies** — of which **air-gapped rests on 2.**
- **RAND**: a 6,500-person survey, **$2.5bn/yr**, 5% attrition pressure.

## Two new failure modes, both recent and both aimed at us

- **SEI (2026):** organisations "collapsed under the weight of their own tooling… until no one can explain their own deployment path." That is the 24-slot ambition's natural endpoint if the minimal profile is not the primary deliverable.
- **RAND (2025): "limited movement toward implementation of continuous authority to operate"** despite three years of enabling policy. **cATO is aspiration, not achievement.** This is load-bearing: if the project's leverage rests on control inheritance and cATO, and cATO is not actually happening, the leverage is theoretical.

## Does the modern version repeat the failures?

The NATO objections 2 and 3 (machine dependence, no catalogue) are solved. Objection 1 — reusable modules cannot be both general and efficient — is **shifted rather than solved**: the *assurance machinery* (SBOM, provenance, signing, control evidence) genuinely is uniform across applications; *application architecture* is not.

**Avoided:** centralising people. Nobody is proposing 200 programmers in one building.

**At risk of repeating:**
- **Optional adoption.** RAND finds Department of the Air Force software factories are mostly **customer-funded** — which is *SDC's exact failure mode encoded in the funding model.* A factory that must win each customer's budget is a factory whose work flow can decline. This is the single most actionable warning in the research.
- **No workflow analysis** before imposing infrastructure.
- **Developer experience** — secondary in SDC's case but not absent, and the civilian evidence (see `05`) makes it a security control in a classified setting.
- **Product variety**, if scope is drawn too broadly.

**The one genuinely new condition in our favour:** the binding constraint has moved from code production to **evidence production**. That puts the factory on a compliance chokepoint no team can opt out of — which is structurally stronger than SDC's position, because SDC's customers could simply decline. But the dependency is explicit: **if control inheritance and cATO are weak, that leverage vanishes and we are back in SDC's losing position.** And RAND says cATO is weak today.

## The scope decision this forces, and it answers the objection

SEI's product-line framework contains a 28-section "Practice Risks" catalogue (one per practice area), and its scoping risk is aimed squarely at this project: too wide a scope and "the core assets will be strained beyond their ability to accommodate the variability; economies of production will be lost; **and the product line will collapse into an old-style, one-at-a-time product development effort**." Too narrow and it stagnates. Both directions fatal.

The research's recommended resolution, which I think we should adopt:

| Layer | Framing | Discipline |
|---|---|---|
| **Assurance substrate** | **Platform** | Mandatory, minimal, consumed verbatim. No forking. This is where uniformity is real. |
| **Accredited deployment patterns** | **Genuine product line** | Model commonality and variability properly, in the SEI sense. A bounded family. |
| **Application architecture** | **Explicitly out of scope** | **This is where SDC and Microsoft Software Factories both died.** Do not go here. |

That is a defensible answer to the scoping objection rather than a hope that it will not come up. It also tells us what "modular swappable slots" means and does not mean: swappability belongs in the substrate and the patterns, never in how an application is built.

## The product-line framing, assessed

More defensible than "factory" for one layer, and it has something factory lacks: a **criteria-based Hall of Fame** with real numbers — CelsiusTech moving from 65% to 20% of system cost being software; an NRO toolkit at 50% cost and schedule reduction with 10× fewer defects. **Three defence or government inductees, and Toshiba is in it** — meaning the durable part of the Japanese software factory survived, under the product-line label, once the factory metaphor was dropped.

But product lines assume **one organisation building a related family of products**. A multi-tenant assurance substrate is not that. Hence the three-layer split above rather than a wholesale relabel.

## The opening

**NIST SP 800-204D explicitly declines to standardise integrated DevSecOps platforms, on the grounds that they are too immature.** A standards body saying "this is not yet standardisable" is an invitation, and it is the cleanest available answer to "why hasn't someone already done this".

## Still missing

The DIB SWAP study, the 2018 Defense Science Board report, and SEI's 2025 *State of DevSecOps in the DoD* — the only DoD-wide baseline — are all confirmed to exist but were not retrievable. MITRE, IDA, Aerospace Corporation and NATO STO were not covered at all.
