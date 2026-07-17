# Card 01 Hook — Provenance and Approval

**Artifact:** `01-hook.png`  
**Status:** Approved canonical Card 01 / Level A  
**Selected candidate:** `01-hook-v1.png`  
**Approval date:** 2026-07-17  
**SHA-256:** `cf97312ae89b7f03bf6c2f5c5e028b29c518b1d4146a0a24871cedf633ff2d9d`  
**Git blob SHA:** `eedd3701ccb72b983bfd14e148509ea0871d9514`

## Source contract

- `pilots/01-agentic-discipline/manifest.yaml`, card `01`
- `pilots/01-agentic-discipline/prompts/00-style-anchor.yaml`
- `pilots/01-agentic-discipline/prompts/01-hook.yaml`
- `pilots/01-agentic-discipline/references/style-anchor-light.png`
- Task 5 in `docs/superpowers/plans/2026-07-17-csdl-pilot-01.md`

## Generation and correction history

1. Built-in image generation was invoked three times with the approved prompt and style anchor. All three outputs were unrelated GitHub-interface screenshots, so they were rejected and were not committed as CSDL drafts.
2. The user explicitly approved a deterministic Pillow fallback for Task 5.
3. The first fallback candidate set was rejected after the user identified broken typography. Its renderer drew glyphs independently and damaged kerning, Ukrainian diacritics, and the `≠` sign.
4. The corrected renderer drew complete Unicode lines with antialiasing, using Inter Display Black for the headline and Inter Regular for supporting copy. Three corrected candidates were reviewed.
5. The user explicitly selected `01-hook-v1.png`.
6. The canonical PNG was reconstructed in GitHub Actions from the reviewed V1 coordinates, copy, palette, and geometry. The runner raster was compared with the locally reviewed V1 before promotion. Geometry, copy, colors, vector, and signal bounds matched. `4,854` pixels—approximately `0.333%` of the canvas—differed only because of font-rasterization and antialiasing differences between environments; no semantic or layout difference was introduced.

This artifact is therefore a transparent deterministic fallback, not a GPT Image 2 output.

## Exact visible copy

```text
СИЛЬНИЙ
АГЕНТ ≠
СТІЙКИЙ
РЕЗУЛЬТАТ

Стабільність з’являється, коли робота має
процес, перевірки й пам’ять.
```

Result: **pass — canonical Ukrainian copy only, in the intended reading order.**

## Raster metadata

- format: PNG
- dimensions: `1080×1350`
- color mode: RGB
- file size: `43,665` bytes
- exact paper color: `#F7F5F0`
- exact primary ink: `#1B1B19`
- exact secondary ink: `#535457`
- exact coral signal: `#C96157`
- unique raster colors: `479`, including antialiasing shades
- exact paper-colored pixels: approximately `90.67%` of the canvas
- coral square: one `190×190` block in the lower-right third
- vector: one thin graphite line terminating at the coral signal

## Candidate decision

- `01-hook-v1.png` — **selected**: clearest hierarchy, one continuous reading path, strongest phone-width legibility, and the quietest Level A expression.
- `01-hook-v2.png` — rejected: the detached inequality hinge introduced an unnecessary second focal stop.
- `01-hook-v3.png` — rejected: the vertical fault weakened the compact headline block and reduced mobile immediacy.
- the initial broken-font candidate set — rejected as a group before selection.

## Manual visual review

- [x] exact headline and supporting copy
- [x] correct Ukrainian diacritics and a clear `≠` sign
- [x] one large Anchor opposed by one small stable coral Signal
- [x] one functional Vector only
- [x] more than 70% perceived negative space
- [x] no extra labels, logo, footer, frame, grid, icons, or UI chrome
- [x] no gradient, shadow, glossy surface, or 3D treatment
- [x] technical but non-sci-fi typography
- [x] full-resolution review passed
- [x] phone-width review at `216×270` passed

## Accepted score

| Criterion | Score |
|---|---:|
| clarity | 5 |
| mobile readability | 5 |
| memorability | 4 |
| CSDL identity | 4 |
| restraint | 5 |
| text fidelity | 5 |
| semantic integrity | 5 |

Average: **4.71 / 5**.
