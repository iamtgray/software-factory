# Scope -- three layers, one boundary

## What forces the decision

SEI's *Framework for Software Product Line Practice* contains a 28-section catalogue of failure modes, one "Practice Risks" section per practice area.

Its scoping risk:

!!! quote "SEI, on scoping a product line"
    "The major risk associated with product line scoping is that the wrong set of products will be targeted."

    Too broad: "If it encompasses product members that vary too widely, the core assets will be strained beyond their ability to accommodate the variability; economies of production will be lost; and **the product line will collapse into an old-style, one-at-a-time product development effort**."

    Too narrow: "New product opportunities will either be rejected as being out of scope or be accepted but then result in too much rework. The product line will stagnate."

This site's promise of "modular slots that work identically in a hyperscale cloud and a GPU-poor disconnected enclave" is the ambition in SEI's first paragraph.

## Each layer wants a different discipline

| Layer | Framing | Discipline |
|---|---|---|
| **Assurance substrate** | **Platform** | Mandatory, minimal, consumed verbatim. No forking. |
| **Accredited deployment patterns** | **Genuine product line** | A bounded family. Model commonality and variability properly, in the SEI sense. |
| **Application architecture** | **Explicitly out of scope** | Both traceable attempts died here. |

When this site says "swappable slots" it means **swappability in the substrate and the patterns**; how an application gets built stays the programme's own business.

### Why the third row is closed

**SDC (1975--78)** -- the first organisation to build and trademark "The Software Factory", roughly 200 programmers centralised in Santa Monica. Cusumano's diagnosis puts **too much product variety** first.

**Microsoft Software Factories (2003--08)** -- model-driven development and domain-specific languages, aiming to generate applications from models.

Standardising *how applications are built* is the ambition that killed both. Two cases is a thin basis for a law. The factory stops at *how evidence about applications is produced*.

## Measuring whether it holds

Toshiba's productivity data behaves like a step function:

!!! danger "Toshiba's reuse thresholds"
    Reuse pays above 80% unchanged. It does nothing between 20% and 80%. **Below 20% it is net harmful.**

If those thresholds hold anywhere outside Toshiba (and I don't know that they do) they give you something to measure: **the modification rate of shared assets.** A slot implementation that programmes fork by 40% is worse than no shared asset at all, because you pay the coordination cost of a shared component and get none of the benefit.

Toshiba also hit a practical reuse ceiling of about 50%, and their productivity curve went +22% in year one, +70% by year five, then **+8% across the next four**. The business case has to survive the curve flattening in year six.

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
    A proposed feature is out of scope if it would make two different applications more similar to each other, and in scope if it would make their *evidence* more similar.

## Where the term came from

SDC's model *"was an important influence on the software standards later developed by the U.S. Department of Defense"* -- the heavyweight, documentation-driven DOD-STD-2167 lineage. And SEI's director sat on the 2018 Defense Science Board task force that put "software factory" back into DoD policy.

The DoD coined the term, built the heavyweight standards regime out of it, and then re-adopted the same word to escape that regime. Two sources thirty years apart tell you how the word travelled, nothing more.

---

**Next:** [The Five Primitives](../how/primitives.md) -- the mechanism.
