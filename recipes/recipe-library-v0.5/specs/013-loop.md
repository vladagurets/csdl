# 013 Loop

## Problem

Show a repeating process whose output changes the next cycle.

## Allowed scenarios

- feedback cycle.
- learning loop.
- recurring operation.

## Ingredients and cardinality

- Required `Loop`: 1–1.
- Required `Node`: 3–5.
- Required `Label`: 3–5.
- Required `Signal`: 1–1.

## Allowed relations

- `Loop repeats Node`.
- `Loop orders Node`.
- `Label attached_to Node`.
- `Signal highlights Node`.

## Forbidden relations

- `Loop connected_to Node` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. place ordered Nodes.
2. connect as one closed Loop.
3. select the compounding Node.

## Expression levels

- Level A: `allowed`.
- Level B: `allowed`.
- Level C: `allowed`.

## Compatible Visual DNA families

- `loop`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `cyclic_clockwise`, `cyclic_counterclockwise`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `stages`, `supporting_copy`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `loop-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Loop`=1, `Node`=5, `Label`=5, `Signal`=1.
- Expression: `B`.
- Density: `medium`.
- Reading path: `cyclic_clockwise`.
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
- exact_stage_order.
- no_ui_containers.
- no_extra_text.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 13 Loop).
- `patterns/visual-dna-sprint-01/specs/13-loop.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `pilots/01-agentic-discipline/canonical/light/16x9/05-synthesis.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Loop`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
