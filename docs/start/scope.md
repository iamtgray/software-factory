# Scope -- Three Layers, One Boundary

Where you draw the factory's boundary is the decision I'd worry about first. Get it wrong and nothing downstream rescues you.

## What forces the decision

SEI's *Framework for Software Product Line Practice* contains a 28-section catalogue of failure modes (one "Practice Risks" section per practice area). It lives inside the framework document itself, which is probably why keyword searches for it come up empty.

Its scoping risk reads like it was written for anything calling itself a software factory:

!!! quote "SEI, on scoping a product line"
    "The major risk associated with product line scoping is that the wrong set of products will be targeted."

    Too broad: "If it encompasses product members that vary too widely, the core assets will be strained beyond their ability to accommodate the variability; economies of production will be lost; and **the product line will collapse into an old-style, one-at-a-time product development effort**."

    Too narrow: "New product opportunities will either be rejected as being out of scope or be accepted but then result in too much rework. The product line will stagnate."

Both directions kill the thing, in opposite ways. And when I catch myself promising "modular slots that work identically in a hyperscale cloud and a GPU-poor disconnected enclave", that sounds a lot like the ambition in SEI's first paragraph.

## Each layer wants a different discipline

| Layer | Framing | Discipline |
|---|---|---|
| **Assurance substrate** | **Platform** | Mandatory, minimal, consumed verbatim. No forking. Uniformity here is worth what it costs. |
| **Accredited deployment patterns** | **Genuine product line** | A bounded family. Model commonality and variability properly, in the SEI sense. |
| **Application architecture** | **Explicitly out of scope** | The two attempts I can trace both died here. |

So when this site says "swappable slots", it means **swappability in the substrate and the patterns**; how an application gets built stays the programme's own business.

### Why I'd keep the third row closed

**SDC (1975--78)** -- the first organisation to build and trademark "The Software Factory", roughly 200 programmers centralised in Santa Monica. Cusumano's diagnosis puts **too much product variety** first, ahead of everything else.

**Microsoft Software Factories (2003--08)** -- model-driven development and domain-specific languages, aiming to generate applications from models. Faded.

Standardising *how applications are built* is the ambition that killed both of them. I haven't found a counter-example, which isn't the same as there not being one -- two cases thirty years apart is a thin basis for a law. Thin or not, it's enough that I'd stop the factory at *how evidence about applications is produced*: narrower ground, and that doesn't seem to have been standardised yet either.

## Measuring whether it holds

Toshiba's own productivity data is the sharpest test I've found, and it behaves like a step function:

!!! danger "Reuse pays above 80% unchanged. It does nothing between 20% and 80%. **Below 20% it is net harmful.**"

If that curve holds anywhere outside Toshiba -- and I don't know that it does -- it gives you something to measure: **the modification rate of shared assets.** A slot implementation that programmes fork by 40% is worse than having no shared asset at all, since you're paying the coordination cost of a shared component and getting none of the benefit.

Toshiba also hit a practical reuse ceiling of about 50%, and their productivity curve went +22% in year one, +70% by year five, then **+8% across the next four**. That last figure is the one I'd plan around. What happens to the business case when the curve flattens in year six?

## What "out of scope" means in practice

What the factory owns:

- producing, signing and binding evidence
- gating on that evidence, unbypassably
- carrying evidence across boundaries
- declaring what each slot implementation can and cannot do
- measuring its own delivery outcomes

What each programme keeps for itself:

- how you structure your application
- which language or framework you use
- your domain model, your API design, your database schema
- whether you use microservices
- your team structure

!!! tip "The test"
    A proposed feature is probably out of scope if it would make two different applications more similar to each other, and in scope if it would make their *evidence* more similar. It's rough, and I'd expect edge cases where it decides nothing at all.

If your line sits somewhere else, which of the layers above would you move across it?

## Worth saying out loud, first

There's an irony worth owning before someone else raises it.

SDC's model *"was an important influence on the software standards later developed by the U.S. Department of Defense"* -- the heavyweight, documentation-driven DOD-STD-2167 lineage. And SEI's director sat on the 2018 Defense Science Board task force that put "software factory" back into DoD policy.

**So the DoD coined the term, built the heavyweight standards regime out of it, and then re-adopted the same word to escape that regime.** That's how the thread reads to me -- two sources with thirty years between them, so it's a story about the word more than a causal account of the policy.

Say it first, with amusement. Then the point belongs to you when a sceptic reaches for it.

---

**Next:** [The Five Primitives](../how/primitives.md) -- the mechanism, now that the boundaries are drawn.
