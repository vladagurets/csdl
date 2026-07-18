# 11 Architecture

## Problem

Explain stable system boundaries and permitted interactions rather than an execution sequence.

## Allowed scenarios

Software context, agent system, service boundary, or a small component map.

## Semantic components

One `Field` defines system scope; `Node`s define actors; `Bridge`s define permitted relations.

## Assembly order

1. Define the system Field.
2. Place bounded Nodes according to ownership.
3. Connect only permitted relations.
4. Emphasize one meaningful boundary or relation.

## Expression levels

Levels A and B are allowed. B is canonical because the relation topology is the teaching object. C is excluded.

## Typography and spacing

Use uniform Node labels, neutral connector lines, 96 px margins, and enough separation to avoid crossing relations.

## Signal constraints

Dusty data blue identifies the technical boundary and tool relation, occupying no more than 10%.

## Canonical content

Exact headline; `USER`, `AGENT`, `TOOLS`, `MEMORY`; and only the three declared relations.

## Hard exclusions

No cloud icons, server racks, code windows, dashboard cards, unlabeled connectors, decorative network nodes, or invented services.

## Prompt DSL contract

`prompts/11-architecture.yaml` defines a four-node context architecture with explicit directed and bidirectional relations.

## Acceptance criteria

System boundary and every relation are unambiguous; no workflow implication; exact labels and directions.

## Canonical evidence

One new canonical example selected from three built-in GPT Image 2 candidates.
