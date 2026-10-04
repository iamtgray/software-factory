# Big Bang, verified by inspection — and one find the research missed

Verified 2026-10-03 against a shallow clone of `repo1.dso.mil/big-bang/bigbang` at chart version **3.34.0**. Clones with no CAC, Apache-2.0 licence present at root (unlike `ironbank-pipeline`, which has none).

## Confirmed

**Big Bang is not an umbrella chart with subcharts.** `chart/Chart.yaml` is `type: application`, has no `dependencies:` key, and there is no `chart/charts/` directory. What it actually does is use Helm to template 48 Flux `HelmRelease` custom resources. This matters because "umbrella chart with conditional subcharts" is the pattern everyone assumes Big Bang uses, and it isn't — so advice derived from that assumption is wrong. I had it wrong in an earlier summary.

**The values surface is as bad as reported.** `chart/values.yaml` is 2,653 lines and `chart/values.schema.json` is 224 KB. (Research said 131 KB; the discrepancy is probably a version difference, so take 224 KB for 3.34.0.) This is the counter-argument to using a Helm values path as a capability interface: at this size nothing is discoverable at runtime and nothing is validated beyond JSON Schema shape.

**The factory-shaped slots are commercial.** The vulnerability-scanning options are, verbatim from `docs/packages/index.md` and `categorization.md`: **Anchore Enterprise** (the Big Bang values key is literally `packages.anchoreEnterprise`, source repo `anchore-enterprise`), **Fortify**, and SonarQube. Two of the three need a licence. Combined with GitLab Ultimate for dependency scanning, an all-open-source Big Bang software factory does not exist. Mine the patterns; don't adopt it as substrate.

## The find the research missed, and it's a good one

Big Bang ships **`oscal-component.yaml` at its repository root** — 1,069 lines of OSCAL component definition, mapping components like the Istio control plane to responsible roles and controls. This is exactly the machine-readable compliance artefact that makes "inherit controls from the platform" work, and therefore exactly the mechanism underneath the cATO value proposition.

Except look at its metadata: `last-modified: 2022-06-06`, `version: 1.39.0`, `oscal-version: 1.0.4`. The chart is at 3.34.0, targeting Kubernetes 1.34.

> **CORRECTED 2026-10-03 — do not use the "untouched for 3.5 years" framing.** I originally inferred abandonment from that metadata. The file has **6 commits in its entire history and was last touched 2026-08-12.** It is not abandoned; **its own self-description is false**, which is a sharper finding than neglect: the content drifted while the one field an auditor would read to judge freshness was never updated, because nothing checks it. It also **fails `compliance-trestle 5.1.0`** with ten duplicated UUIDs — and that went unnoticed because **the OSCAL component-definition model has no referential-integrity constraint** (the SSP model does) and trestle's `RefsValidator` short-circuits to `True`. The format cannot tell you it is broken.
>
> The stronger version of the story, with dates: Big Bang **built** live-cluster OSCAL validation (Feb 2024), **disabled** the gate (Aug 2024, reason: "known issues"), **deleted** it (Sep 2025), and **replaced the file with a markdown table**. Someone built the machine that checks the evidence, it returned inconvenient results, the gate was switched off, and the capability was removed. Full detail and the OSCAL-ecosystem retreat in [09](09-oscal-graveyard-and-cato.md).

That is the same disease as `upload_to_cds.py` in a different organ. The artefacts that constitute *evidence* are the ones nobody maintains, because nothing in the pipeline fails when they rot. Everything that gates a build gets maintained; everything that only gets read by a human at accreditation time decays silently.

**This is a second instance of the thesis, and it generalises it.** The problem is not specifically about diodes. It is that evidence is produced as a side effect, stored somewhere nobody reads, and never verified against the thing it describes. A factory worth building makes evidence a first-class artefact with its own freshness and verification gates — so that stale provenance is a build failure, not a surprise.

Worth considering whether "continuously verified OSCAL that is generated from the running system rather than hand-written" is an outcome in its own right.

## Other claims from the research worth treating as unverified until checked

- RKE2 FIPS: 140-2 via BoringCrypto rather than 140-3, and only Canal rebuilt for FIPS so Cilium breaks the claim. Not yet verified here. If true it is a procurement gate, so verify before writing it in anything customer-facing.
- Harbor replication silently dropping legacy-cosign signatures (issue #20412). Not verified. If true, a transport conformance test is mandatory.
- Big Bang has no umbrella-level image registry rewrite, so pod specs keep naming `registry1.dso.mil`. Plausible given the HelmRelease structure, not verified.

## Recommended architecture from the research, recorded for decision later

RKE2 substrate (Talos as alternative), Flux v2 for GitOps, project-owned capability CRDs rendered by KRO or Kratix and selected by a single `FactoryProfile`, Zarf OCI packages for transport, Tekton plus Chains for CI, ephemeral BuildKit per build with ko/apko preferred, Zot for small deployments and Harbor for larger, Forgejo as default forge, one cluster per environment.

> **Correction, 2026-10-03, verified directly — the renderer half of this is not yet buildable.**
>
> The CRD-as-interface conclusion stands. The *renderer* recommendation does not. I checked both candidates myself via their GitHub release feeds:
>
> - **`syntasso/kratix`** — the most recent release is literally **tagged `latest`** (updated 2026-10-02), with **no semver release since 2024-07**. You cannot pin a version, which is **disqualifying for an air-gapped bundle**, because a Zarf package must reference an immutable tag.
> - **`kubernetes-sigs/kro`** — **`v0.10.0-rc.0`**. Release candidate, not GA.
>
> So keep the slot *contract* as a project-owned CRD, but **write the controllers plainly for now** — one small controller per slot, or a single controller with a slot-type switch — and treat KRO as a migration target once it reaches GA. The contract is renderer-independent, and committing to either option today would import an unpinnable or pre-GA dependency into the component every other slot depends on.
>
> Two further corrections to the list above, from the same sweep: **`kaniko` is dead** (15.7k stars, nothing since 2025-06), so ephemeral BuildKit is now the only credible unprivileged builder rather than one of two. And **Vault is BUSL-1.1** with FIPS builds behind Enterprise — use **OpenBao**, or better **SOPS + age**, which removes a server from the enclave entirely.

Footprint target 8 vCPU / 24 GB / 200 GB across three nodes, against UDS dev at 9 CPU / 28 GB and Big Bang's evaluation quickstart at 8 CPU / 32 GB — both explicitly labelled not production sizings, and Big Bang now publishes no production minimum at all. The saving comes mainly from Forgejo instead of GitLab.
