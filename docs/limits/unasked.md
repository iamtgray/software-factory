# Open questions

Each one is either a decision you take before you build or a risk you price before you fund. Most are about money and organisation.

---

## Who's the buyer, and who pays for whom?

Nothing in the material names a design partner, first customer or beachhead.

The programme office holds the money and wants an authorisation. "Stale provenance is a build failure" imposes a new cost on exactly that party, for a benefit that lands on an assessor, a future maintainer, or the taxpayer.

So who are you billing, and what do they get inside the same financial year? The first software factory, in 1978, was diagnosed at the time as failing because *"middle management were not required by top management to use the Software Factory, leading to a decline in the flow of work."*

## Product, or consulting engagement?

Nothing I've read says who runs the factory in a customer environment, who's on call for it, or who funds its second year. A **product** needs upgrade paths, multi-tenancy and a support boundary; an **engagement** needs none of them and shouldn't pay for them. I can't see how you defer the choice and build both.

!!! danger "Funding model"
    Funding and staffing mismatch is on the record from the first commander of the most-cited modern factory.

    RAND finds current defence software factories are mostly **customer-funded**, which encodes the 1978 failure straight into the budget line: optional adoption, then a decline in the flow of work.

    Across the sources, funding ranks first among failure modes and measurement second.

## What does the GPU estate cost?

The factory is sized in CPU, RAM and disk. There's no figure per enclave, per tenant, per year, and nothing at all for the **GPU estate**, which is plausibly larger than everything else combined and scales per enclave.

The claim that an enclave with eight high-end GPUs gets near-frontier capability is well evidenced technically and never priced.

## Which signing algorithm does the customer mandate?

Worth establishing before the first signature is issued, because the signatures outlive the decision. CNSA and CNSSP-15 are where a mandate would live, SP 800-208 covers the hash-based schemes (LMS and XMSS), and crypto-agility is the claim you'd need afterwards.

Set that against what the design says about its own first primitive:

!!! quote
    "non-negotiable and the one choice that is catastrophic to reverse -- every signature ever issued is over that encoding."

Does the target customer mandate an algorithm or a migration path, and has anybody asked them?

## Restoring from backup resets the anti-rollback defence

A correctness defect, and it only shows up from reading the transfer design and the operations design together.

The transfer design makes the receiver's **monotonic sequence high-water mark** the only defence against rollback and omission. Restore the high side from backup and the high-water mark goes back with it, and nothing in the design protects it. An attacker who can trigger or wait for a restore then replays an older, validly-signed bundle, and every cryptographic check passes.

!!! warning "The fix"
    The high-water mark needs its own integrity and restore semantics, ahead of the first implementation.

## `failurePolicy: Ignore` turns the gate off for you

There's no policy test, no attestation-coverage measure and no stated fail-closed behaviour.

`failurePolicy: Ignore` means the admission gate everything depends on is bypassed whenever the webhook is unavailable.

A gate somebody switched off deliberately is worth less than no gate at all, because everyone downstream carries on trusting it. One that switches *itself* off under load is worse: nobody is told it happened.

## Can two tenants share a cluster?

The interface is custom resources plus an admission webhook. If two projects share a cluster, I don't see how they hold different slot versions or different gate policies enforced by separate webhooks, and a tenant able to edit a custom resource may be able to weaken its own gate.

The October 2024 document carries the strongest language of any version (a hard *"It must be designed for multi-tenancy"*), and no version carries a test that would demonstrate the isolation holds.

## Does the name survive either market?

"Software factory" returns **one GOV.UK hit** (an employment tribunal) against 321 for "secure by design". One search on one government domain, so treat it as an indicator. In the civilian material I've read it's platform engineering, and where "factory" turns up it's usually the pejorative.

No decision is recorded anywhere to rename it, drop the term, or keep it on purpose.

## Do swappable slots survive the reuse step function?

Toshiba's reuse step function is the most prescriptive number in the sources: reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.**

A slot abstraction built so each environment picks a different implementation sits in the band where shared assets are worthless or harmful -- unless the *contract* is what gets reused unchanged while implementations vary beneath it. That reading isn't stated against the Toshiba finding anywhere, and it's only been validated against the easiest case.

---

Who pays, what it costs, who runs it, what it's called -- none of it is settled. Which of those would you want answered before the money moves, and who do you have to go and ask?
