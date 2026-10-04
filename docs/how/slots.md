# Slots and Outcomes

The founding design principle: **define every component position by the outcome it must produce, not by the tool that produces it.**

Individual tools are inputs to a process. The SBOM generator, the scanner, the IDE -- implementation details. What matters is the outcome: a signed SBOM, a scanned artefact, a reviewed diff, a provenance attestation an assessor can check.

Each position then accepts a swappable implementation chosen by environment.

## The test case that proves or breaks it

AI-assisted development uses a managed frontier model in a hyperscale cloud, and a locally-hosted open-weight model behind a gateway in a disconnected enclave.

**Same slot. Different implementation. Not a separate build.**

If the enclave needs its own build, the abstraction has failed and you have two products to maintain, two accreditations to obtain, and a second-class environment that drifts.

## Why the interface must be a Kubernetes API

The obvious implementation is configuration (a values file with a `sbomProvider: syft` key). That doesn't work, and there's a worked example of why.

Big Bang's `values.yaml` is **2,653 lines** with a **224 KB** JSON schema. At that size nothing is discoverable at runtime and nothing is validated beyond structural shape. You can't ask the cluster "which SBOM implementation is installed and how do I call it?" because the answer is spread across a configuration file, some template conditionals, and whatever actually got deployed.

A custom resource gives you two things a configuration path cannot:

- **schema-validated admission** -- a bad slot declaration is rejected at the API server
- **runtime discoverability** -- the core can query what is installed and how to invoke it

!!! note "Correction on the renderer"
    A natural follow-on is to generate those controllers with a composition tool. Two candidates were checked directly, and neither is usable yet: one publishes its latest release under a rolling `latest` tag with no semantic version since 2024, which makes it **unpinnable and therefore unusable in an air-gapped bundle**; the other is still a release candidate.

    **Keep the custom resource as the contract and write the controllers plainly for now.** The contract is renderer-independent, and committing to either option would import an unpinnable or pre-release dependency into the one component everything else depends on.

## The shape of a slot

```yaml
apiVersion: factory.example/v1
kind: SBOMProvider
metadata: { name: default }
spec:                          # what the operator wants -- vendor-neutral
  formats: [cyclonedx-1.7]
  generationContext: build     # before-build | build | after-build
  signed: true
status:
  implementation: syft/1.x     # what won
  invocation:                  # HOW TO CALL IT
    kind: TektonTask
    name: sbom-generate
    resultNames: { sbomUri: SBOM_URI }
  capabilities:
    supportedFormats: [cyclonedx-1.7, spdx-2.3]
    languageCoverage: [go, java, npm, python, rpm, deb]
    knownGaps: [c, cpp, fortran, embedded]
  conditions: [{ type: Ready, status: "True" }]
```

Three rules make this work:

**The core reads only `status`, never `spec`.** `spec` is intent; `status` is reality. Code that reads `spec` is assuming the operator got what they asked for.

**The core never names a product.** Swapping Syft for Trivy changes `status.implementation` and the referenced task. Nothing else in the factory changes.

**Capabilities are declared, so the core degrades rather than crashes.** The `knownGaps` field above is the honest one: no mainstream scanner handles C/C++ dependency resolution reliably outside one package manager, and none handles Fortran or embedded code at all. A factory that silently emits an SBOM with those components missing is producing a confident lie. One that declares the gap lets the gate require a *declared* SBOM for those languages instead.

## Expressing a review policy as an outcome

The hardest slot to abstract.

Different forges express review rules completely differently (submit requirements, approval rules, branch protection, CODEOWNERS). So the slot must not say "use two approvals in GitLab's syntax". It says:

```yaml
kind: SourceForge
spec:
  reviewPolicy:
    approvals: 2
    distinctFromAuthor: true
    staleOnNewCommits: true
status:
  implementation: gerrit/3.x
  mapping: submit-requirements    # how this forge satisfies it
```

One forge maps that to submit requirements, another to approval rules. The factory asks for the outcome and the implementation decides how.

## The 24 slots, and where the gaps are

A sweep across open-source tooling (parsing the CNCF landscape file and health-checking 250+ repositories) mapped candidates onto 24 outcome-defined slots. Most have good options under permissive licences.

**Eight are empty.** Four of them collapse into a single work item:

| Empty slot | Note |
|---|---|
| Cross-domain bundling and transfer | Two projects in 2,430 exist *because of* air-gap; **zero** address cross-domain |
| **Signed review-policy evidence** | Nothing signs "policy X was met for commit Y" -- the A transition has no artefact |
| Signed test-result evidence | A predicate is registered; nothing emits it |
| Signed VEX attestation | No registered predicate; the spec has been frozen since 2023 |
| AI-authorship attestation | Nothing across 51 surveyed AI-agent projects |
| Offline signed MCP tool catalogue | The extension-registry problem again, for agent tools |
| Signed model-weight distribution | The obvious tool has had no release in a year |
| Compliance-evidence generation | The leading project has 46 stars and no release since February |

The four predicate-shaped gaps are one job: **mint the predicates, then teach the provenance tool and the policy gate to emit and check them.** Far smaller than the slot count suggests.

## Consolidations worth taking

The slot count is 24; the component count should be much lower, because several projects credibly cover four or five positions each.

- **One build system plus its provenance tool** covers build execution, signing and test evidence under a single key-separation story.
- **One scanner** covering SBOM, vulnerabilities and misconfiguration means **one offline vulnerability-database import pipeline instead of four** -- which in a disconnected environment is the decisive argument, not the feature comparison.
- **A declarative minimal base-image builder** covers base images, their SBOMs and most of the vulnerability surface, because it *removes* findings rather than suppressing them. That is what keeps a gate switched on.
- **A secrets approach based on encrypted files rather than a server** covers the secrets slot by **removing a component from the enclave**, which is the right instinct whenever it's available.

---

**Next:** [A Worked Example](../example/connected.md) -- the slots in motion, with one bug fix traced end to end.
