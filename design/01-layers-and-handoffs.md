# Layers, hand-offs, and the three primitives

Synthesis over `research/02`–`06`. Written 2026-10-03, before the outcomes research landed, so the outcome list may add requirements — but the structure below is derived from mechanism rather than from requirements, so it should survive.

The point of this document is to answer one question: **when work passes from one layer of the factory to the next, what exactly crosses, who vouches for it, and what does the receiver check?** Get that right and the component choices become almost arbitrary, which is the whole premise.

---

## 1. The thing the research actually converged on

Five research streams ran independently on different questions. They arrived at the same mechanism, which is the strongest signal in the whole exercise.

**Supply-chain integrity** concluded: wrap everything in DSSE → in-toto Statement, bind by `subject[].digest`, and have the pipeline gate issue a signed Verification Summary Attestation so admission control reads one cheap boolean instead of re-verifying ten documents.

**Air-gap transfer** concluded: sign a small, strictly-schema'd manifest that commits to a large payload by hash, so the verifier's whole job is schema validation plus `name == sha256(content)`. It noted this is a rediscovery of Debian's `InRelease`, OSTree's signed summary and Zarf's `aggregateChecksum`.

**Deployment and composition** concluded: slots must be Kubernetes CRDs the project owns, the core must read only `status` and never `spec`, and `status` must carry capability flags so the core degrades rather than crashes.

**The AI layer** concluded: the slot implementation publishes a machine-readable capability descriptor listing `outcomes_enabled`, and a policy gate can refuse a provenance claim from a slot that never advertised that outcome.

Four different problems. One shape. Strip the domain language and there are exactly three primitives, and every hand-off in the factory is built from them:

### Primitive 1 — the digest-bound statement

A small signed document that commits to a large thing by cryptographic hash, carrying a declared type.

Concretely: DSSE envelope, `payloadType`, in-toto Statement v1, `predicateType` URI, `subject[].digest`. The signature covers `PAE(payloadType, body)`, never the raw payload.

This is non-negotiable and it is the one choice that is catastrophic to reverse — every signature ever issued is over that encoding. Where no registered predicate exists (OpenVEX, AI authorship, policy config, transfer manifests), mint a predicate type in a namespace we control and keep the envelope standard. **A non-standard predicate inside a standard envelope costs a little, locally. A non-standard envelope costs everything, permanently.**

### Primitive 2 — the delegated verdict

An accountable party performs an expensive verification once and issues a cheap signed boolean that downstream parties trust instead of repeating the work.

The research found this independently in two places and did not notice they were the same thing:

- **The VSA.** The pipeline gate evaluates provenance shape, SBOM quality, scan results, hermeticity and trusted-task membership, then signs a verdict. Admission control verifies the verdict and nothing else. The research is emphatic that rich policy at admission time is how you take a cluster down.
- **The trusted importer.** A gated low-side release authority verifies the upstream chain and signs its own attestation of what crossed the boundary. The high side's trust terminates at the importer rather than the original builder.

These are one pattern: *verify expensively where you can, assert cheaply where you must, and name the party whose signature you are now trusting.* Recognising them as one pattern means one implementation, one key-management story, one audit format, and one honest sentence in the architecture document about where the chain delegates.

The two rules that make it safe, both from the SLSA spec and both routinely violated: the verdict records the **digest of the policy** that was applied, so a policy change detectably invalidates prior verdicts; and consumers accept only specific **(signer, verifier) pairs**, so a compromised build cannot issue its own passing verdict. If one key signs both the build provenance and the verdict, the verdict is worthless.

### Primitive 3 — the capability descriptor

The implementation declares, in machine-readable form, which outcomes it can actually deliver. The core reads it and turns features off.

The AI research invented this for inference tiers (`outcomes_enabled: [autocomplete, review, test-gen]`). The deployment research invented it for slot CRDs (`status.implementation`, `status.invocation`, `supportedFormats`, `fipsMode`, `slsaSourceLevel`). **These should be the same object.** One descriptor shape, published by every slot implementation, consumed by the core and by the gates.

The reason this matters more than it looks: it is how *degradation becomes a design decision rather than a production surprise*. A factory that says "in this enclave, autonomous multi-file change is disabled, here is the measurement that justifies it" is more credible to an accreditor than one claiming uniform capability that quietly flakes. And because the descriptor is digest-referenced from the attestations (see §4), a gate can verify after the fact that the slot which produced an artefact had advertised the outcome it was used for.

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

---

## 3. The four trust-domain transitions

Most layer boundaries are ordinary function calls. Four of them are trust-domain transitions, where the receiver cannot verify what the sender did by inspection and must rely on a signature. These four are the entire architecture. Everything else is plumbing.

### Transition A — author → source of record

**What crosses:** a diff, plus a declaration of how it was made.

**The problem:** if an agent wrote it, the factory needs to know that later, and no standard exists for saying so. The Linux kernel is the only serious precedent and it is a good one: `Assisted-by: LLM <tools>` as a git trailer, scrutiny proportional to how much was generated, and the hard rule that **agents must not add `Signed-off-by` because only a human can certify the DCO.**

**What the receiver checks:** a human in the DCO chain has signed off; the `Assisted-by` trailer is present when generation was material; mechanical checks that human review cannot perform have run — specifically Unicode normalisation and invisible-character detection, because GlassWorm demonstrated that malicious code can be invisible in every diff view, which makes human review an accountability control rather than a detection control.

**The attestation to mint:** an AI-authorship predicate over the diff digest, signed by the harness identity, carrying model identity, model licence, tier, and the digest of the capability descriptor that was in force. No regime currently requires this. The forward risk is asymmetric: if a future regime does require authorship disclosure, a factory that recorded nothing cannot retrofit it, and recording it costs almost nothing now.

### Transition B — build → judgement

**What crosses:** an artefact digest plus an evidence set.

**The problem:** the evidence is produced by several parties with different trustworthiness, and the gate must not confuse them. Build platform signs provenance and the SBOM; the scanner signs scan results; the VEX issuer signs VEX; the gate itself signs the verdict. Separate identities, decided once, painful to retrofit.

**What the receiver checks:** every document binds to the artefact by `subject[].digest`; the signer of each is the expected signer for that document type; `externalParameters` are allowlisted rather than denylisted, because SLSA says verifiers should reject unrecognised fields there; and the build's task references match a pre-approved trusted-task list. That last check — *provenance that the build only ran steps we approved* — is the highest-value rule in the set and the one most factories omit.

**The output:** a VSA. From here on, nothing re-reads the evidence set in the hot path.

**What the research says we must fix:** the best open implementation in existence ships its build SBOM **unsigned**, by its own documented admission. Since an author signature is now a CISA minimum element, that is simultaneously a security gap and a compliance gap, and closing it is probably the highest-value, lowest-effort differentiator available.

### Transition C — low side → high side

**What crosses:** a single file through a guard that may refuse it, and must not rewrite it.

**The problem, stated exactly:** a diode preserves bytes; a guard enforces content policy and may transform. NCSC guidance *mandates* transformation of complex types and tells you to assume the transformation engine is compromised. Transformation annihilates every digest and therefore every signature.

**The resolution, which is the sharpest finding in the research:** do not let software be transformed. Make it a type the guard can *verify* rather than one it wants to *rewrite*. Ship a flat, uncompressed, content-addressed blob store — every file named `blobs/sha256/<hex>`, fixed-length names, no nesting to recurse into, no archive headers — plus one small strictly-schema'd signed manifest. The guard's entire job becomes schema validation plus confirming each blob's name equals its own hash. That is a *complete* integrity check implementable in a few hundred lines or in hardware, and it requires no understanding of OCI, Helm or ELF.

The accreditation argument that goes with it, and it is a strong one: **content-disarm-and-reconstruct cannot meaningfully disarm a container image, because the payload is executable code by design.** CDR protects document viewers from documents. Applying it to software destroys verifiability while delivering close to zero security benefit. The real control is the factory's attestations plus high-side runtime controls — which is what the evidence set is for.

**What the receiver checks:** schema; manifest signature against a trust root that travelled *inside* the bundle; a strictly monotonic `sequence` per `(producer, destination)` pair against a stored high-water mark, which is the only available defence against replay and rollback when you cannot ask anything; then per-blob hash equality. Evidence in the bundle is additional verification at leisure, so provenance-rich checks degrade gracefully instead of blocking deployment.

**The delegation to be honest about:** if anything was transformed, or if the high side cannot reach the low side's signing infrastructure, trust terminates at the importer. Say so in the architecture document rather than implying an unbroken chain.

### Transition D — registry → runtime

**What crosses:** an image digest.

**What the receiver checks:** a signature and a VSA. Nothing else. Cheap, local, unbypassable, inside a webhook's time budget.

**Why this is the easy one:** because B and C did the work. If admission control is doing anything expensive, the design has failed upstream.

---

## 4. Two conflicts the research left unresolved, and how they resolve

Reading the streams against each other surfaced two direct contradictions. Both resolve cleanly, and neither document states the resolution.

### Conflict 1 — OCI referrers are both the right answer and the thing that breaks

The integrity research recommends the OCI referrers API as primary discovery, and makes registry support for it a hard requirement, because the tag-schema fallback is race-prone by the spec's own admission and will silently lose attestations under concurrency.

The air-gap research observes that `GET /v2/<name>/referrers/<digest>` is a live API call, has no file-based equivalent, and is therefore exactly what dies at the boundary.

**Resolution:** referrers for discovery *within* a connected trust domain; and bundle creation **must materialise the referrers graph into the fallback tag schema and record the explicit subject→referrer mapping in the manifest.** Otherwise the high side holds the signature bytes and cannot find them. Big Bang's Hauler path is the published proof this works — signatures, attestations and SBOMs arrive as ordinary `sha256-<digest>.sig`/`.att`/`.sbom` tags inside a plain OCI layout tarball, and cosign verifies against the internal registry with no reach-back.

So the rule is: **the registry must support referrers; the bundle must not depend on them.**

### Conflict 2 — keyless signing is recommended and impossible

The integrity research recommends keyless where connected, with SPIRE→Fulcio in a disconnected enclave (and establishes this is configuration-only, since Fulcio has a first-class `spiffe` issuer type).

The air-gap research shows keyless forces you back to long-lived keys, because a Fulcio certificate is valid for about ten minutes and the high side cannot reach a Rekor instance to prove the signature was made inside that window. It found a production DoD pipeline doing exactly that — key-based verification, with a `use_alt_key` parameter documented for "re-signing or cross IL".

**Resolution, and this is a clean rule neither document states: keyless within a trust domain, long-lived HSM keys across trust domains.**

SPIRE→Fulcio is correct *inside* the enclave, where the enclave runs its own Fulcio and its own Rekor, and inside the low-side factory for the same reason. But anything whose signature must be verified in a *different* trust domain from the one that produced it must be signed with a long-lived key held in an HSM, with an RFC 3161 timestamp as the transparency substitute — which SLSA explicitly blesses for exactly this case.

That rule also tells you where the importer key lives: in an HSM, used by a gated release authority, never by a transformer and never by a build step.

---

## 5. What this makes of "Kubernetes only, calling out to other systems"

The deployment research recommended capability CRDs where the core reads only `status`. The air-gap research said the diode contract should be "a signed OCI-layout filesystem drop, and the factory must never know the diode exists". The AI research said the inference slot is a gateway endpoint plus a capability descriptor, identical in every tier.

Put together, the off-cluster question stops being a special case:

**Everything outside the cluster is a slot whose implementation happens to live elsewhere, and whose descriptor declares a lower assurance tier.**

The pattern generalises from the research's own `ExternalBuilder` sketch: a pull-based agent polls an in-cluster queue, does work the cluster cannot do, and returns attestations marked `agent-signed` rather than `platform-signed`. The core never learns where the work happened. The *assurance difference* is recorded in the attestation and enforceable by policy — so a gate can require `platform-signed` provenance for a production promotion while accepting `agent-signed` for a development build, and that distinction is machine-checkable rather than a footnote.

The things that are genuinely off-cluster, each via that same contract:

- **HSM and root keys** — PKCS#11; the cluster holds a client credential, never a key. SoftHSM behind the identical interface for development.
- **The diode or guard** — a filesystem drop of the signed bundle. One-way, no callback, no awareness.
- **Non-containerisable builds** — Windows, macOS and iOS signing, FPGA, hardware-in-the-loop rigs. Pull-based agent, `agent-signed`, documented as weaker than an in-cluster L3 build.
- **GPU inference** — in-cluster via device plugin where the estate allows; otherwise an endpoint behind the gateway. The slot contract is identical either way, which is the whole point of the AI seam.
- **Identity** — OIDC only, never LDAP.
- **Long-term artefact storage** — S3 API.

One consequence worth stating plainly because it is a procurement gate rather than an engineering choice, and it is now **verified** against RKE2's own documentation: the page is titled "FIPS **140-2** Enablement", not 140-3. It achieves it by compiling with the `dev.boringcrypto` Go branch against the BoringCrypto module (NIST CMVP certificate 4407). And on the CNI, verbatim: *"RKE2 supports selecting a different CNI via the `--cni` flag and comes bundled with several CNIs including Canal (default), Calico, Cilium, and Multus. **Of these, only Canal (the default) is rebuilt for FIPS compliance.**"*

So choosing Cilium — which is otherwise the better network-policy answer — breaks the FIPS claim, and the claim is 140-2 regardless. Build a cryptographic inventory and establish the accreditor's position on 140-2 versus 140-3 before anything customer-facing mentions FIPS at all.

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
     ▼                                                                │
  Source of record ── reviewed commit, policy stated as an outcome    │
     │                                                                │
     ▼                                                                │
  Build ── ephemeral executor, hermetic prefetch, signing key the      │
     │     build cannot reach                                         │
     │  emits: provenance (platform key), SBOM (platform key, SIGNED) │
     ▼                                                                │
  Evidence ── scan (scanner key), VEX (issuer key, mutable),           │
     │        test results (test key); all bound by subject[].digest; │
     │        discoverable via OCI referrers                          │
     │                                                                │
  [B] build → judgement                                               │
     │  checks: signer matches document type; externalParameters       │
     │          allowlisted; trusted-task membership                  │
     ▼                                                                │
  Judgement ── gate key signs a VSA recording the POLICY DIGEST        │
     │         waivers expire by construction                         │
     ├────────────────────────────┬───────────────────────────────────┤
     │ connected tier             │ disconnected tier                 │
     ▼                            ▼                                   │
  [D] admission                [C] low → high                         │
   verify sig + VSA only         flat content-addressed blobs +        │
   nothing expensive             one small signed manifest;            │
     │                           trust root travels INSIDE;            │
     │                           monotonic sequence per destination;    │
     │                           importer key = HSM, long-lived        │
     │                              │                                 │
     │                              ▼                                 │
     │                           [D] high-side admission               │
     │                            verify sig + VSA only                │
     ▼                              ▼                                 │
  Runtime ◄───────────────────────────────────────────────────────────┘

  Every arrow carries: a digest-bound statement (primitive 1).
  Two arrows issue:    a delegated verdict (primitive 2) — [B] and [C].
  Every box publishes: a capability descriptor (primitive 3).
```

---

## 7. What to build, and what the evidence says to adopt

The prior-art research was blunt that the gap is narrow and most of the stack should be adopted rather than written. Holding to that:

**Adopt:** the CNCF Secure Software Factory reference architecture as the conceptual spine (check its licence; unmaintained since 2022). Syft and Grype or Trivy. cosign with offline verification as the designed-for case, or Notation where the enclave has a PKI — its trust-policy model with a per-scope `audit` level is better thought out than anything in cosign and `audit` is the mode every rollout needs. Tekton with Chains. Conforma for attestation policy, and steal its `volatile_config` waiver design wholesale, because waivers that expire by construction and warn before expiry is the only version of break-glass that survives contact. Zarf for bundling. Kyverno for the thin admission check. apko and melange for base images, because fixing the base image *removes* vulnerability findings rather than suppressing them, and that is what keeps a gate switched on. Hermeto for hermetic prefetch — hermeticity and SBOM quality turn out to be the same problem wearing two hats, which is the strongest argument for doing it. `kubernetes-sigs/agent-sandbox` with gVisor for agent workspaces. Coder's `code-marketplace` for a curated, digest-pinned extension inventory, because mirroring a public registry wholesale is both legally barred and, after GlassWorm, unwise.

**Build, because it genuinely does not exist:**

1. **The transfer envelope and its receiver-side verification path.** This is the flagship. There is exactly one cross-domain implementation in open code, it is ~110 lines, and it throws the signature away.
2. **A signed VEX predicate.** There is no registered in-toto predicate type for VEX, verified against the full predicates directory, so every implementation mints its own. The largest standards gap in the stack.
3. **An AI-authorship predicate**, with the capability-descriptor digest in it.
4. **The unified capability descriptor** shared by inference slots, build slots and transfer slots.
5. **Continuously generated OSCAL**, emitted from the running system rather than hand-written — because the flagship DoD platform's OSCAL component definition has not been touched in three and a half years and roughly 195 chart versions, and that is the evidence an accreditor would most want to trust.

Items 1 and 5 are the same thesis at two different boundaries: evidence decays because nothing fails when it rots. The factory's distinguishing claim is that **evidence is a first-class artefact with its own freshness and verification gates, so stale provenance is a build failure rather than an accreditation surprise.**

---

## 8. Open questions that block design, in order

1. **What will a real guard actually accept?** Maximum single-file size; maximum object count; whether an uncompressed tar of flat content-addressed files is treated as a "simple, verifiable" type or as an archive requiring recursive expansion; whether a hash-only validation policy is acceptable in lieu of semantic inspection; sustained throughput and transfer cadence; whether any high-to-low acknowledgement is permissible at all. **Six of those seven are unanswerable from public sources.** The envelope design is speculative until someone cleared answers them, and no more design effort should go into the format first.
2. ~~Is RKE2 FIPS 140-3 or 140-2?~~ **Answered: 140-2, via BoringCrypto, and only Canal is FIPS-rebuilt.** The remaining question is not technical but a question for an accreditor: is 140-2 acceptable, and is losing Cilium acceptable to keep it? Decide early, because it constrains the network-policy and service-mesh choices.
3. **Does Harbor replication silently drop legacy-cosign signatures** (issue #20412)? If so, a transport conformance test is mandatory, not optional. Mandating OCI 1.1 referrers mode probably sidesteps it, which is a second independent reason for the §4 rule that the registry must support referrers.
4. **What do the outcomes say?** Research still running. It may add obligations — particularly on evidence currency, which is the thesis — and the UK Secure by Design artefact set is the one most likely to reshape the gate design.
