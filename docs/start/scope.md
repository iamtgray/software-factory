# Scope -- What This Is Not

The most consequential decision in designing a factory, and it is about scope rather than technology.

## The risk that forces it

SEI's *Framework for Software Product Line Practice* contains a 28-section catalogue of failure modes (one "Practice Risks" section per practice area). It's embedded in the framework rather than published separately, which is why keyword searches miss it entirely.

Its scoping risk is aimed precisely at anything calling itself a software factory:

!!! quote "SEI, on scoping a product line"
    "The major risk associated with product line scoping is that the wrong set of products will be targeted."

    Too broad: "If it encompasses product members that vary too widely, the core assets will be strained beyond their ability to accommodate the variability; economies of production will be lost; and **the product line will collapse into an old-style, one-at-a-time product development effort**."

    Too narrow: "New product opportunities will either be rejected as being out of scope or be accepted but then result in too much rework. The product line will stagnate."

Both directions are fatal, in opposite ways. And "modular slots that work identically in a hyperscale cloud and a GPU-poor disconnected enclave" is exactly the kind of ambition that gets strained beyond its ability to accommodate variability.

## The answer: three layers, three different disciplines

| Layer | Framing | Discipline |
|---|---|---|
| **Assurance substrate** | **Platform** | Mandatory, minimal, consumed verbatim. No forking. Uniformity here is real. |
| **Accredited deployment patterns** | **Genuine product line** | A bounded family. Model commonality and variability properly, in the SEI sense. |
| **Application architecture** | **Explicitly out of scope** | Where two previous attempts died. Do not go here. |

So when this site says "swappable slots", it means **swappability in the substrate and the patterns**. Never in how an application is built.

### Why the third row is non-negotiable

Both historical failures died in that layer.

**SDC (1975--78)** -- the first organisation to build and trademark "The Software Factory", roughly 200 programmers centralised in Santa Monica. Cusumano's diagnosis puts **too much product variety** first, ahead of everything else.

**Microsoft Software Factories (2003--08)** -- model-driven development and domain-specific languages, aiming to generate applications from models. Faded.

A factory that tries to standardise *how applications are built* is attempting the thing that has failed every time it's been tried. A factory that standardises *how evidence about applications is produced* is attempting something narrower that nobody has finished.

## The measurement rule that enforces it

Toshiba's own productivity data gives the sharpest available test, and it's a step function rather than a gradient:

!!! danger "Reuse pays above 80% unchanged. It does nothing between 20% and 80%. **Below 20% it is net harmful.**"

So there's a concrete metric for whether the scope is right: **track the modification rate of shared assets.** A slot implementation that every programme forks by 40% is worse than having no shared asset at all -- you're paying the coordination cost of a shared component and getting none of the benefit.

Toshiba also hit a practical reuse ceiling of about 50%, and their productivity curve went +22% in year one, +70% by year five, then **+8% across the next four**. Plan for the plateau.

## What "out of scope" means in practice

Things the factory **does** own:

- producing, signing and binding evidence
- gating on that evidence, unbypassably
- carrying evidence across boundaries
- declaring what each slot implementation can and cannot do
- measuring its own delivery outcomes

Things it **does not** own:

- how you structure your application
- which language or framework you use
- your domain model, your API design, your database schema
- whether you use microservices
- your team structure

!!! tip "The test"
    If a proposed feature would make two different applications more similar to each other, it's probably out of scope. If it would make two different applications' *evidence* more similar, it's in scope.

## The thing to say out loud

There's an irony worth owning before someone else raises it.

SDC's model *"was an important influence on the software standards later developed by the U.S. Department of Defense"* -- the heavyweight, documentation-driven DOD-STD-2167 lineage. And SEI's director sat on the 2018 Defense Science Board task force that put "software factory" back into DoD policy.

**The DoD coined the term, built the heavyweight standards regime out of it, and then re-adopted the same word to escape that regime.**

Say it first, with amusement. Much better position than being caught by it.

---

**Next:** [The Five Primitives](../how/primitives.md) -- the mechanism, now that the boundaries are drawn.
