# Task 4 Style Anchor Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore Pilot 01 Task 4 with the missing canonical style-anchor raster, persistent provenance, an independent validation gate, CI enforcement, and truthful operational documentation.

**Architecture:** Keep the repair isolated from unfinished card assets. A dedicated validator checks the shared style-anchor file, while manual visual and copy review is persisted in a sidecar next to the raster. The raster is a deterministic Pillow reconstruction using a custom 5×7 modular glyph alphabet and is explicitly documented as a repair exception rather than an original GPT Image 2 candidate.

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
- The committed Git blob SHA must equal the local `git hash-object` result.

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

Run this exact one-off builder from the repository root:

```bash
python - <<'PY'
from pathlib import Path

from PIL import Image, ImageDraw

PAPER = "#F7F5F0"
INK = "#1B1B19"
CORAL = "#C96157"
GLYPHS = {
    ".": ("00000", "00000", "00000", "00000", "00000", "00110", "00110"),
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01110"),
    "I": ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10010"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
}


def draw_text(
    draw: ImageDraw.ImageDraw,
    position: tuple[int, int],
    text: str,
    *,
    scale: int,
    tracking: int,
) -> None:
    x, y = position
    for character in text:
        if character == " ":
            x += 5 * scale + tracking
            continue
        glyph = GLYPHS[character]
        for row, bits in enumerate(glyph):
            for column, bit in enumerate(bits):
                if bit == "1":
                    left = x + column * scale
                    top = y + row * scale
                    draw.rectangle(
                        (left, top, left + scale - 1, top + scale - 1),
                        fill=INK,
                    )
        x += 5 * scale + tracking


output = Path(
    "pilots/01-agentic-discipline/references/style-anchor-light.png"
)
output.parent.mkdir(parents=True, exist_ok=True)
image = Image.new("RGB", (1080, 1350), PAPER)
draw = ImageDraw.Draw(image)

draw_text(draw, (72, 88), "QUIET", scale=14, tracking=14)
draw_text(draw, (72, 208), "MODULAR", scale=14, tracking=14)
draw_text(draw, (72, 370), "ONE IDEA.", scale=7, tracking=8)
draw_text(draw, (72, 438), "ONE SIGNAL.", scale=7, tracking=8)
draw.line((388, 510, 688, 900), fill=INK, width=3)
draw.rectangle((688, 900, 1007, 1219), fill=CORAL)
image.save(output, format="PNG", optimize=True)
print(output)
PY
```

Expected: the command prints the canonical path and creates an 8031-byte RGB PNG with one 320×320 coral square.

- [ ] **Step 2: Verify exact file identity and raster metadata**

Run:

```bash
sha256sum pilots/01-agentic-discipline/references/style-anchor-light.png
git hash-object pilots/01-agentic-discipline/references/style-anchor-light.png
python tools/validate_style_anchor.py \
  pilots/01-agentic-discipline/references/style-anchor-light.png
```

Expected:

```text
7ba4a191e97a777285b676b17484d8dbc64eed5216b1e1129634f5da81bd49d6
7d9ce5b37525cab14cde8bd8df61881fcd97003a
style anchor valid
```

When uploading through the Git data API, require the returned blob SHA to equal `7d9ce5b37525cab14cde8bd8df61881fcd97003a` before advancing the branch ref.

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

Create `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md` with:

- the artifact status and repair date;
- SHA-256 `7ba4a191e97a777285b676b17484d8dbc64eed5216b1e1129634f5da81bd49d6`;
- Git blob SHA `7d9ce5b37525cab14cde8bd8df61881fcd97003a`;
- all four source inputs;
- the custom 5×7 Pillow construction method;
- exact-copy review;
- PNG, dimensions, RGB mode, file size, palette, unique-color count, coral bounds, and area;
- the complete checked visual-review list;
- approval rationale;
- an explicit statement that the raster is a targeted deterministic repair, not an original GPT Image 2 candidate.

- [ ] **Step 5: Commit the raster and evidence**

```bash
git add \
  pilots/01-agentic-discipline/references/style-anchor-light.png \
  pilots/01-agentic-discipline/references/style-anchor-light.provenance.md
git commit -m "feat: restore the Quiet Modular style anchor"
```

---

### Task 3: Enforce the repair and synchronize operational documentation

**Files:**
- Modify: `.github/workflows/validate.yml`
- Modify: `STATUS.md`
- Modify: `CHANGELOG.md`
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/handoff/CODEX_IMAGE_GENERATION.md`

**Interfaces:**
- Consumes: `tools/validate_style_anchor.py` and the canonical PNG.
- Produces: a required CI check and one consistent Task 5 baseline across all entry points.

- [ ] **Step 1: Add the style-anchor command to CI**

Append after manifest validation in `.github/workflows/validate.yml`:

```yaml
      - name: Validate Pilot 01 style anchor
        run: >-
          python tools/validate_style_anchor.py
          pilots/01-agentic-discipline/references/style-anchor-light.png
```

- [ ] **Step 2: Correct Task 4 evidence in `STATUS.md`**

Use this Task 4 evidence cell:

```markdown
Complete (repaired) | `style-anchor-light.png`, provenance sidecar, dedicated tests, and CI validator
```

Add the style-anchor validator to the current validation block and retain Task 5 as the active next task.

- [ ] **Step 3: Record the repair in `CHANGELOG.md`**

Add under `## Unreleased`:

```markdown
- Repaired Pilot 01 Task 4 by restoring `style-anchor-light.png`, documenting its provenance and manual review, verifying its Git blob byte-for-byte, and adding dedicated unit and CI validation.
```

- [ ] **Step 4: Synchronize the Task 5 baseline**

Update `README.md`, `AGENTS.md`, and `docs/handoff/CODEX_IMAGE_GENERATION.md` so each requires:

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
```

Record the expected results as:

```text
14 passed
manifest valid
style anchor valid
```

Also link or name `style-anchor-light.provenance.md` wherever the shared reference is introduced.

- [ ] **Step 5: Run the complete verification suite**

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

- [ ] **Step 6: Confirm Task 5 remains untouched**

Run:

```bash
git diff --name-only main...HEAD | \
  grep -E 'prompts/01-hook|canonical/light/4x5/01-hook' && exit 1 || true
```

Expected: no output and exit code `0`.

- [ ] **Step 7: Commit the enforcement and status correction**

```bash
git add \
  .github/workflows/validate.yml \
  STATUS.md \
  CHANGELOG.md \
  README.md \
  AGENTS.md \
  docs/handoff/CODEX_IMAGE_GENERATION.md
git commit -m "ci: enforce the Pilot 01 style anchor"
```

- [ ] **Step 8: Open a pull request and verify CI**

Push branch `codex/repair-task-4-style-anchor` and open a draft pull request into `main` titled:

```text
fix: complete Pilot 01 Task 4 style anchor
```

The PR body must list the root cause, restored artifacts, exact hashes, validation results, and explicit confirmation that Task 5 was not started. Wait for the GitHub Actions `Validate CSDL` workflow and inspect the job steps before marking the repair complete.
