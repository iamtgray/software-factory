# What good looks like

The official standard is public, enumerated and passable on screenshots. Underneath it sit a convergent standard, where commercially opposed parties agree, and a structural one that falls out of the architecture whether anyone writes it down or not. The official one on its own is enough for a cATO.

!!! quote "The definition -- DoD Enterprise DevSecOps Fundamentals v2.5, Table 1"
    "In the DoD, a software factory is defined as a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."

**People, tools and processes** puts a software factory in the category of organisation. Measured by **continuously delivering value by deploying**, and scoped to **one specific community of end users** -- so a factory that can't name its user community fails the definition before it reaches the criteria.

## 1. The official bar

The **cATO Evaluation Criteria** (29 May 2024, Distribution Statement A) is the closest thing to an official definition of a good software factory: three competencies from the 2022 memo, assessed against three objects -- platform, process, people.

### Entry gates, before any criterion applies

1. "All the RMF steps must be followed, and the system must be in the Monitor phase of RMF, before a system can apply for a cATO."
2. "In order to receive an approved cATO, the software factory must have a current ATO with no 'High' or 'Very High' unmitigated findings."
3. The applicant already sits in one of two use cases: production inside the factory's own boundary, or delivery across a boundary holding its own ATO, governed by "a Memorandum of Understanding (MOU) and an Interconnection Security Agreement (ISA)."

Then the eligibility conditions, verbatim: the platform "contains essential automation to enable CONMON, ACD, and to support DevSecOps (DSO) tooling for a Secure Software Supply Chain (SSSC)"; "Processes are defined for people using, operating, and maintaining the DSOP"; "People are trained on the DSOP and its processes."

### The criteria themselves

| Competency | Named criteria | The clause that bites |
|---|---|---|
| **Continuous monitoring** | Risk management strategy with stated tolerances; CONMON strategy with implementation, effectiveness and impact measures; boundary diagram; business rules; automated monitoring information, demonstrated live; authorisation package; COOP/DRP; incident response; vulnerability management; audit log analysis; approval memo | The authorising official and designated cybersecurity personnel "must have real-time access to the results of testing, scanning, monitoring, and performance metrics" |
| **Active cyber defence** | Certified cybersecurity service provider; external assessment results and remediation evidence; ongoing testing against "adversary tactics and techniques based on real-world observations" | "A penetration test must be completed on development and operational environments by a qualified third party within 90 days and annually thereafter" |
| **Supply chain -- platform** | A named approved reference design; SBOMs for the platform and for everything passing through it, archived and analysed against new CVEs; activities-and-tools mapping with a roadmap; cloud-native protection across artefacts, configuration and runtime | "Provide an automated export of the SBOM for applications/products passing through the DSOP" |
| **Supply chain -- process** | IaC and CaC against environment drift; control gate and guardrail analysis | "Provide a description of each control gate and what triggers cause the gate to close and open" |
| **Supply chain -- people** | Role-based training verification; separation of duties and least privilege; tabletop exercises with after-action reports; documented education and certification; an insider threat working group "chaired by senior leadership" | "Show evidence that all personnel have gone through the onboarding/offboarding process, without regard to their rank or position" |

The process row is two bullets.

!!! warning "The official standard is gameable"
    The criteria are framed as "guidelines", scoped as "not limited to the way they conduct the following activities", and assessed such that "the presence of these activities will be **partly determined** through demonstrated use of system-level dashboards."

    No pass mark, scoring rubric or published weighting appears anywhere in it. The nearest thing to a decision rule is one sentence: "the key to receiving a cATO is having a robust continuous monitoring strategy that includes automated triggers based on approved thresholds within the auditing and incident response plans."

    Accepted evidence is weaker than the requirement: "Demonstrate each control gate in action (this may be in a non-production environment) **or provide screen shots of control gate output as displayed in a dashboard**." Monitoring timelines are "automated every hour, minute, second; manual once a year, etc." -- no preference stated between the two ends of that sentence.

One phrase nothing in the document obliges you to produce: the platform "generates, analyzes, and displays machine evidence throughout the lifecycle in near real-time." That's its only use of "machine evidence", with no format, signature or verification requirement attached -- the subject of [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

## 2. What commercially opposed sources agree on

Where a consultancy, a platform vendor and a government say the same thing, the agreement is evidence. Shared authorship collapses that arithmetic: Humanitec co-authored the CNCF maturity model, so that pair is one source counted twice. Ranked by how independent the agreement is:

1. **Platform as a product, with a named product manager.** Six independent sources including a survey and a research programme.
2. **Self-service without tickets.** Four unrelated sources.
3. **Reduce cognitive load by shifting *down*: the platform absorbs work that shift-left *adds* to the application team.** Team Topologies in origin, adopted by both the CNCF model and DORA.
4. **The thinnest viable platform.** It "could be just a wiki page... don't make it any thicker than necessary."
5. **Automated, low-friction dependency updating with clear ownership.** Agreed by a commercial scanning vendor and an OpenSSF specification.
6. **Clear, actionable feedback on task outcomes.** One source: DORA 2025 measured this as *the* platform attribute most correlated with positive user experience. Absent from the vendor maturity models. A red cross and a 4,000-line SARIF file fails it even when the finding is correct ([Gates vs Attention](../tradeoffs/gates-vs-attention.md)).

From the defence side, where a consultancy and a vendor converge (and the public government position adds a cost argument, leaving the choice formally open): **don't build your own platform** (see [Build vs Adopt](../tradeoffs/build-vs-adopt.md)); **control inheritance from assessed common control providers is the economic engine**; **draw the authorisation boundary tightly, at design time**; **treat assessors and authorising officials as users** -- "the central delivery constraint is organisational decision confidence, not engineering capability"; **protect the operator feedback loop**.

## 3. What the architecture requires regardless

All yes/no questions:

- **Does the gate live somewhere the tenant cannot edit it?**
- **Does the pipeline definition live outside the application repo, inherited from a governed template?** If a team can change its own pipeline, the first answer is already no.
- **Are there separate signing identities per document type** -- provenance, SBOM, scan results, VEX, test results, the verdict, the release approval? A compromised build issues its own pass the moment one key signs both the provenance and the verdict.
- **Does admission verify a signature and a verdict, and nothing else?** Admission has a one-second budget and an unbypassable position; evaluating hermeticity inside a webhook, against attestations fetched over the network, is how you take a cluster down (see [Gates vs Attention](../tradeoffs/gates-vs-attention.md)).

Reasoning in [The Hand-offs](handoffs.md) and [The Five Primitives](primitives.md).

## 4. How factories fail

Documented patterns, each stated as a check:

| Pattern | What to check |
|---|---|
| **Fake production** | That the environment labelled prod is production. *"'We have 20 apps in prod' because they label an environment prod that's actually dev or test."* |
| **Teams can bypass their own gates** | Whether a tenant can edit the file that gates it. The failure a practitioner named directly: *"developers have access to this Jenkinsfile."* |
| **Ticket-ops** | Whether self-service terminates in a queue. |
| **The golden path as the only road** | Whether an exception route exists, is fast, and is non-punitive. |
| **Gates whose false positives drive suppression** | The suppression count and its trend. Peer-reviewed (FSE 2025): suppressions grow **monotonically**, **50.8% suppress nothing at all**, dead ones silently mask future findings, and the top cause is false positives. I haven't found a named organisation shown switching a gate off. |
| **Mandated adoption, unmeasured satisfaction** | Whether satisfaction is measured independently and published next to compliance, so *"100% adoption, 30% satisfaction"* reads as failure. See [Mandate vs Adoption](../tradeoffs/mandate-vs-adoption.md). |
| **Ivory tower** | Whether teams are standing up a parallel capability. Air-gapped, a shadow platform is a security incident, because code reaches production down a path nobody assessed. |
| **Bureaucratic re-encroachment** | Whether the user-contact budget survives year two. One documented chain: travel budget cut 75%, user-centred design collapsed, deployments fell from many per day to monthly to zero. |
| **Pilot-bounded success** | Whether the second tenant got what the first did. *"The goodness doesn't scale past the protected pilot."* |

## 5. The metrics to run the programme on

Everything above can be satisfied on paper by a factory nobody wants to use, because a mandate guarantees the adoption number.

**The workaround rate.** How often teams route around the factory to ship. The air-gapped equivalent of churn, measurable from the artefacts already in the registry, and it answers the counterfactual a mandate destroys: whether teams would choose this.

**The modification rate of shared assets.** Reuse behaves as a step function: it **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%** ([the measured curve, and the programme it sank](../limits/history.md)). A slot implementation every tenant forks by 40% is worse than shipping no shared asset -- you pay the coordination cost and collect none of the benefit.

Both need a per-tenant baseline taken *before* adoption. I haven't found a programme that does this, and four audits complain about its absence.

For a programme standing up now: what's the baseline, and how long before the mandate lands and makes it unobtainable?
