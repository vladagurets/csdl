# 001 Hero

## Problem

Make one proposition immediately understandable and memorable.

## Allowed scenarios

- opening thesis.
- section thesis.
- key takeaway.

## Ingredients and cardinality

- Required `Anchor`: 1–1.
- Required `Signal`: 1–1.

## Allowed relations

- `Signal highlights Anchor`.

## Forbidden relations

- `Anchor repeats Signal` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. place Anchor.
2. isolate supporting copy.
3. add one semantic Signal.

## Expression levels

- Level A: `allowed`.
- Level B: `allowed`.
- Level C: `allowed`.

## Compatible Visual DNA families

- `hero`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `left_to_right`, `top_left_to_bottom_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `supporting_copy`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `hero-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Expression: `A`.
- Density: `low`.
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
- one_main_idea.
- one_visual_mechanism.
- no_extra_text.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 01 Hero).
- `patterns/visual-dna-sprint-01/specs/01-hero.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `pilots/01-agentic-discipline/canonical/light/16x9/01-hook.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Hero`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
