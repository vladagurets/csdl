# 003 Quote

## Problem

Give one exact statement enough space and hierarchy to be read as an idea, not decoration.

## Allowed scenarios

- principle.
- testimony.
- chapter pause.

## Ingredients and cardinality

- Required `Anchor`: 1–1.
- Required `Signal`: 1–1.

## Allowed relations

- `Signal highlights Anchor`.

## Forbidden relations

- `Anchor orders Signal` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. set quote as Anchor.
2. isolate attribution.
3. add one small Signal.

## Expression levels

- Level A: `allowed`.
- Level B: `allowed`.
- Level C: `forbidden` — No accepted evidence supports this recipe at the expression level.

## Compatible Visual DNA families

- `quote`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `top_left_to_bottom_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `quote`, `attribution`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `quote-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Anchor`=1, `Signal`=1.
- Expression: `A`.
- Density: `low`.
- Reading path: `top_left_to_bottom_right`.
- Palette: light Muted Signal on warm paper; output is exact `1920×1080` PNG.

## Hard exclusions

- extra text.
- logos or repeated footers.
- UI chrome or decorative card shells.
- decorative coordinates or random dot fields.
- gradients, shadows, glossy surfaces, or 3D.
- political, Soviet, or revolutionary-poster styling.
- pixel, bitmap, dot-matrix, segmented, or retro-computer lettering.
- invented speaker.
- portrait.
- giant decorative quote marks.
- rotated copy.
- UI chrome.
- logo.
- footer.
- gradients.
- shadows.
- 3D.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 03 Quote).
- `patterns/visual-dna-sprint-01/specs/03-quote.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `patterns/visual-dna-sprint-01/canonical/light/16x9/03-quote.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Quote`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
