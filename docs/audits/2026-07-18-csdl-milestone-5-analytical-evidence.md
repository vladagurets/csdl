# Milestone 5 Analytical Mode — Evidence Audit

**Date:** 2026-07-18  
**Scope:** Analytical Mode v0.1 only  
**Repository baseline:** clean `main` at `fc3575a8473166dc784c17267d76e13051481dd3`, equal to `origin/main`

## Audit conclusion

Accepted evidence establishes four bounded analytical uses: one exact KPI snapshot, one small exact-lookup table, one ordered single-series percent chart, and one open single-dataset dashboard. It proves the priority of data fidelity over constructive styling, direct labels, visible units and source, honest quantitative domains, preserved order, one dominant signal, restrained color, and the absence of decorative chart chrome.

That evidence does not establish family-specific contracts for bars, scatterplots, waterfall, heatmaps, funnels, maps, networks, uncertainty, or forecasts. Those requirements therefore need deterministic synthetic fixed-data proofs. The proofs may define machine-checkable data and encoding behavior, but they do not claim new accepted raster evidence or authorize raster generation.

## Audited sources

### Foundation

- `specs/2026-07-17-csdl-v0.1-design.md`, section 7, already requires Analytical Mode to subordinate decoration, keep background Field usage at zero or at most 5%, prefer direct labels, highlight at most one series, and never use color as the sole carrier of meaning.
- Sections 4, 9, and 10 require meaning before decoration, semantic color, open component grammar, and quantitative Axis integrity.
- `ROADMAP.md` names all Milestone 5 families and the non-distortion constraint, but deliberately contains no detailed contracts.

### Milestone 2 bounded analytical evidence

- Fixed dataset: `patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml`.
- Families/contracts: `manifest.yaml`, specs and prompts `17-kpi` through `20-dashboard`.
- Accepted rasters: `canonical/light/16x9/17-kpi.png` through `20-dashboard.png`.
- Review evidence: `evaluation/review.md`, including cell-by-cell table checks, a measured chart geometry audit, source/unit checks, candidate rejections, and the analytical contact sheet.

Confirmed evidence:

| Family | Confirmed contract | Bound |
|---|---|---|
| KPI | one exact primary value with label, unit, period, supporting context, and source | W4 fixed demo snapshot only |
| Table | exact row/column lookup, fixed order, units, sparse rules, no decorative cells | 4×4 fixed demo values only |
| Chart | W1–W4 order, `[0, 100]` percent domain, exact values/labels, straight segments, no interpolation, source | one positive ordered line series only |
| Dashboard | one dataset, one primary Pulse, supporting metrics, one consistent trend, direct labels, no widget chrome | one compact operational snapshot only |

The accepted analytical contact sheet was visually reviewed. It confirms open warm-paper compositions, neutral reference structures, dusty-blue data emphasis, direct labels, and restrained density. It cannot prove generalized quantitative behavior beyond the four fixed examples.

### Component Library v0.1

Audited components: Signal, Field, Frame, Vector, Node, Axis, Pulse, Label, and Legend, plus the analytical proof and compatibility matrix.

- Axis already owns sequence, coordinate, lookup, support, and quantitative reference modes; quantitative mode requires an honest domain and exact ordered values.
- Node can represent a data point but remains a public semantic unit, not a chart-mark taxonomy.
- Pulse owns one exact measure with label/unit/period/source context.
- Label requires a single target and preserves quantitative value/unit/period/order.
- Signal is attached emphasis, never free color or decoration.
- Frame supports functional lookup boundaries; Field provides context and is not a generic panel.
- Vector represents semantic action/transformation, not a line-chart segment.
- Legend is conditional, subordinate, limited to two–four text-and-form mappings after direct-label failure is recorded. There is no accepted positive Legend raster.
- The accepted component analytical proof validates `[72, 78, 84, 90]`, `[0, 100]`, W1–W4 order, direct labels, source, and one final Signal.

Conclusion: D-029's fifteen public components are sufficient. Bar, line, point, cell, region, link, and interval are internal analytical marks, not new public components.

### Recipe Library and Prompt DSL v0.5

Audited recipes `017 KPI`, `018 Table`, `019 Chart`, and `020 Dashboard`; the Prompt DSL v0.5 schema; bounded analytical proof; migration map; validators/builders; and negative fixtures.

- The four recipes encode stable user needs rather than individual chart marks.
- Prompt DSL v0.5 permits only its eleven top-level concerns and intentionally rejects undeclared composition vocabulary.
- Its quantitative validator is deliberately coupled to the one Milestone 2 dataset and one Chart proof.
- The bounded analytical proof preserves dataset, series, order, domain, values, units, labels, source, Axis attributes, and Node attributes.
- The distortion fixture proves a changed value is rejected.
- Existing migration is mechanical and preserves all v0.1 sources; no accepted Prompt DSL or raster is rewritten.

Conclusion: extending Prompt DSL v0.5 in place would either break its closed schema or overload recipe content bindings with a full data grammar. Analytical Mode should be an independent versioned extension contract that references a compatible v0.5 recipe and public components. Prompt DSL v0.5 remains unchanged.

## Evidence classification

### Accepted evidence-backed rules

- exact dataset identity, values, order, units, labels, domain, and source;
- direct labels before Legend;
- honest open Axes and no hidden reordering;
- no interpolation or smoothing unless explicitly declared;
- one dominant Signal with other data neutralized;
- color is redundant with label/form;
- sparse analytical surfaces with decorative Field at zero or at most 5%;
- no gradients, shadows, 3D, glossy surfaces, widget chrome, decorative grids, or decorative cell tiles;
- deterministic machine-readable sources and rebuild checks;
- D-029 public components and D-030 recipes remain closed.

### New synthetic fixed-data proof requirements

- positive/negative bars with a zero baseline;
- observed/forecast line segmentation and uncertainty bounds;
- independent quantitative scatter domains;
- signed waterfall reconciliation;
- heatmap matrix identity, fixed order, scale, and non-color missing fallback;
- funnel denominators/conversions and non-monotonic policy;
- normalized geographic rate with identifier/projection/provenance;
- declared node/edge network with non-semantic layout;
- generalized exact-lookup table missing/totals behavior;
- a multi-view dashboard in which every view references one dataset contract.

## Raster decision

No contract gap requires new raster evidence to implement machine-readable Analytical Mode v0.1. Existing KPI/Table/Chart/Dashboard rasters remain the accepted visual calibration. New families receive deterministic specification proofs, not generated images. Any later request to claim visual acceptance for a new family requires a separate candidate/review plan and explicit user approval before generation.

## Risks and controls

- **Risk:** internal marks become hidden public components. **Control:** schemas label them `internal_mark`; compatibility always resolves presentation semantics through D-029 components.
- **Risk:** Prompt DSL v0.5 is silently changed. **Control:** no v0.5 file is modified; Analytical Mode uses its own version/kind and migration documentation.
- **Risk:** a generated package becomes the only truth for values. **Control:** validators load canonical datasets independently and recompute bindings, transforms, domains, and derived values.
- **Risk:** synthetic proofs are mistaken for raster evidence. **Control:** every proof declares `evidence: synthetic_fixed_data` and review notes state that no visual acceptance is claimed.
- **Risk:** deterministic output hides transformation meaning. **Control:** transformations require operation, inputs, output, parameters, formula, audit fields, and reversibility/auditability status.

## Recommendation

Proceed with an independent `analytics/analytical-mode-v0.1/` extension under D-031. Keep Prompt DSL v0.5, D-029, D-030, and all accepted rasters byte-identical. Implement the ten required synthetic fixed-data proofs and reject quantitative mutations mechanically.
