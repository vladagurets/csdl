# Milestone 7 — Cookbook and Design Book v1.0 Implementation Contract

**Objective:** build a coherent bilingual 25–40 page publication from canonical Milestone 1–6 sources while preserving every closed contract and accepted raster.

## Primary signal

A reviewer can open the final A4 landscape PDF, read all Ukrainian editorial content and English canonical terminology in order, locate every required topic, all fifteen components, all 23 recipes, a complete Prompt DSL v0.5 example, Analytical Mode, Accessibility v0.1, provenance, why/do/don’t guidance, and preflight without clipped or missing text.

## Observable acceptance criteria

1. The manifest enumerates 25–40 meaningful pages and the built PDF has exactly the same page count and order.
2. Every explanatory page contains Ukrainian editorial content where required; registered canonical English identifiers remain byte-exact and no translated alias enters public vocabulary.
3. All fifteen components and 23 recipes appear exactly once in their canonical catalog sequences and every Prompt DSL field/example validates against v0.5.
4. Analytical and Accessibility sections cite their owning contracts, preserve semantic digests/counts/thresholds, and distinguish accepted raster evidence from deterministic specification evidence.
5. Full-size renders, contact sheet, text extraction, grayscale review, contrast checks, source links, raster hashes, overflow bounds, two-build hashes, tests, validators, CI drift checks, and `git diff --exit-code` pass.

## Architecture

```text
cookbook/design-book-v1.0/
├── README.md
├── manifest.yaml
├── terminology.yaml
├── provenance.yaml
├── pages/                    # canonical one-page Markdown sources
├── fixtures/negative/        # high-value invalid publication mutations
├── evaluation/review.md
├── generated/                # deterministic checked-in Markdown/index outputs
└── output/                   # ignored PDF, page renders, text, contact sheet, build report
```

The final format is ISO A4 landscape (`297×210 mm`). The builder uses the existing Pillow/PyYAML dependency set and repository-owned deterministic PDF assembly. It records the local font fallback and its digest but does not commit font binaries or resolve the global licensed-font decision.

## Work packets

1. Evidence audit, acceptance contract, and D-033.
2. Canonical publication manifest, terminology, provenance, and page sources.
3. Deterministic Markdown/PDF/page/contact-sheet builder and validator.
4. Negative fixtures and focused tests.
5. Visual, grayscale, reading-order, determinism, full-regression, and CI review.
6. Documentation alignment, integration PR, merge-commit completion, main synchronization, and final full-matrix verification.

## Stop conditions

Stop and request approval if completion requires a new generated/recolored/replaced raster, a committed font binary, a new production dependency, a license decision, or a change to any locked Milestone 1–6 contract.
