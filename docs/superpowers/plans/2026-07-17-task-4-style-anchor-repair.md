# Task 4 Style Anchor Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore Pilot 01 Task 4 with the missing canonical style-anchor raster, persistent provenance, an independent validation gate, CI enforcement, and truthful status evidence.

**Architecture:** Keep the repair isolated from unfinished card assets. A dedicated validator checks the shared style-anchor file, while manual visual and copy review is persisted in a sidecar next to the raster. The raster is a deterministic Pillow reconstruction from the locked Task 4 contract, explicitly documented as a repair exception rather than an original GPT Image 2 candidate.

**Tech Stack:** Python 3.11+, Pillow, pytest, Markdown, GitHub Actions, PNG.

## Global Constraints

- Do not start or modify Task 5.
- Preserve `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml` unchanged.
- Canonical anchor path: `pilots/01-agentic-discipline/references/style-anchor-light.png`.
- Exact raster contract: PNG, `1080×1350`, `RGB`.
- Exact visible words only: `QUIET MODULAR`, `ONE IDEA.`, `ONE SIGNAL.`
- Palette: paper `#F7F5F0`, ink `#1B1B19`, coral `#C96157`.
- No logo, footer, frame, grid, coordinates, icons, gradients, shadows, or extra labels.
- No font binaries or placeholder images may be committed.

---

### Task 1: Add an independent style-anchor validation gate

**Files:**
- Create: `tests/test_validate_style_anchor.py`
- Create: `tools/validate_style_anchor.py`

**Interfaces:**
- Consumes: a candidate style-anchor `Path`.
- Produces: `validate_style_anchor(path: Path) -> list[str]` and a CLI with exit code `0` on success, `1` on validation errors, and `2` on incorrect usage.

- [ ] **Step 1: Write the failing validator tests**

Create `tests/test_validate_style_anchor.py`:

```python
from pathlib import Path

from PIL import Image

from tools.validate_style_anchor import validate_style_anchor


def create_image(
    path: Path,
    *,
    size: tuple[int, int] = (1080, 1350),
    mode: str = "RGB",
    image_format: str = "PNG",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new(mode, size).save(path, format=image_format)


def test_accepts_valid_style_anchor(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    assert validate_style_anchor(path) == []


def test_rejects_missing_style_anchor(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    assert validate_style_anchor(path) == [
        f"missing style anchor: {path.as_posix()}"
    ]


def test_rejects_non_png_content(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, image_format="JPEG")
    assert "style-anchor-light.png must be PNG, got JPEG" in validate_style_anchor(path)


def test_rejects_wrong_dimensions(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, size=(1080, 1080))
    assert "style-anchor-light.png must be 1080x1350, got 1080x1080" in validate_style_anchor(path)


def test_rejects_unsupported_color_mode(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, mode="L")
    assert "style-anchor-light.png must use RGB or RGBA mode, got L" in validate_style_anchor(path)
```

- [ ] **Step 2: Run the focused tests to verify failure**

Run:

```bash
python -m pytest tests/test_validate_style_anchor.py -q
```

Expected: collection fails with `ModuleNotFoundError: No module named 'tools.validate_style_anchor'`.

- [ ] **Step 3: Implement the minimal validator**

Create `tools/validate_style_anchor.py`:

```python
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

EXPECTED_SIZE = (1080, 1350)
ALLOWED_MODES = {"RGB", "RGBA"}


def validate_style_anchor(path: Path) -> list[str]:
    if not path.exists():
        return [f"missing style anchor: {path.as_posix()}"]

    errors: list[str] = []
    try:
        with Image.open(path) as image:
            if image.format != "PNG":
                errors.append(
                    f"{path.name} must be PNG, got {image.format or 'unknown'}"
                )
            if image.size != EXPECTED_SIZE:
                errors.append(
                    f"{path.name} must be 1080x1350, "
                    f"got {image.size[0]}x{image.size[1]}"
                )
            if image.mode not in ALLOWED_MODES:
                errors.append(
                    f"{path.name} must use RGB or RGBA mode, got {image.mode}"
                )
    except OSError:
        errors.append(f"{path.name} must be a readable PNG")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python tools/validate_style_anchor.py STYLE_ANCHOR_PNG")
        return 2

    errors = validate_style_anchor(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("style anchor valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the focused tests to verify success**

Run:

```bash
python -m pytest tests/test_validate_style_anchor.py -q
```

Expected: `5 passed`.

- [ ] **Step 5: Commit the validation gate**

```bash
git add tests/test_validate_style_anchor.py tools/validate_style_anchor.py
git commit -m "test: validate the shared style anchor"
```

---

### Task 2: Create the canonical raster and persistent review evidence

**Files:**
- Create: `pilots/01-agentic-discipline/references/style-anchor-light.png`
- Create: `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md`

**Interfaces:**
- Consumes: `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml` and the locked Task 4 composition contract.
- Produces: the primary visual reference consumed by Tasks 5–11 plus human-readable evidence of its construction and approval.

- [ ] **Step 1: Render the deterministic repair raster**

Run this one-off command from the repository root:

```bash
python - <<'PY'
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

output = Path(
    "pilots/01-agentic-discipline/references/style-anchor-light.png"
)
output.parent.mkdir(parents=True, exist_ok=True)

paper = "#F7F5F0"
ink = "#1B1B19"
coral = "#C96157"
image = Image.new("RGB", (1080, 1350), paper)
draw = ImageDraw.Draw(image)

headline_font = ImageFont.truetype(
    "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf", 104
)
support_font = ImageFont.truetype(
    "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf", 42
)


def tracked_text(
    position: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    tracking: int,
) -> None:
    x, y = position
    for character in text:
        draw.text((x, y), character, font=font, fill=ink)
        x += int(draw.textlength(character, font=font)) + tracking


tracked_text((72, 88), "QUIET", headline_font, 3)
tracked_text((72, 190), "MODULAR", headline_font, 3)
tracked_text((72, 350), "ONE IDEA.", support_font, 2)
tracked_text((72, 410), "ONE SIGNAL.", support_font, 2)

draw.line((372, 462, 688, 900), fill=ink, width=2)
draw.rectangle((688, 900, 1008, 1220), fill=coral)

image.save(output, format="PNG", optimize=True)
print(output)
PY
```

Expected: the command prints the canonical path and creates an RGB PNG with one coral square occupying approximately 7.0% of the canvas.

- [ ] **Step 2: Run deterministic metadata validation**

Run:

```bash
python tools/validate_style_anchor.py \
  pilots/01-agentic-discipline/references/style-anchor-light.png
```

Expected: `style anchor valid`.

- [ ] **Step 3: Complete the manual visual and copy review**

Inspect the raster at full size and at phone width. Confirm all items before writing the sidecar:

```text
[pass] visible words are exactly QUIET MODULAR / ONE IDEA. / ONE SIGNAL.
[pass] no additional visible text
[pass] one muted coral square only
[pass] one thin graphite vector only
[pass] at least 65% perceived negative space
[pass] technical but non-sci-fi typography
[pass] no logo, footer, frame, grid, coordinates, icons, gradients, or shadows
[pass] composition remains legible at phone width
```

- [ ] **Step 4: Create the provenance sidecar**

Create `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md`:

```markdown
# Style Anchor Light — Provenance and Review

**Artifact:** `style-anchor-light.png`  
**Status:** Approved canonical reference for Pilot 01 Tasks 5–11  
**Repair date:** 2026-07-17

## Why this file exists

Task 4 was previously marked complete although its required canonical raster was absent. This sidecar records the repaired artifact and prevents the raster from being treated as unexplained binary state.

## Source inputs

- `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`
- `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`, Task 4
- `specs/2026-07-17-csdl-v0.1-design.md`
- `references/quiet-modular-density-calibration.png` as the broader approved density direction

## Construction method

This is a deterministic Pillow reconstruction made for the targeted Task 4 repair. It uses system-provided Inter Display fonts; no font binary is committed. It is not represented as an original GPT Image 2 candidate. The full three-candidate generative rerun was intentionally outside the selected repair scope.

## Visible copy review

Expected and observed visible words:

```text
QUIET MODULAR
ONE IDEA.
ONE SIGNAL.
```

Result: **pass — exact words only; no additional labels or copy.**

## Raster metadata

- format: PNG
- dimensions: 1080×1350
- color mode: RGB
- paper: `#F7F5F0`
- graphite: `#1B1B19`
- coral signal: `#C96157`

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
```

- [ ] **Step 5: Commit the raster and evidence**

```bash
git add \
  pilots/01-agentic-discipline/references/style-anchor-light.png \
  pilots/01-agentic-discipline/references/style-anchor-light.provenance.md
git commit -m "feat: restore the Quiet Modular style anchor"
```

---

### Task 3: Enforce the repair in CI and correct project status

**Files:**
- Modify: `.github/workflows/validate.yml`
- Modify: `STATUS.md`
- Modify: `CHANGELOG.md`

**Interfaces:**
- Consumes: `tools/validate_style_anchor.py` and the canonical PNG.
- Produces: a required CI check and truthful repository-level completion evidence.

- [ ] **Step 1: Add the style-anchor command to CI**

Append after manifest validation in `.github/workflows/validate.yml`:

```yaml
      - name: Validate Pilot 01 style anchor
        run: >-
          python tools/validate_style_anchor.py
          pilots/01-agentic-discipline/references/style-anchor-light.png
```

- [ ] **Step 2: Correct Task 4 evidence in `STATUS.md`**

Replace the Task 4 evidence cell with:

```markdown
`style-anchor-light.png`, provenance sidecar, and dedicated CI validator
```

Add this sentence to the Summary after the style-anchor statement:

```markdown
The previously missing Task 4 raster has been restored with provenance and an independent validation gate.
```

Do not change the active next task: it remains Task 5.

- [ ] **Step 3: Record the repair in `CHANGELOG.md`**

Add under `## Unreleased`:

```markdown
- Repaired Pilot 01 Task 4 by restoring `style-anchor-light.png`, documenting its provenance and manual review, and adding dedicated unit and CI validation.
```

- [ ] **Step 4: Run the complete verification suite**

Run:

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py \
  pilots/01-agentic-discipline/references/style-anchor-light.png
git diff --check
```

Expected:

```text
14 passed
manifest valid
style anchor valid
```

`git diff --check` must produce no output.

- [ ] **Step 5: Confirm Task 5 remains untouched**

Run:

```bash
git diff --name-only main...HEAD | grep -E 'prompts/01-hook|canonical/light/4x5/01-hook' && exit 1 || true
```

Expected: no output and exit code `0`.

- [ ] **Step 6: Commit the enforcement and status correction**

```bash
git add .github/workflows/validate.yml STATUS.md CHANGELOG.md
git commit -m "ci: enforce the Pilot 01 style anchor"
```

- [ ] **Step 7: Open a pull request**

Push branch `codex/repair-task-4-style-anchor` and open a draft pull request into `main` titled:

```text
fix: complete Pilot 01 Task 4 style anchor
```

The PR body must list the root cause, restored artifacts, validation results, and explicit confirmation that Task 5 was not started.
