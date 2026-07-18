# 02 Signal

## Purpose

Identify the one state, result, transition, value, path, or boundary needing immediate attention.

## Semantic meaning

Signal is an emphasis role attached to another component. It is not a synonym for coral, a required detached shape, or a license for decoration. A solid Node, heavier endpoint, boundary, overlap, marker, or plane can render the same Signal role.

## Visual and spatial contract

A composition contains at most one dominant Signal role and every Signal has exactly one target. Intrinsic rendering is preferred when the selected state belongs to a Node, Axis, Pulse, or Collision. An attached marker or semantic plane is allowed when it owns a distinct role.

## Dimensions and ranges

- area: `0.04–25%` of the canvas;
- Level A maximum: `8%`;
- Level B maximum: `12%`;
- Level C maximum: `25%`;
- count: zero or one dominant Signal role.

Family contracts may narrow these ceilings, as KPI does at `6%` and Table at `5%`.

## Allowed relations

- `highlights → any` with exactly one semantic target;
- `attached_to → any` when a separate marker is necessary;
- `inside → Field` when scope is part of the meaning;
- inbound `Collision produces Signal` for a named intersection;
- inbound `Legend maps_to Signal` only in a validated multi-category analytical exception.

## Forbidden relations

- `groups → any`: Signal does not own grouping;
- `orders → any`: Signal does not establish sequence or scale;
- more than one dominant target;
- color-only meaning or duplicate colored Label emphasis.

## Compatible Visual DNA families

Direct evidence: Hero, Cover, Quote, Big Number, Comparison, Collision, Before / After, Timeline, Matrix, Workflow, Loop, Pipeline, Decision Tree, Framework, KPI, Table, Chart, and Dashboard.

Hierarchy and Architecture still define a semantic signal in accepted review, but their active component arrays keep scope/topology components primary; the component compatibility matrix therefore records only direct manifest usage in v0.1.

## Expression levels

- **A:** one Signal, maximum `8%` area;
- **B:** one Signal, maximum `12%` area;
- **C:** one Signal, maximum `25%` area.

## Typography and semantic color

Use only semantic palette roles: coral for action/change, data blue for data/technical scope, ochre for risk/attention, and mineral green for stable completion. Labels remain neutral unless the Label itself is the declared Signal. Color must be reinforced by form, weight, position, or text.

## Do examples

- Timeline: VERIFY is one solid coral Node while its Label stays neutral.
- Chart: W4 is heavier without displacement and direct Labels preserve values.

## Don't examples

- Do not color both VERIFY and its Label as separate dominant cues.
- Do not add an unrelated underline, dot field, or second plane in the signal color.

## Prompt DSL syntax

```text
Signal(id=<id>, target=<instance-id>, role=<semantic-role>)
```

Required fields: `id`, `target`, `role`. Optional fields: `color`, `area_percent`, `rendering`.

## Validation invariants

- exactly one target per Signal;
- at most one dominant Signal role per composition;
- area stays within the expression and family ceiling;
- color is not the only carrier of meaning;
- intrinsic target state and attached markers are counted together, not as separate Signal allowances.

## Milestone 2 evidence

- `DECISIONS.md`, D-010 and D-013: one dominant signal and one mechanism;
- `specs/2026-07-17-csdl-v0.1-design.md`, section 9.3: semantic palette and area limits;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Timeline, Framework, KPI, Table, Chart, and Dashboard: accepted and rejected signal behavior.
