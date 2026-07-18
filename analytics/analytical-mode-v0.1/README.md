# Analytical Mode v0.1

Analytical Mode is CSDL's independent, additive quantitative extension. It keeps Prompt DSL v0.5 unchanged and makes data identity, values, scales, order, units, missing states, transformations, uncertainty, forecast status, and provenance machine-checkable.

## Canonical contract

- `SPEC.md` — human-readable source of truth;
- `manifest.yaml` — version, inventory, dependencies, proof paths;
- `dataset-schema.yaml` — typed data, missing, provenance, transformation grammar;
- `encoding-schema.yaml` — internal marks, field channels, scales, exclusions;
- `contracts/global.yaml` — global quantitative invariants;
- `contracts/families.yaml` — precise rules and hard exclusions for ten families;
- `contracts/compatibility.yaml` — source mapping to D-029 components and D-030 recipes.

Internal analytical marks are not public components. The public vocabulary remains exactly fifteen component names, and the Recipe Library remains exactly 23 recipes.

## Evidence

Ten typed datasets under `datasets/` drive ten source definitions under `proofs/sources/`. The builder emits the canonical `proofs/packages/` specifications. `fixtures/positive/index.yaml` names the passing proofs; seventeen mutations under `fixtures/negative/` must fail for their indexed exact errors.

Accepted Milestone 2 KPI/Table/Chart/Dashboard rasters remain visual calibration. New families have synthetic fixed-data specification proofs and no accepted raster claim.

## Commands

```bash
.venv/bin/python tools/build_analytical_mode.py analytics/analytical-mode-v0.1
.venv/bin/python tools/validate_analytical_mode.py analytics/analytical-mode-v0.1
```

Incomplete contract review is explicit and tested:

```bash
.venv/bin/python tools/build_analytical_mode.py analytics/analytical-mode-v0.1 --incomplete
.venv/bin/python tools/validate_analytical_mode.py analytics/analytical-mode-v0.1 --incomplete
```

Strict mode requires the exact ten datasets, ten proof sources/packages, positive/negative fixtures, derived indexes, evaluation record, migration, rollback, and deterministic rebuild equality.

## Migration and rollback

See `MIGRATION.md` for the additive v0.5-to-v0.1 binding path and `ROLLBACK.md` for normal-revert behavior. Removing Analytical Mode does not alter Prompt DSL v0.5, Component Library v0.1, Recipe Library v0.5, Pilot 01, Visual DNA Sprint 1, or accepted rasters.
