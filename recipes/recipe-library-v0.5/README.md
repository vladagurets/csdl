# CSDL Recipe Library v0.5

This directory contains the versioned Recipe Library and Prompt DSL v0.5 contract. Markdown specifications are canonical; YAML records mirror them for deterministic selection, validation, migration, and package building.

The complete library contains 23 evidence-backed recipes. The first twenty correspond one-to-one with Visual DNA Sprint 1. Breakdown, Checklist, and Formula preserve distinct accepted Pilot 01 needs. Full Analytical Mode remains out of scope.

## Evidence convention

Every recipe cites existing Foundation, Pilot 01, Visual DNA, or Component Library evidence. An evidence entry states the path, locator, and supported claim. Raster files calibrate a recipe but never replace its Markdown contract.

## Staged validation

`validate_recipe_library.py` and `validate_prompt_dsl.py` accept `require_complete=False` for honest stacked work. Incomplete mode permits a canonical subsequence of complete records or proofs; it never permits a partial record. Strict mode requires all 23 records and all canonical proofs.

## Generated outputs

`index.yaml`, `compatibility.yaml`, and `selection-index.yaml` are derived from `manifest.yaml` plus per-recipe records. Run the builder and then the index validator; a second build must create no diff.
