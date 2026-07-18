# 08 Node

## Purpose

Represent one stage, actor, option, concept, gate, or data point.

## Semantic meaning

A Node is one discrete semantic unit participating in a larger relation or set. Repeated Nodes must represent comparable units even when one becomes the Signal.

## Visual and spatial contract

Use zero to seven Nodes. A Node may be bare, open, solid, or bounded according to role. It needs an identifiable direct Label unless content or value is rendered inside it. It can belong to a Field, Frame, Cluster, Bridge topology, Vector route, Axis, or Loop.

## Dimensions and ranges

- width: `8–488 px`;
- height: `8–240 px`;
- area: `0.02–12%` per Node;
- count: up to seven at Level A, six at B, four conditionally at C.

## Allowed relations

- `inside → Field | Frame`;
- inbound `Cluster groups Node`;
- inbound `Bridge connected_to Node`;
- inbound `Vector directs Node`;
- inbound `Axis orders Node`;
- inbound `Loop repeats Node`;
- inbound `Label attached_to Node`;
- inbound `Signal highlights Node`;
- inbound `Legend maps_to Node` only for a validated multi-category analytical mapping.

## Forbidden relations

- `contains → Field`: a Node is not context;
- `separates → Divider`: a Node is not a boundary;
- `bounds → any`: scope belongs to Field or Frame;
- decorative points, UI pills, repeated cards, or unexplained icons.

## Compatible Visual DNA families

Direct evidence: Timeline, Matrix, Hierarchy, Architecture, Workflow, Loop, Pipeline, Decision Tree, Framework, and Chart.

## Expression levels

- **A:** maximum seven;
- **B:** maximum six;
- **C:** conditional maximum four with short direct Labels and one Signal.

## Typography and semantic color

Use direct neutral Labels and comparable type roles across repeated Nodes. Default is graphite. At most one Node carries the dominant Signal in current evidence.

## Do examples

- Timeline: five bare Nodes in exact order, VERIFY selected once.
- Matrix: four square Nodes at deliberate relative positions with direct Labels.

## Don't examples

- Do not use rounded interface pills, duplicated markers, avatars, or decorative network points.
- Do not vary shapes when members are semantically equal.

## Prompt DSL syntax

```text
Node(id=<id>, role=<stage|actor|option|concept|gate|data-point>)
```

Required fields: `id`, `role`. Optional fields: `content`, `state`, `value`, `unit`, `period`.

## Validation invariants

- one identifiable role per Node;
- repeated Nodes are semantically comparable;
- maximum one dominant selected Node in current contracts;
- no UI card/control treatment;
- direct identity remains readable at review scale.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.1 and Loop recipe;
- `patterns/visual-dna-sprint-01/specs/08-timeline.md`: ordered stages;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Timeline through Dashboard: accepted bare/open/solid/data Nodes and rejected UI treatments.
