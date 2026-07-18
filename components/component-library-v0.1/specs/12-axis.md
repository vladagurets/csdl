# 12 Axis

## Purpose

Establish ordered progression, continuous comparison, lookup alignment, support alignment, or quantitative domain.

## Semantic meaning

An Axis is an open reference structure that makes order, dimension, lookup, or scale explicit. Its semantic mode determines its invariants; Timeline order and Chart scale are not interchangeable.

## Visual and spatial contract

Use one Axis for sequence/support and two for coordinate, lookup, or quantitative structures. Every Axis declares a semantic direction. Quantitative mode declares the domain and exact values; coordinate mode declares independent dimensions; lookup mode preserves aligned headers and values.

## Dimensions and ranges

- width: `122–1728 px`;
- height: `1–864 px`;
- area: `0.05–15%`;
- count: zero to two;
- closure: open.

## Allowed relations

- `orders → Node | Label | Pulse`;
- `inside → Field | Frame`;
- inbound direct Labels;
- inbound one Signal on a transition, value, series, or endpoint.

## Forbidden relations

- `repeats → Loop`: Axis never closes recurrence;
- `produces → Collision`: Axis does not create an intersection result;
- `separates → Divider`: scope distinction is not scale/order;
- pseudo-precise ticks, reversed order, or distorted values.

## Compatible Visual DNA families

Direct evidence: Timeline, Matrix, KPI, Table, Chart, and Dashboard.

## Expression levels

- **A:** maximum two;
- **B:** maximum two;
- **C:** forbidden because lookup and scale require stable repeated structure.

## Typography and semantic color

Use direct Labels, horizontal by default; only short Axis Labels may rotate. Quantitative Labels use tabular figures. Default line is neutral; one semantic series, transition, or endpoint may carry the Signal.

## Do examples

- Timeline: one horizontal sequence Axis with five exact stages.
- Matrix: two independent named coordinate Axes without fake ticks.
- Chart: honest `0–100%` domain and four direct value Labels.

## Don't examples

- Do not truncate an unlabeled quantitative domain.
- Do not close the Axis into a cycle or use it as a Divider.

## Prompt DSL syntax

```text
Axis(id=<id>, mode=<sequence|coordinate|lookup|support|quantitative>, direction=<semantic-direction>)
```

Required fields: `id`, `mode`, `direction`. Optional fields: `domain`, `order`, `scale`, `unit`.

## Validation invariants

- exactly one declared semantic mode and direction;
- quantitative mode declares honest domain and exact ordered values;
- coordinate mode declares independent named dimensions;
- Axis remains open and never substitutes for Loop recurrence;
- no pseudo-precision unsupported by content.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.4 and Analytical Mode;
- `patterns/visual-dna-sprint-01/specs/08-timeline.md`: chronological order;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Matrix, KPI, Table, Chart, and Dashboard: coordinate, support, lookup, and quantitative behavior.
