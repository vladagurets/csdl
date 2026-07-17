# Task 4 Style Anchor Repair Design

**Status:** Approved direction  
**Date:** 2026-07-17  
**Scope:** Repair the incomplete completion of Pilot 01 Task 4 without starting Task 5.

## Context

Pilot 01 Task 4 was marked complete, but its required canonical raster artifact was absent:

```text
pilots/01-agentic-discipline/references/style-anchor-light.png
```

The original Task 4 commit added the shared YAML prompt contract and the broader density-calibration reference, but not the card-specific style anchor. Project status and handoff documents nevertheless treated the missing file as the primary reference consumed by Tasks 5–11.

The root cause was a missing artifact-specific completion gate: the existing asset validator checked canonical cards and adaptations, not shared reference images. A documentation-only completion signal could therefore drift from repository state.

## Goal

Restore Task 4 to a truthful, independently verifiable complete state by adding the canonical style anchor, persistent provenance and review evidence, a dedicated validator with tests, CI enforcement, and corrected operational documentation.

## In Scope

1. Create `pilots/01-agentic-discipline/references/style-anchor-light.png` as a real `1080×1350` RGB PNG.
2. Create `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md` with source inputs, construction method, visible-copy review, visual checklist, image metadata, content hashes, and approval rationale.
3. Create `tools/validate_style_anchor.py` with a focused `validate_style_anchor(path: Path) -> list[str]` interface.
4. Create `tests/test_validate_style_anchor.py` covering a valid anchor, a missing anchor, non-PNG content, truncated PNG data, corrupt PNG checksums, wrong dimensions, and unsupported color mode.
5. Add the dedicated validator to `.github/workflows/validate.yml` so the missing or damaged artifact cannot regress silently.
6. Update `STATUS.md` and `CHANGELOG.md` to record that Task 4 was repaired and to name the new evidence.
7. Update `README.md`, `AGENTS.md`, and `docs/handoff/CODEX_IMAGE_GENERATION.md` so the Task 5 baseline reflects sixteen tests and includes explicit style-anchor validation.

## Out of Scope

- No Task 5 prompt or Card 01 raster work.
- No changes to canonical Pilot 01 copy or locked design decisions.
- No three-candidate style-anchor rerun; that was the declined full-repeat option.
- No font binaries, external source PDFs, API helpers, or placeholder images.
- No expansion of the series-level `validate_assets.py` contract.

## Canonical Raster Contract

The repair creates one calibration poster from the locked Task 4 prompt contract. Because this is the targeted repair path rather than a full generative rerun, the raster is constructed deterministically with Pillow using a custom 5×7 modular glyph alphabet drawn from rectangles. It has no external or system-font dependency, and no font binary is committed.

Required visible copy, and no other text:

```text
QUIET MODULAR
ONE IDEA.
ONE SIGNAL.
```

Required visual properties:

- exact canvas: `1080×1350`;
- mode: `RGB`;
- background: warm paper `#F7F5F0`;
- primary ink: warm graphite `#1B1B19`;
- signal: muted mineral coral `#C96157`;
- upper-left modular technical headline field;
- one coral square in the lower-right third, approximately 7% of canvas area;
- one thin graphite vector connecting the headline field to the square;
- at least 65% perceived negative space;
- no logo, footer, frame, grid, coordinates, icons, gradients, shadows, or extra labels.

The provenance sidecar must explicitly identify deterministic Pillow construction as a Task 4 repair exception so it is not misrepresented as an original GPT Image 2 candidate.

## Validation Design

`tools/validate_style_anchor.py` is intentionally separate from `tools/validate_assets.py`. The existing validator is a series-completion gate and is expected to fail while Cards 02–07 and 16:9 adaptations are absent. Task 4 needs an independent gate that passes before Task 5 begins.

The validator reports errors for:

- missing file;
- non-PNG format;
- unreadable or truncated PNG data;
- corrupt PNG chunk checksums;
- dimensions other than `1080×1350`;
- color mode other than `RGB` or `RGBA`.

The validator must call Pillow's `image.verify()` after reading metadata; `Image.open()` alone can accept a truncated PNG whose header remains intact. Pillow reports truncated data as `OSError` and bad PNG checksums as `SyntaxError`, so the validator catches those two specific exception families and converts them into one readable validation error. Visible-copy fidelity and visual restraint remain manual-review responsibilities and are persisted in the provenance sidecar. The committed binary must also be checked byte-for-byte by comparing its Git blob SHA with the locally calculated `git hash-object` result before branch promotion.

## Acceptance Criteria

Task 4 repair is complete when:

1. the PNG exists at the canonical path and passes the dedicated validator;
2. truncated PNG data and corrupt checksums are rejected by regression tests;
3. the committed Git blob SHA matches the locally calculated blob SHA;
4. the provenance sidecar records all source inputs, exact copy, metadata, checklist results, content hashes, and approval rationale;
5. all sixteen unit tests pass;
6. manifest validation still passes;
7. CI includes and passes the style-anchor command;
8. `STATUS.md` no longer relies only on the original incomplete commit as Task 4 evidence;
9. `README.md`, `AGENTS.md`, and the image-generation handoff expose the current baseline;
10. `CHANGELOG.md` records the repair;
11. Task 5 remains untouched.
