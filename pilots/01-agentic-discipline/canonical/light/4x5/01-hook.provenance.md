# Card 01 Hook — Provenance and Approval

**Artifact:** `01-hook.png`  
**Status:** Approved canonical Card 01 / Level A  
**Selected candidate:** `01-hook-v1.png`  
**Approval date:** 2026-07-17  
**SHA-256:** `0e5dd316842d5e36a18bd54a9b69b85ab1e70af53709f68e3735cf154bef407b`
**Git blob SHA:** `a9676cee42dd31870c683be1a8cb8c7be93855f1`

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
6. The initially promoted canonical file was a semantically identical re-render, not a byte-for-byte copy. That did not satisfy the literal promotion contract and was subsequently replaced.
7. The final canonical PNG is the exact approved V1 byte stream. SHA-256 and Git blob identity were both verified before promotion, and CI now rejects any future byte drift.

This artifact is a transparent deterministic fallback, not a GPT Image 2 output.

## Exact reproduction environment

The approved candidate was reproduced and promoted only after matching all of the following:

- Debian 13 / trixie;
- Python `3.13.5`;
- Pillow `12.2.0`;
- RAQM `0.10.3` with FriBiDi `1.0.16`;
- FreeType `2.14.3`;
- zlib `1.3.1`;
- `InterDisplay-Black.otf` SHA-256 `84ca5a51b3303c01b48cdd271637d3d20c263e09d00ec0ff2a945f122492a4d0`;
- `Inter-Regular.otf` SHA-256 `d4f2b9e148059a15f014cb0f0b8fea8cd11bfa447dd483bedf1b0adc0e2ba799`.

RAQM is required. Rendering the same strings with Pillow's BASIC layout produces different glyph placement and is not canonical.

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
- file size: `43,522` bytes
- exact paper color: `#F7F5F0`
- exact primary ink: `#1B1B19`
- exact secondary ink: `#535457`
- exact coral signal: `#C96157`
- unique raster colors: `480`, including antialiasing shades
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
- [x] canonical PNG is byte-for-byte identical to the selected V1

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
