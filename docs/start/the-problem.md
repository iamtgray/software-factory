# The Problem

A software factory turns source code into a deployable artefact **together with machine-verifiable evidence about how it was made**.

The artefact was never hard. Compiling code and building containers is a solved problem with a dozen good open-source implementations. The evidence is the interesting part -- specifically three properties of it that nobody has made routine:

- it's **current**, rather than describing a state the system left behind months ago
- it's **bound** to the artefact it describes, so you can't accidentally pair a signature with the wrong thing
- something actually **reads** it, rather than it sitting in a bucket until an auditor asks

## Who wants this, and why

Regulated organisations, mostly, and the demand is more consolidated than it looks. A survey of twelve regulatory regimes (US federal, UK MOD, EU CRA, DORA for financial services, FDA for medical devices, automotive, aviation, rail, industrial) found they reduce to **three machine-readable artefacts**:

| | Artefact | Appears as |
|---|---|---|
| **A** | A current component inventory | SBOM, inventory of system components, automated asset inventory, real-time inventory, RXSWIN auditable register, DO-178C Software Configuration Index |
| **B** | Build-and-release provenance | Attestation of practices, integrity validation data, SBOM author signature |
| **C** | A vulnerability-and-remediation ledger | Scan artefacts, security test findings, patch SLA attainment |

Plus two things that don't automate: a risk narrative, and an accountable human signature. No regime pretends otherwise.

One line: *five regulations asking five things are asking what is in it, where it came from, and what is wrong with it -- plus a risk story and a signature.*

!!! tip "The useful consequence"
    Serialising these artefacts is cheap and already solved. **Generating them authoritatively, currently, and with transitive completeness is the product.** That's a much narrower claim than "we build software factories", and it's defensible.

## The pattern behind every documented failure

Across four independently researched examples, the same mechanism appears. Evidence is produced as a side effect of some other process, stored somewhere nothing reads it, and never verified against the thing it describes.

Anything that **gates a build** gets maintained, because it breaks loudly when it drifts. Anything read only by a human at assessment time **rots silently**, because nothing fails when it does.

=== "The boundary case"

    Iron Bank's cross-domain export script verifies a container image's cosign signature on the low side, then ships a bare gzipped OCI layout -- **discarding the SBOM, scan results and attestations the same pipeline had just produced**. Those went to a different bucket, by a different code path, for a web front end to display.

    The artefact and its provenance diverge one step before the boundary.

=== "The compliance case"

    Big Bang ships an OSCAL component definition (the machine-readable file that makes "inherit controls from the platform" work, and therefore the file underpinning continuous authorisation).

    Its metadata declares `last-modified: 2022-06-06`. The file has **six commits in its entire history**, and the last substantive edit was April 2023. Later commits are a URL fix and a global find-and-replace for a departmental renaming, which make it *look* maintained in the commit log.

    It also fails schema validation with ten duplicated UUIDs -- unnoticed because **the OSCAL component-definition model has no referential-integrity constraint**, and the standard validator short-circuits to `true`. The format can't tell you it's broken.

=== "The gate case"

    The same project's commit history, in order:

    - **Aug 2022** -- *"Update OSCAL schema to get pipeline validation to pass."* The validator complained; the document was changed until it stopped.
    - **Feb 2024** -- live-cluster OSCAL validation built.
    - **Aug 2024** -- the gate disabled. Reason given: "known issues".
    - **Sep 2025** -- the capability deleted.

    Someone built the machine that checks the evidence, it returned inconvenient results, and the machine was removed.

=== "The policy case"

    The DoD's cATO memo has required, since February 2022, that *"all security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism for AOs to view the environment."*

    RAND, in 2025: *"limited movement toward implementation of continuous authority to operate."*

    The policy demands continuous evidence. The implementations produce stale documents.

## The sharper diagnosis

Evidence rots because nothing fails when it does. That diagnosis is true but incomplete.

!!! quote "Evidence rots because nothing *reads* it."
    Give it a reader with an appetite and the freshness problem partly solves itself, because stale input produces visibly worse output.

This matters more now than it did three years ago, because there's a new and hungry reader: an AI agent working inside the factory wants exactly this data. An agent fixing a vulnerability needs the SBOM and reachability analysis to judge whether the finding is real. An agent proposing a dependency bump needs the provenance of the thing it's bumping to.

Of **36,870** real-world dependency upgrade recommendations analysed from registry telemetry, **27.76% referenced versions that do not exist**. That's what ungrounded generation looks like at scale, and it's an argument for the evidence graph being queryable rather than merely attached -- "which versions actually exist for this component" is a graph question.

## Why this is not just a defence problem

The air-gapped and cross-domain case is the **sharpest demonstration** of the thesis, because a boundary that strips evidence makes the failure visible and unavoidable.

The general case is any organisation that has to answer "what is running, where did it come from, and what is wrong with it" on demand rather than on an annual cycle. Which, after a survey of twelve regimes, is most of them.

---

**Next:** [What We Got Wrong](corrections.md) -- before you repeat any of the above, find out which parts of it didn't survive verification.
