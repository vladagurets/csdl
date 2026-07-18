# CSDL Milestone 3 — Component Library Implementation Plan

**Date:** 2026-07-18

**Goal:** formalize the first fifteen CSDL components as canonical Markdown and machine-readable YAML so a composition can be described, validated, and reviewed using component vocabulary alone.

**Evidence audit:** [`docs/audits/2026-07-18-csdl-milestone-3-component-evidence.md`](../audits/2026-07-18-csdl-milestone-3-component-evidence.md)

## Scope and constraints

In scope:

- Anchor, Signal, Field, Frame, Cluster, Vector, Divider, Node, Loop, Collision, Bridge, Axis, Pulse, Label, and Legend;
- component semantics, visual/spatial contracts, dimensions/ranges, relations, family compatibility, A/B/C limits, typography/color constraints, do/don't examples, Prompt DSL syntax, validation invariants, and evidence provenance;
- compatibility with all twenty accepted Visual DNA families;
- editorial, structural, and analytical composition proofs using declared components and relations only;
- machine-readable indexes and milestone-level validation.

Out of scope:

- new GPT Image 2 generation or restoration of superseded rasters;
- Milestone 4 recipes or a full Prompt DSL redesign;
- full Analytical Mode, dark mode, portrait/mobile deliverables, public release, tags, or GitHub Releases;
- changes to Constructive Signal, Quiet Modular, Modular Technical, Muted Signal, 16:9, D-028, or canonical copy;
- any change to unrelated PR #7.

## Acceptance contract

Milestone 3 is complete only when all of the following are true:

1. the strict manifest contains exactly the fifteen required IDs and slugs in canonical order;
2. every component has a complete Markdown specification and machine-readable record containing all required semantic, spatial, relation, expression, typography/color, example, Prompt DSL, invariant, and evidence fields;
3. every evidence path exists, every locator is non-empty, and no rule claims positive raster evidence that is absent;
4. `Container` is retired from the Foundation and removed from active Milestone 2 family specifications plus manifest/Prompt DSL component arrays, with the vocabulary decision recorded in `DECISIONS.md` and no change to accepted raster bytes or family semantics;
5. the compatibility matrix covers all fifteen components and all twenty families, and every listed component/family reference exists;
6. allowed and forbidden relations are valid, use the declared relation vocabulary, and contain no identical unconditional contradiction;
7. one editorial, one structural, and one analytical proof validate using only declared component instances, declared relations, semantic attributes, and content/data references;
8. the analytical proof preserves its quantitative domain, values, order, and direct-label requirements exactly;
9. the final index and compatibility matrix are reproducibly built from canonical YAML and match checked-in outputs;
10. the full test suite, every Pilot validator, every Milestone 2 validator, every Milestone 3 validator, and `git diff --check` pass;
11. `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, `README.md`, and repository operating guidance describe Milestone 3 accurately;
12. the final integration PR is merged with green CI, and clean local `main` equals clean `origin/main` after a fresh fetch and strict revalidation.

**Primary signal:** met only when the three composition proofs can be reviewed without undeclared layout/geometry terminology and the validator rejects an injected undeclared primitive.

**Secondary signal:** met only when schema completeness, relation consistency, A/B/C limits, Prompt DSL syntax, evidence provenance, compatibility coverage, indexes, documentation, and regressions all pass.

## Canonical tree

```text
components/component-library-v0.1/
├── README.md
├── manifest.yaml
├── schema.yaml
├── TEMPLATE.md
├── index.yaml
├── compatibility.yaml
├── specs/
│   └── 01-anchor.md … 15-legend.md
├── proofs/
│   ├── 01-editorial.yaml
│   ├── 02-structural.yaml
│   └── 03-analytical.yaml
└── evaluation/
    └── review.md

tools/
├── build_component_library.py
├── validate_component_library.py
├── validate_component_proofs.py
└── validate_component_index.py

tests/
├── test_build_component_library.py
├── test_validate_component_library.py
├── test_validate_component_proofs.py
└── test_validate_component_index.py
```

No raster directory is added. Component do/don't evidence uses repository paths and locators into accepted reviews/specs or the D-028 boards.

## Machine-readable contract

### Library metadata

`manifest.yaml` owns:

- library ID, version, source milestone, canvas, orientation, component count, Markdown authority, and D-028 visual authority;
- required composition vocabulary and relation vocabulary;
- paths to schema, compatibility matrix, proofs, evaluation record, and generated index;
- canonical component records.

### Component record

Every component record defines:

```yaml
id: "01"
slug: anchor
name: Anchor
category: semantic
purpose: "..."
semantic_meaning: "..."
spatial_contract:
  count: {min: 1, max: 1}
  placement: [free]
  negative_space_percent: {min: 50, max: 75}
dimensions:
  unit: px
  width: {min: 0, max: 1728}
  height: {min: 0, max: 936}
  area_percent: {min: 0, max: 100}
relations:
  allowed:
    - {type: attached_to, target: Label, direction: inbound, cardinality: zero_or_many}
  forbidden:
    - {type: decorates, target: any, condition: always}
compatible_families: [hero]
expression_limits:
  A: {status: allowed, max_count: 1}
  B: {status: allowed, max_count: 2}
  C: {status: conditional, max_count: 2}
typography: {role: display, constraints: [all_text_horizontal]}
semantic_color: {default: ink.primary, signal_target_allowed: true}
examples:
  do:
    - {description: "...", evidence: "..."}
  dont:
    - {description: "...", evidence: "..."}
prompt_dsl:
  syntax: "Anchor(id=thesis, role=primary)"
  required_fields: [id, role]
  optional_fields: []
validation_invariants: ["..."]
evidence:
  - {path: "...", locator: "...", supports: "..."}
specification: specs/01-anchor.md
evidence_level: strong
```

The concrete records may narrow ranges or add mode-specific fields. Zero-valued minima are allowed only where absence is valid at a given expression level; they are not placeholders.

### Relation vocabulary

The initial relation enum is deliberately small:

```text
inside, contains, attached_to, connected_to, directs, separates,
orders, overlaps, produces, groups, maps_to, highlights, bounds, repeats
```

Relations are directional, and every relation contract declares `direction` as `inbound`, `outbound`, or `either`. Symmetric behavior must be declared explicitly by the owning component or normalized by the validator. The schema rejects arbitrary predicates.

### Expression-level contract

Each component has an A/B/C entry with:

- `status`: `allowed`, `conditional`, or `forbidden`;
- maximum instance count;
- optional area, node, item, or relation ceilings;
- a non-empty condition when status is conditional;
- a non-empty reason when status is forbidden.

The global Foundation density and signal-area rules remain authoritative. Component records may narrow but never widen them.

### Evidence contract

Every positive or negative example includes:

- a repository-relative path that exists;
- a locator such as a Markdown heading, YAML key, review family heading, or named canonical board region;
- a concise statement of what the evidence supports;
- evidence level `strong`, `bounded`, or `constrained` at component level.

`Legend` is explicitly `constrained`: the library documents a narrow exception and direct-label precedence without claiming an accepted Legend raster.

## Markdown specification template

Every `specs/<id>-<slug>.md` contains these exact headings:

1. Purpose
2. Semantic meaning
3. Visual and spatial contract
4. Dimensions and ranges
5. Allowed relations
6. Forbidden relations
7. Compatible Visual DNA families
8. Expression levels
9. Typography and semantic color
10. Do examples
11. Don't examples
12. Prompt DSL syntax
13. Validation invariants
14. Milestone 2 evidence

The Markdown explains intent and trade-offs. YAML carries values required for validation. A validator checks section presence and rejects placeholder markers.

## Compatibility matrix

`compatibility.yaml` is built from component records and contains:

- one row per component and one column per twenty-family slug;
- state `direct`, `conditional`, or `incompatible`;
- at least one direct/conditional component for every family;
- a family-centric reverse index for proof and review tooling;
- explicit `Legend` conditional status only for Chart and Dashboard;
- no `Container` row or reference.

The builder is deterministic. The validator compares the checked-in matrix with freshly derived data and rejects unknown families, duplicate rows, missing cells, and drift.

## Composition proof contract

Each proof YAML defines:

- ID, mode (`editorial`, `structural`, `analytical`), source family, expression level, evidence path, and content/data reference;
- `instances`, each with an ID and one declared component slug;
- `relations`, each using instance IDs and a declared relation enum;
- semantic attributes defined by the target component contract;
- no freeform `mechanism`, `layout`, `geometry`, `shape`, `plane`, `line`, `box`, `card`, `panel`, `grid`, `row`, `column`, or directional-position field.

Planned proofs:

1. **Editorial:** Big Number — Pulse, Anchor, Label, Signal.
2. **Structural:** Architecture — Field, Node, Bridge, Label, Signal role on the boundary/relation.
3. **Analytical:** Chart — Axis, Node, Label, Signal with fixed W1–W4 values and a 0–100 domain.

The analytical proof validator compares values/order/domain to `patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml`. It must reject a changed value, reordered period, truncated domain, missing direct Label, or added Legend.

## Validation strategy

### `validate_component_library.py`

Strict mode validates:

- readable manifest/schema;
- exact fifteen-component order and count;
- unique IDs, slugs, and names;
- all required fields and Markdown sections;
- enums, ranges, count bounds, expression-level entries, Prompt DSL fields, and no placeholders;
- valid family and evidence references;
- declared relation predicates/targets/cardinalities;
- no unconditional allowed/forbidden contradiction;
- no undeclared active component names in the Foundation component table or Milestone 2 manifest, Prompt DSL component arrays, and backticked family-spec component terms.

Programmatic `require_complete=False` accepts only a canonical-order subsequence of fully complete component records. It never accepts a partial record or an out-of-order component, while allowing dependency packets to add later canonical IDs such as `Label` before every intervening component exists.

### `validate_component_proofs.py`

Validates:

- exactly three mode-distinct proofs in strict mode;
- declared component instances and compatible source family;
- declared relation predicates and component-level relation permission;
- allowed expression level and count/area/item limits;
- absence of forbidden freeform layout/geometry keys;
- analytical data/domain/order fidelity and direct-label precedence.

### `build_component_library.py`

Builds `index.yaml` and `compatibility.yaml` deterministically from the manifest and proof set. It performs no raster mutation.

### `validate_component_index.py`

Rebuilds expected data in memory and rejects checked-in index/matrix drift, missing reverse mappings, or documentation/index inconsistency.

### Focused negative tests

Tests inject one defect at a time:

- sixteenth or missing component;
- duplicate ID/slug;
- missing semantic/relation/expression/Prompt DSL field;
- partial record in incomplete mode;
- invalid family or evidence path;
- contradictory relation;
- missing Markdown section or placeholder marker;
- undeclared `Container` or ad hoc proof primitive;
- incompatible component/family pair;
- analytical value/domain/order distortion;
- generated index/matrix drift.

## Dependency-aware packetization and stacked PR order

Every branch is based on the preceding stack tip. A public contract is edited by only one active packet at a time. Intermediate PRs are not merged automatically.

| Packet | Branch | Base | Components/deliverables |
|---:|---|---|---|
| 0 | `codex/m3-plan` | `main` | evidence audit and this implementation plan |
| 1 | `codex/m3-component-infrastructure` | packet 0 | tree, empty accepted-set manifest, schema, template, validators, builder, focused tests, README, evidence convention |
| 2 | `codex/m3-components-foundation` | packet 1 | Field, Frame, Anchor, Signal, Label; record the vocabulary decision and resolve `Container` aliases in the Foundation plus active M2 contracts |
| 3 | `codex/m3-components-units` | packet 2 | Node, Cluster, Divider, Axis |
| 4 | `codex/m3-components-relations` | packet 3 | Vector, Bridge, Loop, Collision |
| 5 | `codex/m3-components-analytical` | packet 4 | Pulse and constrained Legend |
| 6 | `codex/m3-composition-proofs` | packet 5 | three proofs, compatibility matrix, final index, evaluation review, strict milestone validators |
| 7 | `codex/m3-release` | packet 6 | completion audit and project documentation; final integration PR to `main` |

The infrastructure manifest contains no fake component entries. In incomplete validation, `components: []` is an honest accepted-set state. Each later packet appends only fully specified components in dependency order. Strict validation becomes green after packet 5 and remains green thereafter.

## Per-packet workflow

For each packet:

1. add a failing focused test at the contract boundary;
2. implement the minimum schema/tooling/spec changes;
3. run targeted tests;
4. run `validate_component_library(..., require_complete=False)` until all fifteen exist, then strict validation;
5. run relevant Milestone 2 catalog/data/index validators and the full Pilot/Milestone 2 regression set when active M2 contracts change;
6. update `components/component-library-v0.1/evaluation/review.md` with exact files, evidence status, validation commands/results, and unresolved risk;
7. commit, push, and open a stacked PR against the preceding branch;
8. do not merge the intermediate PR.

## Milestone-wide completion audit

Packet 6 and packet 7 run, in order:

```bash
.venv/bin/python -m pytest -q
.venv/bin/python tools/validate_manifest.py pilots/01-agentic-discipline/manifest.yaml
.venv/bin/python tools/validate_style_anchor.py pilots/01-agentic-discipline/references/style-anchor-light.png
.venv/bin/python tools/validate_assets.py pilots/01-agentic-discipline
.venv/bin/python tools/validate_scores.py pilots/01-agentic-discipline/evaluation/scores.csv
.venv/bin/python tools/validate_pattern_catalog.py patterns/visual-dna-sprint-01/manifest.yaml
.venv/bin/python tools/validate_pattern_data.py patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml
.venv/bin/python tools/validate_pattern_assets.py patterns/visual-dna-sprint-01
.venv/bin/python tools/validate_pattern_scores.py patterns/visual-dna-sprint-01/evaluation/scores.csv
.venv/bin/python tools/validate_pattern_review.py patterns/visual-dna-sprint-01
.venv/bin/python tools/build_pattern_catalog.py patterns/visual-dna-sprint-01
.venv/bin/python tools/validate_pattern_index.py patterns/visual-dna-sprint-01
.venv/bin/python tools/validate_component_library.py components/component-library-v0.1/manifest.yaml
.venv/bin/python tools/validate_component_proofs.py components/component-library-v0.1
.venv/bin/python tools/build_component_library.py components/component-library-v0.1
.venv/bin/python tools/validate_component_index.py components/component-library-v0.1
git diff --check
```

The final release PR is merged only after GitHub CI is green and the completion audit is recorded. The preferred merge method is a merge commit so packet history remains traceable.

## Exit, compatibility, and rollback implications

- No canonical raster changes are planned. Milestone 2 hashes, dimensions, scores, previews, and contact sheets must remain valid.
- Retiring `Container` changes active text/YAML vocabulary but not rendered semantics. Rollback is a normal commit revert; no migration or generated asset rollback is required.
- Component IDs/slugs become stable public identifiers for later milestones. Renaming requires a future explicit compatibility decision.
- The Prompt DSL addition is backward-compatible: existing family prompts remain valid after replacing the three `Container` aliases, and component proof syntax is additive.
- No production dependency, database, deployment, secret, permission, tag, or release artifact is involved.
- Milestone 4 remains planned and untouched.

## Stop rules

Stop and request a user decision only if:

- evidence forces a change to a locked decision or D-028 authority;
- `Container` cannot be retired without changing accepted visual semantics;
- a component requires new raster evidence to define a non-speculative contract;
- two contracts have materially different compatibility or quantitative consequences that repository evidence cannot resolve;
- GitHub permissions, required checks, or branch protection prevent the explicitly authorized final integration merge.

Otherwise choose the smallest repository-supported contract, record the limitation, and continue.
