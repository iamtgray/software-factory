# 12 — DoD primaries: cATO Evaluation Criteria, Continuous Authorization Implementation Guide, Software Modernization Strategy

Sources read in full (local cache, text-extraction proxy output):

| # | File | Document | Date | Distribution |
|---|---|---|---|---|
| 02 | `sources/dod/02-cato-evaluation-criteria.md` | Continuous Authorization to Operate (cATO) Evaluation Criteria — DevSecOps Use Case, 19 pp. | 29 May 2024 | **STATEMENT A** — approved for public release, distribution unlimited |
| 03 | `sources/dod/03-continuous-authorization-impl-guide.md` | DevSecOps Continuous Authorization Implementation Guide, DoD CIO, v1.0, 26 pp. (author: Mark Smiley, Ph.D.) | March 2024 (changelog: 21 Mar 2024) | **STATEMENT C** — US Government agencies and their contractors only |
| 07 | `sources/dod/07-software-mod-strategy.md` | Department of Defense Software Modernization Strategy, v1.0, 14 pp., with DepSecDef cover memo | Strategy Nov 2021; memo 1 Feb 2022 | Unclassified, public |

Cross-checked against `sources/dod/04-cato-memo.md` (the signed 3 Feb 2022 cATO memo) where the three documents are silent.

---

## 1. Corrections to the site

**C1 — The Implementation Guide is DISTRIBUTION STATEMENT C, not public release.** Verbatim, p. i: *"DISTRIBUTION STATEMENT C. Distribution authorized to U.S. Government Agencies and their contractors; Administrative or Operational Use. Other requests for this document shall be referred to the Department of the DoD Chief Information Officer."* The Evaluation Criteria (Statement A) and the Software Modernization Strategy (unclassified, public) are both freely quotable. The Implementation Guide is not. Everything the site most wants from it — Appendix B, Table 2, the "collect evidence" sentence — is inside the restricted document. Recommend the site cite the Evaluation Criteria and the Strategy for load-bearing claims and treat the Implementation Guide as corroboration only, or seek a release determination. This is the single most consequential finding for publication.

**C2 — Document 07 is a DoD document, not a DoW document.** The brief described it as the "DoW Software Modernization Strategy". The artefact is titled *Department of Defense Software Modernization Strategy*, November 2021, Version 1.0, transmitted by a Deputy Secretary of Defense memorandum dated 1 Feb 2022 ("SUBJECT: Department of Defense Software Modernization"). The Department of War renaming postdates it by three and a half years. Any citation styling it "DoW" is an anachronism. (The proxy's `Published Time: Thu, 03 Feb 2022` is the PDF's web-publication timestamp, not the document date.)

**C3 — The dashboard requirement was *weakened* between the memo and the Evaluation Criteria, and the site should know it.** The signed memo (04, line 26) says *"For cATO, **all** security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism for AOs to view the environment."* The Evaluation Criteria (02, Appendix D §1.0, p. 11) reissues the same clause as: *"Demonstrate **which** security controls are fed into a system-level dashboard view, providing a real time and robust mechanism for AOs to view the environment."* "All" became "which". The 2024 implementing criteria ask an applicant to show the *subset* that reaches the dashboard — not to assert universal coverage. If the site uses the memo's "all security controls" as its policy ceiling, it must disclose that the operative evaluation criteria no longer require "all". This is an argument *for* the site's broader thesis (policy intent outran implementation) but it means the memo quote cannot be presented as the current standard.

**C4 — The memo itself licenses manual controls, so the policy does not uniformly "demand continuous machine-verifiable evidence".** 04, line 22: *"Automated monitoring should be as near real time as feasible. Manual controls will have different timelines associated, but must be included in the overall monitoring strategy."* The Evaluation Criteria operationalises exactly that (see §7B below, "automated every hour, minute, second; manual once a year"). The honest framing is that the policy demands *continuous risk visibility*, mandates automation *where feasible*, and explicitly accommodates manual controls — not that it mandates machine-verifiable evidence throughout.

**C5 — The "three competencies" are renamed in the Evaluation Criteria.** The memo's third competency is *"the adoption and use of an approved DevSecOps reference design"*. The Evaluation Criteria's Appendix D heading 3.0 is *"Secure Software Supply Chain (SSSC) and DevSecOps"*, and Appendix C explicitly reconciles the two sets of concepts (p. 9). The Implementation Guide (p. 2) lists the memo's three and then adds: *"In addition, the cATO memo calls out the need for a Secure Software Supply Chain (SSSC) and relates that to the third competency."* If the site enumerates competencies, it should use the memo's wording and note the recasting, not blend them.

**C6 — Two extraction losses limit what can be claimed as verbatim.** (a) **Bold formatting did not survive.** The Evaluation Criteria states (p. 10): *"Items in bold in this section indicate documents or artifacts that must be delivered as part of the application for cATO package."* Zero bold markers survived in the cached markdown (`grep -c '\*\*'` = 0). The list of *mandatory deliverables* therefore **cannot be reconstructed** from this cache — only the full candidate list below. Do not assert which Appendix D items are mandatory without re-reading the PDF. (b) **Figures and one table are images and did not extract.** Figures 1–5 of the Evaluation Criteria and Figures 1–4 of the Implementation Guide are absent; Implementation Guide **Table 1** (cATO Memo Competencies Assessment Crosswalk, p. 7) extracted as an empty shell. Fortunately the *same* crosswalk flattened into readable text in the Evaluation Criteria as Figure 5 (see §3A), so the content is recovered from the public document.

**Verified without correction:** the DoD CISO approval claim (§4), the "modifies requirements for re-authorizing" claim (§5, with an attribution caveat), and the verbatim "pipeline and process-generated evidence" quote (§6).

---

## 2. The Evaluation Criteria in full structure

The Evaluation Criteria is the closest thing to an official DoD definition of a *good software factory*. Its architecture is two-layered and that layering matters: a **three-competency** frame inherited from the memo, mapped onto a **three-object** assessment (Platform, Process, People).

### 2A. The gating preconditions (before any criterion applies)

Four hard gates, all from document 02:

1. *"All the RMF steps must be followed, and the system must be in the Monitor phase of RMF, before a system can apply for a cATO."* (p. 6, note to Figure 3)
2. *"This assumes that before applying for a cATO, the software factory has already progressed into the monitoring phase of RMF and has a valid ATO."* (Appendix B, p. 7)
3. *"In order to receive an approved cATO, the software factory must have a current ATO with no 'High' or 'Very High' unmitigated findings."* (p. 8)
4. The applicant must already sit in Use Case 1 or Use Case 2 (Appendix A, pp. 5–6): *"Programs or software factories applying for a DSO cATO should already be in one of the following use case categories."*
   - **Use Case 1 (inside the software factory boundary):** DevSecOps platform already has an ATO; software is developed and deployed within its own system boundary; the factory seeks a cATO covering its production environment. *"This is the main use case for a SWF leveraging cATO. Example: Software developed and put into production using the Platform One (P1) Party Bus."*
   - **Use Case 2 (outside the SWF boundary):** deployment into a separate authorisation boundary with its own ATO. *"This involves at least two authorization boundaries and there must be agreements in place to pass software across the boundary and subsequently pass results and feedback back to the software factory. Example: The Forge Software Factory has an ATO to build software that is then deployed on Navy ships, each of which have their own ATOs."* Outcome mechanism: *"through a Memorandum of Understanding (MOU) and an Interconnection Security Agreement (ISA)."*

### 2B. The three conditions of eligibility (Appendix C, p. 9)

*"To be considered for cATO, the environment must ensure:*
*1) The DevSecOps Platform (DSOP) contains essential automation to enable CONMON, ACD, and to support DevSecOps (DSO) tooling for a Secure Software Supply Chain (SSSC).*
*2) Processes are defined for people using, operating, and maintaining the DSOP.*
*3) People are trained on the DSOP and its processes."*

And the scope: *"The cATO applies to the software factory, which includes the DSOP, and the software produced by the software factory."*

### 2C. The criteria themselves — Appendix D, enumerated

Framing sentences, p. 10, verbatim and important:

> *"The following list of activities associated with the Continuous Authorization to Operate (cATO) competencies are what the DoD CISO considers when Component CISOs present systems that are requesting to move into a cATO state."*
>
> *"The presence of these activities will be partly determined through demonstrated use of system-level dashboards, which are a culmination of information received from logging, testing, and the following activities to provide a real-time view of the environment. Components are not limited to the way they conduct the following activities; however, this document offers guidelines to achieving a cATO."*
>
> *"Items in bold in this section indicate documents or artifacts that must be delivered as part of the application for cATO package."*

Note "guidelines", "not limited to", and "partly determined" — this is a guideline set assessed by judgement, not a conformance checklist. (The Implementation Guide says the same of its own table: *"The intent is not to say that all these practices need to be implemented, such as in a conformance checklist"*, p. 15.)

---

#### 1.0 Continuous Monitoring (pp. 10–13)

Nine top-level criteria:

**1. cATO Risk Management Strategy**
- Must include established cATO risk tolerances based on the Components' risk posture guidance
- Must include process, management, and tracking of insider and external threats
- IAW DoDI 8510.01

**2. System CONMON Strategy**
- Will be assessed IAW organizational Risk Management Strategy
- Includes plan to continuously assess and track vulnerabilities on all the system assets within the infrastructure
- Includes determination of organizationally or software factory-specified metrics (measures) to establish patterns and discern threats: *implementation measures* (execution of security policy), *effectiveness/efficiency measures* (results of security services delivery), *impact measures* (business or mission consequences of security events)
- *"Includes timelines for continuous monitoring of security controls (automated every hour, minute, second; manual once a year, etc.)"*
- Includes tight coupling with auditing and incident response strategies

**3. System Authorization Boundary Diagram**
- Include data flows (including PII)
- Include detailed information for all external connections IAW Appendix E Diagram Requirements of the DISA Connection Process Guide

**4. Business Rules** — *"examples of the type of business rules to be established by the system"*:
- Closely involve DoDM 8140.03-certified cybersecurity experts throughout the life of the program
- Define and assign cybersecurity roles and responsibilities
- Identify and retain SMEs to ensure the cybersecurity risk posture is maintained during operations
- Establish a vulnerability coordination Point of Contact
- Align staffing to address detected and identified vulnerabilities
- *"AO and designated cybersecurity personnel must have real-time access to the results of testing, scanning, monitoring, and performance metrics at the platform or application level in a mutually agreeable format (i.e., dashboards, alerts, etc.)"*
- *"Identify, assess, prioritize, and share risk information in real time"*
- *"Identify risks in real time and initiate corrective action plans to mitigate them"*

**5. Automated Monitoring Information** — the densest criterion for the site's thesis:
- Status of dashboarding activities, including a demonstration of the dashboard in operation
- *"Must be readily available and as near real time as feasible"*
- *"Includes a dashboard with relevant current information and requirements that helps security personnel perform their tasks"*
- *"Must provide compliance reporting statistics to the Continuous Monitoring & Risk Scoring (CMRS) system of record via automated processes if possible. If not possible, manual reporting is required until automated process is developed."*
- Includes an alerting capability that contacts security personnel when appropriate
- *"Demonstrate which security controls are fed into a system-level dashboard view, providing a real time and robust mechanism for AOs to view the environment"*
- *"Helps secure the software supply chain, the software development pipeline and its environment must be monitored as well"*

**6. System Authorization Package Documentation** (leveraged from the Component's RMF Inventory Tool) — Security Assessment Plan (SAP); Security Assessment Report (SAR); Risk Assessment Report (RAR); System Security Plan (SSP); ATO memo (signed); Plan of Action and Milestones (POA&Ms); *"Update documents in response to CONMON process"*. The nested **Security Assessment** must *"cover the DSOP supporting full lifecycle, including the delivery pipeline"* and address: threat modelling and vulnerability analysis; independent verification of assessment plans and evidence; penetration testing; attack surface reviews; **manual code reviews**; verifying the scope of T&E; SAST; DAST; IAST.

**7. Continuity of Operations Plan (COOP) / Disaster Recovery Plan (DRP)** — evidence of COOP/DRP testing (read-throughs, walk-throughs, simulations; backup activities; restoration plan).

**8. Incident Response Plan** — Incident Response Management; evidence of a programme in place including policies, plans, procedures, defined roles, training, proof of communication efforts; examples of evidence include read-throughs, walk-throughs, simulations, tabletop exercise; capabilities to detect and respond to attackers (behaviour monitoring evidence; intrusion detection/prevention systems evidence).

**9. Continuous Vulnerability Management Documentation**
- Evidence of mitigation: published expectations and timelines for corrective action plans and remediation efforts; published plan to ensure availability of staff and resources; findings tracked using Deficiency Reports and system-level POA&Ms
- Vulnerability scanning procedures IAW DoDI 8530.01
- *"Leverage process and automation to enable identification of highest priority items and vulnerabilities to remediate (verified through documentation and demonstration)"*
- Monitor for new threat and vulnerability information IAW DoD and Component level ISCM strategies. *"Critical and moderate vulnerabilities are documented upon discovery and mitigated within a timeframe acceptable to the AO"*

**10. Audit log analysis**
- Collect, analyse, alert, review, and retain audit logs IAW NIST SP 800-53 security controls
- Evaluation of events that could help detect, understand, or recover from an attack, as described in Appendix A of OMB M-21-31

**11. cATO Approval Memo** (located on the RMF Knowledge Service)
- *"While cATO approval authority resides with the DoD CISO, this template will be filled out by the cATO Assessment Methodology Working Group and submitted with the Components' cATO package"*

#### 2.0 Active Cyber Defense (pp. 13–14)

Three top-level criteria:

**1. Certified Cybersecurity Service Provider (CSSP)** — IAW DoDI 8530.01, meeting the Evaluator's Scoring Metrics requirements; *External* CSSP Service Level Agreement for both on-premises and cloud systems; *Internal* documentation of methodology supporting ACD; *Inherited* agreements/documentation where integration occurs; outline scope and parameters of CSSP support; employ CSSP sensors and tools to detect vulnerabilities; *"Provide evidence that CSSP received training on DevSecOps principles for the Software Factories that are being monitored"*.

**2. External Assessment Results and Remediation Evidence** — *"A penetration test must be completed on development and operational environments by a qualified third party within 90 days and annually thereafter, with one of the following options, per the AO:"* Cyber Operations Rapid Assessment (CORA); Red/Blue Team assessment; Pen Testing; *"Exception-to-Policy is required for any other type of assessment"*. Focus areas include testing effectiveness and resiliency of enterprise assets (people, processes, and technology) and testing the authorisation boundary IAW DoDI 8531.01. Deliverables: a Vulnerability and Penetration Assessment; AO-provided results with findings and planned mitigations; updated POA&Ms; Lessons Learned tracking.

**3. Security Testing and Documentation** — *"Security testing should be conducted on an ongoing basis and test against adversary tactics and techniques based on real-world observations"*; strategy and budget for automated cybersecurity testing resources; documentation of the ongoing iterations of cybersecurity analysis and penetration testing; documentation and evaluation of the impact of system or environment changes to the cybersecurity defence posture.

#### 3.0 Secure Software Supply Chain (SSSC) and DevSecOps (pp. 14–17)

##### 3.1 Authorize the DevSecOps Platform (p. 14–15)

**1. Use of a DSOP that implements an approved DevSecOps Reference Design, or implementation of an approved DevSecOps Reference Design** — identify the Reference Design to which the DSOP adheres; approved DoD Enterprise DevSecOps Reference Designs are posted to the DoD CIO public library.

**2. Software Bill of Materials (SBOM)**
- *"Provide a SBOM for the DSOP with a statement of how it was developed"*
- *"Provide an automated export of the SBOM for applications/products passing through the DSOP"*
- *"Specify the SBOM format and how often it is generated"*; *"SBOM should be in one of the common formats"*: SPDX, SWID, CycloneDX
- *"However, the format has not yet been mandated. SBOM is currently undergoing regulatory action, Defense Information Systems Agency (DISA) Federal Acquisition Regulation (FAR) is the lead"*
- *"Maintain an archive of SBOMs for products passing through pipelines. This can be kept in the same area as the assessment evidence (e.g., results of security tests) for the products"*
- *"Explain how the SBOMs are analyzed. If a new cybersecurity vulnerability appears in the Common Vulnerabilities and Exposures (CVE®) system, explain how the organization applies it to the SBOMs"*

**3. Activities and Tools Mapping** — based on the *DevSecOps Activities and Tools Guidebook*, provide the mapping of required and preferred DevSecOps activities to the system's implementation; include any additional documentation listed with the mapped activities; provide Activities and Tools Mapping POA&Ms/Roadmap to show continuous improvement; provide demonstration of various activities (selected activities determined during the cATO evaluation).

**4. Cloud Native Application Protection Platform (CNAPP)** — *"Employ an integrated set of security and compliance capabilities to secure and protect cloud-native applications across development and production"*:
- *Artifact Scanning:* Software Composition Analysis to review artefacts to find open-source libraries included (*"This should be addressed in the creation of the SBOMs"*); Application Security Testing such as SAST, DAST, and IAST
- *Cloud Configuration:* Cloud Security Posture Management (CSPM) for continuous monitoring, detection, and remediation of cloud security misconfigurations; Cloud Infrastructure Entitlement Management (CIEM); Infrastructure as Code (IaC) Scanning *"to find security flaws before pushing to production"*
- *Runtime Protection:* Cloud Workload Protection (CWPP) for runtime enforcement; Cloud Detection and Response (CDR)

Related mandate from p. 7: *"Hosting an environment (development, test, staging, production, etc.) on a cloud requires the deployment of a Cloud Native Application Protection Platform (CNAPP)."*

##### 3.2 Authorize the Process (pp. 15–16)

**1.** *"Reliance on Infrastructure as Code (IaC) and Configuration as Code (CaC) to avoid environment drift"*

**2. Control Gate and Guardrail Analysis**
- These processes should be described in the Incident Response Management section
- *"Provide a description of each control gate and what triggers cause the gate to close and open. This should include what triggers an alert and how to respond to that alert"*
- *"Demonstrate each control gate in action (this may be in a non-production environment) or provide screen shots of control gate output as displayed in a dashboard"*
- *"Provide a description of each guardrail and the process that occurs when something is out of the risk tolerance for each guardrail"*

Note how thin 3.2 is: two bullets. The *process* half of "Platform, Process, People" is the least specified part of the criteria.

##### 3.3 Authorize the People (pp. 16–17)

**1. Verification of appropriate training for each member of the team(s), based on their role(s)** — organisation chart showing the roles within the DSO Team; demonstrate appropriate separation of duties and least privilege applied to all personnel; *"Periodically conduct Tabletop Exercises with the whole team and produce After Action Reports"* covering security incident response procedures, standard procedures for the DSOP including how to respond when a control gate triggers, how to respond to a security alert, and requests for elevated privileges.

**2. The organizational DevSecOps education, certification, and training process is documented** — *"Documentation need not be text documents but may be in online learning management tools that assessors can view."* Possible areas: Agile, DevSecOps, secure coding, security automation tools, interpreting vulnerability scanning reports, cATO method. Team members trained in the cATO method:
- Trained on the appropriate version of the DoD Enterprise DevSecOps Reference Design
- Trained on the security automation tools and how they are used
- Trained on the CI/CD control gates, promotion rules, and the established risk tolerances
- Trained on the resolution/adjudication of security findings that result in exceeding the risk tolerances
- Ability to perform root cause analysis of "critical" and "substantive" security findings
- Trained in continuous monitoring feedback loops for ensuring continuous risk monitoring against tolerances
- Trained in the establishment of POA&M and security dashboard monitoring in a DevSecOps environment

Plus verification per role on the Product/Application Team, DSOP Team, or Security Team; verification of cybersecurity team member qualifications IAW DoDM 8140.03; document cross-functional team training and shadowing.

**3. Insider Threat Monitoring** — *"Validate an insider threat working group is established, active, and chaired by senior leadership"*; the group identifies critical areas for review along with thresholds for analysis. Protective concepts: separation of duties, paired programming, least privilege management with respect to containers/cloud environments.

**4. Onboarding/Offboarding** — a process defined for new team members based on role; *"Show evidence that all personnel have gone through the onboarding/offboarding process, without regard to their rank or position."*

### 2D. The assessment method (Appendix B, p. 7, and Figure 4)

Eight chevrons, recovered from the flattened Figure 4: **Identify Assessors → Develop Assessment Plan → Assess DevSecOps Platform → Assess Teams → Assess Processes → Develop cATO Authorization Recommendation → Authorize cATO → Monitor Risk**, mapped to RMF *Prepare / Assess / Authorize / Monitor*. Sub-activities as extracted: identify skills, train on method, identify activities, develop schedule, identify costs; identify critical cATO practices, develop eval criteria and scoring, coordinate with PMO, coordinate with AO; review key practices, review evidence of use, interview personnel, score against eval criteria, capture findings; aggregate findings, roll up scores, develop recommendation, identify constraints; review with PMO, review with AO, review with CISO, CISO issues authorization; continuous monitoring, alert/action triggered if issue found, alert may trigger a cATO review, if review triggered the CISO decides if cATO is revoked.

The operative monitoring-and-revocation sentence (p. 8): *"Upon identification of an issue or anomaly, the CSSP, along with the Security Control Assessor (SCA), shall investigate and mitigate as necessary. If the issue or anomaly is outside of agreed upon thresholds, the CSSP or SCA in collaboration with the Authorizing Official (AO) may initiate a review of the cATO. If so, the CISO may decide to revoke the cATO. However, with the approval of the originating Component authorizing official, the system can revert to its original ATO by kicking off a new workflow in the Component's RMF Inventory Tool, if the cATO is revoked."*

Also p. 7, the actual key to approval: *"However, the key to receiving a cATO is having a robust continuous monitoring strategy that includes automated triggers based on approved thresholds within the auditing and incident response plans. The automated triggers and approved thresholds should include both internal and external threats."*

Governing authorities (p. 8): *"The approval to implement cATO process within a DevSecOps software factory is granted by following the RMF guidelines identified in CNSSI 1253, NIST SP 800-53 and DoDI 8510.01."* Supply chain: *"validate that they are following cybersecurity supply chain risk management guidance in accordance with NIST SP 800-161r1."*

### 3A. The competency/assessment crosswalk (Figure 5, p. 9) — recovered

The figure flattened into text. Reconstructed as a 3×3 grid (rows = assessment objects, columns = memo competencies):

| | SSSC & DevSecOps | Active Cyber Defense | CONMON |
|---|---|---|---|
| **DSOP** | *"Automation to secure the supply chain, enforce policy, and enable control gates"* | *"Automation generates evidence and alerts; automatically kills bad containers; CSSP integrated with DSOP team"* | *"Generates, analyzes, and displays machine evidence throughout the lifecycle in near real-time"* |
| **Process** | *"DSOP engineering to monitor and improve practices"* | *"Ongoing active cyber testing, including incident response"* | *"CONMON process regularly validated and tested"* |
| **People** | *"Cyber dashboard collects relevant information for all DSO stages; all staff trained on DSO process"* | *"Team understands active cyber artifacts and approach to defend; CSSP integrated into team"* | *"Team trained on CONMON automation and DSOP alerts generated by the software factory"* |

Caveat: the row/column assignment is my reconstruction from a flattened figure; the cell text is verbatim. The DSOP/CONMON cell — *"Generates, analyzes, and displays machine evidence throughout the lifecycle in near real-time"* — is the strongest single phrase in the public document for the site's thesis, and the only instance of "machine evidence" in it.

---

## 3. Appendix B of the Implementation Guide — FOUND

**Appendix B is present and complete in the cached text.** It is titled **"Appendix B. Requirements"** (pp. 15–18) and its substance is **Table 2: cATO Requirements** — 44 numbered practices in seven families, each tagged **T** (threshold) or **O** (objective). Reminder: document 03 is DISTRIBUTION STATEMENT C.

The governing definitions, verbatim (p. 15):

> *"This section summarizes the requirements to assess for a cATO. The intent is to provide an abstraction of the practices to provide flexibility to implementing organizations. It also indicates which requirements are threshold (T) and which are objective (O). **A threshold requirement must be met, while an objective requirement is one that should be met, but which may not be fully met initially, while still obtaining a cATO.**"*

> *"Table 2 is a list of continuous risk management practices for cATO. **The intent is not to say that all these practices need to be implemented, such as in a conformance checklist**, but rather organizations typically use these types of practices for continuously managing their risk. An organization could leverage this table for identifying which practices are necessary for their cATO implementation and the assessors would review this implementation to determine its effectiveness."*

> *"The practices ensure continuous risk management, continuous security education and training of DevSecOps teams, and are supported by a DSOP that provides the underpinnings of zero-trust with a software factory."*

### Table 2 in full (44 rows)

**IC — Key cATO Processes and Practices: Information capture practices**

| ID | Description | Level |
|---|---|---|
| IC01 | Capture mission essential functions, and their supporting assets and data. | T |
| IC02 | Identify and capture risk tolerances and thresholds based on an understanding of the criticality of mission, systems, and key system parameters for cybersecurity, cyber resiliency, and cyber survivability. | T |
| IC03 | Identify cyber threats to network and data architecture, assets supporting essential mission functions and cybersecurity architecture. | T |
| IC04 | Collect evidence for establishing a baseline risk posture. | T |

**RA — Reduce the Attack Surface**

| ID | Description | Level |
|---|---|---|
| RA01 | Leverage DSOP Zero Trust with both ingress/egress and east/west traffic enforcement. | T |
| RA02 | Leverage a Cloud Native Access Point or Boundary Cloud Access Point. | T |

**SA — Security Automation risk determination practices**

| ID | Description | Level |
|---|---|---|
| SA01 | Adjudicate findings, including false positives capture and analysis. | T |
| SA02 | Set guardrail thresholds, control gate risk acceptance tolerances, and notification thresholds. | T |
| SA03 | **Automate security control configurations and validation.** | **O** |
| SA04 | Perform security scanning: dependency analysis, static and dynamic application analysis, prioritizing method, and adjudication. | T |
| SA05 | Perform pen-testing and threat emulation: threat modeling, pen-testing methods, and assets. | T |
| SA06 | Perform risk assessments: mission based, threat based, resiliency / survivability based. | T |
| SA07 | Perform verification and validation testing of cybersecurity, cyber resiliency, cyber survivability requirements. | T |
| SA08 | Perform configuration management of system and control configurations. | T |
| SA09 | Perform Security control mitigation effectiveness testing and analysis. | T |
| SA10 | **Capture, visualize, and provide feedback on security findings during pipeline runs.** | **T** |

**CM — Continuous Monitoring practices**

| ID | Description | Level |
|---|---|---|
| CM01 | Continuously monitor behavior and implement / improve proactive preventive / resiliency capabilities. | O |
| CM02 | Establish event triggers: on findings / risk tolerances / change in threat / mitigation effectiveness. | T |
| CM03 | **Provide availability of findings, plan of action, security posture, and residual risk through DevSecOps dashboards.** | **T** |
| CM04 | Monitor for change in the threat landscape. | O |
| CM05 | Monitor for change in secure configurations. | T |
| CM06 | Monitor control compliance and continued effectiveness of controls against the changing threat. | T |
| CM07 | Establish metrics: identification, collection, and trend analysis. | T |

**RM — Continuous Risk Management practices**

| ID | Description | Level |
|---|---|---|
| RM01 | Establish or assign a group for managing risks. Should include designated AO representative, development security team, DSOP security team, and mission owners. | T |
| RM02 | Establish a method for aggregating findings into a risk posture on cybersecurity, cyber resiliency, and cyber survivability. | T |
| RM03 | Identify vulnerabilities and perform impact analysis for establishing risk prioritization. | T |
| RM04 | Establish a dashboard visualization of risk information for continuous review. | T |
| RM05 | **Establish periodic reviews of risk and risk remediation / adjudication.** Establish approach for ad-hoc resolution of risks that exceed thresholds. | T |
| RM06 | Monitor and respond to security posture, status of metrics, change in threat, and effectiveness of controls. | O |

**PP — DSOP cATO practices** (header verbatim: *"for a DSOP that already has an authorization; many of these practices will be inherited by the team responsible for cATO"*)

| ID | Description | Level |
|---|---|---|
| PP01 | Compliance with capabilities and practices listed in the DevSecOps Fundamentals Guidebook: DevSecOps Tools & Activities [5] and in one of the DoD Enterprise DevSecOps Reference Designs (RD), such as: the DoD Enterprise DevSecOps Reference Design: CNCF Kubernetes [6]. | **O** |
| PP02 | Implement zero-trust and boundary access point. | T |
| PP03 | Establish a SOC continuous monitoring strategy using the Software Factory. | O |
| PP04 | Establish CSSP application monitoring for non-approved or malicious actions. | T |
| PP05 | Configure the security sidecar for unique application traffic inspection and handling events. | T |
| PP06 | **Identify application control inheritance from the DSOP using a shared security model.** | **T** |
| PP07 | Establish the use of security automation for monitoring the application security posture hosted on the DSOP. | T |
| PP08 | Implement agreed-to risk tolerances in the pipeline guardrails and control gates with event trigger routing. | T |
| PP09 | Establish a cyber operations feedback loop and review of application incidents in collaboration with the program office DevSecOps team. | O |
| PP10 | Visualize the security posture of the application and the DSOP on a dashboard. | T |

**TP — Organization's development, security, and assessor Team Practices**

| ID | Description | Level |
|---|---|---|
| TP01 | Establish an organizational DevSecOps position education, certification, and training process. | T |
| TP02 | Establish hiring position descriptions and certification requirements in line with the DoD Cyber Workforce Framework (DCWF). | O |
| TP03 | Establish a training compliance / validation process to ensure team members meet cybersecurity education, certification, and training requirements. | T |
| TP04 | Ensure that members of the team have experience in developing secure applications, working in a DevSecOps culture, and assessing security practices. | O |
| TP05 | Train team members in the cATO method and practices. | T |
| TP06 | Identify cultural change challenges and the change management approach. | T |
| TP07 | Expand the use of (specialized) training programs for senior technology leaders and project managers on software modernization and cATO methods and practices. | T |
| TP08 | Train the team in performing threat actor analysis, mitigation practices, developing secure code, security automation, determining mitigation effectiveness, the software factory, continuous monitoring, and risk management. | O |

Tally: 44 requirements, 33 threshold, 11 objective.

### Why Appendix B is the most important finding in document 03

**Two rows, read together, are the sharpest evidence *against* the site's strong thesis:**

- **SA03 "Automate security control configurations and validation" is an OBJECTIVE (O)** — i.e. *"should be met, but which may not be fully met initially, while still obtaining a cATO."* The one requirement that most directly says "make control validation a machine operation" is explicitly not mandatory.
- **PP01, compliance with the DevSecOps Fundamentals Guidebook and a Reference Design, is also an OBJECTIVE (O)** — even though the memo's third competency is *"the adoption and use of an approved DevSecOps reference design"*. The Implementation Guide downgrades the memo's own third competency to an aspiration. Note the direct conflict with the Evaluation Criteria §3.1, which lists Reference Design adherence as a flat requirement. The two 2024 documents disagree.

**And the rows most *supportive* of the thesis, both threshold:**

- **SA10 "Capture, visualize, and provide feedback on security findings during pipeline runs" (T)** — evidence generated *by the pipeline run*.
- **CM03 "Provide availability of findings, plan of action, security posture, and residual risk through DevSecOps dashboards" (T)** — the POA&M itself, a classically document-shaped artefact, is required to be *available through a dashboard*. This is the closest the corpus comes to saying "the document becomes a view over live data".
- **IC04 "Collect evidence for establishing a baseline risk posture" (T)**, **RM04 dashboard visualisation (T)**, **PP10 visualise on a dashboard (T)**.

---

## 4. Who approves a cATO, and at what level — VERIFIED

The site's claim stands. Three mutually reinforcing statements in the Evaluation Criteria (29 May 2024):

1. **The footnote the site cites.** Footnote 1, p. 8, attached to the sentence *"Once the Chief Information Security Officer (CISO)¹ grants a cATO, continuous monitoring practices (including the CSSP) monitor the risk"*:

   > **¹** *"Currently, this level of authority is at the DoD-level. Once cATO criteria is standardized for the DevSecOps use case, the DoD CISO will delegate approval authority to the Component CISO or equivalent."*

2. **Appendix D §1.0, p. 13:** *"While cATO approval authority resides with the DoD CISO, this template will be filled out by the cATO Assessment Methodology Working Group and submitted with the Components' cATO package"*

3. **Appendix D framing, p. 10:** *"The following list of activities ... are what the DoD CISO considers when Component CISOs present systems that are requesting to move into a cATO state."*

Plus the process route, p. 3: packages are *"send[t] to DCIO(CS) for review and approval"* (Deputy CIO for Cybersecurity), and the Figure 4 chevron sequence ends *"Review with CISO / CISO Issues authorization"*. The memo (04, line 49) sets the same route: *"the AO will notify the component CISO ... Together the AO and component CISO will present this request and the supporting body of evidence to the DoD CISO for consideration."*

**Arithmetic on "27 months".** Memo signed 3 Feb 2022; Evaluation Criteria dated 29 May 2024. That is 27 months and 26 days — so "27 months" is correct as a floor and the site is safe saying "more than 27 months" or "over two years". Delegation to Component CISOs was still *prospective* at that date, conditioned on *"Once cATO criteria is standardized for the DevSecOps use case"*. Department-wide, single-office approval: confirmed.

**One nuance to hold.** The Implementation Guide (March 2024, two months earlier) repeatedly frames the decision as the **AO's**: *"That document lists activities and documentation to be evaluated by the cATO Authorizing Official"* (p. 3); *"Provide a final organizational readiness risk determination and recommendation for the AO to consider, using an AO cATO decision briefing, including all conditions of the authorization"* (p. 6); *"the AO will approve the assessment team and their capabilities as part of the authorization process"* (p. 5). The word CISO does not appear in document 03 at all. The two 2024 documents are not aligned on who signs. The Evaluation Criteria is the later, Statement A, authority-bearing document and should be cited for the DoD CISO claim; the discrepancy is itself usable evidence that the approval pathway was unsettled.

---

## 5. "It modifies re-authorisation" — substance VERIFIED, phrase NOT in these three documents

**The quoted phrase is not in any of the three documents.** `grep -i "re-authoriz|reauthoriz"` returns 0 in all three. It is from the **signed memo**, which the site must cite for it (04-cato-memo.md, line 51):

> *"DoD CISO approved cATOs do not have an expiration date and will remain in effect as long as the required real time risk posture is maintained. **The cATO determination does not affect the underlying system ATO. Rather, it modifies requirements for re-authorizing that system's ATO.** cATOs are a privilege and represent the gold standard for cybersecurity risk management for systems. They represent a raise the bar effort for system risk monitoring and management."*

If the site attributes this to the Evaluation Criteria it should be corrected to the memo.

**The three documents fully corroborate the substance — cATO is not a route *to* authorisation** — in four operative sentences, the clearest being the Implementation Guide's:

> *"**Systems seeking a cATO must have already achieved an Authorization to Operate (ATO) and have entered the Risk Management Framework (RMF) monitor stage.**"* — document 03, p. 2, first line under "What is Continuous Authorization?"

That is the single cleanest sentence for the point. The publicly citable equivalents, from document 02:

- *"All the RMF steps must be followed, and the system must be in the Monitor phase of RMF, before a system can apply for a cATO."* (p. 6)
- *"This assumes that before applying for a cATO, the software factory has already progressed into the monitoring phase of RMF and has a valid ATO."* (p. 7)
- *"In order to receive an approved cATO, the software factory must have a current ATO with no 'High' or 'Very High' unmitigated findings."* (p. 8)

And the reversion mechanism, p. 8: *"with the approval of the originating Component authorizing official, the system can revert to its original ATO ... if the cATO is revoked."* The ATO persists underneath throughout; cATO is a state layered on it.

**Related: cATO is a *superset* of an existing, unused RMF concept.** Document 03, p. 2:

> *"A cATO is a superset of the National Institute of Standards and Technology (NIST) Risk Management Framework (RMF) term ongoing authorization ... **which has existed for years but lacked the automation to make it effective across a broad community.** Continuous authorization for DevSecOps includes additional aspects, such as assessing the team and a DevSecOps Platform for supporting continuous risk monitoring."*

That sentence is a gift to the site's argument: the policy concept pre-existed and failed *for want of automation*. The NIST definition it builds on (Glossary, p. 20, quoting NIST 800-37r2) is explicitly periodic: *"risk determinations and risk acceptance decisions taken at agreed-upon and documented frequencies ... Ongoing authorization is a time-driven or event-driven authorization process."*

**A counter-nuance the site should not overlook:** the Evaluation Criteria's own executive summary concedes the document-based approach is not abolished — *"cATO moves away from **solely** a document-based, point-in-time technical security assessment approach (**though some point-in-time documents are still required**)"* (p. 3). The parenthesis is in the original.

---

## 6. Control inheritance mechanics

### What is specified

**Named mechanism: a "shared security model".** The only named mechanism in the corpus, document 03 Table 2:

> **PP06 — "Identify application control inheritance from the DSOP using a shared security model."  Level: T**

The surrounding family header (p. 17) states the premise: *"PP — DSOP cATO practices; for a DSOP that already has an authorization; **many of these practices will be inherited by the team responsible for cATO.**"*

**Who performs it:** *"DSOP control inheritance by an application is identified by the DSOP security team."* (03, DevSecOps Platform Practices, p. 7)

**What is inherited, and the premise:** *"The cATO assessment assumes the DevSecOps platform is already authorized to operate and is in a state of continuous monitoring. **The applicable continuous monitoring practices will be inherited for use in the cATO authorization.**"* (03, p. 7) — note the object of inheritance is *continuous monitoring practices*, not control implementation statements.

**Who sets the tolerances applications inherit:** *"The DSOP team establishes the technical security controls and risk tolerances required for applications traversing the pipeline. If stricter tolerances need to be applied, the development team should work with the DSOP cATO team to apply them."* (03, p. 9)

**Cross-boundary inheritance (Use Case 2)** — two different mechanisms named in the two documents, which is worth flagging:
- Document 02, p. 6: *"An outcome of issuing a cATO for use case 2 is to seamlessly deliver software factory products into the production environment through a **Memorandum of Understanding (MOU) and an Interconnection Security Agreement (ISA)**."*
- Document 03, p. 13: *"An outcome of issuing a cATO for use case 2 is to seamlessly incorporate software factory products through **reciprocity agreements** into the production environment."*

**Inheritance of CSSP/ACD:** document 02 §2.0 lists CSSP provision in three modes — *"External"*, *"Internal"*, and *"Inherited – Agreements/documentation where integration occurs"* (p. 13).

**Two supporting NIST definitions are carried in the Implementation Guide glossary** (pp. 19–20) and are the nearest thing to a formal inheritance apparatus: **Common Control Provider** (*"an organizational official responsible for the development, implementation, assessment, and monitoring of common controls (i.e., controls inheritable by organizational systems)"*) and **Authorization to Use** (*"the official management decision given by an authorizing official to authorize the use of an information system, service, or application based on the information in an existing authorization package generated by another organization ... typically applies to cloud and shared systems, services, and applications"*). Note: "Authorization to Use" appears **only** in document 03's glossary and is not used in its body; the Evaluation Criteria does not define it at all.

**Who holds the risk under Use Case 1:** *"The cATO is issued to the software factory managing the environment that also has the responsibility for managing the risk for the single authorization boundary that is hosting multiple applications (subsystems)."* (03, p. 4)

### What is NOT specified — and these are the gaps the site can legitimately press on

- **No percentages. None.** No "X% of controls inherited", no inheritance ratios, no figures of any kind. Searched: `inherit` (6 hits in 03, 2 in 02, 0 in 07) with full context review; `%`, `percent`, `percentage`. The only percentages anywhere in the corpus are test-coverage metrics (03, p. 11: *"percentage of test coverage passed, percentage of passing functional tests ... percentage of threat actor actions mitigated"*). The widely circulated "inherit ~80% of controls from the platform" figure is **not** from these documents.
- **No required artefact format for inheritance.** Nothing specifies how an inheritance claim is expressed, exchanged, or machine-verified. PP06 says "identify ... using a shared security model" and stops. The SSP, SAR, SAP and POA&Ms are named as the authorisation-package artefacts (02, p. 11) with no format requirement.
- **No required machine format for anything** except the SBOM, and even there the Evaluation Criteria explicitly declines to mandate one: *"However, the format has not yet been mandated."*
- **No OSCAL.** See §8.

---

## 7. Evidence, artefacts and automation — verbatim, with locators

### 7A. Supporting "compliance evidence should be a build output"

Ordered by strength.

**[1] The keystone — document 07, §5.2 Goal 2, objective "Accelerate Software Deployment with Continuous Authorization", PDF p. 8** (the objective opens on p. 7 and the passage continues past the p. 7 footer; cached source lines 261–267). The phrase the site quotes is verbatim present. Full passage:

> *"**Accelerate Software Deployment with Continuous Authorization.** Many DoD Components identify obtaining an Authority to Operate (ATO) as the longest step in developing and deploying software. Automation creates opportunities that allow DoD to reevaluate the ATO process, shifting authorization from a "check-the-box for hundreds of security controls" activity to a "continuous authorization" activity. Continuous authorization encompasses validating the quality and security of the software development platform, process, and platform team. **It couples this validation with automation to produce real-time and continuous evidence, verifying the defensive posture of the platform and resulting software in real time. DoD's cybersecurity professionals must collaborate with software developers and system engineers to identify pipeline and process-generated evidence that verifies appropriate protections are in place for resilient and survivable software.**"*

Confirmed verbatim: **"pipeline and process-generated evidence"**. Exact locator for citation: DoD Software Modernization Strategy, v1.0, November 2021, §5.2 (Goal 2: Establish Department-wide Software Factory Ecosystem), objective *"Accelerate Software Deployment with Continuous Authorization"*, p. 8. Three things make it the keystone: *"produce"* (evidence is manufactured, not compiled), *"pipeline and process-generated"* (the generator is named as the pipeline), and *"real-time and continuous"* (currency is a property of the evidence). The surrounding goal is the Department-wide software factory ecosystem — so the demand is explicitly placed on factories, not on security staff.

Strongest supporting locator in the same document, document 07, §4 Process Transformation, "Cyber Survivability" bullet, p. 5:

> *"**A compliance mindset may lead to a false sense of security. Cybersecurity should be the driver and compliance an outcome.** DoD must shift from a cybersecurity "snapshot in time" compliance culture to a cybersecurity practitioner culture where automation, real-time continuous risk monitoring, including supply chain risk and rapid incident response, are the norm, and integrated into software development pipelines. System security engineering methods and practices must be identified early and leverage new technologies and approaches to streamline risk processes for software, **to inform continuous authorization**, and to enable Defensive Cyberspace Operations (DCO)."*

And the framing of the whole Process Transformation section, p. 4: *"These changes must consider not only pace and agility, but incentives to facilitate new behavior, policy updates to allow for innovation and experimentation, and **a shift from software compliance to operational readiness**."* Desired outcomes include *"reducing the lead time for cybersecurity compliance."*

Also document 07, §5.1 Goal 1, "Accelerate Cloud Adoption through Automated Design Patterns", p. 7 — the only "Compliance as Code" reference in the corpus:

> *"DoD must provide reusable automated design patterns, such as Infrastructure as Code, **Compliance as Code**, and hardened software containers, to ease the burden required in standing up and configuring virtual development environments. These automated design patterns must be available across the enterprise, **integrated into authorization processes**, and continuously updated and configuration controlled."*

**[2] Evidence as a pipeline product — document 03, p. 4** (Statement C). The Software Factory *"should include"*:

> *"**Automation that includes at least one DevSecOps pipeline with automated guardrails and control gates that collect evidence for making continuous risk assessments and determinations during software development**"*

This is the single most direct statement in the corpus that the pipeline is the evidence-collection apparatus. Restricted distribution — use with care.

**[3] Machine evidence — document 02, Figure 5, p. 9** (Statement A, publicly citable):

> *"Generates, analyzes, and displays machine evidence throughout the lifecycle in near real-time"* (DSOP × CONMON cell)

> *"Automation generates evidence and alerts; automatically kills bad containers; CSSP integrated with DSOP team"* (DSOP × ACD cell)

> *"Automation to secure the supply chain, enforce policy, and enable control gates"* (DSOP × SSSC cell)

Paralleled in document 03, p. 6: *"for CONMON, the software factory must have the automation to generate, analyze and display machine evidence."*

**[4] Automated SBOM export — document 02, §3.1, p. 14:** *"Provide an automated export of the SBOM for applications/products passing through the DSOP"*; *"Specify the SBOM format and how often it is generated"*; *"Maintain an archive of SBOMs for products passing through pipelines. This can be kept in the same area as the assessment evidence (e.g., results of security tests) for the products"*.

**[5] Currency as a requirement — document 02, §1.0, p. 11:** *"Must be readily available and as near real time as feasible"*; *"Includes a dashboard with relevant **current** information and requirements that helps security personnel perform their tasks"*. Only four occurrences of "current" in document 02; this is the only one making currency a property of the evidence.

**[6] Real-time access as a business rule — document 02, §1.0, p. 11:** *"AO and designated cybersecurity personnel must have real-time access to the results of testing, scanning, monitoring, and performance metrics at the platform or application level in a mutually agreeable format (i.e., dashboards, alerts, etc.)"*; *"Identify, assess, prioritize, and share risk information in real time"*; *"Identify risks in real time and initiate corrective action plans to mitigate them"*.

**[7] The pipeline is itself in scope — document 02, §1.0, p. 11:** *"Helps secure the software supply chain, the software development pipeline and its environment must be monitored as well"*. And §1.0, p. 11–12: the Security Assessment must *"cover the DSOP supporting full lifecycle, **including the delivery pipeline**"*.

**[8] Continuous automated control validation — document 03, p. 9:** *"The DevSecOps team continuously validates sub-system secure configurations and security control compliance using security automation."* And: *"The DevSecOps team continuously reassesses artifacts in the artifact repository to ensure that the residual risk remains acceptable."* And p. 7: *"Security automation is used for monitoring the application security posture within the production system. In addition, the automation provides for periodic checks of secure configurations."*

**[9] Automated authorisation decisions — document 03, p. 8:** *"**Many of these practices can be automated, including risk determinations and continued ongoing authorization decisions.**"* The decision itself, not merely the evidence, is contemplated as automatable. Note the hedge: *"can be"*.

**[10] The factory definition itself — document 02 Glossary, p. 19 (and 03, p. 20):** *"Software Factory is a software assembly plant that contains multiple pipelines ... to produce a set of software deployable artifacts **with minimal human intervention**."*

**[11] Environment drift — document 02, §3.2, p. 15:** *"Reliance on Infrastructure as Code (IaC) and Configuration as Code (CaC) to avoid environment drift"*.

**[12] Table 2 threshold rows — document 03, Appendix B:** SA10 (T) *"Capture, visualize, and provide feedback on security findings during pipeline runs"*; CM03 (T) *"Provide availability of findings, plan of action, security posture, and residual risk through DevSecOps dashboards"*; IC04 (T) *"Collect evidence for establishing a baseline risk posture"*; CM05 (T) *"Monitor for change in secure configurations"*; CM06 (T) *"Monitor control compliance and continued effectiveness of controls against the changing threat"*; PP07 (T), PP10 (T), RM04 (T).

**[13] The automated-trigger gate — document 02, p. 7:** *"the key to receiving a cATO is having a robust continuous monitoring strategy that includes **automated triggers based on approved thresholds** within the auditing and incident response plans."*

### 7B. Undercutting the thesis — where periodic, manual, human-produced evidence is permitted

Honest accounting. These matter as much as §7A.

**[a] Screenshots are an acceptable substitute for demonstration. Document 02, §3.2, p. 15:**

> *"Demonstrate each control gate in action (this may be in a non-production environment) **or provide screen shots of control gate output as displayed in a dashboard**"*

A static PNG of a dashboard satisfies the control-gate criterion. This is the most damaging single sentence in the public document for the "evidence is a build output" thesis, and the site should confront it rather than omit it. It also shows the *mechanism* of degradation: the criteria ask for a *demonstration*, demonstrations are hard to schedule, and a screenshot is an accepted fallback — so the artefact that reaches the assessor is a picture of a dashboard, which is a document.

**[b] Manual reporting is explicitly permitted as a fallback. Document 02, §1.0, p. 11:**

> *"Must provide compliance reporting statistics to the Continuous Monitoring & Risk Scoring (CMRS) system of record via automated processes **if possible. If not possible, manual reporting is required until automated process is developed.**"*

**[c] Annual manual control monitoring is an explicitly contemplated timeline. Document 02, §1.0, p. 10:**

> *"Includes timelines for continuous monitoring of security controls (**automated every hour, minute, second; manual once a year, etc.**)"*

A control monitored by hand once a year sits inside the same sentence as a control monitored every second, with no preference stated. This is the Evaluation Criteria operationalising the memo's own *"Manual controls will have different timelines associated"*.

**[d] The method is a shift to *periodic* assessment, not continuous assessment. Document 03, p. 5:**

> *"This assessment method is a fundamental shift from a point-in-time assessment of organizational compliance with security controls **to a periodic assessment of an organization's continued readiness** for managing risk throughout the application lifecycle from development through operations under continuous integration, delivery, and deployment."*

The *system's* risk monitoring is continuous; the *assessment of the organisation* is periodic. The authorisation apparatus itself never becomes continuous. If the site claims the policy makes assessment continuous, this sentence refutes it.

**[e] Meeting minutes are named as acceptable evidence. Document 03, p. 6:**

> *"Gather and review organization's practice documentation and evidence. For example, **evidence may be provided through various types of tracking systems, meeting minutes, and pipeline security scanning reports.**"*

Minutes and scan reports sit in one list as equivalent evidence classes.

**[f] Demonstrations and interviews are first-class evidence. Document 03, p. 6, "High Level Evaluation Criteria":**

> *"Practices are defined and documented."*
> *"Evidence exists on the use of risk management and continuous monitoring practices. **This evidence includes demonstrations.**"*
> *"The workforce is knowledgeable on the cATO practices."*

And p. 5: *"...through the review of evidence of use of the practices, **interviews with personnel** performing the practices to determine the level of organizational understanding..."* A substantial fraction of the cATO evidence base is human testimony, which cannot be a build output.

**[g] Point-in-time documents are expressly retained. Document 02, p. 3:**

> *"cATO moves away from **solely** a document-based, point-in-time technical security assessment approach (**though some point-in-time documents are still required**), towards focusing on a continuous risk determination and authorization concept..."*

**[h] The required package is a document set.** Document 02, §1.0, p. 11 lists SAP, SAR, RAR, SSP, signed ATO memo, POA&Ms, plus *"Update documents in response to CONMON process"*; p. 13 adds the cATO Approval Memo template. Plus the explicit mandatory-deliverable framing (p. 10): *"Items in bold in this section indicate **documents or artifacts that must be delivered** as part of the application for cATO package."*

**[i] Automating control validation is optional. Document 03, Table 2: SA03 "Automate security control configurations and validation" — level O.** Objective means *"should be met, but which may not be fully met initially, while still obtaining a cATO."* A factory can obtain a cATO without automating control validation.

**[j] Reference-design compliance is also optional. Document 03, Table 2: PP01 — level O**, despite being the memo's third competency.

**[k] Manual and periodic testing feed the gates. Document 03, p. 9:**

> *"The DevSecOps team **periodically** uses dynamic vulnerability tools, threat actor emulation, pen-testing, and analysis from operations to determine security control effectiveness. **This is an area in which some of the testing may be manual, such as pen-testing, but the results of which can be used for control gate pass/fail determination.**"*

Manual results flowing into automated gates: the gate is automated, its input is not. Also document 02 §1.0 requires *"Manual code reviews"* within the Security Assessment, and document 02 §2.0 sets a **90-day-then-annual** cadence for third-party penetration testing.

**[l] Dashboards aggregate manual results too. Document 03, p. 5:** *"Continuous security posture (or status) and risk reporting, including dashboards, that aggregate and display results from automated (**and possibly manual**) security vulnerability analysis, control compliance scans, and security control effectiveness..."*

**[m] Periodic risk review is a threshold requirement. Document 03, Table 2: RM05 (T) "Establish periodic reviews of risk and risk remediation / adjudication."** Periodicity is mandatory; continuity of review is not.

**[n] Training documentation may be any viewable form. Document 02, §3.3, p. 16:** *"Documentation need not be text documents but may be in online learning management tools that assessors can view."* Permissive about *medium*, silent on machine-readability.

**[o] No mandated SBOM format. Document 02, §3.1, p. 14:** *"However, the format has not yet been mandated. SBOM is currently undergoing regulatory action, Defense Information Systems Agency (DISA) Federal Acquisition Regulation (FAR) is the lead."* As of May 2024 the one genuinely machine-readable artefact in the criteria had no mandated schema.

**[p] "Partly determined", "not limited to", "guidelines". Document 02, p. 10** — the criteria disclaim being a conformance standard, as does document 03 p. 15 (*"not ... a conformance checklist"*). There is no pass mark, no scoring rubric published, and weighting is left to each assessment team (document 03, p. 6: *"Weighting can be established for the key areas"*).

### 7C. The fair synthesis

The corpus requires **continuous risk monitoring** and a **real-time dashboard**, and names the **pipeline** as the generator of evidence. It does not require that evidence be **machine-readable**, **signed**, **attested**, **reproducible** or in any **standard format**; it accepts **screenshots**, **meeting minutes**, **interviews** and **demonstrations**; it assesses the organisation **periodically**; it lists the automation of control validation as **optional**; and it still demands a conventional **document package** (SSP, SAR, RAR, SAP, POA&Ms, signed ATO memo). The site's thesis is better stated as: *the policy demands continuous evidence and names the pipeline as its source, but specifies no machine-verifiable form for it — and that unspecified gap is exactly where the stale document reappears.* That version survives contact with the primaries. A stronger version ("the policy already demands machine-verifiable evidence") does not.

---

## 8. Search counts

All counts case-insensitive regex over the full cached text of each file. Page-furniture noise is separated out where it would mislead.

| Term | 02 Eval Criteria | 03 Impl Guide | 07 SW Mod Strategy |
|---|---|---|---|
| **OSCAL** | **0** | **0** | **0** |
| **SBOM** | **10** | **3** | **0** |
| **reproducible / reproducib\*** | **0** | **0** | **0** |
| **attestation / attest\*** | **0** | **0** | **0** |
| **SLSA** | **0** | **0** | **0** |
| **in-toto** | **0** | **0** | **0** |
| **Sigstore** | **0** | **0** | **0** |
| **provenance** | **0** | **0** | **0** |
| **signature** | **0** | **0** | **0** |
| **cross-domain / "cross domain"** | **0** | **0** | **0** |
| **air gap / air-gap / airgap** | **0** | **0** | **0** |
| **classified** | **0** | **0** | **0** |
| **impact level / IL2–IL6** | **0** | **0** | **0** |

Supplementary counts gathered for the evidence analysis:

| Term | 02 | 03 | 07 |
|---|---|---|---|
| evidence | 14 | 8 | 2 |
| automat\* | 20 | 25 | 18 |
| "machine evidence" | 1 | 1 | 0 |
| machine-readable / "machine readable" | 0 | 0 | 0 |
| dashboard | 9 | 9 | 0 |
| real-time / "real time" | 3 / 5 | 3 / 1 | 2 / 2 |
| "near real" | 2 | 3 | 0 |
| manual | 3 | 2 | 0 |
| periodic\* | 1 | 4 | 0 |
| annual | 1 | 0 | 1 |
| artifact / artefact | 6 | 4 | 1 |
| "screen shot" / screenshot | 1 / 0 | 0 | 0 |
| inherit\* | 2 | 6 | 0 |
| reciprocity | 0 | 1 | 1 |
| "authorization to use" | 0 | 2 | 0 |
| re-authoriz\* / reauthoriz\* | 0 | 0 | 0 |
| zero trust / zero-trust | 0 | 3 | 1 |
| Infrastructure as Code / IaC | 2 / 2 | 0 | 1 |
| "Compliance as Code" | 0 | 0 | **1** |
| hash / immutab\* / "digital sign" / cryptograph\* | 0 | 0 | 0 |
| classification (substantive) | 0 | 1 | 1 |

### Notes on the zero and near-zero results

- **OSCAL: absolutely absent.** Zero hits across all three documents, 128 KB of text, including the Evaluation Criteria's SBOM section where a machine-readable control-catalogue format would most naturally appear, and including all five reference lists. The DoD's own 2024 cATO criteria specify no machine-readable format for control or assessment information. For a site arguing about OSCAL's fate in defence, this is a positive finding, not a null result: the policy that most needed OSCAL did not cite it.
- **No supply-chain integrity primitives whatsoever.** Zero for attestation, provenance, signature, SLSA, in-toto, Sigstore, reproducible, hash, immutable, cryptographic, digital signature. The entire SSSC competency rests on **SBOM** (and SBOM alone, with no mandated format) plus scanning and CNAPP tooling. The documents invoke NIST SP 800-161r1 for C-SCRM by reference (02, p. 8) and the memo's SBOM rationale (*"to prevent any combination of human errors, supply chain interdictions, unintended code"*, quoted in 03, p. 2), but name no integrity mechanism. The gap between this and contemporary industry practice (signed attestations, verifiable provenance) is wide and is cleanly documentable from these sources.
- **"classified": 0 substantive hits.** All raw matches were the `UNCLASSIFIED` / `Unclassified` page furniture — 38 in document 02, 52 in document 03, 25 in document 07. The word "classified" as a security marking of *data* appears nowhere.
- **"classification" (substantive): 2 hits total**, both oblique:
  - 03, p. 4: *"the production/operational environment is outside the DSOP, such as when the hosting environment is an embedded system or **a system of a higher classification than the development environment**"* — the only acknowledgement in the corpus that evidence might have to cross a classification boundary, and it offers no mechanism beyond *"the risk governance team must work with the authorizing official for the production environment to identify the risk tolerances"*.
  - 07, p. 6: *"The requirement for cloud across **all classification domains**, from enterprise to tactical edge, is still valid."*
- **Cross-domain, air gap, impact level: all zero.** No IL2/IL4/IL5/IL6 designations, no DISA impact-level vocabulary, no cross-domain solution or guard discussion, no disconnected/intermittent-connectivity provision anywhere. **This is a real and quotable hole.** Use Case 2 is explicitly about deploying into separate boundaries — Navy ships, weapon systems, embedded systems, higher-classification environments — and the mechanism offered is entirely administrative: an MOU plus an ISA (02), or "reciprocity agreements" (03), with a requirement that results *"pass ... back to the software factory"* and an obligation to *"include detailed information for all external connections IAW Appendix E Diagram Requirements of the DISA Connection Process Guide"*. How continuous machine evidence traverses an air gap or a classification boundary is simply not addressed. The dashboard is assumed reachable. For deployed and tactical systems — the ones the Strategy's own three-years-hence vignette is about (*"from fighter aircraft to communications equipment"*) — the policy has no answer.
- **SBOM is concentrated in one place.** 10 of 10 hits in document 02 are in §3.1 (p. 14). Document 03's 3 hits are: the memo quotation (p. 2), the acronym list (p. 21), and a single line of implementation advice (p. 12: *"Create SBOMs for the DSOP and applications passing through it."*). Document 07 (2021) predates SBOM in DoD policy vocabulary entirely: **0 hits**.

---

## 9. Not found — and what was searched

| Sought | Status | How searched |
|---|---|---|
| OSCAL, in any form | **Not found** | Case-insensitive `OSCAL` across all three files, plus `machine.?readable`, `control catalog`, and manual review of all five reference lists and both glossaries |
| Attestation, provenance, signing, SLSA, in-toto, Sigstore, reproducible builds | **Not found** | Case-insensitive regex per term, plus `hash`, `immutab`, `digital sign`, `cryptograph`, and manual review of 02 §3.1 (the SBOM/SSSC section) and 03 Table 2 family SA |
| Control-inheritance **percentages** | **Not found** | `inherit` with full context review (8 hits total), plus `%`, `percent`, `percentage`. Only percentages in the corpus are test-coverage metrics (03, p. 11) |
| Required **artefact format** for inheritance or control evidence | **Not found** | Full read of 03 "DevSecOps Platform Practices" (p. 7), Table 2 family PP, both glossaries, and 02 §1.0 authorisation-package list. Only format guidance anywhere is the SBOM's SPDX/SWID/CycloneDX, explicitly *"not yet been mandated"* |
| Cross-domain, air gap, impact level (IL2–IL6), classified-data handling | **Not found** | Per-term regex incl. hyphen/space/concatenated variants and `IL[0-9]`; `classif` hits triaged against page furniture (115 of 117 raw hits were `UNCLASSIFIED` markers) |
| The phrase **"modifies requirements for re-authorizing"** in documents 02/03/07 | **Not found in these three** — located in the signed memo (`04-cato-memo.md`, line 51) | `re-?authoriz` and `reauthoriz` across all three (0 hits each), then across 04 |
| Which Appendix D items are **mandatory deliverables** | **Not determinable from this cache** | Bold formatting did not survive extraction: `grep -c '\*\*'` = 0 in document 02, despite p. 10 stating *"Items in bold ... must be delivered"*. Requires re-reading the PDF |
| Implementation Guide **Table 1** (competency crosswalk, p. 7) | **Extracted empty** — content recovered from document 02 Figure 5 instead | Direct read of 03 lines 284–286; cross-referenced to 02 lines 208–215 |
| Figures 1–5 (doc 02) and Figures 1–4 (doc 03) | **Not retrievable** (images). Figures 4 and 5 of document 02 flattened into readable text; the rest did not | Direct read; figure captions present, bodies absent |
| A published pass mark, scoring rubric or weighting scheme for the criteria | **Not found** | Read of 02 p. 10 framing and 03 pp. 5–6 assessment method. Both devolve weighting to the assessment team: *"Weighting can be established for the key areas"* (03, p. 6) |
| Evaluation Criteria **Appendix B** as a high-value artefact | **Present but thin** — document 02's Appendix B is 1.5 pages of assessment-method overview (pp. 7–8), *not* a requirements table. The substantive requirements table is **document 03's** Appendix B (Table 2, 44 rows, §3 above). Earlier research flagging "Appendix B" should be read as pointing at document 03 | Direct read of both |

**Authoritative-source caveat for the whole file.** Both 2024 documents disclaim finality and point elsewhere. Document 02, p. 4: *"Please note that due to evolving requirements, this is a living document on the RMF Knowledge Service. Appropriate communities will be notified as updates are made."* Document 02, p. 7: *"**While the DoD RMF Knowledge Service is the authoritative source for cATO implementation guidance**, this appendix provides an overview..."* Document 03, p. 2 and p. 6 both route readers to `https://rmfks.osd.mil` for the current criteria. The RMF KS is CAC-gated and not retrievable here. Anything the site asserts as *current* DoD requirement should be dated to these documents (May 2024 / March 2024) rather than stated in the present tense.
