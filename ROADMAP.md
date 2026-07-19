# CSDL Roadmap

This roadmap orders work by validation dependency, not by calendar dates. A later milestone starts only after the preceding exit criteria are met.

## Milestone 0 — Foundation Lock v0.1

**State:** complete

Delivered:

- design-language purpose and core principles;
- Constructive Signal / Quiet Modular direction;
- Modular Technical typography roles;
- Muted Signal light palette;
- expression levels A/B/C;
- 16:9 canonical landscape grid and spacing;
- visual grammar vocabulary;
- recipes 001 Hero, 005 Comparison, and 013 Loop;
- minimal Prompt DSL;
- quality rubric;
- reference-first workflow.

Exit criterion: approved Foundation Design Specification. **Met.**

## Milestone 1 — Pilot 01: Agentic Discipline

**State:** complete

Goal: prove that one coherent seven-slide 16:9 presentation series can be generated, evaluated, revised, and released without visual drift.

Deliverables:

- seven canonical 1920×1080 light-mode slides;
- prompt files for every card;
- landscape readability previews and contact sheet;
- completed rubric scores and review notes;
- first canonical Visual DNA release.

Exit criteria:

- all required assets validate;
- clarity, presentation readability, and text fidelity are 5/5 for every slide;
- all other scores are at least 4/5;
- every card average is at least 4.4;
- the series reads as one system without repeated logos or decorative overload.

Exit criterion status: **met for Pilot 01 v0.1.0**.

## Milestone 2 — Visual DNA Sprint 1

**State:** complete

Create and validate the first 20 pattern families:

1. Hero
2. Cover
3. Quote
4. Big Number
5. Comparison
6. Collision
7. Before / After
8. Timeline
9. Matrix
10. Hierarchy
11. Architecture
12. Workflow
13. Loop
14. Pipeline
15. Decision Tree
16. Framework
17. KPI
18. Table
19. Chart
20. Dashboard

Delivered:

- one accepted canonical example for each family at its declared expression level, with the series distributed across 13 Level A, 6 Level B, and 1 Level C examples;
- audited Pilot 01 evidence reused for Hero, Comparison, and Loop without unnecessary regeneration;
- D-028 corrective evidence generated under the three-board primary Visual DNA authority and secondary Pilot execution reference;
- machine-readable manifest, schema, family specifications, Prompt DSL packages, fixed analytical prototype data, scores, review records, and index;
- twenty `1280×720` previews plus full, editorial, structural, and analytical `3840×2160` contact sheets;
- strict catalog, data, raster, score, review, preview, contact-sheet, and index validation.

Exit criterion: patterns are recognizably CSDL without depending on a logo.

Exit criterion status: **met for Visual DNA Sprint 1**. The complete evidence and validation contract remains documented in [`docs/plans/2026-07-18-csdl-milestone-2.md`](docs/plans/2026-07-18-csdl-milestone-2.md).

## Milestone 3 — Component Library

**State:** complete

Formalize the first component set:

- Anchor
- Signal
- Field
- Frame
- Cluster
- Vector
- Divider
- Node
- Loop
- Collision
- Bridge
- Axis
- Pulse
- Label
- Legend

For each component, define purpose, semantic meaning, dimensions, allowed relations, compatible recipes, expression-level limits, do/don’t examples, and Prompt DSL syntax.

Delivered: all fifteen component records and Markdown specifications; editorial Big Number, structural Architecture, and fixed-data analytical Chart proofs using declared vocabulary alone; deterministic index and compatibility outputs covering 15 components × 20 families; strict library, proof, and index validators; and complete review evidence without new raster generation.

Exit criterion: a composition can be described and reviewed using component vocabulary alone.

Exit criterion status: **met for Component Library v0.1**.

## Milestone 4 — Recipe Library and Prompt DSL v0.5

**State:** complete

Convert validated patterns into reusable recipes. Each recipe includes:

- problem it solves;
- ingredients;
- assembly order;
- allowed levels;
- landscape presentation constraints;
- semantic color rules;
- canonical examples;
- negative prompts;
- machine-readable YAML schema;
- validation rules.

Delivered:

- 23 evidence-backed recipes: the twenty accepted Visual DNA families plus Breakdown, Checklist, and Formula from accepted Pilot 01 evidence;
- complete canonical Markdown specifications and per-recipe YAML records with stable IDs, ingredients/cardinality, relations, assembly, A/B/C limits, family compatibility, presentation constraints, content, defaults, exclusions, evidence, migration, and rollback;
- layout-free outline schema and Prompt DSL v0.5 schema separating semantic intent, content, instances, relations, generation constraints, and provenance;
- deterministic selection, package, migration, proof, compatibility, index, and selection-index builders;
- mechanical migration coverage for seven Pilot 01 and twenty Visual DNA recipe prompts, with the shared style anchor retained as reference-only calibration evidence;
- editorial Big Number, structural Workflow, and bounded analytical Chart end-to-end proofs plus one Pilot Comparison migration proof;
- six negative fixtures covering layout terms, undeclared components, forbidden relations, unsupported combinations, copy changes, and analytical distortion;
- strict and incomplete-mode validators plus complete regression coverage without raster generation or mutation.

The evidence does not justify approximately fifty distinct recipes. Future additions require a new semantic need demonstrated by real usage.

Exit criterion: a new topic can be converted from outline to generation package without inventing layout rules ad hoc.

Exit criterion status: **met for Recipe Library and Prompt DSL v0.5**.

## Milestone 5 — Analytical Mode

**State:** complete

Add precise rules for bars, lines, scatterplots, waterfall, heatmaps, funnels, maps, networks, tables, uncertainty, forecasts, negative values, sources, and direct labeling.

Constraint: constructive styling must never distort quantitative relationships.

Implementation contract: [`docs/plans/2026-07-18-csdl-milestone-5.md`](docs/plans/2026-07-18-csdl-milestone-5.md). D-031 keeps Prompt DSL v0.5 unchanged and versions Analytical Mode as an independent additive extension.

Delivered:

- canonical Markdown specification, manifest, typed dataset schema, analytical encoding schema, global/family contracts, migration, and rollback documentation;
- ten canonical fixed datasets covering all required families and semantics;
- deterministic transformation, package, index, dataset-index, and compatibility builders;
- strict and tested incomplete-mode validation that reloads datasets independently and recomputes transformations;
- ten end-to-end proof paths for signed bars, observed/forecast/uncertainty line, scatterplot, waterfall, heatmap, funnel, normalized map, directed network, exact table, and single-dataset dashboard;
- seventeen exact-error negative fixtures and focused quantitative mutation tests;
- unchanged Prompt DSL v0.5, fifteen-component D-029 vocabulary, 23-recipe D-030 library, and accepted Milestone 1–4 rasters.

Exit criterion: every family has precise machine-readable rules and a deterministic fixed-data proof; all strict validators and drift checks pass. **Met for Analytical Mode v0.1.**

## Milestone 6 — Night Mode and Accessibility

**State:** complete

Validate the dark palette, contrast, projector behavior, landscape readability, color-vision robustness, and monochrome fallback.

Implementation contract: [`docs/plans/2026-07-18-csdl-milestone-6.md`](docs/plans/2026-07-18-csdl-milestone-6.md). D-032 keeps Prompt DSL v0.5 and all Milestone 1–5 contracts/rasters unchanged while versioning accessibility and output profiles as an independent additive extension.

Delivered:

- canonical specification, manifest, versioned token/proof schemas, and light/night/monochrome/projector profiles;
- exact sRGB contrast, critical-stroke, focus, raised-surface, prohibited-pair, CVD, fallback, Legend, and analytical contracts;
- complete Component/Recipe/Prompt DSL/Analytical Mode compatibility;
- ten deterministic end-to-end proofs and seventeen exact-error negative fixtures;
- deterministic package/index/contrast/compatibility/raster-hash builders and strict/incomplete validators;
- migration, rollback, evidence review, accepted-raster SHA-256 inventory, and CI drift checks.

Exit criterion: all Milestone 1–6 gates pass, accepted raster hashes remain unchanged, and green merge-commit integration is recorded. **Met for Night Mode and Accessibility v0.1.**

## Milestone 7 — Cookbook and Design Book v1.0

**State:** complete

Build a compact bilingual 25–40 page guide from canonical Markdown sources. D-033 selects an additive `cookbook/design-book-v1.0/` boundary and ISO A4 landscape pages instead of reusing the 16:9 slide canvas.

Delivered:

- 32 canonical one-page Markdown sources with Ukrainian editorial explanation and protected English identifiers;
- complete coverage of philosophy, Quiet Modular/A/B/C, tokens, typography boundaries, grammar, all fifteen components, all 23 recipes, Prompt DSL v0.5, Analytical Mode v0.1, accessibility, provenance, practice, and preflight;
- machine-readable manifest, terminology registry, page/source map, and accepted-raster inventory dependency;
- deterministic assembled Markdown/index, A4 PDF with Unicode text layer, full-size color/grayscale renders, contact sheet, and build report;
- twelve exact-error negative publication fixtures and focused test/validator/CI drift coverage;
- unchanged Milestone 1–6 contracts and all sixty accepted raster hashes.

Exit criterion: all Milestone 1–7 gates pass, accepted raster hashes remain unchanged, and green merge-commit integration is recorded. **Met for Cookbook and Design Book v1.0 through PR #69 and merge commit `4c20829f4923c164b48985d06a49247ff372ed4f`.**

## Milestone 8 — Public release and licensing decision

**State:** noncommercial source-available licensing selected; tagged release policy remains undecided

The selected working repository is `vladagurets/csdl`. D-034 assigns PolyForm Noncommercial 1.0.0 to software and machine-readable materials, CC BY-NC-SA 4.0 to original documentation and visual materials, separate written terms to commercial use, and a distinct trademark boundary. Before calling CSDL a tagged public release, resolve the exact font licensing policy, long-term asset-distribution strategy, stable versioning model, release notes, tag, and GitHub Release.
