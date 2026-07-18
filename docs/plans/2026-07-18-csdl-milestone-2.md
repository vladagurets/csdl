# CSDL Milestone 2 — Visual DNA Sprint 1 Implementation Plan

**Goal:** formalize and validate the first 20 CSDL pattern families as a machine-readable, reviewable 16:9 catalog. Hero, Comparison, and Loop reuse passing Pilot 01 evidence. The other 17 families receive one new canonical example selected from three independent GPT Image 2 candidates.

**Primary signal:** the finished catalog is recognizably CSDL without a logo, every family has valid canonical evidence, and all milestone validators pass without placeholders.

## Acceptance contract

Milestone 2 is complete only when:

1. the catalog manifest contains exactly the 20 roadmap families in canonical order;
2. every family has a complete Markdown specification and Prompt DSL contract;
3. Hero, Comparison, and Loop cite audited Pilot 01 raster, prompt, review, score, and hash evidence;
4. each of the other 17 families has three reviewed candidates and one promoted `1920×1080` PNG;
5. accepted examples score `5` for clarity, presentation readability, and text/data fidelity, at least `4` elsewhere, and at least `4.4` on average;
6. analytical prototypes preserve the fixed dataset exactly and do not claim to define full Analytical Mode;
7. machine-readable indexes, landscape previews, contact sheets, tests, and all validators pass;
8. `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, and relevant catalog documentation match the delivered state;
9. no placeholder score, unresolved product decision, extra text, decorative geometry, UI chrome, or untracked canonical evidence remains.

## Canonical tree

```text
patterns/visual-dna-sprint-01/
├── README.md
├── manifest.yaml
├── schema.yaml
├── index.yaml
├── specs/
│   └── 01-hero.md … 20-dashboard.md
├── prompts/
│   └── 02-cover.yaml … 20-dashboard.yaml
├── data/
│   └── agent-reliability-demo.yaml
├── drafts/light/16x9/<family>/
├── canonical/light/16x9/
│   └── 02-cover.png … 20-dashboard.png
├── previews/landscape/
├── contact-sheets/
│   ├── visual-dna-01-editorial.png
│   ├── visual-dna-01-structural.png
│   ├── visual-dna-01-analytical.png
│   └── visual-dna-01-all.png
└── evaluation/
    ├── rubric.yaml
    ├── scores.csv
    └── review.md
```

Pilot-backed families do not duplicate rasters. Their `canonical_example` paths point to the approved Pilot 01 assets, while `index.yaml` resolves all 20 families into one catalog.

## Manifest and schema contract

`manifest.yaml` is the content and evidence source of truth. Each family entry must define:

- stable two-digit ID, slug, display name, and wave;
- problem and allowed scenarios;
- semantic components and deterministic assembly order;
- allowed expression levels and one canonical level;
- typography, spacing, signal, density, and hard-exclusion constraints;
- exact canonical copy or an explicit dataset reference;
- Prompt DSL and Markdown specification paths;
- evidence mode: `pilot_reference` or `generated`;
- canonical raster path and candidate-generation requirement;
- acceptance requirements.

`schema.yaml` defines required keys, allowed enums, the canonical family order, evidence rules, and path conventions. `tools/validate_pattern_catalog.py` enforces this schema without adding a production dependency.

## Pattern specification format

Every `specs/<id>-<slug>.md` uses the same required sections:

1. Problem;
2. Allowed scenarios;
3. Semantic components;
4. Assembly order;
5. Expression levels;
6. Typography and spacing;
7. Signal constraints;
8. Canonical content;
9. Hard exclusions;
10. Prompt DSL contract;
11. Acceptance criteria;
12. Canonical evidence.

The specification explains semantics; the manifest holds values that validators need.

## Expression-level selection

Level is selected by semantic pressure, not visual novelty:

- **A / Quiet:** one proposition, one comparison, one route, or analytical reading where structure must recede;
- **B / Constructive:** the relationship itself is the teaching object and needs two–four active nodes, controlled motion, intersection, or containment;
- **C / Signal:** title, culmination, or a single unavoidable collision with very short copy.

The canonical set targets the locked distribution exactly: 13 Level A examples, 6 Level B examples, and 1 Level C example. A family lists only levels that preserve its core semantic mechanism. Analytical prototypes are Level A in this milestone.

## Review and evaluation contract

For every generated example:

1. invoke built-in `$imagegen` three independent times with the same Prompt DSL and approved Pilot 01 style anchor;
2. retain candidates under ignored `drafts/` and record filenames plus SHA-256 hashes;
3. compare all three at source resolution and normalized `1920×1080`;
4. build and inspect a `1280×720` preview;
5. verify exact copy or every dataset value;
6. reject extra text, logos, footers, UI chrome, decorative geometry, incorrect level, weak hierarchy, or distorted quantities;
7. select one passing candidate and record the selection rationale, rejection reasons, raster mode/dimensions, normalization, hashes, removable-element check, and remaining risk;
8. score the seven Pilot 01 rubric dimensions, interpreting `text_fidelity` as `content_fidelity` for analytical data.

Pilot references must pass the same catalog checks from their persisted Pilot 01 review and score evidence; they are not regenerated.

## Validation tooling

- `validate_pattern_catalog.py`: manifest/schema consistency, family order, required spec/prompt paths, canonical levels, evidence rules, and no placeholders;
- `validate_pattern_assets.py`: required generated PNGs, exact `1920×1080`, RGB/RGBA, and Pilot reference resolution;
- `validate_pattern_scores.py`: exactly 20 accepted evidence rows and rubric thresholds with no zeros/blanks;
- `validate_pattern_data.py`: fixed analytical dataset schema and exact values referenced by KPI, Table, Chart, and Dashboard;
- catalog builders: `1280×720` previews, wave contact sheets, all-family contact sheet, and generated `index.yaml`;
- tests: positive fixtures plus one focused failure case for each validation rule.

Cheap gates run before visual gates: tests → catalog/schema → data → assets → scores → generated indexes/contact sheets.

## Delivery sequence and Git topology

The milestone uses a stacked series so every pull request has a narrow diff while upstream packets remain unmerged:

1. `codex/m2-infrastructure` → `main`: plan, tree, manifest/schema, all family specifications and Prompt DSL packages, dataset, tests, validators;
2. `codex/m2-pilot-evidence` → infrastructure branch: Hero, Comparison, and Loop audit/index evidence;
3. one branch and pull request per new family, each based on the preceding stack tip, in this order:
   - Wave A: `cover`, `quote`, `big-number`, `collision`, `before-after`;
   - Wave B: `timeline`, `matrix`, `hierarchy`, `architecture`, `workflow`, `pipeline`, `decision-tree`, `framework`;
   - Wave C: `kpi`, `table`, `chart`, `dashboard`;
4. `codex/m2-catalog-release` → final family branch: generated index, all contact sheets, milestone-wide validation, and release documentation.

Each family commit contains only its canonical PNG, preview, Prompt DSL adjustments if generation exposed a contract defect, review entry, score row, index update, and status/changelog note. Pull requests are never merged automatically.

## Family execution order

### Pilot audit

Hero → Comparison → Loop. Confirm exact Pilot 01 asset path, prompt, review paragraph, score, dimensions, color mode, SHA-256, expression level, and semantic mechanism.

### Wave A — Editorial

Cover → Quote → Big Number → Collision → Before / After.

### Wave B — Structural

Timeline → Matrix → Hierarchy → Architecture → Workflow → Pipeline → Decision Tree → Framework.

### Wave C — Analytical prototypes

KPI → Table → Chart → Dashboard. All four reuse `data/agent-reliability-demo.yaml`. They demonstrate visual DNA only; quantitative grammar remains deferred to Milestone 5.

## Stop and escalation rules

Stop only when:

- built-in Codex image generation is unavailable after the complete Prompt DSL package exists;
- a passing candidate would require changing a locked design decision;
- two credible semantic directions have materially different product consequences that repository evidence cannot resolve.

Candidate failure alone is not a product gate: regenerate the failing family with the same contract and document the rejection.
