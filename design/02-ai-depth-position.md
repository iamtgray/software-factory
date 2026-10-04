# What deep AI integration actually does to the architecture

A position, argued ahead of the research that will test it. Written 2026-10-03. `research/12-ai-native-factory.md` is being compiled now and may correct parts of this; where a claim depends on that research I have said so.

The question: is deep AI integration a set of features bolted onto a conventional software factory, or does it change the factory's architecture?

**My answer: it does not break the three primitives, but it inverts the factory's economics, and that inversion changes what the factory is *for*.** Four consequences follow, and the third is the one I think matters most.

---

> ## Revised 2026-10-03 after `research/12-ai-native-factory.md`
>
> The research tested this position and largely upheld it, with one sharper formulation and five corrections. Recorded here rather than silently edited, because a document that quietly rewrites its own history is the disease this project exists to cure.
>
> **The better formulation, which I am adopting:** every AI pattern that actually works in a delivery pipeline has one shape — **a non-deterministic generator proposes, a deterministic verifier decides.** So *AI does not change the architecture; it validates it.* That is a stronger and more useful claim than "it extends the model", and it explains why the three primitives survive rather than merely asserting that they do.
>
> **Corrections, in order of how much they change:**
>
> 1. **One of my build items does not need building.** `openvex/vexflow` (Apache-2.0, Go) already turns a maintainer typing `/not_affected:vulnerable_code_not_present` into a **Sigstore-signed in-toto OpenVEX attestation**, with OWNERS-based authorisation. It is GitHub-coupled but via pluggable `api.Scanner` / `api.VexPublisher` interfaces, so the work is a bounded port to an air-gapped forge rather than a new design. Notably it contains **no AI at all** — and VEX-Bench suggests a model should not be trusted with that decision anyway (<70% macro-F1 on justification selection). **Port, do not build.**
> 2. **Three predicates I assumed I would mint are already registered**: `test-result/v0.1`, `runtime-trace/v0.1` and `svr/v0.2`. The eval-result attestation should **extend `test-result`**, not invent a type — reportedly about a day's work, and the best value-for-effort item on the list. My own `research/03` listed these and I missed it.
> 3. **Primitive 2 needs one more rule.** The verdict must record the **model identity and capability-descriptor digest** alongside the policy digest, so that *a model swap detectably invalidates prior verdicts exactly as a policy change does.* That is the hole in my §4 and it is a good catch.
> 4. **Primitive 3 should carry measured capability, not declared.** The descriptor should publish last night's **signed eval score**, not a hand-maintained `outcomes_enabled` list. Otherwise it is a promise rather than a property, and it rots like every other hand-written artefact.
> 5. **There is a fifth transition: A′, agent→agent.** Do not build a multi-agent delegation chain in the core — keep agents as leaves. Two reasons: attribution laundering (a chain destroys the link between a change and an accountable identity), and the fact that "independent" verifying agents collapse to very few corruption-distinct domains, so redundancy buys less than it appears to.
>
> **And one inversion that is better news than anything in my original §3:** the air-gapped tier gets the ***better*** AI story, not the worse one — because what survives without frontier models is exactly the set of patterns that have deterministic verifiers, which is exactly the set that is attestable. My §4 framing of "degradation must be explicit" is still right, but it undersold this. The things that die in an enclave (agentic review as a gate, autonomous multi-file remediation, VEX justification selection, multi-agent planning) are mostly things a factory should not have trusted anyway.
>
> Claims of mine the research weakened: the reproducible-generation speculation in §5 (see the note added there), and the review-bottleneck economics in §2, which remains unmeasured.

---

## 1. AI breaks the determinism that provenance quietly assumes

The entire supply-chain integrity model assumes a derivation. SLSA provenance says *this builder, with these parameters, produced this digest*. Reproducible builds are the gold standard because they let a third party re-run the derivation and compare. Attestation is meaningful because the process is repeatable and therefore checkable.

An agent is not a derivation. Run it twice on the same ticket and you get two different diffs, both possibly correct. So the strongest claim available collapses from:

> "this artefact is the correct output of this process applied to these inputs"

to:

> "this diff was produced by this process at this time, and a named human accepted it"

That is a materially weaker guarantee, and pretending otherwise would be dishonest to an accreditor. The practical consequence is that **the accountable-acceptance step stops being quality assurance and becomes the integrity boundary.** In a classical factory, review catches mistakes while the provenance chain carries the integrity guarantee. In an AI-heavy factory, review is the only place where a non-deterministic process is converted into an accountable assertion.

This is uncomfortable, because the research also established that **human review is not a reliable detection control** — GlassWorm's Unicode variation selectors are invisible in every diff view, and an infected extension reached Microsoft's own marketplace. So the integrity boundary now rests on a control that demonstrably fails against adversarial input.

The resolution is to split the two jobs explicitly and stop conflating them:

- **Machines detect.** Unicode normalisation, invisible-character detection, licence and snippet scanning, reachability analysis, test execution, policy evaluation. All mechanical, all attestable.
- **Humans are accountable.** A named person in the DCO chain asserts they understand and will defend the change. The Linux kernel got this exactly right: *"You are expected to understand and to be able to defend everything you submit"*, and agents must not add `Signed-off-by` because only a human can certify the DCO.

Neither substitutes for the other, and the attestation at that boundary should record **both** — what was checked mechanically, and who accepted the residue.

## 2. The economics invert, and that reorients the whole factory

Classically the expensive steps were build and test, and review was comparatively cheap. If agents generate change far faster than humans can review it, that reverses: generation becomes cheap and **review becomes the scarce resource**.

Everything follows from that. A factory optimised for AI-generated change is **a factory optimised for review throughput**, not build speed. Which means:

- The highest-value output of the factory is no longer the artefact. It is **the evidence that makes a change cheap to review** — a blast-radius analysis, a reachability verdict, a passing test suite that actually covers the diff, a statement that this change touches nothing else.
- Gates must have brutally low false-positive rates, because a reviewer drowning in findings approves blind. The research found that CPE false positives are the dominant cause of unusable gates, and that fixing the base image *removes* findings rather than suppressing them. That is no longer a hygiene preference; it is load-bearing, because a gate that gets switched off has zero value and a gate that exhausts reviewers has negative value.
- The factory should attest what it checked mechanically **so the human reviews only what is left.** That is the single most useful thing it can do for throughput.

This is a genuine reorientation. It does not change the primitives, but it changes which outputs matter, and therefore where to spend effort.

## 3. The evidence graph is also the agent's context substrate

This is the one I think is non-obvious and most important.

Every piece of evidence the factory produces today — SBOMs, provenance, scan results, VEX, test results, OSCAL — is produced *for humans and auditors*, and the research establishes with some force that almost nobody reads it. Iron Bank ships the artefact to the high side and routes the evidence to a different bucket. Big Bang's OSCAL component definition has been stale for three and a half years. The thesis so far has been that **evidence rots because nothing fails when it does.**

Put an agent in the loop and that changes, because the agent *wants* this data:

- An agent fixing a CVE needs the SBOM, the reachability analysis and the VEX history to decide whether the finding is real.
- An agent proposing a dependency bump needs the provenance of what it is bumping to.
- An agent writing a control narrative needs the running system's actual configuration, not a document from 2022.
- An agent triaging a failure needs the test-result and scan attestations for the last known-good build.

So the factory's evidence graph becomes **machine-consumable context in the hot path**. Which gives a sharper diagnosis than the one I had: evidence rots not because nothing fails when it rots, but because **nothing reads it**. Give it a reader with an appetite and the freshness problem partly solves itself, because stale context produces visibly worse agent output.

Two architectural consequences:

- **Evidence must be queryable, not merely attached.** OCI referrers answer "what is attached to this digest". They cannot answer "which images contain this purl", "what was built from this commit", "which artefacts does this new CVE affect". Those are graph questions, and they are exactly the questions an agent asks. This upgrades the graph store from a nice-to-have to a core component — and makes Archivista's insight (in-toto `subject`s are graph edges, so you traverse from a commit to everything built from it) more interesting than GUAC's heavier ambition, given GUAC's recommended backend is still non-persistent in-memory.
- **Evidence freshness becomes measurable through use.** If an agent's context includes the provenance of what it is modifying, a stale or missing attestation degrades a visible output rather than lurking until accreditation.

I think this is the strongest argument for the project, and it is a *better* argument than the air-gap one because it applies to every customer rather than only the ones with diodes. The air-gap case remains the sharpest demonstration; this is the general case.

## 4. The primitives hold — and the human boundary turns out to be the same pattern

Testing deep AI integration against the existing model:

| Primitive | Verdict |
|---|---|
| **Digest-bound statement** | Holds unchanged. An AI-authorship predicate is just another `predicateType` over a diff digest. An eval-result predicate fits the same way. |
| **Delegated verdict** | Holds, and becomes more important — see below. |
| **Capability descriptor** | Holds, and becomes central rather than peripheral. |

I briefly thought accountable human acceptance was a fourth primitive. It is not: **it is the delegated verdict applied at the human boundary.** A party performs a verification that downstream cannot repeat, and signs a cheap assertion that downstream trusts instead. That is precisely the VSA pattern and precisely the trusted-importer pattern. The human reviewer is a third instance of the same shape, with the same two safety rules — record what policy was in force, and never let the producer also be the verifier.

That is a satisfying result, because it means one mechanism covers the gate, the cross-domain importer and the human reviewer. One implementation, one audit format, one honest sentence about where trust delegates.

The capability descriptor earns its promotion for a specific reason: if agent capability varies by tier, then **task granularity and review policy must vary with it too.** A GPU-poor enclave at roughly half of frontier capability should not merely have "autonomous multi-file change" disabled; it should decompose work into smaller units and apply *more* human scrutiny per change. That makes the descriptor an input to the review policy, not just a feature flag — and it makes degradation a declared, gate-enforced property rather than observed flakiness.

---

## 5. The provenance fork for spec-driven development

If the spec becomes the source of truth and code is generated from it, what gets attested? Two options:

**Option A — attest the spec, treat code as a build output.** Intellectually cleaner and matches how we treat compiled artefacts. It requires generation to be reproducible, which with a hosted frontier model it is not.

**Option B — keep attesting the commit; record the spec, prompts, model identity and eval results as *inputs*.** The spec goes in `resolvedDependencies` exactly like a lock file. Generated code is committed and reviewed, so transition A still carries accountability.

**Option B, clearly, for now.** It preserves the existing architecture entirely, costs almost nothing, and keeps a human in the DCO chain, which no regime currently lets you avoid.

**Revision:** the research weakened this section's speculation considerably, and in an interesting way. A pre-registered study found that the *uncited* generation condition is significantly **more** deterministic (d ≈ −0.72 to −0.76), while **only** the cited condition enables hallucination detection (86–88% versus 0%). So **verifiability and determinism trade off structurally** — you cannot have both, and the more reproducible configuration is the less checkable one. That makes Option A less attractive than I thought even where it is achievable, and it argues for a different move entirely: a **deterministic citation-resolution check** at verify time, which gets 86–88% hallucination detection at a 0% false-positive rate with no model in the verification path. Take that over chasing reproducible generation.

One counterintuitive point still worth holding onto, though, now as speculation rather than a plan: **the air-gapped case is where Option A first becomes feasible.** Reproducible generation needs pinned weights, a pinned harness, a pinned prompt and temperature zero — and an air-gapped enclave with fixed local weights is the one environment where all four are natural. Deterministic code generation, with the generation itself attestable as a derivation, is more achievable on the high side than in the cloud. If that holds up it is a surprising inversion of the usual "the high side is the degraded tier" story, and it needs testing rather than believing.

---

## 6. What this means for the build list

Revised after the research. **Build:**

1. **The AI-authorship predicate**, carrying harness, model identity and licence, tier, the capability-descriptor digest, the spec and context-file digests — and, per the GitInject finding that the critical vulnerabilities in agent harnesses are structural rather than model-behavioural (CI credential and config handling, with all four major providers vulnerable by default), **the credential and egress posture the agent ran under.**
2. **An eval-result attestation — by extending the already-registered `test-result/v0.1`**, not by minting a type. Reportedly about a day's work and the best value-for-effort item on the list, because it makes a model or harness swap gate-able like any other dependency change instead of landing silently.
3. **An attested agent-run record**, extending the registered `runtime-trace/v0.1` and sourced from durable workflow history **captured outside the agent's reach**. Nothing does this today, and it is what makes an agent run auditable rather than merely logged.
4. **The queryable evidence graph**, first-class, because it is the agent's context substrate as well as the auditor's record. The Sonatype telemetry is the empirical case: 27.76% of real upgrade recommendations referenced non-existent versions, which is what ungrounded generation looks like at scale.
5. **Three-valued reachability with a degeneracy detector.** 52.9% of 78,000 real SBOMs declare no dependency edges at all, and detecting that degenerate case moved KEV recall from 0.600 to 0.950. Cheap, mechanical, large effect.

**Port rather than build:** `openvex/vexflow` already produces Sigstore-signed in-toto OpenVEX attestations from a maintainer's one-line comment, authorised via OWNERS. It is GitHub-coupled through pluggable `api.Scanner` / `api.VexPublisher` interfaces, so an air-gapped-forge adapter is bounded work against a designed seam. This removes the signed-VEX predicate from the build list entirely.

**Adopt:** `Inspect` (MIT, UK AISI) for evals — local providers, sandboxing, and an `EvalLog` with a header/sample split that is straightforward to sign. `Temporal` (MIT) or `Dapr Agents` (Apache-2.0, CNCF, where every MCP tool call is already a durably recorded child workflow) for durable agent runs — explicitly **not** Restate (BSL) or Inngest (SSPL). `OpenRewrite` for mechanical refactoring, which is deterministic, reproducible, offline and **strictly better than a model wherever a recipe exists**. `complyctl` plus Gemara, which pulls policy **from an OCI registry** — the same transport shape as the transfer envelope.

And one reframing of an existing item: **continuously generated OSCAL stops being a compliance nicety and becomes an instance of the general rule that evidence should have a machine reader.** The research sharpens why this is ours to own: **Lula 1 (observed-state to OSCAL) is now in maintenance mode, replaced by an eMASS spreadsheet importer.** Taken with Big Bang's three-and-a-half-year-stale component definition, the ecosystem is drifting *back* towards documents. We will own this capability, not consume it.

And one reframing of an existing item: **continuously generated OSCAL stops being a compliance nicety and becomes an instance of the general rule that evidence should have a machine reader.** If nothing reads it, it rots; the cure is a reader, and the reader is increasingly an agent.

## 7. What I am least sure about

- Whether agent-driven volume genuinely overwhelms review in practice, or whether it plateaus because reviewers reject low-quality change and the loop self-limits. The economics argument in §2 depends on this and I have no data. Flagged for the research.
- Whether the queryable-graph claim survives contact with how agents actually consume context — it may be that a repository map plus targeted search beats a formal evidence graph, which is what the GPU-poor context-budget finding would suggest.
- Whether anyone treats an agent run as a durable, replayable, attestable workflow today, or whether that is all still chat-shaped. Asked.
- The reproducible-generation claim in §5 is mine and untested.
