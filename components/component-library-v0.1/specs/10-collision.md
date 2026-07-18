# 10 Collision

## Purpose

Show two forces or Anchors producing one consequential intersection, constraint, or synthesis.

## Semantic meaning

Collision is a named result created by one functional overlap between exactly two inputs. Adjacency, a connector between stopped forms, or a decorative Venn overlap is insufficient.

## Visual and spatial contract

Use one Collision with two equal inputs and one overlap. Name the result at the intersection. Preserve at least `50%` negative space at Level B and keep the interaction intrinsic, controlled, and readable.

## Dimensions and ranges

- width: `244–1472 px`;
- height: `144–720 px`;
- area: `2–55%`;
- inputs: exactly two;
- overlap: exactly one;
- result: required.

## Allowed relations

- `overlaps → Anchor` for both inputs;
- `produces → Signal` for the named result;
- `inside → Field`;
- inbound direct Labels.

## Forbidden relations

- `groups → Cluster`: peers are forces, not a set;
- `orders → Axis`;
- `directs → Vector`;
- `repeats → Loop`;
- debris, sparks, rays, shards, unlabeled overlap, or decorative `VS`.

## Compatible Visual DNA families

Direct evidence: Collision.

## Expression levels

- **A:** forbidden because interaction pressure is the teaching object;
- **B:** one, maximum `55%` area and minimum `50%` negative space;
- **C:** conditional one with very short inputs and result.

## Typography and semantic color

Inputs use equal display roles and horizontal text. The overlap may carry the one semantic Signal and its result Label; no explosion language or duplicate accents are allowed.

## Do examples

- Use two equal graphite planes crossing once with the coral overlap named НАДІЙНІСТЬ.

## Don't examples

- Do not stop two planes beside a connector and call it Collision.
- Do not add impact debris or leave the overlap unnamed.

## Prompt DSL syntax

```text
Collision(id=<id>, inputs=<anchor-ids>, result=<content-ref>)
```

Required fields: `id`, `inputs`, `result`. Optional fields: `overlap_role`, `signal_state`.

## Validation invariants

- exactly two inputs and one named result;
- intrinsic single overlap;
- overlap is functional, never an explosion effect;
- Level B preserves at least `50%` negative space.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.4: conflict/comparison/synthesis point;
- `patterns/visual-dna-sprint-01/specs/06-collision.md`: two Anchors, one overlap, one Signal;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Collision accepted record: intrinsic overlap and rejected adjacent/overdense variants.
