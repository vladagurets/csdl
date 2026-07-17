# Style Anchor Light — GPT Image 2 Provenance and Review

**Artifact:** `style-anchor-light.png`

**Status:** Approved canonical reference for Pilot 01 Tasks 6–11

**Approval date:** 2026-07-17

**Selected candidate:** `style-anchor-light-inter-v1-selected-source.png`

**Selected source SHA-256:** `58b6bbb2fdff56b9b87fbb602f341952ed9ff636977111efd6808ecbb2a767fc`

**Canonical SHA-256:** `c262389d5fbfbd8b2f90039f671d81625476aebf40dfbfc5f19373c6fd91f675`

**Canonical Git blob SHA:** `2608f9c3f4a068aa0dcdd3226b6fb4e169553dc9`

## Why this file replaced the previous anchor

The first Task 4 repair used a deterministic custom 5×7 bitmap alphabet. The user rejected that pixel typography as an active visual reference because it did not represent the approved Ukrainian-capable direction and could bias later cards toward retro-computer lettering. The bitmap raster is removed from the active tree and remains available only through Git history.

The replacement completes the original reference-first intent with GPT Image 2, three candidate variants, exact Ukrainian copy review, explicit human selection, and a canonical 1080×1350 output.

## Source inputs

- `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`
- `pilots/01-agentic-discipline/canonical/light/4x5/01-hook.png` as the primary typography and visual reference
- `references/quiet-modular-density-calibration.png` as the broader Quiet Modular calibration reference used during initial exploration
- Foundation v0.1 and Task 4 of `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`

## Generation and selection history

1. Three exploratory GPT Image 2 candidates were generated from the broader density-calibration reference. They proved Ukrainian text rendering but did not match the already approved Card 01 typography closely enough.
2. The user identified `canonical/light/4x5/01-hook.png` as the preferred typography source. Its approved fallback uses Inter Display Black for the headline and Inter Regular for supporting copy.
3. Three new GPT Image 2 candidates were generated reference-first from Card 01:
   - `style-anchor-light-inter-v1-selected-source.png` — **selected**. Strongest continuity with Card 01, clearest Ukrainian hierarchy, and the user's explicit visual preference.
   - `style-anchor-light-inter-v2-raw.png` — rejected. Quieter scale, but weaker display presence and less faithful to the preferred Card 01 expression.
   - `style-anchor-light-inter-v3-raw.png` — rejected. Mixed weights created a more poster-like first line and a less balanced hierarchy.
4. The user supplied `Generated image 5.png` and explicitly confirmed that this exact image was the selected source. Its SHA-256 matches the original built-in GPT Image 2 output byte-for-byte.
5. The selected `1122×1402` RGB source was resized mechanically to `1080×1350` with Pillow LANCZOS. It was not regenerated, cropped, recolored, redrawn, or compositionally altered.

Draft candidates remain under the ignored `drafts/` tree. The selected source hash above is persistent review evidence even though drafts are not committed.

## Approved copy

Expected and observed visible copy:

```text
ТИХА
МОДУЛЬНІСТЬ
ОДНА ІДЕЯ.
ОДИН СИГНАЛ.
```

Result: **pass — exact Ukrainian words only, with correct `І` and `Ь`; no additional labels or copy.**

## Typography decision

- family direction: the Ukrainian-capable Inter display/body relationship already approved on Card 01;
- headline: heavy Inter-style display weight;
- supporting copy: regular neutral Inter-style sans;
- rendering: complete antialiased Unicode words, not separately constructed glyphs;
- exclusions: no pixel, bitmap, dot-matrix, segmented, retro-computer, sci-fi novelty, Soviet, revolutionary, or imitation-1920s typography.

The selected headline uses a broad upper-left field rather than the original literal five-column span. The user explicitly chose this exact composition after seeing the alternatives; that selection supersedes the earlier five-column calibration constraint without changing the locked Quiet Modular direction.

## Raster metadata

- format: PNG;
- dimensions: `1080×1350`;
- color mode: RGB;
- unique raster colors: `8,862`, including antialiasing and the selected GPT tonal variation;
- canonical SHA-256: `c262389d5fbfbd8b2f90039f671d81625476aebf40dfbfc5f19373c6fd91f675`;
- canonical Git blob SHA: `2608f9c3f4a068aa0dcdd3226b6fb4e169553dc9`.

The dedicated CLI validator pins the canonical SHA-256 in addition to checking PNG format, complete data, dimensions, and color mode. CI therefore rejects both file corruption and any unreviewed replacement, including restoration of the superseded pixel raster.

## Manual visual review

- [x] exact Ukrainian copy only
- [x] smooth non-pixel typography consistent with Card 01
- [x] one coral signal square
- [x] one thin graphite vector
- [x] at least 65% perceived negative space
- [x] one top-left-to-bottom-right reading path
- [x] no logo, footer, frame, visible grid, coordinates, icons, UI chrome, or extra labels
- [x] full-resolution review passed
- [x] `216×270` phone-width review passed
- [x] user explicitly selected the exact source image

## Approval rationale

This anchor preserves the visual mechanism and restraint of Quiet Modular while using proven Ukrainian typography from Card 01. It removes the misleading pixel-font precedent and is the active primary reference for Cards 02–07.
