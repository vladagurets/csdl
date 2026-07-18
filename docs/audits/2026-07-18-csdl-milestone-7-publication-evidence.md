# Milestone 7 Cookbook and Design Book v1.0 — Evidence Audit

**Date:** 2026-07-18  
**Baseline:** clean `main` at `d4d60aa468481e3998212b87cb5240a88f6a6b6d`, equal to freshly fetched `origin/main`  
**Scope:** publication only; no Milestone 8, license, tag, GitHub Release, new raster evidence, or public-release claim

## Audit question

What is the smallest repository-supported publication architecture that can turn the completed Milestone 1–6 language into a coherent bilingual 25–40 page guide without mutating its public vocabulary, quantitative meaning, accessibility boundary, or accepted visual evidence?

## Sources reviewed

The mandatory documents were read in the repository-defined order: `STATUS.md`, `DECISIONS.md`, the Foundation specification, Pilot manifest, Pilot plan, shared-anchor Prompt DSL, anchor provenance, and raster handoff. The audit then checked the active Foundation/Pilot/Visual DNA documentation; all twenty Visual DNA family records and indexes; the fifteen Component Library specifications, manifest, compatibility/index outputs, proofs, and review; the 23 Recipe Library specifications and records, Prompt DSL v0.5 schema, indexes, proofs, migrations, fixtures, and review; Analytical Mode v0.1 specification, schemas, contracts, ten datasets/proofs, indexes, fixtures, and review; Accessibility v0.1 specification, profile/token/contrast/fallback/compatibility contracts, ten proofs, fixtures, review, and sixty-file hash inventory; repository docs, tests, tools, and CI.

The audit independently confirmed:

- exactly fifteen public components, in D-029 order;
- exactly 23 recipes, in D-030 order;
- Prompt DSL compatibility remains exactly `0.5` in both additive extensions;
- ten Analytical Mode families and source-backed proof paths;
- four Accessibility profiles: `light`, `night`, `monochrome`, and `projector`;
- all sixty accepted PNG files match the SHA-256 inventory;
- the repository has only Pillow and PyYAML as production dependencies.

## Canonical rules that can be stated directly

- CSDL is a design language, not a fixed template collection.
- Constructive Signal is the direction; Quiet Modular is the default expression.
- Level A is quiet/default, Level B constructive, and Level C a rare signal peak; the standard seven-screen rhythm is `A → A → B → A → B → A → C`.
- One screen carries one main idea, one visual mechanism, and one dominant Signal; default negative space is 50–75% depending on expression.
- Geometry must communicate scope, direction, relation, order, state, or emphasis.
- The presentation master remains `1920×1080`, 16:9 landscape. It is evidence embedded in the book, not the book page format.
- The public component vocabulary is exactly Anchor, Signal, Field, Frame, Cluster, Vector, Divider, Node, Loop, Collision, Bridge, Axis, Pulse, Label, and Legend.
- The public recipe vocabulary is exactly the 23 D-030 records. Legend is conditional and direct labels take precedence.
- Prompt DSL v0.5 is closed and separates semantic intent, exact content, component instances, relations, generation constraints, and provenance.
- Analytical Mode preserves dataset identity, bindings, domain, order, values, units, labels, source, missing states, transformations, uncertainty, and forecast semantics before style.
- Accessibility maps semantic roles rather than pixels; informative text uses at least 4.5:1, meaningful non-text at least 3:1, and projector output uses 7:1 and 4.5:1 respectively.
- Markdown is canonical; images calibrate it and raster wording is never canonical copy.

## Editorial synthesis supported by multiple sources

- Quiet Modular is best taught as a discipline of subtraction: semantic ownership first, then the smallest geometry that exposes it.
- Components answer “what role does this element own?” while recipes answer “what explanatory problem is this composition solving?”
- A/B/C is a rhythm system, not a quality ladder: Level C is not “better,” only rarer and more compressed.
- Accessibility and Analytical Mode share one governing idea: visual character may strengthen meaning but may not replace or distort it.
- Human designers and generative agents can use the same workflow when the brief is converted into stable intent, exact content, component relations, constraints, and provenance before rendering.

## Unresolved or deferred decisions

- Exact licensed display, reading, and monospace font families remain unresolved. Inter/Arial/other local implementations are evidence or build fallbacks, not a global font lock.
- Night/projector/monochrome/CVD mappings have deterministic specification evidence but no accepted raster calibration.
- Legend has a constrained contract and no accepted positive family raster.
- Prompt DSL v1, a recipe expansion beyond 23, icon construction, alternate slide canvases, long-term high-resolution storage, license, release strategy, and asset-distribution policy remain deferred.
- The publication PDF is a deterministic derived artifact; Markdown remains the accessible canonical source and the font used for local rendering is recorded in build provenance.

## Claims that must not be made

- Do not call this a public release or imply a selected license.
- Do not claim final font licensing or exact global font families.
- Do not claim accepted visual evidence for night, projector, monochrome, CVD, new analytical families, or a positive Legend use.
- Do not call deterministic specification proofs accepted generated rasters.
- Do not infer authoritative copy from AI-rendered reference text.
- Do not invent components, recipes, Prompt DSL fields, analytical values, visual examples, or accessibility semantics.
- Do not present the 16:9 presentation canvas as the book page merely because it is canonical for slides.

## Publication format evaluation

| Option | Readability and density | Evidence placement | Deterministic build | Decision |
|---|---|---|---|---|
| 16:9 landscape | familiar on screen but too shallow for sustained bilingual explanation | exact slide fit | feasible | rejected as an unexamined reuse of the slide canvas |
| A4 portrait | strong for prose but weak for side-by-side grammar, recipes, and uncropped 16:9 evidence | small evidence reproductions | feasible | rejected for this visual/technical guide |
| A4 landscape | two-column Ukrainian explanation plus English terms; useful on screen and in print | uncropped 16:9 evidence with captions | feasible with current Python stack | selected |

## D-033 recommendation

Use `cookbook/design-book-v1.0/` as an additive publication boundary. Store one canonical Markdown source per page and enumerate exactly 25–40 pages in `manifest.yaml`. Keep technical terms in a validated English registry, map every page and claim to repository evidence in `provenance.yaml`, assemble a derived Markdown book, and build a page-accurate A4 landscape PDF with deterministic review renders and a contact sheet. Generated outputs are derived and never hand-edited. Existing rasters may be embedded unchanged; their source paths and hashes stay pinned.

No new generated raster evidence is required. Publication page renders and contact sheets are deterministic QA outputs, not new CSDL visual authority.
