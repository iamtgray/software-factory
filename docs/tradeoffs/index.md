# Trade-offs

Most material about software factories reads as though the only cost is effort -- do more of the good things and you get a better factory. The evidence says otherwise. Several of the central properties are in genuine tension, and a few of the most-recommended practices have measured negative effects.

Five of them actually change a design decision.

---

**[Integrity vs Inspection](integrity-vs-inspection.md)**
:   The central unsolved tension. A guard that sanitises content by rewriting it destroys every signature that proves the content is trustworthy. You can inspect bytes or you can verify them; guidance mandates the first, supply-chain practice requires the second. No published standard, vendor document or paper reconciles the two.

**[Gates vs Attention](gates-vs-attention.md)**
:   Every gate you add consumes reviewer attention, which is the factory's scarcest resource. Strictness and survival are inversely related: suppressions grow monotonically, half of them suppress nothing, and the measured cause is false positives. A gate that exhausts its reviewers is worth less than no gate.

**[Mandate vs Adoption](mandate-vs-adoption.md)**
:   The uncomfortable numbers. Platform users show **−8% throughput and −14% change stability**, and *mandating* exclusive use costs a further 6% of throughput. In a classified environment the usual escape valve (people route around the platform) is a security incident rather than a productivity loss.

**[AI: Capability vs Provability](ai.md)**
:   The capability you want and the provability you need pull in opposite directions. Reproducible generation is *less* verifiable than non-reproducible generation. And the air-gapped tier gets the better AI story, because what survives without frontier models is exactly what has deterministic verifiers.

**[Build vs Adopt](build-vs-adopt.md)**
:   Eight slots are empty, but twelve projects with under 300 stars sit on the critical path with no substitute. The question isn't "does this exist". It's "will it exist in three years, and is the feature we need behind a licence".

---

## The meta-trade-off

Running underneath all five: **every property you add costs operational burden, and operational burden is what gets factories switched off.**

The pattern is consistent across every documented failure. Nobody abandons a factory because it lacked a feature. They abandon it because the deployment path became something nobody could explain, or the gate produced findings nobody could action, or the platform team became an approvals bureaucracy, or the budget for the thing that made it work was cut.

!!! quote "SEI, 2026"
    Organisations "collapsed under the weight of their own tooling... until no one can explain their own deployment path."

Which is why the minimal profile is the primary deliverable rather than a stripped-down afterthought, and why a realistic hardware footprint matters more than a feature matrix. Published evaluation environments for comparable platforms want **9 CPU / 28 GB** and **8 CPU / 32 GB** -- both explicitly labelled as *not* production sizings, with one project publishing no production minimum at all.
