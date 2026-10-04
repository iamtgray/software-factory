# Build vs Adopt

The default answer is adopt. The interesting question is the second one: **will it still exist in three years, and is the feature you need behind a licence?**

## The strongest consensus in the field

!!! quote "Do not build your own platform"
    Said by a consultancy, by a platform vendor, **and by the DoD's own implementation guide**, which puts it as "should be avoided if possible".

    When a consultancy that bills for building things, a vendor that sells one, and a government guide all agree, that's as close to settled as this field gets.

And there's a cautionary data point behind it. One of the most-cited software factories spent four years building its own platform and delivered nothing from that effort.

## The eight genuinely empty slots

From a sweep of 24 outcome-defined slots against open source, with 250+ repositories health-checked:

| Empty slot | State |
|---|---|
| **Cross-domain bundling and transfer** | Two projects in 2,430 exist *because of* air-gap; **zero** address cross-domain |
| **Signed review-policy evidence** | Everything configures or reports; **nothing signs "policy X was met for commit Y"** |
| Signed test-result evidence | A predicate is registered; nothing emits it |
| Signed VEX attestation | No registered predicate -- and the specification has been **frozen since 2023** |
| AI-authorship attestation | Nothing across 51 surveyed AI-agent projects |
| Offline signed agent-tool catalogue | The extension-registry problem again |
| Signed model-weight distribution | The obvious tool has had no release in a year |
| Compliance-evidence generation | The leading project has **46 stars** and no release since February |

!!! tip "Four of these are one job"
    The predicate-shaped gaps -- VEX, test results, AI authorship, review policy -- collapse into: **mint the predicates, then teach the provenance tool and the policy gate to emit and check them.**

    Far smaller than the slot count suggests.

And one that moved from the build list to the adopt list on inspection: **signed VEX already exists.** A tool turns a maintainer's single structured comment into a Sigstore-signed in-toto attestation, authorised against a code-owners file. It's coupled to one forge by default but through pluggable interfaces, so porting it is bounded work against a designed seam. **Port, don't build** -- and note it contains no AI, which is correct, because a model scores under 70% on that decision.

## The sustainability problem

This is the part that should give you pause. **Twelve projects with fewer than 300 stars sit on the critical path with no substitute:**

| Project role | Stars |
|---|---|
| **The only tool that issues a signed verdict over an attestation set** | **44** |
| Air-gapped bundle CLI | 54 |
| Private signing infrastructure scaffolding | 89 |
| Hermetic dependency prefetch | 111 |
| Attestation graph store | 116 |
| Remote attestation verification | 186 |
| **The provenance generator the whole evidence chain hangs off** | **277** |
| Compliance toolkit | 281 |

Two of those deserve emphasis. The 44-star project is **actively maintained** (a release two days before this was written), so the risk is **bus factor, not abandonment.** It's simultaneously the most load-bearing and least-known component in the stack. And the 277-star one carries the entire evidence chain.

!!! success "The honest response, and a possible contribution"
    Contribute upstream now. It's cheaper than forking later.

    And it suggests something a funded programme could offer that isn't code: **becoming an accountable, funded consumer of three tiny projects that everything else quietly depends on.** Arguably worth more than another platform.

## The graveyard

Projects that look alive and aren't:

- **the canonical reference implementation of the DORA metrics** -- last commit January 2024
- **a container builder with 15,700 stars** -- dead since mid-2025
- **a development-environment tool with 15,000 stars** -- alpha-only releases since mid-2025
- the official prototype of a well-known reference architecture -- **zero releases, ever**

And version numbers that overstate maturity: one project is at v5.130.1 on 62 stars; another has been at v0.0.3 since 2024.

!!! warning "Health-check before adopting, every time"
    Stars measure past attention, not current maintenance. A release feed and a last-commit date take thirty seconds to check and will save you a year.

## The licence pattern, which is not a coincidence

| Trap | Consequence |
|---|---|
| A major secrets manager relicensed to a non-open business-source licence, with **FIPS builds behind the enterprise tier** | Use the open fork |
| A workspace platform puts **prebuilds behind its paid tier** | That is *the one feature* an air-gapped deployment needs |
| A forge's community edition puts **the entire signed-review outcome behind its paid tier** | The empty slot above is empty partly by commercial design |
| A secret scanner under a strong copyleft licence | Fine to run, awkward to redistribute |
| A DoD-adjacent platform core under a strong copyleft licence | Surprising, and worth checking before you build on it |

!!! danger "In five separate cases the paid tier *is* the slot-critical feature"
    Open-core vendors have converged on gating exactly what a regulated or disconnected deployment needs. Assume this and check, rather than discovering it at renewal.

## Consolidations that reduce the surface

The slot count is 24. The component count should be far lower, and the reasons are operational rather than feature-driven:

**One scanner covering SBOM, vulnerabilities and misconfiguration** means **one offline vulnerability-database import pipeline instead of four.** In a disconnected environment that is the decisive argument, and it has nothing to do with the feature comparison.

**One build system plus its provenance tool** covers build execution, signing and test evidence under a single key-separation story.

**A declarative minimal base-image builder** covers base images, their SBOMs and most of the vulnerability surface -- because it *removes* findings rather than suppressing them, which is what keeps the gate switched on.

**Encrypted-file secrets rather than a secrets server** covers the slot by **removing a component from the enclave.** Whenever an option removes a server, take it.

!!! tip "On adopting an assembled stack"
    One integrated open factory collapses five slots at once. The reason to care isn't the product. It's that the components arrive **integrated and tested together** rather than adopted blind.

    **Steal the assembly, not the product.**

## The OSCAL lesson

A natural conclusion from everything on this site is "we should generate compliance evidence continuously". The track record says that's naive, and it says so from experience:

- one project **deleted** its OSCAL and replaced the tool, stating that **"OSCAL proved too complex... automated tests alone were insufficient"**
- a government automation repository is **404**
- two major vendors migrated to different formats entirely; a third **archived both of its attempts**
- **the next major version of the standard has no active work**
- and across four key defence documents, OSCAL has **zero genuine references** -- it is not even demanded

That's multiple well-resourced, independently motivated organisations building this and abandoning it. Concluding "we'll simply do it better" is exactly the arrogance that killed the 1978 attempt.

!!! success "Separate the outcome from the serialisation"
    The **outcome** -- continuous, machine-verifiable control status -- is demanded verbatim by policy.

    The **serialisation** is contested, and the obvious candidate is a graveyard.

    So build to the outcome and keep the format swappable -- which is this project's founding principle applied to itself. **Never pitch "we generate OSCAL". Pitch "we generate continuous control evidence, currently serialised as X".**

## The one thing standards give you for free

A standards body has explicitly **declined to standardise integrated secure-development platforms, on the grounds that they are too immature.**

That's the cleanest available answer to "why hasn't someone already done this", and it came from the people whose job is to say when something is ready.
