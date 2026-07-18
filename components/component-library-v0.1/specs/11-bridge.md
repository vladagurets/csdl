# 11 Bridge

## Purpose

Connect semantically distant components for topology, ownership, or explicit branching without implying continuous progress.

## Semantic meaning

A Bridge is a declared relation between separate Nodes, Fields, Frames, or Clusters. It can be undirected, directed, or bidirectional according to content, but it is not a continuous operational carrier.

## Visual and spatial contract

Every Bridge has exactly two endpoints and one role. Use up to four. Avoid unrelated crossings. Add direct relation or branch Labels when direction alone does not preserve meaning.

## Dimensions and ranges

- width: `24–1536 px`;
- height: `1–720 px`;
- area: `0.02–8%`;
- count: zero to four;
- endpoints: exactly two.

## Allowed relations

- `connected_to → Node | Field | Frame | Cluster`;
- `directs → Node` only for explicit direction/branch semantics;
- `inside → Field`;
- inbound direct Label.

## Forbidden relations

- `orders → Axis`: topology is not a continuous reference structure;
- `repeats → Loop`;
- `produces → Collision`;
- `separates → Divider`;
- unlabeled crossings or decorative network links.

## Compatible Visual DNA families

Direct evidence: Hierarchy, Architecture, and Decision Tree.

## Expression levels

- **A:** maximum four;
- **B:** maximum four;
- **C:** forbidden because multiple topology relations conflict with a short single-peak composition.

## Typography and semantic color

Use direct relation or branch Labels where needed; never float a caption between unrelated links. Default is neutral. One risk or technical relation may carry the Signal.

## Do examples

- Architecture: exactly three directed/bidirectional Bridges and no invented service relation.
- Decision Tree: two attached, non-crossing, mutually exclusive labeled branches.

## Don't examples

- Do not use Bridge for a continuous Workflow/Pipeline route.
- Do not cross unrelated relations or omit branch meaning.

## Prompt DSL syntax

```text
Bridge(id=<id>, source=<instance-id>, target=<instance-id>, role=<topology|ownership|branch>)
```

Required fields: `id`, `source`, `target`, `role`. Optional fields: `direction`, `label`, `branch_value`, `signal_state`.

## Validation invariants

- exactly two endpoints and one relation role;
- direction/branch Labels agree with content;
- unrelated Bridges never cross;
- continuous operational routes use Vector instead.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.4: distant-concept connection;
- `patterns/visual-dna-sprint-01/specs/11-architecture.md`: stable permitted topology;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Hierarchy, Architecture, and Decision Tree: ownership, topology, and branching behavior.
