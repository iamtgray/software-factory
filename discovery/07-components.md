# The component landscape: what's empty, what's a trap, what's dying

From `research/11-component-landscape.md` — 24 outcome-defined slots, 250+ repos health-checked on 2026-10-03. **Primary** unless marked; the four items in §4 I verified myself.

**Method worth reusing:** GitHub **Atom feeds** (`/releases.atom`, `/commits/main.atom`) are **not** API-rate-limited, so project health can be checked at scale without a token. That is how 250+ repos got checked with no `gh` and no auth. Also: CNCF `landscape.yml` now carries four AI categories (AI Agent, Inference, AI Native Infra, Training) that most people don't know exist. And **`ossf/landscape` is 404 on both branches** — gone.

## 1. The empty slots — this is the build list

1. **Cross-domain bundling and transfer — confirmed empty.** Zarf and Hauler do *disconnected*, not *cross-domain*. There is no guard-verifiable flat content-addressed format, no receiver-side verifier, no monotonic replay defence, no materialisation of the referrers graph into a manifest, and no chunk-level delta integrated with any OCI bundler. **Two projects in 2,430 CNCF items exist because of air-gap; zero address cross-domain.**
2. **Compliance-evidence generation — near-empty.** The OSCAL *format* is healthy; generating it from a live system is `defenseunicorns/lula` at **46 stars with no release since 2026-02**, plus a 30-star release-candidate translator. Taken with Lula 1 moving to maintenance mode and Big Bang's stale component definition, this is ours to own.
3. **VEX attestation — empty, and worse than we thought.** No registered in-toto VEX predicate (checked against v1.2.0). **`openvex/spec` has been frozen since 2023-08-22.** `vexctl` 216 stars, `go-vex` 71, `gocsaf/csaf` 72, and `chainguard-dev/vex` is **archived**. **Under 600 stars across the entire VEX tool surface.**
4. **Signed review-policy evidence — new, and the sharpest find.** Everything configures or reports; **nothing signs "policy X was met for commit Y".** So **Transition A is the only hand-off in the architecture with no signed artefact at all** — which is exactly the transition `design/02` argues becomes the integrity boundary once agents are writing code.
5. **Signed test-result evidence — new.** No registered test predicate in use. CDEvents has the vocabulary at 176 stars.
6. **Offline signed MCP tool catalogue — new.** The VS Code marketplace problem again, this time for agent tools.
7. **Signed model-weight distribution.** `sigstore/model-transparency` has had no release in a year.
8. **AI-authorship predicate** — confirmed empty across all 51 CNCF AI Agent entries.

**Items 3–6 are one work item**: mint the predicates, teach Tekton Chains and Conforma to emit and check them. That is a far smaller build than the slot count suggests.

## 2. Consolidations worth taking

- **Konflux** collapses slots 6, 7, 9, 10 and 14 — and the reason to care is not the product but that **Hermeto and Conforma arrive integrated and tested** rather than adopted blind. *Steal the assembly, not the product.*
- **Trivy** collapses 9, 11, 12 and IaC scanning. The decisive argument is operational: **one offline vulnerability-database import pipeline instead of four.**
- **apko + melange + Wolfi** collapses 8, 9 and 11 — CVEs *removed* rather than waived, which is what keeps the slot-14 gate switched on rather than disabled.
- **Tekton + Chains** collapses 6, 10 and 13 under one key-separation story.
- **SPIRE** collapses 23 and the keyless half of 10 (Fulcio's `spiffe` issuer is configuration only).
- **SOPS + age** collapses 22 by *removing a server* from the enclave — the right instinct for air-gap.

## 3. Licence traps, and the pattern behind them

**Fatal:** HashiCorp **Vault is BUSL-1.1** and its FIPS builds are Enterprise-only → use **OpenBao**. CodeQL is source-available. **Bearer is Elastic 2.0.**

**Serious:** **TruffleHog is AGPL-3.0** → gitleaks. **Coder is AGPL-3.0 *and* puts prebuilds behind Premium** — the one feature an air-gapped deployment needs. **GitLab CE puts the entire slot-5 outcome behind Premium.** InSpec relicensed to a Chef EULA.

**Moderate:** Grafana and Loki AGPL-3.0; **UDS Core is AGPL-3.0** (surprising for something DoD-adjacent); Semgrep's cross-file taint analysis is Pro; Chainguard Images are commercial; Flox is GPL-2.0.

**The pattern: in five separate cases the paid tier *is* the slot-critical feature.** Open-core vendors have converged on putting exactly the thing a regulated or disconnected deployment needs behind the licence. Assume it and check before adopting, every time.

## 4. Health — verified directly

I checked these four myself rather than taking them on report, because they bear on recommendations already made in `design/01`:

| Project | Finding | Consequence |
|---|---|---|
| **`conforma/cli`** | **v0.10.28, released 2026-10-01** — actively shipping | **Alive, not abandoned.** The 44 stars are an *adoption and bus-factor* risk, not a liveness one. Important distinction: it is the **only project that issues a signed verdict over an attestation set**, so it is simultaneously the most load-bearing and least-known thing in the stack. Contribute upstream. |
| **`tektoncd/chains`** | **v0.29.7, released 2026-10-01** — actively shipping | Alive. But 277 stars, and **the whole evidence chain hangs off it.** |
| **`syntasso/kratix`** | Latest release is literally **tagged `latest`**, updated 2026-10-02 | **Confirmed: no semver release since 2024-07.** You cannot pin a version, which is **disqualifying for an air-gapped bundle.** |
| **`kubernetes-sigs/kro`** | **v0.10.0-rc.0** | Release-candidate only. Not yet GA. |

That last pair breaks the composition-mechanism recommendation in `design/01` §7 and is corrected there.

**Dead** (reported, not personally verified): `dora-team/fourkeys` — **the canonical DORA implementation, last commit 2024-01-23, abandoned**; **`kaniko`, 15.7k stars, dead since 2025-06**; **`loft-sh/devpod`, 15k stars, last release an alpha in 2025-06**; `keptn/lifecycle-toolkit`; `tern`; `spdx-sbom-generator` (releases stop 2022); `terrascan`; `chainguard-dev/vex` archived; `devfile/api`. **FRSCA confirmed: zero releases, ever.**

**Stalled but alive:** `slsa-verifier` (15 months), `slsa-github-generator` (19 months), **`notation` stable for 18 months** despite CNCF incubating status, `archivista` (11 months), TGI effectively abandoned, **Aider quiet since 2026-05** despite 49k stars, Clair, cve-bin-tool, Pelorus, detect-secrets.

**Version numbers overstating maturity:** `hivecommons/hive` is **v5.130.1 on 62 stars** and is CNCF sandbox; `kyverno-json` has been v0.0.3 since 2024; `veraison` is v0.0.26xxxx.

### The real risk class

**Twelve sub-300-star projects sit on the critical path with no substitute:** `conforma/cli` (44), `uds-cli` (54), `sigstore/scaffolding` (89), `hermeto` (111), `archivista` (116), `trustee` (186), **`tektoncd/chains` (277)**, `compliance-trestle` (281).

This is the honest sustainability picture, and it is not a reason to abandon the approach — it is a reason to **contribute upstream to Chains, Conforma and Hermeto now**, which is cheaper than forking later. It also reframes the project's possible contribution: the most valuable thing an open-source secure factory could do for the ecosystem may be to become a *funded, accountable consumer* of three tiny projects that everything else quietly depends on.

## 5. Native disconnected support is rare, and one design is worth copying

Only **Zarf** and **Hauler** exist *because of* air-gap. Three more treat disconnected operation as first-class: **cosign** (the best offline flag surface of anything surveyed), **OSTree** (**the best delta design in open source** — a signed summary over static deltas, which is the sign-the-index pattern the transfer envelope should copy), and **Grype** (`grype zarf:/path.tar.zst`, offline, no extraction).

Also: **zot** serves an OCI layout straight from a directory, so you can rsync a registry; Pulp export/import; Hermeto; SOPS+age; Flux `OCIRepository`; ANSSI's `lidi`; and **`desync` (432 stars) — the only maintained content-defined-chunking delta tool**, which matters because chunk-level delta is a requirement for crossing a throughput-limited guard.

## 6. Recommended defaults, per slot

1 Coder + agent-sandbox · 2 vLLM + Envoy AI Gateway · 3 OpenHands · 4 Gitea, or **Gerrit if review must be evidenced** · 5 Gerrit submit requirements + gitsign · 6 Tekton + Chains · 7 Hermeto · 8 apko + melange / Wolfi · 9 Hermeto + Syft, signed · 10 cosign + Chains + go-TUF · 11 Trivy + OSV-Scanner → Dependency-Track + Copacetic · 12 Semgrep OSS + gitleaks + Grant + Checkov + bincapz · 13 Chains over a test TaskRun · 14 **Conforma** · 15 Harbor low-side / **zot high-side** · 16 Zarf + Hauler + desync · 17 Kyverno · 18 **Flux** (`OCIRepository` removes the need for a high-side git server) · 19 trestle + Lula · 20 Prometheus + OTel + CDEvents + DevLake · 21 Backstage · 22 SOPS + age · 23 SPIRE · 24 Crossplane, watching KRO.

Open-core tier boundaries are tagged unverified throughout, because pricing pages were not fetchable.
