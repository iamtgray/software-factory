# What Nobody Asked

Three independent critics were pointed at the research programme and asked what was missing. Their verdict was consistent: the work is unusually strong on formats, mechanisms and failure history, and close to silent on **running the thing and selling it**.

This page is their findings. It is the least comfortable page here and probably the most useful, because every item on it is cheap to fix now and expensive to discover later.

---

## There is no buyer

Across roughly 16,000 lines of research and design, there are **zero occurrences** of "design partner", "first customer", "target customer", "beachhead" or "pilot customer". Verified by search.

The product is specified by a gap in the artefact landscape rather than by anyone's purchasing decision. That alone is survivable. The sharper problem is that **the central thesis is adversarial to the only party with a budget.**

The programme office holds the money and wants an authorisation. "Stale provenance is a build failure" imposes a new cost on exactly that party, in exchange for a benefit that accrues to an assessor, a future maintainer, or the taxpayer. Nobody has worked out how to sell that, and the history on this site says what happens when you don't: the first software factory, in 1978, failed because *"middle management were not required by top management to use the Software Factory, leading to a decline in the flow of work."*

## There is no operating model

Nobody has established who runs the factory in a customer environment, who is on call for it, or who funds its second year.

This is not an implementation detail. It decides whether the thing is a **product** or a **consulting engagement**, and those have different architectures: a product needs upgrade paths, multi-tenancy and a support boundary, while an engagement needs none of them and should not pay for them.

It is also, by the project's own evidence, the variable that decides the outcome. The best-evidenced failure mode in the entire research corpus is funding and staffing mismatch, on the record from the first commander of the most-cited modern factory. And RAND finds current defence software factories are mostly **customer-funded**, which encodes the 1978 failure directly into the budget line.

!!! danger "The design documents contain no response to this"
    Keyword counts across both design documents: **zero** for funding, operator, operate, turnover, on-call, or day-two.

    The research ranked funding first and measurement second among failure modes. The architecture answers neither. It is an unusually well-evidenced set of warnings that has informed no decision.

## There is no cost model in money

The factory is sized in CPU, RAM and disk. There is no figure per enclave, per tenant, per year — and in particular **no price for the GPU estate**, which is plausibly larger than everything else combined and scales per enclave.

Which means the AI position's economics rest on a number nobody has written down. The claim that an enclave with eight high-end GPUs gets near-frontier capability is well evidenced technically and completely unpriced commercially.

## The signing algorithm question was never asked

**Zero mentions of CNSA, CNSSP-15, SP 800-208, LMS, XMSS or crypto-agility anywhere in the research.**

Set that against what the design says about its own first primitive: *"non-negotiable and the one choice that is catastrophic to reverse — every signature ever issued is over that encoding."*

A project about to start issuing long-lived signatures for defence customers, which has not asked whether those customers mandate particular algorithms or a post-quantum migration path, has a gap precisely where it has declared reversal impossible. This is the clearest instance on the site of the research being deep on the mechanism and silent on the requirement.

## Backup and restore silently defeat the flagship guarantee

This one is a correctness defect rather than a coverage gap, and it emerges only from reading two documents together.

The transfer design makes the receiver's **monotonic sequence high-water mark** the only defence against rollback and omission, because a one-way boundary offers nothing else. Nobody asked what happens when the high side is restored from backup.

Restoring resets the high-water mark. An attacker who can trigger or wait for a restore can then replay an older, validly-signed bundle, and every cryptographic check passes.

!!! warning "The fix is cheap; not having noticed is the problem"
    The high-water mark must be treated as security state with its own integrity and restore semantics, not as cache. That is a small amount of work and it needs to be in the design before the first implementation, not after the first incident.

## Nobody asked how the factory tests itself

Four specific absences, and no hits anywhere for "policy test", "attestation coverage", "fail-closed" or `failurePolicy`.

The last is the consequential one. **`failurePolicy: Ignore` means the admission gate everything depends on is bypassed whenever the webhook is unavailable.** The entire architecture routes its guarantees through one cheap check at deployment time, and nobody has specified what happens when that check cannot run.

Given this site argues that a gate which gets switched off is worth less than no gate, a gate that switches *itself* off under load deserved an answer.

## Multi-tenancy was never resolved

The interface is custom resources plus an admission webhook. If two projects share a cluster, they cannot hold different slot versions or different gate policies enforced by separate webhooks, and a tenant with the ability to edit a custom resource may be able to weaken its own gate.

That decides the cost model and the gate-integrity story simultaneously. Note also that a multi-tenancy isolation test was a stated **must** in the 2019 defence reference design and was quietly dropped in October 2024 — so the one regime that asked for it has stopped asking, which is not the same as it not mattering.

## The name is wrong and no decision has been taken

The evidence is decisive in both target markets. "Software factory" returns **one GOV.UK hit** — an employment tribunal — against 321 for "secure by design". The civilian world says platform engineering, and where "factory" appears it is usually the pejorative.

There are **zero hits** across the research for "rename", "drop the term" or "what to call it". The project has gathered conclusive evidence that its own name is a liability in both markets it is aimed at, and has not acted on it.

## And the swappable-slots ambition contradicts the project's own best finding

The most prescriptive number in the research is Toshiba's reuse step function: reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.**

A slot abstraction whose entire value proposition is that each environment picks a different implementation is, by construction, operating in the band where shared assets are worthless or harmful — unless the *contract* is what gets reused unchanged while implementations vary beneath it. That is the defensible reading, and it is the one the design intends. But it has never been stated against the Toshiba finding, and it has only been validated against the easiest case.

---

## How to read this page

None of it says the architecture is wrong. The critics were explicit that the research is strong and the mechanism is probably correct.

What it says is that **the mechanism was the easy part**, and that the project has repeatedly done the hard technical work while leaving the questions that actually kill programmes unasked. Which is itself an instance of the pattern this whole site is about: the things nobody checks are the things that rot.
