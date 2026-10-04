# Premise

Captured 2026-10-03, before any research. Revised 2026-10-04, after six research streams, an adversarial refutation pass over eight load-bearing claims and three completeness critics.

This is a living document. The original is kept below rather than overwritten, because this project is about documents that drift from the reality they describe, and quietly editing the founding statement to look prescient would be the same failure in miniature. Five things listed below were wrong — the first two being the two halves of a single original sentence — and one of them was the central thesis.

---

## What was believed at the outset

Verbatim from the 2026-10-03 capture, condensed only where sections repeated themselves:

> "Software factory" is, today, a thing a large system integrator sells to a large prime. The bundle usually contains SBOM generation, AV and malware scanning, developer tooling, pipeline controls, and a pile of accreditation paperwork. It is bespoke, expensive, and the integration is the product.
>
> There is no open-source project that integrates best-of-breed components into one coherent, *deployable* software factory — one that also produces SBOMs and packages artefacts for transfer through a cross-domain solution into a high-side environment. That absence is the thing worth attacking.
>
> Assembling the tools is the easy part. The value is the opinionated glue: the attestation and provenance chain, the policy gates, and an artefact and manifest format that survives a diode or CDS crossing intact. That third one is the least solved. A guard that transforms content to sanitise it breaks every digest it touches, and a one-way diode means the high side cannot call back to a transparency log, an OCSP responder, or an OIDC endpoint to verify anything. The bundle has to carry its own proof.

## What was wrong

**"There is no open-source software factory."** Konflux-CI's README describes it as *"a cloud-native software factory"* bringing together *"best-in-class open source projects"* — Apache-2.0, self-hostable. The phrase is taken. (Primary.)

**"...that also produces SBOMs."** SBOM production is commodity. Konflux attaches them, Zarf generates them by default via Syft, Iron Bank emits four formats. Both halves of the original sentence are falsifiable in ninety seconds, which is worse than being merely wrong. (Primary.)

**"The bundle has to carry its own proof" — because evidence does not cross the boundary. Refuted.** It does cross, today, by default. Hauler carries cosign signatures, attestations, SBOMs *and* the OCI 1.1 referrers graph in a standard zstd-compressed OCI layout (`--exclude-extras` defaults to false) and reconstructs the tags on the far side. `zarf package verify` performs full offline verification against a Sigstore trusted root embedded in the binary, with `--insecure-ignore-tlog` defaulting true "for air-gap" and RFC 3161 timestamp support. The test the original set — a high side independently establishing what it was given, with zero network access — **is met by an existing command**. (Verified by adversarial refutation.)

The consequence is a correction to the build plan, not a smaller version of the original one. **Do not invent a bespoke transfer format for the sneakernet case.** A standard OCI layout already crosses and is read by five tools; a new format would be a one-implementation artefact needing its own accreditation, and the first question would be "why not OCI layout?"

**And the claim that only one cross-domain implementation exists in open code — refuted.** `hairgap`, `eurydice` and ANSSI's `lidi` were found quickly. That negative was asserted with no working code search. Standing rule for everything this project writes: no universal negative over open code. The *description* of Iron Bank's `upload_to_cds.py` survives intact; only the uniqueness quantifier is deleted.

**The pitch was also stronger than the evidence.** Do not write that policy demands machine-verifiable evidence while implementations fail to deliver it. The cATO memo's "**all** security controls will need to be fed into a system level dashboard view" became "**which** security controls" by the 2024 Evaluation Criteria; those criteria accept "screen shots of control gate output as displayed in a dashboard" as evidence, so a PNG meets the requirement; automating control validation is an Objective rather than a threshold requirement; and the memo itself licenses manual controls. (Verified.)

## The current premise

Policy demands continuous evidence and names the pipeline as its source, but specifies **no machine-verifiable form** — and that gap is where the stale document walks back in.

Evidence rots because **nothing reads it**. Anything that gates a build is maintained, because it breaks loudly when it drifts. Anything read only by a human at assessment time rots silently, because nothing fails when it does.

So the buildable gap is not transport. It is four things, in rough order of tractability:

1. **A fail-closed receiver-side gate.** Hauler's disconnected-side `load` has one flag and no verification; `--ignore-errors` demotes a verification failure to a warning, "including storing images that failed verification"; `zarf package deploy --verify` defaults to `if-possible`. The evidence arrives and nothing is obliged to look at it.
2. **Shipment-level evidence.** Nothing states what a transfer is supposed to contain, who authorised it, or what policy was in force, so omission and rollback are undetectable by construction.
3. **Upstream provenance crossing.** Zarf regenerates SBOMs locally, so the packager's assertion substitutes for the builder's.
4. **The guard-mediated case**, which no open-source project models at all. Guard acceptance criteria remain blocked behind a cleared conversation, so the envelope format stays undesigned until they are answered.

## What survived untouched: outcomes over inputs

The only part of the original that verification did not dent.

Individual tools are inputs. **Every component slot is defined by the outcome it must produce**, not by the tool that produces it — a signed SBOM, a scanned artefact, a reviewed diff, a provenance attestation an auditor can check. Each slot then accepts a swappable implementation chosen by environment.

The original test case was AI-assisted development on Bedrock in a hyperscale cloud and something like LiteLLM in front of locally-hosted models in a high-side enclave: same slot, different implementation, not a separate build. The inference half of that holds — the inference seam is solved and cheap. The *harness* half does not transfer cleanly: Anthropic does not support routing Claude Code to non-Claude models through any gateway, so the harness is a licensing seam and the high side needs a different one. That is a real crack in the abstraction and it should be stated rather than smoothed over.

One correction to the reuse ambition. Toshiba's own data makes reuse a step function — it pays above 80% unchanged, does nothing between 20% and 80%, and is **net harmful below 20%**. A slot abstraction whose value is that every environment picks a different implementation sits in the dead band, unless what gets reused unchanged is the **contract** while implementations vary beneath it. That is the defensible reading and it is the intended one, but it has to be stated against the Toshiba finding rather than assumed.

## Scope

Three layers, three different disciplines:

- **Assurance substrate = platform.** Mandatory, minimal, consumed verbatim, no forking.
- **Accredited deployment patterns = a genuine product line.** A bounded family with commonality and variability modelled properly.
- **Application architecture = explicitly out of scope.** SDC (1978) and Microsoft Software Factories (2008) both died there.

Swappability belongs in the substrate and the patterns, never in how an application is built.

## Who it is for

Still: any organisation that has to answer "what is running, where did it come from, and what is wrong with it" on demand rather than annually. Cloud-first because that is where the primitives are; deployable on-premises, disconnected, air-gapped and high-side because that is where the constraint bites.

Deliberately not defence-only. Defence has the hardest constraints, so solving for it covers regulated finance, CNI, health and automotive as easier cases.

The original's non-technical half stands unchanged: for defence customers "open source" is a procurement and accreditation story as much as a technical one, and a factory nobody can get through an accreditation process is a demo. Designed in, not bolted on.

Two caveats the original did not have. **The name is a liability** — "software factory" returns one GOV.UK hit (an employment tribunal) against 321 for "secure by design", and the civilian world has settled on platform engineering. No naming decision has been taken. And **the DevSecOps Continuous Authorization Implementation Guide is DISTRIBUTION STATEMENT C**, so nothing from it may appear in any publicly publishable output, including this project's microsite; cite the cATO Evaluation Criteria (Statement A) and the Software Modernization Strategy (public) instead.

## What there is still no answer to

Flagged rather than filled, because inventing answers here is how the rest of the document got into trouble.

- **No buyer.** Zero occurrences of "design partner", "first customer", "target customer", "beachhead" or "pilot customer" across ~16,000 lines. Worse, the thesis is adversarial to the only party with a budget: the programme office wants an authorisation, and "stale provenance is a build failure" bills them for a benefit accruing to an assessor.
- **No operating model.** Who runs the factory in a customer environment, who is on call, who funds year two. This decides whether the thing is a product or a consulting engagement, and those want different architectures.
- **No cost model in money.** Sized in CPU, RAM and disk only. No figure per enclave, per tenant, per year, and no price at all for the GPU estate, which plausibly dominates and scales per enclave.
- **No response to the two failure modes the research ranked highest.** Funding-and-staffing mismatch first (on the record from the first commander of the most-cited modern factory; RAND finds current defence software factories are mostly customer-funded, which encodes SDC's 1978 failure into the budget line), measurement absence second. Keyword counts across both design documents: zero for funding, operator, operate, turnover, on-call, day-two.
- **No signing-algorithm decision.** Zero mentions of CNSA, CNSSP-15, SP 800-208, LMS, XMSS or crypto-agility, against a primitive the design itself calls catastrophic to reverse.
- **A known correctness defect.** The receiver's monotonic high-water mark is the only defence against rollback across a one-way boundary, and restoring the high side from backup resets it. It must be security state with its own integrity and restore semantics.

The curated record of what is known, with a status against each item, is `discovery/00-index.md`. Where this document and the published site disagree, the site is more recent and the site is right.
