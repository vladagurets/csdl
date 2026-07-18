# 022 Checklist

## Problem

Evaluate readiness through a bounded set of required questions with one selected gate.

## Allowed scenarios

- readiness review.
- preflight questions.
- completion gate.

## Ingredients and cardinality

- Required `Anchor`: 1–1.
- Required `Cluster`: 1–1.
- Required `Node`: 3–6.
- Required `Signal`: 1–1.
- Optional `Label`: 0–6.

## Allowed relations

- `Cluster groups Node`.
- `Signal highlights Node`.
- `Label attached_to Node`.

## Forbidden relations

- `Cluster orders Node` is forbidden because it substitutes another semantic mechanism.

## Assembly order

1. state the readiness question as one Anchor.
2. group three to six interrogative Nodes without sequence.
3. select one gate or unresolved question once.

## Expression levels

- Level A: `allowed`.
- Level B: `conditional` — Up to six questions remain peer gates without chronology.
- Level C: `forbidden` — A checklist needs multiple readable questions.

## Compatible Visual DNA families

- `framework`.

## Canvas and presentation constraints

- Canonical canvas: `1920×1080`, 16:9 landscape; safe margins `96×72` px.
- Reading paths: `top_left_to_bottom_right`.
- The composition must remain naturally readable at `1280×720` and preserve one main idea, one mechanism, and one dominant signal.

## Negative space, typography, and semantic color

- Negative space: 50–75 percent.
- Display/body/code roles: `modular_technical`, `neutral_sans`, and `technical_mono`; all body copy remains horizontal.
- Dominant signal: `coral`. Color reinforces form or label and never becomes the only carrier of meaning.

## Content contract

- Required bindings: `headline`, `questions`, `supporting`.
- Optional bindings: none.
- Copy/data is exact, order-preserving, and limited to 60 words or atomic values.
- Data contract: `none`.

## Prompt DSL v0.5

- Semantic mechanism: `peer-question-readiness-gate`.
- Required concerns: `semantic_intent`, `content`, `component_instances`, `relations`, `generation_constraints`, `provenance`.
- Optional fields: `component_instances[].attributes`, `provenance.source_prompt`.
- Component instances and relations use only Milestone 3 public vocabulary; content bindings remain separate from semantic intent and generation constraints.

## Deterministic defaults

- Component cardinality: `Anchor`=1, `Cluster`=1, `Node`=4, `Signal`=1, `Label`=0.
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
- questions are typographic modules, not colored cards.
- one coral marker only; no repeated checkmarks.
- no footer, logo, frame, large background shape, or extra text.
- all visible copy exact.
- Container or ad hoc layout and geometry primitives.
## Validation invariants

- Every required content binding is present and exact.
- Ingredient counts remain inside declared cardinality.
- Every instance and relation is permitted by Component Library v0.1.
- No undeclared layout or geometry terminology is present.
- One main idea, one visual mechanism, and one dominant Signal remain observable.

## Canonical examples and evidence

- `pilots/01-agentic-discipline/prompts/06-takeaway.yaml` — Canonical content and legacy mechanism. (accepted legacy Prompt DSL package).
- `pilots/01-agentic-discipline/evaluation/review.md` — Three-candidate selection, exact-copy, readability, and score evidence. (Slide 06 — Operational takeaway / Level A).
- `pilots/01-agentic-discipline/canonical/light/16x9/06-takeaway.png` — Accepted presentation-scale example. (canonical raster).

## Compatibility and rollback

- Legacy names: `Checklist`.
- Migration: Legacy 2x2 zone language is discarded; Cluster membership and direct Node content preserve the checklist semantics.
- Rollback: Revert the additive recipe record and derived outputs; accepted Pilot prompt and raster bytes remain unchanged.
