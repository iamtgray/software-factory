# Slots and Outcomes

**Every component position is defined by the outcome it must produce.** The SBOM generator, the scanner, the IDE are inputs -- which one you pick is an implementation detail. The outcome names the position: a signed SBOM, a scanned artefact, a reviewed diff, a provenance attestation an assessor can check.

## The test case

AI-assisted development stretches the idea furthest: a managed frontier model in a hyperscale cloud, and a locally-hosted open-weight model behind a gateway in a disconnected enclave. Both fill the same slot, out of one build.

If the enclave needs its own build, the abstraction has failed -- two products to maintain, two accreditations to obtain, and a second-class environment that quietly drifts.

## Why the interface should be a Kubernetes API

The obvious implementation is configuration -- a values file with a `sbomProvider: syft` key.

Big Bang's `values.yaml` is **2,653 lines** with a **224 KB** JSON schema -- at that size nothing is discoverable at runtime, and validation stops at structural shape. You can't ask the cluster "which SBOM implementation is installed and how do I call it?" because the answer is spread across a configuration file, some template conditionals, and whatever actually got deployed.

A custom resource does what a values file can't:

- a bad slot declaration gets rejected at the API server, because the schema is enforced at admission
- the core can query what is installed and how to invoke it

!!! note "On generating the controllers"
    A natural follow-on is to generate those controllers with a composition tool. The two candidates aren't usable yet: one publishes its latest release under a rolling `latest` tag with no semantic version since 2024, which makes it **unpinnable and therefore unusable in an air-gapped bundle**; the other is still a release candidate.

    So the custom resource stays the contract -- it's renderer-independent -- and the controllers get written plainly.

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

**The core reads only `status`.** Code that reads `spec` is assuming the operator got what they asked for.

**The core never names a product.** Swapping Syft for Trivy changes `status.implementation` and the referenced task, and nothing else in the factory.

**Capabilities are declared, so the core degrades gracefully when an implementation falls short.** No mainstream scanner I checked resolves C/C++ dependencies reliably outside one package manager, and none touch Fortran or embedded code at all. Declaring the gap lets the gate require a *declared* SBOM for those languages.

## Expressing a review policy as an outcome

Every forge expresses review rules differently (submit requirements, approval rules, branch protection, CODEOWNERS). So the slot states the review outcome in forge-neutral terms and leaves the syntax to whichever forge is installed:

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

## The 24 slots, and where the gaps are

I mapped candidates onto 24 outcome-defined slots, working from the CNCF landscape file and health-checking 250+ repositories.

**Eight are empty.**

| Empty slot | Note |
|---|---|
| Cross-domain bundling and transfer | Two projects in 2,430 exist *because of* air-gap; none of them address cross-domain |
| **Signed review-policy evidence** | Nothing in the survey signs "policy X was met for commit Y" -- [hand-off A](handoffs.md) has no artefact |
| Signed test-result evidence | A predicate is registered; nothing emits it |
| Signed VEX attestation | No registered predicate, and the spec has been frozen since 2023 |
| AI-authorship attestation | Nothing in the 51 AI-agent projects checked |
| Offline signed MCP tool catalogue | The extension-registry problem again, for agent tools |
| Signed model-weight distribution | The obvious tool has had no release in a year |
| Compliance-evidence generation | The leading project has 46 stars and no release since February |

Four of those rows are the same job: mint the predicates, then teach the provenance tool and the policy gate to emit and check them.

## Consolidations worth taking

The slot count is 24; the component count should come out much lower, because several projects credibly cover four or five positions each.

- **One build system plus its provenance tool** covers build execution, signing and test evidence under a single key-separation story.
- **One scanner** covering SBOM, vulnerabilities and misconfiguration means **one offline vulnerability-database import pipeline, down from four**.
- **A declarative minimal base-image builder** covers base images, their SBOMs and most of the vulnerability surface, because it *removes* findings at source.
- **A secrets approach based on encrypted files** covers the secrets slot and **removes a component from the enclave** -- there's no server to stand up and keep running inside it.

Cross-domain transfer and signed review-policy evidence are unavoidable; AI-authorship attestation could sit on the shelf for a year without anyone noticing. Which of the eight block your first accreditation?

---

**Next:** [A Worked Example](../example/connected.md) -- the slots in motion, with one bug fix traced end to end.
