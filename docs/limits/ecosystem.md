# Ecosystem Risk

A factory is an assembly of other people's projects, which makes the health of those projects an architectural property. Every dependency below is a risk you're choosing to carry.

## Twelve projects under 300 stars, nine of them on the critical path

| Role | Stars | If it dies |
|---|---|---|
| **The only tool I found that issues a signed verdict over an attestation set** | **44** | **Nothing I found replaces it** |
| Compliance-evidence generator | 46 | Build it |
| Air-gapped bundle CLI | 54 | Drop to the bundler underneath it |
| VEX document library | 71 | Write it |
| CSAF/VEX library | 72 | Write it |
| Private signing infrastructure scaffolding | 89 | Deploy the components by hand |
| Hermetic dependency prefetch | 111 | A functional package manager, at roughly ten times the cost |
| Attestation graph store | 116 | OCI referrers only, losing the graph queries |
| Admission controller | 182 | A general-purpose policy engine |
| Remote attestation verification | 186 | **Nothing I found replaces it** |
| **The provenance generator the whole evidence chain hangs off** | **277** | One alternative, less mature |
| Compliance toolkit | 281 | Hand-written documents |

Only two of them seem to have no substitute at all. For the rest "substitute" means *write it yourself* or *accept a worse option*, both of which you pay for in engineering time -- and all twelve are small enough that one maintainer leaving is an architectural event.

Two of them worry me more than the rest.

The **44-star project** is actively maintained and cutting releases. The risk it carries is **bus factor**: the release history depends on a very small number of hands. I haven't found anything else in open source that signs a verdict over a set of attestations, which is the mechanism the delegated-verdict pattern depends on -- so on my reading it's both the most load-bearing and the least known thing in the stack. That reading is only as good as my search; one project I missed would change it.

The **277-star project** carries the entire evidence chain. Also healthy, also tiny.

What to do about that is a decision, so it lives on [Build vs Adopt](../tradeoffs/build-vs-adopt.md).

## The graveyard, with famous residents

Projects whose star counts are the only living thing about them:

| What it is | State |
|---|---|
| **The reference implementation of the DORA metrics** | Last commit **January 2024** |
| A container image builder, **15,700 stars** | Dead since mid-2025 |
| A development-environment tool, **15,000 stars** | Alpha-only releases since mid-2025 |
| The official prototype of a well-known secure-factory reference architecture | **Zero releases, ever**, and I couldn't find its advertised SBOM output anywhere in the code |
| A layer-aware SBOM generator | Abandoned |
| An infrastructure security scanner | Abandoned |

**Stalled but alive** is a separate category, and by my count a larger one: a provenance verifier untouched for 15 months, its generator for 19, a CNCF-incubating signing tool whose stable release is 18 months old, a popular coding assistant quiet for months despite 49,000 stars.

### Version numbers that overstate maturity

One project is at **v5.130.1 on 62 stars** and is in a foundation's sandbox tier. Another has been at **v0.0.3 since 2024**. A third publishes its latest release under a rolling `latest` tag with **no semantic version since 2024** -- which makes it unpinnable, and therefore unusable in an air-gapped bundle where every reference must be immutable.

!!! warning "The check I wish I'd run first"
    Stars measure past attention. Current maintenance shows up in the release feed and the last-commit date, which take thirty seconds to read and would have saved me weeks if I'd started there.

## The licence pattern

| Trap | Why it hurts |
|---|---|
| A major secrets manager relicensed to a non-open business-source licence, with **FIPS builds behind the enterprise tier** | FIPS is a procurement gate, so this isn't negotiable |
| A workspace platform puts **prebuilds behind its paid tier** | That is *the one feature* an air-gapped deployment needs |
| A forge's community edition puts **the entire signed-review outcome behind its paid tier** | One of the eight empty slots is empty partly by commercial design |
| A secret scanner under strong copyleft | Fine to run, awkward to redistribute |
| A DoD-adjacent platform core under strong copyleft | Surprising; worth checking before you build on it |

!!! danger "In five separate cases the paid tier *is* the slot-critical feature"
    The open-core vendors in this list have converged on gating the thing a regulated or disconnected deployment needs. Whether that's deliberate targeting or just where the money happens to sit, I can't tell from outside; the bill you get is the same either way.

    **So: which tier holds the feature you actually need?** Worth settling at evaluation time, because renewal is an expensive moment to find out, with the platform already load-bearing.

The open factory I've seen cited most often as a reference implementation has its security-scanning slot filled by **commercial products**, with dependency scanning requiring a paid forge tier. I couldn't assemble an all-open-source version of it from what's published, though I'd be glad to be shown one. Its patterns are worth mining. Adopt it as a substrate and you inherit those commercial dependencies -- can your deployment carry them?

## The OSCAL retreat

The clearest case of informed abandonment I found anywhere in this stack. Several well-resourced organisations built on OSCAL and walked away, independently of each other so far as I can see, and at least one said why. The direction of travel, as far as I can read it from outside: **the ecosystem is drifting back towards documents.** The evidence is catalogued under [Build vs Adopt](../tradeoffs/build-vs-adopt.md), since what it changes is a decision about what to build.

## Where disconnected operation is genuinely first-class

Rare enough that the list is short:

**Only two projects in 2,430 catalogued exist *because of* air-gap.** Three more treat disconnected operation as first-class -- one signing tool with the best offline flag surface of anything surveyed, one OS image system with **the best delta design I've seen** (a signed index over static deltas, which is the pattern I'd copy for a transfer bundle), and one scanner that reads a bundle in place without extraction or network.

**Zero of the 2,430 address cross-domain.** That is a count of the catalogue, and open source is wider than the catalogue: outside it, one-way transfer implementations do exist, and a universal negative over open code is never a safe thing to claim. What I haven't found anywhere is something that bundles artefacts *and* their evidence for a guard-mediated crossing -- and a gap that old may simply mean the problem is hard.

One encouraging signal: the cloud-native community now has a formally recognised **air-gapped working group**. It's a stub with no content yet, so I can't tell whether it goes anywhere -- but the problem domain has been acknowledged somewhere official.
