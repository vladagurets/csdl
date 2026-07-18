# Night Mode and Accessibility v0.1

This directory contains CSDL's independent additive contract for accessible light, night, monochrome, and projector output. It preserves Prompt DSL v0.5, the fifteen public components, the 23 recipes, Analytical Mode v0.1 quantitative meaning, and all accepted raster bytes.

## Canonical inputs

- `SPEC.md` — normative Markdown specification;
- `manifest.yaml` — version, dependencies, profiles, proof inventory, and outputs;
- `token-schema.yaml` and `proof-schema.yaml` — versioned machine schemas;
- `contracts/tokens.yaml` — calibrated semantic mappings;
- `contracts/contrast.yaml` — sRGB thresholds, focus, strokes, and prohibited pairs;
- `contracts/fallbacks.yaml` — CVD, monochrome, status, Legend, and analytical redundancy;
- `contracts/compatibility.yaml` — Component, Recipe, Prompt DSL, and Analytical Mode source matrix;
- `proofs/sources/` — ten authored deterministic proof sources;
- `fixtures/negative/` — seventeen exact-error mutations;
- `MIGRATION.md`, `ROLLBACK.md`, and `evaluation/review.md` — operational and evidence records.

## Derived outputs

- `proofs/packages/` — ten deterministic accessibility packages;
- `index.yaml` — profile/proof inventory;
- `contrast-matrix.yaml` — independently reproducible allowed-pair ratios;
- `compatibility.yaml` — derived dependency compatibility;
- `evaluation/raster-hashes.yaml` — SHA-256 inventory for all sixty tracked accepted PNGs.

## Validation

```bash
.venv/bin/python tools/build_accessibility_mode.py accessibility/night-mode-v0.1
.venv/bin/python tools/validate_accessibility_mode.py accessibility/night-mode-v0.1
git diff --exit-code
```

Use `--incomplete` only for a partial historical branch or contract-development check. Strict mode requires the exact proof, fixture, document, compatibility, contrast, index, and raster-hash inventory.

## Evidence boundary

Accepted light rasters calibrate hierarchy and Constructive Signal identity. WCAG 2.2 supports the measurable contrast/color-independent baseline. Night/projector/CVD/monochrome outputs are deterministic specification proofs only. No new raster was generated, recolored, or visually accepted for Milestone 6.
