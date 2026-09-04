# 011 Architecture

## Problem

Explain stable system boundaries and permitted interactions.

## Allowed scenarios

- software context.
- agent system.
- service boundary.

## Ingredients and cardinality

- Required `Field`: 1–2.
- Required `Node`: 2–7.
- Required `Bridge`: 1–4.
- Required `Label`: 2–7.

## Allowed relations

- `Field contains Node`.
- `Bridge connected_to Node`.
- `Label attached_to Node`.

## Forbidden relations

- `Bridge orders Node` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. define system Field.
2. place bounded Nodes.
3. connect only permitted relations.
4. emphasize one boundary.

## Expression levels

- Level A: `allowed`.
- Level B: `allowed`.
- Level C: `forbidden` — No accepted evidence supports this recipe at the expression level.

## Compatible Visual DNA families

- `architecture`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `outside_to_inside`, `center_out`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `data_blue`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `nodes`, `relations`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `architecture-mechanism`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`, `provenance.dataset`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Field`=1, `Node`=4, `Bridge`=3, `Label`=4.
- Expression: `B`.
- Density: `medium`.
- Reading path: `outside_to_inside`.
- Palette: light Muted Signal on warm paper; output is exact `1920×1080` PNG.

## Hard exclusions

- extra text.
- logos or repeated footers.
- UI chrome or decorative card shells.
- decorative coordinates or random dot fields.
- gradients, shadows, glossy surfaces, or 3D.
- political, Soviet, or revolutionary-poster styling.
- pixel, bitmap, dot-matrix, segmented, or retro-computer lettering.
- cloud icons.
- server racks.
- code windows.
- dashboard cards.
- unlabeled connectors.
- decorative network nodes.
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

- `patterns/visual-dna-sprint-01/manifest.yaml` — Problem, scenarios, components, assembly, levels, content, and exclusions. (family 11 Architecture).
- `patterns/visual-dna-sprint-01/specs/11-architecture.md` — Canonical Markdown semantic and Prompt DSL evidence. (complete family contract).
- `patterns/visual-dna-sprint-01/canonical/light/16x9/9.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Architecture`.
- Migration: Legacy Prompt DSL v0.1 content is rebound mechanically to explicit v0.5 instances, relations, and deterministic constraints; source files remain unchanged.
- Rollback: Revert the additive recipe record and derived outputs; accepted source prompts and raster bytes remain unchanged.
