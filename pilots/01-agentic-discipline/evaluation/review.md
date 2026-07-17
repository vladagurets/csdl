# Pilot 01 Visual Review

## Review protocol

For each card:

1. View at full resolution.
2. View its generated mobile preview at 100% browser size.
3. Compare every visible word against `manifest.yaml` manually; do not accept approximate Ukrainian text.
4. Name the visual mechanism in one sentence.
5. Identify any element that can be removed without reducing meaning.
6. Score all seven rubric criteria.

## Card 01 — Hook / Level A

**Canonical output:** `canonical/light/4x5/01-hook.png`  
**Selected draft name:** `01-hook-v1.png`  
**Selection:** explicitly approved by the user on 2026-07-17

### Generation route

- Built-in image generation was invoked three times with `prompts/01-hook.yaml` and the approved style anchor.
- All three generated outputs were unrelated GitHub-interface screenshots. They were rejected and not committed as CSDL drafts.
- The user explicitly approved a deterministic Pillow fallback.
- The first Pillow candidate set was rejected after the user identified broken typography caused by independent glyph rendering.
- The renderer was corrected to draw complete Unicode lines with antialiasing, Inter Display Black for the headline, and Inter Regular for supporting copy.
- Three corrected candidates were then reviewed.

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

### Raster and mobile review

- format: PNG — pass
- dimensions: `1080×1350` — pass
- color mode: RGB — pass
- SHA-256: `cf97312ae89b7f03bf6c2f5c5e028b29c518b1d4146a0a24871cedf633ff2d9d`
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

The detailed fallback and raster provenance is persisted in `canonical/light/4x5/01-hook.provenance.md`.

## Series-level checks

- Sequence follows `A → A → B → A → B → A → C`.
- No adjacent cards repeat the same dominant composition.
- The coral signal has one semantic role per card.
- Cards 01 and 07 are memorable but visibly different.
- Card 04 presents complementary mechanisms and does not manufacture a false rivalry.
- No card contains political, Soviet, revolutionary, or retro-propaganda cues.
