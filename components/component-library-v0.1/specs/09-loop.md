# 09 Loop

## Purpose

Represent a closed recurring process whose output changes or feeds the next cycle.

## Semantic meaning

A Loop is one directed recurrence over three to five ordered stages. Repetition is the mechanism, not a decorative circular arrangement.

## Visual and spatial contract

Use one Loop. Place three to five Nodes in exact cyclic order, expose one direction, and close the route exactly once. Keep the center open at Level A; allow only short center copy at B/C. One Node may carry the Signal.

## Dimensions and ranges

- width: `360–980 px`;
- height: `360–760 px`;
- area: `10–45%`;
- Nodes: three to five;
- closure: exactly one;
- count: zero or one Loop.

## Allowed relations

- `repeats → Node`;
- `orders → Node` cyclically;
- `inside → Field`;
- inbound stage Labels;
- inbound one Signal.

## Forbidden relations

- `connected_to → Bridge`: topology does not create recurrence;
- `separates → Divider`;
- `produces → Collision`;
- broken closure, duplicated markers, orbit decoration, or UI pills.

## Compatible Visual DNA families

Direct evidence: Loop.

## Expression levels

- **A:** one, up to five Nodes, no center copy;
- **B:** one, up to five, short center copy allowed;
- **C:** conditional one with three to four directly labeled stages and very short center copy.

## Typography and semantic color

Use direct neutral stage Labels. Default connector is neutral. Exactly one current/compounding Node may carry the Signal; multiple colored stages require evidence beyond v0.1.

## Do examples

- Use the Pilot-backed five-stage order and mark COMPOUND once.

## Don't examples

- Do not use rounded interface pills or duplicate Node markers.
- Do not leave a return arrow visibly open or add orbit lines.

## Prompt DSL syntax

```text
Loop(id=<id>, members=<node-ids>, direction=<clockwise|counterclockwise>, closed=true)
```

Required fields: `id`, `members`, `direction`, `closed`. Optional fields: `active_node`, `center_label`.

## Validation invariants

- three to five Nodes in exact cyclic order;
- route closes exactly once;
- one unambiguous direction;
- maximum one dominant Signal Node;
- decorative circular placement without closure fails.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, recipe 013: expression and stage rules;
- `patterns/visual-dna-sprint-01/specs/13-loop.md`: closed ordered mechanism;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Loop Pilot audit: accepted closure and rejected UI/duplicate-marker variants.
