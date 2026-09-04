# Recipe 030: Layer Stack

## Problem

Explain ordered layers of abstraction, protocol, or responsibility.

## Distinction

`Hierarchy` owns parent-child decomposition and authority. `Layer Stack` owns
an ordered set of peer scopes where each layer has a distinct responsibility.

## Ingredients

One ordering `Axis`, three to six `Cluster` layers, neutral `Divider`
separations, direct `Label` instances, and at most one `Signal`.

## Acceptance

The abstraction direction is named. Adjacency does not imply dependency unless
explicitly stated. Repeated decorative slabs are forbidden.
