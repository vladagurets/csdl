# CSDL Cookbook and Design Book v1.0

This directory is the additive Milestone 7 publication contract. One Markdown file owns each book page. Canonical CSDL technical details are expanded from the completed Milestone 1–6 manifests and contracts, so the book does not fork the public vocabulary or quantitative/accessibility rules.

## Authority

- `pages/` owns Ukrainian editorial explanation and page-level reading order.
- `manifest.yaml` owns page order, format, required topics, and output contract.
- `terminology.yaml` owns protected English identifiers and Ukrainian editorial glosses.
- `provenance.yaml` maps every page to repository evidence.
- Component, recipe, Prompt DSL, Analytical Mode, and Accessibility source contracts remain authoritative for technical facts.
- `generated/` is deterministic and checked in; never edit it by hand.
- `output/` contains ignored derived PDF/review artifacts.

## Build and validate

```bash
.venv/bin/python tools/build_design_book.py cookbook/design-book-v1.0
.venv/bin/python tools/validate_design_book.py cookbook/design-book-v1.0
```

The builder emits:

```text
generated/csdl-cookbook-design-book-v1.0.md
generated/index.yaml
output/pdf/csdl-cookbook-design-book-v1.0.pdf
output/pages/001.png … 032.png
output/grayscale/001.png … 032.png
output/contact-sheet.png
output/extracted-text.txt
output/build-report.yaml
```

The PDF is A4 landscape and includes a deterministic invisible Unicode text layer in page reading order. Markdown remains the canonical accessible source. The local rendering font is a build fallback, not a global licensed-font decision; its path and SHA-256 are recorded in the ignored build report.

No publication render becomes accepted CSDL raster evidence. Existing source rasters are embedded without byte changes and stay governed by `accessibility/night-mode-v0.1/evaluation/raster-hashes.yaml`.
