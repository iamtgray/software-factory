# Trade-offs

Most of what I've read about software factories treats effort as the only cost -- do more of the good things and you get a better factory. That hasn't matched what I found. Several of the properties a factory is meant to have sit in genuine tension with each other, and a few of the most-recommended practices have measured negative effects. Every property I've looked at carries a price, and the price is paid as operational burden by whoever has to run the thing.

These are the tensions that changed a design decision here. There are probably others I haven't walked into yet.

---

**[Integrity vs Inspection](integrity-vs-inspection.md)**
:   The one I still can't resolve. A guard that sanitises content by rewriting it destroys every signature that proves the content is trustworthy. You can inspect bytes or you can verify them; guidance mandates the first, supply-chain practice requires the second. I haven't found a published standard, vendor document or paper that reconciles the two. I've looked fairly hard, though that isn't the same as there not being one.

**[Gates vs Attention](gates-vs-attention.md)**
:   Every gate you add consumes reviewer attention, which is the scarcest thing the factory has. Strictness and survival seem to pull against each other: suppressions grow monotonically, half of them suppress nothing, and the measured cause is false positives. A gate that exhausts its reviewers has negative value -- the factory would be safer with it switched off.

**[Mandate vs Adoption](mandate-vs-adoption.md)**
:   The uncomfortable numbers. Platform users show **−8% throughput and −14% change stability**, and *mandating* exclusive use costs a further 6% of throughput. In a classified environment the usual escape valve (people routing around the platform) becomes a security incident. That last step is my inference, and it's the part of the commercial evidence I'd least trust to carry across.

**[AI: Capability vs Provability](ai.md)**
:   The capability you want and the provability you need pull in opposite directions. The steps that make generation more reproducible appear to make its output harder to check. And on my reading the air-gapped tier gets the better AI story, because what survives without frontier models is roughly the set of things that have deterministic verifiers.

**[Build vs Adopt](build-vs-adopt.md)**
:   Eight slots are empty, and twelve projects with under 300 stars carry the stack -- nine of them on the critical path. Each slot turns on whether the tool will still exist in three years, and whether the feature we need sits behind a licence. I can't answer either question honestly from a README.

---

## The meta-trade-off

Underneath all of them sits the same mechanism, or at least that's how it reads to me. **Every property you add costs operational burden, and operational burden is what gets factories switched off.**

The failures I've read about all look like variants of it. None of them failed for want of a feature. The deployment path became something nobody could explain, or the gate produced findings nobody could action, or the platform team became an approvals bureaucracy, or the budget for the thing that made it work was cut.

!!! quote "SEI, 2026"
    Organisations "collapsed under the weight of their own tooling... until no one can explain their own deployment path."

That's why the minimal profile is the primary deliverable, and why I think a realistic hardware footprint decides whether anyone can run the thing at all. Published evaluation environments for comparable platforms want **9 CPU / 28 GB** and **8 CPU / 32 GB** -- both explicitly labelled as *not* production sizings, with one project publishing no production minimum at all. So the number a real deployment needs is one I don't have; I've been assuming it's higher than either.

Which of these bites first probably depends more on your environment than on anything written here. Which of them are you already paying for, without having decided to?
