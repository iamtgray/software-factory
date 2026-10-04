# Build vs Adopt

The default answer is adopt. The harder question is **whether it will still exist in three years, and whether the feature you need sits behind a licence.**

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

One of those eight looked as though it could move to the adopt list, and the story of why it can't is instructive. A tool exists that turns a maintainer's single structured comment into a Sigstore-signed in-toto VEX attestation, authorised against a code-owners file. The design is exactly right, and it contains no AI -- correctly, since a model scores under 70% on that decision.

But it is at **10 stars, v0.0.1, one maintainer, with a README that calls it experimental.** An earlier version of this page said that removed the signed-VEX item from the build list. It doesn't: adopting it means owning it. **Take the design as a head start; budget for the implementation.**

That is the general shape of the adopt decision in this field, and it is why the next section matters more than the slot count.

## What adopting costs you later

Health is the part of the adopt decision nobody prices in. Twelve projects under 300 stars sit on the critical path with no substitute, several well-known tools are dead despite their star counts, and in five separate cases a vendor's paid tier *is* the feature a disconnected deployment needs. The survey behind those findings is on [Ecosystem Health](../limits/ecosystem.md).

Two things fall out of it for the decision. Health-check before you adopt, every time -- a release feed and a last-commit date take thirty seconds and will save you a year. And where the gated feature is the slot-critical one, the answer is the open fork or the empty slot rather than the paid tier; one of the eight slots above is empty partly by commercial design.

!!! success "The response, and a possible contribution"
    Contribute upstream now. It's cheaper than forking later, and far cheaper than discovering a maintainer has moved on.

    It also suggests something a funded programme could give the ecosystem that isn't code: **becoming an accountable, funded consumer of three tiny projects that everything else quietly depends on.** Arguably worth more than another platform.

## Consolidations that reduce the surface

The slot count is 24. The component count should be far lower, and the reasons are operational rather than feature-driven:

**One scanner covering SBOM, vulnerabilities and misconfiguration** means **one offline vulnerability-database import pipeline instead of four.** In a disconnected environment that is the decisive argument, and it has nothing to do with the feature comparison.

**One build system plus its provenance tool** covers build execution, signing and test evidence under a single key-separation story.

**A declarative minimal base-image builder** covers base images, their SBOMs and most of the vulnerability surface -- because it *removes* findings rather than suppressing them, which is what keeps the gate switched on.

**Encrypted-file secrets rather than a secrets server** covers the slot by **removing a component from the enclave.** Whenever an option removes a server, take it.

!!! example "On adopting an assembled stack"
    One integrated open factory collapses five slots at once. The reason to care isn't the product. It's that the components arrive **integrated and tested together** rather than adopted blind.

    **Steal the assembly, not the product.**

## The OSCAL lesson

A natural conclusion from everything on this site is "we should generate compliance evidence continuously". The track record says that's naive, and it says so from experience:

- one project **deleted** its OSCAL and replaced the tool, stating that **"OSCAL proved too complex... automated tests alone were insufficient"**
- a government automation repository is **404**
- two major vendors migrated to different formats entirely; a third **archived both of its attempts**
- **the next major version of the standard has no active work**
- one project's live-cluster validation was **built, then disabled, then deleted** over eighteen months
- and across four key defence documents, OSCAL has **zero genuine references** -- it is not even demanded

That's multiple well-resourced, independently motivated organisations building this and abandoning it. Concluding "we'll simply do it better" is exactly the arrogance that killed the 1978 attempt.

!!! success "Separate the outcome from the serialisation"
    The **outcome** -- continuous, machine-verifiable control status -- is demanded verbatim by policy.

    The **serialisation** is contested, and its most obvious candidate is the one its own adopters have walked away from.

    So build to the outcome and keep the format swappable -- which is this project's founding principle applied to itself. **Never pitch "we generate OSCAL". Pitch "we generate continuous control evidence, currently serialised as X".**

## The one thing standards give you for free

A standards body has explicitly **declined to standardise integrated secure-development platforms, on the grounds that they are too immature.**

That's the cleanest available answer to "why hasn't someone already done this", and it came from the people whose job is to say when something is ready.
