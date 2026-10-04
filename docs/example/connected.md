# A Change, End to End

A vulnerability is reported in a library used by `payments-api`. Someone has to fix it, and the fix has to reach production with evidence an assessor could check two years later.

Throughout: **D** is the final image digest, **C** is the git commit.

---

## 1. The advisory arrives

A new CVE lands in the vulnerability database. A scheduled scan of what is *already running* flags `payments-api` as affected.

**The scan covers the running system.** The surviving US federal obligation after the 2026 deregulation is "an SBOM of the **runtime production environment** upon request", so this scan is the compliance artefact that satisfies it. Runtime SBOM assembly is thinly served: a Kubernetes operator for the *Deployed* type exists at a few hundred stars, and past that a narrow search turns up nothing.

**The finding is probably wrong.** Registry telemetry: 65% of open-source CVEs lack a severity score in the national database, and independent severity assessments agree with it only **55.7%** of the time. Matching on vendor-product identifiers against open-ended version ranges looks like the dominant source of false positives.

## 2. Triage

Is the vulnerable code **reachable** from this application?

Only one outcome is work:

| Verdict | Action | Artefact |
|---|---|---|
| Not present | Record and move on | Signed VEX: `vulnerable_code_not_present` |
| Present, unreachable | Record and move on | Signed VEX: `vulnerable_code_not_in_execute_path` |
| Reachable | Fix it | Proceed to step 3 |

If recording "not reachable" takes a ticket and a security review, it doesn't get recorded, and findings accumulate until someone disables the gate or waives it wholesale.

!!! note "A tool exists for this, with no model in the loop"
    An existing open-source tool turns a maintainer typing a single structured comment into a **Sigstore-signed in-toto VEX attestation**, authorised against a code-owners file.

    It's coupled to one forge, but through pluggable interfaces, so porting it should be bounded work. I haven't tried the port.

    The signed-VEX work stays on the build list all the same. The tool is at 10 stars, v0.0.1, one maintainer, and its own README calls it experimental.

    A model should *not* make this call either way: the best measured performance on selecting the right VEX justification is under 70%.

**52.9% of 78,000 real-world SBOMs declare no dependency edges at all.** Reachability analysis over a graph with no edges silently returns "not reachable" for everything, and detecting that degenerate case moved recall on known-exploited vulnerabilities from 0.60 to 0.95.

## 3. The fix gets written

An agent is given the ticket, the SBOM, the reachability verdict and the advisory. It proposes a dependency bump and adjusts two call sites.

Of 36,870 real upgrade recommendations analysed, **27.76% referenced versions that do not exist**. The agent resolves the dependency graph and reads the real version list, so the bump it proposes names a version that exists.

The agent's permitted actions come from the [capability descriptor](../how/primitives.md#3-the-capability-descriptor). In this tier, `single-file-change` and `test-gen` are enabled. If this had been a sprawling refactor, the descriptor would have refused it and the work would have been decomposed.

**The agent never holds a push credential.** It proposes; a separate non-model process performs the privileged action after a gate. An agent holding repository access, untrusted input and network egress can be induced to exfiltrate, and prompt engineering is not a defence.

## 4. Mechanical checks the human cannot perform

Before review, deterministic checks run on the diff:

- **Unicode normalisation and invisible-character detection.** A real worm used Unicode variation selectors that render as blank lines -- invisible in the diff views I've tried, executable to the interpreter -- and reached a major marketplace.
- **Licence and snippet scanning**, because model output can carry training-data-derived code.
- **Secret scanning.**
- Build, test, lint.

## 5. Review, and the only legally meaningful signature

A human reads the diff and signs off.

!!! danger "An agent may never sign off on its own work"
    Only a human can certify the Developer Certificate of Origin. The kernel's policy is explicit: *"You are expected to understand and to be able to defend everything you submit."*

The commit carries an `Assisted-by:` trailer naming the tools, and scrutiny is proportional to how much was generated.

This transition produces the one document I haven't found anything in open source emitting: an attestation that the review policy was met for commit **C**, carrying what was checked mechanically, who accepted the remainder, the model identity and the capability-descriptor digest. See [the empty slots](../how/slots.md#the-24-slots-and-where-the-gaps-are).

## 6. The build

An ephemeral executor, provisioned fresh. Dependencies prefetched and hash-verified *before* the network is cut, then the build runs with no network access.

**Hermeticity is a lock-file discipline problem.** If every dependency is pinned with a digest in a lock file the prefetcher understands, hermeticity is a flag; a build that fetches a tarball from a URL mid-compile makes it a project.

A hermetic build with a prefetch step has already produced a complete, hash-verified dependency list. That list *is* a build-time SBOM, and its hashes come from the fetch itself, so they describe what the compiler actually consumed.

!!! note "A common misreading the specification contradicts"
    SLSA Build Level 3 demands isolation and ephemerality, and the specification is explicit that hermeticity falls outside those requirements. I've watched teams read the two as one, conclude L3 is unreachable, and stop trying.

    The hard L3 requirement is that **cache poisoning must be impossible** -- the output must be identical whether or not the cache is used. Every CI cache I've looked at keys on a tenant-supplied cache key, which makes it poisonable. Fixing that looks like a platform rewrite.

## 7. Evidence production

The build emits, all bound to **D** by digest, all wrapped in the same envelope:

| Document | Signed by |
|---|---|
| Build provenance | Build platform key (unreachable from build steps) |
| Build-time SBOM | Build platform key |
| Vulnerability scan result | Scanner identity |
| Test results | Test task identity |
| The step-2 VEX | VEX-issuer identity |

**The SBOM must be signed**, and an author signature is now a baseline element in the current minimum-elements guidance. The most mature open factory I've looked at ships its *build-time* SBOM unsigned while cryptographically signing its *release-time* one.

## 8. The gate

Now the expensive reasoning happens, once:

- every document binds to **D**
- each signer is the expected signer for that document type
- external build parameters match an **allowlist**, and anything absent from it fails the check
- **the build only ran approved tasks** (the check I keep finding absent)
- scan findings are either below threshold or covered by a verified VEX statement from an authorised issuer

The gate signs a **verdict** recording the digest of the policy that produced it, and the model identity and capability-descriptor digest from step 3.

!!! tip "Waivers that expire by construction"
    Every real gate needs break-glass. The better implementations make exclusions carry `effectiveOn` and `effectiveUntil` dates, a link to a tracking issue, and warnings before expiry.

    Open-ended exclusions have been measured: suppressions grow **monotonically**, **50.8% suppress nothing at all**, and dead suppressions **silently mask future findings**.

## 9. Signing and promotion

The release authority signs a release approval, and signs the image. All ten documents -- build provenance, build-time SBOM, scan result, VEX, test results, review-policy evidence, AI authorship, the verdict, the release approval and the image signature -- are attached in the registry as referrers, discoverable by querying the digest.

**Hard registry requirement:** the referrers API must be supported. The fallback tag scheme is race-prone by the specification's own admission, and two concurrent attestation pushes will silently lose one.

## 10. Deployment

GitOps reconciles the new digest. Admission control verifies **a signature and the verdict**. The check is local and fits inside a webhook's time budget.

## 11. The loop closes

The running-system inventory updates. The next scheduled scan sees the new version. If a future advisory affects it, step 1 begins again with current data.

---

## What exists at the end

Ten signed documents by six distinct identities -- eight bound to the image digest **D**, and two (review-policy evidence and AI authorship) bound to the commit **C**, because that is what they are statements about:

```mermaid
graph LR
    C[commit C] -->|resolvedDependencies| P[Build provenance]
    P --> D[image D]
    S[SBOM attestation] --> D
    V[Scan result] --> D
    X[VEX] --> D
    T[Test results] --> D
    R[Review-policy evidence] --> C
    A[AI authorship] --> C
    G[<b>Verdict</b>] --> D
    RA[Release approval] --> D
    L[Image signature] --> D
    G -.->|the only one admission reads| ADM[Admission control]
```

## What this flow shows

**Admission control reads one document**, and everything else exists to justify it.

**Six identities.** If a single key signed all of this, the verdict would be worthless -- a compromised build could issue its own pass.

**The expensive step is step 2.** The fix in step 3 came to a dependency bump and two call sites.

**The scarce resource is reviewer attention.** What makes step 5 quick is a passing test suite that actually covers the diff, a reachability verdict, and a statement that this change touches nothing else.

---

**Next:** [The Same Change, Air-Gapped](airgap.md) -- the same eleven steps, where the agent and attestation discovery break, and keyless signing survives.
