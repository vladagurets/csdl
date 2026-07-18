# 05 Cluster

## Purpose

Group related concepts, evidence, or measures without automatically implying order.

## Semantic meaning

A Cluster is a set whose members share one role, model, or review context. It establishes membership and comparable weight; it does not establish chronology, direction, or containment by itself.

## Visual and spatial contract

Use two to six members and one Cluster per composition. Express grouping through proximity, alignment, and repetition rather than card shells. Members may be Nodes, Labels, or a subordinate Pulse. One Signal may select a member without changing the other members' semantic equality.

## Dimensions and ranges

- width: `244–1472 px`;
- height: `64–720 px`;
- area: `2–40%`;
- members: two to six;
- count: zero or one Cluster.

## Allowed relations

- `groups → Node | Label | Pulse`;
- `inside → Field | Frame` when context or scope is declared;
- inbound `Signal highlights Cluster` or one member.

## Forbidden relations

- `orders → any`: order belongs to Axis;
- `directs → any`: action belongs to Vector or Bridge;
- `repeats → Loop`: recurrence is not grouping;
- decorative enclosure or network connections between equal members.

## Compatible Visual DNA families

Direct evidence: Framework and Dashboard.

## Expression levels

- **A:** one Cluster, maximum four members;
- **B:** one, maximum six members;
- **C:** forbidden because multiple peer members conflict with the short single-peak contract.

## Typography and semantic color

Use equal Label roles for comparable members. Default color is graphite. At most one member carries the Signal; member Labels stay neutral unless the Label itself is the declared Signal.

## Do examples

- Framework: four equal open Nodes form one non-sequential mental model.
- Dashboard: three supporting measures form a subordinate aligned Cluster beside one Pulse.

## Don't examples

- Do not turn equal concepts into four dashboard cards.
- Do not add arrows that imply a false sequence.

## Prompt DSL syntax

```text
Cluster(id=<id>, members=<instance-ids>, role=<group-role>)
```

Required fields: `id`, `members`, `role`. Optional fields: `alignment`, `equality`, `signal_member`.

## Validation invariants

- two to six semantically related members;
- no implied chronology without a separate Axis;
- maximum one Signal member;
- proximity and alignment replace decorative enclosure.

## Milestone 2 evidence

- `specs/2026-07-17-csdl-v0.1-design.md`, section 10.1: related-concept/evidence group;
- `patterns/visual-dna-sprint-01/specs/16-framework.md`: equal non-sequential concept Nodes;
- `patterns/visual-dna-sprint-01/evaluation/review.md`, Framework and Dashboard: accepted peer and subordinate metric Clusters.
