# 03 Field

## Purpose

Establish context, environment, coordinate space, or state scope without defaulting to a closed panel.

## Semantic meaning

A Field is the space in which components share context or state. It can be implicit, use an open boundary, or use one restrained semantic plane. It is never a generic card background.

## Visual and spatial contract

Use one Field for shared context and two only for peer comparison or before/after states. A Field may contain Anchors, Nodes, Clusters, or Frames. Its boundary can remain incomplete when proximity and spacing already make scope clear.

## Dimensions and ranges

- width: `244–1728 px`;
- height: `144–936 px`;
- area: `12–90%` of the canvas;
- count: zero to two;
- Level A normally preserves at least `60%` negative space;
- Level B normally preserves at least `45%` negative space.

## Allowed relations

- `contains → Anchor | Node | Cluster | Frame`;
- inbound `Divider separates Field` for peer scopes;
- `bounds → Node` when context membership is the meaning.

## Forbidden relations

- `directs → any`: direction belongs to Vector, Axis, Bridge, or Loop;
- `maps_to → any`: indirect key mapping belongs to Legend;
- a closed decorative panel with no context meaning;
- repeated Fields used as dashboard cards.

## Compatible Visual DNA families

Direct evidence: Cover, Comparison, Before / After, Matrix, and Architecture.

## Expression levels

- **A:** maximum two Fields, at least `60%` negative space by default;
- **B:** maximum two, at least `45%` negative space;
- **C:** conditional maximum one, supporting a short cover or culmination.

## Typography and semantic color

A Field carries no body-copy role. Labels name its scope. Default rendering is warm paper, open space, or a low-chroma boundary. A Field may be the target of one semantic Signal but cannot become a generic filled card.

## Do examples

- Architecture: one open technical Field places USER outside and AGENT, TOOLS, MEMORY inside.
- Comparison: two equal open Fields preserve complementary weight.

## Don't examples

- Do not wrap every content group in a closed background panel.
- Do not use multiple empty regions as decorative layout columns.

## Prompt DSL syntax

```text
Field(id=<id>, role=<context|state|coordinate>)
```

Required fields: `id`, `role`. Optional fields: `boundary`, `signal_state`, `openness`.

## Validation invariants

- every Field declares a context or state role;
- a Field never exists solely to decorate the background;
- two Fields require peer comparison or before/after semantics;
- membership remains unambiguous at `1280×720` review scale.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.1: context/environment meaning;
- `patterns/visual-dna-sprint-01/specs/05-comparison.md` and `11-architecture.md`: peer and system scope;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Matrix and Architecture: accepted open coordinate and system Fields.
