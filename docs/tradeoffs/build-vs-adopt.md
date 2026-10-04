# Build vs Adopt

The default answer is adopt. Two things decide each case: whether the thing will **still exist in three years**, and whether the feature you need sits **behind a licence**.

## Where the field agrees

A consultancy that bills for building things and a vendor that sells one both say **don't build your own platform.**

The DoD reference design (Distribution Statement A) argues cost: *"Operating a custom DevSecOps platform is an expensive endeavor because software factories require the same level of continuous investment as a software application."*

One of the most-cited software factories spent four years building its own platform and delivered nothing.

## The slots that came back empty

From a sweep of 24 outcome-defined slots against open source, with 250+ repositories health-checked, these are the ones where I found nothing I could use:

| Empty slot | State |
|---|---|
| **Cross-domain bundling and transfer** | Two projects in 2,430 exist *because of* air-gap; none that I found address cross-domain |
| **Signed review-policy evidence** | The tools in this slot configure and report; none of them signs "policy X was met for commit Y" |
| Signed test-result evidence | A predicate is registered; I've not found anything that emits it |
| Signed VEX attestation | No registered predicate, and the specification has been **frozen since 2023** |
| AI-authorship attestation | Nothing in 51 surveyed AI-agent projects |
| Offline signed agent-tool catalogue | The extension-registry problem again |
| Signed model-weight distribution | The obvious tool has had no release in a year |
| Compliance-evidence generation | The leading candidate has **46 stars** and no release since February |

!!! tip "The predicate gaps may be one job"
    The predicate-shaped gaps (VEX, test results, AI authorship, review policy) collapse into the same work: **mint the predicates, then teach the provenance tool and the policy gate to emit and check them.**

    How much per-predicate fiddliness hides behind "mint the predicates" is unmeasured.

One of those slots came close to moving to the adopt list. A tool exists that turns a maintainer's single structured comment into a Sigstore-signed in-toto VEX attestation, authorised against a code-owners file. It contains no AI, and the best measured model performance on selecting a VEX justification is under 70%.

But it sits at **10 stars, v0.0.1, one maintainer, with a README that calls it experimental** -- adopting it means owning it, so signed VEX stays on the build list.

## What adopting costs you later

Twelve projects under 300 stars carry the stack, nine of them on the critical path and two with no substitute I could find. Several well-known tools are dead on every check I ran. And in five separate cases a vendor's paid tier *is* the feature a disconnected deployment needs. The survey behind those findings is on [Ecosystem Health](../limits/ecosystem.md).

So: health-check before you adopt, every time. A release feed and a last-commit date take thirty seconds. Where the gated feature is the slot-critical one, plan on the open fork, or on living with the empty slot.

Contributing upstream costs less than forking later, and less again than finding out a maintainer has moved on. And a funded programme can be the accountable, funded consumer of three tiny projects that everything else depends on.

## Consolidations that reduce the surface

The slot count is 24. The component count should be far lower, for operational reasons:

**One scanner covering SBOM, vulnerabilities and misconfiguration** means **one offline vulnerability-database import pipeline, down from four.** In a disconnected environment that single pipeline decides the choice of scanner on its own.

**One build system plus its provenance tool** covers build execution, signing and test evidence under a single key-separation story.

**A declarative minimal base-image builder** takes base images, their SBOMs and most of the vulnerability surface. It *removes* findings: the vulnerable package leaves the image altogether.

**Encrypted-file secrets** fill the slot with files that live in the repository, so the enclave runs **one server fewer.**

!!! example "On adopting an assembled stack"
    One integrated open factory collapses five slots at once. The components arrive **tested together**, with the integration work done and open to inspection.

## The OSCAL lesson

The format built for continuous compliance evidence has a graveyard behind it:

- one project **deleted** its OSCAL and replaced the tool, stating that **"OSCAL proved too complex... automated tests alone were insufficient"**
- a government automation repository is **404**
- two major vendors migrated to different formats entirely; a third **archived both of its attempts**
- the next major version of the standard has no active work that I can find
- one project's live-cluster validation was **built (Feb 2024), disabled (Aug 2024, "known issues"), then deleted (Sep 2025)**
- and across **all eight** cached defence primary documents, OSCAL has **zero occurrences** (no primary document I hold asks for it)

Each of those is a well-resourced, independently motivated organisation that built this and walked away.

!!! success "Separate the outcome from the serialisation"
    The **outcome** (continuous control status an authorising official can act on, generated by the pipeline) is what policy demands. Policy names the pipeline as the source and then specifies **no machine-verifiable form** for the evidence. Screenshots of a dashboard are accepted as proof that a control gate works.

    So build to the outcome and keep the format swappable. Pitch **"we generate continuous control evidence, currently serialised as X"**.

## What the standards bodies say

A standards body has declined to standardise integrated secure-development platforms, on the grounds that they are too immature.

So: which of the empty slots does your programme need filled, and which can it live without?
