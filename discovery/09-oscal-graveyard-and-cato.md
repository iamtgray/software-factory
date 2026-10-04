# A correction to my own claim, an OSCAL graveyard, and the cATO verdict

From `research/01a-defence-outcomes.md`. Recorded 2026-10-03. This file contains the most uncomfortable findings in the programme, including one error of mine and one serious challenge to a build recommendation.

---

## 1. Correction: I had the OSCAL staleness wrong

I have been saying Big Bang's `oscal-component.yaml` was "untouched for ~3.5 years and ~195 chart versions". **That is not accurate and I should stop saying it.**

I have now pulled the actual commit history myself. **All six commits, verbatim:**

```
2026-08-12  338acdef  Docs: Update relevant DoD terminology to DoW
2023-12-10  21e47636  fix issue with incorrect url format
2023-10-02  2af34f98  Changed repo1.dso.mil/platform-one/big-bang to repo1.dso.mil/big-bang
2023-04-26  dffd02b4  Resolve "Ensure all packages have valid OSCAL documents"
2022-08-02  ad72da73  Update OSCAL schema to get pipeline validation to pass
2022-05-17  1c7e7893  Big Bang Oscal document that's aggregated from components
```

The file **still exists at HEAD**. (The research reported it had been "replaced with a markdown table" — the *file* has not been replaced, so that claim applies to the surrounding documentation at most. Treating it as unverified.)

Read what those commits actually are, because the story is in the messages rather than the dates:

- **2026-08-12** is a sweeping find-and-replace for the department's renaming from DoD to **DoW**. The file was touched *incidentally*, by a global edit, not deliberately.
- **2023-10-02** and **2023-12-10** are URL corrections following a repository path rename.
- **The last substantive change to the content was 2023-04-26.**

So the content *is* roughly three and a half years stale — my original instinct was right — but **the mechanism is different and more damning than simple neglect.** The file is periodically touched by mechanical sweeps that make it *look* maintained in the commit log, while nobody has reviewed its substance since April 2023. Its metadata, meanwhile, claims 2022-06-06, 12 components and `oscal-version: 1.0.4`.

**And the 2022-08-02 commit is the one to quote:** *"Update OSCAL schema to get pipeline validation to pass."* When the validator complained, the response was to change the document until it stopped complaining. That is gate fatigue in a single commit message — two years before they disabled the gate outright.

**It also fails validation.** `compliance-trestle 5.1.0` rejects it: ten duplicated UUIDs, two pairs of components sharing an identity.

And the reason nobody noticed is structural, which is the real finding: **the OSCAL component-definition model has no referential-integrity constraint** (the SSP model does), and `trestle`'s `RefsValidator` short-circuits to `True`. So dangling party and role references are **uncatchable by design**. The format cannot tell you it is broken.

## 2. The thesis, in its purest form, with dates

Big Bang:

1. **Built** live-cluster OSCAL validation — February 2024.
2. **Disabled** the gate — August 2024, reason given: "known issues".
3. **Deleted** it — September 2025.
4. **Replaced the file with a markdown table.**

Someone built the machine that checks the evidence, it produced inconvenient results, the gate was switched off, and eighteen months later the capability was removed. That is "evidence rots because nothing fails when it does" with a commit log attached. Use this, not the staleness claim.

## 3. But OSCAL is a graveyard, and this challenges my build recommendation

I recommended building "continuously generated OSCAL". The research makes that look naive, and I should say so plainly rather than defend it.

- **Defence Unicorns deleted UDS Core's OSCAL** and shipped Lula 2 with the explanation that **"OSCAL proved too complex… automated tests alone were insufficient."**
- **`GSA/fedramp-automation` is 404.**
- **Red Hat and ComplianceAsCode moved to Gemara.** **Cloud Security Alliance moved to STIX 2.1.** **AWS archived both of its attempts.**
- **"OSCAL v2 has no active work."**
- And the finding that should stop anyone: **OSCAL has zero genuine hits across four key DoD documents.** It is not even demanded.

That is not an unoccupied gap. It is **multiple well-resourced, independently-motivated organisations building OSCAL automation and abandoning it**, with at least one stating why. Concluding "we will simply do it better" would be exactly the arrogance the SDC and Microsoft post-mortems warn about.

**The honest reframing, which I think survives:** separate the outcome from the serialisation. The *outcome* — continuous, machine-verifiable control status that an AO can act on — is demanded verbatim by the cATO memo and the Software Modernization Strategy ("pipeline and process-generated evidence"). The *serialisation* is contested, and OSCAL is a failed one. So build to the outcome and keep the format swappable, which is this project's founding principle applied to itself. Watch Gemara, since Red Hat and ComplianceAsCode both moved there and `complyctl` already pulls Gemara policy from an OCI registry — the same transport shape as the transfer envelope.

**Do not put "we generate OSCAL" in a pitch.** Put "we generate continuous control evidence, currently serialised as X".

## 4. cATO: real policy, genuine route, effectively zero holders

The decisive evidence is DoD's own.

- The DoD CIO's **March 2025 *State of DevSecOps*** (with SEI and MITRE) says DoD is **"waiting for DoD Component CISOs to nominate"** software factories, and that nominees **"will become"** the pathfinders. Pre-2022 arrangements are "inconsistent across DoD Components."
- The **FY25–26 Implementation Plan** marks **"Pilot cATO process and issue cATO"** as **Carryover**, and lists "Provide cATO Analytics" as a *future* deliverable — i.e. DoD did not have its own adoption numbers.
- **Evaluation Criteria footnote 1:** approval was still at **DoD CISO level, department-wide, 27 months after the memo.**
- The Army's trajectory: "cATOs by end of summer" (May 2024) → "approve two CI/CD pipelines" (Oct 2024) → **"seven folks in the hopper"** (Feb 2025).

**Two things that are widely misrepresented and that we must not repeat:**

1. **cATO "modifies requirements for re-authorizing".** You need a conventional ATO first. It is not a route *to* authorisation; it is a different way of *keeping* one. Every "18 months to continuous" pitch that implies otherwise is wrong.
2. **By April 2025 the acting DoD CIO said "I'm blowing up the RMF. The RMF is archaic"** and launched **SWFT**, which assesses **the artefact and the supplier** — not the organisation, and not the pipeline.

That last point is strategically significant. If SWFT is the direction, then the unit of assessment moves to the *artefact and its evidence*, which is precisely what a transfer envelope and a signed evidence set are. **The policy drift is toward us, not away.** But it also means betting the project on cATO control inheritance is betting on a mechanism the department's own CIO was publicly disparaging.

## 5. The outcome list — 13 items, from policy rather than opinion

Each has a demander, a proving artefact, and an honest difficulty rating in the source. Compressed:

| | Outcome | Demander |
|---|---|---|
| **O1** | An auditor ties a running container to a reviewed commit **without the build system** | DIB SWAP 2019 "code provenance" — **absent from every DoD compliance document** |
| **O2** | Machine-enumerable inherited / hybrid / owned controls | Reference Design §5.1.1 — **deferred in 2019** |
| **O3** | **The compliance artefact is a build output, not a document** | 2022 Software Modernization Strategy, verbatim: "pipeline and process-generated evidence" — **the keystone, and unsolved** |
| **O4** | Near-real-time control status for an AO | cATO memo — "**all** security controls" into a dashboard |
| **O5** | An independently reproduced SBOM, diffed against the supplier's | SWFT 2025 |
| **O6** | Non-bypassable control gates with auditable blocks | — |
| **O7** | Reconstructible environment, drift detectable | IaC/CaC |
| **O8** | **Multi-tenancy with a demonstrated isolation test** | A 2019 **must**, **quietly dropped Oct 2024** |
| **O9** | Published comparable DORA figures | The framework exists — the **"DoD4"** (OUSD(A&S), Oct 2024): DORA4 plus Value/ROI plus Cyber Resilience incl. "average time to achieve ATO". **No published values anywhere.** |
| **O10** | Inheritance as a contract, **with change notification** | — |
| **O11** | The factory's own supply chain verifiable | — |
| **O12** | Third-party pen test of dev **and** prod within 90 days, annually | — |
| **O13** | Per-person training evidence | — |

**Conspicuously *not* demanded anywhere: reproducible builds, signature verification at admission, or OSCAL.** Three things the technical community treats as table stakes and no policy asks for. That is a gap between engineering fashion and regulatory demand that we should be careful about — it means building them is a choice to be justified on merit, not a compliance requirement to be waved through.

**O3 is the keystone and it is ours.** "The compliance artefact is a build output, not a document" is the project's thesis quoted back from DoD's own strategy, and the research marks it unsolved.

**O9 is the free win.** A metrics framework exists, published by OUSD(A&S), and *nobody has published any values against it.* Being the first to publish DoD4 figures for a real factory would be a differentiator that costs almost nothing, and it directly addresses the measurement absence four audits complain about.

## 6. The three best-sourced criticisms to have answers for

1. **Kessel Run** (*Air & Space Forces Magazine*, 1 Mar 2025): co-founder Bryon Kroger — it was **"failing"**, **"the empire struck back"**; 50% staff turnover every six months; ex-director Beachkofski — "drifting", training budget cut.
2. **GAO-23-105611:** none of 17 DSB/DIB recommendations fully implemented, 13 with outstanding actions, and DoD **"do not plan to fully implement"**. The DSB's pass/fail software-factory source-selection gate became non-mandatory guidance. **GAO-22-105230: only 10 of 59 major programmes used a software factory**, and DoD officials called **six months to a year** delivery "more suitable" against the DIB's two weeks.
3. **DoD's own FY25–26 carryovers:** no software factory criteria or metrics, no SBOM implementation guidance, no cATO issued, no cost data.

That third one is the most useful, because it is DoD auditing itself and finding the same absence we found: **there are no criteria, no metrics, no guidance and no cost data.** Which is either the strongest argument for doing this work, or the strongest argument that nobody will buy it. Probably both.

## 7. Gaps

No GAO or IG report specifically auditing Kessel Run was found (gao.gov and dodig.mil 403, oversight.gov search unusable — **retry all three via the `r.jina.ai` proxy**, which broke the `.gov` wall after this research completed). No audited before/after ATO durations. No cost figures. Also: "Overwatch" is almost certainly the **Navy Overmatch Software Armory**.
