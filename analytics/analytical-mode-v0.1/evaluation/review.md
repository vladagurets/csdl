# Analytical Mode v0.1 — Proof Review

**Evidence class:** deterministic synthetic fixed data  
**Visual calibration:** accepted Milestone 2 KPI, Table, Chart, and Dashboard rasters  
**Raster generation or mutation:** none

## Review method

Each proof was reviewed through two independent paths:

1. the builder loaded the canonical typed dataset and derived the package/specification;
2. the validator reloaded the canonical dataset independently, recomputed transformations, and compared identity, fields, records, order, missing states, units, source, domains, components, relations, and derived values.

Synthetic proofs establish data and encoding correctness only. They do not claim raster acceptance for a new family.

## Proof decisions

| Proof | Fixed evidence | Mechanical acceptance |
|---|---|---|
| Bar | `[12, -5, 8, -3]` in declared category order | signed values share a zero baseline; domain crosses zero; units/direct labels retained |
| Line | four observed and two forecast quarters | boundary at `2027-Q1`; two-quarter horizon; 80% prediction intervals satisfy lower ≤ estimate ≤ upper |
| Scatterplot | four configurations | independent x/y domains, declared proportional-area run count, category labels, no invented trend |
| Waterfall | 100, +25, −10, +15, 130 | recomputed cumulative `[100, 125, 115, 130, 130]` and exact final reconciliation |
| Heatmap | 2×3 fixed matrix | row/column order fixed; unavailable Beta/W2 remains `N/A`, not zero; numeric/text fallback accompanies color |
| Funnel | 1000 → 650 → 390 → 195 | previous-stage conversions `[100, 65, 60, 50]`; absolute counts and denominator semantics retained |
| Map | PT-11, PT-17, PT-15 | ISO identifiers, declared projection, rates `[4.0, 6.0, null]` per 100,000 runs, unavailable region explicit |
| Network | three nodes, three directed weighted edges | unique identities/endpoints; direction/weight explicit; spatial distance declared non-semantic |
| Table | two products × two quarters × two measures | exact lookup, row/column/measure order, attached units, one suppressed value explicit |
| Dashboard | accepted W1–W4 reliability values | snapshot, trend, and lookup views reference `dashboard-agent-reliability-v1@1.0.0` and reconcile exactly |

## Negative review

Seventeen indexed fixtures cover all requested failures: truncated bar baseline; undeclared log scale; dual axis without exception; reordered time; mutated value; missing unit; missing source; misleading denominator; forecast as observed; inverted uncertainty; invalid normalization; raw map count claimed as rate; semantic network distance; color-only meaning; unsupported component combination; undeclared layout; and nondeterministic output.

Each fixture is a deterministic mutation descriptor over one accepted proof package. The strict validator requires the exact indexed error for every fixture.

## Component and recipe compatibility

- No public component was added. All proofs use subsets of D-029.
- No recipe was added. Proofs reference only `018`, `019`, or `020` with their exact v0.5 IDs/slugs/versions.
- Internal marks never appear as component names.
- Legend remains conditional and is not instantiated; heatmap accessibility uses direct numeric/missing labels and explicit scale endpoints.

## Remaining visual risk

Bars, scatterplots, waterfall, heatmaps, funnels, maps, networks, forecast segmentation, and uncertainty bands have no accepted raster evidence. Their deterministic contracts are complete, but visual candidate generation would require a separate user-approved raster packet. Milestone 5 does not generate placeholders or claim that schema proofs replace visual review.
