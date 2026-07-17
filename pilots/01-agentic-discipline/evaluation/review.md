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

## Card 02 — Problem / Level A

**Canonical output:** `canonical/light/4x5/02-problem.png`

**Selected draft name:** `02-problem-v1.png`

**Selection:** explicitly approved by the user on 2026-07-17

**Promotion identity:** byte-for-byte exact selected normalized candidate

### Generation route

- Built-in GPT Image 2 generation was invoked three independent times with `prompts/02-problem.yaml` and the approved `references/style-anchor-light.png` reference.
- Each source output was mechanically normalized from `1122×1402` to `1080×1350` with `sips`; there was no crop, redraw, recolor, regeneration, or compositional edit.
- All three normalized candidates were reviewed together at full resolution and at `216×270` phone width.
- The user explicitly selected V1 after the side-by-side review.

### Candidate review

- `02-problem-v1.png` — **selected**. The incomplete Loop reads immediately, the separate coral dash has one unambiguous break-point role, the left-weighted composition preserves controlled asymmetry, and the headline, diagram, and consequences form the clearest single reading path at phone width.
- `02-problem-v2.png` — rejected. The larger centered Loop occupies too much of the field, weakens the intended Quiet asymmetry, and makes the reading path bend back toward the lower-left copy.
- `02-problem-v3.png` — rejected. The coral signal is rendered as a square Node rather than a distinct break point, creating the appearance of four Nodes and violating the specified component roles.

### Exact-copy review

Expected and observed copy:

```text
AD-HOC РОБОТА РОЗПАДАЄТЬСЯ МІЖ СЕСІЯМИ
Рішення губляться.
Перевірки повторюються.
Помилки повертаються.
```

Result: **pass — every visible character matches manifest card `02`; all text is horizontal and no additional labels are present.**

### Raster, identity, and mobile review

- selected built-in source: PNG, `1122×1402`, RGB, SHA-256 `be5fef28b1ebe7ffa5202c03fd4d9b86c6313fda1bedd86a33bc4574c19805da`;
- canonical output: PNG, `1080×1350`, RGB, `1,095,616` bytes;
- canonical SHA-256: `3b1693ed05ee6c61753fbd37e1b6f128333f3012da98f0ca91ca2a263c1c0525`;
- canonical Git blob SHA: `ddc8cf538f6e65c8f7c6dab8b3da14f4b566c3d0`;
- byte-for-byte identity with selected normalized `02-problem-v1.png` — pass;
- full-resolution review — pass;
- `216×270` phone-width review — pass;
- smooth Ukrainian-capable non-pixel typography — pass;
- exactly one incomplete Loop, three graphite square Nodes, and one coral break point — pass;
- logo, footer, frame, grid, coordinates, icons, UI chrome, extra labels, tangled fragments, explosion, shadow, glossy surface, or 3D treatment — absent.

### Visual mechanism

One thin graphite Loop fails at one coral break point while three square Nodes remain separated around the cycle; the three consequences below name what that discontinuity causes between sessions.

No displayed element can be removed without weakening the problem statement, the incomplete-cycle mechanism, or one of its three explicit consequences.

### Accepted rubric score

| Criterion | Score | Evidence |
|---|---:|---|
| clarity | 5 | The broken-cycle problem reads in one headline-to-Loop scan. |
| mobile_readability | 5 | Headline and all three consequences remain readable at phone width. |
| memorability | 4 | The single broken Loop is distinct without inflating the card to Level C. |
| csdl_identity | 4 | Quiet Modular typography, asymmetry, semantic geometry, and one coral Signal are recognizable. |
| restraint | 5 | The card contains only the required copy and one diagram. |
| text_fidelity | 5 | Exact canonical Ukrainian copy with no extra text. |
| semantic_integrity | 5 | Loop, Nodes, and coral break point each carry one explicit role. |

Average: **4.71 / 5**.

## Series-level checks

- Sequence follows `A → A → B → A → B → A → C`.
- No adjacent cards repeat the same dominant composition.
- The coral signal has one semantic role per card.
- Cards 01 and 07 are memorable but visibly different.
- Card 04 presents complementary mechanisms and does not manufacture a false rivalry.
- No card contains political, Soviet, revolutionary, or retro-propaganda cues.
