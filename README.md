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

The original premise — that no open-source project integrates best-of-breed components
into a coherent software factory with SBOM production — turned out to be falsifiable in
about ninety seconds. Konflux-CI already describes itself as exactly that, and SBOM
generation is commodity.

The narrow, defensible gap is that **the evidence does not cross the boundary with the
artefact**. Everything upstream of an air-gap is solved well by several projects. The
moment an artefact crosses into a high-side enclave it arrives as a bare tarball and the
receiver takes it on trust. The only cross-domain packaging implementation in open code
verifies the signature on the low side and then discards it.

Generalised: evidence is produced as a side effect, stored where nobody reads it, and
never checked against what it describes. Anything that gates a build gets maintained;
anything read only by a human at accreditation time rots silently, because nothing fails
when it does. The flagship DoD platform's OSCAL component definition — the artefact that
makes control inheritance and therefore cATO work — has not been touched in three and a
half years.

So the factory's distinguishing claim is that evidence is a first-class artefact with its
own freshness and verification gates, and stale provenance is a build failure rather than
an accreditation surprise.

Status: research phase. Nothing is built yet.
