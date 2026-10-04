# Glossary

The terms I had to pin down before the rest of the site would hold together. Where a definition comes from a standard or a policy document I've said so; where it's my own reading, I've tried to say that too.

Air gap
:   An environment with no network path to the outside. Transfer happens by physical media and nothing inspects the bytes. Cross-domain is the **mediated** case, where a guard reads what crosses and may rewrite it; conflating the two is behind most of the confusion I've run into here. See [The Same Change, Air-Gapped](example/airgap.md).

Attestation
:   A signed statement about an artefact, bound to it by cryptographic digest. In practice: a DSSE envelope wrapping an in-toto Statement with a declared predicate type. Pretty much everything else in a factory gets traded in these.

Capability descriptor
:   A machine-readable declaration by a slot implementation of which outcomes it can actually deliver. The factory core reads it at startup and switches off the features the implementation cannot support. Limits then surface in configuration, where there is still time to plan around them. Every capability it claims must have been **measured** on the implementation making the claim. See [The Five Primitives](how/primitives.md).

cATO
:   Continuous Authorization to Operate. US DoD policy since February 2022, requiring continuous monitoring fed into a live dashboard. The unit it authorises is the **system**. Its whole scope is the **maintenance** of an authorisation already granted: the route to obtaining that first authorisation runs through the ordinary assessment process. A handful of pre-2022 programmes still operate one; I've found no published count, and DoD's own plan still lists issuing a cATO as carried-over work.

CDR -- Content Disarm and Reconstruction
:   Deconstructing a file, discarding anything not explicitly permitted, and regenerating it. It protects document viewers from documents, and **cannot meaningfully sanitise compiled code**, where the payload is executable by design -- so applying it to software changes every digest without addressing the threat.

Control inheritance
:   A system claiming compliance with a security control because the platform it runs on has already been assessed against it. The economic engine of the whole proposition -- and why there's a machine-readable control-mapping file at all.

Cross-domain
:   Transfer mediated by a guard or diode, which **may refuse or rewrite what crosses**. Rewriting breaks signatures, and I haven't found anyone who's solved that cleanly. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

Delegated verdict
:   An accountable party verifies expensively once and signs a cheap assertion. Everyone downstream checks that one signature and inherits the verdict. The same shape turns up in the policy gate, the cross-domain importer and the human reviewer.

Diode
:   A device enforcing one-way data flow physically. Its guarantee covers direction of travel, and the payload bytes arrive **exactly as they were sent**. Digests therefore survive the crossing. Put a guard in front of the diode and it is the guard's rewriting that breaks them.

DSSE
:   Dead Simple Signing Envelope. The signature covers a pre-authentication encoding of the payload *and* its declared type together, which defeats the type-confusion attacks that affected ad-hoc JSON signing. **Never invent an alternative** -- the tooling assumes this encoding, so anything else won't verify.

Golden path / paved road
:   A pre-assembled, supported route through the factory -- pipeline, project template and documentation shipped as one unit. It earns its keep by being the fastest road available, and turns into a **golden cage** the moment it is the only one.

Guard
:   A device enforcing content policy at a security boundary: inspection, validation, filtering, and possibly transformation. See [Integrity vs Inspection](tradeoffs/integrity-vs-inspection.md).

Hermetic build
:   A build with no network access, achieved by prefetching all declared dependencies first. **SLSA Build Level 3 leaves it optional**, which seems to catch a lot of people out. Hermeticity turns out to be a question of lock-file discipline: pin every dependency, fetch it by digest, and the network can stay switched off for free. Getting that right produces a hash-verified dependency list as a side effect, which is why I treat hermeticity and SBOM quality as one problem.

in-toto Statement
:   The standard wrapper binding a claim to an artefact: a `subject` with digests, and a `predicateType` URI declaring what kind of claim it is. Artefacts are matched **purely by digest**, which leaves the verifier to judge whether a given match is meaningful.

Internal developer platform
:   The civilian term for what defence calls a software factory. Searching "software factory" got me defence material and vendor copy; searching platform engineering got me the evidence base.

OCI referrers
:   The registry mechanism for discovering what is attached to an artefact digest -- signatures, SBOMs, attestations. A **live API call**, and I've found no file-based equivalent, so a bundle has to materialise the graph into tags before crossing a boundary. The rule: *the registry must support it; the bundle must not depend on it.*

OSCAL
:   A machine-readable format for compliance information. The obvious candidate for automated control evidence, and **the clearest case of informed abandonment I've come across** -- more than one well-resourced organisation built on it and walked away. Build to the outcome; keep the serialisation swappable. See [Build vs Adopt](tradeoffs/build-vs-adopt.md).

Provenance
:   An attestation describing how an artefact was built -- builder identity, parameters, resolved dependencies. Its trust model splits parameters into **external** (untrusted, must be verified downstream) and **internal** (platform-set, trusted).

Reachability
:   Whether vulnerable code can actually be invoked from the application. The question that decides whether a finding is real. **52.9% of real-world SBOMs declare no dependency edges at all**, so reachability analysis over them silently returns "not reachable" for everything.

Software factory
:   DoD's own definition, from *DevSecOps Fundamentals v2.5* section 2.3: *"a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes."* Evidence, provenance, signatures and compliance appear **nowhere in it**; the whole definition rests on people, tools, processes and automation. The same document distinguishes it from a **DevSecOps platform** -- *"A software factory encompasses the entire set of software capabilities required to deliver resilient software capability at speed. The DevSecOps platform consists of those software capabilities that are common across all software factories."* Reading those two together, I take the containment to run platform, then factories, then pipelines. The civilian equivalent term is *internal developer platform*.

Slot
:   A component position defined by the **outcome it must produce**. Which tool fills it stays an implementation choice, made per environment. That's what lets one architecture serve a cloud and an enclave. See [Slots and Outcomes](how/slots.md).

SLSA
:   A framework of levels for build integrity. Level 3 demands isolation, ephemerality, and that **cache poisoning be impossible**, meaning output must be identical whether or not the cache is used. Every CI cache I've looked at fails this. And **I can't find SLSA in any regulatory text**, which is a weak negative, so a better search may well turn one up. It's the instrument you reach for to satisfy an obligation written somewhere else, so cite the obligation and name SLSA as the means of meeting it.

Trusted importer
:   An accountable party on the near side of a boundary that verifies the upstream chain and signs its own attestation of what crossed. The cost is that the far side's cryptographic trust now terminates at the importer; the builder's own signature stops at the boundary and goes no further. Say so plainly wherever the chain is described, because any claim of an unbroken chain back to the builder would be false.

VEX -- Vulnerability Exploitability eXchange
:   A statement that a vulnerability does or does not affect a product, with a machine-readable justification. The mechanism that keeps a gate switched on, and it holds only while recording a statement costs an engineer thirty seconds. Make it a ticket and the team will find a reason to switch the gate off. **I can't find a registered predicate type for it**, and the specification has been frozen since 2023.

VSA -- Verification Summary Attestation
:   The concrete form of a delegated verdict. Records the digest of the **policy** that produced it, so a policy change detectably invalidates prior verdicts. The only document admission control should read.
