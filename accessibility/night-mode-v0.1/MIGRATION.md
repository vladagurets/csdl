# Night Mode and Accessibility v0.1 Migration

## Versioning decision

Night Mode and Accessibility v0.1 is an additive extension under D-032. Prompt DSL v0.5, Component Library v0.1, Recipe Library v0.5, and Analytical Mode v0.1 remain unchanged and validate independently.

## Mechanical migration path

1. Keep the existing CSDL generation or analytical package byte-identical.
2. Choose one accessibility output profile: light, night, monochrome, or projector.
3. Reference the source package by repository-relative path and exact kind.
4. Declare every informative text role and adjacent foreground/background token pair.
5. Declare every meaningful graphical object, component, token pair, and critical stroke width.
6. Declare each semantic meaning and at least one non-color carrier.
7. For analytical output, retain direct values, units, source, order, missing states, uncertainty, forecast, direction, and weight from Analytical Mode.
8. Build the accessibility package and validate its source digest, semantic equivalence, contrast, fallbacks, and deterministic provenance.

The migration never recolors an accepted raster. It produces a deterministic specification for a future renderer or reviewed generation workflow.

## Compatibility

- Prompt DSL: `0.5`, unchanged.
- Component Library: `0.1`, exactly fifteen public components.
- Recipe Library: `0.5`, exactly 23 recipes.
- Analytical Mode: `0.1`, all ten families and quantitative invariants preserved.
- Accepted rasters: immutable evidence, not migration outputs.

## Breaking-change rule

A future contract that removes a profile, token role, threshold, fallback carrier, semantic state, compatibility mapping, output/provenance field, or proof invariant requires a new version and a documented source-to-source migration. It must not silently alter v0.1 packages.
