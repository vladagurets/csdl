# Style Anchor Light — Provenance and Review

**Artifact:** `style-anchor-light.png`  
**Status:** Approved canonical reference for Pilot 01 Tasks 5–11  
**Repair date:** 2026-07-17  
**SHA-256:** `7ba4a191e97a777285b676b17484d8dbc64eed5216b1e1129634f5da81bd49d6`  
**Git blob SHA:** `7d9ce5b37525cab14cde8bd8df61881fcd97003a`

## Why this file exists

Task 4 was previously marked complete although its required canonical raster was absent. This sidecar records the repaired artifact and prevents the raster from being treated as unexplained binary state.

## Source inputs

- `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`
- `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`, Task 4
- `specs/2026-07-17-csdl-v0.1-design.md`
- `references/quiet-modular-density-calibration.png` as repository provenance for the broader approved density direction; no pixels were copied or transformed from it

## Construction method

This is a deterministic Pillow reconstruction made for the targeted Task 4 repair. All visible letters are built from a custom 5×7 modular glyph alphabet drawn as graphite rectangles; no external or system font is required and no font binary is committed. The raster contains exactly the three locked palette colors and is saved directly as an RGB PNG. It is not represented as an original GPT Image 2 candidate. The full three-candidate generative rerun was intentionally outside the selected repair scope.

Before the branch was advanced, the SHA returned by GitHub for the uploaded blob was compared with the local `git hash-object` result. Both were exactly `7d9ce5b37525cab14cde8bd8df61881fcd97003a`.

## Visible copy review

Expected and observed visible words:

```text
QUIET MODULAR
ONE IDEA.
ONE SIGNAL.
```

Result: **pass — exact words only; no additional labels or copy.**

The headline is visually broken across two rows (`QUIET` / `MODULAR`) while preserving the exact words and reading order.

## Raster metadata

- format: PNG
- dimensions: 1080×1350
- color mode: RGB
- file size: 8031 bytes
- paper: `#F7F5F0`
- graphite: `#1B1B19`
- coral signal: `#C96157`
- unique colors: 3
- coral square pixel bounds: `(688, 900)` through `(1007, 1219)`
- coral square area: 102,400 pixels, approximately 7.02% of the canvas

## Manual visual review

- [x] one upper-left modular technical headline field
- [x] one muted coral square in the lower-right third
- [x] one thin graphite vector connects the headline field and signal
- [x] at least 65% perceived negative space
- [x] technical but non-sci-fi typography
- [x] readable at phone width
- [x] no logo, footer, frame, grid, coordinates, icons, gradients, shadows, or extra labels

## Approval rationale

The artifact is intentionally sparse, preserves the locked Muted Signal palette, demonstrates the Quiet Modular Level A density, and provides a stable visual reference without adding semantic or decorative noise. It is approved as the shared light-mode anchor consumed by Pilot 01 Tasks 5–11.
