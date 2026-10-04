# What deep AI integration actually does to the architecture

Written 2026-10-03, rewritten 2026-10-04 after `research/12-ai-native-factory.md` and the adversarial verification pass. This is one argument rather than an argument with revisions bolted on; where the earlier version of this document was wrong, the body says so in place.

The question: is deep AI integration a set of features bolted onto a conventional software factory, or does it change the factory's architecture?

**The answer: it does not break the primitives — it validates them.** Every AI pattern that actually works in a delivery pipeline has one shape: **a non-deterministic generator proposes, a deterministic verifier decides.** That is the delegated verdict, which the architecture already had. What AI changes is not the mechanism but the economics, and that reorientation changes what the factory is *for*.

---

## 1. AI breaks the determinism that provenance quietly assumes

The entire supply-chain integrity model assumes a derivation. SLSA provenance says *this builder, with these parameters, produced this digest*. Reproducible builds are the gold standard because they let a third party re-run the derivation and compare. Attestation is meaningful because the process is repeatable and therefore checkable.

An agent is not a derivation. Run it twice on the same ticket and you get two different diffs, both possibly correct. So the strongest claim available collapses from:

> "this artefact is the correct output of this process applied to these inputs"

to:

> "this diff was produced by this process at this time, and a named human accepted it"

That is a materially weaker guarantee, and pretending otherwise would be dishonest to an accreditor. The practical consequence is that **the accountable-acceptance step stops being quality assurance and becomes the integrity boundary.** In a classical factory, review catches mistakes while the provenance chain carries the integrity guarantee. In an AI-heavy factory, review is the only place where a non-deterministic process is converted into an accountable assertion.

This is uncomfortable, because the research also established that **human review is not a reliable detection control** — GlassWorm's Unicode variation selectors render as blank lines, invisible in editors, diffs and most static analysis but executable to the interpreter, and an infected extension reached Microsoft's own marketplace. So the integrity boundary now rests on a control that demonstrably fails against adversarial input.

The resolution is to split the two jobs explicitly and stop conflating them:

- **Machines detect.** Unicode normalisation, invisible-character detection, licence and snippet scanning, reachability analysis, test execution, policy evaluation. All mechanical, all attestable.
- **Humans are accountable.** A named person in the DCO chain asserts they understand and will defend the change. The Linux kernel got this exactly right: *"You are expected to understand and to be able to defend everything you submit"*, and agents must not add `Signed-off-by` because only a human can certify the DCO.

Neither substitutes for the other, and the attestation at that boundary should record **both** — what was checked mechanically, and who accepted the residue.

The structural gap is that this hand-off — transition A, author to source of record — is the one with no signed artefact anywhere we could find in open source. Everything either configures review rules or reports on them; nothing signs "policy X was met for commit Y". That is a weak negative rather than a proven absence (we had no working code search at scale, and the standing rule after verification is that no document in this programme asserts a universal negative over open code), but it held up against directed searching and it is the gap AI makes load-bearing.

## 2. Attention, not review, is the scarce resource — and build capacity matters *more*

Classically the expensive steps were build and test, and review was comparatively cheap. If agents generate change far faster than humans can accept it, that reverses.

The earlier version of this document said "review becomes the scarce resource" and flagged the economics as unmeasured. Verification supported the direction and corrected the noun, which matters more than it sounds. The scarce resource is not review capacity in the abstract; it is **reviewer attention, measured in human-attention-units per merged change.** And the correction that follows is the opposite of what the original implied: **build, test and CI capacity rise in importance rather than falling**, because mechanical verification is precisely how you spend less attention per change. A factory that cuts its build capacity to fund review throughput has the causality backwards.

So a factory optimised for AI-generated change is a factory optimised for **attention per change**, and everything follows from that:

- The highest-value output of the factory is no longer the artefact. It is **the evidence that makes a change cheap to review** — a blast-radius analysis, a reachability verdict, a passing test suite that actually covers the diff, a statement that this change touches nothing else.
- Gates must have brutally low false-positive rates, because a reviewer drowning in findings approves blind. CPE false positives are the dominant cause of unusable gates, and fixing the base image *removes* findings rather than suppressing them. That is no longer a hygiene preference; it is load-bearing, because a gate that gets switched off has zero value and a gate that exhausts reviewers has negative value.
- The factory should attest what it checked mechanically **so the human reviews only what is left.** That is the single most useful thing it can do for throughput.
- Feedback quality beats breadth. DORA 2025 found that clear, actionable feedback on task outcomes is *the* platform attribute most correlated with positive user experience — and it is nearly absent from every vendor maturity model. A red cross over a 4,000-line SARIF file is a failure even when the finding is correct.

One commercial observation, which is mine rather than a research finding and should be treated as such: this is the only argument in the programme that bills the party that benefits. "Stale provenance is a build failure" charges a delivery team for a benefit accruing to an assessor. "Here is the evidence that makes your change cheap to review" charges them for something they feel the same week. If the programme ever finds a first customer, this section is the reason they say yes.

## 3. The evidence graph is also the agent's context substrate

This is the one I think is non-obvious and most important.

Every piece of evidence the factory produces today — SBOMs, provenance, scan results, VEX, test results, control narratives — is produced *for humans and auditors*, and almost nobody reads it.

The diagnosis needs stating carefully, because the obvious version of it is wrong and verification refuted it. **Evidence does cross an air-gap.** Hauler carries cosign signatures, attestations, SBOMs and the OCI 1.1 referrers graph by default in a standard zstd-compressed OCI layout and reconstructs the tags on the far side; `zarf package verify` performs full offline verification against a Sigstore trusted root embedded in the binary. Transport is solved and has been for a while. What is missing is a **fail-closed receiver**: Hauler's disconnected-side `load` has no verification, its `--ignore-errors` demotes a verification failure to a warning and will store images that failed verification, and `zarf package deploy --verify` defaults to `if-possible`. So the evidence arrives and nothing is obliged to look at it.

The same mechanism, one layer up, explains the implementation evidence:

- Iron Bank's cross-domain job cosign-verifies on the low side and then **discards the signature**, shipping a bare gzipped OCI layout; the sibling job routes the SBOM, scan and VAT directories to a *different* bucket. The artefact and its evidence diverge one step before the boundary, and nothing downstream complains.
- Big Bang's OSCAL component definition is the cleaner case, and the earlier version of this document got it wrong. I said it had been "stale for three and a half years". **The file has six commits ever.** The last substantive edit was April 2023; the two commits after it are a URL fix following a repository rename and a global departmental find-and-replace from DoD to DoW. So the content is roughly three years stale, but the mechanism is more damning than neglect: **mechanical sweeps make it look maintained in the commit log** while nobody has reviewed its substance. Its metadata still claims 2022. It fails `compliance-trestle` with ten duplicated UUIDs, and nobody caught that because the OSCAL component-definition model has no referential-integrity constraint and the standard validator short-circuits to `true` — the format cannot tell you it is broken.
- The sharper version of the same story is the gate, with dates: Big Bang **built** live-cluster OSCAL validation in February 2024, **disabled** the gate in August 2024 citing "known issues", and **deleted** it in September 2025.

So: anything gating a build is maintained; anything read only by a human at accreditation time rots, because nothing fails when it does.

Put an agent in the loop and that changes, because the agent *wants* this data:

- An agent fixing a CVE needs the SBOM, the reachability analysis and the VEX history to decide whether the finding is real.
- An agent proposing a dependency bump needs the provenance of what it is bumping to.
- An agent writing a control narrative needs the running system's actual configuration, not a document whose metadata says 2022.
- An agent triaging a failure needs the test-result and scan attestations for the last known-good build.

So the factory's evidence graph becomes **machine-consumable context in the hot path**, which gives a sharper diagnosis than the one I had: evidence rots not merely because nothing fails when it rots, but because **nothing reads it**. Give it a reader with an appetite and the freshness problem partly solves itself, because stale context produces visibly worse agent output.

Two pieces of telemetry make this empirical rather than hopeful.

**Sonatype 2026: of 36,870 real upgrade recommendations, 27.76% referenced non-existent versions.** That is what ungrounded generation looks like at production scale — more than a quarter of the advice points at a release that does not exist. An agent with the dependency graph in front of it cannot make that error; an agent without it makes it a quarter of the time. The same dataset reports that about 95% of vulnerable component downloads had a fix already available, which tells you the factory's job is not *finding* the problem.

**DORA 2025: "When platform quality is high, the effect of AI adoption on organizational performance becomes strong and positive… when platform quality is low, the effect is negligible."** That is the strongest external support the whole position has, and it runs the right way round: platform quality is not a nice-to-have alongside AI adoption, it is the thing that decides whether AI adoption pays at all. Evidence quality is a component of platform quality, which makes the evidence graph an AI-enablement investment rather than a compliance one.

Two architectural consequences:

- **Evidence must be queryable, not merely attached.** OCI referrers answer "what is attached to this digest". They cannot answer "which images contain this purl", "what was built from this commit", "which artefacts does this new CVE affect". Those are graph questions, and they are exactly the questions an agent asks. This upgrades the graph store from a nice-to-have to a core component — and makes Archivista's insight (in-toto `subject`s are graph edges, so you traverse from a commit to everything built from it) more interesting than GUAC's heavier ambition, given GUAC's recommended backend is still non-persistent in-memory.
- **Evidence freshness becomes measurable through use.** If an agent's context includes the provenance of what it is modifying, a stale or missing attestation degrades a visible output rather than lurking until accreditation.

I think this is the strongest argument for the project, and it is a *better* argument than the air-gap one because it applies to every customer rather than only the ones with diodes. The air-gap case remains the sharpest demonstration; this is the general case.

## 4. The five primitives hold — and AI stresses three of them

The original formulation had three primitives. Verification found two more — trust configuration and freshness state — which had been quietly treated as fields in a manifest rather than as things the architecture must carry everywhere. That was a real hole, and it matters here because one of the two missing primitives is the one AI leans on hardest.

| Primitive | What AI does to it |
|---|---|
| **1. Digest-bound statement** | Holds unchanged, and is barely stressed. An AI-authorship predicate is just another `predicateType` over a diff digest; an eval-result predicate fits the same way. |
| **2. Delegated verdict** | **Stressed, and gains a rule.** See below. |
| **3. Capability descriptor** | **Stressed hardest.** Promoted from peripheral to central, and must carry measured rather than declared capability. |
| **4. Trust configuration** | Lightly stressed. Model weights cross the airlock signed — `sigstore/model-transparency` signs them via PKCS#11/HSM into a DSSE in-toto bundle with per-file digests, so they travel the *same* path as container images. That adds a signer to the trust root chain, not a new mechanism. Hard reject on pickle; safetensors only. |
| **5. Freshness and monotonicity state** | **Stressed, and this is the one the original three-primitive formulation would have missed.** Every AI verdict has a freshness dependency: the eval score behind a capability claim, the model and harness version behind a diff, the vulnerability-database version behind a triage verdict. An eval score with no `validNotAfter` is a promise about a system that has since been upgraded. |

I briefly thought accountable human acceptance was a further primitive. It is not: **it is the delegated verdict applied at the human boundary.** A party performs a verification that downstream cannot repeat, and signs a cheap assertion that downstream trusts instead. That is precisely the VSA pattern and precisely the trusted-importer pattern. The human reviewer is a third instance of the same shape, with the same safety rules: record what policy was in force, and never let the producer also be the verifier.

That is a satisfying result, because one mechanism covers the gate, the cross-domain importer and the human reviewer. One implementation, one audit format, one honest sentence about where trust delegates.

**The rule AI adds to primitive 2:** the verdict must record the **model identity and the capability-descriptor digest** alongside the policy digest, so that a model swap detectably invalidates prior verdicts exactly as a policy change does. That was the hole in the original version of this section. Without it, a model upgrade — which per the research can change capability by a large factor from the *same* base model, on a post-training cadence rather than a hardware one — silently inherits every verdict issued by its predecessor.

**The rule AI adds to primitive 3:** the descriptor must publish **last night's signed eval score**, not a hand-maintained `outcomesEnabled` list. Otherwise it is a promise rather than a property, and it rots like every other hand-written artefact — which is the failure mode this entire document is about.

The capability descriptor earns its promotion for a specific reason: if agent capability varies by tier, then **task granularity and review policy must vary with it too.** A GPU-poor enclave at roughly half of frontier capability should not merely have "autonomous multi-file change" disabled; it should decompose work into smaller units and apply *more* human scrutiny per change. That makes the descriptor an input to the review policy, not just a feature flag — and it makes degradation a declared, gate-enforced property rather than observed flakiness.

## 5. A fifth transition: agent → agent, and the recommendation is don't

The architecture had four trust-domain transitions: A author→source of record, B build→judgement, C low side→high side, D registry→runtime. Deep AI integration adds a fifth, **A′ agent→agent**, and the recommendation is to decline it.

**Keep agents as leaves. No delegation chains in the core.** Two reasons:

- **Attribution laundering.** A delegation chain destroys the link between a change and an accountable identity, which is the one thing §1 establishes the architecture cannot afford to lose. If an agent accepts work from another agent, the DCO chain terminates in nobody.
- **Correlated verifiers.** "Independent" verifying agents collapse to very few genuinely corruption-distinct domains — same weights family, same harness, same prompt lineage, same tool surface — so redundancy buys far less than the agent count suggests. Five agents agreeing is not five checks.

This is a declining rather than a deferral. A multi-agent planner is the kind of thing that looks like capability and is actually an un-attestable hand-off, and it belongs in the set of things that die in an enclave and should not be mourned (see §7).

## 6. The provenance fork for spec-driven development

If the spec becomes the source of truth and code is generated from it, what gets attested? Two options:

**Option A — attest the spec, treat code as a build output.** Intellectually cleaner and matches how we treat compiled artefacts. It requires generation to be reproducible, which with a hosted frontier model it is not.

**Option B — keep attesting the commit; record the spec, prompts, model identity and eval results as *inputs*.** The spec goes in `resolvedDependencies` exactly like a lock file. Generated code is committed and reviewed, so transition A still carries accountability.

**Option B, clearly.** It preserves the existing architecture entirely, costs almost nothing, and keeps a human in the DCO chain, which no regime currently lets you avoid.

The earlier version of this document hedged towards Option A on the grounds that an air-gapped enclave with pinned weights, a pinned harness, a pinned prompt and temperature zero is the one environment where reproducible generation is natural. The research weakened that considerably, and in an interesting way: a pre-registered study found the *uncited* generation condition is significantly **more** deterministic (d ≈ −0.72 to −0.76), while **only** the cited condition enables hallucination detection (86–88% versus 0%). So **verifiability and determinism trade off structurally.** You cannot have both, and the more reproducible configuration is the less checkable one.

That makes Option A less attractive even where it is achievable, and it argues for a different move entirely: a **deterministic citation-resolution check** at verify time, which gets 86–88% hallucination detection at a 0% false-positive rate with no model in the verification path. Take that over chasing reproducible generation.

The pinned-weights-in-an-enclave observation survives only as an unverified curiosity, not a plan: if deterministic generation ever becomes worth having, the high side is where it becomes feasible first. That is mine, untested, and nothing in the design depends on it.

## 7. The three seams, honestly: inference yes, harness partly, capability no

The research's verdict on whether you can run this at all, seam by seam. It is worth keeping in this blunt form because two of the three answers are not the ones a vendor would give.

**The inference seam: yes, and cheaply.** Solved by configuration. MIT and Apache-2.0 weights are available at every size band that matters, so accreditation does not require accepting a bespoke licence. Bedrock is GA in both GovCloud regions with frontier Claude models available — read the columns, because newest models are often Geo-cross-region rather than in-region, and the Mantle endpoint offers better in-region residency in `us-gov-west-1`. Treat it as a four-dimensional lookup rather than a yes/no. Bedrock Custom Model Import is *unavailable* in GovCloud, which is a useful accident: the air-gap self-hosted implementation is also the GovCloud fine-tune implementation, so it earns its keep even if you never ship to a classified enclave. ADC service availability is not publicly enumerable, so do not architect on a managed frontier API existing high-side.

**The harness seam: partly, and it is a licensing problem rather than a technical one.** Anthropic does not support routing Claude Code to non-Claude models through any gateway and is adding an `allowedProviders` pin, so Claude Code is a valid harness in the cloud tiers via Bedrock but cannot be the high-side default. Mirroring the VS Code Marketplace is legally barred, including for non-Microsoft extensions, with real and recent enforcement; Open VSX carries 18,827 extensions against the Marketplace's 150,956, and several of the ones developers expect are permanently absent. Open VSX Mirror Mode copies metadata only and a partial mirror deletes everything it does not match, so the right tool for a disconnected registry is a curated digest-pinned inventory. The workspace layer thinned badly in 2026 — only Eclipse Che and Coder remain credible for air-gap, with `kubernetes-sigs/agent-sandbox` as the per-task sandbox substrate. None of this is unsolvable; all of it is procurement and packaging work that nobody budgets for.

**The capability seam: no, and the cliff is hardware rather than classification.** The GPU-poor tier sits at 48–60% of frontier across two benchmarks. Parity needs 320B–750B parameters, which is 4–8 H200s. Against that, an open-weight model placed fourth of seventeen at 62.9% versus a 64.5% leader on the one contamination-controlled independent leaderboard reachable, within overlapping error bars, with the highest pass@any on the board, at a third of the cost. So open weights reached frontier parity during 2026 *if you buy the GPUs*, and capability now moves on a post-training cadence, which means the airlock cadence rather than the hardware refresh determines high-side capability over time.

And the inversion, which is better news than the capability answer suggests: **the air-gapped tier gets the *better* AI story, not the worse one — because what survives without frontier models is exactly the set of patterns that have deterministic verifiers, which is exactly the set that is attestable.**

What survives: false-positive triage of scanner findings (the strongest real result in the field — F1 0.912–0.955, with one deployment eliminating 94–98% of false positives at under $0.12 per alarm against 10–20 minutes of human time), validated test generation behind a filter chain (75% build / 57% pass / 25% coverage gain, so roughly three in four discarded), mechanical refactoring from recipes, local eval harnesses, agent sandboxing.

What dies: agentic review as a gate (31,073 comments in the wild, 56.3% rejected and 36.4% accepted, and nothing emitting a signed verdict), autonomous multi-file remediation, VEX justification selection (under 70% macro-F1 on choosing the justification), multi-agent planning. Mostly things a factory should not have trusted anyway.

The factory's own agent has all three legs of the lethal trifecta by default — private data, untrusted content, external communication — and that must be broken structurally rather than by prompt engineering: the agent never holds a push credential, tool output is untrusted input that may never alter the agent's permissions or instructions, no dynamic tool loading, and agents stay leaves per §5. The critical vulnerabilities in agent harnesses are structural rather than model-behavioural — CI credential and configuration handling, with all four major providers vulnerable by default — which is why the authorship predicate records credential and egress posture.

## 8. What this means for the build list

**Build:**

1. **The AI-authorship predicate**, carrying harness, model identity and licence, tier, the capability-descriptor digest, the spec and context-file digests, and **the credential and egress posture the agent ran under**. Nothing registered covers this, so minting a predicate is the right move — the envelope rule is "mint custom predicates freely, never a custom envelope", and this is the former.
2. **An eval-result attestation by extending the already-registered `test-result/v0.1`**, not by minting a type. Reportedly about a day's work and the best value-for-effort item on the list, because it makes a model or harness swap gate-able like any other dependency change instead of landing silently. Three predicates are already registered — `test-result/v0.1`, `runtime-trace/v0.1` and `svr/v0.2` — and the discipline is to extend those three before inventing anything. My own `research/03` listed them and the first draft of this document missed it.
3. **An attested agent-run record**, extending the registered `runtime-trace/v0.1` and sourced from durable workflow history **captured outside the agent's reach**. We found nothing doing this, though with no code search at scale that is a weak negative rather than a proven absence. It is what makes an agent run auditable rather than merely logged.
4. **The queryable evidence graph**, first-class, because it is the agent's context substrate as well as the auditor's record. Sonatype's 27.76% of 36,870 upgrade recommendations pointing at non-existent versions is the empirical case, and DORA's platform-quality finding is the commercial one.
5. **Three-valued reachability with a degeneracy detector.** 52.9% of 78,000 real SBOMs declare no dependency edges at all, and detecting that degenerate case moved KEV recall from 0.600 to 0.950. Cheap, mechanical, large effect.
6. **Signed VEX.** An earlier version of this document struck this item on the grounds that `openvex/vexflow` already does it — Sigstore-signed in-toto OpenVEX attestations from a maintainer's one-line comment, OWNERS-authorised, GitHub-coupled through pluggable `api.Scanner` / `api.VexPublisher` interfaces. That was too generous. **It is v0.0.1, 10 stars, one maintainer, and its own README calls it experimental.** Adopting it means owning it, so the item stays on the build list: take the design as a head start, budget for the implementation. There is also still no registered in-toto predicate for VEX, and `openvex/spec` has been frozen since August 2023, so this is a mint-a-predicate case too. Notably vexflow contains no AI at all, and a model should not be trusted with the justification decision anyway.

**Adopt:** `Inspect` (MIT, UK AISI) for evals — local providers, sandboxing, and an `EvalLog` with a header/sample split that is straightforward to sign. `Temporal` (MIT) or `Dapr Agents` (Apache-2.0, CNCF, where every MCP tool call is already a durably recorded child workflow) for durable agent runs — explicitly **not** Restate (BSL) or Inngest (SSPL). `OpenRewrite` for mechanical refactoring, which is deterministic, reproducible, offline and **strictly better than a model wherever a recipe exists**. `complyctl` plus Gemara, which pulls policy **from an OCI registry** — the same transport shape as the transfer envelope. Prefer CLI-in-sandbox over MCP for build, scan and SBOM work: MCP is under the Linux Foundation with a real deprecation policy, which is the strongest maturity signal in the stack for a ten-year interface, but tool schemas cost context and context is the scarcest resource on a GPU-poor high side.

**Decline:** `AGENTS.md` as a capability lever. Two independent studies find no correctness gain and over 20% cost increase. Keep it for *constraints*, not performance.

**And one item that needs restating rather than reframing.** The earlier version of this document said continuously generated OSCAL "becomes an instance of the general rule that evidence should have a machine reader" and that we would own the capability. The rule is right; the serialisation was a mistake, and the research makes the first draft look naive.

**OSCAL is an ecosystem graveyard.** One project deleted its OSCAL saying *"OSCAL proved too complex… automated tests alone were insufficient"*; a government automation repository is 404; two vendors migrated away; a third archived both attempts; the next major version has no active work; and **OSCAL has zero occurrences across all eight cached DoD primary documents** — it is not even demanded. Lula 1 (observed-state to OSCAL) is in maintenance mode, replaced by an eMASS spreadsheet importer. That is not an unoccupied gap; it is multiple well-resourced organisations building the same automation and abandoning it, at least one of them saying why.

So: **never pitch "we generate OSCAL". Pitch the outcome and keep the serialisation swappable.** The outcome — continuous, machine-readable control status an authorising official can act on — is what the policy actually asks for, and it is worth being precise about how much it asks. The DoD Software Modernization Strategy names the source: it "couples this validation with automation to produce real-time and continuous evidence… identify **pipeline and process-generated evidence** that verifies appropriate protections are in place". But no primary specifies a machine-verifiable *form*. The 2024 cATO Evaluation Criteria accepts "screen shots of control gate output as displayed in a dashboard" as evidence, so a PNG meets the requirement, and "automate security control configurations and validation" is an Objective rather than a threshold.

The honest statement is therefore narrower than the one the project started with, and more useful: **policy demands continuous evidence and names the pipeline as its source, but specifies no machine-verifiable form — and that gap is exactly where the stale document returns.** Big Bang's six-commit component definition is what fills a gap shaped like that. An agent that reads the evidence is the first reader with both an appetite and a reason to complain when it is wrong, which is why this belongs in an AI document at all.

## 9. What I am least sure about

- **The money.** This document commits the programme to GPUs and says nothing about what they cost. The capability answer in §7 is "4–8 H200s for parity", which plausibly dominates the cost of an enclave and scales *per* enclave — and there is no figure anywhere in the design for it, per enclave, per tenant, per year. That is the largest open question here and it is a commercial one, not a technical one. It needs a number before anyone is shown this.
- **Who runs it.** Nothing in this document establishes who operates the agent estate in a customer environment, who is on call when the inference endpoint degrades, or who funds the eval harness in year two. An eval score that is only trustworthy if it was produced last night is an operational commitment, not an artefact.
- Whether the queryable-graph claim survives contact with how agents actually consume context. It may be that a repository map plus targeted search beats a formal evidence graph, which is what the GPU-poor context-budget finding would suggest.
- Whether anyone treats an agent run as a durable, replayable, attestable workflow today, or whether that is all still chat-shaped. Asked, and the answer so far is a weak negative.
- The pinned-weights reproducible-generation inversion in §6 is mine and untested, and nothing depends on it.
