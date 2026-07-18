# Analytical Mode v0.1 Migration

## Versioning decision

Analytical Mode v0.1 is an additive extension. Prompt DSL v0.5 remains unchanged and continues to validate independently.

## Mechanical migration path

1. Keep the existing Prompt DSL v0.5 outline/package and its exact content.
2. Select one compatible analytical recipe: `018 Table`, `019 Chart`, or `020 Dashboard`.
3. Create a typed v0.1 dataset with stable identity/version, fields, records, ordering, missing states, transformations, and provenance.
4. Create a proof/source definition that references the typed dataset and the unchanged v0.5 recipe.
5. Bind fields to internal analytical marks and declare domains, scales, order, units, labels, missing, uncertainty, forecast, geography, or network semantics as applicable.
6. Express public presentation semantics with D-029 components and relations only.
7. Run `tools/build_analytical_mode.py`; validate the resulting package independently against the canonical dataset.

The accepted Milestone 4 bounded Chart proof remains valid. It is compatibility evidence for the v0.1 line family; no migration rewrites that package or the Milestone 2 dataset.

## Compatibility

- Prompt DSL: `0.5`, unchanged.
- Component Library: `0.1`, exactly fifteen public components.
- Recipe Library: `0.5`, exactly 23 recipes.
- Accepted rasters: immutable evidence; no generated image is a migration output.

## Breaking-change rule

A future Analytical Mode schema that removes or changes a required field, field type, missing status, transformation operation, internal mark, or family invariant requires a new version and a documented source-to-source migration. It must not silently alter v0.1 packages.
