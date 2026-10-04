#!/usr/bin/env python3
"""Build a single HTML page from all MkDocs documentation in nav order."""

import yaml
import markdown
from pathlib import Path

DOCS = Path(__file__).parent / "docs"

def extract_paths(nav):
    """Walk the mkdocs nav structure and yield markdown file paths in order."""
    for item in nav:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    yield value
                elif isinstance(value, list):
                    yield from extract_paths(value)

def main():
    with open(Path(__file__).parent / "mkdocs.yml") as f:
        raw = f.read()
    # Strip !!python/name tags that safe_load can't handle
    import re
    raw = re.sub(r"!!python/name:\S+", "''", raw)
    config = yaml.safe_load(raw)

    md_paths = list(extract_paths(config["nav"]))

    combined = []
    for rel in md_paths:
        p = DOCS / rel
        if p.exists():
            combined.append(p.read_text())
        else:
            combined.append(f"<!-- missing: {rel} -->")

    full_md = "\n\n---\n\n".join(combined)

    md = markdown.Markdown(
        extensions=[
            "tables",
            "attr_list",
            "md_in_html",
            "def_list",
            "admonition",
            "pymdownx.details",
            "pymdownx.superfences",
            "pymdownx.highlight",
            "pymdownx.inlinehilite",
            "pymdownx.tabbed",
        ],
        extension_configs={
            "pymdownx.tabbed": {"alternate_style": True},
            "pymdownx.highlight": {"anchor_linenums": True},
        },
    )

    body = md.convert(full_md)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Secure Software Factory — Complete Reference</title>
<style>
  body {{ max-width: 52em; margin: 2em auto; padding: 0 1em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.6; color: #222; }}
  h1 {{ border-bottom: 2px solid #3949ab; padding-bottom: .3em; }}
  h2 {{ border-bottom: 1px solid #ddd; padding-bottom: .2em; margin-top: 2em; }}
  h3 {{ margin-top: 1.5em; }}
  hr {{ border: none; border-top: 2px solid #3949ab; margin: 3em 0; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  th, td {{ border: 1px solid #ccc; padding: .5em .75em; text-align: left; }}
  th {{ background: #eef0f9; }}
  code {{ background: #f5f5f5; padding: .15em .3em; border-radius: 3px; font-size: .9em; }}
  pre {{ background: #f5f5f5; padding: 1em; overflow-x: auto; border-radius: 4px; }}
  pre code {{ background: none; padding: 0; }}
  details {{ background: #f5f6fc; border: 1px solid #c5cae9; border-radius: 4px; padding: .75em 1em; margin: 1em 0; }}
  summary {{ font-weight: bold; cursor: pointer; }}
  .admonition {{ border-left: 4px solid #3949ab; padding: .75em 1em; margin: 1em 0; background: #f5f6fc; }}
  .admonition-title {{ font-weight: bold; }}
  .mermaid {{ text-align: center; margin: 1em 0; }}
</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad: true}});</script>
</head>
<body>
{body}
</body>
</html>"""

    out = Path(__file__).parent / "secure-software-factory-complete.html"
    out.write_text(html)
    print(f"Written to {out} ({len(html):,} bytes, {len(md_paths)} pages)")

if __name__ == "__main__":
    main()
