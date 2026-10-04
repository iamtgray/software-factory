# Evidence Status

Every claim on this site carries a confidence level. The research conditions make the distinction unusually important.

## Why this page exists

The research ran **without a working search engine**. The fetch tooling failed throughout, and every general search engine was blocked by CAPTCHAs or rate limits. Everything came from constructing likely URLs, cloning repositories and grepping them, and using open APIs -- plus, late on, a text-extraction proxy that defeated the government-site blocking which had stopped everything else.

That cuts two ways:

**Positive findings are unusually strong.** They came from reading specifications, source code and commit histories rather than summarising secondary coverage. Several corrections on this site exist precisely because someone read the source instead of the documentation.

**Every negative finding is weak.** "We found no X" means "we did not find one by the methods available".

## The levels

| Status | Meaning | How to use it |
|---|---|---|
| **Verified** | Checked against a primary source directly in this programme | Quote it, including to customers |
| **Primary** | Read from a specification, repository or vendor document, with the source cited | Strong; attribute it |
| **Weak negative** | "We found no X", with no search engine available | A lead, not a fact |
| **Unverified** | Flagged as unconfirmed | Do not repeat externally |
| **Blocked** | Not publicly knowable | Needs a cleared conversation |
| **Corrected** | Previously asserted, then found wrong | The correction is the finding |

## Verified

Checked directly, mostly by reading source and commit history:

- A cross-domain export script verifies a signature on the low side and then **discards it**, shipping a bare archive. The repository containing it has **no licence file anywhere** -- source-available, legally unusable, evidence only.
- A major platform is **not** an umbrella Helm chart with subcharts, contrary to universal assumption. It templates Flux resources. Its values file is **2,653 lines** with a **224 KB** schema.
- That platform's security-scanning slot is filled by **commercial** products. An all-open-source version does not exist.
- Its OSCAL file has **six commits in its entire history**; the last substantive edit was April 2023, and later commits are a URL fix and a global find-and-replace. The metadata still claims 2022.
- A widely-recommended Kubernetes distribution documents **FIPS 140-2**, not 140-3, and states that **only the default network plugin is rebuilt for FIPS** -- so choosing the better network-policy option breaks the FIPS claim.
- **OMB M-26-05 rescinds the US federal software self-attestation regime**, in those words, describing the prior policy as having "imposed unproven and burdensome software accounting processes".
- What survived it: maintain a complete inventory, and provide "**an SBOM of the runtime production environment** upon request".
- A cloud compliance framework requires that "authoritative sources are used to **automatically generate real-time inventories** of all information resources when needed" -- the strongest regulatory support the thesis has, found in a public git repository.
- The **cATO memo** authorises *systems*, not organisations, and requires that "**all** security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism" for assessors.
- One composition tool publishes its latest release as a rolling `latest` tag with no semantic version since 2024 -- **unpinnable, therefore unusable air-gapped.** Its main alternative is a release candidate.
- The tool that issues signed verdicts over attestation sets is **actively maintained** despite 44 stars -- bus-factor risk, not abandonment.

## Corrected

Each of these was asserted confidently and then demolished:

| Original claim | Status | Corrected to |
|---|---|---|
| "No open-source project is a software factory, and ours produces SBOMs" | **Falsifiable in 90 seconds** | One project self-describes in exactly those words; SBOM generation is commodity |
| **"Evidence does not cross the air-gap with the artefact"** | **Refuted** | It does, by default, in common tooling. What is missing is that **nothing on the far side is obliged to look** |
| "Only one cross-domain implementation exists in open code" | **Refuted** | A universal negative asserted with no code search. Counter-examples found within minutes |
| "The OSCAL file was untouched for 3.5 years" | **Wrong mechanism** | Six commits; mechanical sweeps make it *look* maintained |
| "Three primitives suffice" | **Incomplete** | **Five** -- trust configuration and freshness state were being treated as manifest fields |
| "CDR delivers close to zero security benefit" | **Overreach** | No CDR engine has a sanitiser for compiled code; cite the measured 13% soundness figure instead |
| "Review becomes the bottleneck" | **Imprecise** | **Reviewer attention** is scarce; build and test capacity *rise* in importance |

Eight load-bearing claims went to adversarial verification; seven were adjudicated before an outage killed the eighth. **Two refuted, five weakened, nothing survived intact.**

## Blocked

Not publicly knowable. Needs cleared conversations:

- **What a real cross-domain guard accepts** -- six of seven necessary parameters. This blocks the transfer-format design outright.
- Controlled requirement sets, baseline lists and assessment methodologies.
- How software actually enters classified cloud regions.
- Whether frontier model APIs exist in classified regions, for a given region and model.
- Alliance-level information exchange gateway specifications.

## Weak negatives

Treat as leads. Re-check if search access improves:

- "No published standard, vendor document or paper reconciles transform-based inspection with artefact signing." *This one is load-bearing, and it's weak.*
- "No standard exists for attesting AI-generated code."
- "No regime imposes requirements on AI-generated code in assured software."
- "No policy addresses handling assurance evidence across classification boundaries."
- "No tooling exists for runtime or deployed SBOMs." *Which is awkward, because that's now the surviving US obligation.*

## Unverified

Flagged by the research, not confirmed:

- A registry's replication may silently drop signatures made with older signing tooling. If true, a transport conformance test is mandatory.
- Open-core pricing-tier boundaries throughout -- pricing pages were not fetchable.
- The current regulatory position on AI in assured software. **Needs a dedicated pass before anything citing a regulator is written.**
- One analyst forecast that 40% of companies will downgrade or disable autonomous agents by 2027 due to governance gaps. No primary analyst material was obtainable at all.

## The standing rule

!!! danger "No claim may assert a universal negative over open code."
    Learned the hard way. Without code search at scale, "we found none" means "we did not find one", and the strength of that depends entirely on how you looked -- which must be stated.
