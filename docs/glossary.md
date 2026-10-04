# Glossary

Air gap
:   An environment with no network path to the outside. Transfer happens by physical media and nothing inspects the bytes. Cross-domain is the **mediated** case, where a guard reads what crosses and may rewrite it. See [The Same Change, Air-Gapped](example/airgap.md).

Attestation
:   A signed statement about an artefact, bound to it by cryptographic digest. In practice: a DSSE envelope wrapping an in-toto Statement with a declared predicate type.

Capability descriptor
:   A machine-readable declaration by a slot implementation of which outcomes it can actually deliver. The factory core reads it at startup and switches off the features the implementation cannot support, so limits surface in configuration while there's still time to plan around them. Every capability it claims must have been **measured** on the implementation making the claim. See [The Five Primitives](how/primitives.md).

cATO
:   Continuous Authorization to Operate. US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. The unit it authorises is the **system**. Its scope is the **maintenance** of an authorisation already granted -- the route to obtaining that first authorisation runs through the ordinary assessment process. A handful of pre-2022 programmes still operate one; I've found no published count, and DoD's own plan still lists issuing a cATO as carried-over work.

CDR -- Content Disarm and Reconstruction
:   Deconstructing a file, discarding anything not explicitly permitted, and regenerating it. It **cannot meaningfully sanitise compiled code**, where the payload is executable by design -- applied to software it changes every digest without addressing the threat.

Control inheritance
:   A system claiming compliance with a security control because the platform it runs on has already been assessed against it.

Cross-domain
:   Transfer mediated by a guard or diode, which **may refuse or rewrite what crosses**. Rewriting breaks signatures. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

Delegated verdict
:   An accountable party verifies expensively once and signs a cheap assertion. Everyone downstream checks that one signature and inherits the verdict. The same shape turns up in the policy gate, the cross-domain importer and the human reviewer.

Diode
:   A device enforcing one-way data flow physically. Its guarantee covers direction of travel, and the payload bytes arrive **exactly as they were sent**, so digests survive the crossing. Put a guard in front of the diode and it is the guard's rewriting that breaks them.

DSSE
:   Dead Simple Signing Envelope. The signature covers a pre-authentication encoding of the payload *and* its declared type together, which defeats the type-confusion attacks that affected ad-hoc JSON signing. The tooling assumes this encoding, so anything else won't verify.

Golden path / paved road
:   A pre-assembled, supported route through the factory -- pipeline, project template and documentation shipped as one unit. It becomes a **golden cage** the moment it's the only route on offer.

Guard
:   A device enforcing content policy at a security boundary: inspection, validation, filtering, and possibly transformation. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

Hermetic build
:   A build with no network access, achieved by prefetching all declared dependencies first. **SLSA Build Level 3 leaves it optional.** Hermeticity is a question of lock-file discipline: pin every dependency, fetch it by digest, and the network can stay switched off.

in-toto Statement
:   The standard wrapper binding a claim to an artefact: a `subject` with digests, and a `predicateType` URI declaring what kind of claim it is. Artefacts are matched **purely by digest**, which leaves the verifier to judge whether a given match is meaningful.

Internal developer platform
:   The civilian term for what defence calls a software factory.

OCI referrers
:   The registry mechanism for discovering what is attached to an artefact digest -- signatures, SBOMs, attestations. It's a **live API call** with no file-based equivalent, so a bundle has to materialise the graph into tags before crossing a boundary. *The registry must support it; the bundle must not depend on it.*

OSCAL
:   A machine-readable format for compliance information. More than one well-resourced organisation built automated control evidence on it and walked away. See [Build vs Adopt](tradeoffs/build-vs-adopt.md).

Provenance
:   An attestation describing how an artefact was built -- builder identity, parameters, resolved dependencies. Its trust model splits parameters into **external** (untrusted, must be verified downstream) and **internal** (platform-set, trusted).

Reachability
:   Whether vulnerable code can actually be invoked from the application. **52.9% of real-world SBOMs declare no dependency edges at all**, so reachability analysis over them silently returns "not reachable" for everything.

Software factory
:   DoD's own definition, from *DevSecOps Fundamentals v2.5* section 2.3: *"a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."* Evidence, provenance, signatures and compliance appear **nowhere in it**. The same document distinguishes it from a **DevSecOps platform** -- *"A software factory encompasses the entire set of software capabilities required to deliver resilient software capability at speed. The DevSecOps platform consists of those software capabilities that are common across all software factories."* The containment therefore runs platform, then factories, then pipelines. The civilian equivalent term is *internal developer platform*.

Slot
:   A component position defined by the **outcome it must produce**. Which tool fills it stays an implementation choice, made per environment. See [Slots and Outcomes](how/slots.md).

SLSA
:   A set of levels for build integrity. Level 3 demands isolation, ephemerality, and that **cache poisoning be impossible**, meaning output must be identical whether or not the cache is used. Every CI cache I've looked at fails this. It appears in no regulatory text I can find.

Trusted importer
:   An accountable party on the near side of a boundary that verifies the upstream chain and signs its own attestation of what crossed. The cost is that the far side's cryptographic trust now terminates at the importer, not at the builder.

VEX -- Vulnerability Exploitability eXchange
:   A statement that a vulnerability does or does not affect a product, with a machine-readable justification. It keeps a gate switched on only while recording a statement costs an engineer thirty seconds -- make it a ticket and the team will find a reason to switch the gate off. There's no registered predicate type for it, and the specification has been frozen since 2023.

VSA -- Verification Summary Attestation
:   The concrete form of a delegated verdict. Records the digest of the **policy** that produced it, so a policy change detectably invalidates prior verdicts.
