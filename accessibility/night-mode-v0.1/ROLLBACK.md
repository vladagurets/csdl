# Night Mode and Accessibility v0.1 Rollback

Night Mode and Accessibility is additive and contains no production dependency, database migration, secret, permission, deployment, or raster mutation.

Before integration, close the stack and return to `main`. After integration, revert the Milestone 6 merge commit. The revert removes `accessibility/night-mode-v0.1/`, its tools/tests, CI steps, and documentation state.

Rollback preserves:

- Prompt DSL v0.5;
- Component Library v0.1 with fifteen public components;
- Recipe Library v0.5 with 23 recipes;
- Analytical Mode v0.1 data, encodings, and proofs;
- Visual DNA Sprint 1 and Pilot 01 contracts;
- every accepted raster byte.

No data conversion is required. Downstream consumers stop resolving `kind: accessibility-package` and continue using the unchanged source packages.
