# Premise

Captured 2026-10-03. This is the statement of intent the research is serving. Everything else should be traceable back to it.

## The gap

"Software factory" is, today, a thing a large system integrator sells to a large prime. The bundle usually contains SBOM generation, AV and malware scanning, developer tooling, pipeline controls, and a pile of accreditation paperwork. It is bespoke, expensive, and the integration is the product.

There is no open-source project that integrates best-of-breed components into one coherent, *deployable* software factory — one that also produces SBOMs and packages artefacts for transfer through a cross-domain solution into a high-side environment. That absence is the thing worth attacking.

## Who it is for

Any organisation that needs to understand what capabilities exist for building a secure software factory. The focus is cloud, because that is where the interesting primitives are, but the toolchain must be deployable anywhere — on-premises, disconnected, air-gapped, high-side.

Deliberately not scoped to defence only. Defence has the hardest constraints, so solving for it covers regulated finance, CNI, health and automotive as easier cases.

## Design principle: outcomes over inputs

Individual tools are inputs to a process. The SBOM generator, the IDE, the scanner — these are implementation details. What matters is the outcome the factory delivers.

So: **every component slot is defined by the outcome it must produce**, not by the tool that produces it. A signed SBOM. A scanned artefact. A reviewed diff. A provenance attestation that an auditor can check. Each slot then accepts a swappable implementation chosen by environment.

The test case that proves or breaks the architecture: AI-assisted development uses Amazon Bedrock in a hyperscale cloud, and something like LiteLLM in front of locally-hosted models in a high-side enclave. Same slot. Different implementation. **Not a separate special build.** If the high side needs its own build, the abstraction has failed.

This also dictates research order. Find the outcomes first — the things that genuinely move the needle and that customers do not have today. Outcomes define the components; components define which swappable modules are needed. Doing it the other way round produces a tool inventory, which is not an architecture.

## Where the difficulty actually is

Assembling the tools is the easy part. The value is the opinionated glue:

- the attestation and provenance chain
- the policy gates
- an artefact and manifest format that survives a diode or CDS crossing intact

That third one is the least solved. A guard that transforms content to sanitise it breaks every digest it touches, and a one-way diode means the high side cannot call back to a transparency log, an OCSP responder, or an OIDC endpoint to verify anything. The bundle has to carry its own proof.

## The non-technical half

For defence customers, "open source" is a procurement and accreditation story as much as a technical one. A factory nobody can get through an accreditation process is a demo. This needs to be designed in, not bolted on.

## Research questions, in order

1. What outcomes do customers actually want? (`research/01-outcomes.md`)
2. Who has already tried this, and what is genuinely missing? (`research/02-prior-art.md`)
3. What does the integrity layer look like at format level? (`research/03-supply-chain-integrity.md`)
4. What survives a cross-domain crossing? (`research/04-airgap-cds-transfer.md`)
5. Can the AI slot really be swappable? (`research/05-ai-layer.md`)
6. How does it deploy, and how are slots selected? (`research/06-deployment-composition.md`)

Then: how the layers interact and hand off to each other, and deployment strategy — probably Kubernetes-only with defined seams out to things that cannot live in a cluster.
