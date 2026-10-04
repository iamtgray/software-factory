# What You Can Quote

Every claim on this site carries a confidence level, and the level decides where you can repeat it: to a customer, inside the room, or not at all. Use this page before you put anything in a deck.

## The levels, and what each licenses

| Status | Meaning | What you may do with it |
|---|---|---|
| **Verified** | Checked against a primary source directly | Quote it, including to customers |
| **Primary** | Read from a specification, repository or vendor document, with the source cited | Strong; attribute it |
| **Weak negative** | "No X was found" | A lead, not a fact. Do not assert it |
| **Unverified** | Flagged as unconfirmed | Do not let it leave the room |
| **Blocked** | Not publicly knowable | Say so plainly, and get a cleared conversation |

Negatives are weak because no search engine was available, so "no X was found" means "none was found by the methods available" — which is not absence, and in particular no universal negative over open code can be asserted.

!!! danger "One source is not publicly quotable at all"
    The **DevSecOps Continuous Authorization Implementation Guide** carries **Distribution Statement C** — US Government agencies and their contractors only.

    Nothing from it may appear on a public site, in a public deck, or in a document going to an uncleared third party. This matters because several of the things the project most wants to cite are inside it.

## Verified -- quote these

Checked against primary sources, mostly source and commit history:

- A cross-domain export script verifies a signature on the low side and then **discards it**, shipping a bare archive. The repository containing it has **no licence file anywhere** -- source-available, legally unusable, evidence only.
- A major platform is **not** an umbrella Helm chart with subcharts, contrary to universal assumption. It templates Flux resources. Its values file is **2,653 lines** with a **224 KB** schema.
- That platform's security-scanning slot is filled by **commercial** products. An all-open-source version does not exist.
- Its OSCAL file has **six commits in its entire history**; the last substantive edit was April 2023, and later commits are a URL fix and a global find-and-replace. The metadata still claims 2022.
- A widely-recommended Kubernetes distribution documents **FIPS 140-2**, not 140-3, and states that **only the default network plugin is rebuilt for FIPS** -- so choosing the better network-policy option breaks the FIPS claim.
- **OMB M-26-05 rescinds the US federal software self-attestation regime**, in those words, describing the prior policy as having "imposed unproven and burdensome software accounting processes".
- What survived it: maintain a complete inventory, and provide "**an SBOM of the runtime production environment** upon request".
- A cloud compliance framework requires that "authoritative sources are used to **automatically generate real-time inventories** of all information resources when needed" -- the strongest regulatory support the thesis has, and it is in a public git repository.
- The **cATO memo** authorises *systems*, not organisations, and requires that "**all** security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism" for assessors. **But the 2024 evaluation criteria weakened "all" to "which"**, accept "screen shots of control gate output as displayed in a dashboard" as evidence, and list automated control validation as an *objective* rather than a threshold requirement. The memo cannot be presented as the current standard.
- One composition tool publishes its latest release as a rolling `latest` tag with no semantic version since 2024 -- **unpinnable, therefore unusable air-gapped.** Its main alternative is a release candidate.
- The tool that issues signed verdicts over attestation sets is **actively maintained** despite 44 stars -- bus-factor risk, not abandonment.

## Blocked -- say it is not knowable

Not publicly knowable. These need cleared conversations, not more research:

- **What a real cross-domain guard accepts** -- six of seven necessary parameters. This blocks the transfer-format design outright.
- Controlled requirement sets, baseline lists and assessment methodologies.
- How software actually enters classified cloud regions.
- Whether frontier model APIs exist in classified regions, for a given region and model.
- Alliance-level information exchange gateway specifications.

## Weak negatives -- do not assert these

Treat as leads. Re-check if search access improves:

- "No published standard, vendor document or paper reconciles transform-based inspection with artefact signing." *This one is load-bearing, and it's weak.*
- "No standard exists for attesting AI-generated code."
- "No regime imposes requirements on AI-generated code in assured software."
- "No policy addresses handling assurance evidence across classification boundaries."
- "No tooling exists for runtime or deployed SBOMs." *Which is awkward, because that's now the surviving US obligation.*

## Unverified -- these must not leave the room

- A registry's replication may silently drop signatures made with older signing tooling. If true, a transport conformance test is mandatory.
- Open-core pricing-tier boundaries throughout -- pricing pages were not fetchable.
- The current regulatory position on AI in assured software. **Needs a dedicated pass before anything citing a regulator is written.**
- One analyst forecast that 40% of companies will downgrade or disable autonomous agents by 2027 due to governance gaps. No primary analyst material was obtainable at all.
