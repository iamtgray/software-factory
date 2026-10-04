# Layers, hand-offs, and the five primitives

Synthesis over `research/02`–`06`, rewritten 2026-10-04 after adversarial verification of eight load-bearing claims — three refuted, five weakened, **nothing survived intact**. The structure below is derived from mechanism rather than from requirements, which is why it mostly survived; the parts that did not survive are marked, because the corrections are the most credible material in this document.

The point of this document is to answer one question: **when work passes from one layer of the factory to the next, what exactly crosses, who vouches for it, and what does the receiver check?** Get that right and the component choices become almost arbitrary, which is the whole premise.

Two standing constraints before anything else.

**Publication.** The *DevSecOps Continuous Authorization Implementation Guide* carries **Distribution Statement C** — US Government agencies and their contractors only. Nothing from it may be quoted in any publicly publishable document, which is a real loss: its Appendix B (44 practices across 7 families) is where most of the useful detail lives. The cATO Evaluation Criteria (Statement A) and the DoD Software Modernization Strategy (public) carry the public argument instead.

**Negatives.** No finding in this document may assert a universal negative over open code. We had no working code search for any of this work, so "we found none" means "we did not find one", and its strength depends entirely on how we looked. The claim that only one cross-domain implementation exists in open source was refuted in minutes once someone looked properly — `hairgap`, `eurydice` and ANSSI's `lidi` are all one-way transfer implementations.

---

## 1. The thing the research actually converged on

Five research streams ran independently on different questions. They arrived at the same mechanism, which is the strongest signal in the whole exercise.

**Supply-chain integrity** concluded: wrap everything in DSSE → in-toto Statement, bind by `subject[].digest`, and have the pipeline gate issue a signed Verification Summary Attestation so admission control reads one cheap boolean instead of re-verifying ten documents.

**Air-gap transfer** concluded: sign a small, strictly-schema'd manifest that commits to a large payload by hash, so the verifier's whole job is schema validation plus `name == sha256(content)`. It noted this is a rediscovery of Debian's `InRelease`, OSTree's signed summary and Zarf's `aggregateChecksum`.

**Deployment and composition** concluded: slots must be Kubernetes CRDs the project owns, the core must read only `status` and never `spec`, and `status` must carry capability flags so the core degrades rather than crashes.

**The AI layer** concluded: the slot implementation publishes a machine-readable capability descriptor listing `outcomes_enabled`, and a policy gate can refuse a provenance claim from a slot that never advertised that outcome.

Four different problems. One shape. Strip the domain language and there are **five** primitives, and every hand-off in the factory is built from them.

> **This section said three until verification.** Trust configuration and freshness state were present in the design but demoted to *fields in a transfer manifest* — an air-gap implementation detail rather than something the architecture carries everywhere. That was wrong in a way that matters: both are needed by every verifier at every boundary, both must be rotatable, and both have failure modes that require no forgery at all. Treating them as manifest fields meant the connected tier silently inherited the ambient versions (a reachable CA, a live transparency log, a verifier with no memory) and nobody wrote down what happens when the ambient version is absent. Promoting them makes the disconnected case a *configuration* of the same architecture rather than a different one.

### Primitive 1 — the digest-bound statement

A small signed document that commits to a large thing by cryptographic hash, carrying a declared type.

Concretely: DSSE envelope, `payloadType`, in-toto Statement v1, `predicateType` URI, `subject[].digest`. The signature covers `PAE(payloadType, body)`, never the raw payload — which is what defeats the type-confusion attacks that plagued ad-hoc JSON signing.

This is non-negotiable and it is the one choice that is catastrophic to reverse — every signature ever issued is over that encoding. Where no registered predicate exists (OpenVEX, AI authorship, policy config, shipment manifests), mint a predicate type in a namespace we control and keep the envelope standard. **A non-standard predicate inside a standard envelope costs a little, locally. A non-standard envelope costs everything, permanently.**

Three predicates *are* already registered — `test-result/v0.1`, `runtime-trace/v0.1`, `svr/v0.2` — and should be extended rather than reinvented. The eval-result attestation that primitive 3 needs is about a day's work on top of `test-result`.

Note also, against the "catastrophic to reverse" framing, §8: nobody has asked which signature algorithm a defence customer will mandate.

### Primitive 2 — the delegated verdict

An accountable party performs an expensive verification once and issues a cheap signed assertion that downstream parties trust instead of repeating the work.

The research found this in three places and did not notice they were one thing:

- **The policy gate.** It evaluates provenance shape, SBOM quality, scan results, hermeticity and trusted-task membership, then signs a verdict. Admission control verifies the verdict and nothing else. Rich policy at admission time is how you take a cluster down.
- **The cross-domain importer.** A gated low-side release authority verifies the upstream chain and signs its own attestation of what crossed the boundary. The high side's trust terminates at the importer rather than the original builder.
- **The human reviewer.** A named person asserts the change is defensible and signs off in the commit. Same pattern, lower assurance, no machine format — see Transition A.

One pattern: *verify expensively where you can, assert cheaply where you must, and name the party whose signature you are now trusting.* Recognising them as one pattern means one implementation, one key-management story, one audit format, and one honest sentence about where the chain delegates.

Three rules make it safe, all three routinely violated:

- the verdict records the **digest of the policy** that was applied, so a policy change detectably invalidates prior verdicts;
- where AI was involved, the verdict records the **model identity and the capability-descriptor digest**, so a model swap invalidates prior verdicts exactly as a policy change does — this is new, and it is the difference between an AI-assisted gate and an unfalsifiable one;
- consumers accept only specific **(signer, verifier) pairs**. If one key signs both the build provenance and the verdict, the verdict is worthless.

### Primitive 3 — the capability descriptor

The implementation declares, in machine-readable form, which outcomes it can actually deliver. The core reads it and turns features off.

The AI research invented this for inference tiers (`outcomes_enabled: [autocomplete, review, test-gen]`). The deployment research invented it for slot CRDs (`status.implementation`, `status.invocation`, `supportedFormats`, `fipsMode`, `slsaSourceLevel`). **These should be the same object.** One descriptor shape, published by every slot implementation, consumed by the core and by the gates.

The descriptor must carry **measured** capability — a signed evaluation score, with the attestation digest — not a hand-maintained list of promises. A declared-only descriptor rots exactly like every other hand-written compliance artefact, which is the failure this whole programme is about.

That is also how *degradation becomes a design decision rather than a production surprise*. A factory that says "in this enclave, autonomous multi-file change is disabled, here is the measurement that justifies it" is more credible to an assessor than one claiming uniform capability that quietly flakes. And because the descriptor is digest-referenced from the attestations, a gate can verify after the fact that the slot which produced an artefact had advertised the outcome it was used for.

### Primitive 4 — trust configuration

The keys, roots, revocations and validity windows a verifier needs in order to check anything at all.

Easy to miss because when connected it is **ambient**: the verifier reaches a CA, a transparency log, a revocation endpoint. Remove the network and it becomes **payload** — versioned, rotatable, and travelling with the artefact.

What it must comprise:

- the current trust root **plus the full chain of previous roots**, so a verifier offline for years can walk forward to the present;
- **per-instance validity windows**, cumulative and never replaced, because signatures made in the past must still verify;
- a **revocation set with an explicit issue time**, and a stated policy that anything newer than that time is *unknown* rather than *valid*. Getting this backwards is how an offline verifier is talked into accepting a revoked key.

Rotation is solved: TUF-style threshold signing, new root metadata signed by a threshold of the old root's keys, walkable offline with no network. Ship the whole chain every time.

**Bootstrap is not solvable cryptographically.** The first root arrives out of band — courier, two-person integrity, a fingerprint read over an authenticated voice channel, or embedded in an accredited binary — because a self-asserted root is not a root. So the first crossing is a trusted-*process* problem, and this document is the place that has to say so rather than leaving it implied.

### Primitive 5 — freshness and monotonicity state

Evidence about *when* and *in what order*, plus the state a receiver keeps so that omission and rollback are detectable.

Why it is a primitive and not a field: a verifier with no memory cannot tell that it was handed an *old* valid bundle, or that a bundle was silently skipped. Neither attack requires any forgery. Every signature checks out.

| Element | What it prevents |
|---|---|
| `validNotBefore` / `validNotAfter` | Indefinite replay of a stale artefact |
| `sequence`, strictly monotonic per (producer, destination) pair | Rollback and omission |
| `supersedes` | Ambiguity about which of two valid bundles is current |
| A high-water mark **retained by the receiver** | All of the above — without it the other fields are decoration |
| The vulnerability-database version and timestamp behind any scan verdict | A months-old scan being read as a current one |

The receiver-held high-water mark is the load-bearing part, and it has a correctness defect that only emerges when you read the transfer design against operations: **restoring the high side from backup resets it.** See §8.

---

## 2. The layer model

Seven layers. The only thing that matters about this list is the boundaries between the entries, which §3 covers.

| # | Layer | Outcome it owes the next layer |
|---|---|---|
| 1 | **Intent** — ticket, requirement, threat assessment | An identified, accountable unit of work with a stated security obligation |
| 2 | **Authoring** — IDE, agent harness, inference slot, sandbox | A diff whose authorship and method are declared |
| 3 | **Source of record** — forge, review, branch policy | A commit, reviewed per a stated policy, attributable to a human in the DCO chain |
| 4 | **Build** — CI, hermetic prefetch, ephemeral executor | An artefact plus non-falsifiable provenance about how it was made |
| 5 | **Evidence** — SBOM, scan, VEX, test results, attestations | A complete, digest-bound, signed evidence set discoverable from the artefact |
| 6 | **Judgement** — policy gate, waiver workflow, VSA issuance | A signed verdict naming the policy version that produced it |
| 7 | **Delivery** — bundle, transfer, admission, runtime | A running workload whose right to run was checked at the moment of use |

Layers 1–6 are the same in every environment. Layer 7 is where environment tiers diverge, and even there the *contract* is identical; only the implementation changes.

Worth being blunt about how much of this the doctrine asks for. The authoritative definition (DevSecOps Fundamentals v2.5 §2.3) is that a software factory is "a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes." It mentions neither evidence nor provenance. The word **"signed" appears zero times** in that document, and nobody is ever told to verify a signature — not at pull, not at build, not at admission, not at deploy. The model is trust-by-source plus rescan with two mandated scanners. Across the reference design and Fundamentals together, `reproducible`, `OSCAL`, `admission`, `attestation`, `SLSA`, `in-toto`, `Sigstore`, `cosign`, `provenance`, `notary`, `checksum` and `digest` all score zero. **SBOM is the exception — it is demanded once, Fundamentals §3.3.1.2 — so SBOM never belongs in a list of absences.**

Layers 5 and 6 are therefore things we are choosing on merit, not compliance requirements we can wave through. That is a harder sell and a more honest one.

---

## 3. The five trust-domain transitions

Most layer boundaries are ordinary function calls. Five are trust-domain transitions, where the receiver cannot verify what the sender did by inspection and must rely on a signature. These are the entire architecture. Everything else is plumbing.

Keep the number at five. Each one needs a key, a policy, an audit trail and an honest sentence about what it delegates, and adding a sixth because it looked architecturally tidy is how operational burden becomes the reason the thing gets switched off.

### Transition A — author → source of record

**What crosses:** a diff, plus a declaration of how it was made.

**The problem:** if an agent wrote it, the factory needs to know that later, and no standard exists for saying so. The Linux kernel is the only serious precedent and it is a good one: `Assisted-by: LLM <tools>` as a git trailer, scrutiny proportional to how much was generated, and the hard rule that **agents must not add `Signed-off-by` because only a human can certify the DCO.**

**What the receiver checks:** a human in the DCO chain has signed off; the `Assisted-by` trailer is present when generation was material; mechanical checks that human review cannot perform have run — specifically Unicode normalisation and invisible-character detection, because GlassWorm demonstrated that malicious code can be invisible in every diff view, which makes human review an accountability control rather than a detection control.

**This is the only hand-off in the ecosystem with no signed artefact at all.** The sweep of 24 slots found that everything available either *configures* review rules or *reports* on them; nothing signs "policy X was met for commit Y". And it matters more under AI authorship than it did before, for a specific reason: when a model drafts most of a change, the human sign-off is the only place accountability attaches, and it is precisely the thing that currently exists as an unsigned text line in a commit message. The integrity boundary moved to the one boundary with no cryptography on it.

**The attestation to mint:** an AI-authorship predicate over the diff digest, signed by the harness identity, carrying model identity, model licence, tier, the digest of the capability descriptor that was in force, and the harness's **credential and egress posture** — the known harness vulnerabilities are structural (CI credential and config handling) rather than model-behavioural, so posture is the thing worth recording. No regime currently requires any of this. The forward risk is asymmetric: a factory that recorded nothing cannot retrofit it, and recording it costs almost nothing now.

### Transition A′ — agent → agent, and the recommendation is don't

**What crosses:** nothing, if the design is right.

**Keep agents as leaves. No delegation chains in the core.** Two reasons, both structural rather than a bet on current model quality:

- **Attribution laundering.** A chain destroys the link between a change and an accountable identity. If agent A asked B to ask C and C made the edit, the trailer says nothing useful and no human was in the loop at the point the decision was taken. Transition A's whole value is that a named person is answerable; a delegation chain dissolves exactly that.
- **False independence.** "Independent" verifying agents collapse to very few genuinely corruption-distinct domains — same model family, same prompt lineage, same tool outputs. Redundancy buys far less than the agent count suggests, and the count is what gets quoted.

This is listed as a transition because it is one, and because naming it is how you stop it being added later as an obvious productivity win. Where multi-agent structure is genuinely wanted, put it inside a single accountable harness identity so the attestation at A still names one signer.

### Transition B — build → judgement

**What crosses:** an artefact digest plus an evidence set.

**The problem:** the evidence is produced by several parties with different trustworthiness, and the gate must not confuse them. Build platform signs provenance and the SBOM; the scanner signs scan results; the VEX issuer signs VEX; the test task signs test results; the gate itself signs the verdict. Separate identities, decided once, painful to retrofit.

**What the receiver checks:** every document binds to the artefact by `subject[].digest`; the signer of each is the expected signer for that document type; `externalParameters` are allowlisted rather than denylisted, because SLSA says verifiers should reject unrecognised fields there; and the build's task references match a pre-approved trusted-task list. That last check — *provenance that the build only ran steps we approved* — is the highest-value rule in the set and the one most factories omit.

**The output:** a VSA. From here on, nothing re-reads the evidence set in the hot path.

**What to fix:** the best open implementation ships its **build-time** SBOM unsigned, by its own documented admission, and since an author signature is now a CISA minimum element that is both a security and a compliance gap. But the earlier claim that this was "the cheapest differentiator available" was overstated: the same project **cryptographically signs its release-time SBOM**. Only the build-time one is unsigned. Worth fixing, not worth leading with.

### Transition C — low side → high side

This transition was wrong in this document and the correction is substantial. Two cases that were being treated as one.

#### The media-gap case: the gap claim is refuted

**The claim "evidence does not cross the air-gap with the artefact" is false, and it was the central thesis.**

Hauler carries cosign signatures, attestations, SBOMs *and* the OCI 1.1 referrers graph **by default** — `--exclude-extras` defaults to false — in a standard zstd-compressed OCI layout, and reconstructs the `sha256-<digest>.sig` / `.att` / `.sbom` tags and re-pushes referrers by digest on the far side. `zarf package verify` performs full offline verification with a Sigstore trusted root **embedded in the binary**, `--insecure-ignore-tlog` defaulting to true "for air-gap", and RFC 3161 timestamp verification. The test this project set — a high side independently establishing what it was given with zero network access and no ability to ask anything — **is met today by an existing command.**

So the earlier "build a transfer envelope, it is the flagship" framing is deleted. **Do not invent a bespoke transfer format for the sneakernet case.** A standard OCI layout already crosses and is read by five tools; a new format would be a one-implementation artefact needing its own accreditation, and an accreditor's first question would be "why not OCI layout?", to which "we thought evidence didn't cross" is a factually wrong answer.

**What is actually missing, and this is the new build target:**

1. **A fail-closed receiver-side gate.** The evidence arrives; nothing is obliged to look at it. Hauler's disconnected-side `load` has one flag and no verification of any kind, and its `--ignore-errors` demotes a verification failure to a warning *"including storing images that failed verification"*. `zarf package deploy --verify` defaults to `if-possible`, so an unsigned package deploys quietly. Fail-closed is the whole product here.
2. **Shipment-level evidence.** What crosses is *per-image* signing evidence that rides along because the cosign tag convention happens to live inside the OCI layout. Nothing states what a transfer is *supposed* to contain, who authorised it, or what policy was in force — so **omission and rollback are undetectable by construction**. This is where primitives 4 and 5 become payload: a signed shipment manifest carrying the trust configuration, the `sequence`, `supersedes`, validity window and the authorising identity.
3. **Upstream provenance.** Zarf regenerates SBOMs locally with Syft, so the packager's assertion substitutes for the builder's. Build provenance, SLSA attestations, scan verdicts, VEX and control evidence do not cross at all.
4. **The guard-mediated case**, below, which nothing in open source models.

**What the receiver checks, in order:** schema → shipment-manifest signature against a trust root that travelled *inside* the bundle → `sequence` against the stored high-water mark → per-blob hash equality → per-image signature and VSA. Everything past the first four is additional verification at leisure, so provenance-rich checks degrade gracefully instead of blocking deployment.

#### The guard-mediated case: genuinely unsolved

**What crosses:** a single file through a device that may refuse it, and must not rewrite it.

**The problem, stated exactly:** a diode preserves bytes; a guard enforces content policy and may transform. NCSC guidance *mandates* transformation of complex types and tells you to assume the transformation engine is compromised. Transformation annihilates every digest and therefore every signature. Letting the guard re-sign its output converts an expected compromise into a total provenance bypass.

**The resolution, corrected:** do not let software be transformed. Make it a type the guard can *verify* rather than one it wants to *rewrite* — a flat content-addressed blob store, every file named `blobs/sha256/<hex>`, fixed-length names, plus one small strictly-schema'd signed manifest. Guidance explicitly permits this: transformation "may not be needed where the content format is simple enough to be verified directly".

The word **uncompressed** is deleted from that description, along with "no nesting to recurse into". The payload *is* nested — it is container layers — and claiming otherwise invites an easy rebuttal from anyone who has run `tar tf` on one. What survives is that the *high-assurance* check needs no understanding of the nesting, which requires splitting the work across **two control points**:

1. **A low-side structural inspector.** Expands each blob in a scratch area under explicit recursion and expansion limits. Rejects path escapes, device nodes, FIFOs, sockets, setuid and setgid bits, and capability xattrs. Multi-scans. **Emits only a verdict — never modified bytes.**
2. **A high-assurance control point, kept single-function.** Schema validation plus per-blob `name == sha256(content)`. No parsing of application formats, no unbounded loops, no semantic understanding. Implementable in a few hundred lines or in hardware.

That split works because it separates the risky operation (parsing untrusted content) from the trusted one (comparing hashes), and only the second needs high assurance. The first can be compromised without the far side losing integrity, because it never produces bytes that cross.

**The accreditation argument, with the rhetoric removed:** the defensible version is that **no content-disarm engine has a sanitiser for compiled code**, so transforming a software bundle changes every digest without touching the threat — binary reconstruction achieves 13% soundness (USENIX Security 2024). The earlier "close to zero security benefit" phrasing was overreach and a hostile reviewer will dismantle it, because CDR genuinely does strip unexpected file types, normalise archive structure and detect polyglots. What it cannot do is protect a cluster from a backdoored binary, because the payload is executable by design. The control doing the real work is the evidence chain plus high-side runtime enforcement.

**Iron Bank's `upload_to_cds.py`, scoped to this case only.** It is ~110 lines, it cosign-verifies on the low side and then **discards the signature**, shipping a bare gzipped OCI layout with no manifest, no checksum file, no SBOM and no attestations, with no receiver-side counterpart. Its sibling `upload_to_s3.py` sends the SBOM, scan and VAT directories to a *different* bucket, so artefact and evidence diverge one step before the boundary. And `skopeo copy` is called with neither `--all` nor `--preserve-digests`, so a multi-arch image is reduced to one platform and the signed manifest-list digest does not survive — even if the signature shipped, it would not verify. The repository has **no licence file**, so this is evidence only; never copy the code. What is deleted is the uniqueness claim, not the dissection.

**The delegation to be honest about:** if anything was transformed, or if the high side cannot reach the low side's signing infrastructure, trust terminates at the importer. Say so rather than implying an unbroken chain.

### Transition D — registry → runtime

**What crosses:** an image digest.

**What the receiver checks:** a signature and a VSA. Nothing else. Cheap, local, inside a webhook's time budget.

**Why this is the easy one:** because B and C did the work. If admission control is doing anything expensive, the design has failed upstream.

It is not, however, unbypassable, which this document previously asserted. `failurePolicy: Ignore` on the admission webhook means the gate everything depends on is skipped whenever the webhook is unavailable. See §8.

---

## 4. Two conflicts the research left unresolved, and how they resolve

Reading the streams against each other surfaced two direct contradictions. One resolved as written. The other resolved the wrong way round, and the wrong version was actionable advice, which makes it the most important correction in this document.

### Conflict 1 — OCI referrers are both the right answer and the thing that breaks

The integrity research recommends the OCI referrers API as primary discovery, and makes registry support for it a hard requirement, because the tag-schema fallback is race-prone by the spec's own admission and will silently lose attestations under concurrency.

The air-gap research observes that `GET /v2/<name>/referrers/<digest>` is a live API call, has no file-based equivalent, and is therefore exactly what dies at the boundary.

**Resolution:** referrers for discovery *within* a connected trust domain; and bundle creation must materialise the referrers graph into the fallback tag schema and record the explicit subject→referrer mapping in the shipment manifest. Otherwise the high side holds the signature bytes and cannot find them. Hauler is the published proof this works, and it does it by default rather than on request — which is the same evidence that refuted the gap claim in §3.

So the rule stands: **the registry must support referrers; the bundle must not depend on them.**

### Conflict 2 — keyless signing was recommended and declared impossible. The "impossible" half was wrong

What this document used to say: *keyless within a trust domain, long-lived HSM keys across trust domains*, reasoning that a Fulcio certificate is valid for about ten minutes and a high side that cannot reach Rekor cannot prove the signature was made inside that window.

**That inverts the thing Sigstore exists to do.** The signature is timestamped and the verifier checks the timestamp falls inside the certificate's validity window; the proof travels in the bundle as a transparency-log inclusion proof and signed checkpoint, or an RFC 3161 timestamp. The client specification states the goal outright: *"we decouple the payload lifetime from the certificate lifetime."*

The verifier tested it rather than reasoning about it. A bundle whose leaf certificate was valid for ten minutes on 28 July 2026, carrying no RFC 3161 timestamps and no long-lived key, **verified offline two months after expiry** with all egress forced through a dead proxy. Corrupting one byte of the inclusion proof's root hash made it fail, confirming the Merkle proof is load-bearing rather than decorative.

**The corrected rule:**

- **Inside a trust domain, keyless is right and is configuration-only.** Fulcio has a first-class `spiffe` issuer type with a validated trust-domain field, so SPIRE→Fulcio in a disconnected enclave needs no code changes.
- **Across a boundary, keyless still works — provided the bundle carries its own verification material.** Inclusion proof, signed checkpoint, trusted root. That is a bundle-construction requirement, which is to say it is primitive 4 doing its job, not a key-management requirement.
- **A long-lived hardware key is a legitimate accreditation choice and never a cryptographic necessity.** If an accreditor wants an HSM-held key at the importer, that is a defensible answer to a policy question. Do not claim you need one because keyless cannot cross, because it can, and someone will demonstrate it in front of you.

The production DoD pipeline doing key-based cross-IL re-signing (`use_alt_key`, documented inline as "useful during re-signing or cross IL") is evidence of what a real programme chose, not evidence that the alternative is impossible.

---

## 5. What this makes of "Kubernetes only, calling out to other systems"

The deployment research recommended capability CRDs where the core reads only `status`. The air-gap research said the diode contract should be "a signed OCI-layout filesystem drop, and the factory must never know the diode exists". The AI research said the inference slot is a gateway endpoint plus a capability descriptor, identical in every tier.

Put together, the off-cluster question stops being a special case:

**Everything outside the cluster is a slot whose implementation happens to live elsewhere, and whose descriptor declares a lower assurance tier.**

The pattern generalises from the research's own `ExternalBuilder` sketch: a pull-based agent polls an in-cluster queue, does work the cluster cannot do, and returns attestations marked `agent-signed` rather than `platform-signed`. The core never learns where the work happened. The *assurance difference* is recorded in the attestation and enforceable by policy — so a gate can require `platform-signed` provenance for a production promotion while accepting `agent-signed` for a development build, and that distinction is machine-checkable rather than a footnote.

The things that are genuinely off-cluster, each via that same contract:

- **HSM and root keys** — PKCS#11; the cluster holds a client credential, never a key. SoftHSM behind the identical interface for development. Note from §4 that this is now an accreditation choice rather than a cryptographic necessity.
- **The diode or guard** — a filesystem drop of the signed bundle. One-way, no callback, no awareness.
- **Non-containerisable builds** — Windows, macOS and iOS signing, FPGA, hardware-in-the-loop rigs. Pull-based agent, `agent-signed`, documented as weaker than an in-cluster L3 build.
- **GPU inference** — in-cluster via device plugin where the estate allows; otherwise an endpoint behind the gateway. The slot contract is identical either way, which is the whole point of the AI seam. It is also the line item with no price against it (§8).
- **Identity** — OIDC only, never LDAP.
- **Long-term artefact storage** — S3 API.

One consequence worth stating plainly because it is a procurement gate rather than an engineering choice, and it is **verified** against RKE2's own documentation: the page is titled "FIPS **140-2** Enablement", not 140-3. It achieves it by compiling with the `dev.boringcrypto` Go branch against the BoringCrypto module (NIST CMVP certificate 4407). And on the CNI, verbatim: *"RKE2 supports selecting a different CNI via the `--cni` flag and comes bundled with several CNIs including Canal (default), Calico, Cilium, and Multus. **Of these, only Canal (the default) is rebuilt for FIPS compliance.**"*

So choosing Cilium — which is otherwise the better network-policy answer — breaks the FIPS claim, and the claim is 140-2 regardless. Build a cryptographic inventory and establish the accreditor's position on 140-2 versus 140-3 before anything customer-facing mentions FIPS at all. That inventory is also where the signing-algorithm question in §8 has to be answered.

---

## 6. The spine, in one page

```
  Intent ──────────────────────────────────────────────────────────────┐
     │                                                                │
  [A] author → source of record                                       │
     │  crosses: diff + authorship declaration                        │
     │  signs:   harness identity (AI-authorship predicate)           │
     │  checks:  human DCO sign-off; Assisted-by; Unicode/invisible-   │
     │           character detection; agents MUST NOT sign off        │
     │  NOTE:    the only hand-off with NO signed artefact in open     │
     │           source — and the integrity boundary under AI          │
     │                                                                │
     │  [A′] agent → agent: DON'T. Agents are leaves.                  │
     │       attribution laundering; false independence                │
     ▼                                                                │
  Source of record ── reviewed commit, policy stated as an outcome    │
     │                                                                │
     ▼                                                                │
  Build ── ephemeral executor, hermetic prefetch, signing key the      │
     │     build cannot reach                                         │
     │  emits: provenance (platform key), SBOM (platform key, signed) │
     ▼                                                                │
  Evidence ── scan (scanner key), VEX (issuer key, mutable),           │
     │        test results (test key); all bound by subject[].digest; │
     │        discoverable via OCI referrers                          │
     │                                                                │
  [B] build → judgement                                               │
     │  checks: signer matches document type; externalParameters       │
     │          allowlisted; trusted-task membership                  │
     ▼                                                                │
  Judgement ── gate key signs a VSA recording the POLICY DIGEST,       │
     │         and the MODEL + CAPABILITY-DESCRIPTOR DIGEST where      │
     │         AI was involved; waivers expire by construction         │
     ├────────────────────────────┬───────────────────────────────────┤
     │ connected tier             │ disconnected tier                 │
     ▼                            ▼                                   │
  [D] admission                [C] low → high                         │
   verify sig + VSA only         standard OCI layout (evidence ALREADY │
   nothing expensive             crosses) + one signed SHIPMENT         │
   failurePolicy: OPEN QUESTION  MANIFEST; fail-closed receiver gate;   │
     │                           trust config travels INSIDE;          │
     │                           monotonic sequence vs high-water mark │
     │                           (security state — survives restore);  │
     │                           guard case: 2 control points —        │
     │                           low-side inspector emits a VERDICT    │
     │                           only; high-assurance = schema +       │
     │                           name == sha256(content)               │
     │                              │                                 │
     │                              ▼                                 │
     │                           [D] high-side admission               │
     │                            verify sig + VSA only                │
     ▼                              ▼                                 │
  Runtime ◄───────────────────────────────────────────────────────────┘

  Every arrow carries: a digest-bound statement (primitive 1).
  Two arrows issue:    a delegated verdict (primitive 2) — [B] and [C].
  Every box publishes: a capability descriptor (primitive 3), measured.
  Every verification:  consults trust configuration (4) and freshness
                       and monotonicity state (5). Ambient when
                       connected; payload when not.
```

---

## 7. What to build, and what the evidence says to adopt

The prior-art research was blunt that the gap is narrow and most of the stack should be adopted rather than written. Holding to that.

**Adopt:** the CNCF Secure Software Factory reference architecture as the conceptual spine (check its licence; unmaintained since 2022). Syft and Grype or Trivy. cosign with offline verification as the designed-for case, or Notation where the enclave has a PKI — its trust-policy model with a per-scope `audit` level is better thought out than anything in cosign, and `audit` is the mode every rollout needs. Tekton with Chains. Conforma for attestation policy, and steal its `volatile_config` waiver design wholesale, because waivers that expire by construction and warn before expiry are the only version of break-glass that survives contact. Zarf for bundling and Hauler for the OCI-layout haul. Kyverno for the thin admission check. apko and melange for base images, because fixing the base image *removes* vulnerability findings rather than suppressing them, and that is what keeps a gate switched on. Hermeto for hermetic prefetch — hermeticity and SBOM quality turn out to be the same problem wearing two hats. `kubernetes-sigs/agent-sandbox` with gVisor for agent workspaces. Coder's `code-marketplace` for a curated, digest-pinned extension inventory, because mirroring a public registry wholesale is both legally barred and, after GlassWorm, unwise.

The strongest consensus in the field is *don't build your own platform* — said by a consultancy that bills for building things, by a vendor that sells one, and by DoD's own guidance. That third source carries **Distribution Statement C**, so it cannot be quoted publicly; the point stands on the two commercial sources, which disagree with each other about almost everything else.

**Build, because it genuinely does not exist:**

1. **The fail-closed receiver-side gate, over a signed shipment manifest.** This is the flagship, and it is a different thing from what this document used to claim. Not a transfer format — a *verification obligation*. It states what a transfer should contain, who authorised it, what policy was in force, and what sequence number it carries, and it refuses rather than warns. The receiver-held high-water mark is security state, not cache.
2. **A signed VEX predicate.** There is no registered in-toto predicate type for VEX, verified against the full predicates directory, so every implementation mints its own, and `openvex/spec` has been frozen since 2023-08-22. `openvex/vexflow` has the right design — a maintainer's structured comment becomes a Sigstore-signed in-toto OpenVEX attestation, authorised against a code-owners file — but it is **v0.0.1, 10 stars, one maintainer, self-described experimental**. An earlier version of this list said that removed the item. It does not: adopting it means owning it. **Take the design as a head start; budget for the implementation.**
3. **An AI-authorship predicate**, with the capability-descriptor digest and the harness credential and egress posture in it.
4. **The unified capability descriptor** shared by inference slots, build slots and transfer slots, carrying measured scores. The eval-result attestation extends the registered `test-result/v0.1` rather than minting a new type; the same applies to `runtime-trace/v0.1` and `svr/v0.2`. **Extend the three registered predicates; mint only what genuinely has no type.**
5. **An SBOM degeneracy detector.** 52.9% of 78,000 real SBOMs declare **no dependency edges at all**, and adding a degeneracy check moved KEV recall from 0.600 to 0.950. Cheap, mechanical, large effect, and it attacks the thing an SBOM gate actually fails on rather than the thing people assume it fails on.
6. **Continuous control evidence — outcome, not serialisation.** The old item 5 here read "continuously generated OSCAL". That is deleted, and so is the "untouched for three and a half years" claim it rested on.

On both of those, plainly, because the correction is the valuable part. The flagship DoD platform's OSCAL component definition has **6 commits ever**; the last substantive edit was **April 2023**; the later commits are a URL fix and a global departmental find-and-replace, so mechanical sweeps make it *look* maintained while its own metadata still claims 2022. It fails `compliance-trestle` with ten duplicated UUIDs, uncatchable because the OSCAL component-definition model has **no referential-integrity constraint** and the standard validator short-circuits to `true`. The sharper story is the gate, with dates: **built Feb 2024, disabled Aug 2024 ("known issues"), deleted Sep 2025**, and replaced with a markdown table.

And OSCAL is an ecosystem graveyard, not a lonely failure. One project deleted its OSCAL saying *"OSCAL proved too complex… automated tests alone were insufficient"*; a government automation repo is 404; two vendors migrated away; a third archived both attempts; the next major version has no active work; and OSCAL has **zero occurrences across all eight cached DoD primary documents** — it is not even demanded. So: **never pitch "we generate OSCAL". Pitch the outcome and keep the serialisation swappable** — this project's founding principle applied to itself.

### The thesis, in its surviving form

This document used to assert that *policy demands machine-verifiable evidence while implementations fail to deliver it.* The primaries do not support that, and the half-sentence that carried it does not exist. Specifically:

- the cATO memo's "**all** security controls will need to be fed into a system level dashboard view" became "**which** security controls" in the 2024 Evaluation Criteria;
- those criteria accept "**screen shots of control gate output as displayed in a dashboard**" as evidence, so a PNG meets the requirement;
- "Automate security control configurations and validation" is an **Objective**, not a threshold requirement — optional;
- the memo licenses manual controls outright: "Manual controls will have different timelines associated";
- the Implementation Guide describes the method as a shift to "a periodic assessment".

**The correct statement: policy demands continuous evidence and names the pipeline as its source, but specifies no machine-verifiable form — and that gap is where the stale document returns.** Weaker, and it is the version that survives someone reading the documents in front of you.

Public support for it, verbatim from the DoD Software Modernization Strategy: *"It couples this validation with automation to produce real-time and continuous evidence… identify **pipeline and process-generated evidence** that verifies appropriate protections are in place"*. And the best single piece of supporting evidence found, a DoD practitioner quoted in a DoD CIO publication: *"The RMF process was going to be the bottleneck. We looked at the NIST 853 controls and identified 100 controls that were required at the application layer. **We baked those into our pipeline for automated control and testing.** Then we **continuously monitor** and make sure the controls stay up to date."*

Two further corrections that bear on how this is pitched. **cATO authorises systems, not organisations, and it modifies how you keep an authorisation rather than being a route to getting one** — a conventional ATO is a prerequisite, approval was still at DoD CISO level department-wide 27 months after the memo, and "organizations don't have to provide metrics for cATO effectiveness", so it is unmeasured by design. And **Runtime/Deployed SBOM tooling is thin, not absent**: a Deployed-type Kubernetes operator exists at a few hundred stars, and the underlying research marked this a weak negative on a narrow search. Do not claim an absence there.

The remaining distinguishing claim is narrower than the old one and still worth making: **evidence is a first-class artefact with its own freshness and verification gates, so staleness is detectable rather than an accreditation surprise.** Note that this is a cost imposed on one party for a benefit accruing to another — see §8, immediately.

---

## 8. The questions nobody asked, as open design obligations

Three independent critics audited the programme. Their consistent verdict: strong on formats, mechanisms and failure history; **close to silent on running the thing and selling it.** This section states their blocking findings as design obligations with the evidence for why they matter. The architecture has **no answer** to most of them. Saying so is better than inventing one, and every item here is cheap now and expensive later.

**There is no buyer, and the thesis is adversarial to the only party with a budget.** Zero occurrences across ~16,000 lines of "design partner", "first customer", "target customer", "beachhead" or "pilot customer". The product is specified by a gap in the artefact landscape rather than by anyone's purchasing decision. Worse: the programme office holds the money and wants an authorisation, and "stale provenance is a build failure" bills exactly that party for a benefit accruing to an assessor, a future maintainer or the taxpayer. The history in this corpus says what happens next — the first software factory failed in 1978 because *"middle management were not required by top management to use the Software Factory, leading to a decline in the flow of work."* **Obligation: name a first customer, and state which of their costs the factory reduces in the first quarter.**

**There is no operating model.** Nobody has established who runs the factory in a customer environment, who is on call, or who funds year two. This is not an implementation detail: it decides whether this is a **product** (upgrade paths, multi-tenancy, a support boundary) or a **consulting engagement** (none of those, and it should not pay for them), and those are different architectures. It is also the variable the project's own evidence ranks first. Funding-and-staffing mismatch is the best-evidenced failure mode in the corpus, on the record from the first commander of the most-cited modern factory, and RAND finds current defence software factories are mostly **customer-funded** — SDC's 1978 failure mode encoded in the budget line. Keyword counts across both design documents: **zero** for fund/funding, operator, operate, turnover, on-call, day-two. **Obligation: pick product or engagement, in writing, before the next architectural decision.**

**There is no cost model in money.** The factory is sized in CPU, RAM and disk only. No figure per enclave, per tenant, per year, and **no price for the GPU estate**, which plausibly dominates everything else and scales per enclave. The claim that eight high-end GPUs buy near-frontier capability is well evidenced technically and entirely unpriced commercially. **Obligation: a per-enclave annual figure with the GPU line itemised, even if it is wrong by a factor of two.**

**The signing-algorithm question was never asked.** Zero mentions of CNSA, CNSSP-15, SP 800-208, LMS, XMSS or crypto-agility anywhere in the research — against primitive 1, which this document calls "catastrophic to reverse". A programme about to start issuing long-lived signatures for defence customers, which has not asked whether those customers mandate particular algorithms or a post-quantum migration path, has its largest gap exactly where it has declared reversal impossible. **Obligation: answer it alongside the FIPS cryptographic inventory in §5, because it is the same conversation with the same accreditor.**

**Backup and restore silently defeat primitive 5.** A correctness defect, not a coverage gap, and it only appears when you read the transfer design against operations. The receiver's monotonic high-water mark is the only defence against rollback and omission across a one-way boundary. **Restoring the high side from backup resets it.** An attacker who can trigger or simply wait for a restore then replays an older, validly-signed bundle, and every cryptographic check passes. **Obligation: the high-water mark is security state with its own integrity protection and explicit restore semantics — never cache. Small amount of work; belongs in the design before the first implementation rather than after the first incident.**

**`failurePolicy: Ignore` switches off the gate the whole architecture routes through.** No hits anywhere in the research for `failurePolicy`, "fail-closed", "policy test" or "attestation coverage". Transition D is the single cheap check that everything upstream relies on, and nobody specified what happens when the webhook is unavailable. Given this programme's own argument that a gate which gets switched off is worth less than no gate, a gate that switches *itself* off under load deserves an answer. **Obligation: specify the failure mode explicitly, with the availability engineering that makes fail-closed survivable, because fail-closed on an unavailable webhook stops deployments.**

**Multi-tenancy is mandated with no acceptance criterion.** The interface is CRDs plus an admission webhook; if two projects share a cluster they cannot hold different slot versions or different gate policies enforced by separate webhooks, and a tenant able to edit a custom resource may be able to weaken its own gate — which collides with the one hard design constraint from practice, *"developers have access to this Jenkinsfile"*: the gate must live where the tenant cannot edit it. The doctrine is no help and the correction here matters: the October 2024 document carries the *strongest* language of any version, "It must be designed for multi-tenancy", and **nothing was dropped** (an earlier claim that a 2019 isolation test was quietly removed was wrong in both halves). What is true is that **no document in any version defines a test demonstrating the isolation holds**, which is more damning. Anyone claiming to have met it is self-certifying against nothing. **Obligation: write the test.**

**Nobody has rigorously measured any software factory, and that includes this one.** Four audits find the absence; there is no controlled study, no before/after baseline and no agreed pre-factory ATO baseline at all. DoD's own Carryover items are better evidence than any external audit: "Establish software factory criteria and metrics", "Collect cost data on agile software programs", "Publish SBOM Implementation Guidance for DoD", "Pilot cATO process and issue cATO". Measurement absence was the critics' second-ranked failure mode. **Obligation: define the factory's own metrics before claiming benefit — and position around the absence of measurement rather than around claimed benefit.** Two claims that were half-invented have been retracted outright and must not reappear: "over 50 software factories, only a few delivering real outcomes" (the real sentence is the opposite in tone, and the pejorative clause appears nowhere) and "most don't track whether the software worked" (not in the document). Never attribute a composite sentence to a document nobody has opened.

**The platform costs throughput before it pays, and mandate makes it worse.** DORA 2024: internal developer platform users show **−8% throughput and −14% change stability**; mandated exclusive use costs a further **−6%**; developer independence is +5%; platform engineering follows a J-curve. DORA's prescription is that a platform must let users *"break out"*. A mandated air-gapped platform sits in the worst cell of that table. **Obligation: predict the dip publicly and design a break-out path, because a programme that does not gets cancelled in the dip.**

**The swappable-slots ambition sits in the band where reuse is worthless or harmful.** Toshiba's step function: reuse pays above 80% unchanged, does nothing between 20% and 80%, and is **net harmful below 20%**. A slot abstraction whose value proposition is that every environment picks a different implementation is, by construction, in the dead band — *unless the thing reused unchanged is the **contract** while implementations vary beneath it.* That is the defensible reading and it is what the design intends, but it has never been stated against the Toshiba finding until now, and it has only been validated against the easiest case. **Obligation: track the modification rate of shared assets.** A slot contract every programme forks by 40% is worse than no shared asset. This is also why the scope decision holds: assurance substrate = **platform** (mandatory, minimal, consumed verbatim); accredited deployment patterns = **a genuine product line**; application architecture = **explicitly out of scope**, because that is where SDC (1978) and Microsoft Software Factories (2008) both died.

**The name is wrong and no decision has been taken.** "Software factory" returns **one GOV.UK hit** — an employment tribunal — against 321 for "secure by design", and the civilian world has settled on platform engineering. Zero hits across the research for "rename" or "what to call it". **Obligation: take the decision.** It costs nothing now and it is embarrassing to take later.

---

## 9. Open questions that block design, in order

1. **What will a real guard actually accept?** Maximum single-file size; maximum object count; whether a flat tar of content-addressed blobs reads as a "simple, verifiable" type or as an archive requiring recursive expansion; whether a hash-only validation policy is acceptable in lieu of semantic inspection; sustained throughput and transfer cadence; whether any high-to-low acknowledgement is permissible at all. **Six of those seven are unanswerable from public sources** — NCDSMO Raise the Bar, the Cross Domain Baseline List and the LBSA methodology are controlled. The *two-control-point structure* in §3 survives not knowing the answers; the specific encoding does not. So no more design effort on the format. It is a cleared conversation, not a research task.
2. ~~Is RKE2 FIPS 140-3 or 140-2?~~ **Answered: 140-2, via BoringCrypto, and only Canal is FIPS-rebuilt.** The remaining question is for an accreditor: is 140-2 acceptable, and is losing Cilium acceptable to keep it? Fold the signing-algorithm and post-quantum question from §8 into the same conversation.
3. **Does Harbor replication silently drop legacy-cosign signatures** (issue #20412)? If so, a transport conformance test is mandatory, not optional. Mandating OCI 1.1 referrers mode probably sidesteps it, which is a second independent reason for the §4 rule that the registry must support referrers.
4. **Product or engagement?** From §8. This blocks more design than anything technical on this list, because multi-tenancy, upgrade paths and the support boundary are all downstream of it, and all three are expensive to add late.
5. **Who is the first customer, and what does the factory make cheaper for them in quarter one?** Also from §8. Until this is answered the architecture is being specified by an artefact gap rather than by a requirement, which is how the 1968–2008 attempts were specified too.
