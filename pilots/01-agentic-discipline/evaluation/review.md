# Pilot 01 Visual Review

## Review protocol

For each card:

1. View at full resolution.
2. View its generated mobile preview at 100% browser size.
3. Compare every visible word against `manifest.yaml` manually; do not accept approximate Ukrainian text.
4. Name the visual mechanism in one sentence.
5. Identify any element that can be removed without reducing meaning.
6. Score all seven rubric criteria.

## Shared style anchor — Task 4 reopened typography correction

**Canonical output:** `references/style-anchor-light.png`

**Selected source:** `style-anchor-light-inter-v1-selected-source.png`

**Selection:** explicitly approved by the user on 2026-07-17

### Candidate review

- `style-anchor-light-inter-v1-selected-source.png` — **selected**. Exact file supplied back by the user as `Generated image 5.png`; strongest continuity with Card 01's Inter Display Black / Inter Regular hierarchy and the user's preferred balance of display weight, supporting copy, vector, signal, and negative space.
- `style-anchor-light-inter-v2-raw.png` — rejected. The quieter scale weakened the display presence and did not match the explicitly preferred candidate.
- `style-anchor-light-inter-v3-raw.png` — rejected. Mixed headline weights made `ТИХА` too dominant and reduced the balanced Quiet Modular hierarchy.

Three earlier exploratory candidates generated from the broad density-calibration sheet were rejected before the final candidate set because they did not match the already approved Card 01 typography closely enough.

### Exact-copy review

Expected and observed:

```text
ТИХА
МОДУЛЬНІСТЬ
ОДНА ІДЕЯ.
ОДИН СИГНАЛ.
```

Result: **pass — exact Ukrainian copy, including `І` and `Ь`, with no additional text.**

### Raster and mobile review

- selected GPT source: PNG, `1122×1402`, RGB, SHA-256 `58b6bbb2fdff56b9b87fbb602f341952ed9ff636977111efd6808ecbb2a767fc`;
- canonical output: PNG, `1080×1350`, RGB, SHA-256 `c262389d5fbfbd8b2f90039f671d81625476aebf40dfbfc5f19373c6fd91f675`;
- normalization: Pillow LANCZOS resize only; no crop, redraw, recolor, regeneration, or composition change;
- full-resolution review — pass;
- `216×270` phone-width review — pass;
- pixel/bitmap/dot-matrix typography — absent;
- logo, footer, frame, grid, coordinates, icons, UI chrome, or extra labels — absent.

The selected composition uses a broad upper-left headline field rather than the original literal five-column span. The user's explicit selection of this exact image is the recorded approval for that override.

## Card 01 — Hook / Level A

**Canonical output:** `canonical/light/4x5/01-hook.png`  
**Selected draft name:** `01-hook-v1.png`  
**Selection:** explicitly approved by the user on 2026-07-17
**Promotion identity:** byte-for-byte exact selected candidate

### Generation route

- Built-in image generation was invoked three times with `prompts/01-hook.yaml` and the approved style anchor.
- All three generated outputs were unrelated GitHub-interface screenshots. They were rejected and not committed as CSDL drafts.
- The user explicitly approved a deterministic Pillow fallback.
- The first Pillow candidate set was rejected after the user identified broken typography caused by independent glyph rendering.
- The renderer was corrected to draw complete Unicode lines with antialiasing, Inter Display Black for the headline, and Inter Regular for supporting copy.
- Three corrected candidates were then reviewed.
- The user selected V1, and the final canonical PNG is the exact V1 byte stream rather than a subsequent approximation or re-render.

### Candidate review

- `01-hook-v1.png` — **selected**. Clearest hierarchy, one uninterrupted top-left-to-lower-right reading path, strongest phone-width legibility, and the quietest Level A expression.
- `01-hook-v2.png` — rejected. The detached `≠` hinge created a second focal stop and slowed the headline scan.
- `01-hook-v3.png` — rejected. The vertical fault weakened the compact headline block and reduced mobile immediacy.
- initial broken-font candidate set — rejected as a group before selection because kerning, Ukrainian diacritics, and the `≠` sign were visibly damaged.

### Exact-copy review

Expected and observed copy:

```text
СИЛЬНИЙ АГЕНТ ≠ СТІЙКИЙ РЕЗУЛЬТАТ
Стабільність з’являється, коли робота має процес, перевірки й пам’ять.
```

Result: **pass — every visible word matches manifest card `01`; line wrapping preserves the exact words and reading order.**

### Raster, identity, and mobile review

- format: PNG — pass
- dimensions: `1080×1350` — pass
- color mode: RGB — pass
- file size: `43,522` bytes — pass
- SHA-256: `0e5dd316842d5e36a18bd54a9b69b85ab1e70af53709f68e3735cf154bef407b` — pass
- Git blob SHA: `a9676cee42dd31870c683be1a8cb8c7be93855f1` — pass
- byte-for-byte identity with selected `01-hook-v1.png` — pass
- one coral object only — pass
- exact paper-colored area: approximately `90.67%` — pass
- full-resolution review — pass
- `216×270` phone-width preview — pass
- no logo, footer, frame, grid, icons, extra labels, UI chrome, gradient, shadow, or 3D treatment — pass

### Visual mechanism

One large typographic Anchor presents the unstable proposition; one small, stable coral Signal in the lower-right third is connected by a single functional graphite Vector.

No displayed element can be removed without weakening either the proposition, the stabilizing contrast, or the reading path.

### Accepted rubric score

| Criterion | Score | Evidence |
|---|---:|---|
| clarity | 5 | Main proposition reads immediately. |
| mobile_readability | 5 | Headline and two supporting lines remain readable at phone width. |
| memorability | 4 | Strong Anchor-versus-Signal image without Level C dramatization. |
| csdl_identity | 4 | Quiet Modular palette, geometry, asymmetry, and semantic signal are recognizable. |
| restraint | 5 | Every visible element has a role; no removable decoration remains. |
| text_fidelity | 5 | Exact canonical Ukrainian copy. |
| semantic_integrity | 5 | Typography, Vector, and coral Signal each have one explicit role. |

Average: **4.71 / 5**.

The detailed fallback, renderer requirements, and exact raster provenance are persisted in `canonical/light/4x5/01-hook.provenance.md`.

## Series-level checks

- Sequence follows `A → A → B → A → B → A → C`.
- No adjacent cards repeat the same dominant composition.
- The coral signal has one semantic role per card.
- Cards 01 and 07 are memorable but visibly different.
- Card 04 presents complementary mechanisms and does not manufacture a false rivalry.
- No card contains political, Soviet, revolutionary, or retro-propaganda cues.
