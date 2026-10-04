# What You Can Quote

Claims on this site are meant to carry a confidence level, and if you find one that doesn't, treat it as unverified until someone has checked it. The level decides where you can repeat it: to a customer, inside the room, or nowhere. Worth a read before you put anything in a deck.

## The levels, and what each licenses

| Status | Meaning | What you may do with it |
|---|---|---|
| **Verified** | Checked against a primary source directly | Quote it, including to customers |
| **Primary** | Read from a specification, repository or vendor document, with the source cited | Strong; attribute it |
| **Weak negative** | "No X was found" | Treat it as a lead to chase. Do not assert it |
| **Unverified** | Flagged as unconfirmed | Do not let it leave the room |
| **Blocked** | Not publicly knowable | Say so plainly, and get a cleared conversation |

Negatives here are weak because there was no search engine to hand. So "No X was found" means one thing: none was found by the methods available. A better search may well turn X up tomorrow. I don't think a flat negative over open code survives contact with reality at all -- the corpus is far too big for anyone to claim they've swept it.

!!! danger "One source is not publicly quotable at all"
    The **DevSecOps Continuous Authorization Implementation Guide** carries **Distribution Statement C** -- US Government agencies and their contractors only.

    Nothing from it may appear on a public site, in a public deck, or in a document going to an uncleared third party. Awkward, because several of the things the project most wants to cite are inside it.

## Verified -- quote these

Checked against primary sources, mostly source and commit history:

- A cross-domain export script verifies a signature on the low side and then **discards it**, shipping a bare archive. I couldn't find **a licence file anywhere** in the repository that holds it -- source-available, legally unusable, evidence only.
- The assumption I keep running into (that a major platform is an umbrella Helm chart with subcharts) is wrong. It templates Flux resources. Its values file is **2,653 lines** with a **224 KB** schema.
- That platform's security-scanning slot is filled by **commercial** products, so an all-open-source equivalent looks like something you'd be building yourself.
- Its OSCAL file has **six commits in its entire history**; the last substantive edit was April 2023, and later commits are a URL fix and a global find-and-replace. The metadata still claims 2022.
- A widely-recommended Kubernetes distribution documents **FIPS 140-2** throughout, a generation behind the current **140-3**, and states that **only the default network plugin is rebuilt for FIPS**. Read straight, that means choosing the better network-policy option breaks the FIPS claim, and I'd be glad to be told I've read it wrong.
- **OMB M-26-05 rescinds the US federal software self-attestation regime**, in those words, describing the prior policy as having "imposed unproven and burdensome software accounting processes".
- What survived it: maintain a complete inventory, and provide "**an SBOM of the runtime production environment** upon request".
- A cloud compliance framework requires that "authoritative sources are used to **automatically generate real-time inventories** of all information resources when needed" -- the strongest regulatory support I've found for the thesis, and it's sitting in a public git repository.
- The **cATO memo** authorises individual *systems*, and as far as I can see the authorisation it grants stops at the system boundary. It requires that "**all** security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism" for assessors. **But the 2024 evaluation criteria weakened "all" to "which"** and accept "screen shots of control gate output as displayed in a dashboard" as evidence. The memo itself also licenses the manual route -- "Manual controls will have different timelines associated" -- so I don't think it can be presented as the current standard.
- One composition tool publishes its latest release as a rolling `latest` tag with no semantic version since 2024 -- **unpinnable, therefore unusable air-gapped.** Its main alternative is a release candidate.
- The tool that issues signed verdicts over attestation sets is **actively maintained** on 44 stars. Is that a bus factor you can live with?

## Blocked -- say it is not knowable

I couldn't get at any of these from open sources, and I don't expect they're there to be got. A cleared conversation looks like the only route:

- **What a real cross-domain guard accepts** -- six of seven necessary parameters. This blocks the transfer-format design outright.
- Controlled requirement sets, baseline lists and assessment methodologies.
- How software actually enters classified cloud regions.
- Whether frontier model APIs exist in classified regions, for a given region and model.
- Alliance-level information exchange gateway specifications.

## Weak negatives -- do not assert these

Treat as leads. Re-check if search access improves:

- "No published standard, vendor document or paper reconciles transform-based inspection with artefact signing." *Load-bearing, and the one I'm least able to defend.*
- "No standard exists for attesting AI-generated code."
- "No regime imposes requirements on AI-generated code in assured software."
- "No policy addresses handling assurance evidence across classification boundaries."

!!! warning "One weak negative is wrong -- do not repeat it"
    **"No tooling exists for runtime or deployed SBOMs" is wrong.** A Kubernetes operator for the *Deployed* SBOM type exists at a few hundred stars. Runtime SBOM tooling looks **thin** to me, though that's an impression I haven't put a number on -- so size the gap and let the size be the claim. The runtime SBOM is now the surviving US federal obligation, which makes the size of that gap worth knowing.

    Same trap on the other side. Open source carries several one-way transfer implementations (`hairgap`, `eurydice` and ANSSI's `lidi`), so treat any sweeping claim about what open code doesn't contain with suspicion -- mine included. Where this site says "zero projects address cross-domain", that's scoped to the 2,430-project catalogue surveyed, and it needs stating with that scope attached.

## Unverified -- these must not leave the room

- A registry's replication may silently drop signatures made with older signing tooling. If that's right, a transport conformance test is mandatory.
- Open-core pricing-tier boundaries throughout -- the pricing pages wouldn't fetch.
- The current regulatory position on AI in assured software. **Needs a dedicated pass before anything citing a regulator is written.**
- One analyst forecast that 40% of companies will downgrade or disable autonomous agents by 2027 due to governance gaps. I couldn't get at the primary analyst material at all, so I'd treat the number as hearsay.

## Before it goes in a deck

What status does the claim carry, and does the room you're standing in clear that status? If you're unsure about the second, it stays in the room.
