# Ecosystem Risk

A factory is an assembly of other people's projects, which makes the health of those projects an architectural property.

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

Only two have no substitute I could find. For the rest "substitute" means *write it yourself* or *accept a worse option*, both of which cost engineering time.

The **44-star project** is actively maintained and cutting releases. The risk is **bus factor**: the release history depends on a very small number of hands. I haven't found anything else in open source that signs a verdict over a set of attestations, which is the mechanism the delegated-verdict pattern depends on.

The **277-star project** carries the entire evidence chain, is maintained, and is just as small.

What to do about it is a decision, so it lives on [Build vs Adopt](../tradeoffs/build-vs-adopt.md).

## The graveyard

| What it is | State |
|---|---|
| **The reference implementation of the DORA metrics** | Last commit **January 2024** |
| A container image builder, **15,700 stars** | Dead since mid-2025 |
| A development-environment tool, **15,000 stars** | Alpha-only releases since mid-2025 |
| The official prototype of a well-known secure-factory reference architecture | **Zero releases, ever**, and I couldn't find its advertised SBOM output anywhere in the code |
| A layer-aware SBOM generator | Abandoned |
| An infrastructure security scanner | Abandoned |

**Stalled but alive** is a separate and larger category: a provenance verifier untouched for 15 months, its generator for 19, a CNCF-incubating signing tool whose stable release is 18 months old, a popular coding assistant quiet for months despite 49,000 stars.

### Version numbers that overstate maturity

One project is at **v5.130.1 on 62 stars** and is in a foundation's sandbox tier. Another has been at **v0.0.3 since 2024**. A third publishes its latest release under a rolling `latest` tag with **no semantic version since 2024** -- which makes it unpinnable, and therefore unusable in an air-gapped bundle where every reference must be immutable.

!!! warning "Stars measure past attention, not current maintenance"
    Current maintenance shows up in the release feed and the last-commit date.

## The licence pattern

| Trap | Why it hurts |
|---|---|
| A major secrets manager relicensed to a non-open business-source licence, with **FIPS builds behind the enterprise tier** | FIPS is a procurement gate, so this isn't negotiable |
| A workspace platform puts **prebuilds behind its paid tier** | That is *the one feature* an air-gapped deployment needs |
| A forge's community edition puts **the entire signed-review outcome behind its paid tier** | One of the eight empty slots is empty partly by commercial design |
| A secret scanner under strong copyleft | Fine to run, awkward to redistribute |
| A DoD-adjacent platform core under strong copyleft | Worth checking before you build on it |

!!! danger "In five separate cases the paid tier *is* the slot-critical feature"
    Settle which tier holds the feature you need at evaluation time, not at renewal with the platform already load-bearing.

The open factory most often cited as a reference implementation has its security-scanning slot filled by **commercial products**, with dependency scanning requiring a paid forge tier. I couldn't assemble an all-open-source version of it from what's published. Adopt it as a substrate and you inherit those commercial dependencies.

## The OSCAL retreat

Several well-resourced organisations built on OSCAL and walked away, independently of each other, and at least one said why. The direction of travel: **OSCAL tooling is drifting back towards documents.** The evidence is catalogued under [Build vs Adopt](../tradeoffs/build-vs-adopt.md).

## Where disconnected operation is genuinely first-class

**Only two projects in 2,430 catalogued exist *because of* air-gap.** Three more treat disconnected operation as first-class -- one signing tool with the best offline flag surface of anything surveyed, one OS image system that ships **a signed index over static deltas**, and one scanner that reads a bundle in place without extraction or network.

**Zero of the 2,430 address cross-domain.** That's a count of the catalogue; one-way transfer implementations do exist outside it. What I haven't found anywhere is something that bundles artefacts *and* their evidence for a guard-mediated crossing.

The cloud-native community now has a formally recognised **air-gapped working group**, a stub with no content yet.
