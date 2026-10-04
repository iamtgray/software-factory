# DoD primaries: *The State of DevSecOps* (Mar 2025) and *Software Modernization Implementation Plan FY25–26*

**Sources read in full, first-hand:**

- `sources/dod/01-state-of-devsecops.md` — *The State of DevSecOps*, Office of the DoD CIO, March 2025, 47pp, Distribution Statement A. Insights drawn from "two Federally Funded Research and Development Centers" — SEI (Carnegie Mellon, contract FA8702-15-D-0002) and MITRE. Original PDF: `dodcio.defense.gov/Portals/0/Documents/Library/DevSecOpsStateOf.pdf`.
- `sources/dod/10-sw-mod-impl-plan-fy25-26.md` — *Software Modernization Implementation Plan, FY25–26, Unclassified Summary*, 27pp. Original: `dodcio.defense.gov/Portals/0/Documents/Library/SW-Mod-I-Plan25-26.pdf`.

Locators below are given as section number plus the page number from the running footer ("The State of DevSecOps within the Department of Defense | *n*"), which survived the text extraction. The Implementation Plan is cited by task number and page footer.

---

## Corrections to the site

### C1. The "over 50 software factories" quote is half-real. The damaging half is invented.

The site (`08-defence-discourse-and-failure.md:117`, `00-index.md`) attributes to this report: *"Over 50 software factories exist in name… only a few delivering real outcomes."*

The first clause exists. The second does not appear anywhere in the document. What the report actually says, in the Executive Summary (p.3), is unambiguously positive:

> "Over the past 5 years, DoD has made significant strides in adopting DevSecOps practices. There are over 50 software factories using DevSecOps to deliver code into production, learning how to incorporate these practices into the high-stakes DoD environment and providing templates and patterns for generalized transition."

Note "using DevSecOps to deliver code into production" — the opposite of "exist in name". The nearest thing to the pejorative half is the separate sentence immediately following:

> "Pockets of excellence have emerged across DoD in which DevSecOps practices have been successfully implemented, resulting in faster deployment cycles, enhanced security, higher software quality, greater operational efficiency, and improved end user value." (Exec. Summary, p.3; repeated §1.2, p.7)

"Pockets of excellence" carries the implication that the rest are not excellent, but it is a weaker and differently-shaped claim, and it is not attached to the number 50. **Searched for:** "only a few", "in name", "real outcomes", "exist in name", "few deliver", every instance of "50". The composite sentence is not in the document. If the site uses it, it must be attributed to whoever composed it, not to the DoD CIO.

### C2. The "75% in six months" figure is real but is not this report's finding, and the "most don't track whether the software worked" half is not in the document.

Verbatim, §2 "Celebrating Successes So Far" (p.10):

> "At present, approximately 78 DoD acquisition programs have adopted the software acquisition pathway. Seventy-five percent of those programs are delivering software in less than six months."

Footnote 2 sources this to *Structuring Change to Last: An Update on Innovation at the Department of Defense*, DoD, August 2024 — **not** to original work by this study. So it is second-hand even inside the report.

The clause "but most don't track whether the software worked" is **not found**. **Searched for:** "track", "outcome", "whether the software", "did we build the right thing", "value metric", "MOE". The report's actual position is the reverse of indifference: §8.1 (p.40) devotes the first row of Table 8-1 to exactly that question —

> "Did we build the right thing? Seek evidence that the product is useful to the user: Does the product satisfy Measures of effectiveness (MOE) or other value metrics, defined by users?"

— and §8 (p.39) notes "The Software Acquisition Pathway (and the Army's new software metrics) require the reporting of value metrics in units meaningful to the mission". Table 8-1 is a list of *questions to ask*, with no values attached, so the underlying point (nobody has published outcome data) survives — but the quoted sentence must be dropped.

Also available as a flanking figure, same page, properly sourced to GAO-24-106831:

> "In its most recent Weapon Systems Annual Assessment, the Government Accountability Office (GAO) reported that 75 to 80 percent of the 40 Major Defense Acquisition Programs (MDAP) it monitors have adopted modern development practices, including Agile and DevSecOps. GAO found that almost half of those MDAPs deliver software capability in less than four months." (§2, p.10)

### C3. The cATO quotes are correct, verbatim. But "effectively nobody holds a cATO" is not what the report says, and needs rewording.

Both site quotes (`09-oscal-graveyard-and-cato.md:69`) verify exactly. §5.6 "Baseline and Moving Forward" (p.29):

> "With the release of updated criteria, DoD is waiting for DoD Component CISOs to nominate software factories demonstrating the appropriate continuous monitoring, active cyber, and DevSecOps practices. These nominees will become the pathfinders that other programs can model and learn from."

And the "inconsistent" line, same paragraph, also verifies:

> "Prior to the 2022 cATO memo, several DoD software factories were operating in a fashion aligned with cATO but inconsistent across DoD Components."

**But** the very next sentence of that same paragraph says those arrangements persist and are working:

> "Those programs are still operating their continuous ATO as the updated cATO is adopted, and they are demonstrating enhanced security and identifying attacks to the DoD software supply chain faster than traditional programs."

Plus §5.1 (p.27): "DoD Components are actively applying the new cATO evaluation criteria to their software activities. Several programs have been submitted as pathfinders." And §5.6: "The Office of the DoD CIO has reviewed several candidates and is enthusiastic about their potential".

So the accurate formulation is: **no count of cATO holders exists in either document**, and the pathfinder cohort under the *updated* criteria had not been named as of March 2025 — not that nobody holds one. The Implementation Plan corroborates the stronger version in a more useful way (see F7 below): "Pilot cATO process and issue cATO" closed FY23–24 as **Carryover**, and FY25–26 task 2.4 promises "additional platforms with cATOs", the word "additional" implying a non-zero but unstated baseline.

**Searched for a count:** "number of cATO", "cATOs issued", "how many", any digit adjacent to "cATO", across both documents. **Not found.** Neither document states how many systems or platforms hold a cATO.

### C4. "No DoD4" — correct for these two documents, with one wrinkle worth knowing.

Neither document defines the "DoD4", and neither publishes values against it. The string "DORA" does not appear at all in *The State of DevSecOps* — not once in 47 pages, despite Forsgren/Humble/Kim's *Accelerate* appearing in the Works Cited (p.42). **Searched for:** "DORA", "DoD4", "DoD 4", "four key metrics", "deployment frequency", "lead time", "change fail", "MTTR", "ROI", "return on investment", "cyber resilience", "time to achieve ATO".

The wrinkle: DORA appears **once**, in the Implementation Plan, as a *future* intention under task 3.3 Modernize JCIDS for DevSecOps (p.14):

> "This task will provide updated JCIDS guidance that integrates DevSecOps more thoroughly in the joint requirements process and will identify expected outputs and recommended metrics like DORA metrics."

That is a planned deliverable with no date and no values. It strengthens rather than weakens the site's O9 point: as of the FY25–26 plan, DoD had not yet settled on DORA metrics in its joint requirements process, let alone published figures.

### C5. The report *does* define "software factory", identically in three places, and the definition is not original to it.

See F1. The site should cite the definition to *cloud.mil* via this report, since footnote 9 does.

---

## Verbatim findings by theme

### F1. Definition of "software factory"

Three identical statements. Executive Summary (p.3):

> "In DoD, a software factory is defined as a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."

§3 opener (p.13), with attribution:

> "DoD defines a software factory as 'a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes.'"

Footnote 9 sources this to: Cloud.Mil, "What is DevSecOps?", accessed 27 September 2024, `https://www.cloud.mil/devsecops/`. The Glossary (p.45) repeats it verbatim. The Implementation Plan glossary (Appendix A, p.19) repeats it verbatim under "DoD Software Factory". **It is therefore the stable, canonical DoD definition — identical across two independent publications.**

The report also defines **four** types (§3.1, p.14; Glossary pp.45–46): Mission-Critical Platforms; Training and Education; Innovation Pipelines; IaC and CI/CD. Footnote 11 (p.15) is important: **"A participant from the Innovation Pipelines category was not available for this study. Future studies will be sure to include this group."** One of the four categories has zero data in the only DoD-wide baseline that exists.

And the deliberate refusal to count:

> "Rather than assuming some correct number of software factories exists, we should place our focus on outcomes: How many of our systems are leveraging DevSecOps and agile practices to deliver mission-critical capabilities? How many are still trapped in legacy, waterfall models that can't keep pace with the changing environment?" (§3.2 "Support, Not Control", p.14)

Those are rhetorical questions. The report does not answer either of them.

### F2. What measured data the report actually contains

This matters for the "nobody has measured" claim, so here is the complete inventory.

**Survey instrument and sample (§3.3, pp.15–16):**

> "We used an established DevSecOps readiness assessment (which has been implemented with over two dozen DoD DevSecOps organizations) to derive 41 questions on team practices across these seven categories. We also established a rubric practitioners used to objectively rank the availability, frequency, degree, etc., of these artifacts and practices in their organization. Higher scores indicate use of more and better practices associated with that category. We also asked about use of metrics, reporting of metrics, and process measures including deployment frequency and lead times."

> "Over the course of several months, we met with 36 practitioners from 19 software organizations across the DoD Components."

Study-wide: "we interviewed more than 75 leaders and practitioners across DoD, representing 19 different software organizations of all types and test organizations representing cyber, developmental, and operational test" (§1.3, p.8; also Exec. Summary p.4). Workforce sub-study: "we conducted interviews with approximately 30 individuals at 19 DoD software factories and software organizations" (§7.1, p.36).

**Maturity distribution (Figure 3-2 "Behavior Profile Cultural Attribute Category", p.16).** Scores on a ~5-point scale by factory type across the seven cultural attributes. Values as extracted: 4.00, 3.40, 3.00, 3.29, 3.50, 3.20, 2.71, 3.40, 3.17, 4.00, 3.50, 2.83, 3.20, 4.00, 3.33, 3.33, 2.50, 3.00, 2.71, 2.80, 3.33. The figure legend is "Mission Critical / Training & Education / IaC & CI/CD — Average Rating by Cultural Attribute". **The chart-to-cell mapping did not survive text extraction**, so individual attribute scores cannot be reliably recovered from this file; the original PDF would be needed to tabulate them. The seven attributes are Leadership; Effective Communication; Collaborative Team Environment; Empowered Workforce; Rapid Feedback Loops; Continuous Learning and Skill Development; Skilled Workforce (§3.3, p.15).

Interpretation, verbatim (§3.3 "Baseline and Moving Forward", pp.17–18):

> "We have provided a baseline for measuring the degree to which behaviors that align with cultural attributes associated with DevSecOps are present in DoD software factories. We can use this baseline to observe how behaviors mature over time and potentially correlate these with outcomes including delivery speed, workforce retention, and user satisfaction."

Note the tense: *potentially correlate*. No correlation with outcomes was performed.

**Workforce percentages (§7.1, pp.36–37):**

> "When asked about the biggest risks their organizations face, 20 percent of the participants pointed to the long hiring lead time, which can result in potential candidates accepting opportunities elsewhere."

> "In our interviews, 68 percent of the participants cited pay disparity with similar positions in industry as a reason for staff leaving. For example, one team leader claimed that only 40 percent of the military staff chose to reenlist after their tour, opting instead to pursue a higher salary in the commercial sector."

**Delivery figures.** The 78 programmes / 75% / six months and GAO 75–80% / 40 MDAPs / four months, both quoted in C2 above (§2, p.10) — both second-hand.

**Iron Bank inventory (§2, p.10):**

> "the Iron Bank container repository has experienced an explosion of new containers and now holds over 1,200 hardened container images with approximately 400 commercial and 800 open-source images."

**Single-programme delivery data (§5.4 Success Story, pp.28–29):**

> "A NAVSEA team delivered 13 updates to an application in one of NAVSEA's production clouds over the last 9 months. They are also rapidly iterating software in Research Development Test & Evaluation (RDT&E) with features/bug fixes developed and delivered in 24-48 hours, farm-to-table."

> "Naval Sea Systems Command (NAVSEA) assessed and approved multiple software factories in CY24 following DevSecOps standards. Using the Afloat Software Authorization Playbook (ASAP) process, NAVSEA software factories are rapidly delivering new software solutions for afloat and ashore programs… This streamlined process has significantly reduced the time required to deploy critical software updates"

(No baseline given for "significantly reduced" — the Defence Unicorns "six months to under two days" figure already in the site's notes is the external pairing for this.)

**Other named numbers:**

- Training & Education factory interviewee: "there were 'days where we've done [deployments] 20 times.'" (§3.3, p.16)
- LaunchPad: "delivering digital-engineering-related software solutions to over 650 users from 175 different organizations" (§4.3, p.22)
- AFSC/SW "has already completed an initial inventory and assessment of about 30 AFMC software activities" (§2, p.11)
- MEPCOM: "a dedicated team of 20-25 government personnel"; "Leadership gave Matt 51 percent authority in decision-making"; "Every two weeks the team delivered working software" (§2, p.12)
- Kessel Run "received funding from at least five different program elements" (§4.3, p.21, citing RAND RRA550-1, 2022)
- Interagency agreement process "can consequently take up to six months… [vs] processed in 30 days" (§4.5, p.24)
- "The CWF Implementation Plan sets a goal to reduce time-to-hire to 60 days by FY27" (§7.2, p.37)
- DAU: "'micro-learning' course modules that are typically 10-15 minutes long"; partnerships "have yielded over 100 DevSecOps course offerings" (§7.2, p.38)
- One anonymous team: "We looked at the NIST 853 controls and identified 100 controls that were required at the application layer" (§6.6 sidebar, p.35)
- Implementation Plan, p.4: "Of the initial forty-one (41) tasks identified in the FY23-24 implementation plan, twenty-seven (27) were accomplished, twelve (12) were carried over to the FY25-26 implementation plan, and two (2) were combined with other tasks"
- Implementation Plan task 3.6 (p.16): "Programs adopting the software acquisition pathway increased at an annual rate of approximately 50% and accelerated delivery cadence to the end user."

**What is absent.** No deployment-frequency values. No lead-time values. No change-failure-rate or MTTR values. No cost figures, no budget totals, no per-factory spend. No named list of the "over 50" factories. No before/after comparison for any factory. No controlled comparison of DevSecOps against non-DevSecOps programmes. No cATO counts. The culture scores are the only original quantitative output of the study, and they measure *self-reported practice adoption*, not delivery outcomes.

### F3. Self-criticism — the most valuable sentences in the document

These are ordered roughly by force.

**On the study's own method (§1.3 and §3.3):**

> "This study focused on the current state of DoD practices. We used quantitative metrics, although at this point in our journey, it was necessary to augment them with qualitative information via user surveys." (Exec. Summary, p.3)

> "To limit the disruption to software teams, we did not attempt a comprehensive survey with a broad data call. Instead, we attempted to find a representative sample that would provide an initial indicator and validate the approach." (§3.3, p.15)

**On not knowing what is happening (§4.4, p.24):**

> "We don't currently have insight into how widely IDIQs or OTAs are being used in the DoD to enable DevSecOps activities."

**On being unable to measure value (§4.7, p.25):**

> "Software factories today employ widely different funding models that are often combined in novel ways, making it difficult to measure or quantify the 'best fit' approaches for delivering value in different contexts. Inconsistent mechanisms for reporting utilization of cloud-based services contribute to the complexity. We have some insight into the efficacy and fitness of these different approaches in different contexts but need to continue gathering data."

**On reference metrics not existing (§4.7, p.26):**

> "The development of a baseline set of common, goal-oriented 'reference metrics' could further facilitate such analysis."

**On fragmented, incompatible reporting (§4.2, p.20):**

> "Currently, there are several systems, approaches, and reporting cycles for collecting DevSecOps metrics from the DoD Components and acquisition programs. Acquisition programs currently provide various subsets of their DevSecOps metrics or status information to multiple OSD stakeholders, often by differing means, formats, or reporting systems."

**On factories not being able to model their own finances (§4.3, p.23):**

> "Several DoD software factories indicated they have inadequate business models to support the level of effort and growth they are expected to achieve. While some factory leaders bristled at being held to long-term budgets in a dynamic environment, DoD Components noted that the software factories can't yet adequately model use of funds. The consequence of inadequate business models keeps those software factories underfunded and understaffed, which can affect both morale and the timely delivery of capabilities."

**On cost data being uncapturable (§4.3, p.23 and §4.6, p.25):**

> "cloud services have been purchased through a wide variety of contracts with differing terms and utilization data isn't captured or reported in uniform ways, contributing to the difficulty in calculating and forecasting true costs in fee-for-service approaches."

> "The variety of mechanisms organizations have used to purchase cloud services presents a challenge to obtaining utilization data. This challenge makes it difficult to report and model costs, which in turn affects capacity planning."

**On cATO effectiveness being unmeasured, and voluntarily so (§5.6, p.30):**

> "Organizations don't have to provide metrics for cATO effectiveness, but we are interested in potential metrics to evaluate the effectiveness of the cATO process from a DoD governance perspective."

That sentence is the single strongest support for the site's thesis in either document. The five candidate metrics that follow — Mean Time to Patch Vulnerabilities, guardrail/control-gate trend metrics, feedback communication frequency, mitigation effectiveness, security posture dashboard metrics — are proposals, with no values.

**On measurement for pathfinders being prospective (§5.6, pp.29–30):**

> "Pathfinder cATO software factory measures will include lead times and process flow status to help software teams plan and negotiate commitments. At the enterprise level, this data will provide visibility into improvements in the timeliness of cATO approvals"

Future tense throughout.

**On policy intent not reaching implementers (§6.3, p.33) — direct participant quote:**

> "The intent is good news. The intent is changing the narrative, but that intent that has not trickled down to the tactical implementation level. You may have a policy at the DoD level that is very broad, but there can be a lot of constraints added between the DoD level and the implementors."

**On the test/compliance wall (§6.3, p.33) — participant quotes:**

> "I am agile up to the point of being tested. I go super-fast up till test and compliance."

> "AOs …[are]… removed from the consequences of not having a given app—so their only incentive is to achieve security or not approve it at all."

> "[We are] told to take risks and upset the apple carts… but contradicted by the ITAS (Information Technology Approval System) not trusting us to make a decision over $500.00."

**On AO behaviour (§5.4, p.28):**

> "Too often, cybersecurity teams, IT infrastructure teams, development teams, leadership, AOs, and DoD Component CISOs don't engage in a collaborative manner, which is necessary to achieve cATO."

> "it is a common refrain that AOs are 'biased to caution' rather than 'biased to action' resulting in delays of software capabilities."

**On reciprocity failing (§5.5, p.29):**

> "Common discussion points included lack of reciprocity and cases in which reciprocity guidance was unclear, leading to uncertainty with how assessors and AOs would interpret guidance (e.g., when controls could be inherited). The lack of reciprocity between the Military Services prevents mission owners from making their own decisions, and it blocks developers from using tools developed at other Military Services. An interviewee described an instance of cross-Military Service ATO authorization taking several months—common frustration."

**On the ecosystem being unmanaged (§3, p.13):**

> "In the absence of a strategic centralized approach, every successful software factory had to evolve its own business operations. Most efforts have been successful but were accomplished through perseverance and dedication."

> "Over the past four years, it has become apparent that DoD needs to apply more consistency to nurturing and managing the software factory ecosystem."

**On consolidation being resisted (§4.3, p.21):**

> "Some interviewees felt that DoD tries to force consolidation instead of building services people want to use."

> "Participants expressed concern that the initial enthusiasm to promote DevSecOps and associated software factories downplayed some of the technical complexities that differentiate systems and drive their pipeline requirements. That concern influences some programs to create their own pipelines and/or software factories because large 'enterprise' software factories don't support their unique needs."

**On supply-chain mandates being unvalidated (§4.5, p.24):**

> "These issuances have not yet been widely established or validated, which creates an excellent early opportunity to instrument their use to understand the executability of the associated business processes and the overall effectiveness of these approaches."

(Referring to NIST SP 800-218 and EO 14028 — i.e. the secure-development and SBOM mandates.)

**On workforce initiatives being early (§7.3, p.38):**

> "While substantial progress has been made, many improvement actions remain in the early stages of implementation."

**On acquisition latency being invisible to tooling (§4.5, p.24)** — useful if the site argues platform metrics under-report real cycle time:

> "They affect speed of software delivery but may be invisible in technical software tracking metrics because they occur before development teams start instrumenting their software development and delivery processes."

### F4. Evidence, artefacts, continuous monitoring, control inheritance

**The best quote in either document for "compliance evidence should be a build output".** §6.6 sidebar, attributed "— Anonymous" (p.35):

> "The RMF process was going to be the bottleneck. We looked at the NIST 853 controls and identified 100 controls that were required at the application layer. We baked those into our pipeline for automated control and testing. Then we continuously monitor and make sure the controls stay up to date."

("NIST 853" is an extraction or original typo for NIST SP 800-53.) This is a DoD practitioner, in a DoD CIO publication, describing exactly the pattern — controls identified, baked into the pipeline, automated, continuously monitored. It is presented as a success story, not a deviation.

Paired sidebar, same page, same attribution:

> "You need to build a culture that gets Operational Test, Pen Testers, and certifiers involved. I brought cyber into sprint reviews and the Authorizing Official was there as well. I tried to have cyber folks understand they are agile too."

**cATO requires evidence, demonstrated (§5.3, p.28):**

> "A high-level summary of the evaluation criteria for cATO requires that practices are defined and documented; evidence exists on the use of risk management and continuous monitoring practices, with demonstrations; the workforce is knowledgeable on the cATO practices; and the level of implementation of the cATO risk management practices has been reviewed for effectiveness."

**The three competencies (§5.2, p.27):**

> "There are three main competencies that must be demonstrated by the Authorizing Official: ongoing visibility of key cybersecurity activities inside of the system boundary with a robust continuous monitoring of RMF controls; the ability to conduct active cyber defense in real time; and the adoption and use of an approved DevSecOps reference design."

**cATO definition (§5.1, p.27; Glossary p.44; identical in the Implementation Plan glossary, p.19):**

> "cATO is the state achieved when the organization that develops, secures, and operates a system has demonstrated sufficient maturity in its ability to maintain a resilient cybersecurity posture that traditional risk assessments and authorizations become redundant. This organization must have implemented robust, continuous information security monitoring capabilities; active cyber defense; and secure software supply chain requirements to enable continuous delivery of capabilities without adversely impacting the system's cyber posture."

Note "traditional risk assessments and authorizations become **redundant**" — not supplemented. The document-as-deliverable is explicitly displaced.

**Prerequisite, which bounds any greenfield cATO claim (§5.2, p.27):**

> "To obtain a cATO, the system must have an existing ATO and have entered the RMF monitoring stage."

**Artefacts as the unit of cultural measurement (§3.3, p.15):**

> "Understanding culture requires analysis of artifacts and practices in context. Those artifacts and practices reflect the shared understanding that guides behaviors… To talk about culture in DevSecOps teams in a meaningful and repeatable way, we needed to develop an objective, evidence-based approach."

> "In addition, we asked practitioners to provide concrete examples of artifacts or process descriptions."

**Policy to be written from evidence (§3, p.13):**

> "The Office of the DoD CIO is planning to write DoD policy to codify successful, evidence-based practices and to strengthen the Digital Arsenal."

**Control inheritance via hardened images (Glossary, "Iron Bank", p.45):**

> "These hardened containers, along with security accreditation reciprocity, greatly simplifies and speeds the process of obtaining an Approval to Connect (ATC) or Authority to Operate (ATO)."

**Compliance checking as a CI output (Glossary, "Continuous Integration", p.44):**

> "The security scans include, but are not limited to, dynamic code analysis, test coverage, dependency/BOM checking, and compliance checking. The outputs from continuous integration include the continuous build outputs, plus automation test results and security scan results."

This is the DoD's own glossary placing BOM checking and compliance checking among the *outputs of the build*. Directly on-thesis.

**Where measures should come from (Table 8-1, §8.1, p.40):**

> "Measures may come from test reports, problem reports, change requests"
> "Measures may come from ticketing time stamps and release dates"
> "Evidence should be found with change requests in the ticketing system properly labeled, prioritized, and tracked to successful closure"

**Reciprocity as default policy (§5.5, p.29):**

> "In the May 2, 2024, memo, 'Resolving Risk Management and Cybersecurity Reciprocity Issues,' the Deputy Secretary of Defense directed that reciprocity be the default stance, 'except when cybersecurity risk is too great,' and further directed that when reciprocity issues can't be resolved by the DoD Component-level CIOs, they be elevated directly to the DoD CIO for resolution."

### F5. Measurement framework actually published in *The State of DevSecOps*

There is one, and it is a question set, not a metric set. §8.1 Table 8-1 "Data Linking DevSecOps Organizations with Mission Outcomes" (p.40), seven rows: *Did we build the right thing? / Did we build the product right? / Did we get the product to the right people? / Is the product delivered quickly and frequently? / Is the product delivered at the speed of relevance? / Is the product adaptable to change? / Is development responsive to user feedback?*

The one row closest to DORA (§8.1, p.40):

> "Is the product delivered quickly and frequently? Are we tracking lead times to user, and deployment frequency to operations or operationally representative environments? Are deployment frequencies stable/predictable over time?"

Note "*Are we tracking*" — the question is whether tracking happens at all.

The anti-aggregation rules (§8, p.39 and §8.2, p.41) are worth quoting if the site argues against enterprise-level dashboards:

> "if a business system has a deployment frequency to end users of once per week and a fighter aircraft has a deployment frequency to flight test once per month, taking the 'average deployment frequency' between the two isn't meaningful."

> "Data can be aggregated, but metrics can't. Metrics have already combined data, often in complicated ways. Don't combine again without carefully checking the math. Often, the metric used is a proxy, and not a direct measure."

> "Manage to mission value, not metrics. The metric is not the objective—it just tells you how you're doing against the mission objective."

Also noted (§4.6, p.25): the Navy PEO Digital Innovation Adoption Kit's "World-Class Alignment Metrics (WAMs)", described in footnote 21 as offering "a standard measuring methodology that also links technology outcomes to the mission outcomes they produce" with "metrics… associated with data sources, both manual and automated (e.g. ticketing systems)". No values published. Possibly a lead worth chasing separately.

### F6. The strategic framing, for context

> "Existing Cyber practices, Test and Evaluation practices, Acquisition, and others including Requirements, AI, and Accounting all need to be realigned towards rapid, incremental delivery and operationalization of minimal mission capability." (Exec. Summary, p.4)

> "Most important: systematically equipping DoD with the 'software weaponry' needed to maintain strategic advantages against adversaries in a digital world." (§3, p.13)

> "The goal is for the government to own the means of production while contractors and the DIB provide domain expertise using DoD software factories and DevSecOps platforms." (§4.5, p.24)

That last one is a clean statement of the inversion the site is arguing about, in DoD's own words.

Six characteristics of effective policy, "S-P-E-E-E-D" (§6.2, p.32): Socialized; address the entire DoD **P**ortfolio; **E**xecutable; consider implementor **E**xpertise; **E**volving; easily **D**iscoverable. Most quotable:

> "While strategic-level policy and guidance may be visionary in nature, operational-level policy issuances should be executable based on current capabilities and limitations. Policy that can't be implemented will be ignored or will generate frustration."

> "Highly prescriptive IF-THEN-ELSE type guidance isn't a viable approach to complex DevSecOps environments and challenges."

---

## F7. Implementation Plan FY25–26: carryover and incomplete items

**Confirmed: both site claims are correct.**

From Appendix D, "Results of FY 23-24 Software Modernization Implementation Plan" (pp.25–26), a two-column table of subtask against Result:

> "3.1.2  Pilot cATO process and issue cATO  **Carryover**"

Sibling subtask for contrast: "3.1.1 Publish cATO follow-on guidance — Completed". So the *guidance* shipped and the *pilot and issuance* did not.

And "Provide cATO Analytics" is confirmed as a future deliverable — Implementation Plan §2.4 (p.11), subtask **2.4.2**, repeated in Appendix B (p.21). Task 2.4's stated outcome:

> "This task will deliver additional platforms with cATOs, cATO analytics regarding adoption and impact, and training material for Authorizing Officials."

Full task 2.4 description, which is itself an admission:

> "Continuous Authorization to Operate (cATO) (defined in glossary) must become a standard business practice. This requires not only having sound criteria to issue a cATO, but building a community of Authorizing Officials who understand the criteria itself and can provide feedback into the process to better inform criteria requirements for sound risk decisions. DoD must continue to work with DoD Components to help software platforms mature their people, processes, and technology to obtain a cATO; issue cATOs to qualifying platforms; and educate Authorizing Officials on leveraging and trusting cATOs." (§2.4, p.11)

"**must become** a standard business practice" and "educate Authorizing Officials on **leveraging and trusting** cATOs" — as of FY25, it is not standard and AOs do not trust it.

### Complete list of FY23–24 Carryover and OBE items (Appendix D, pp.25–26)

Twelve Carryover, two OBE ("overcome by events"), twenty-seven Completed.

| ID | Subtask | Result |
|---|---|---|
| 1.3.1 | Evolve BCAPs to a Zero Trust architecture | **OBE** |
| 1.3.2 | Establish the Defensive Cyberspace Operations (DCO) capability | **Carryover** |
| 1.3.3 | Operationalize DCO with the CSSP community | **Carryover** |
| 1.3.4 | Modernize cloud endpoint security | **OBE** |
| **2.1.1** | **Establish software factory criteria and metrics** | **Carryover** |
| 2.1.2 | Inventory digital platforms and software factories | Completed |
| 2.1.4 | Implement pilot to provide Digital Engineering as a Service (DEaaS) | **Carryover** |
| **2.2.2** | **Publish Software Bill of Materials (SBOM) Implementation Guidance for DoD** | **Carryover** |
| 2.2.3 | Provide clear Agile Software and DevSecOps testing guidance | **Carryover** |
| **3.1.2** | **Pilot cATO process and issue cATO** | **Carryover** |
| 3.2.2 | Promote software modernization across all acquisition pathways | **Carryover** |
| **3.2.4** | **Collect cost data on agile software programs** | **Carryover** |

(Appendix D as extracted lists ten Carryover rows against the stated count of twelve; two rows appear to have been lost in extraction, most plausibly from the Goal 2 continuation across the page break at p.25/26 where the footer is duplicated. The ten above are verbatim.)

**The four bolded rows are the ones that matter to the site, and together they are devastating in a way the site has not yet used:**

1. **2.1.1 "Establish software factory criteria and metrics" — Carryover.** DoD set itself the task of defining what a software factory must meet and how to measure it, over FY23–24, and did not finish. This is *direct documentary confirmation* of the measurement absence, from the DoD's own scorecard, and it is stronger than anything in *The State of DevSecOps*. It also explains why *The State of DevSecOps* contains no delivery metrics: the criteria and metrics did not exist when it was written.
2. **2.2.2 "Publish SBOM Implementation Guidance for DoD" — Carryover.** DoD-wide SBOM implementation guidance was not published in FY23–24, despite EO 14028 (May 2021) and OMB M-22-18. The FY25–26 successor is weaker still: subtask **3.2.3 "Pilot SBOM Repository Capability"** (§3.2, p.14) — a pilot of a repository, not guidance. Task 3.2's framing claims DoD "rolled out software attestation and software bill of materials (SBOMs) requirements in alignment with… Executive Order 14028, and Office of Management and Budget Memo, M-22-18" — requirements rolled out, implementation guidance carried over.
3. **3.2.4 "Collect cost data on agile software programs" — Carryover.** No cost data on agile software programmes was collected in FY23–24. This pairs exactly with the *State of DevSecOps* admissions at §4.3/§4.6/§4.7 that cost and utilisation data cannot be obtained. **If anyone asks for the cost of a DoD software factory, the answer is that DoD tried to collect it, failed, and carried the task over.**
4. **2.2.3 "Provide clear Agile Software and DevSecOps testing guidance" — Carryover**, and then *re-listed again* as FY25–26 subtask **3.1.3 "Provide Clear Software Agile and DevSecOps Testing Guidance"** (§3.1, p.13). Same words, third attempt, second plan.

### Other FY25–26 items relevant to metrics, evidence or cost

- **2.1.1 "Provide DevSecOps Adoption Analytics"** (§2.1, p.9). Task 2.1's outcome: "This task will provide visibility of adoption through appropriate data and metrics captured in the DoD IT Portfolio Repository (DITPR) and a Catalog". So as of FY25, adoption visibility is a deliverable, not a fact.
- **2.1.2 "Publish a DevSecOps Platform and Software Factory Catalog"** (§2.1, p.9) — a catalogue of factories is still to be published, FY25–26. The FY23–24 "Inventory digital platforms and software factories" completed, but the published catalogue did not follow.
- **2.1.4 "Provide DoD-wide Software Assurance Capabilities"** (§2.1, p.9).
- **2.5.3 "Develop an approach to analyze the implementation of the Software Factory Financial Operating Model"** (§2.5, p.11) — an approach to analysis, i.e. two steps removed from figures. Task 2.5's own framing: "Across factories, financial operating models are inconsistent."
- **3.2.1 "Publish Secure Coding Practices and Metrics"** (§3.2, p.14). Task description: "This includes requiring software developers to meet or exceed performance metrics for following secure coding practices." Metrics not yet published.
- **3.1.4 "Provide Test and Evaluation Analytics and Updated Capabilities"** (§3.1, p.13).
- **3.6.2 "Improve Software Acquisition Analytics"** (§3.6, p.16).
- **3.3 "will identify expected outputs and recommended metrics like DORA metrics"** (§3.3, p.14) — see C4.
- An orphan objective. Appendix B (p.23) lists the objective **"Treat Software as Data"** under Goal 3 with **no tasks or subtasks mapped to it at all** — the only objective in the entire mapping table with an empty task column.

### Scale-of-adoption admission, Implementation Plan §2.1 (p.9)

> "The DevSecOps platforms and software factories that are the tangible implementation of this modern software approach are still in the early stages of adoption as the cultural shift required to make this ecosystem mainstream is significant."

March 2025, nine years after the first DoD software factory. Pair with Goal 2's framing (p.9):

> "In FY23-24, DoD established a software factory ecosystem baseline with the more mature software factories proving the value of DevSecOps through software delivery results."

"The **more mature** software factories" — DoD's own hedge, and the closest either document comes to the site's "only a few delivering real outcomes". It is weaker, and it is in the Implementation Plan, not *The State of DevSecOps*.

### Developer-experience admission, §2.2 (p.10)

> "Software developers and engineers continue to struggle through approval processes and red tape to obtain access to common development tools. This hinders productivity and delays the delivery of software capability. DoD governance must adjust regulations which hinder the talent pool from accessing the common tools needed to effectively develop software."

---

## Not found — explicit negative results

Each of these was searched case-insensitively across both files; the search terms are listed so the negative is reusable.

| Claim or item | Searched for | Result |
|---|---|---|
| "only a few delivering real outcomes" | `only a few`, `in name`, `real outcomes`, `few deliver`, all instances of `50` | **Not found.** The "over 50" clause exists; the pejorative clause does not. |
| "most don't track whether the software worked" | `track`, `outcome`, `whether the software`, `MOE`, `value metric` | **Not found.** Report argues the opposite intent (Table 8-1). |
| "DoD4" metrics framework | `DoD4`, `DoD 4`, `four key metrics`, `DORA`, `cyber resilience`, `time to achieve ATO`, `ROI`, `return on investment` | **Not defined in either document. No values published in either.** `DORA` occurs zero times in *The State of DevSecOps* and once in the Implementation Plan, as a future intention (§3.3). |
| Count of cATO holders | `cATO` adjacent to any digit, `number of`, `how many`, `issued` | **Not found in either document.** |
| DORA four metrics with values | `deployment frequency`, `lead time`, `change fail`, `MTTR`, `mean time to restore` | Named as things to track (§8.1, §5.6). **No values anywhere.** |
| Named list of the 50+ factories | `50`, `software factories` enumerated | **Not found.** Individually named: Platform One, Kessel Run, Kobayashi Maru, BESPIN, Tron/TRON, Rogue One, Corsair Ranch, SKI CAMP, DISA C2, Army Software Factory, XVIII/XVII Airborne Data Warfare Center, LaunchPad, AFSC/SW. Thirteen, from "over 50". |
| SBOM in *The State of DevSecOps* | `SBOM`, `bill of materials`, `BOM` | `SBOM` **not found**. `BOM` appears once, in the Glossary under Continuous Integration ("dependency/BOM checking"). The Implementation Plan has both (task 3.2, Appendix D 2.2.2). |
| Per-factory or programme budget figures | `$`, `million`, `billion`, `budget` with digits | **Not found.** Only `$500.00` (the ITAS approval-threshold complaint, §6.3) and the funding-*type* taxonomy in Table 4-1 with no amounts. |
| Any controlled study or comparison group | `control group`, `baseline` + comparison, `compared to`, `versus` | **Not found.** The word "baseline" appears often, always meaning "first measurement", never "comparator". |
| OSCAL | `OSCAL` | **Not found in either document.** Notable given the site's OSCAL thread — DoD's only DevSecOps baseline does not mention it. |

---

## Does "nobody has rigorously measured any software factory" survive?

**Yes, with one required amendment.** The claim must become *"nobody has published delivery or outcome metrics for a DoD software factory"* rather than *"no measurement exists"*.

What exists is a self-reported cultural-practice survey — 36 practitioners, 19 organisations, 41 questions, seven attributes, one of four factory categories entirely absent (footnote 11) — producing average maturity scores per factory type, which the report itself describes as something that could "**potentially** correlate… with outcomes including delivery speed, workforce retention, and user satisfaction" (§3.3, p.17). The correlation was not done. Everything resembling a delivery metric in the report (78 programmes, 75% in six months, GAO's 75–80% and four months) is cited to prior DoD and GAO publications, not generated by the study. Single-programme anecdotes (NAVSEA's 13 updates in 9 months, "20 times" in a day) have no baselines and no methodology.

More damning than anything in *The State of DevSecOps*: the Implementation Plan's own scorecard records "**Establish software factory criteria and metrics — Carryover**" and "**Collect cost data on agile software programs — Carryover**" for FY23–24. DoD set itself the task of defining software factory metrics and collecting cost data, and recorded its own failure to do either. That is a better citation than any of the four external audits, because it is the Department marking its own homework and giving itself an incomplete.

The report's own sentence to lead with: "**Organizations don't have to provide metrics for cATO effectiveness, but we are interested in potential metrics to evaluate the effectiveness of the cATO process from a DoD governance perspective.**" (§5.6, p.30)
