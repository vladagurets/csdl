# CSDL Analytical Mode v0.1

**Status:** active implementation  
**Canonical source:** Markdown  
**Machine contract:** `manifest.yaml`, `dataset-schema.yaml`, `encoding-schema.yaml`, and `contracts/`  
**Version boundary:** independent additive extension; Prompt DSL v0.5 unchanged

## 1. Purpose

Analytical Mode makes quantitative tables, charts, maps, networks, and multi-view compositions reproducible without allowing Constructive Signal styling to change what the data says. Domain, order, values, units, labels, missing states, transformations, and provenance take priority over asymmetry, signal rhythm, or decorative geometry.

## 2. Contract layers

1. A typed dataset owns identity, version, fields, records, missing states, declared transformations, and provenance.
2. Analytical intent states the claim and the lookup/comparison task.
3. A compatible Recipe Library v0.5 recipe carries the proven presentation need.
4. An Analytical Mode encoding binds fields to internal marks, domains, scales, order, labels, uncertainty, forecast, and family options.
5. D-029 component instances and relations express public CSDL semantics.
6. A deterministic specification is derived from the canonical dataset and encoding.

Internal marks are not public components. `bar`, `line`, `point`, `cell`, `region`, `network-node`, `network-edge`, `waterfall-step`, `funnel-stage`, and `interval-band` exist only inside the v0.1 encoding contract.

## 3. Typed data

Every dataset declares:

- stable identity and semantic version;
- unit of analysis;
- dimension, measure, and identifier fields;
- categorical, ordinal, temporal, quantitative, geographic, or identifier types;
- units, display formats, domain, category/order metadata, aggregation, denominator, and normalization where applicable;
- source, source type, source date, retrieval period, and method;
- record identity and exact values;
- missing, null, suppressed, not-applicable, and unavailable semantics;
- explicit transformations with formula, inputs, output, parameters, and reversible/auditable status.

Zero is a value, not missing data. A null cell must have one missing-status declaration. Suppressed and unavailable values may never be converted to zero. Every transformation must be deterministic and reproducible from source records. A transformation that changes meaning without declaring the new measure, denominator, unit, or interpretation is invalid.

## 4. Global encoding invariants

- Dataset identity, bindings, domain, order, exact values, units, labels, and source are immutable between the canonical dataset and derived package.
- Bar-like length encodings include zero. Line and scatter domains include zero only when zero is semantically relevant; any truncation is visible and declared.
- Log scales are forbidden by default. A valid log scale is explicit and uses positive-only data.
- Dual axes are forbidden by default. An exception requires an explicit rationale, independent units, and a non-misleading review; v0.1 proofs contain none.
- Position, length, area, and color may not encode conflicting values.
- Color is never the sole carrier of meaning. Text, form, pattern, or direct labels provide a redundant carrier.
- Direct labels take precedence. Legend remains the constrained D-029 exception and requires a recorded direct-label failure.
- At most one series or state carries the dominant Signal; other data remains neutral unless a semantic category contract requires otherwise.
- Decorative geometry is disabled. Field is absent or occupies at most 5% when it serves context.
- 3D, perspective, gradients, shadows, glossy surfaces, chartjunk, UI chrome, decorative coordinate systems, and random dot fields are excluded.
- Every analytical claim traces to one dataset field or declared transformation.

## 5. Family rules

### Bars

Bars preserve declared categorical order and begin at zero. Grouped bars compare peers; stacked bars represent additive parts; normalized stacks sum to the declared total. Positive and negative values extend from the same zero reference. Units stay on the quantitative Axis or direct labels. 3D, perspective, and area distortion are prohibited.

### Lines

Lines require a temporal or explicitly ordered x domain. Missing intervals render as gaps unless a declared interpolation method is used. Smoothing never replaces source points and requires a reproducible method. Observed and forecast segments are separated at a declared boundary. Forecast horizon, status, uncertainty type, interval level, lower, estimate, and upper remain explicit.

### Scatterplots

Scatterplots bind independent quantitative x/y fields and domains. The contract states whether zero matters to each domain. Overplotting policy, categories, selected labels, and any size encoding are explicit. Size uses declared area semantics. Trend lines require a named deterministic method. Spatial placement outside these bindings is decoration and invalid.

### Waterfall

Waterfalls distinguish start, signed increment, subtotal, and total semantics. Cumulative values are recomputed in declared order against a zero reference. The final total must reconcile to the start plus all included increments. Sorting for visual effect is forbidden.

### Heatmaps

Heatmaps declare matrix identity, fixed row/column order, continuous or discrete scale, domain, and missing-cell semantics. Every cell has a text/form fallback so color is not the only carrier. Missing cells are not zero. The scale is exposed through direct endpoints or a constrained accessible key.

### Funnels

Funnels preserve stage order and expose absolute values with conversion rates. Each rate declares whether its denominator is the previous stage or the initial cohort. Non-monotonic data is shown as such or rejected by an explicitly declared policy; it is never silently sorted. Width is proportional to value, not decorative area.

### Maps

Maps bind declared geographic identifiers and projection. Absolute counts and normalized rates are different measures. Comparable-rate claims require the rate field, denominator, unit, and geographic provenance. Missing regions and supplied uncertainty are visible. Raw counts across unequal populations cannot be labeled as comparable rates.

### Networks

Networks declare unique nodes and edges, direction, weight, and missing-edge semantics. Layout is non-semantic by default. Distance, angle, or clustering cannot be interpreted quantitatively without a declared encoding contract. Links are Bridge semantics publicly and internal `network-edge` marks analytically.

### Tables

Tables support exact lookup. Row and column order are data semantics, not layout vocabulary. Text aligns by role and numbers use tabular or decimal alignment. Units remain attached. Totals and subtotals are declared derived records. Missing states are explicit. Semantic emphasis is restrained; decorative tiles and zebra styling are excluded.

### Dashboards

A dashboard is a multi-view analytical composition, not UI chrome. Every view names one shared dataset identity/version, its own intent, bindings, domain, and units. Repeated measures reconcile exactly. One view owns the primary Signal; the rest remain subordinate. Sources and missing states remain visible.

## 6. Uncertainty and forecasts

An interval declares whether it is a confidence, credible, prediction, or descriptive range. A confidence/credible level is required when applicable. Lower ≤ estimate ≤ upper for every record. The point estimate cannot hide the interval. Forecast records declare their horizon and status, and never use the same undifferentiated treatment as observed facts.

## 7. Sources and provenance

Every dataset includes a human-readable source, source type, source date, retrieval period, and method. Synthetic fixtures say so explicitly and make no external empirical claim. Derived specifications carry source identity and dataset version forward. A source label cannot be dropped for presentation cleanliness.

## 8. Compatibility

Analytical Mode uses Recipe Library v0.5 recipes `018 Table`, `019 Chart`, and `020 Dashboard` for the ten v0.1 proof needs. It does not add recipes. Public presentation semantics use only the fifteen D-029 components. `contracts/compatibility.yaml` is the canonical mapping; deterministic `compatibility.yaml` is derived from it.

## 9. Evidence status

Accepted KPI, Table, Chart, and Dashboard rasters calibrate restrained Analytical Mode presentation. New v0.1 families use synthetic fixed-data specification proofs only. Those proofs establish deterministic correctness, not raster acceptance. No raster generation or mutation is part of Milestone 5.
