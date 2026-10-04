# Open Questions

The formats, mechanisms and failure history feel settled enough to me now. What's left is the set of things I can't answer from here, and each one is either a decision you have to take before you build or a risk you have to price before you fund.

They look cheap to settle now and expensive to discover later. Most of them turn out to be about money and organisation, which surprised me.

---

## Who's the buyer, and who pays for whom?

I haven't found a named design partner, first customer or beachhead anywhere in the material. What specifies the product is a gap in the artefacts, and a programme can live with that for a while. The money is where it bites: **the central thesis is adversarial to the one party that looks like it holds a budget.**

The programme office holds the money and wants an authorisation. "Stale provenance is a build failure" imposes a new cost on exactly that party, for a benefit that lands on an assessor, a future maintainer, or the taxpayer.

So who are you billing, and what do they get inside the same financial year? The cost of ducking that is on the record. The first software factory, in 1978, was diagnosed at the time as failing because *"middle management were not required by top management to use the Software Factory, leading to a decline in the flow of work."*

## Product, or consulting engagement?

Nothing I've read says who runs the factory in a customer environment, who's on call for it, or who funds its second year. That one comes first, because I think the answer picks the architecture.

A **product** needs upgrade paths, multi-tenancy and a support boundary; an **engagement** needs none of them and shouldn't pay for them. I can't see how you defer the choice and build both.

!!! danger "The variable I'd watch hardest"
    The best-evidenced failure mode I've found in the field is funding and staffing mismatch, and it's on the record from the first commander of the most-cited modern factory.

    RAND finds current defence software factories are mostly **customer-funded**, which as I read it encodes the 1978 failure straight into the budget line: optional adoption, then a decline in the flow of work.

    Across the sources I've got, funding ranks first among failure modes and measurement second. An architecture that answers neither is a well-evidenced set of warnings that has informed no decision.

## What does the GPU estate cost?

The factory is sized in CPU, RAM and disk. I can't find a figure per enclave, per tenant, per year, and nothing at all for the **GPU estate** -- which is plausibly larger than everything else combined and scales per enclave.

The claim that an enclave with eight high-end GPUs gets near-frontier capability looks well evidenced technically and unpriced in everything I've read. Until someone writes the number down, the AI economics rest on a figure I don't have.

## Which signing algorithm does the customer mandate?

Worth establishing before the first signature is issued, because the signatures outlive the decision. CNSA and CNSSP-15 are where a mandate would live, SP 800-208 covers the hash-based schemes (LMS and XMSS), and crypto-agility is the property you'd want to be able to claim afterwards.

Set that against what the design says about its own first primitive:

!!! quote
    "non-negotiable and the one choice that is catastrophic to reverse — every signature ever issued is over that encoding."

A project about to start issuing long-lived signatures for defence customers has a gap exactly where it has declared reversal impossible. So does the target customer mandate an algorithm or a migration path, and has anybody asked them?

## Restoring from backup resets the anti-rollback defence

This one looks like a correctness defect to me, and it only showed up from reading the transfer design and the operations design together. Neither is wrong on its own.

The transfer design makes the receiver's **monotonic sequence high-water mark** the only defence against rollback and omission, and I can't see what else a one-way boundary gives you.

**Restore the high side from backup and the high-water mark goes back with it**, unless something protects it that I haven't found. An attacker who can trigger or wait for a restore can then replay an older, validly-signed bundle, and every cryptographic check passes.

!!! warning "The fix looks cheap"
    The high-water mark needs its own integrity and restore semantics. The work looks small from here, and it belongs in the design ahead of the first implementation. Learning it from an incident costs considerably more.

## `failurePolicy: Ignore` turns the gate off for you

I can't find a policy test, an attestation-coverage measure, or any stated fail-closed behaviour. The one that worries me is `failurePolicy`.

**`failurePolicy: Ignore` means the admission gate everything depends on is bypassed whenever the webhook is unavailable.** The architecture routes its guarantees through one cheap check at deployment time, and nothing I've read specifies the behaviour when that check can't run.

A gate somebody switched off deliberately is already worth less than no gate at all, because everyone downstream carries on trusting it. A gate that switches *itself* off under load is worse again: nobody is even told it happened.

## Can two tenants share a cluster?

The interface is custom resources plus an admission webhook. If two projects share a cluster, I don't see how they hold different slot versions or different gate policies enforced by separate webhooks, and a tenant able to edit a custom resource may be able to weaken its own gate.

That decides the cost model and the gate-integrity story together.

The October 2024 document carries the strongest language of any version (a hard *"It must be designed for multi-tenancy"*) and **I can't find a test in any version that would demonstrate the isolation holds.** So it's a mandated design property with no acceptance criterion attached, and anyone claiming to have met it is self-certifying against nothing.

## Does the name survive either market?

"Software factory" returns **one GOV.UK hit** (an employment tribunal) against 321 for "secure by design". That's one search on one government domain, so treat it as an indicator. In the civilian material I've read it's platform engineering, and where "factory" turns up it's usually the pejorative.

I can't see a decision recorded anywhere to rename, drop the term, or keep it on purpose. My read is that the name is a liability in both markets the thing is aimed at. Is that a cost you're happy to carry?

## Do swappable slots survive the reuse step function?

The most prescriptive number I've found is Toshiba's reuse step function: reuse **pays above 80% unchanged, does nothing between 20% and 80%, and is net harmful below 20%.**

A slot abstraction built so each environment picks a different implementation is, on the face of it, sitting in the band where shared assets are worthless or harmful -- unless the *contract* is what gets reused unchanged while implementations vary beneath it. I think that's the defensible reading, and I think it's what the design intends. It isn't stated against the Toshiba finding anywhere I've found, and it's only been validated against the easiest case.

---

Who pays, what it costs, who runs it, what it's called -- none of that is settled, and a probably-correct mechanism does nothing for any of it. Which of them would you want answered before the money moves, and who do you have to go and ask?
