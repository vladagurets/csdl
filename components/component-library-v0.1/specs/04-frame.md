# 04 Frame

## Purpose

Create a functional boundary for scope, lookup, or nested ownership depth.

## Semantic meaning

A Frame is a visible or implied boundary whose edge improves interpretation. It owns analytical lookup or ownership scope, not generic visual grouping.

## Visual and spatial contract

Prefer open Frames and sparse rules. Close a Frame only when enclosure is itself meaningful. Frames may nest to express up to four ownership levels or contain Nodes, Axes, Labels, and subordinate Frames. A Frame may sit inside a Field.

## Dimensions and ranges

- width: `122–1728 px`;
- height: `64–936 px`;
- area: `1–80%` of the canvas;
- count: zero to four;
- nesting depth: zero to four.

## Allowed relations

- `contains → Node | Axis | Label`;
- `contains → Frame` only for explicit nested ownership depth;
- `inside → Field` for bounded scope inside context;
- `bounds → any` when the boundary changes interpretation.

## Forbidden relations

- `directs → any`: a Frame is not a route;
- `repeats → Loop`: repeated edges do not establish recurrence;
- decorative card shells;
- arbitrary closed boxes around every Node.

## Compatible Visual DNA families

Direct/bounded evidence: Hierarchy and Table.

The Hierarchy mapping replaces the retired `Container` alias with the accepted raster's actual nested open-boundary behavior. Table retains its original open lookup Frame.

## Expression levels

- **A:** maximum four, nesting depth four;
- **B:** maximum four, nesting depth four;
- **C:** forbidden because repeated functional boundaries conflict with a short single-peak composition.

## Typography and semantic color

Frame has no text role; Labels name scope or lookup coordinates directly. Default color is `neutral.line`. Signal color may mark a meaningful current scope or boundary but cannot turn the Frame into decoration.

## Do examples

- Hierarchy: four progressively nested open Frames express OBJECTIVE → MILESTONE → TASK → CHECK ownership depth.
- Table: sparse horizontal rules create one open lookup Frame.

## Don't examples

- Do not wrap every row, cell, or Node in a card shell.
- Do not use one continuous Frame edge as a workflow arrow.

## Prompt DSL syntax

```text
Frame(id=<id>, scope=<scope-ref>)
```

Required fields: `id`, `scope`. Optional fields: `openness`, `nesting_depth`, `boundary_style`, `signal_state`.

## Validation invariants

- every Frame changes scope, lookup, or ownership interpretation;
- nested Frames preserve one unambiguous ownership path;
- a Frame cannot be justified by visual grouping alone;
- Level C contains no Frame.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.1 and D-029 note: functional scope boundary;
- `patterns/visual-dna-sprint-01/specs/10-hierarchy.md`: nested open Frame mapping;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Hierarchy and Table: accepted nested-depth and sparse lookup boundaries.
