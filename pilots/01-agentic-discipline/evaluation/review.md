# Pilot 01 Visual Review — 16:9 Restart

## Review protocol

For the shared anchor and each slide:

1. Review all three candidates together.
2. Verify every visible character against the Prompt DSL and `manifest.yaml`.
3. Inspect at full `1920×1080` resolution and at `1280×720` review size.
4. Reject portrait framing, extra text, weak hierarchy, non-semantic decoration, or an incorrect expression level.
5. Record filenames, rejection reasons, selected candidate, raster metadata, visual mechanism, strongest decision, removable-element check, remaining risk, and selection rationale.
6. Score all seven rubric criteria for each accepted slide.

## Restart record

The earlier 4:5 style anchor, Cards 01–02, phone-width evidence, and accepted scores were superseded by decision D-027. They are not reused as visual or scoring evidence for this 16:9 series and remain available only in Git history.

## Shared style anchor

**Selected:** `style-anchor-light-v2.png`
**Canonical:** `references/style-anchor-light.png`
**Canonical SHA-256:** `6c8504246745d77efe19749e77d51d2cd1d1db26b004975298215bd395311c2a`

- `style-anchor-light-v1.png` — rejected: too large and dense for the Quiet Modular default.
- `style-anchor-light-v2.png` — selected: best landscape balance, clearest Inter-style hierarchy, one left-to-right Vector, and one semantic coral Signal.
- `style-anchor-light-v3.png` — rejected: display weight is too forceful and condensed.

Exact copy: pass. Source `1672×941` RGB; canonical `1920×1080` RGB after resize-only normalization. Full-resolution and `1280×720` review: pass. Detailed hashes and rationale are recorded in the adjacent provenance sidecar.

## Slides 01–07

All sources were built-in GPT Image 2 landscape outputs at `1672×941`, RGB. Every reviewed candidate was mechanically resized with `sips` to `1920×1080`; there was no crop, redraw, recolor, text edit, or compositional change. Every selected slide passed full-resolution and `1280×720` review.

### Slide 01 — Hook / Level A

**Selected:** `01-hook-v2.png`
**Canonical SHA-256:** `39de00d730e534c942fbb96e6fe5cf932e7e14c0a89926877406ba3cade62d8c`

- `01-hook-v1.png` — rejected: placing `≠` at the end of the first line creates a detached secondary stop.
- `01-hook-v2.png` — selected: strongest two-line proposition, exact copy, and clearest left-to-right Anchor → Vector → Signal path.
- `01-hook-v3.png` — rejected: smaller headline scale weakens the opening hook.

Exact-copy review: pass for the headline and supporting sentence, including `≠`, `’`, `і`, and `й`; no extra text. Visual mechanism: one typographic Anchor opposed by one stable coral Signal. Strongest decision: the symbol begins the second line and reads as the hinge. Element removed during selection: detached end-of-line hinge. Remaining risk: none material at `1280×720`. Score: `4.86`.

### Slide 02 — Problem / Level A

**Selected:** `02-problem-v2.png`
**Canonical SHA-256:** `1f8cc56f434268ec61622722d3da7d7d38567d7d9079d7d1c2273c1a872f1e5b`

- `02-problem-v1.png` — rejected: the oversized Loop competes with the headline and makes the coral break feel detached.
- `02-problem-v2.png` — selected: exact copy, exactly three filled graphite Nodes, and one unmistakable coral break in a quiet incomplete Loop.
- `02-problem-v3.png` — rejected: outlined Nodes weaken the shared component grammar.

Exact-copy review: pass for headline and all three consequence lines; no extra text. Visual mechanism: a cycle loses continuity at one coral break while three Nodes remain separated. Strongest decision: compact right-side Loop balances the three-line headline. Element removed during selection: oversized diagram. Remaining risk: none material. Score: `4.86`.

### Slide 03 — Four-layer model / Level B

**Selected:** `03-model-v2.png`
**Canonical SHA-256:** `d64bcc7b9c558e69ea990b3bd25061254ea36a76d595b2b3f5bdfbc74f339576`

- `03-model-v1.png` — rejected: four large rectangular blocks read like dashboard cards rather than Nodes.
- `03-model-v2.png` — selected: four equal square Nodes form one clear controlled sequence; the fourth coral Node is the single active state.
- `03-model-v3.png` — rejected: the branching connector implies a hierarchy not present in the manifest.

Exact-copy review: pass for headline and all four supporting sentences, including `Пам’ять`; no layer labels were invented. Visual mechanism: four aligned Nodes form a controlled Cluster and one Vector. Strongest decision: horizontal progression makes the landscape canvas do semantic work. Element removed during selection: dashboard-like blocks and branching hierarchy. Remaining risk: service blue is visible but subordinate. Score: `4.86`.

### Slide 04 — Complementary comparison / Level A

**Selected:** `04-comparison-v3.png`
**Canonical SHA-256:** `c97326715a6345fe099d08a197dc4422411a6a529082934d8f40c63de3049aff`

- `04-comparison-v1.png` — rejected: six coral bullets plus a coral square create seven competing signals.
- `04-comparison-v2.png` — rejected: repeated coral bullets again violate one-signal restraint.
- `04-comparison-v3.png` — selected: exact ten text blocks, equal fields, graphite dashes, one divider, and one small coral Signal.

Exact-copy review: pass for the headline, titles, six points, and supporting sentence; English case, plus signs, and Ukrainian text all match the manifest. Visual mechanism: two complementary open Fields separated by one Divider. Strongest decision: neutral bullets keep the mechanisms equal instead of adversarial. Element removed during selection: six decorative coral bullets. Remaining risk: this is the densest slide, but all text passes `1280×720`. Score: `4.86`.

### Slide 05 — Synthesis loop / Level B

**Selected:** `05-synthesis-v1.png`
**Canonical SHA-256:** `1b7a4045fdbf616f8787dbfaf81161158b06d9efda67d7361102653d810497c8`

- `05-synthesis-v1.png` — selected: five simple Nodes, one active coral Node, thin connectors, exact stage order, and no UI containers.
- `05-synthesis-v2.png` — rejected: five rounded pills turn the diagram into interface chrome.
- `05-synthesis-v3.png` — rejected: stage pills plus separate circular markers duplicate the Node role.

Exact-copy review: pass for headline, supporting sentence, and all five English stages in the required order. Visual mechanism: one Loop compounds learning from UNDERSTAND through COMPOUND. Strongest decision: bare circular Nodes preserve semantic geometry. Element removed during selection: colored stage containers. Remaining risk: none material. Score: `5.00`.

### Slide 06 — Operational takeaway / Level A

**Selected:** `06-takeaway-v2.png`
**Canonical SHA-256:** `422cab41115b8b69334653f05237055357ae526c93c2a631ac7550ef61522a45`

- `06-takeaway-v1.png` — rejected: full cross-divider lines make the open Cluster read as a table.
- `06-takeaway-v2.png` — selected: exact copy, four equally readable open typographic modules, and one small coral marker on the fourth question.
- `06-takeaway-v3.png` — rejected: oversized question typography pushes the slide toward poster expression.

Exact-copy review: pass for headline, four questions, and supporting sentence; all question marks and Ukrainian letters match. Visual mechanism: one open 2×2 Cluster with the fourth Node selected. Strongest decision: alignment alone forms the Cluster. Element removed during selection: table grid. Remaining risk: none material. Score: `4.86`.

### Slide 07 — Share formula / Level C

**Selected:** `07-share-card-v2.png`
**Canonical SHA-256:** `43fc54769dfa4c737da35b9c71b668a0bcd239671b319f3621a0e4e2ea37ad29`

- `07-share-card-v1.png` — rejected: the graphite block is too small to make the intended Collision legible.
- `07-share-card-v2.png` — selected: exact formula, strong but restrained Signal plane, and a clear compact graphite Anchor at the intersection.
- `07-share-card-v3.png` — rejected: the larger graphite block compresses the formula and overstates the Collision.

Exact-copy review: pass for both formula lines, including both multiplication signs, `=`, comma, and `ПАМ’ЯТЬ`. Visual mechanism: one coral Signal plane intersects one graphite Anchor while the formula bridges them. Strongest decision: the right-side plane creates the only Level C peak in the series. Element removed during selection: overlarge collision mass. Remaining risk: none material. Score: `5.00`.

## Series-level result

- rhythm A → A → B → A → B → A → C: pass;
- Slides 01–06 remain quieter than Slide 07: pass;
- no repeated logo, footer, border, or UI chrome: pass;
- one dominant signal color per slide: pass;
- Slide 04 is complementary, not adversarial: pass;
- all manifest copy exact: pass;
- full-resolution and `1280×720` readability: pass;
- contact sheet coherence: pass.
