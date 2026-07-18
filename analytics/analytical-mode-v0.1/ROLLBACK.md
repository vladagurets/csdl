# Analytical Mode v0.1 Rollback

Analytical Mode is additive and contains no production dependency, database migration, secret, permission, or deployment change.

To roll back before integration, close the stack and return to `main`. To roll back after integration, revert the Milestone 5 merge commit. The revert removes `analytics/analytical-mode-v0.1/`, its tools/tests, CI steps, and documentation state.

Rollback preserves:

- Prompt DSL v0.5 and all migration proofs;
- Recipe Library v0.5 with 23 recipes;
- Component Library v0.1 with fifteen public components;
- Visual DNA Sprint 1 and Pilot 01 contracts;
- every accepted raster byte.

No data conversion is required. Downstream consumers should stop resolving `kind: analytical-package` documents and continue using the unchanged v0.5 generation packages.
