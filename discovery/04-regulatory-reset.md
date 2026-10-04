# The US compliance driver collapsed, and what replaced it is better for us

Verified 2026-10-03 by reading the primary documents, not a summary. This materially changes the compliance story the project was assuming.

## What happened

**OMB M-26-05, "Adopting a Risk-based Approach to Software and Hardware Security"** (January 2026) rescinds the entire US federal software self-attestation regime. Verbatim from the PDF:

> "0MB Memorandum M-22-18, Enhancing the Security of the Software Supply Chain through Secure Software Development Practices (M-22-18), **imposed unproven and burdensome** software accounting processes that prioritized compliance over genuine security…"

> "**M-22-18 and M-23-16, a companion policy, are hereby rescinded.**"

So the CISA Secure Software Development Attestation Form regime — which was the single most-cited driver for "you need a software factory to produce attestations" — is gone. Self-attestation is now optional.

Separately, **EO 14306** (11 June 2025, *"Sustaining Select Efforts To Strengthen the Nation's Cybersecurity and Amending Executive Order 13694 and Executive Order 14144"*) exists and amends EO 14144. The research reports it struck §2(b) — the machine-readable attestation repository, CISA continuous validation, public naming of failures and DOJ referral. The EO's existence and its amendment of 14144 are verified; the specific §2(b) strike is from the research and I have not read that clause myself.

**Do not build a pitch on EO 14028 / M-22-18 / self-attestation.** Anyone in a US federal procurement conversation will know this and the project will look like it did no homework.

## What survived, and why it is better for us

Two obligations remain in M-26-05, and they are *more* aligned with the project's thesis than what they replaced:

> "Agencies shall continue to **maintain a complete inventory of software and hardware**…"

> "…provide **an SBOM of the runtime production environment** upon request."

Read that second one carefully, because it is the find. The surviving requirement is not a build-time SBOM of an artefact. It is an SBOM of **the runtime production environment** — what is actually deployed and running, now.

`research/03` established, independently and before this was known, that almost every SBOM generator produces Source, Build or Analyzed scope against an artefact rather than assembling a current inventory of a running system.

> **CORRECTED 2026-10-04 — the claim that stood here, "Deployed and Runtime SBOMs have no tooling at all", is wrong and must not be repeated. See `00-index.md` 8.3.** **Runtime/Deployed SBOM tooling is thin, not absent:** a Deployed-type Kubernetes operator exists at a few hundred stars, and the underlying research marked this a **weak negative on a narrow search**. Claim immaturity, and go and measure it. Do not claim an absence — and note the standing rule (0.2) that no document here may assert a universal negative over open code.

So the one US obligation that survived a deregulatory purge is the one the tooling ecosystem serves worst. That is a better gap than the one we started with, and it is not defence-specific. **Before committing to build anything here, assess the Deployed-type operator that already exists.**

## The pattern this confirms

Both M-26-05's framing and FedRAMP's direction point the same way: away from documents produced once, toward capability demonstrated continuously.

**FedRAMP 20x KSI-PIY-GIV, verified verbatim** from `github.com/FedRAMP/rules`, `fedramp-consolidated-rules.json`:

> `"KSI-PIY-GIV": { "name": "Generating Inventories", "statement": "Authoritative sources are used to automatically generate real-time inventories of all information resources when needed." }`

"Automatically generate real-time inventories." Not "maintain documentation of". The research also notes FedRAMP 20x never mentions SBOM at all — it asks for the capability an SBOM is a snapshot of.

This is the strongest regulatory support the project's thesis has, and it was found in machine-readable form in a public git repository, which is itself the point.

## The gap, restated in regulatory terms

The research surveyed twelve regimes and found the obligations are overwhelmingly **continuous** — MOD ISN 2023/09 §25 ("risk analysis should be continuous… projects **must be able to evidence this**") and §46 ("must continuously reassess"); DORA Art. 8 ("on a continuous basis", "every time any major change occurs"); FDA ("regularly updated… on a continuous basis"); PCI DSS 12.5.1 ("kept current"); DEFSTAN 05-138 control 1301 ("automated discovery and management tools to maintain an up-to-date, complete, accurate, and readily available inventory").

But **verification is episodic and manual.** PCI DSS tests its own requirement by "examine documentation and interview personnel". CMMC's affirmation is a signature. MOD's CAAT tool is a self-assessment questionnaire.

**Obligations are continuous; verification is episodic. That space is the product.** It is the same thesis as the diode envelope and the stale OSCAL file, arriving from a third direction.

## Consolidation: twelve regimes, three machine artefacts

The deduplication is the useful output. Across twelve regimes the machine-readable asks reduce to three:

- **A. A current component inventory.** Called SBOM, inventory of system components, automated asset inventory, real-time inventory, RXSWIN auditable register, or DO-178C Software Configuration Index depending on the regime. Twelve regimes, one artefact. *Serialising it is cheap; generating it authoritatively, currently and transitively complete is the product.*
- **B. Build-and-release provenance.** Fourteen references across the corpus.
- **C. A vulnerability-and-remediation ledger.** Thirteen references.

Plus two that do not automate: a risk/threat narrative (the factory supplies inputs and change triggers, not the prose), and the accountable human signature (MOD Statement of Assurance, CMMC affirmation, CRA Declaration of Conformity). No regime pretends the signature automates away — which is the same conclusion `design/02` reached from the AI direction.

One line: *five regulations asking five things are asking what is in it, where it came from, and what is wrong with it — plus a risk story and a signature.*

## Corrections to things the project believed

- **SLSA, in-toto and Sigstore appear in zero regulatory texts.** Searched across CISA's 2026 minimum elements, SP 800-218, the CISA attestation form, M-26-05, DEFSTAN 05-138, the DSIT Code of Practice and ISN 2023/09. **You can comply *via* SLSA; you can never comply *by* it.** Never pitch SLSA level as a compliance outcome.
- **The CRA SBOM is not a customer deliverable.** Annex I Pt II(1) requires it be drawn up machine-readably covering "at the very least the top-level dependencies"; Annex VII(8) discloses it only "further to a reasoned request from a market surveillance authority"; a recital states "Manufacturers should not be obliged to make the SBOM public."
- **UK MOD terminology, corrected.** It is a **risk register**, not a "risk ledger". There is no "Secure by Design Assurance Portal" — the tool is **CAAT (Cyber Activity and Assurance Tracker)**, which replaced DART, is a **self-assessment**, is **MOD-personnel-only**, and is **OFFICIAL-only with SECRET "available soon"**. The binding instrument on industry is **ISN 2023/09**. MOD states flatly that the Statement of Assurance "is not a replacement for accreditation or a certificate".
- **DEFSTAN 05-138 has zero hits for SBOM, SPDX or CycloneDX.** Pitch to UK defence in **control numbers** (1301, 2423 — both of which demand *automated* inventory tooling), not in SBOM vocabulary.
- **No regime anywhere imposes requirements on AI-generated code in assured software.** Confirms `design/02` §6: recording model identity per diff is cheap insurance against a rule that does not yet exist, not a current compliance need.

## The flagged gap worth the most to us

The research found that **no UK or other policy addresses handling assurance evidence across classification boundaries** — and MOD's own tooling admits the problem by being OFFICIAL-only with SECRET pending.

Least prior art, most defence-specific value, and it is the same problem as the transfer envelope. The accreditation regime has no answer for how its own evidence crosses the boundary it mandates.

## Dates to have to hand

CMMC phases: 10 Nov 2025 / 2026 / 2027 / 2028 (full). CRA: Ch. IV 11 Jun 2026, Art. 14 reporting 11 Sep 2026, general application 11 Dec 2027. UK CS&R (NIS) Bill at Lords Report stage, sitting 26 Oct 2026.

One CRA detail with direct product relevance: **the 14-day vulnerability final-report clock starts on your own fix release.** Near-impossible to hit manually, straightforward to automate from a pipeline.
