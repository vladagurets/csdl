# 14 Label

## Purpose

Name or qualify one component directly so meaning does not depend on position or color alone.

## Semantic meaning

A Label is a short textual attachment with exactly one semantic target. Headlines owned by Anchor are not automatically Labels; long explanatory body copy is not a Label.

## Visual and spatial contract

Attach each Label closely and unambiguously to one target. Keep it horizontal by default. A short Label may rotate when an Axis requires it, but body copy never rotates. Analytical values retain their unit, period, and direct target association.

## Dimensions and ranges

- default type size: `24–30 px`;
- default line height: `1.10–1.25`;
- rendered width: `24–980 px`;
- rendered height: `20–88 px`;
- area: `0.02–8%` per Label;
- count: up to 25 at Level A for exact analytical lookup.

## Allowed relations

- `attached_to → any` with exactly one target;
- `inside → Field | Frame` when the target's scope requires it;
- inbound `Legend maps_to Label` only for a validated indirect analytical key.

## Forbidden relations

- `directs → any`: text alone does not establish a route;
- `produces → any`: a Label names but does not cause a result;
- `repeats → Loop`: repeated words do not establish recurrence;
- one Label floating between multiple possible targets.

## Compatible Visual DNA families

Direct evidence: Big Number, Collision, Timeline, Matrix, Hierarchy, Architecture, Workflow, Loop, Pipeline, Decision Tree, Framework, KPI, Table, Chart, and Dashboard.

## Expression levels

- **A:** maximum 25; short Axis Labels may rotate;
- **B:** maximum 12; short Axis Labels may rotate;
- **C:** conditional maximum four; only essential short Labels remain and body copy is excluded.

## Typography and semantic color

Use the Foundation `label` token and neutral high-legibility sans by default. Display roles remain with Anchor. Default color is `ink.primary`. A colored Label counts as part of the one Signal role; it is not a free secondary accent.

## Do examples

- Matrix: label each Axis and Node directly; keep the selected Node's Label neutral.
- Chart: directly label all four points and retain `DEMO DATA` source provenance.

## Don't examples

- Do not color a Label as a duplicate of an already solid Signal Node.
- Do not omit units, periods, source text, or exact punctuation from analytical Labels.

## Prompt DSL syntax

```text
Label(id=<id>, text=<content-ref>, target=<instance-id>)
```

Required fields: `id`, `text`, `target`. Optional fields: `role`, `rotation`, `color`, `unit`, `period`.

## Validation invariants

- exactly one target per Label;
- readable at the source family's review scale;
- colored Labels count toward the single Signal role;
- quantitative value, unit, period, and order remain exact;
- body copy is never rotated or misclassified as a Label.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, sections 8.4–8.5: size, line-height, and rotation rules;
- `patterns/visual-dna-sprint-01/specs/19-chart.md`: direct point Labels and exact-data requirement;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Matrix, KPI, Table, Chart, and Dashboard: accepted direct labels plus duplicate/missing-label rejections.
