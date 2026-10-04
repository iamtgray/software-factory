# AI: Capability vs Provability

The capability you want and the provability you need pull in opposite directions, in three separate ways. All three have counterintuitive resolutions.

## 1. AI breaks the determinism that provenance assumes

The whole supply-chain integrity model assumes a **derivation**. Provenance says *this builder, with these parameters, produced this digest*. Reproducible builds are the gold standard because a third party can re-run the derivation and compare.

An agent isn't a derivation. Run it twice on the same ticket and you get two different diffs, both possibly correct. So the strongest available claim collapses from:

> "this artefact is the correct output of this process applied to these inputs"

to:

> "this diff was produced by this process at this time, and a named human accepted it"

That's a materially weaker guarantee, and pretending otherwise to an assessor would be dishonest.

### What follows: the human boundary becomes load-bearing

In a conventional factory, review catches mistakes while the provenance chain carries the integrity guarantee. Under heavy AI authorship, **review is the only place where a non-deterministic process becomes an accountable assertion.**

Which is awkward, because review demonstrably fails against adversarial content. A real worm used Unicode variation selectors that render as blank lines (invisible in editors, diffs and most static analysis, executable to the interpreter) and reached a major marketplace.

!!! success "Split the two jobs"
    **Machines detect.** Unicode normalisation, invisible-character detection, licence scanning, reachability, tests, policy.

    **Humans are accountable.** A named person asserts they understand the change and will defend it. Only a human can certify the Developer Certificate of Origin -- an agent may never sign off on its own work.

    Neither substitutes for the other. Record both.

There's an uncomfortable structural gap here. This transition (author to source of record) is **the only hand-off in the architecture with no signed artefact anywhere in open source.** Everything either configures review rules or reports on them. Nothing signs "policy X was met for commit Y".

## 2. Verifiability and determinism trade off against each other

The intuition is that making generation reproducible (pin the weights, pin the prompt, temperature zero) gets you back to a derivation, and therefore back to strong provenance. An air-gapped enclave with fixed local weights is the one place all of that is natural.

The evidence says the opposite. A pre-registered study found that the **uncited** generation condition is significantly *more* deterministic (d ≈ −0.72 to −0.76), while **only** the cited condition enables hallucination detection -- **86-88% versus 0%**.

You cannot have both: the more reproducible configuration is the **less checkable** one.

**So don't chase reproducible generation.** Take the deterministic **citation-resolution check** at verify time instead: 86-88% hallucination detection at a 0% false-positive rate, with **no model in the verification path at all**.

### The provenance fork this settles

If a specification becomes the source of truth and code is generated from it, what gets attested?

| Option | Assessment |
|---|---|
| Attest the specification, treat code as a build output | Cleaner in principle. Requires reproducible generation, which per above is the less verifiable configuration. |
| **Attest the commit; record the specification, prompts, model identity and evaluation results as *inputs*** | **Take this one.** The specification goes in the resolved-dependencies list exactly like a lock file. Code is committed and reviewed, so a human stays in the accountability chain -- which no regime currently lets you avoid. |

## 3. The air-gapped tier gets the better AI story

The usual framing is that a disconnected enclave is the degraded tier. For AI specifically, that's backwards.

The capability gap is now a hardware gap rather than a classification gap:

| Tier | Capability vs frontier |
|---|---|
| Government cloud with managed models | Near parity -- the penalty is operational, not capability |
| Enclave, ~8 high-end GPUs | **~95-100%** on contamination-controlled bug fixing |
| Enclave, 1-2 GPUs | **48-60%** |

On the one contamination-controlled independent leaderboard available, an open-weight model placed **fourth of seventeen at 62.9% against a 64.5% leader**, within overlapping error bars, with the highest pass-at-any score on the board, at **a third of the cost**. Permissively licensed weights are available at every size band that matters, which materially simplifies accreditation.

!!! info "The inversion"
    **What survives without frontier models is exactly the set of patterns that have deterministic verifiers -- which is exactly the set that is attestable.**

    Survives: false-positive triage of scanner findings, validated test generation behind a filter chain, mechanical refactoring from recipes, local evaluation harnesses, agent sandboxing.

    Dies: agentic review as a gate, autonomous multi-file remediation, VEX justification selection, multi-agent planning.

    Most of what dies is what a factory shouldn't have trusted anyway.

## The shape every working pattern shares

Across every stage where AI is genuinely useful today, one structure recurs:

A non-deterministic generator proposes; a deterministic verifier decides. So **AI validates the architecture rather than changing it** -- the delegated verdict was already the right pattern, and AI makes it mandatory rather than merely sensible.

Two additions this forces:

- the verdict must record the **model identity and capability-descriptor digest**, so a model swap invalidates prior verdicts exactly as a policy change does
- the capability descriptor must carry **measured** capability -- last night's signed evaluation score -- not a hand-maintained list of promises

## What is real, what is not

| Capability | Status |
|---|---|
| False-positive triage of static-analysis findings | **Real.** F1 0.91-0.96; one deployment eliminated 94-98% at <$0.12/alarm |
| Agent-authored diffs and pull requests | **Real.** 33,000 measured -- documentation, CI and build changes merge well; performance work and bug fixes badly |
| Mechanical refactoring | **Real, and not AI.** Recipe-based tools are deterministic, reproducible, offline -- strictly better than a model where a recipe exists |
| Validated test generation | **Real, but only behind a filter chain** -- 75% build / 57% pass / 25% coverage gain means roughly **3 in 4 discarded** |
| Exploitability assessment | **Emerging.** ~80% F1 binary, but **under 70%** on selecting the justification |
| AI code review as a **gate** | **Vapour.** 56.3% of comments rejected in the wild; nothing emits a signed verdict |
| `AGENTS.md` as a performance lever | **Vapour.** Two studies find no correctness gain and >20% cost increase. Keep it for *constraints*, not capability |
| LLM inside the policy gate | **Vapour, and architecturally wrong.** The gate must be deterministic |
| AI in admission control | **Never.** |

## The attack surface you take on

The factory's agent has all three legs of the exfiltration trifecta **by default**: access to private data (source, secrets, tickets), exposure to untrusted content (dependency source, issue text, tool output), and the ability to communicate externally.

This must be broken structurally, not by prompt engineering:

- **the agent never holds a push credential** -- it proposes, a separate non-model process acts after a gate
- **tool output is untrusted input** -- it may never alter the agent's permissions, tool list or instructions
- **no dynamic tool loading** -- pin the tool set per task
- **keep agents as leaves** -- no delegation chains, because they launder attribution and "independent" verifiers collapse to very few genuinely distinct domains

And one finding that redirects where to spend security effort: the critical vulnerabilities in agent harnesses are **structural rather than model-behavioural** -- credential and configuration handling in CI, with all four major providers vulnerable by default. So record the credential and egress posture the agent ran under, in the authorship attestation.

## No regulator has anything to say about this yet

Across the twelve regimes surveyed -- US federal, UK MOD, EU CRA, DORA, FDA, automotive, aviation, rail and industrial among them -- **none imposes requirements on AI-generated code in assured software.** That is a scoped finding, not a universal one: it is a survey of twelve, not a search of everything. The obligations attach to outcomes -- tested, reviewed, provenanced, vulnerability-managed -- regardless of authorship.

A factory producing the same evidence regardless of who wrote the code is therefore already aligned. The forward risk runs one way, though: if a future rule *does* require authorship disclosure, a factory that recorded nothing can't retrofit it. Recording model identity per diff is cheap now and impossible retrospectively.
