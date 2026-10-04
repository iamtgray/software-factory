# 11 — DoD primaries: Reference Design (CNCF K8s) and DevSecOps Fundamentals v2.5

Source documents read in full (both cached locally as plain markdown):

| Ref | Document | Version / date | Pages | Local path |
|---|---|---|---|---|
| **RD** | DoD Enterprise DevSecOps Reference Design: CNCF Kubernetes | **v2.1, September 2021** (approved by Nicolas Chaillan, DoD/USAF Chief Software Officer; cleared for public release 22 Oct 2021) | 32 | `sources/dod/05-refdesign-cncf-k8s.md` |
| **FUND** | DoD Enterprise DevSecOps Fundamentals | **v2.5**, approved by the DoD Software Modernization Senior Steering Group **16 October 2024** | 44 | `sources/dod/06-devsecops-fundamentals-v2.5.md` |

Locators below are given as document section/table plus the PDF page number carried in the extracted text, and the line number in the local markdown file (`md:N`) so quotes can be re-found.

Two version facts matter before anything else, because three of the site's claims turn on dates:

- The RD on disk is **v2.1 (September 2021)**, *not* the 2019 edition. Its only "What's New in Version 2" note (§1.6, p.3, md:251) is a single bullet: *"Refactored the document's overall structure to align with the shift to a DevSecOps Document Set approach."* No 2019 text is available in the cache, so claims specifically about *the 2019 reference design* cannot be verified from this material — marked accordingly below.
- The RD carries a self-destruct clause on its cover page (md:18): **"This document automatically expires 1-year from publication date unless revised."** On its own terms it expired in September 2022. It has never been superseded by a public v3. This is probably the single most useful fact in this file for the site's argument.
- The **October 2024** document in the cache is FUND v2.5, not a reference design revision. The site appears to have conflated the two.

---

## The definition

**Software factory — the canonical DoD definition.** FUND gives it twice, identically, once in the key-concepts table and once in the glossary. The table version is marked "In the DoD, a software factory is defined as…", which makes it the authoritative form:

> **"In the DoD, a software factory is defined as a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."**
>
> — FUND v2.5, §2.3, Table 1 "DevSecOps Key Concepts", pp. 4–5 (md:252–256)

The same wording appears without the "In the DoD" framing in the body and the glossary:

> "A software factory is a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes. Software factories are strongly linked to one or more specific software supply chains but the software factory itself is not an entire software supply chain."
>
> — FUND v2.5, §3.1.2 "Software Factory", p. 7 (md:292–296)

> "Software Factory | A software factory is defined as a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."
>
> — FUND v2.5, Glossary of Key Terms, p. 37 (md:1043–1049)

Note the three load-bearing properties of this definition: it is about **people, tools and processes** (not a product); its measure is **continuously deliver value by deploying**; and it is scoped to **a specific community of end users**. It says nothing about containers, Kubernetes, cloud, or any tool. FUND makes that explicit:

> "Note that a DevSecOps implementation does not require a specific architecture, containers, or even explicit use of cloud computing. However, the use of these components is strongly recommended, and in some cases mandated by specific DoD reference designs."
>
> — FUND v2.5, §3.1, p. 6 (md:278)

**DevSecOps platform.** Defined three times in FUND, and the three are **not identical** — see the correction below. The body definition is the fullest:

> "A DevSecOps platform is defined as a group of resources and capabilities that form a base upon which other capabilities or services are built and operated within the same technical framework. It provides a comprehensive set of common tools, services, and infrastructure to support the implementation and execution of DevSecOps practices within an organization and serves as a centralized hub for managing and automating various phases of the software development lifecycle, with a strong focus on security. It can be a multi-tenant environment that brings together a significant portion of a software supply chain, operating under cATO or a provisional ATO. Each DevSecOps platform may be composed of multiple software factories, multiple environments, multiple tools, and numerous cyber resiliency tools and techniques."
>
> — FUND v2.5, §3.1.3 "DevSecOps Platform", p. 11 (md:389)

**The distinction between a software factory and a DevSecOps platform.** FUND draws it explicitly and in one sentence pair:

> "A software factory encompasses the entire set of software capabilities required to deliver resilient software capability at speed. The DevSecOps platform consists of those software capabilities that are common across all software factories and provides a standardized and secure foundation for software development."
>
> — FUND v2.5, §3.1 "DevSecOps Implementation Components", p. 6 (md:276)

Plus the containment relation, which runs **platform ⊃ factory ⊃ pipelines**:

> "Each DevSecOps platform may be composed of multiple software factories, multiple environments, multiple tools, and numerous cyber resiliency tools and techniques." (§3.1.3, p. 11, md:389)
>
> "Software factories may contain multiple assembly lines, or in software parlance, CI/CD pipelines." (§3.1.2, p. 8, md:318)

So: the **factory** is the whole set of capabilities needed to deliver for one user community; the **platform** is the common, reusable subset shared across factories; a platform can host many factories; a factory can run many pipelines. The factory is the unit of *delivery*; the platform is the unit of *reuse and authorisation*.

Note the RD (2021) describes the layering slightly differently and attributes it to FUND:

> "The DevSecOps Fundamentals describes a DevSecOps platform as a multi-tenet environment consisting of three distinct layers: Infrastructure, Platform/Software Factory, and Application(s)."
>
> — RD v2.1, §3 "Software Factory Interconnects", p. 4 (md:271) — *note "multi-tenet" is a typo for "multi-tenant" in the source*

In the 2021 RD, "Platform/Software Factory" is a **single layer** — the two terms are elided. FUND v2.5 is the document that separates them. If the site needs a clean distinction, it comes from 2024, not 2021.

**Continuous ATO (cATO).** FUND gives it three times in identical wording (§2.3 Table 1 p. 5 md:270; §3.3.1.2 p. 21 md:555; Glossary p. 34 md:977):

> "cATO is the state achieved when the organization that develops, secures, and operates a system has demonstrated sufficient maturity in their ability to maintain a resilient cybersecurity posture that traditional risk assessments and authorizations become redundant. This organization must have implemented robust information security continuous monitoring capabilities, active cyber defense, and secure software supply chain requirements to enable continuous delivery of capabilities without adversely impacting the system's cyber posture."

The three pillars are therefore **continuous monitoring, active cyber defence, secure software supply chain** — each is given a definitional bullet at FUND §3.3.1.2, p. 21 (md:557–574). And the key procedural requirement:

> "A DevSecOps platform and its software factories must complete an authorization. Once an authorization is approved, the DevSecOps platform and its software factories can expedite future authorization activities and processes by obtaining a cATO. cATO moves away from a control assessment point-in-time document-based approach (though some documents are still required) towards a continuous risk determination and authorization concept by continuously assessing, monitoring, and managing risk. cATO raises the security standard over a traditional Authorization to Operate (ATO) and provides the ability to deploy updated software more rapidly while improving security. **cATO includes the need for a Secure Software Supply Chain (SSSC) and requires a Software Bill of Materials (SBOM).**"
>
> — FUND v2.5, §3.3.1.2, p. 22 (md:576), emphasis added

**The RD v2.1 never mentions cATO at all.** Searched: `cATO`, `continuous authorization`, `Authorization to Operate`. Hits in RD: "ATO" twice (both incidental — "a Cloud Service Provider with a DoD provisional authorization or ATO", §4.2 p. 15 md:532; and "Speed up ATO process" as a tool benefit in Table 7, p. 19 md:668), plus one "Authorization to Connect (ATC)" (§4.1 p. 14 md:518). The reference design predates the cATO regime entirely.

**Hardened container — no formal definition in either document.** Neither has a glossary entry for it. It is used ~20 times in the RD as an undefined primitive, and the normative content is delegated to DISA:

> "Container hardening | Harden the deliverable for production deployment. **Containers must follow the DISA Container Hardening Guide.**"
>
> — RD v2.1, Table 4 "Develop Phase Activities", p. 18 (md:578), citing *DISA, "Container Hardening Process Guide, V1R1," October 15, 2020*

The closest thing to a definition is descriptive, via Iron Bank's output:

> "The Iron Bank artifact repository provides hardened, secure technical implementation guide (STIG) compliant, and centrally updated, scanned, and signed containers that increases the cyber survivability of these software artifacts."
>
> — RD v2.1, §3.3, pp. 7–8 (md:340)

And FUND's glossary entry for Iron Bank (p. 36, md:1033):

> "Iron Bank | Holds the hardened container images of DevSecOps components that DoD mission software teams can utilize to instantiate their own DevSecOps pipeline. It also holds the hardened containers for base operating systems, web servers, application servers, databases, API gateways, message busses for use by DoD mission software teams as a mission system deployment baseline. These hardened containers, along with security accreditation reciprocity, greatly simplifies and speeds the process of obtaining an Approval to Connect (ATC) or Authority to Operate (ATO)."

So "hardened" in DoD usage means *STIG-compliant, centrally scanned, centrally signed, and accredited by someone else* — it is an **accreditation provenance claim, not a technical property**. That is worth saying on the site plainly.

---

## Corrections to the site

### C1 — The Reference Design §5.1.1 is not about control inheritance, and the version on disk is 2021, not 2019

The site says RD §5.1.1 defined machine-enumerable inherited/hybrid/owned controls and deferred it in 2019. In the cached document:

> "5.1.1 CSP Managed Services for Continuous Monitoring" — RD v2.1, p. 25 (md:96 contents, md:892 body)

§5.1.1 is one paragraph about using cloud-provider monitoring services alongside third-party tools ("both/and" rather than "either/or"). It contains no control categorisation, no inherited/hybrid/owned taxonomy, and nothing deferred. Searched the whole RD for: `inherit`, `inheritable`, `hybrid`, `common control`, `owned control`, `defer`. **Zero hits for all of them.** The RD v2.1 does not discuss control inheritance at any point, in any section.

**Status: the claim as written is wrong for the cached v2.1.** It may be true of RD v1.0 (2019), which is not in the cache and could not be retrieved. If the site keeps the claim it must be re-scoped to v1.0 and sourced separately — and note that §5.1.1 in v2.1 is occupied by different content, which is itself evidence that the structure changed.

**What the documents *do* say about inheriting controls from an authorised platform** — this lives in FUND, not the RD, and it is about IaC baselines and CSP PaaS, not about factories inheriting from factories:

> "It accelerates the authorization process with inheritable common controls and the use of PaaS services, which reduces the need for Security Technical Implementation Guides (STIGs), Assured Compliance Assessment Solution (ACAS), and Host-Based Security System (HBSS). If implemented correctly, it can shorten the deployment of networking, identity, and security policies for security compliance from the standard 30 weeks to hours."
>
> — FUND v2.5, §3.1.5 "Infrastructure as Code (IaC)", p. 14 (md:429)

> "Baselines significantly reduce mission owner security responsibilities by leveraging security control inheritance from CSP PaaS managed services, where host and middleware security is the responsibility of the CSP including hardening and patching. **Each baseline documents its associated inheritable controls to expedite the Assessment and Authorization (A&A) process.** DoD IaC baselines can be built into DevSecOps pipelines to rapidly deploy the entire environment and mission applications."
>
> — FUND v2.5, §3.1.5, p. 14 (md:435), emphasis added

Note what this is and is not. "Each baseline documents its associated inheritable controls" is the closest thing in either document to a demand that inheritance be written down. It is a statement of fact about DoD-published IaC baselines (hosted at `https://www.hacc.mil/Portfolio/DOD-Cloud-IaC/`), not a requirement imposed on a factory, and "documents" is deliberately format-free — no schema, no machine-readability, no enumeration. The only machine-readability requirement anywhere in either document is about *policy* files, not controls (see T4 below).

The adjacent cached source does carry platform-to-application inheritance as a named practice — `sources/dod/03-continuous-authorization-impl-guide.md` line 668: *"PP06 Identify application control inheritance from the DSOP using a shared security model"*, and line 310: *"DSOP control inheritance by an application is identified by the DSOP security team."* If the site wants a citable inheritance requirement, that guide is the place, not the reference design.

### C2 — The multi-tenancy isolation claim fails in both directions

The site says a demonstrated isolation test was a stated **must** in the 2019 RD and was quietly dropped in an October 2024 revision.

**On the "dropped in October 2024" half — this is the wrong way round.** The October 2024 document (FUND v2.5) contains the *strongest* multi-tenancy language of the two, and it is a hard `must`:

> "4. **Scalability and Flexibility**: Scales and adapts to the needs of the organization. **It must be designed for multi-tenancy** and accommodate different types of applications, technologies, and deployment environments, including on-premises, cloud, and hybrid infrastructures."
>
> — FUND v2.5, §3.1.2, item 4 of "An ideal DevSecOps software factory does the following", p. 10 (md:371), emphasis added

A weaker companion statement sits in the digital-platform capability description:

> "These capabilities **should** support multi-tenancy, enforce separation of duties for privileged users, and be considered part of the cyber survivability supply chain of the final software artifacts produced."
>
> — FUND v2.5, §3.1.2, p. 8 (md:310), emphasis added

And the platform definition is permissive, not mandatory: *"It **can be** a multi-tenant environment…"* (§3.1.3, p. 11, md:389).

**On the "demonstrated isolation test" half — not found in either document, in any version on disk.** Searched: `isolation`, `isolated`, `tenant isolation`, `multi-tenant`, `multi-tenancy`, `multi-tenet`, `demonstrat`, `isolation test`, `penetration`, `breakout`, `escape`. Results:

- RD v2.1: one `multi-tenet` (the typo at §3, md:271, quoted above) and one `isolated`, which is about sidecar containers, not tenants — *"the two containers can share disk and network resources while their running components are fully isolated from one another"* (§3.4, p. 8, md:358). **No isolation test, no demonstration requirement.**
- FUND v2.5: three `multi-ten*` hits (all quoted above), one `multi-tenant`, one scare-quoted `"isolated"` about embedded projectiles (§3.1.1, p. 6, md:284), and one `isolate` about isolating defects in small changes (§3.1.4, p. 12, md:405). **No isolation test.**

**Status: wrong on both halves as stated.** The accurate version of this point is far more damning and the site should use it instead: *both documents require multi-tenancy as a design property and neither ever defines a test that would demonstrate the isolation actually holds.* The `must` is on the design intent; there is no verification obligation attached to it anywhere. That is a genuine gap, and it is present in the current (October 2024) document, not absent from it.

### C3 — "Don't build your own platform" is real, correctly attributed, and in neither of these two documents

Searched both documents for: `avoided if possible`, `build your own`, `building your own`, `roll your own`, `bespoke`, `custom platform`. **Zero hits in both.**

The sentence the site is paraphrasing exists, and it is almost verbatim — but it is in the **DevSecOps Continuous Authorization Implementation Guide** (April 2024), already cached as `sources/dod/03-continuous-authorization-impl-guide.md`, line 418, in the "Practical Implementation Advice" section. It appears as the **last of five ranked options** for standing up a DevSecOps platform (DSOP):

> "Choose one of the following options to build out the DSOP.
> - Use an existing DSOP (e.g., Platform One Party Bus).
> - Use a new instance of a DSOP (e.g., Platform One Big Bang).
> - Use an integrated set of cloud-native tools.
> - Use an existing commercial integrated DevSecOps tool.
> - **Build a new DSOP using hardened components. This is the most time-consuming approach, and it should be avoided if possible.**"

**Status: the claim is substantively right but the citation needs fixing** — attribute it to the Continuous Authorization Implementation Guide, April 2024, "Practical Implementation Advice", not to the reference design or Fundamentals. The ranked-list framing is worth quoting in full on the site, because it shows DoD putting *reuse someone else's platform* first and *build it yourself* fifth and last.

The closest the RD comes is a cost argument rather than a prohibition, and it is still useful:

> "Operating a custom DevSecOps platform is an expensive endeavor because software factories require the same level of continuous investment as a software application. There are financial benefits for programs to plan a migration to a containerized software factory, reaping the benefits of centrally managed and hardened containers that have been fully vetted. In situations where a containerized software factory is impractical, or the factory requires extensive policy customizations, the program should consult with DoD CIO and (if applicable) its own DevSecOps program office to explore options and collaborate to create, sustain, and deliver program-specific hardened containers to Iron Bank."
>
> — RD v2.1, §4.1, p. 15 (md:524)

FUND's equivalent is softer still — encouragement, not prohibition:

> "Every DoD organization is encouraged to seek out an existing managed PaaS to learn about and begin applying DevSecOps." (§3.1.2, p. 11, md:381)
>
> "DoD organizations are encouraged to leverage government-managed and curated platforms, such as Platform One's tailorable Big Bang platform, and contribute modifications back to the baseline to provide the DoD-enterprise with a growing set of pre-configured integrations." (§3.1.3, p. 12, md:399)

### C4 — The "zero references" claim holds for reproducible builds, admission-time signature verification and OSCAL — but SBOM is an explicit requirement, and the site must not lump it in

See T4 below for the full search table. Summary of the correction: **SBOM is demanded**, once, unambiguously, in the current document — *"cATO includes the need for a Secure Software Supply Chain (SSSC) and requires a Software Bill of Materials (SBOM)"* (FUND v2.5 §3.3.1.2, p. 22, md:576). If the site's "zero genuine references" list includes SBOM, that is a factual error. The three named in the brief (reproducible builds, signature verification at admission, OSCAL) are all confirmed absent.

### C5 — Minor but citable: FUND v2.5 contradicts itself on whether a DevSecOps platform is necessary

The same sentence appears in the key-concepts table and in the glossary with one word changed:

> §2.3, Table 1, p. 5 (md:258): "Use of a DevSecOps platform **is necessary** to accelerate development, delivery, and cybersecurity accreditation."
>
> Glossary, p. 36 (md:1019): "Use of a DevSecOps platform **is encouraged** to accelerate development, delivery, and cybersecurity accreditation"

Two different modal strengths for the same proposition, inside one 44-page document, approved by a steering group. Useful if the site wants to argue the normative layer is loose. (The glossary version also drops the full stop.)

---

## Theme: what the Reference Design actually requires

### The five mandatory interconnects

This is the RD's compliance core — the only place it uses "must be present in order to be compliant":

> "Figure 1: Kubernetes Reference Design Interconnects identifies the specific Kubernetes interconnects that **must be present in order to be compliant with this reference design**. The specific interconnects include:
> - Cloud Native Access Point (CNAP) at the Infrastructure layer manages all north-south network traffic.
> - Use of a conformant Kubernetes installation in each of the development environments.
> - Clear identification of a locally centralized artifact repository to host hardened containers from Iron Bank, the DoD Centralized Artifact Repository (DCAR) of hardened and centrally accredited containers.
> - Use of a service mesh within the K8s orchestrator to manage all east-west network traffic.
> - Mandatory adoption of the Sidecar Container Security Stack (SCSS) to implement zero trust down to the container/function level, also providing behavior protection."
>
> — RD v2.1, §3, p. 5 (md:277–287)

### Architecture layers and the official decomposition (for checking against 24 "slots")

**RD v2.1 — three layers** (§3, p. 4, md:271): **Infrastructure**, **Platform/Software Factory**, **Application(s)**. Interconnects are the tools and activities that exist *within or between* these layers.

**FUND v2.5 — three capability groups** (§3.1.2, Figure 2 "Software Capabilities of a Software Factory", pp. 7–8, md:300–316). Figure 2 itself is an image and did not survive text extraction, so the component boxes inside it are **not recoverable from this cache** — flagged as a gap. The prose descriptions of each group are complete and are the best available substitute:

- **Infrastructure Capabilities** — "supply the hosting environment for the software factory, explicitly providing compute, storage, network resources, and additional CSP managed services to enable function, cybersecurity, and non-functional capabilities. Typically, this is either an approved or DoD provisionally authorized environment provided by a CSP but is not limited to a CSP." (md:302–306)
- **Digital Platform Capabilities** — "include the distinct development environments of the software factory, its CI/CD pipelines, a clearly implemented log aggregation and analysis strategy, and continuous monitoring operations. These capabilities should support multi-tenancy, enforce separation of duties for privileged users, and be considered part of the cyber survivability supply chain of the final software artifacts produced." Expanded in the next paragraph to include: "planning and backlog functionality, configuration management (CM) repositories, and local and released artifact repositories. Access control for privileged users is expected to follow an environment-wide least privilege access model. Continuous monitoring assesses the state of compliance for all resources and services evaluated against NIST SP 800-53 controls." (md:308–312)
- **Application Capabilities** — "include application frameworks, data stores such as relational or NoSQL databases and object stores, and other middleware unique to the application and outside the realm of the CI/CD pipeline." (md:314–316)

So the extractable official decomposition is roughly **13–15 named capabilities across 3 groups**, not 24, and it is a *capability* decomposition with no outcome or verification attached to any item. Anyone comparing a 24-slot proposal against this should note the official list is coarser and strictly nominal.

**RD v2.1 software factory lifecycle — four phases** (§4, p. 12, Figure 4, md:456): **Design, Instantiate, Verify, Operate & Monitor.** "Security is applied across all software factory phases."

**FUND v2.5 DevSecOps lifecycle — ten phases** (§2.2, pp. 3–4, md:222–240): Plan, Develop, Build, Test, Release, Deliver, Deploy, Operate, Monitor, Feedback. Each is given a one-line definition; the activity detail is explicitly pushed out to the *DevSecOps Fundamentals Guidebook: DevSecOps Activities & Tools* (May 2023), which is **not in the cache** and is where the actual required/preferred tool tables live for non-K8s factories.

### The "ideal software factory" seven properties

FUND §3.1.2, pp. 10–11 (md:363–379) — the nearest thing in FUND to an outcome list. Headings verbatim, with the load-bearing clauses:

1. **Standardization** — "Establishes standardized practices, processes, and tools… promotes consistency and reduces variability"
2. **Automation** — "Automates various activities of the software development lifecycle, including code compilation, testing, and deployment"
3. **CI/CD** — "It moves Developmental and Operational Test and Evaluation activities earlier in the CI/CD pipelines instead of bolted on at the end"
4. **Scalability and Flexibility** — "**It must be designed for multi-tenancy** and accommodate different types of applications, technologies, and deployment environments, including on-premises, cloud, and hybrid infrastructures"
5. **Security and Compliance** — "It provides a dynamically scalable set of pipelines with **three distinct cyber survivability control gates** and integrates security scanning tools, vulnerability assessments, and compliance checks to identify and address security issues early on… provides assurance as an AO that functional, security, integration, operational, and all other tests are reliably performed and passed prior to formal release and delivery"
6. **Collaboration and Communication** — "provides shared repositories, issue tracking systems, and collaboration tools"
7. **Continuous Improvement** — "collecting metrics, analyzing performance, and identifying areas for enhancement"

Item 5's "three distinct cyber survivability control gates" is the only quantified structural requirement in the list. The three gates are identifiable from the environment-promotion narrative (§3.1.2, pp. 9–10, md:331–339): **dev→test** (merge/peer review + CI), **test→integration**, and **integration→release/deliver**. Continuous Deployment adds a fourth, outside the pipeline: *"This is the first additional control gate outside of the control gates depicted in the software CI/CD pipeline"* (§3.2.4, p. 18, md:509).

### Tooling mandates — RD v2.1 REQUIRED / PREFERRED table (23 REQUIRED, 5 PREFERRED)

This is the only genuinely normative tool list in either document. Reconstructed from Tables 1–15.

| # | Tool / capability | Baseline | Locator |
|---|---|---|---|
| 1 | Logging agent | REQUIRED | Table 1, p. 10 (md:388) |
| 2 | Logging storage and retrieval service | REQUIRED | Table 1 (md:392) |
| 3 | Log visualization and analysis | **PREFERRED** | Table 1 (md:396) |
| 4 | Container policy enforcement (sidecar) | REQUIRED | Table 1 (md:402) |
| 5 | Runtime Defense — "Creates runtime behavior models, including whitelist and least privilege" | REQUIRED | Table 1 (md:408) |
| 6 | Service mesh proxy ("Only required if the application uses microservices") | REQUIRED | Table 1 (md:412) |
| 7 | Service mesh ("only required if the application uses microservices") | REQUIRED | Table 1 (md:416) |
| 8 | Vulnerability management | REQUIRED | Table 1 (md:420) |
| 9 | CVE service / host-based security | REQUIRED | Table 1 (md:426) |
| 10 | Zero Trust down to container level — "strong identities per Pod with certificates, mTLS tunneling and whitelisting of East-West traffic down to the Pod level" | REQUIRED | Table 1 (md:434) |
| 11 | CI/CD orchestrator — create pipeline workflow | REQUIRED | Table 2, p. 13 (md:474) |
| 12 | Container builder — "**Must use a hardened container image from Iron Bank as the base image in all cases**" | REQUIRED | Table 5, p. 18 (md:590) |
| 13 | Artifact repository / container registry | REQUIRED | Table 5 (md:604) |
| 14 | **TWO DIFFERENT** container security tools — "OS check. **Two are required because scan results are too disparate.**" | REQUIRED | Table 7, p. 19 (md:636) |
| 15 | Container policy enforcement (test phase) | REQUIRED | Table 7 (md:652) |
| 16 | Security compliance tool (STIG / NIST 800-53 scan) — benefit: "Speed up ATO process" | **PREFERRED** | Table 7 (md:664) |
| 17 | IaC / CaC — "Automated 'push button' instantiation of the applications running on K8s in addition to the software factory itself (including the SCSS stack on top)" | REQUIRED | Table 9, p. 20 (md:698) |
| 18 | GitOps Kubernetes capability — "Pull source code from git repositories instead of requiring the CI/CD pipeline to push artifacts to the next environment" | **PREFERRED** | Table 9 (md:704) |
| 19 | CNCF-certified Kubernetes | REQUIRED | Table 11, p. 21 (md:740) |
| 20 | Service mesh (deploy phase) | REQUIRED | Table 11 (md:764) |
| 21 | Resource/service/container policy enforcement (monitor) | REQUIRED | Table 14, p. 23 (md:828) |
| 22 | Vulnerability management (monitor) | REQUIRED | Table 14 (md:834) |
| 23 | CVE service / host-based security (monitor) | REQUIRED | Table 14 (md:840) |
| 24 | Netflow analysis | REQUIRED | Table 15, p. 23 (md:852) |
| 25 | Centralized logging | REQUIRED | Table 15 (md:858) |
| 26 | Centralized analysis (SIEM/SOAR, Tier 3 CSSP tools) | **PREFERRED** | Table 15 (md:866) |

Note #14 — **two different container scanners are mandatory**, justified on the grounds that one scanner's results cannot be trusted alone. That is the only redundancy-of-verification requirement in either document, and it is about scanning, not about build integrity.

### Tooling prohibitions

There is exactly one, and it is about APIs rather than tools:

> "It is critically important to **avoid the proprietary APIs** that are sometimes added by vendors on top of the existing CNCF Kubernetes APIs. These APIs are not portable and may create vendor lock-in!"
>
> — RD v2.1, §2 "Assumptions and Principles", p. 4 (md:263)

Everything else is positive mandate. The RD explicitly refuses to prescribe a toolchain:

> "There are no 'one size fits all' or hard rules about what CI/CD processes should look like and what tools must be used. Each software team needs to embrace the DevSecOps culture and define processes that suit its software system architectural choices."
>
> — RD v2.1, §4, p. 12 (md:462)

FUND reinforces this and adds a ratchet rule — reference designs may only *add* requirements, never remove them:

> "Every DevSecOps software factory and platform must include a minimal set of common tooling. The use of the word common is indicative of a class of tooling; it does not, nor should it be construed that the same tool must be used across every implementation."
>
> "DoD approved reference designs augment the DevSecOps Fundamentals Guidebook: DevSecOps Activities & Tools, adding in its environmentally specific required and preferred tooling. **Reference designs do not remove a required tool or activity, only augment.**"
>
> — FUND v2.5, §3.1.6 "Common Tools", pp. 14–15 (md:439, md:441–443)

### Other hard mandates in RD v2.1 (full list of normative `must`)

- "**Kubernetes must be part of the production environment.**" (§1.2, p. 1, md:162)
- "the selected Kubernetes implementation must have submitted conformance testing results for review and certification by the CNCF" (§2, p. 4, md:259)
- "**The SCSS must be used for cybersecurity monitoring of the application** in this reference design." (§4, p. 12, md:456)
- "The components of this reference design's software factory **must be instantiated as follows: A CSP-agnostic solution running a CNCF Certified K8s using hardened containers from Iron Bank.**" (§4, p. 12, md:460)
- "These tools are pluggable and must integrate into the CI/CD orchestrator. In this reference design, **instantiations must rely on a containerized software factory instantiated from a set of DevSecOps hardened containers from Iron Bank.**" (§4.1, p. 13, md:508)
- "If the build is successful and a container image is defined, **the pipeline must also trigger a container security scan.**" (§4.1, p. 14, md:518)
- "**Must leverage approved and hardened container images strictly from the Iron Bank repository**" (Table 4, p. 18, md:574)
- "**Containers must follow the DISA Container Hardening Guide.**" (Table 4, p. 18, md:578)
- "**The data format for the policies must be a structured machine-readable format, e.g. JSON or YAML.**" (Tables 1, 7, 14 — repeated three times, md:404, md:654, md:830)
- "Continuous monitoring of a K8s cluster **must include behavior and signature-based detection in the runtime environment.**" (§5.1, p. 24, md:878)
- "Each application team must determine how the application is decomposed into containers and the specific monitoring mechanisms within those." (§5.1, p. 24, md:882)
- "this reference design **mandates a container orchestration layer**" (§4.3, p. 16, md:538)

The repeated machine-readable-policy requirement is the **only machine-readability mandate in either document**, and it applies to policy-as-data (JSON/YAML), not to controls, evidence, or SBOMs.

---

## Theme: hardened containers, image provenance, scanning, and where images may come from

The registry model is the most prescriptive thing in either document. It is **source-restrictive and centrally-trusted**, with no local verification obligation.

**Where images may come from — Iron Bank, strictly:**

> "Container image selection | **Must leverage approved and hardened container images strictly from the Iron Bank repository**"
>
> — RD v2.1, Table 4 "Develop Phase Activities", p. 18 (md:574)

> "Container builder | Build a container image based on a build instruction file. **Must use a hardened container image from Iron Bank as the base image in all cases.**"
>
> — RD v2.1, Table 5 "Build Phase Tools", p. 18 (md:592)

**The local mirror pattern** — a locally centralised repository that pulls from Iron Bank and also holds locally built artefacts:

> "A Locally Centralized Artifact Repository is a local repository tied to the software factory. It stores artifacts pulled from Iron Bank, the DoD repository of **digitally signed** binary container images that have been hardened. The local artifact repository also stores locally developed artifacts used in the DevSecOps processes. Artifacts stored here include, but are not limited to, container images, binary executables, virtual machine (VM) images, archives, and documentation."
>
> — RD v2.1, §3.3, p. 7 (md:338)

> "Programs may opt for a single artifact repository and rely on the use of tags to distinguish between the different content types. It is also permissible to have separate artifact repositories to store local artifacts and released artifacts."
>
> — RD v2.1, §3.3, p. 7 (md:346) — echoed in FUND's "Artifact Repository" glossary entry, p. 34 (md:957)

**Provenance claim** — Iron Bank signs; no one is told to check the signature:

> "The Iron Bank artifact repository provides hardened, secure technical implementation guide (STIG) compliant, and centrally updated, scanned, and signed containers that increases the cyber survivability of these software artifacts. At time of writing this reference design, over 300 artifacts were in Iron Bank, with more being added continuously."
>
> — RD v2.1, §3.3, pp. 7–8 (md:340–344)

This is the whole of the provenance story. The word "signed" appears **twice** in the RD, both times as a property of Iron Bank's output (md:338, md:340). The word "signature" appears twice and both are **antivirus-style CVE signatures, not cryptographic signatures**: "Signature-based continuous scanning using Common Vulnerabilities and Exposures (CVEs)" (§3.4, p. 9, md:376) and "must include behavior and signature-based detection in the runtime environment" (§5.1, p. 24, md:878). **FUND v2.5 contains the word "signed" zero times** (the three naive grep hits are all "designed").

**Scanning requirements** — this is where the RD invests:

- Two independent container security tools, mandatory (Table 7, p. 19, md:636) — "OS check. Two are required because scan results are too disparate."
- A container security scan must fire on every image build (§4.1, p. 14, md:518).
- Container policy enforcement at Test (Table 7, md:652) and at Monitor (Table 14, md:828), both REQUIRED, both with machine-readable policy formats.
- Vulnerability management and a CVE service, REQUIRED in both the sidecar and the Monitor phase (md:420, md:426, md:834, md:840).
- Hardening to the DISA Container Hardening Process Guide V1R1 (Table 4, md:578).
- Security compliance scanning against STIGs and NIST 800-53 is only **PREFERRED** (Table 7, md:664).

**Immutability** is asserted as a benefit of hardened containers, with no enforcement mechanism:

> "Adoption of hardened containers as a form of immutable infrastructure results in standardization of common infrastructure components that achieve consistent and predictable results."
>
> — RD v2.1, §2, p. 4 (md:265)

FUND's glossary (p. 36, md:1023) defines immutable infrastructure as "computer infrastructure (virtual machines, containers, network appliances) that cannot be changed once deployed", sourced to `glossary.cncf.io`.

**The gap, stated plainly for the site:** the model is *trust by source and rescan*, not *verify by signature*. Images must come from Iron Bank; Iron Bank signs them; nothing in either document requires anyone to verify that signature at pull, at build, at admission, or at deploy. The verification burden is discharged by scanning the artefact again locally with two different scanners. That is a defensible 2021 design, and it is exactly the thing the 2021 SolarWinds-era supply-chain literature moved away from.

---

## Theme: what is NOT demanded — search results in full

Every term below was searched case-insensitively across both complete documents, including the contents pages, figure captions, tables, footnotes, acronym list and glossary.

| Term searched | RD v2.1 | FUND v2.5 | Verdict |
|---|---|---|---|
| `reproducib*` (reproducible build, reproducibility) | **0** | **0** | **Confirmed absent.** Also 0 across all eight cached DoD sources. |
| `OSCAL` | **0** | **0** | **Confirmed absent.** Also 0 across all eight cached DoD sources. |
| `admission` (admission control, admission controller, admission webhook) | **0** | **0** | **Confirmed absent.** |
| `signature verification` / signature as cryptographic | **0** | **0** | **Confirmed absent.** RD's 2 `signature` hits are CVE/AV signatures; its 2 `signed` hits describe Iron Bank. FUND: 0 of either. |
| `attestation` / `attest*` | **0** | **0** | **Confirmed absent.** |
| `SLSA` | **0** | **0** | **Confirmed absent.** |
| `in-toto` / `intoto` | **0** | **0** | **Confirmed absent.** |
| `Sigstore` | **0** | **0** | **Confirmed absent.** |
| `cosign` | **0** | **0** | **Confirmed absent.** |
| `provenance` | **0** | **0** | **Confirmed absent.** |
| `notary` | **0** | **0** | **Confirmed absent.** |
| `hash` / `checksum` / `digest` | **0** | **0** | **Confirmed absent.** No artefact-identity-by-content anywhere. |
| `SBOM` | **0** | **1** | **PRESENT AND REQUIRED in FUND** — see below. |
| `Bill of Materials` | **0** | **1** | Same single occurrence. |
| `OPA` / `Gatekeeper` / `Kyverno` | **0** | **0** | Absent — "container policy enforcement" is named generically and product-agnostically. |
| `air gap` / `air-gap` / `airgap` | **0** | **0** | **Confirmed absent** as a phrase (see disconnected-operation section below for what *is* said). |
| `inherit*` / `common control` | **0** | **3** | RD absent; FUND has them only re IaC baselines and CSP PaaS. |
| `isolation test` / `demonstrated isolation` | **0** | **0** | **Confirmed absent.** |
| `avoided if possible` / `build your own` | **0** | **0** | Absent from both; exists in the Continuous Authorization Implementation Guide. |

**The one correction in this table.** SBOM is not merely mentioned — it is required, and it is required as a condition of cATO:

> "cATO includes the need for a Secure Software Supply Chain (SSSC) and **requires a Software Bill of Materials (SBOM)**."
>
> — FUND v2.5, §3.3.1.2, p. 22 (md:576), emphasis added

Three things about that sentence are worth the site's attention. It is the **only** occurrence of SBOM in 44 pages. **SBOM is not in FUND's acronym list** (pp. 32–33) and not in its glossary (pp. 34–38) — the one hard supply-chain artefact requirement in the document is defined nowhere in it. And nothing states **what format, what depth, when generated, who consumes it, or what happens if it is absent**. It is a requirement with no verification and no acceptance criterion. That is still a demand, and the site must not claim zero references to SBOM.

A near-miss worth noting: FUND's glossary entry for Continuous Integration (p. 35, md:997–1001) lists "dependency/BOM checking" among the security scans CI should run — "The security scans include, but are not limited to, dynamic code analysis, test coverage, **dependency/BOM checking**, and compliance checking." That is the only other BOM-adjacent text, it is in a glossary not a requirements table, and it is "not limited to" hedged.

**The supply-chain framing that *is* present** — FUND leans on NIST, and the quoted NIST passage is nearly an argument for exactly the things FUND then fails to require:

> "Per NIST SP 800-204D, 'Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines,' a software supply chain **must not** be reduced to merely a set of artifacts. Every software supply chain **must explicitly address every link** that exists between writing source code through production deployment:
>
> '*While software composition (e.g., dependency management) is under the purview of software supply chain activities, other often overlooked activities are central to the software supply chain. This includes writing source code; building, packaging, and delivering an application; and repackaging and containerization.*'"
>
> — FUND v2.5, §3.1.4, p. 13 (md:409–411)

And the observability-over-each-link requirement, which is the closest FUND gets to build-integrity evidence:

> "It is crucial to monitor each step, or link, in the software supply chain across every segment of the CI/CD pipeline. This monitoring involves **collecting and analyzing comprehensive metadata at each stage**, providing visibility into the entire process."
>
> — FUND v2.5, §3.1.4, pp. 13–14 (md:419–421)

"Comprehensive metadata at each stage" is as near as either document comes to attestation. It names no format, no signing, no verification, and no consumer. The site can fairly say: **DoD asks for metadata about every link in the chain and never once asks for that metadata to be signed or checked.**

FUND also cites NIST SP 800-218 (SSDF) and its four practice groups — Prepare the Organization, Protect the Software, Produce Well-Secured Software, Respond to Vulnerabilities (§3.3.1.2, pp. 21–22, md:561–574) — with the obligation stated as *"software factories **should** follow"*. The SSDF is where signing and provenance requirements actually live; FUND incorporates it by reference at "should" strength and does not restate any of its content.

---

## Theme: required artefacts

**Neither document contains a consolidated "a compliant factory must produce X" list.** Searched: `deliverable`, `artifact list`, `evidence`, `documentation required`, `shall produce`, `required artifacts`. No such section exists. The closest available is reconstructive, and comes from the Outputs columns of RD v2.1's activity and tool tables. Compiled in full here because it is the nearest thing to an official outcome list:

| Artefact | Produced by | Locator |
|---|---|---|
| Pipeline workflow configuration | CI/CD orchestrator (create workflow) | Table 2, p. 13 (md:488) |
| Pipeline workflow execution results — "control gate validation, stage transition, activity execution" | CI/CD orchestrator | Table 2 (md:502) |
| **Event and activity audit logs** — benefit stated as "Auditable trail of activities" | CI/CD orchestrator | Table 2 (md:496, md:504) |
| Vulnerability report and recommended mitigation | Container hardening (Develop) | Table 4, p. 18 (md:580) |
| **Hardened container & build file** | Container hardening (Develop) | Table 4 (md:582) |
| OCI-compliant container image | Container builder (Build) | Table 5, p. 18 (md:600) |
| Container image | Containerize activity (Build) | Table 6, p. 19 (md:624) |
| **Version-controlled container image** | Store artifacts (Build) | Table 5 & 6 (md:608, md:628) |
| Vulnerability report and recommended mitigation ×2 (two scanners) | Container security tools (Test) | Table 7, p. 19 (md:648) |
| **Compliance report** | Container policy enforcement (Test) | Table 7 (md:660) |
| Container compliance report | Container policy enforcement activity (Test) | Table 8, p. 20 (md:690) |
| Vulnerability report (STIG / NIST 800-53) — PREFERRED only | Security compliance tool (Test) | Table 7 (md:672) |
| **Release go / no-go decision** + "Artifacts are tagged with release tag if go decision is made" | Release go/no-go activity | Table 10, p. 21 (md:730–732) |
| Running container | CNCF-certified Kubernetes (Deploy) | Table 11, p. 21 (md:762) |
| New container instance in the registry | Deliver container to registry (Deploy) | Table 12, p. 22 (md:792) |
| Control-plane service status reports; data-plane routed comms | Service mesh (Deploy) | Table 11 (md:776–778) |
| Scale policy; optimised resource allocation | Scale (Operate) | Table 13, p. 22 (md:806–808) |
| Balanced resource utilisation | Load balancing (Operate) | Table 13 (md:818) |
| Aggregated logs forwarded to Tier 2 CSSP; incident alerts and reports | Continuous monitoring / SIEM-SOAR | §5.1, p. 24 (md:882) |
| Change requests generated from incidents — "makes the DevSecOps pipeline a full closed loop from secure operations to planning" | Incident management | §5.1, p. 25 (md:890) |

Inputs to the release go/no-go gate are specified and are effectively the evidence bundle (Table 10, p. 21, md:724–728): **"Design documentation; Version controlled artifacts; Version controlled test reports; Security test and scan reports."**

Observe what is on this list and what is not. Reports, decisions, tags and logs — all of them. **No build record, no provenance record, no SBOM, no signature, no attestation, no bill of materials.** The RD's artefact set is entirely *scan output and human decision*. FUND adds SBOM once, at cATO level, outside any table.

---

## Theme: air-gapped, disconnected and classified operation; impact levels

`air gap` / `air-gap` / `airgap` is **absent from both documents**. What exists:

**FUND v2.5 — the requirement that factories work disconnected and at multiple classifications:**

> "DoD needs multiple software factories tuned for specific types of software systems, such as web applications or embedded systems that may include significant amounts of HWIL for automated testing. **It also requires software factories operating at varying classification levels in both cloud and on-premises or disconnected environments.**"
>
> — FUND v2.5, §3.1.2, p. 10 (md:359), emphasis added

That is the entire treatment. One sentence. No guidance on how, no cross-domain transfer, no mirror/sync model, no impact-level mapping.

FUND also pushes back on "isolated" as a mental model, which is relevant if the site argues about disconnected provenance:

> "It is easy, but naïve and incorrect, to dismiss an embedded system in a projectile as 'isolated' and disconnected. The projectile includes embedded software that was compiled leveraging 3rd party libraries and links to hardware drivers and relies upon features of embedded firmware."
>
> — FUND v2.5, §3.1.1, p. 6 (md:284)

And the deployment-to-disconnected-asset problem, memorably:

> "if this artifact is destined for an underwater resource, it may be several orders of magnitude harder to automatically push a 750MB release of software to a submersed vehicle operating at 300 feet below the surface of the ocean."
>
> — FUND v2.5, §3.2.4, p. 18 (md:515)

FUND's Figure 4 case — production environment outside the factory's ATO boundary — is the structural version of this: *"a second software factory use case where the production environment is external to the software factory security boundaries as defined in their Authorization to Operate (ATO) (e.g., software developed and delivered to a weapons system or afloat asset)"* (§3.1.2, p. 8, md:324).

**Impact levels.** FUND v2.5 mentions them **once**, and only as an acronym expansion: "IL | Impact Level" (acronym list, p. 33, md:893). The term is never used in the body. RD v2.1 is the only one that assigns them:

> "A Cloud Native Access Point (CNAP) provides a zero-trust architecture on Cloud One to provide access to development, testing, and production enclaves at **Impact Level 2 (IL-2), Impact Level 4 (IL-4), and Impact Level 5 (IL-5)**. CNAP provides access to Platform One DevSecOps environments by using an internet-facing Cloud-native zero trust environment."
>
> — RD v2.1, §3.1, p. 6 (md:302), citing the DISA Cloud Computing SRG v1r3

**IL-6 and above are never mentioned in either document.** The ceiling in the reference design is IL-5.

**Classified operation, RD v2.1** — one sentence, framed as a containerisation benefit rather than a requirement:

> "Containerization of the entire CI/CD stack ensures there is no drift possible between different K8s cluster environments (development, test, staging, production). **It further ensures there is no drift between different K8s cluster environments spanning multiple classification levels.** Containerization also streamlines the update/accreditation process associated with the introduction and adoption of new DevSecOps tooling."
>
> — RD v2.1, §4.1, p. 13 (md:510), emphasis added

**Hosting is deliberately unconstrained**, which is the RD's main concession to on-prem and edge:

> "The reference design does not constrain the software factory hosting environment, which could be a Cloud Service Provider with a DoD provisional authorization or ATO, DoD data centers or even on-premises servers."
>
> — RD v2.1, §4.2, p. 15 (md:532)

> "This enables a Cloud agnostic, elastic instantiation of a DevSecOps software factory anywhere: Cloud, On Premise, Embedded System, Edge Computing."
>
> — RD v2.1, §1.2, p. 1 (md:160)

> "Kubernetes provides an API that ensures total abstraction of orchestration, compute, storage, networking, and other core services that guarantees software can run in any environment, from the Cloud to being embedded inside platforms like jets or satellites."
>
> — RD v2.1, §3.2, p. 7 (md:318)

---

## Supporting material the site may want

**The product-rule security argument** — the most quotable passage in FUND, and a genuinely good argument for caring about every link:

> "the cybersecurity and risk postures of a specific artifact or application would be calculated using the product rule across the entirety of the software supply chain. If the compiler is 90% secure, the code repository is 90% secure, the artifact repository is 90% secure, and the container orchestrator is 90% secure – the overall system is not 90% secure. The cybersecurity level of the end-to-end ecosystem is actually .9 * .9 *.9 * .9, or roughly 65% secure."
>
> "if a DevSecOps team only increases security 5%, raising each level from 90% to 95%, then overall cyber survivability security jumps from 65% to 81%."
>
> — FUND v2.5, §3.1.1, pp. 6–7 (md:286–288)

**Released ≠ deployed** — FUND is emphatic, twice (§3.1.2, p. 10, md:341–343; §3.2.3, p. 17, md:500):

> "**Released is never equivalent to Deployed!** This is a source of confusion for many. A released artifact is available for deployment. Deployment may or may not occur instantly."

**cATO's effect on per-application authorisation:**

> "Under the shift to a cATO, each software factory will have its processes, teams, and storage reviewed, certified, and continuously monitored to allow them to deploy applications into a continuously monitored system. This shift greatly lessens the initial burden of achieving an ATO for each piece of software, as the process and roll out are certified and fed into a continuous monitoring architecture."
>
> — FUND v2.5, §3.1.2, p. 10 (md:361)

**Zero trust is mandatory for factories and platforms:**

> "DevSecOps software factories and platforms **must adopt zero trust as the target security model** for cybersecurity. Teams should consistently strive to bake in as many of the zero trust principles as are supported by their architecture across each of the ten phases of the DevSecOps lifecycle."
>
> — FUND v2.5, §3.3.1.1, p. 20 (md:545)

**The RD's stated audiences** (§1.2, pp. 1–2, md:170–185) are a useful four-way split: hardened-container providers; platform/baseline providers; organisation DevSecOps teams who instantiate and maintain factories; program application teams who use them; plus Authorizing Officials.

**Platform One is named as the reference implementation** in both: *"Platform One is the first DoD-wide approved DevSecOps Managed Service"* (RD §4.1, p. 15, md:526); and FUND points to Big Bang (§3.1.3, p. 12, md:399) and to the CAC-gated *DoD DevSecOps Platform and Software Factory Inventory* at `https://go.intelink.gov/ab7U5ad` (§3.1.2, p. 11, md:383–385).

**Non-inclusive language in the source.** RD v2.1 uses "whitelist"/"whitelisting" three times (md:368, md:408, md:436) in normative requirements text. If the site quotes Table 1 verbatim, flag it with `[sic]` rather than silently altering a quotation.

---

## Gaps and limits of this extraction

- **All figures are lost.** Both documents were extracted as text; every `Figure N` is a caption with no image. The casualties that matter: RD **Figure 5** (Containerized Software Factory Reference Design), RD **Figure 7** (Software Factory – DevSecOps Services), RD **Figure 1** (the interconnect diagram), FUND **Figure 2** (Software Capabilities of a Software Factory) and FUND **Figure 5** (DevSecOps Platform). Figure 2 is the official component decomposition and is the single most relevant thing for checking a 24-slot proposal against. Its *prose* description is captured above, but the boxes inside the diagram are not recoverable from this cache.
- **Table extraction is lossy.** The markdown has flattened RD tables into runs of cell text without row boundaries. Row-to-baseline mappings above were reconstructed by reading cell order and are reliable, but exact column alignment for any given row should be re-checked against the PDF before being quoted as a table.
- **RD v1.0 (2019) is not available.** Any claim about the 2019 edition cannot be verified from this material.
- **Two referenced documents that carry the actual requirements are not cached**: the *DevSecOps Fundamentals Guidebook: DevSecOps Activities & Tools* (May 2023) — where the required/preferred tool tables for non-Kubernetes factories live — and the *DISA Container Hardening Process Guide V1R1* (15 Oct 2020), which is the sole normative authority for what "hardened" means. Both are load-bearing for the site's argument and neither has been read.
- FUND v2.5 §1.6-equivalent change log does not exist; there is no "what's new in v2.5" section, so the delta from v2.0 cannot be established from this document.
