# Task 4 Style Anchor Repair Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restore Pilot 01 Task 4 with the missing canonical style-anchor raster, persistent provenance, an independent validation gate, CI enforcement, and truthful operational documentation.

**Architecture:** Keep the repair isolated from unfinished card assets. A dedicated validator checks the shared reference independently of the series-level card validator. Manual copy and visual review live beside the raster in a provenance sidecar. The raster is a deterministic Pillow reconstruction using a custom 5×7 modular glyph alphabet and is explicitly documented as a repair exception rather than an original GPT Image 2 candidate.

**Tech Stack:** Python 3.11+, Pillow, pytest, Markdown, GitHub Actions, PNG.

## Global Constraints

- Do not create or modify Task 5 files.
- Preserve `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml` unchanged.
- Canonical anchor path: `pilots/01-agentic-discipline/references/style-anchor-light.png`.
- Exact contract: PNG, `1080×1350`, RGB, visible copy limited to `QUIET MODULAR`, `ONE IDEA.`, `ONE SIGNAL.`
- Locked colors: paper `#F7F5F0`, ink `#1B1B19`, coral `#C96157`.
- No font binaries, placeholders, logo, footer, frame, grid, coordinates, icons, gradients, shadows, or extra labels.
- The GitHub blob SHA must equal the local `git hash-object` result before the branch ref advances.

---

### Task 1: Add the independent validation gate

**Files:**
- Create: `tests/test_validate_style_anchor.py`
- Create: `tools/validate_style_anchor.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_validate_style_anchor.py
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


def test_rejects_truncated_png(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    path.write_bytes(path.read_bytes()[:-12])
    assert "style-anchor-light.png must be a readable PNG" in validate_style_anchor(path)


def test_rejects_corrupt_png_checksum(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path)
    data = bytearray(path.read_bytes())
    idat = data.index(b"IDAT")
    data[idat + 8] ^= 0x01
    path.write_bytes(data)
    assert "style-anchor-light.png must be a readable PNG" in validate_style_anchor(path)


def test_rejects_wrong_dimensions(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, size=(1080, 1080))
    assert "style-anchor-light.png must be 1080x1350, got 1080x1080" in validate_style_anchor(path)


def test_rejects_unsupported_color_mode(tmp_path: Path) -> None:
    path = tmp_path / "style-anchor-light.png"
    create_image(path, mode="L")
    assert "style-anchor-light.png must use RGB or RGBA mode, got L" in validate_style_anchor(path)
```

- [ ] **Step 2: Verify the red phases**

Run before implementing the module:

```bash
python -m pytest tests/test_validate_style_anchor.py -q
```

Expected: import failure because `tools.validate_style_anchor` does not exist.

After the first implementation that only calls `Image.open()`, add the truncated-PNG test. Expected: `1 failed, 5 passed` because a PNG with an intact header but truncated tail is incorrectly accepted.

After adding `image.verify()` but catching only `OSError`, add the checksum test. Expected: `1 failed, 6 passed` because Pillow raises `SyntaxError` for a corrupt PNG chunk checksum.

- [ ] **Step 3: Implement the minimal validator**

```python
# tools/validate_style_anchor.py
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
            image.verify()
    except (OSError, SyntaxError):
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

- [ ] **Step 4: Verify the final green phase**

```bash
python -m pytest tests/test_validate_style_anchor.py -q
```

Expected: `7 passed`.

- [ ] **Step 5: Commit**

```bash
git add tests/test_validate_style_anchor.py tools/validate_style_anchor.py
git commit -m "test: validate the shared style anchor"
```

---

### Task 2: Create the canonical raster and provenance

**Files:**
- Create: `pilots/01-agentic-discipline/references/style-anchor-light.png`
- Create: `pilots/01-agentic-discipline/references/style-anchor-light.provenance.md`

- [ ] **Step 1: Render the exact deterministic raster**

Run from the repository root:

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


def draw_text(draw, position, text, *, scale, tracking):
    x, y = position
    for character in text:
        if character == " ":
            x += 5 * scale + tracking
            continue
        for row, bits in enumerate(GLYPHS[character]):
            for column, bit in enumerate(bits):
                if bit == "1":
                    left = x + column * scale
                    top = y + row * scale
                    draw.rectangle(
                        (left, top, left + scale - 1, top + scale - 1),
                        fill=INK,
                    )
        x += 5 * scale + tracking


output = Path("pilots/01-agentic-discipline/references/style-anchor-light.png")
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

- [ ] **Step 2: Verify raster identity**

```bash
sha256sum pilots/01-agentic-discipline/references/style-anchor-light.png
git hash-object pilots/01-agentic-discipline/references/style-anchor-light.png
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
```

Expected:

```text
7ba4a191e97a777285b676b17484d8dbc64eed5216b1e1129634f5da81bd49d6
7d9ce5b37525cab14cde8bd8df61881fcd97003a
style anchor valid
```

When using the Git data API, compare its returned blob SHA with the expected Git blob SHA before advancing the branch.

- [ ] **Step 3: Complete manual review**

Confirm at full size and phone width:

```text
[pass] exact visible words only
[pass] one muted coral square
[pass] one thin graphite vector
[pass] at least 65% perceived negative space
[pass] technical but non-sci-fi typography
[pass] no logo, footer, frame, grid, coordinates, icons, gradients, shadows, or extra labels
[pass] readable at phone width
```

- [ ] **Step 4: Create the provenance sidecar**

Record source inputs, deterministic construction, exact copy, full metadata, SHA-256, Git blob SHA, manual checklist, and approval rationale. State explicitly that the raster is a targeted deterministic repair, not an original GPT Image 2 candidate.

- [ ] **Step 5: Commit**

```bash
git add pilots/01-agentic-discipline/references/style-anchor-light.png \
  pilots/01-agentic-discipline/references/style-anchor-light.provenance.md
git commit -m "feat: restore the Quiet Modular style anchor"
```

---

### Task 3: Enforce the repair and synchronize handoff state

**Files:**
- Modify: `.github/workflows/validate.yml`
- Modify: `STATUS.md`
- Modify: `CHANGELOG.md`
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/handoff/CODEX_IMAGE_GENERATION.md`

- [ ] **Step 1: Add the CI gate**

```yaml
      - name: Validate Pilot 01 style anchor
        run: >-
          python tools/validate_style_anchor.py
          pilots/01-agentic-discipline/references/style-anchor-light.png
```

- [ ] **Step 2: Synchronize repository state**

Record Task 4 as `Complete (repaired)` in `STATUS.md`, add the repair entry to `CHANGELOG.md`, and expose both the PNG and provenance sidecar in the README and agent handoff.

All Task 5 entry points must require:

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
```

Expected:

```text
16 passed
manifest valid
style anchor valid
```

- [ ] **Step 3: Run complete verification**

```bash
python -m pytest -q
python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
git diff --check
```

Expected: sixteen tests pass, both validators pass, and `git diff --check` has no output.

- [ ] **Step 4: Confirm Task 5 is untouched**

```bash
git diff --name-only main...HEAD | \
  grep -E 'prompts/01-hook|canonical/light/4x5/01-hook' && exit 1 || true
```

Expected: no output and exit code `0`.

- [ ] **Step 5: Open the PR and inspect GitHub Actions**

Open a draft PR from `codex/repair-task-4-style-anchor` into `main` titled:

```text
fix: complete Pilot 01 Task 4 style anchor
```

The PR body must state the root cause, restored artifacts, exact hashes, all red→green regression evidence, test/validator results, and the Task 5 scope boundary. Inspect every `Validate CSDL` job step before marking the repair complete.
