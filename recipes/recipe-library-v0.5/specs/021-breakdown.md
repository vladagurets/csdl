# 021 Breakdown

## Problem

Show that an expected recurring system fails to retain continuity and exposes detached consequences.

## Allowed scenarios

- failed recurrence.
- lost context.
- broken operating cycle.

## Ingredients and cardinality

- Required `Loop`: 1–1.
- Required `Node`: 3–5.
- Required `Label`: 1–5.
- Required `Signal`: 1–1.

## Allowed relations

- `Loop repeats Node`.
- `Loop orders Node`.
- `Label attached_to Node`.
- `Signal highlights Node`.

## Forbidden relations

- `Loop connected_to Node` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. declare the expected closed recurrence.
2. place three to five consequence Nodes in exact content order.
3. highlight the failed transition or consequence once.

## Expression levels

- Level A: `allowed`.
- Level B: `conditional` — The recurrence and consequences remain the only mechanism.
- Level C: `forbidden` — Failure diagnosis requires readable consequences rather than a short Signal peak.

## Compatible Visual DNA families

- `loop`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `left_to_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `supporting_lines`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `expected-recurrence-with-one-failed-transition`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Loop`=1, `Node`=3, `Label`=3, `Signal`=1.
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
- compose directly for 16:9.
- the broken loop is the only diagram.
- nodes are simple squares without icons.
- no fragments, explosion, footer, logo, grid, or extra text.
- all text horizontal and exact.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `pilots/01-agentic-discipline/prompts/02-problem.yaml` — Canonical content and legacy mechanism. (accepted legacy Prompt DSL package).
- `pilots/01-agentic-discipline/evaluation/review.md` — Three-candidate selection, exact-copy, readability, and score evidence. (Slide 02 — Problem / Level A).
- `pilots/01-agentic-discipline/canonical/light/16x9/2.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Breakdown`.
- Migration: Legacy incomplete Loop wording becomes a closed expected Loop with one failed-transition Signal so Milestone 3 Loop invariants remain intact.
- Rollback: Revert the additive recipe record and derived outputs; accepted Pilot prompt and raster bytes remain unchanged.
