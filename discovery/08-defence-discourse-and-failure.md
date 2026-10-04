# What the industry has actually said, what went wrong, and the cATO memo read first-hand

Combines `research/07-defence-industry-discourse.md` (~36,000 words) and `research/09-failure-modes.md`. Recorded 2026-10-03. The cATO section I verified myself; the rest is **Primary** as reported.

**Two tooling unlocks worth keeping.** `curl https://r.jina.ai/<url>` renders JavaScript and defeats Cloudflare — **it got through the `.gov` 403 wall that had blocked every agent**, which is how the cATO memo below was finally read. And `search.brave.com` works where Google, Bing, DuckDuckGo, Mojeek and SearXNG all CAPTCHA. Also note **the DoD is now styled "Department of War" (DoW)** across dodcio.defense.gov, which corroborates Big Bang's `Chart.yaml` describing "DoW hardened and approved packages".

---

## 1. Does detailed public material exist? Yes — and not from the primes

**Nine of seventeen US primes and SIs published nothing at all**: Boeing, L3Harris, Northrop, Parsons, ManTech, CACI, Accenture Federal, Deloitte US, IBM — Deloitte checked against a full 6,386-URL sitemap scan. UK and European primes are worse: QinetiQ has one consulting brochure, Babcock returns "Nothing Found", and Capgemini's software factories are for carmakers.

**No prime or SI has published a single failure case study, and none publishes a DORA metric.**

The substance sits with practitioners doing retrospectives, one vendor, and two governments. The three best sources:

1. **The Kessel Run post-mortem transcript** — four current and former leaders dissecting a cancelled programme two of them founded. The best source in the entire brief, with nothing close behind it.
2. **Bryon Kroger, "The software factory reckoning"** — the man who coined the term saying it lost the plot. Notably **not in Rise8's own sitemap**; found only via Marginalia.
3. **UK MOD "Evidence-led assurance for the SDLC"** (21 Sept 2026, OGL-licensed), which cites Platform One and the DoD guide by name. **It is Part 1 of 3, and Part 2 — the normative standard — is unwritten.** That is an open door.

Plus Second Front's ATO-pitfalls writing (by an ex-IC/NGA CISO) and Defence Unicorns' open-source `uds-software-factory`.

## 2. The cATO memo, read first-hand — and the fork resolves

The research flagged an unresolved fork: DoD doctrine reportedly treats cATO as *"an organizational state of cybersecurity maturity"*, while Kroger — who coined cATO and now argues the term should be retired — points out that NIST 800-37 authorises **systems**, and that the drift "favored certain technologies and political interests." Different architectures follow from each reading, so it mattered.

I retrieved the signed memo (4 Feb 2022, Office of the Secretary of Defense). Verbatim:

> "The purpose of this memo is to provide specific guidance on the necessary steps **to allow systems to operate under a cATO state.**"

> "In order to achieve cATO, the Authorizing Official (AO) must be able to demonstrate **three main competencies**: **On-going visibility** of key cybersecurity activities inside of the system boundary with a robust continuous monitoring of RMF controls; the ability to conduct **active cyber defense** in order to respond to cyber threats in real time; and the **adoption and use of an approved DevSecOps reference design.**"

> "The AO must approve, support and manage an organization's CONMON plan for all applications."

**The fork resolves in Kroger's favour on the narrow point.** The memo authorises *systems*; the organisational element is the AO's continuous-monitoring plan, not the unit of authorisation. The "organizational state of maturity" framing is downstream drift, not the policy. Design for system-scoped authorisation with organisation-level monitoring, and do not build an architecture that assumes the organisation itself gets certified.

**And the memo contains the strongest possible support for this project's thesis, in DoD's own words:**

> "For cATO, **all security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism for AOs to view the environment.** Using this information, the AO will be better positioned to make real time and informed risk decisions…"

A continuous, machine-fed evidence requirement, in authoritative policy, since February 2022.

> **CORRECTED 2026-10-04, twice over. See `00-index.md` 0.8 / 13.4 and 1.5.**
>
> **(a) Do not use the strong thesis.** The memo sentence above does not survive its own successors: the 2024 Evaluation Criteria reissued "**all** security controls" as "**which** security controls", accepts *"screen shots of control gate output as displayed in a dashboard"* as evidence (a PNG meets the requirement), makes "automate security control configurations and validation" an **Objective** rather than a threshold requirement, and the memo itself licenses manual controls — *"Manual controls will have different timelines associated"*. **The statement that survives: policy demands continuous evidence and names the pipeline as its source, but specifies no machine-verifiable form — and that gap is where the stale document returns.**
>
> **(b) Do not write "three-and-a-half-year-stale OSCAL file."** Big Bang's `oscal-component.yaml` has **six commits ever**; the last substantive edit was **April 2023**; the later commits are a URL fix and a global departmental find-and-replace, so **mechanical sweeps make it look maintained in the commit log** while nobody has reviewed its substance. Its metadata still claims 2022. The sharper framing is the gate, with dates: **built Feb 2024, disabled Aug 2024 ("known issues"), deleted Sep 2025.**

Set against RAND's 2025 finding of "limited movement toward implementation of continuous authority to operate", the weaker version of the gap is still documented from both ends — and it is the version that survives someone reading the primaries in front of you.

All the other DoD primaries are now reachable the same way — the Reference Designs, the cATO Evaluation Criteria, the Continuous Authorization Implementation Guide, DoWI 8430.01 "Accelerated Mission Software", the Software Modernization Strategy, and *The State of DevSecOps Report*.

## 3. What makes a good one — ★★★ means commercially opposed sources agree

★★★ **Don't build your own platform.** Said by a consultancy, a platform vendor, **and the DoD's own implementation guide** ("should be avoided if possible").
★★★ **Control inheritance from assessed common control providers is the economic engine.**
★★★ **Draw the authorisation boundary tightly, at design time.**
★★★ **The pipeline definition lives outside the application repo, inherited from a governed template.** Booz Allen, and the only published code anyone offered.
★★★ **Compliance as a by-product of engineering** — machine-readable evidence, OSCAL.
★★★ **Treat assessors and AOs as users.** Rise8 and UK MOD reach this independently, which makes it the most interesting agreement in the corpus: *"the central delivery constraint is organisational decision confidence, not engineering capability."*
★★★ **Change behaviour first; culture follows.**
★★★ **Protect the operator feedback loop.**
★★ Opinionated platform, serving 95% well. ★★ Embed assessors at a stated ratio (VA used 1:4). ★★ Assume air-gap by default and embed the scan report immutably in the bundle. ★★ **The UK's five decision states beat the US binary** authorise/don't — and it is free to copy.

## 4. What makes a bad one — the richer half, contrary to expectation

- **Fake production.** *"'We have 20 apps in prod' because they label an environment prod that's actually dev or test."*
- **EVM re-baselining** as institutionalised lying.
- **Teams can bypass their own gates.** Booz Allen, plainly: *"developers have access to this Jenkinsfile."* This is the key design constraint, and it is why the gate must live where the tenant cannot edit it.
- **Mission creep** — including the specific trap of becoming a factory-builder for others.
- **Platform wars**, and building your own platform. Kessel Run spent four years on one and delivered nothing from it.
- **Talent dilution** — 1,200 people, roughly 400 doing the work.
- **Bureaucratic re-encroachment.** TDY budget cut 75% → user-centred design collapsed → deployments fell from many per day, to monthly, to zero.
- **"The goodness doesn't scale past the protected pilot."**
- **Accountability levers never pulled**, because the replacement cycle is slower than tolerance for poor performance.
- **Gates that increase the risk they exist to reduce** — transaction cost drives up batch size, which drives up incidents.
- **"Compliance eats mission"** — the contracting officer is personally liable and is handed a contract that buys hours.

### The best-documented single finding in the whole programme

UK NAO, HC 797, on Defence Digital — cause and effect in one audited sentence:

> Defence Digital had *"a culture focused on the approvals process rather than outcomes"*, which *"incentivised [TLB CIOs] to maintain or produce their own separate capabilities… rather than rely on shared ones."*

That is the ivory-tower-to-shadow-platform mechanism, audited. And per `discovery/05`, in a classified environment a shadow platform is a security incident rather than a productivity loss.

### Gate fatigue, now with peer-reviewed evidence

Hu, Wang, Rubin & Pradel, **FSE 2025**: suppressions grow **monotonically**, **50.8% suppress nothing**, dead suppressions **silently mask future findings**, and the top cause is false positives. Note the honest limit: the research **could not substantiate any named organisation switching gates off**. Say so rather than asserting it.

## 5. Kessel Run, the honest version

Created July 2017 after AOC-WS 10.2 was cancelled ($374m → $745m development, >$3.5bn lifecycle), with AOC Pathfinder promising capability "within one year."

**Delivered:** real applications, Slapshot at Kabul (123,000 evacuees), and durable policy change — continuous ATO and the software acquisition pathway. **Did not deliver** the AOC replacement; KRADOS only reached *"parity with TBMCS"* in August 2022.

Kroger, who co-founded it: by 2022 it was **"failing"** and **"not doing its mission"** — and pointedly, *"It's the Air Force that failed Kessel Run."* The structural fact that explains most of it: *"We were turning over 50 percent of our staff every six months"*, and *"What software company… turns over their entire C suite every two years?"*

March 2025: reverted to "government-led, vendor-managed", single vendor per portfolio. A serving engineer, anonymous and fearing reprisal: *"It's back to the future."* **February 2026: Kessel Run opened a new Next-Generation AOC programme — RFP November 2026, contract award June 2027.** Ten years after the cancellation it was created to fix.

Kroger is also the sharpest anti-platform sceptic, and the line to have an answer for: *"if you want to make toast, you don't go build a toaster… Just build the apps."*

## 6. Nobody has rigorously measured any of this

Four audit findings of the absence (GAO-21-105298, GAO-23-105611, GAO-23-105867, NAO HC 797). **No controlled study, no before/after baseline, no peer-reviewed evaluation of any named factory.** GAO's hard number: **only 6 of 36 weapon programmes self-reporting Agile delivered software to users in under three months** (June 2021). GAO-23-105611 recommendations 1 and 6 — performance measures, and data to measure outcome-oriented goals — are both still **Open**, with DoD responding that some actions "may be impractical or outdated."

**Position the project around the absence of measurement, not around claimed benefit.** Everyone else is claiming; nobody is measuring; that is an available differentiator.

## 7. The strongest evidence-based negative anywhere, and it is aimed at us

**DORA 2024** (primary, 39MB PDF retrieved). Internal developer platform users show +8% individual productivity, +10% team performance, +6% organisational performance — **but throughput −8% and change stability −14%**, with the report stating that "change failure rate and rate of rework are significantly increased when a platform is being used."

Two under-cited findings on top: **mandated exclusive platform use costs a further −6% throughput**, and platform use combined with instability predicts burnout. The lever that helps is **developer independence, +5%**.

DORA's own prescription is the design instruction: *"a platform should provide methods for users… to break out of the tools and automations provided in the platform."*

Caveats to state when quoting it: correlational; 89% of respondents reported using an IDP, so the comparison group is small; the definition is broad; the J-curve applies; and DORA itself raises reverse causation.

**This is the number that should shape the design.** A mandated, air-gapped platform sits squarely in the worst cell of that table — mandated exclusive use, no escape hatch, no external managed services. The mitigations are not optional extras.

## 8. Numbers worth quoting, and ones to avoid

**Use:** GAO-19-471 — **$90bn FY2019 federal IT spend, 80% on legacy maintenance** (the only independent audit figure; prefer it over the ubiquitous but weak Standish 13/8/70). **Defence Unicorns: NAVSEA approval 6 months → under 2 days, then 13 production updates in 9 months** — published against their own commercial interest, and a hint that accreditation speed may not be the binding constraint. **Govini: DISA IL5 provisional authorisation July 2024, then separate ATOs January, June and August 2025** — two years to coverage despite "reciprocity", so impact levels are separate regimes rather than a ladder. **VA baseline: 568-day average ATO, 143 days to fix criticals, 74 POA&Ms per production system**, moving to cATO with roughly 70% inheritance, of which ~27% from the platform alone — the only decomposed figure anywhere, and it suggests vendor claims of "80–90% inherited from the platform" are one recycled 2019 number. **Second Front: DIY FedRAMP $1.5M typical, $3.7M+ complex, underestimated by 40–60%.**

> **RETRACTED — both of these were half-invented, and the source has now been read.** See [10](10-dod-primaries-devsecops.md).
>
> The real sentence is the *opposite* in tone: *"There are over 50 software factories using DevSecOps to deliver code into production, learning how to incorporate these practices into the high-stakes DoD environment and providing templates and patterns for generalized transition."* The clause **"only a few delivering real outcomes" appears nowhere** in the document. Searched for `only a few`, `in name`, `real outcomes`, `few deliver`, and every instance of `50`.
>
> On the second: *"approximately 78 DoD acquisition programs have adopted the software acquisition pathway. Seventy-five percent of those programs are delivering software in less than six months"* is real, but sourced in a footnote to an August 2024 fact sheet rather than measured by the study. **"But most don't track whether the software worked" is not in the document**, and the report argues the reverse intent — its evaluation table leads with "Did we build the right thing?"
>
> Both composites were plausible, pejorative, and would have been embarrassing to repeat in front of anyone who had read the report. **Never attribute a composite sentence to a document nobody in the programme has opened.**

**Avoid:** Scale AI's figures, Peraton's 50–75%, and Platform One's "days instead of a year" — no baselines, no sources. Also note there is **no agreed pre-factory ATO baseline at all**: Rise8 says six months to two years, Second Front says 18–24 months, neither cites a source. "Six months" is the de facto baseline, converging independently at RTX, Lockheed, Sigma and Defence Unicorns.

## 9. Design implications, consolidated

- **Ship per-tenant outcome measurement, baselined before adoption.** Nobody does this, four audits complain about it, and it is cheap.
- **Never be the only road; always be the fastest.** Build a deliberate escape hatch, because DORA measures the cost of not having one at −6% throughput.
- **Expiring, self-pruning suppressions** — and own the CPE/identity layer rather than handing out a mute button.
- **The gate must live where the tenant cannot edit it.** Booz Allen's Jenkinsfile problem is the canonical failure.
- **Fund as a product, or buy.** Customer-funded is SDC's failure encoded in the budget line.
- **Composable and forkable beats hosted and singular.**
- **Design against operator rotation** — 50% staff turnover every six months was Kessel Run's actual cause of death.
- **State the margin over components obtained separately.** If the answer is "integration", say which integration and what it saves.

## 10. Two openings

**The UK gap is real and unoccupied.** "Software factory" returns **1 GOV.UK hit** — an employment tribunal — against **321 for "secure by design"**. So don't use the name here. MOD abolished accreditation certificates in July 2023 and left the evidence manual; "Evidence-led assurance" is MOD trying to mechanise it, and **Part 2, the normative standard, is unwritten**. **No UK or EU commercial product exists in this space.** And the Technology Code of Practice point 3 — publish your code — is enforced by spend control, which is a stronger open-source lever than anything in US federal.

**The business-model space is bracketed by two real examples:** Nava (Apache-2.0 reference architecture, public benefit corporation) and Defence Unicorns (open-core, licensed per environment, priced on the accreditation boundary). Both are closer prior art than anything a prime has published.
