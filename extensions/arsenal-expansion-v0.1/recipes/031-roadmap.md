# Recipe 031: Roadmap

## Problem

Coordinate parallel workstreams, milestone conditions, bounded windows, and
dependencies on one declared time domain.

## Distinction

`Timeline` owns a single chronological sequence. `Roadmap` owns multiple
workstreams plus cross-stream dependencies and milestone conditions.

## Ingredients

One time `Axis`, two to four workstream `Cluster` instances, milestones as
`Node`, explicit `Threshold` conditions, optional `Band` windows, one `Signal`,
and an optional critical `Trace`.

## Acceptance

Dates or periods are explicit. Workstreams remain peers. Dependency and timing
are not inferred from proximity alone.
