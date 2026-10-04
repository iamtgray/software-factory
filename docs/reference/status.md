# What you can quote

Claims on this site are meant to carry a confidence level, and if you find one that doesn't, treat it as unverified until someone has checked it.

## The levels

| Status | Meaning | What you may do with it |
|---|---|---|
| **Verified** | Checked against a primary source directly | Quote it, including to customers |
| **Primary** | Read from a specification, repository or vendor document, with the source cited | Strong; attribute it |
| **Weak negative** | "No X was found" | Treat it as a lead to chase. Do not assert it |
| **Unverified** | Flagged as unconfirmed | Do not let it leave the room |
| **Blocked** | Not publicly knowable | Say so plainly, and get a cleared conversation |

Negatives here are weak because there was no search engine to hand -- "No X was found" means none was found by the methods available, and a better search may well turn X up tomorrow.

!!! danger "One source is not publicly quotable at all"
    The **DevSecOps Continuous Authorization Implementation Guide** carries **Distribution Statement C** -- US Government agencies and their contractors only.

    Nothing from it may appear on a public site, in a public deck, or in a document going to an uncleared third party.

## Verified -- quote these

Checked against primary sources, mostly source and commit history:

- A cross-domain export script verifies a signature on the low side and then **discards it**, shipping a bare archive. There's no **licence file anywhere** in the repository that holds it.
- The assumption I keep running into (that a major platform is an umbrella Helm chart with subcharts) is wrong. It templates Flux resources. Its values file is **2,653 lines** with a **224 KB** schema.
- That platform's security-scanning slot is filled by **commercial** products, so an all-open-source equivalent is something you'd be building yourself.
- Its OSCAL file has **six commits in its entire history**; the last substantive edit was April 2023, and later commits are a URL fix and a global find-and-replace. The metadata still claims 2022.
- A widely-recommended Kubernetes distribution documents **FIPS 140-2** throughout, a generation behind the current **140-3**, and states that **only the default network plugin is rebuilt for FIPS**. So choosing the better network-policy option breaks the FIPS claim.
- **OMB M-26-05 rescinds the US federal software self-attestation regime**, in those words, describing the prior policy as having "imposed unproven and burdensome software accounting processes".
- What survived it: maintain a complete inventory, and provide "**an SBOM of the runtime production environment** upon request".
- A cloud compliance framework requires that "authoritative sources are used to **automatically generate real-time inventories** of all information resources when needed". It's in a public git repository.
- The **cATO memo** authorises individual *systems*, and the authorisation it grants stops at the system boundary. It requires that "**all** security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism" for assessors. **But the 2024 evaluation criteria weakened "all" to "which"** and accept "screen shots of control gate output as displayed in a dashboard" as evidence. The memo itself also licenses the manual route -- "Manual controls will have different timelines associated" -- so it can't be presented as the current standard.
- One composition tool publishes its latest release as a rolling `latest` tag with no semantic version since 2024 -- **unpinnable, therefore unusable air-gapped.** Its main alternative is a release candidate.
- The tool that issues signed verdicts over attestation sets is **actively maintained** on 44 stars.

## Blocked -- say it is not knowable

I couldn't get at any of these from open sources, so a cleared conversation is the only route:

- **What a real cross-domain guard accepts** -- six of seven necessary parameters. This blocks the transfer-format design outright.
- Controlled requirement sets, baseline lists and assessment methodologies.
- How software actually enters classified cloud regions.
- Whether frontier model APIs exist in classified regions, for a given region and model.
- Alliance-level information exchange gateway specifications.

## Weak negatives -- do not assert these

Treat as leads. Re-check if search access improves:

- "No published standard, vendor document or paper reconciles transform-based inspection with artefact signing."
- "No standard exists for attesting AI-generated code."
- "No regime imposes requirements on AI-generated code in assured software."
- "No policy addresses handling assurance evidence across classification boundaries."

!!! warning "One weak negative is wrong -- do not repeat it"
    **"No tooling exists for runtime or deployed SBOMs" is wrong.** A Kubernetes operator for the *Deployed* SBOM type exists at a few hundred stars. Runtime SBOM tooling looks thin, though I haven't put a number on that. The runtime SBOM is now the surviving US federal obligation.

    Open source carries several one-way transfer implementations (`hairgap`, `eurydice` and ANSSI's `lidi`). Where this site says "zero projects address cross-domain", that's scoped to the 2,430-project catalogue surveyed.

## Unverified -- these must not leave the room

- A registry's replication may silently drop signatures made with older signing tooling. If that's right, a transport conformance test is mandatory.
- Open-core pricing-tier boundaries throughout -- the pricing pages wouldn't fetch.
- The current regulatory position on AI in assured software. **Needs a dedicated pass before anything citing a regulator is written.**
- One analyst forecast that 40% of companies will downgrade or disable autonomous agents by 2027 due to governance gaps. I couldn't get at the primary analyst material at all.

## Before it goes in a deck

Check what status the claim carries, and whether the room you're standing in clears that status. If you're unsure about the second, don't use the claim.
