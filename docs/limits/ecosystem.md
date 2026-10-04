# Ecosystem Health

A factory is an assembly of other people's projects. So the health of those projects is an architectural property, not an operational detail.

## Twelve projects on the critical path with no substitute

| Role | Stars |
|---|---|
| **The only tool that issues a signed verdict over an attestation set** | **44** |
| Air-gapped bundle CLI | 54 |
| Private signing infrastructure scaffolding | 89 |
| Hermetic dependency prefetch | 111 |
| Attestation graph store | 116 |
| Remote attestation verification | 186 |
| **The provenance generator the whole evidence chain hangs off** | **277** |
| Compliance toolkit | 281 |

Two deserve particular attention.

The **44-star project** is actively maintained -- it cut a release two days before this was written. So the risk is **bus factor, not abandonment**. It's simultaneously the most load-bearing and the least known component in the whole stack: nothing else in open source signs a verdict over a set of attestations, which is the mechanism the entire delegated-verdict pattern depends on.

The **277-star project** carries the entire evidence chain. Also healthy, also tiny.

What to do about that is a decision rather than a health finding, so it lives on [Build vs Adopt](../tradeoffs/build-vs-adopt.md).

## The graveyard, with famous residents

Projects that look alive from their star count and aren't:

| What it is | State |
|---|---|
| **The canonical reference implementation of the DORA metrics** | Last commit **January 2024** |
| A container image builder, **15,700 stars** | Dead since mid-2025 |
| A development-environment tool, **15,000 stars** | Alpha-only releases since mid-2025 |
| The official prototype of a well-known secure-factory reference architecture | **Zero releases, ever** -- and it generates no SBOMs despite implying otherwise |
| A layer-aware SBOM generator | Abandoned |
| An infrastructure security scanner | Abandoned |

**Stalled but alive** is a separate and larger category: a provenance verifier untouched for 15 months, its generator for 19, a CNCF-incubating signing tool whose stable release is 18 months old, a popular coding assistant quiet for months despite 49,000 stars.

### Version numbers that overstate maturity

One project is at **v5.130.1 on 62 stars** and is in a foundation's sandbox tier. Another has been at **v0.0.3 since 2024**. A third publishes its latest release under a rolling `latest` tag with **no semantic version since 2024** -- which makes it unpinnable, and therefore unusable in an air-gapped bundle where every reference must be immutable.

!!! warning "Health-check before adopting, every time"
    Stars measure past attention, not current maintenance. A release feed and a last-commit date take thirty seconds and will save you a year.

    The method that made this survey possible: **project release feeds aren't rate-limited**, so hundreds of repositories can be checked without authentication.

## The licence pattern

| Trap | Why it hurts |
|---|---|
| A major secrets manager relicensed to a non-open business-source licence, with **FIPS builds behind the enterprise tier** | FIPS is a procurement gate, so this isn't negotiable |
| A workspace platform puts **prebuilds behind its paid tier** | That is *the one feature* an air-gapped deployment needs |
| A forge's community edition puts **the entire signed-review outcome behind its paid tier** | One of the eight empty slots is empty partly by commercial design |
| A secret scanner under strong copyleft | Fine to run, awkward to redistribute |
| A DoD-adjacent platform core under strong copyleft | Surprising; check before building on it |

!!! danger "In five separate cases the paid tier *is* the slot-critical feature"
    Open-core vendors have converged on gating exactly what a regulated or disconnected deployment needs. That's a business model, not an accident.

    **Assume it, and check** -- rather than discovering it at renewal, with the platform already load-bearing.

A related finding: the open factory most often cited as a reference implementation has its security-scanning slot filled by **commercial products**, with dependency scanning requiring a paid forge tier. **An all-open-source version of it doesn't exist.** Mine its patterns; don't adopt it as a substrate and expect to stay open source.

## The OSCAL retreat

The clearest case of informed abandonment in the whole survey. Several well-resourced, independently motivated organisations built on OSCAL and walked away, and at least one said why. Read the direction rather than the snapshot: **the ecosystem is drifting back towards documents.** The evidence is catalogued under [Build vs Adopt](../tradeoffs/build-vs-adopt.md), since what it changes is a decision about what to build rather than a tool to cross off.

## Where disconnected operation is genuinely first-class

Rare, and worth knowing precisely:

**Only two projects in 2,430 catalogued exist *because of* air-gap.** Three more treat disconnected operation as first-class -- one signing tool with the best offline flag surface of anything surveyed, one OS image system with **the best delta design in open source** (a signed index over static deltas, which is the pattern a transfer bundle should copy), and one scanner that reads a bundle in place without extraction or network.

**Zero address cross-domain.** Which is both the gap and the warning: nobody has done it, and the reasons may include it being genuinely hard.

One encouraging signal: the cloud-native community now has a formally recognised **air-gapped working group**. It's a stub with no content yet, but the problem domain has been acknowledged.
