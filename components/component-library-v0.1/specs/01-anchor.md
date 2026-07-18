# 01 Anchor

## Purpose

Carry the composition's dominant proposition or central concept.

## Semantic meaning

An Anchor is the first semantic read and the ownership root for subordinate content. It is defined by conceptual dominance, not by raw area: a large plane without content ownership is not an Anchor.

## Visual and spatial contract

Use one Anchor by default. Two peer Anchors are permitted only when comparison or Collision is the declared mechanism. An Anchor may sit inside a Field, receive direct Labels, or be highlighted by one Signal. It must preserve one unambiguous primary idea.

## Dimensions and ranges

- width: `122–1274 px`;
- height: `44–936 px`;
- area: `1–35%` of the canvas;
- Level A negative space: normally `60–75%`;
- count: one by default, two only for evidenced peer semantics.

These ranges include typographic Anchors and semantic blocks. They do not authorize decorative scale.

## Allowed relations

- `inside → Field` for declared context;
- inbound `Label attached_to Anchor` for direct naming or qualification;
- inbound `Signal highlights Anchor` for the one dominant emphasis;
- `Anchor overlaps Collision` only when the intersection is the visual mechanism.

## Forbidden relations

- `maps_to → Legend`: a primary proposition is not an indirect key;
- `repeats → Loop`: repetition alone does not turn the main idea into a cycle;
- a second peer Anchor without comparison or collision semantics;
- a decorative plane promoted by size alone.

## Compatible Visual DNA families

Direct evidence: Hero, Cover, Quote, Big Number, Comparison, Collision, Hierarchy, and Framework.

## Expression levels

- **A:** one or two peer Anchors, maximum `18%` area;
- **B:** one or two, maximum `28%` area when relationship pressure is the teaching object;
- **C:** conditional, maximum two and `35%` area; copy stays short and represents one proposition or peer-force pair.

## Typography and semantic color

Use Modular Technical display typography for textual Anchors, keep text horizontal, and permit at most one typographic trick. Default color is `ink.primary`. Signal color may target the Anchor but cannot create another semantic owner.

## Do examples

- Hero: one proposition owns the first read and terminates at one small Signal.
- Collision: two peer Anchors converge into one named result.

## Don't examples

- Do not treat a large background plane as an Anchor when it owns no content.
- Do not add a second unsupported headline at peer weight.

## Prompt DSL syntax

```text
Anchor(id=<id>, role=<primary|peer>, content=<copy-ref>)
```

Required fields: `id`, `role`. Optional fields: `content`, `weight`, `span`.

## Validation invariants

- at least one Anchor owns the main idea in every compatible editorial composition;
- two Anchors require peer comparison or Collision semantics;
- size alone never establishes Anchor status;
- the Anchor remains the first semantic read after a Signal is applied.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.1: Foundation Anchor meaning;
- `patterns/visual-dna-sprint-01/specs/01-hero.md`, Semantic components: one proposition Anchor;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Hero and Collision accepted records: one-primary and two-peer behavior.
