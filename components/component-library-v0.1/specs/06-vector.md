# 06 Vector

## Purpose

Communicate direction, action, or transformation between declared semantic sources and targets.

## Semantic meaning

A Vector is an active route whose direction changes how connected components are read. It can express one state change, separate operational actions, or one continuous transformation carrier.

## Visual and spatial contract

Every Vector has a source, target, and role. Use a single segment for one transition, separate segments for Workflow actions, and one continuous carrier for Pipeline transformation. Each instance has at most one terminal arrowhead; bends are semantic only when stage transformation requires them.

## Dimensions and ranges

- width: `24–1536 px`;
- height: `1–720 px`;
- area: `0.02–8%`;
- count: up to three at Level A, two at B, one conditionally at C.

## Allowed relations

- `directs → Node | Anchor | Field`;
- `inside → Field` for a scoped route;
- inbound direct Label;
- inbound Signal on the declared carrier or transition.

## Forbidden relations

- `repeats → Loop`: Vector alone never closes recurrence;
- `orders → Axis`: an unlabeled route is not a reference structure;
- `connected_to → Bridge`: topology is not continuous action;
- a decorative arrow with no source, target, or role.

## Compatible Visual DNA families

Direct evidence: Before / After, Workflow, and Pipeline.

## Expression levels

- **A:** maximum three;
- **B:** maximum two;
- **C:** conditional maximum one decisive direction.

## Typography and semantic color

Vector carries no text inside its thin route. Labels attach to the route or endpoints. Default is neutral; one semantic carrier may use the declared Signal color.

## Do examples

- Workflow: three separate neutral Vectors connect four actions without forming a shared Axis.
- Pipeline: one continuous data-blue carrier passes through all five gates.

## Don't examples

- Do not use an arrow as decoration or as an unlabeled quantitative Axis.
- Do not break a declared continuous carrier between transformation gates.

## Prompt DSL syntax

```text
Vector(id=<id>, source=<instance-id>, target=<instance-id>, role=<action|transformation|carrier>)
```

Required fields: `id`, `source`, `target`, `role`. Optional fields: `continuity`, `direction`, `signal_state`.

## Validation invariants

- one declared source, target, and semantic role;
- arrow direction matches reading/transformation direction;
- separate Workflow Vectors never become a shared Axis;
- continuous Pipeline carrier stays unbroken through every gate.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.4: direction/action/transformation;
- `patterns/visual-dna-sprint-01/specs/12-workflow.md`: separate action route;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Before / After, Workflow, and Pipeline: state change, segmented actions, and continuous carrier.
