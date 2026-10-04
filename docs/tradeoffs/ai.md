# AI: Capability vs Provability

## Where AI breaks the determinism that provenance assumes

The whole supply-chain integrity model assumes a **derivation**. Provenance says *this builder, with these parameters, produced this digest*. Reproducible builds are the gold standard because a third party can re-run the derivation and compare.

An agent breaks that assumption. Run it twice on the same ticket and you get two different diffs, both possibly correct. So the strongest available claim collapses from:

> "this artefact is the correct output of this process applied to these inputs"

to:

> "this diff was produced by this process at this time, and a named human accepted it"

### The human boundary becomes load-bearing

In a conventional factory, review catches mistakes while the provenance chain carries the integrity guarantee. Under heavy AI authorship it's the only place a non-deterministic process becomes an accountable assertion.

Review doesn't hold up against adversarial content. A real worm used Unicode variation selectors that render as blank lines -- editors, diffs and most static analysis show nothing at all, while the interpreter executes them -- and reached a major marketplace.

!!! success "Split the two jobs"
    **Machines detect.** Unicode normalisation, invisible-character detection, licence scanning, reachability, tests, policy.

    **Humans are accountable.** A named person asserts they understand the change and will defend it. Only a human can certify the Developer Certificate of Origin. An agent must never sign off on its own work.

The author-to-source-of-record hand-off is the one step in the architecture with no signed artefact anywhere in open source. Everything I've looked at either configures review rules or reports on them; nothing signs "policy X was met for commit Y".

## Verifiability and determinism trade off against each other

Pin the weights, pin the prompt, set temperature to zero, and generation starts to look like a derivation again, with strong provenance available behind it. An air-gapped enclave with fixed local weights is about the only setting where all of that comes naturally.

A pre-registered study prices that configuration. The **uncited** generation condition is significantly *more* deterministic (d ≈ −0.72 to −0.76), while **only** the cited condition enables hallucination detection -- **86-88% versus 0%**. One study, so the effect size wants replicating.

So spend the determinism at verify time instead. The deterministic **citation-resolution check** earns 86-88% hallucination detection at a 0% false-positive rate, with **no model in the verification path**.

### Where that leaves the provenance fork

If a specification becomes the source of truth and code is generated from it, what gets attested?

| Option | Assessment |
|---|---|
| Attest the specification, treat code as a build output | Cleaner in principle. Requires reproducible generation, which per above is the less verifiable configuration. |
| **Attest the commit; record the specification, prompts, model identity and evaluation results as *inputs*** | **The one to take.** The specification goes in the resolved-dependencies list exactly like a lock file. Code is committed and reviewed, so a human stays in the accountability chain -- which no regime surveyed lets you avoid. |

## Capability by deployment tier

Capability tracks the size of the GPU estate more than anything else:

| Tier | Capability vs frontier |
|---|---|
| Government cloud with managed models | Near parity -- the penalty falls on operations |
| Enclave, ~8 high-end GPUs | **~95-100%** on contamination-controlled bug fixing |
| Enclave, 1-2 GPUs | **48-60%** |

On the one contamination-controlled independent leaderboard available, an open-weight model placed **fourth of seventeen at 62.9% against a 64.5% leader**, within overlapping error bars, with the highest pass-at-any score on the board, at **a third of the cost**. Permissively licensed weights exist at every size band that matters.

!!! info "The inversion"
    The patterns that survive without frontier models are the same set that has deterministic verifiers -- which is the same set you can attest.

    Survives: false-positive triage of scanner findings, validated test generation behind a filter chain, mechanical refactoring from recipes, local evaluation harnesses, agent sandboxing.

    Dies: agentic review as a gate, autonomous multi-file remediation, VEX justification selection, multi-agent planning.

## Generator proposes, verifier decides

Where AI earns its keep today: a non-deterministic generator proposes; a deterministic verifier decides.

That changes what a verdict has to record:

- the verdict must carry the **model identity and capability-descriptor digest**, so a model swap invalidates prior verdicts exactly as a policy change does
- the capability descriptor must carry **measured** capability -- last night's signed evaluation score, with every entry traceable to a run that produced a number

## What is real and what is vapour

| Capability | Status |
|---|---|
| False-positive triage of static-analysis findings | **Real.** F1 0.91-0.96; one deployment eliminated 94-98% at <$0.12/alarm |
| Agent-authored diffs and pull requests | **Real.** 33,000 measured -- documentation, CI and build changes merge well; performance work and bug fixes badly |
| Mechanical refactoring | **Real, and it is plain tooling.** Recipe-based tools are deterministic, reproducible, offline -- strictly better than a model where a recipe exists |
| Validated test generation | **Real, but only behind a filter chain** -- 75% build / 57% pass / 25% coverage gain means roughly **3 in 4 discarded** |
| Exploitability assessment | **Emerging.** ~80% F1 binary, but **under 70%** on selecting the justification |
| AI code review as a **gate** | **Vapour.** 56.3% of comments rejected in the wild, and nothing available emits a signed verdict |
| `AGENTS.md` as a performance lever | **Vapour.** Two studies find no correctness gain and >20% cost increase. Keep it for *constraints* alone |
| LLM inside the policy gate | **Vapour, and architecturally wrong.** The gate must be deterministic |
| AI in admission control | **Never.** |

## The attack surface you take on

The factory's agent has all three legs of the exfiltration trifecta **by default**: access to private data (source, secrets, tickets), exposure to untrusted content (dependency source, issue text, tool output), and the ability to communicate externally.

The fix belongs in the architecture, at a layer below the prompt. The rules:

- **the agent never holds a push credential** -- it proposes, a separate non-model process acts after a gate
- **tool output is untrusted input** -- it may never alter the agent's permissions, tool list or instructions
- **no dynamic tool loading** -- pin the tool set per task
- **keep agents as leaves** -- no delegation chains, because they launder attribution, and in the setups I've taken apart the "independent" verifiers collapse to very few genuinely distinct domains

In the published agent-harness work, the critical vulnerabilities are **structural** -- credential and configuration handling in CI, with all four major providers vulnerable by default. If that generalises, the security effort belongs in the plumbing and not in prompt hardening. So record the credential and egress posture the agent ran under, in the authorship attestation.

## What the twelve regimes surveyed require

Across the twelve regimes surveyed -- US federal, UK MOD, EU CRA, DORA, FDA, automotive, aviation, rail and industrial among them -- **none imposes requirements on AI-generated code in assured software.**

The regulatory position moves quickly and the survey is a snapshot, so it wants a dedicated pass before anyone quotes it in front of a regulator.

What the regimes do say attaches to outcomes -- tested, reviewed, provenanced, vulnerability-managed -- regardless of authorship. So a factory producing the same evidence whoever wrote the code should already be aligned.

The forward risk runs one way, though: if a future rule *does* require authorship disclosure, a factory that recorded nothing can't retrofit it. Recording model identity per diff is cheap now.

Two questions for whoever owns this:

1. Is anyone in your chain willing to put their name on an agent-authored diff
2. Is what you're recording today enough to answer an authorship question asked in 2028
