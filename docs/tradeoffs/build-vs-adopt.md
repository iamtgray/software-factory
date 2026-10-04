# Build vs Adopt

The default answer is adopt. What decides each case, as far as I can tell, is **whether the thing will still exist in three years, and whether the feature you need sits behind a licence.**

## Where the field seems to agree

!!! quote "Do not build your own platform"
    Said by a consultancy that bills for building things, and by a vendor that sells one. When those two agree (and they disagree with each other about almost everything else) I take it as about as settled as anything gets here.

The publicly citable government position argues cost, and it's useful on exactly that ground. The DoD reference design (Distribution Statement A): *"Operating a custom DevSecOps platform is an expensive endeavor because software factories require the same level of continuous investment as a software application."*

And there's a cautionary data point behind it. One of the most-cited software factories spent four years building its own platform and delivered nothing from that effort.

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

    That reads to me like one piece of work covering all four. The part I'm least sure of is how much per-predicate fiddliness hides behind "mint the predicates".

One of those slots came close to moving to the adopt list. A tool exists that turns a maintainer's single structured comment into a Sigstore-signed in-toto VEX attestation, authorised against a code-owners file. The design looks right to me, and it contains no AI -- correctly, I'd say, since a model scores under 70% on that decision.

But it sits at **10 stars, v0.0.1, one maintainer, with a README that calls it experimental.** Adopting that tool means owning it, so signed VEX stays on the build list. The design is a head start you get for nothing. Can your programme fund the implementation behind it?

The adopt decision here usually ends up looking like that one, and the bill for it lands later.

## What adopting costs you later

Health is the part of the adopt decision I've yet to see anyone price in. Twelve projects under 300 stars carry the stack, nine of them on the critical path and two with no substitute I could find. Several well-known tools are dead on every check I ran, whatever their star counts suggest. And in five separate cases a vendor's paid tier *is* the feature a disconnected deployment needs. The survey behind those findings is on [Ecosystem Health](../limits/ecosystem.md).

So: health-check before you adopt, every time. A release feed and a last-commit date take thirty seconds and might save you a year. And where the gated feature is the slot-critical one, plan on the open fork, or on living with the empty slot -- one of the slots above looks empty partly by commercial design.

!!! success "The response, and a possible contribution"
    Contribute upstream now. It's cheaper than forking later, and cheaper again than discovering a maintainer has moved on.

    It also suggests something a funded programme could give back beyond writing code: **becoming an accountable, funded consumer of three tiny projects that everything else quietly depends on.** I think that's worth more than another platform, though I'd understand a programme manager disagreeing.

## Consolidations that reduce the surface

The slot count is 24. The component count should be far lower, and my reasons are all operational:

**One scanner covering SBOM, vulnerabilities and misconfiguration** means **one offline vulnerability-database import pipeline, down from four.** In a disconnected environment I'd expect that single pipeline to decide the choice of scanner on its own.

**One build system plus its provenance tool** covers build execution, signing and test evidence under a single key-separation story.

**A declarative minimal base-image builder** covers base images, their SBOMs and most of the vulnerability surface. It *removes* findings: the vulnerable package leaves the image altogether, and a gate with nothing left to argue about stays switched on.

**Encrypted-file secrets** cover the slot with files that live in the repository, so the enclave runs **one server fewer.** I'd take any option that removes a server from the enclave.

!!! example "On adopting an assembled stack"
    One integrated open factory collapses five slots at once. The value, as I read it, is that the components arrive **integrated and tested together**, with the integration work already done and open to inspection.

    **Steal the assembly. Leave the product where it is.**

## The OSCAL lesson

Everything on this site points towards generating compliance evidence continuously. The format built for that job has a graveyard behind it:

- one project **deleted** its OSCAL and replaced the tool, stating that **"OSCAL proved too complex... automated tests alone were insufficient"**
- a government automation repository is **404**
- two major vendors migrated to different formats entirely; a third **archived both of its attempts**
- the next major version of the standard has no active work that I can find
- one project's live-cluster validation was **built (Feb 2024), disabled (Aug 2024, "known issues"), then deleted (Sep 2025)**
- and across **all eight** cached defence primary documents, OSCAL has **zero occurrences** (no primary document I hold asks for it)

Each of those is a well-resourced, independently motivated organisation that built this and walked away. I can't prove each of them was right to. But "we'll simply do it better" reads to me as exactly the arrogance that killed the 1978 attempt.

!!! success "Separate the outcome from the serialisation"
    The **outcome** (continuous control status an authorising official can act on, generated by the pipeline) is what policy demands. Policy names the pipeline as the source and then specifies **no machine-verifiable form** for the evidence. Screen shots of a dashboard are accepted as proof that a control gate works.

    The **serialisation** is contested, and its most obvious candidate is the one its own adopters have walked away from.

    So build to the outcome and keep the format swappable, which is this project's founding principle applied to itself. **Pitch "we generate continuous control evidence, currently serialised as X"** -- the format name sits in the subordinate clause, where it can be swapped out on the day its adopters finish leaving.

## What the standards bodies give you for free

A standards body has explicitly **declined to standardise integrated secure-development platforms, on the grounds that they are too immature.**

For anyone asking "why hasn't someone already done this", that's about as good a source as you'll find: the people whose job is to say when something is ready don't think it's ready yet. Which leaves the one question I can't answer from here: of the slots that came back empty, which does your programme actually need filled, and which can it live without?
