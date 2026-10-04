# Open Questions

The formats, mechanisms and failure history are settled. What follows is not: nine items, each of which is either a decision you have to take before you build, or a risk you have to price before you fund.

They are cheap to settle now and expensive to discover later. Most of them are not technical.

---

## Decide who the buyer is, and who pays for whom

There is no named design partner, first customer or beachhead. The product is specified by a gap in the artefact landscape rather than by anyone's purchasing decision. That alone is survivable. This is the sharper problem: **the central thesis is adversarial to the only party with a budget.**

The programme office holds the money and wants an authorisation. "Stale provenance is a build failure" imposes a new cost on exactly that party, in exchange for a benefit that accrues to an assessor, a future maintainer, or the taxpayer.

So decide who you are billing and what they get in the same financial year. The alternative is on the record. The first software factory, in 1978, failed because *"middle management were not required by top management to use the Software Factory, leading to a decline in the flow of work."*

## Decide whether this is a product or a consulting engagement

Nobody runs the factory in a customer environment, nobody is on call for it, and nobody funds its second year. Settle that first, because it is not an implementation detail — it chooses the architecture.

A **product** needs upgrade paths, multi-tenancy and a support boundary. An **engagement** needs none of them and should not pay for them. You cannot defer the choice and build both.

!!! danger "This is the variable that decides the outcome"
    The best-evidenced failure mode in the whole field is funding and staffing mismatch, on the record from the first commander of the most-cited modern factory.

    RAND finds current defence software factories are mostly **customer-funded**, which encodes the 1978 failure directly into the budget line: optional adoption, then a decline in the flow of work.

    Funding ranks first among failure modes and measurement second. An architecture that answers neither is a well-evidenced set of warnings that has informed no decision.

## Price the GPU estate before you believe the AI position

The factory is sized in CPU, RAM and disk. There is no figure per enclave, per tenant, per year — and in particular **no price for the GPU estate**, which is plausibly larger than everything else combined and scales per enclave.

The claim that an enclave with eight high-end GPUs gets near-frontier capability is well evidenced technically and completely unpriced commercially. Until someone writes the number down, the AI economics rest on an unknown.

## Decide the signing algorithm against the customer's mandate, not your preference

Before the first signature is issued, establish whether the target customers mandate particular algorithms or a post-quantum migration path. The relevant regimes are CNSA and CNSSP-15, the relevant standard is SP 800-208, the relevant primitives are LMS and XMSS, and the relevant property is crypto-agility.

Set that against what the design says about its own first primitive:

!!! quote
    "non-negotiable and the one choice that is catastrophic to reverse — every signature ever issued is over that encoding."

A project about to start issuing long-lived signatures for defence customers has a gap precisely where it has declared reversal impossible. Deep on the mechanism, silent on the requirement.

## Treat the high-water mark as security state, not cache

This one is a correctness defect rather than a decision, and it only emerges from reading the transfer design and the operations design together.

The transfer design makes the receiver's **monotonic sequence high-water mark** the only defence against rollback and omission, because a one-way boundary offers nothing else.

**Restoring the high side from backup resets the high-water mark.** An attacker who can trigger or wait for a restore can then replay an older, validly-signed bundle, and every cryptographic check passes.

!!! warning "The fix is cheap"
    The high-water mark needs its own integrity and restore semantics. That is a small amount of work, and it has to be in the design before the first implementation rather than after the first incident.

## Specify what happens when the admission gate cannot run

There is no policy test, no attestation-coverage measure, and no stated fail-closed behaviour. The consequential one is `failurePolicy`.

**`failurePolicy: Ignore` means the admission gate everything depends on is bypassed whenever the webhook is unavailable.** The entire architecture routes its guarantees through one cheap check at deployment time, and nothing specifies the behaviour when that check cannot run.

A gate that gets switched off is worth less than no gate. A gate that switches *itself* off under load is worse, because nobody is told.

## Resolve multi-tenancy, or accept the cost model it forces

The interface is custom resources plus an admission webhook. If two projects share a cluster, they cannot hold different slot versions or different gate policies enforced by separate webhooks, and a tenant able to edit a custom resource may be able to weaken its own gate.

That decides the cost model and the gate-integrity story simultaneously.

The October 2024 document carries the strongest language of any version — a hard *"It must be designed for multi-tenancy"* — and **no document in any version defines a test that would demonstrate the isolation holds.** So multi-tenancy is a mandated design property with no acceptance criterion attached, and anyone claiming to have met it is self-certifying against nothing.

## Take the naming decision

The evidence is decisive in both target markets. "Software factory" returns **one GOV.UK hit** — an employment tribunal — against 321 for "secure by design". The civilian world says platform engineering, and where "factory" appears it is usually the pejorative.

No decision has been taken to rename, drop the term, or keep it on purpose. The name is a liability in both markets the thing is aimed at, and that is a decision, not a research finding.

## Reconcile swappable slots with the reuse step function

The most prescriptive number in the evidence is Toshiba's reuse step function: reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.**

A slot abstraction whose entire value proposition is that each environment picks a different implementation is, by construction, operating in the band where shared assets are worthless or harmful — unless the *contract* is what gets reused unchanged while implementations vary beneath it. That is the defensible reading and the one the design intends. It has never been stated against the Toshiba finding, and it has only been validated against the easiest case.

---

None of this says the architecture is wrong; the mechanism is probably correct. It says the mechanism was the easy part, and the questions that actually kill programmes are still open.
