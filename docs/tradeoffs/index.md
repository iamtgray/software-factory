# Trade-offs

Some of the properties a factory is meant to have conflict with each other, and several of the most-recommended practices have measured negative effects. These five changed a design decision here.

---

**[Integrity vs Inspection](integrity-vs-inspection.md)**
:   A guard that sanitises content by rewriting it destroys every signature that proves the content is trustworthy. Guidance mandates inspection, supply-chain practice requires verification, and I haven't found a published standard, vendor document or paper that reconciles the two.

**[Gates vs Attention](gates-vs-attention.md)**
:   Every gate you add consumes reviewer attention. Suppressions grow monotonically, half of them suppress nothing, and the measured cause is false positives.

**[Mandate vs Adoption](mandate-vs-adoption.md)**
:   Platform users show **−8% throughput and −14% change stability**, and *mandating* exclusive use costs a further 6% of throughput. In a classified environment the usual escape valve (people routing around the platform) becomes a security incident. The figures are measured across platform users generally; the classified-environment consequence is extrapolated.

**[AI: Capability vs Provability](ai.md)**
:   The steps that make generation more reproducible appear to make its output harder to check. The air-gapped tier gets the better AI story, because what survives without frontier models is roughly the set of things with deterministic verifiers.

**[Build vs Adopt](build-vs-adopt.md)**
:   Eight slots are empty, and twelve projects with under 300 stars carry the stack -- nine of them on the critical path. Each slot turns on whether the tool will still exist in three years, and whether the feature we need sits behind a licence.

## The meta-trade-off

**Every property you add costs operational burden, and operational burden is what gets factories switched off.**

None of the documented failures failed for want of a feature. The deployment path became something nobody could explain, or the gate produced findings nobody could action, or the platform team became an approvals bureaucracy, or the budget for the thing that made it work was cut.

!!! quote "SEI, 2026"
    Organisations "collapsed under the weight of their own tooling... until no one can explain their own deployment path."

That's why the minimal profile is the primary deliverable, and why a realistic hardware footprint decides whether anyone can run the thing. Published evaluation environments for comparable platforms want **9 CPU / 28 GB** and **8 CPU / 32 GB** -- both explicitly labelled as *not* production sizings, with one project publishing no production minimum at all.
