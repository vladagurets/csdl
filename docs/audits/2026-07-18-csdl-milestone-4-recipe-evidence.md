# Milestone 4 Recipe and Prompt DSL Evidence Audit

**Audit date:** 2026-07-18  
**Repository baseline:** `main` and freshly fetched `origin/main` at `108da1ab69816f2a0a9a201e260a018fb3a9c12d`  
**Worktree at audit start:** clean  
**Scope:** Recipe Library and Prompt DSL v0.5 only; full Analytical Mode remains deferred.

## Audit question

What is the smallest evidence-backed recipe set that can convert a new outline into a deterministic CSDL generation package without inventing layout rules, while preserving accepted Pilot 01 and Visual DNA prompt contracts?

## Evidence reviewed

### Foundation

The Foundation specification establishes three calibrated recipes and the governing constraints for every later recipe:

- `001 Hero`: one proposition, one dominant Anchor, one Signal, A/B/C support, and 65–75% negative space at Level A;
- `005 Comparison`: two peer positions, one subordinate Divider, complementary rather than automatically adversarial semantics, and A/B/C support;
- `013 Loop`: one closed recurrence over three to five ordered stages, one active stage, and A/B/C support;
- one `1920×1080` landscape canvas, a `96×72` safe margin, one main idea, one mechanism, one dominant signal, and expression-specific negative-space/signal limits;
- declarative Prompt DSL, semantic geometry, Markdown authority, and explicit political/retro/decorative exclusions.

Sources: `specs/2026-07-17-csdl-v0.1-design.md` sections 5–13 and `DECISIONS.md` D-011 through D-018.

### Visual DNA Sprint 1

All twenty families have complete problem/scenario/component/assembly/expression/content/exclusion/Prompt DSL/evidence contracts in `patterns/visual-dna-sprint-01/manifest.yaml`, matching Markdown specifications, prompt packages, canonical evidence, scores, and review records.

| ID | Family | Distinct semantic need | Evidence status |
|---|---|---|---|
| 01 | Hero | one immediately understood proposition | accepted Pilot reference |
| 02 | Cover | establish a series or section premise | accepted generated evidence |
| 03 | Quote | present one exact statement as the idea | accepted generated evidence |
| 04 | Big Number | make one exact quantity explanatory | accepted generated evidence |
| 05 | Comparison | compare two peer systems or positions | accepted Pilot reference |
| 06 | Collision | show two forces producing one result | accepted generated evidence |
| 07 | Before / After | show a changed property across two states | accepted generated evidence |
| 08 | Timeline | show ordered change over time | accepted generated evidence |
| 09 | Matrix | place options on two independent dimensions | accepted generated evidence |
| 10 | Hierarchy | show ownership or decomposition depth | accepted generated evidence |
| 11 | Architecture | show stable system scope and permitted topology | accepted generated evidence |
| 12 | Workflow | show the next action in an operational sequence | accepted generated evidence |
| 13 | Loop | show recurrence that changes the next cycle | accepted Pilot reference |
| 14 | Pipeline | show material/data transformed through fixed gates | accepted generated evidence |
| 15 | Decision Tree | show a bounded branching rule and consequences | accepted generated evidence |
| 16 | Framework | organize mutually necessary peer concepts | accepted generated evidence |
| 17 | KPI | expose one bounded operational measure | accepted generated evidence |
| 18 | Table | support exact lookup in a small fixed dataset | accepted generated evidence |
| 19 | Chart | reveal one bounded quantitative trend honestly | accepted generated evidence |
| 20 | Dashboard | summarize a small operational state around one signal | accepted generated evidence |

The twenty needs are not superficial layout variants. The accepted review evidence distinguishes chronology from workflow, workflow from pipeline, hierarchy from topology, recurrence from open sequence, peer grouping from coordinate position, and snapshot/lookup/trend/composite analytical uses from one another.

The four analytical families are explicitly bounded prototypes. Their fixed dataset preserves week order, values, units, a 0–100 percent domain, direct labels, and `DEMO DATA` provenance. This evidence supports recipe contracts for those four existing scenarios, not bars, scatterplots, uncertainty, forecasts, or other Milestone 5 behavior.

### Component Library v0.1

`components/component-library-v0.1/manifest.yaml` locks exactly fifteen public components: Anchor, Signal, Field, Frame, Cluster, Vector, Divider, Node, Loop, Collision, Bridge, Axis, Pulse, Label, and constrained Legend. It defines fourteen public relation types, component cardinality and ranges, A/B/C limits, allowed and forbidden relations, family compatibility, Prompt DSL attributes, and validation invariants.

The deterministic `compatibility.yaml` covers all `15×20` component/family pairs. The three accepted composition proofs establish:

- editorial: Big Number through Anchor, Pulse, Label, and Signal;
- structural: Architecture through Field, Node, and Bridge;
- analytical: Chart through Axis, Node, Label, and Signal while preserving `[72, 78, 84, 90]` on `[0, 100]`.

The proof validator already rejects undeclared layout terminology, component-incompatible relations, and quantitative value distortion. Milestone 4 should reuse these contracts instead of creating Container, row/column, card, panel, box, coordinate, or other geometry primitives.

### Pilot 01 Prompt DSL and generation packages

The seven accepted slide prompts use seven recipe names. Four are already Visual DNA families: Hero, Framework, Comparison, and Loop. Three additional recipes have accepted canonical raster, candidate-selection, exact-copy, readability, score, and mechanism evidence:

| Proposed ID | Legacy name | Distinct need | Why it is not an alias |
|---|---|---|---|
| `021` | Breakdown | show a system whose expected recurrence has failed or detached | Loop requires one closed recurrence; Breakdown requires declared failed closure and detached consequences |
| `022` | Checklist | evaluate readiness through a bounded interrogative set | Framework groups peer concepts; Checklist groups required questions and produces a readiness gate |
| `023` | Formula | state an exact symbolic relationship and its result | Collision explains interacting forces; Formula preserves operators, operand order, equality, and exact result copy |

Pilot 01 also exposes v0.1 migration hazards: free-form zone terminology (`left`, `right`, `columns`, `2x2`), inconsistent `level` versus `expression`, `copy` versus `content`, component count maps versus explicit instances, and composition prose that predates the Milestone 3 compatibility matrix. A v0.5 migration must derive instances and relations from the selected recipe contract, retain exact content, and reject rather than preserve undeclared layout primitives.

The shared style-anchor prompt is calibration evidence, not a topic recipe. It remains an immutable legacy reference package and is referenced by v0.5 generation constraints; it is not promoted into a twenty-fourth recipe.

### Current schemas, validators, builders, and tests

Existing tooling establishes repository conventions used by Milestone 4:

- Python 3.11, PyYAML, Pillow, and pytest only; no new production dependency is necessary;
- strict and `require_complete=False` validation for staged contracts;
- exact top-level allowlists, placeholder rejection, evidence-path checks, canonical order/path rules, public-vocabulary checks, and deterministic derived-output comparison;
- mutation tests for unknown layout keys, forbidden relations, quantitative distortion, and generated-output drift;
- builders serialize with Unicode enabled and stable insertion order.

Baseline before Milestone 4 implementation:

```text
.venv/bin/python -m pytest -q
71 passed

Pilot 01 validators
manifest valid; style anchor valid; assets valid; scores valid

Milestone 2 validators/builders
pattern catalog/data/assets/scores/review/index valid; catalog built without drift

Milestone 3 validators/builders
component library/proofs/index valid; library built without drift
```

## Minimum justified recipe set

The evidence supports **23 recipes**:

1. the twenty accepted Visual DNA families, preserving their canonical order and IDs `001`–`020`;
2. Breakdown, Checklist, and Formula as IDs `021`–`023`, each backed by a distinct accepted Pilot 01 scenario.

It does not support approximately fifty distinct recipes. Expanding beyond 23 would either duplicate an existing semantic need, introduce unsupported component relations, or begin deferred Analytical Mode. The library must therefore stop at 23 until real usage produces new evidence.

## Prompt DSL v0.5 boundary

The evidence supports a declarative package with five separate concerns:

1. semantic intent and selected scenario;
2. immutable content references/bindings;
3. explicit instances from the fifteen-component public vocabulary;
4. explicit relations from the fourteen-relation public vocabulary;
5. deterministic generation constraints and hard exclusions.

The DSL may describe reading-path and presentation constraints through controlled enums, percentages, canvas values, typography roles, and semantic palette tokens. It must not encode placement through layout, geometry, coordinates, rows, columns, cards, panels, boxes, or other ad hoc primitives.

## Compatibility and rollback conclusion

- Recipe IDs/slugs and DSL version `0.5` are additive; accepted v0.1 source prompts and canonical rasters remain unchanged.
- Migration is mechanical: identify the recipe, bind exact legacy copy/data, instantiate the recipe's allowed component contract, apply deterministic defaults, and record the source path/version.
- Unsupported legacy hints are reported as normalized or rejected; they never become public vocabulary.
- A normal commit revert removes the Milestone 4 library and tooling without changing Pilot 01, Milestone 2, Milestone 3, schemas, data, or raster bytes.
- Full Analytical Mode, dark mode, portrait/mobile outputs, raster regeneration, public release, tags, and releases remain outside this milestone.

## Audit decision

Proceed with a 23-recipe Recipe Library v0.5 and Prompt DSL v0.5. Require complete Markdown and YAML contracts for every recipe, deterministic indexes and package building, strict/incomplete validators, three end-to-end proofs, one Pilot migration proof, negative fixtures, full regression validation, and clean-tree rebuild evidence before completion.
