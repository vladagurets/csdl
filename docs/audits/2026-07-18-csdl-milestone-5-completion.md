# Milestone 5 Analytical Mode v0.1 — Completion Audit

**Date:** 2026-07-18  
**Integration branch:** `codex/m5-integration`  
**Final state target:** merge commit to `main`, then clean-main post-merge validation

## Outcome

Analytical Mode v0.1 is implemented as the independent additive extension fixed by D-031. Prompt DSL v0.5 remains unchanged. D-029 remains exactly fifteen public components and D-030 remains exactly 23 recipes. Internal analytical marks never become public components.

## Supported families and semantics

- bar, including signed values and zero baseline;
- line, including missing intervals, observed/forecast segmentation, horizon, and uncertainty interval semantics;
- scatterplot with independent quantitative domains and declared size/category encodings;
- waterfall with signed cumulative reconciliation;
- heatmap with matrix identity, fixed order, domain, accessible non-color fallback, and missing cells;
- funnel with absolute values, explicit denominators, conversion rates, and non-monotonic policy;
- map with geographic identity/projection, normalized rate, denominator, provenance, and missing region semantics;
- network with node/edge identity, direction, weight, missing-edge meaning, and non-semantic layout;
- exact-lookup table with units, ordering, alignment, totals policy, source, and missing status;
- multi-view dashboard with one dataset identity/version and exact repeated-measure reconciliation.

Global contracts cover negative/zero values, domains, ordering, units, sources, direct labels, conditional Legend use, log/dual-axis defaults, transformations, normalization, missing/null/suppressed/not-applicable/unavailable states, color redundancy, decorative Field ≤5%, and hard chartjunk exclusions.

## Version and migration boundary

- Analytical package: `language: CSDL`, `version: "0.1"`, `kind: analytical-package`.
- Prompt DSL compatibility: `0.5`; no v0.5 schema or package changed.
- Migration: additive typed-dataset + encoding binding to recipe `018`, `019`, or `020`.
- Rollback: revert the Milestone 5 merge; all Milestone 1–4 sources and rasters remain valid.

## Proof coverage

Ten canonical fixed datasets and ten deterministic packages cover every required path:

```text
typed dataset
→ analytical intent
→ compatible v0.5 recipe
→ Analytical Mode v0.1 encoding
→ D-029 component instances/relations
→ deterministic independently validated specification
```

Critical derived evidence:

- waterfall cumulative: `[100, 125, 115, 130, 130]`;
- funnel previous-stage conversion: `[100.0, 65.0, 60.0, 50.0]`;
- normalized map rates: `[4.0, 6.0, null]` per 100,000 runs;
- dashboard views: one `dashboard-agent-reliability-v1@1.0.0` contract.

Seventeen negative fixtures reject truncated baseline, undeclared log, unapproved dual axis, reordered time, mutated value, missing unit/source, wrong denominator, forecast-as-observed, inverted uncertainty, invalid normalization, raw-count rate claim, semantic network distance, color-only meaning, unsupported component, layout vocabulary, and nondeterministic output.

## Local validation evidence

The complete pre-integration matrix exited zero:

- tests: 125 collected / 125 passed;
- Pilot 01: manifest, style anchor, assets, and scores valid;
- Milestone 2: catalog, data, assets, scores, review, rebuilt previews/contact sheets, and index valid;
- Milestone 3: component library, proofs, rebuilt index/compatibility, and index valid;
- Milestone 4: recipe library, rebuilt proofs, Prompt DSL v0.5, rebuilt indexes, and index valid;
- Milestone 5: rebuilt ten packages plus three indexes; strict Analytical Mode validation valid;
- `git diff --check`: pass;
- second builder pass: no tracked drift;
- PNG comparison against `origin/main`: no changed paths.

## Stack traceability

| Packet | Branch | Pull request |
|---|---|---|
| Evidence/architecture | `codex/m5-01-architecture` | #56 |
| Contracts/datasets | `codex/m5-02-contracts` | #57 |
| Tooling/invariants | `codex/m5-03-tooling` | #58 |
| Proofs/fixtures | `codex/m5-04-proofs` | #59 |
| Completion/CI | `codex/m5-05-docs` | #60 |
| Final integration | `codex/m5-integration` | final PR to `main` |

Intermediate PRs are traceability views only and must not be merged independently. After the final integration PR is green and merged with a merge commit, they are closed as integrated without deleting branches.

## Documentation and raster status

README, STATUS, ROADMAP, CHANGELOG, DECISIONS, AGENTS, the canonical spec, library README, evidence review, migration, and rollback documents agree on Milestone 5 completion and Milestone 6 deferral. No accepted raster was generated, replaced, normalized, or otherwise modified.

## Remaining risk

The new families have deterministic specification evidence, not accepted raster evidence. This does not defer any machine contract, but a future visual-generation objective must use a separate user-approved three-candidate/review packet before claiming canonical visual examples. Milestone 6 Night Mode has not started.
