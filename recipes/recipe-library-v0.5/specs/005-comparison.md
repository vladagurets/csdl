# 005 Comparison

## Problem

Compare two systems without implying conflict unless conflict is the content.

## Allowed scenarios

- approach comparison.
- complementary roles.
- trade-off.

## Ingredients and cardinality

- Required `Anchor`: 2–2.
- Required `Field`: 2–2.
- Required `Divider`: 1–1.
- Required `Signal`: 1–1.

## Allowed relations

- `Field contains Anchor`.
- `Divider separates Field`.
- `Signal highlights Anchor`.

## Forbidden relations

- `Divider orders Field` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. create two open Fields.
2. align criteria.
3. separate with Divider.
4. add one Signal.

## Expression levels

- Level A: `allowed`.
- Level B: `allowed`.
- Level C: `allowed`.

## Compatible Visual DNA families

- `comparison`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `left_to_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `left`, `right`, `supporting_copy`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 140 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `comparison-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Anchor`=2, `Field`=2, `Divider`=1, `Signal`=1.
- Expression: `A`.
- Density: `medium`.
- Reading path: `left_to_right`.
- Palette: light Muted Signal on warm paper; output is exact `1920×1080` PNG.

## Hard exclusions

- extra text.
- logos or repeated footers.
- UI chrome or decorative card shells.
- decorative coordinates or random dot fields.
- gradients, shadows, glossy surfaces, or 3D.
- political, Soviet, or revolutionary-poster styling.
- pixel, bitmap, dot-matrix, segmented, or retro-computer lettering.
- exact_copy.
- complementary_not_adversarial.
- repeated_colored_bullets.
- no_extra_text.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 05 Comparison).
- `patterns/visual-dna-sprint-01/specs/05-comparison.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `pilots/01-agentic-discipline/canonical/light/16x9/4.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Comparison`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
