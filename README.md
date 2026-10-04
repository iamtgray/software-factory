# software-factory

Research and design for an open-source, modular secure software factory: a deployable
set of components defined by the outcomes they produce, able to run in a hyperscale
cloud or an air-gapped enclave without becoming two different products.

## Where to start

1. [`notes/00-premise.md`](notes/00-premise.md) — why this project exists and what it is for.
2. [`discovery/00-index.md`](discovery/00-index.md) — **the catalogue of everything we have found, with how much to trust each item.** Start here for facts.
3. [`design/01-layers-and-handoffs.md`](design/01-layers-and-handoffs.md) — what we concluded: the three primitives and the four trust-domain transitions.

## Running the site

```bash
python3 -m venv .venv && .venv/bin/pip install mkdocs-material pyyaml markdown
.venv/bin/mkdocs serve                  # http://127.0.0.1:8000
.venv/bin/mkdocs build --strict         # must pass before committing
.venv/bin/python build_single_page.py   # one self-contained HTML file
```

`.github/workflows/deploy-docs.yml` publishes to GitHub Pages on push to `main`.
`site_url` in `mkdocs.yml` assumes the repo will be called `software-factory` --
change it if not, or internal links in the published build will be wrong.

## Layout

| Path | Contents |
|---|---|
| `notes/` | Framing and running working notes |
| `discovery/` | Curated record of findings, with verification status. The thing to cite. |
| `research/` | Raw research output, one file per question. Long; source material for `discovery/`. |
| `design/` | Architecture: primitives, hand-offs, slot contracts, deployment |

## The short version

Twelve regulatory regimes, across US and UK defence, the EU, financial services, medical
devices, automotive and aviation, reduce to three machine-readable artefacts: a current
component inventory, build-and-release provenance, and a vulnerability-and-remediation
ledger. Serialising those is cheap and already solved. Generating them authoritatively,
currently, and with transitive completeness is the product.

Policy demands continuous evidence and names the pipeline as its source, but specifies no
machine-verifiable form. The DoD's cATO evaluation criteria accept "screen shots of
control gate output as displayed in a dashboard" as proof that a control gate works, and
list automating control validation as an objective rather than a requirement. That gap is
where the stale document walks back in.

Evidence rots because nothing reads it. Anything that gates a build gets maintained,
because it breaks loudly when it drifts. Anything read only by a human at assessment time
rots silently. The flagship DoD platform built live compliance validation in February
2024, disabled the gate that August, and deleted the capability in September 2025.

Transport is not the gap: a standard OCI layout already carries signatures, attestations
and SBOMs across an air gap, and an existing command verifies them offline. What is
missing is that nothing on the far side is obliged to look. The buildable work is a
fail-closed receiver-side gate over a signed shipment manifest, and the guard-mediated
case, which no open-source project models at all.

Status: research phase. Nothing is built yet.
