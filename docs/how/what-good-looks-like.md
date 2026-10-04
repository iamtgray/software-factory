# What Good Looks Like

Three standards exist to hold a real factory against: the official one, which is public, enumerated, and not actually a test; the convergent one, where commercially opposed parties agree and the agreement therefore means something; and the structural one, which falls out of the architecture whether anyone writes it down or not.

Hold a factory against all three and you get a verdict. Hold it against only the first and you get a cATO.

!!! quote "The definition to start from -- DoD Enterprise DevSecOps Fundamentals v2.5, Table 1"
    "In the DoD, a software factory is defined as a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."

Three load-bearing properties: **people, tools and processes**, not a product; measured by **continuously delivering value by deploying**, not by throughput; scoped to **one specific community of end users**. A factory that cannot name its user community fails the definition before you reach the criteria.

## 1. The official bar

The **cATO Evaluation Criteria** (29 May 2024, Distribution Statement A) is the closest thing to an official definition of a good software factory: three competencies inherited from the 2022 memo, assessed against three objects -- platform, process, people.

### The entry gates, which come before any criterion applies

1. "All the RMF steps must be followed, and the system must be in the Monitor phase of RMF, before a system can apply for a cATO."
2. A current authorisation -- the criteria "assume that before applying for a cATO, the software factory has already progressed into the monitoring phase of RMF and has a valid ATO."
3. "In order to receive an approved cATO, the software factory must have a current ATO with no 'High' or 'Very High' unmitigated findings."
4. The applicant already sits in one of two use cases: production inside the factory's own boundary, or delivery across a boundary holding its own ATO, governed by "a Memorandum of Understanding (MOU) and an Interconnection Security Agreement (ISA)."

Then three eligibility conditions, verbatim: the platform "contains essential automation to enable CONMON, ACD, and to support DevSecOps (DSO) tooling for a Secure Software Supply Chain (SSSC)"; "Processes are defined for people using, operating, and maintaining the DSOP"; "People are trained on the DSOP and its processes."

### The criteria themselves

| Competency | Named criteria | The clause that bites |
|---|---|---|
| **Continuous monitoring** | Risk management strategy with stated tolerances; CONMON strategy with implementation, effectiveness and impact measures; authorisation boundary diagram; business rules; automated monitoring information, demonstrated live; authorisation package; COOP/DRP; incident response; vulnerability management; audit log analysis; approval memo | Assessors "must have real-time access to the results of testing, scanning, monitoring, and performance metrics" |
| **Active cyber defence** | Certified cybersecurity service provider; external assessment results and remediation evidence; ongoing testing against "adversary tactics and techniques based on real-world observations" | "A penetration test must be completed on development and operational environments by a qualified third party within 90 days and annually thereafter" |
| **Supply chain -- platform** | A named approved reference design; SBOMs for the platform and for everything passing through it, archived and analysed against new CVEs; activities-and-tools mapping with a roadmap; cloud-native protection across artefacts, configuration and runtime | "Provide an automated export of the SBOM for applications/products passing through the DSOP" |
| **Supply chain -- process** | IaC and CaC against environment drift; control gate and guardrail analysis | "Provide a description of each control gate and what triggers cause the gate to close and open" |
| **Supply chain -- people** | Role-based training verification; separation of duties and least privilege; tabletop exercises with after-action reports; documented education and certification; an insider threat working group "chaired by senior leadership" | "Show evidence that all personnel have gone through the onboarding/offboarding process, without regard to their rank or position" |

The process row is two bullets. The *process* half of platform-process-people is the least specified part of the official standard.

!!! warning "The official standard is not a test"
    The criteria are framed as "guidelines", scoped as "not limited to the way they conduct the following activities", and assessed such that "the presence of these activities will be **partly determined** through demonstrated use of system-level dashboards."

    There is **no pass mark, no published scoring rubric and no published weighting.** The nearest thing to a decision rule is one sentence: "the key to receiving a cATO is having a robust continuous monitoring strategy that includes automated triggers based on approved thresholds."

    And the accepted evidence is weaker than the requirement implies: "Demonstrate each control gate in action (this may be in a non-production environment) **or provide screen shots of control gate output as displayed in a dashboard**." A PNG of a dashboard satisfies the control-gate criterion. Monitoring timelines are specified as "automated every hour, minute, second; manual once a year, etc.", with no preference stated between the two ends of that sentence.

    Necessary, insufficient, gameable. Pass it, then apply a real standard.

The strongest phrase in the document is also the one nothing in it obliges you to produce: the platform "generates, analyzes, and displays machine evidence throughout the lifecycle in near real-time." That is its only use of "machine evidence", and no format, signature or verification is attached to it anywhere -- which is the subject of [Integrity vs Inspection](../tradeoffs/integrity-vs-inspection.md).

## 2. What commercially opposed sources agree on

Where a consultancy, a platform vendor and a government say the same thing, the agreement is evidence. Where two sources share an author it is one source counted twice -- Humanitec co-authored the CNCF maturity model, so those two corroborate nothing.

Ranked by independence of agreement:

1. **Platform as a product, with a named product manager.** Six independent sources including a survey and a research programme. Settled; treat as given.
2. **Self-service without tickets.** Four unrelated sources.
3. **Reduce cognitive load by shifting *down*, not left** -- because shift-left *adds* load to the application team. Team Topologies in origin, adopted by both the CNCF model and DORA.
4. **The thinnest viable platform.** "Could be just a wiki page... don't make it any thicker than necessary."
5. **Automated, low-friction dependency updating with clear ownership.** Agreed by a commercial scanning vendor and an OpenSSF specification -- unrelated parties, and the strongest security-side finding available.
6. **Clear, actionable feedback on task outcomes.** One source, and the best-evidenced single claim available: DORA 2025 measured this as *the* platform attribute most correlated with positive user experience. It is nearly absent from every vendor maturity model, which makes it the highest-leverage item on this page. A red cross and a 4,000-line SARIF file fails it even when the finding is correct -- see [Gates vs Attention](../tradeoffs/gates-vs-attention.md).

From the defence side, where a consultancy, a vendor and a government document converge: **don't build your own platform** (see [Build vs Adopt](../tradeoffs/build-vs-adopt.md)); **control inheritance from assessed common control providers is the economic engine**; **draw the authorisation boundary tightly, at design time**; **the pipeline definition lives outside the application repo, inherited from a governed template**; **treat assessors and authorising officials as users** -- "the central delivery constraint is organisational decision confidence, not engineering capability"; **change behaviour first, culture follows**; **protect the operator feedback loop**.

## 3. What the architecture requires regardless

Four requirements fall out of the structure rather than anyone's guidance, which is why they survive disagreement about everything else. Each is a yes/no question:

- **Does the gate live somewhere the tenant cannot edit it?** A gate defined in the repository it gates is not a gate.
- **Does the pipeline definition live outside the application repo, inherited from a governed template?** If a team can change its own pipeline, the first answer is already no.
- **Are there separate signing identities per document type** -- build provenance, SBOM, scan results, VEX, test results, the verdict, the release approval? If one key signs the provenance and the verdict, a compromised build issues its own pass.
- **Does admission verify a signature and a verdict, and nothing else?** Rich policy belongs at the gate, where failure is early and cheap. Admission has a one-second budget and an unbypassable position; evaluating hermeticity inside a webhook against attestations fetched over the network is how you take a cluster down.

Reasoning for all four in [The Hand-offs](handoffs.md) and [The Five Primitives](primitives.md).

## 4. What good is not

Documented failure patterns, stated as checks:

| Pattern | What to check |
|---|---|
| **Fake production** | That the environment labelled prod is production. *"'We have 20 apps in prod' because they label an environment prod that's actually dev or test."* |
| **Teams can bypass their own gates** | Whether a tenant can edit the file that gates it. *"Developers have access to this Jenkinsfile."* |
| **Ticket-ops** | Whether self-service terminates in a queue. A vending machine with a human behind it is not a platform. |
| **The golden path as the only road** | Whether an exception route exists, is fast, and is non-punitive. Never be the only road; always be the fastest. |
| **Gates whose false positives drive suppression** | The suppression count and its trend. Peer-reviewed (FSE 2025): suppressions grow **monotonically**, **50.8% suppress nothing at all**, dead suppressions silently mask future findings, and the top cause is false positives. The honest limit: no named organisation has been shown switching a gate off. |
| **Mandated adoption, unmeasured satisfaction** | Whether satisfaction is measured independently and published next to compliance, so *"100% adoption, 30% satisfaction"* reads as failure. See [Mandate vs Adoption](../tradeoffs/mandate-vs-adoption.md). |
| **Ivory tower** | Whether teams are standing up a parallel capability. A national audit office found the mechanism in one sentence: a culture focused on the approvals process rather than outcomes *incentivised* separate capabilities over shared ones. Air-gapped, that shadow platform is a security incident. |
| **Bureaucratic re-encroachment** | Whether the user-contact budget survives year two. One documented chain: travel budget cut 75%, user-centred design collapsed, deployments fell from many per day to monthly to zero. |
| **Pilot-bounded success** | Whether the second tenant got what the first did. *"The goodness doesn't scale past the protected pilot."* |

## 5. The two metrics worth running the programme on

Everything above can be satisfied on paper by a factory nobody wants to use, because a mandate guarantees the adoption number. Two measures cannot be produced by a mandate.

**The workaround rate.** How often teams route around the factory to ship. It is the air-gapped equivalent of churn, it is measurable from the artefacts already in the registry, and it answers the counterfactual a mandate destroys -- *would* teams choose this?

**The modification rate of shared assets.** Reuse is a step function, not a gradient: it **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%** ([the measured curve, and the programme it sank](../limits/history.md)). A slot implementation every tenant forks by 40% is worse than shipping no shared asset at all -- you pay the coordination cost and collect none of the benefit.

Both need a baseline taken *before* adoption, per tenant. Nobody does this, four audits complain about its absence, and it is cheap -- which makes it the one criterion here a programme could be first at.
