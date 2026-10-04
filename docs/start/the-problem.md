# The Problem

I'm using "software factory" to mean something that turns source code into a deployable artefact **together with machine-verifiable evidence about how it was made**.

A dozen good open-source implementations already compile code and build containers. The evidence is the harder part, and these properties of it aren't routine anywhere I've looked:

- it's **current**, describing the system as it stands today
- it's **bound** to the artefact it describes, so you can't accidentally pair a signature with the wrong thing
- something actually **reads** it, often enough that a defect surfaces long before an auditor asks

## Who wants this, and why

Regulated organisations, mostly. I looked at twelve regimes (US federal, UK MOD, EU CRA, DORA for financial services, FDA for medical devices, automotive, aviation, rail, industrial), and they reduce to the same machine-readable artefacts:

| | Artefact | Appears as |
|---|---|---|
| **A** | A current component inventory | SBOM, inventory of system components, automated asset inventory, real-time inventory, RXSWIN auditable register, DO-178C Software Configuration Index |
| **B** | Build-and-release provenance | Attestation of practices, integrity validation data, SBOM author signature |
| **C** | A vulnerability-and-remediation ledger | Scan artefacts, security test findings, patch SLA attainment |

Plus the parts that don't automate: a risk narrative, and an accountable human signature.

Generating these artefacts authoritatively, currently, and with transitive completeness is the product. Off-the-shelf tooling already serialises them well enough once something trustworthy has filled them in.

## The pattern in the failures

The same mechanism runs through all four examples below: evidence produced as a side effect of something else, stored somewhere nothing reads it, never checked against the thing it describes.

Things that **gate a build** tend to get maintained, because they break loudly when they drift. Evidence read only by a human at assessment time has no such alarm.

=== "The boundary case"

    Iron Bank's cross-domain export script verifies a container image's cosign signature on the low side, then ships a bare gzipped OCI layout -- **discarding the SBOM, scan results and attestations the same pipeline had just produced**. Those went to a different bucket, by a different code path, for a web front end to display.

=== "The compliance case"

    Big Bang ships an OSCAL component definition (the machine-readable file that makes "inherit controls from the platform" work, and therefore underpins continuous authorisation).

    Its metadata declares `last-modified: 2022-06-06`. The file has **six commits in its entire history**, and the last substantive edit was April 2023. Later commits are a URL fix and a global find-and-replace for a departmental renaming, which make it *look* maintained in the commit log.

    It also fails schema validation with ten duplicated UUIDs. **The OSCAL component-definition model has no referential-integrity constraint**, and the standard validator short-circuits to `true`.

=== "The gate case"

    The same project's commit history, in order:

    - **Aug 2022** -- *"Update OSCAL schema to get pipeline validation to pass."*
    - **Feb 2024** -- live-cluster OSCAL validation built.
    - **Aug 2024** -- the gate disabled. Reason given: "known issues".
    - **Sep 2025** -- the capability deleted.

=== "The policy case"

    The DoD's cATO memo required, in February 2022, that *"all security controls will need to be fed into a system level dashboard view, providing a real time and robust mechanism for AOs to view the environment."*

    By the 2024 evaluation criteria, "all" had become **"which"**: *"Demonstrate which security controls are fed into a system-level dashboard view."* And the criteria go on to accept, as satisfactory evidence of a control gate working, *"screen shots of control gate output as displayed in a dashboard."*

    RAND, in 2025: *"limited movement toward implementation of continuous authority to operate."*

    Policy demands continuous evidence, names the pipeline as its source, and then specifies no machine-verifiable form. The memo itself licenses the manual route: *"Manual controls will have different timelines associated."*

## Why nothing fails when it rots

Evidence rots because nothing reads it. Give it a reader and the freshness problem partly solves itself: stale input produces visibly worse output.

The new reader is an AI agent working inside the factory, and it wants more or less exactly this data. An agent fixing a vulnerability needs the SBOM and reachability analysis to judge whether the finding is real at all. One proposing a dependency bump needs the provenance of whatever it's bumping to.

Of **36,870** real-world dependency upgrade recommendations analysed from registry telemetry, **27.76% referenced versions that do not exist**. "Which versions actually exist for this component" is a graph question, and a document attached alongside the artefact leaves it unanswered.

## Somebody has already done this

A DoD practitioner, quoted anonymously in a DoD CIO publication, describes something very close to this as a success:

!!! quote "From *The State of DevSecOps*, §6.6"
    "The RMF process was going to be the bottleneck. We looked at the NIST 853 controls and identified **100 controls that were required at the application layer. We baked those into our pipeline for automated control and testing.** Then we **continuously monitor** and make sure the controls stay up to date."

DoD published that while its own flagship platform ships compliance evidence that hasn't been reviewed since 2023. I can't find anything in the system that turns an isolated success into the norm.

## How far beyond defence this goes

The general case is any organisation that has to answer "what is running, where did it come from, and what is wrong with it" on demand, whenever a regulator, a customer or an incident asks. On the twelve regimes I looked at, that's most of them.

Air-gapped and cross-domain work gets a lot of space here because a boundary that strips evidence makes the failure visible.

---

**Next:** [Scope -- Three Layers, One Boundary](scope.md) -- the boundary that keeps the whole idea from collapsing, and the one layer that is explicitly out of bounds.
