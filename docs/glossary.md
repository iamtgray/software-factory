# Glossary

Air gap
:   An environment with no network path to the outside. Transfer happens by physical media and nothing inspects the bytes. **Distinct from cross-domain**, and conflating the two causes most confusion in this field. See [The Same Change, Air-Gapped](example/airgap.md).

Attestation
:   A signed statement about an artefact, bound to it by cryptographic digest. In practice: a DSSE envelope wrapping an in-toto Statement with a declared predicate type. The universal currency of a factory.

Capability descriptor
:   A machine-readable declaration by a slot implementation of which outcomes it can actually deliver. Lets the factory core turn features off rather than discovering limits as production flakiness. Should carry **measured** capability, not promises. See [The Five Primitives](how/primitives.md).

cATO
:   Continuous Authorization to Operate. US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. It authorises **systems**, not organisations, and **modifies how you keep an authorisation rather than providing a route to getting one**. A handful of pre-2022 programmes still operate one; no count has ever been published, and DoD's own plan still lists issuing a cATO as carried-over work.

CDR -- Content Disarm and Reconstruction
:   Deconstructing a file, discarding anything not explicitly permitted, and regenerating it. Protects document viewers from documents. **Cannot meaningfully sanitise compiled code**, because the payload is executable by design -- so applying it to software changes every digest without addressing the threat.

Control inheritance
:   A system claiming compliance with a security control because the platform it runs on has already been assessed against it. The economic engine of the whole proposition -- and the reason the machine-readable control-mapping file matters.

Cross-domain
:   Transfer mediated by a guard or diode, which **may refuse or rewrite what crosses**. Rewriting breaks signatures, which is the central unsolved tension. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

Delegated verdict
:   An accountable party verifies expensively once and signs a cheap assertion that downstream trusts instead of repeating the work. One pattern covering three instances: the policy gate, the cross-domain importer, and the human reviewer.

Diode
:   A device enforcing one-way data flow physically. **Does not alter payload bytes** -- its property is flow, not content. So a diode preserves digests; a guard in front of it may not.

DSSE
:   Dead Simple Signing Envelope. The signature covers a pre-authentication encoding of the payload *and* its declared type together, which defeats the type-confusion attacks that affected ad-hoc JSON signing. **Never invent an alternative** -- every signature ever issued is over this encoding.

Golden path / paved road
:   A pre-assembled, supported route through the factory -- pipeline, project template and documentation shipped as one unit. Becomes a **golden cage** when it's the only road rather than the fastest one.

Guard
:   A device enforcing content policy at a security boundary: inspection, validation, filtering, and possibly transformation. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

Hermetic build
:   A build with no network access, achieved by prefetching all declared dependencies first. **Not required for SLSA Build Level 3** -- a widely believed error. Hermeticity is a lock-file discipline problem, not a sandboxing one, and it produces a hash-verified dependency list as a side effect, which is why hermeticity and SBOM quality are the same problem.

in-toto Statement
:   The standard wrapper binding a claim to an artefact: a `subject` with digests, and a `predicateType` URI declaring what kind of claim it is. Artefacts are matched **purely by digest**, so the verifier must independently decide whether a match is meaningful.

Internal developer platform
:   The civilian term for what defence calls a software factory. Search for "software factory" and you get defence material and vendor copy; the evidence base is filed under platform engineering.

OCI referrers
:   The registry mechanism for discovering what is attached to an artefact digest -- signatures, SBOMs, attestations. A **live API call** with no file-based equivalent, so a bundle must materialise the graph into tags before crossing a boundary. The rule: *the registry must support it; the bundle must not depend on it.*

OSCAL
:   A machine-readable format for compliance information. The obvious candidate for automated control evidence, and **the clearest case of informed abandonment in the ecosystem** -- multiple well-resourced organisations built on it and walked away. Build to the outcome; keep the serialisation swappable. See [Build vs Adopt](tradeoffs/build-vs-adopt.md).

Provenance
:   An attestation describing how an artefact was built -- builder identity, parameters, resolved dependencies. Its trust model splits parameters into **external** (untrusted, must be verified downstream) and **internal** (platform-set, trusted).

Reachability
:   Whether vulnerable code can actually be invoked from the application. The question that decides whether a finding is real. **52.9% of real-world SBOMs declare no dependency edges at all**, so reachability analysis over them silently returns "not reachable" for everything.

Slot
:   A component position defined by the **outcome it must produce** rather than the tool that fills it. The mechanism that lets one architecture serve a cloud and an enclave. See [Slots and Outcomes](how/slots.md).

SLSA
:   A framework of levels for build integrity. Level 3 demands isolation, ephemerality, and -- the sleeper requirement -- that **cache poisoning be impossible**, meaning output must be identical whether or not the cache is used. Most CI caches fail this. And **SLSA appears in zero regulatory texts**: you comply *via* it, never *by* it.

Trusted importer
:   An accountable party on the near side of a boundary that verifies the upstream chain and signs its own attestation of what crossed. The cost is that the far side's cryptographic trust now terminates at the importer rather than the original builder. Say so rather than implying an unbroken chain.

VEX -- Vulnerability Exploitability eXchange
:   A statement that a vulnerability does or does not affect a product, with a machine-readable justification. The mechanism that keeps a gate switched on -- but only if recording one costs thirty seconds rather than a ticket. **No registered predicate type exists**, and the specification has been frozen since 2023.

VSA -- Verification Summary Attestation
:   The concrete form of a delegated verdict. Records the digest of the **policy** that produced it, so a policy change detectably invalidates prior verdicts. The only document admission control should read.
