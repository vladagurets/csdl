# CSDL Dynamics Expansion v0.1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an additive, evidence-gated Dynamics Expansion v0.1 package that adds four static dynamics recipes, two candidate components, six candidate relations, three deterministic analytical families, and twelve unpromoted visual candidates without changing canonical contracts or accepted raster evidence.

**Architecture:** Implement one isolated package under `extensions/dynamics-expansion-v0.1/`, following the existing Arsenal Expansion pattern while keeping every new term package-local. Separate normative records, deterministic builders, validators, visual-review tooling, and user-selection evidence so each boundary can be tested independently and rolled back without touching baseline consumers.

**Tech Stack:** Python 3.11+, PyYAML 6.x, Pillow 11.x, pytest 8.x, Markdown, YAML, built-in Codex image generation with GPT Image 2.

**Spec:** `docs/superpowers/specs/2026-09-03-csdl-dynamics-expansion-v0.1-design.md`

## Global Constraints

- Do not begin execution until D-035 has been selected, reviewed, and promoted into Component Library v0.2, Recipe Library v0.6, and Analytical Mode v0.2, or the actual equivalent promoted versions.
- At execution time, use `superpowers:using-git-worktrees` to create an isolated worktree from the promoted D-035 baseline; never execute this plan in the current dirty checkout.
- Preferred execution branch: `codex/dynamics-expansion-v0-1`.
- Keep all Dynamics vocabulary local to `extensions/dynamics-expansion-v0.1/`.
- Preserve the canonical `1920x1080` landscape canvas, Quiet Modular direction, A/B/C amplitude system, and static-output contract.
- Implement exactly 4 recipes, 2 candidate components, 6 candidate relations, and 3 analytical families.
- Generate exactly 3 materially different candidates per recipe, for 12 unique PNG files total.
- Do not mutate baseline manifests, Prompt DSL schemas, or the protected accepted-raster inventory.
- Public promotion is outside this plan.
- User selection is mandatory before accepted candidate scoring.
- Every commit step below is conditional on explicit user authorization to commit. Without that authorization, do not stage or commit; report the listed message as the suggested commit message.
- Do not add production dependencies. Use only Python, PyYAML, Pillow, pytest, and the standard library.
- Use `.venv/bin/python` for every Python command.

## File Responsibility Map

### Normative package

- `extensions/dynamics-expansion-v0.1/manifest.yaml`: identity, baseline, targets, exact candidate lists, evidence gates, and protected inventory.
- `extensions/dynamics-expansion-v0.1/schema.yaml`: required manifest and record shapes.
- `extensions/dynamics-expansion-v0.1/components/*.yaml`: machine-readable `Lane` and `Stock` contracts.
- `extensions/dynamics-expansion-v0.1/components/*.md`: canonical component explanations.
- `extensions/dynamics-expansion-v0.1/relations/relations.yaml`: six candidate relation contracts.
- `extensions/dynamics-expansion-v0.1/recipes/*.yaml`: machine-readable recipe contracts.
- `extensions/dynamics-expansion-v0.1/recipes/*.md`: canonical recipe explanations.
- `extensions/dynamics-expansion-v0.1/prompts/*.yaml`: exact visible copy, reference roles, and three material candidate directions.
- `extensions/dynamics-expansion-v0.1/analytics/families.yaml`: analytical family contracts.
- `extensions/dynamics-expansion-v0.1/analytics/datasets/*.yaml`: fixed typed synthetic data.
- `extensions/dynamics-expansion-v0.1/analytics/proofs/*.yaml`: deterministic derived proofs.
- `extensions/dynamics-expansion-v0.1/fixtures/negative/*.yaml`: exact invalid mutations and expected errors.

### Tooling

- `tools/build_dynamics_expansion.py`: derive analytical proofs, index, and compatibility outputs.
- `tools/validate_dynamics_expansion.py`: validate all normative, analytical, compatibility, and protected-raster contracts.
- `tools/build_dynamics_review.py`: validate candidates, build four comparison boards, build one overview, and write hashes.
- `tests/test_dynamics_expansion.py`: focused TDD coverage for every package boundary and mutation.

### Visual evidence

- `extensions/dynamics-expansion-v0.1/drafts/light/16x9/<recipe>/v1.png` through `v3.png`: ignored independent candidates.
- `extensions/dynamics-expansion-v0.1/selection/boards/*.png`: four review boards.
- `extensions/dynamics-expansion-v0.1/selection/overview.png`: four-board review overview.
- `extensions/dynamics-expansion-v0.1/selection/candidate-hashes.yaml`: candidate metadata and SHA-256 inventory.
- `extensions/dynamics-expansion-v0.1/selection/selected/*.png`: user-selected package-local evidence, created only after selection.
- `extensions/dynamics-expansion-v0.1/evaluation/review.md`: filenames, copy review, rejection reasons, selection rationale, and risks.
- `extensions/dynamics-expansion-v0.1/evaluation/scores.csv`: accepted-candidate rubric scores after user selection.

---

### Task 1: Bind the package identity and version boundary

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/manifest.yaml`
- Create: `extensions/dynamics-expansion-v0.1/schema.yaml`
- Create: `extensions/dynamics-expansion-v0.1/README.md`
- Create: `extensions/dynamics-expansion-v0.1/SPEC.md`
- Create: `extensions/dynamics-expansion-v0.1/MIGRATION.md`
- Create: `extensions/dynamics-expansion-v0.1/ROLLBACK.md`
- Create: `tools/validate_dynamics_expansion.py`
- Create: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: promoted D-035 manifests at `components/component-library-v0.2/manifest.yaml`, `recipes/recipe-library-v0.6/manifest.yaml`, and `analytics/analytical-mode-v0.2/manifest.yaml`.
- Produces: `validate_identity(manifest: dict[str, Any]) -> list[str]`, `validate_baseline(repository: Path, manifest: dict[str, Any]) -> list[str]`, and the exact manifest lists consumed by all later tasks.

- [ ] **Step 1: Write the failing identity and baseline tests**

```python
from pathlib import Path

import yaml

from tools.validate_dynamics_expansion import validate_baseline, validate_identity


ROOT = Path(__file__).parents[1]
DYNAMICS = ROOT / "extensions/dynamics-expansion-v0.1"


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_dynamics_identity_and_exact_candidate_lists() -> None:
    manifest = _load(DYNAMICS / "manifest.yaml")
    assert validate_identity(manifest) == []
    assert [entry["name"] for entry in manifest["components"]] == ["Lane", "Stock"]
    assert [entry["name"] for entry in manifest["recipes"]] == [
        "Interaction Sequence",
        "Feedback Control",
        "Stock / Flow",
        "Scenario Fan",
    ]
    assert manifest["relations"] == [
        "sends_to",
        "measures",
        "corrects",
        "flows_into",
        "flows_out_of",
        "diverges_to",
    ]
    assert manifest["analytical_families"] == [
        "controlchart",
        "slopegraph",
        "dotplot",
    ]


def test_dynamics_baseline_is_the_promoted_d035_contract() -> None:
    manifest = _load(DYNAMICS / "manifest.yaml")
    assert validate_baseline(ROOT, manifest) == []
    assert manifest["baseline"] == {
        "component_library": "components/component-library-v0.2/manifest.yaml",
        "component_count": 18,
        "recipe_library": "recipes/recipe-library-v0.6/manifest.yaml",
        "recipe_count": 31,
        "analytical_mode": "analytics/analytical-mode-v0.2/manifest.yaml",
        "analytical_family_count": 16,
    }
```

- [ ] **Step 2: Run the focused tests and confirm the expected failure**

Run:

```bash
.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_dynamics_identity_and_exact_candidate_lists tests/test_dynamics_expansion.py::test_dynamics_baseline_is_the_promoted_d035_contract -q
```

Expected: FAIL because `tools.validate_dynamics_expansion` and the package manifest do not exist.

- [ ] **Step 3: Create the exact manifest contract**

```yaml
extension:
  id: dynamics-expansion-v0.1
  version: 0.1.0
  status: candidate
  language: CSDL
  kind: evidence-gated-extension

baseline:
  component_library: components/component-library-v0.2/manifest.yaml
  component_count: 18
  recipe_library: recipes/recipe-library-v0.6/manifest.yaml
  recipe_count: 31
  analytical_mode: analytics/analytical-mode-v0.2/manifest.yaml
  analytical_family_count: 16

targets:
  component_library: component-library-v0.3
  component_count: 20
  recipe_library: recipe-library-v0.7
  recipe_count: 35
  analytical_mode: analytical-mode-v0.3
  analytical_family_count: 19

protected_raster_inventory: accessibility/night-mode-v0.1/evaluation/raster-hashes.yaml

components:
  - {name: Lane, record: components/lane.yaml}
  - {name: Stock, record: components/stock.yaml}

relations: [sends_to, measures, corrects, flows_into, flows_out_of, diverges_to]

recipes:
  - {id: '032', name: Interaction Sequence, record: recipes/032-interaction-sequence.yaml}
  - {id: '033', name: Feedback Control, record: recipes/033-feedback-control.yaml}
  - {id: '034', name: Stock / Flow, record: recipes/034-stock-flow.yaml}
  - {id: '035', name: Scenario Fan, record: recipes/035-scenario-fan.yaml}

analytical_families: [controlchart, slopegraph, dotplot]

analytical_datasets:
  - {id: 01-controlchart, family: controlchart, path: analytics/datasets/01-controlchart.yaml}
  - {id: 02-slopegraph, family: slopegraph, path: analytics/datasets/02-slopegraph.yaml}
  - {id: 03-dotplot, family: dotplot, path: analytics/datasets/03-dotplot.yaml}

generated:
  index: generated/index.yaml
  compatibility: generated/compatibility.yaml

evidence_gate:
  recipe_candidate_count: 3
  visual_selection: user
  accepted_raster_dimensions: 1920x1080
  accepted_raster_mode: RGB
  public_promotion_before_selection: false
  public_component_minimum_distinct_uses: 2
  analytical_raster_required: false
  animation_allowed: false
  existing_raster_mutation: forbidden
```

- [ ] **Step 4: Implement identity and baseline validation**

```python
EXPECTED_IDENTITY = {
    "id": "dynamics-expansion-v0.1",
    "version": "0.1.0",
    "status": "candidate",
    "language": "CSDL",
    "kind": "evidence-gated-extension",
}
EXPECTED_COMPONENTS = ["Lane", "Stock"]
EXPECTED_RECIPES = [
    "Interaction Sequence",
    "Feedback Control",
    "Stock / Flow",
    "Scenario Fan",
]
EXPECTED_RELATIONS = [
    "sends_to",
    "measures",
    "corrects",
    "flows_into",
    "flows_out_of",
    "diverges_to",
]
EXPECTED_ANALYTICAL_FAMILIES = ["controlchart", "slopegraph", "dotplot"]


def validate_identity(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if manifest.get("extension") != EXPECTED_IDENTITY:
        errors.append("dynamics extension identity must match v0.1 candidate contract")
    if [entry.get("name") for entry in manifest.get("components", [])] != EXPECTED_COMPONENTS:
        errors.append("dynamics component order must be Lane, Stock")
    if [entry.get("name") for entry in manifest.get("recipes", [])] != EXPECTED_RECIPES:
        errors.append("dynamics recipe order must match IDs 032-035")
    if manifest.get("relations") != EXPECTED_RELATIONS:
        errors.append("dynamics relation order must match the approved contract")
    if manifest.get("analytical_families") != EXPECTED_ANALYTICAL_FAMILIES:
        errors.append("dynamics analytical family order must match the approved contract")
    return errors
```

Implement `validate_baseline()` with the same count-reading pattern as `validate_arsenal_expansion.py`, but require counts `18`, `31`, and `16` from the promoted manifests.

- [ ] **Step 5: Add the package schema and normative overview documents**

`schema.yaml` must require all top-level manifest keys shown above, string recipe IDs, candidate status, and exact record paths. `README.md` and package `SPEC.md` must state that D-035 promotion is a prerequisite, animation is forbidden, and public promotion is outside the package. `MIGRATION.md` and `ROLLBACK.md` must use the additive sequence from design sections 21 and 22 without claiming automatic migration.

- [ ] **Step 6: Run the focused tests**

Run:

```bash
.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_dynamics_identity_and_exact_candidate_lists tests/test_dynamics_expansion.py::test_dynamics_baseline_is_the_promoted_d035_contract -q
```

Expected: `2 passed`.

- [ ] **Step 7: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/manifest.yaml extensions/dynamics-expansion-v0.1/schema.yaml extensions/dynamics-expansion-v0.1/README.md extensions/dynamics-expansion-v0.1/SPEC.md extensions/dynamics-expansion-v0.1/MIGRATION.md extensions/dynamics-expansion-v0.1/ROLLBACK.md tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: define dynamics expansion contract"
```

---

### Task 2: Define Lane, Stock, and candidate relations

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/components/lane.yaml`
- Create: `extensions/dynamics-expansion-v0.1/components/lane.md`
- Create: `extensions/dynamics-expansion-v0.1/components/stock.yaml`
- Create: `extensions/dynamics-expansion-v0.1/components/stock.md`
- Create: `extensions/dynamics-expansion-v0.1/relations/relations.yaml`
- Modify: `tools/validate_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: `EXPECTED_COMPONENTS`, `EXPECTED_RELATIONS`, `_load(path, errors, label)`.
- Produces: `validate_candidate_vocabulary(root: Path, manifest: dict[str, Any]) -> tuple[list[str], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]`.

- [ ] **Step 1: Write failing vocabulary tests**

Extend the existing validator import with `validate_candidate_vocabulary`.

```python
def test_candidate_components_and_relations_are_distinct() -> None:
    manifest = _load(DYNAMICS / "manifest.yaml")
    errors, components, relations = validate_candidate_vocabulary(DYNAMICS, manifest)
    assert errors == []
    assert list(components) == ["Lane", "Stock"]
    assert list(relations) == [
        "sends_to", "measures", "corrects",
        "flows_into", "flows_out_of", "diverges_to",
    ]
    assert components["Lane"]["required_evidence"] == [
        "032 Interaction Sequence", "033 Feedback Control",
    ]
    assert components["Stock"]["required_evidence"] == [
        "033 Feedback Control", "034 Stock / Flow",
    ]
```

- [ ] **Step 2: Run the test and confirm failure**

Run:

```bash
.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_candidate_components_and_relations_are_distinct -q
```

Expected: FAIL because the vocabulary files and validator function do not exist.

- [ ] **Step 3: Create the component records**

```yaml
# components/lane.yaml
name: Lane
slug: lane
status: candidate
category: structural
semantic_meaning: A stable channel of responsibility owned by one actor, controller, system, or workstream across an ordered interaction.
distinct_from:
  Field: context without ordered responsibility
  Cluster: grouping without a temporal route
  Band: bounded interval on an Axis
  Frame: functional boundary or lookup scope
required_evidence: ['032 Interaction Sequence', '033 Feedback Control']
relations: [contains, attached_to, orders, sends_to, measures, corrects]
validation_invariants:
  - One Lane has exactly one declared owner.
  - Lane order is non-semantic unless the recipe declares it.
  - Lane width and color never imply priority by themselves.
  - A Lane is not a decorative card or UI panel.
specification: components/lane.md
```

```yaml
# components/stock.yaml
name: Stock
slug: stock
status: candidate
category: semantic-analytical
semantic_meaning: A declared quantity or state changed through measured inflows and outflows with conservation semantics.
distinct_from:
  Node: generic entity, state, actor, or stage
  Pulse: highlighted exact value without accumulation semantics
  Cluster: group without conservation
  Band: interval rather than stored state
required_evidence: ['033 Feedback Control', '034 Stock / Flow']
relations: [flows_into, flows_out_of, measures, highlights, attached_to, bounds]
validation_invariants:
  - Stock identity and unit are explicit.
  - Starting value plus inflows minus outflows equals ending value.
  - Area is non-quantitative unless an analytical encoding declares it.
  - Color is not the only carrier of stock state.
specification: components/stock.md
```

- [ ] **Step 4: Create the exact relation records**

```yaml
language: CSDL
version: 0.1-candidate
relations:
  sends_to:
    subject_categories: [actor, Lane, Node]
    object_categories: [actor, Lane, Node]
    meaning: Transmit a named message, request, result, or response.
    exclusions: [causation, ownership, guaranteed delivery]
  measures:
    subject_categories: [controller, observer, Lane, Trace, Node]
    object_categories: [Stock, Node, Pulse]
    meaning: Read a named property, unit, and observation point from a target.
    exclusions: [undeclared field, implicit unit]
  corrects:
    subject_categories: [controller, Lane, Vector, Node]
    object_categories: [Stock, Node]
    meaning: Change a measured state in response to a declared deviation.
    exclusions: [unmeasured intervention, undeclared direction]
  flows_into:
    subject_categories: [Vector, Trace, Node]
    object_categories: [Stock]
    meaning: Increase a Stock by a declared rate or quantity over an interval.
    exclusions: [unsigned quantity, missing unit]
  flows_out_of:
    subject_categories: [Stock]
    object_categories: [Vector, Trace, Node]
    meaning: Decrease a Stock by a declared rate or quantity over an interval.
    exclusions: [unsigned quantity, missing unit]
  diverges_to:
    subject_categories: [Node, Trace]
    object_categories: [Trace]
    meaning: Separate one observed state into named future scenario paths.
    exclusions: [implicit decision, invented probability]
```

- [ ] **Step 5: Implement vocabulary validation**

Validate exact candidate status, category, semantic meaning, non-empty distinctions, required evidence, Markdown specification existence, relation order, relation meaning, and non-empty exclusions. Reject `Gate`, `Delta`, `Container`, `Layer`, `Marker`, and `Path` as component aliases.

Add these test helpers after the vocabulary records exist so every recipe test resolves the promoted baseline and package-local candidates through one stable interface:

```python
def _allowed_components() -> set[str]:
    manifest = _load(DYNAMICS / "manifest.yaml")
    baseline = _load(ROOT / manifest["baseline"]["component_library"])
    return set(baseline["vocabulary"]["components"]) | {
        entry["name"] for entry in manifest["components"]
    }


def _allowed_relations() -> set[str]:
    manifest = _load(DYNAMICS / "manifest.yaml")
    baseline = _load(ROOT / manifest["baseline"]["component_library"])
    return set(baseline["vocabulary"]["relations"]) | set(manifest["relations"])
```

- [ ] **Step 6: Run the focused test**

Run:

```bash
.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_candidate_components_and_relations_are_distinct -q
```

Expected: PASS.

- [ ] **Step 7: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/components extensions/dynamics-expansion-v0.1/relations tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: add dynamics vocabulary candidates"
```

---

### Task 3: Add Interaction Sequence

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/recipes/032-interaction-sequence.yaml`
- Create: `extensions/dynamics-expansion-v0.1/recipes/032-interaction-sequence.md`
- Create: `extensions/dynamics-expansion-v0.1/prompts/032-interaction-sequence.yaml`
- Modify: `tools/validate_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: allowed baseline plus candidate components and relations.
- Produces: `validate_recipe_record(root: Path, entry: dict[str, Any], allowed_components: set[str], allowed_relations: set[str]) -> list[str]` and recipe ID `032`.

- [ ] **Step 1: Write the failing recipe test**

Extend the existing validator import with `validate_recipe_record`.

```python
def test_interaction_sequence_owns_actor_time_messages() -> None:
    manifest = _load(DYNAMICS / "manifest.yaml")
    entry = manifest["recipes"][0]
    errors = validate_recipe_record(DYNAMICS, entry, _allowed_components(), _allowed_relations())
    assert errors == []
    recipe = _load(DYNAMICS / entry["record"])
    assert recipe["id"] == "032"
    assert recipe["expression_levels"] == {"A": "allowed", "B": "allowed", "C": "forbidden"}
    assert recipe["content_contract"]["visible_copy"] == [
        "ДЕ АГЕНТ ЧЕКАЄ", "USER", "AGENT", "TOOL", "ЗАПИТ",
        "ВИКЛИК", "РЕЗУЛЬТАТ", "ВІДПОВІДЬ", "ОЧІКУВАННЯ", "RETRY",
    ]
```

- [ ] **Step 2: Run the test and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_interaction_sequence_owns_actor_time_messages -q`

Expected: FAIL because recipe `032` does not exist.

- [ ] **Step 3: Create the machine-readable recipe**

```yaml
id: '032'
slug: interaction-sequence
name: Interaction Sequence
version: 0.7-candidate
status: candidate
problem: Explain ordered message exchange between multiple actors, including waits, returns, errors, or retries.
distinguishes_from: Workflow owns operational order and Architecture owns stable boundaries; Interaction Sequence owns actor-to-actor message chronology.
allowed_scenarios: [API flow, agent handoff, authentication, failure and retry]
ingredients:
  required:
    - {component: Lane, min: 2, max: 4, default: 3}
    - {component: Node, min: 2, max: 8, default: 4}
    - {component: Trace, min: 1, max: 3, default: 1}
    - {component: Vector, min: 2, max: 8, default: 4}
    - {component: Label, min: 4, max: 12, default: 8}
    - {component: Signal, min: 1, max: 1, default: 1}
  optional: []
relations:
  allowed:
    - {subject: Lane, type: sends_to, object: Lane}
    - {subject: Vector, type: directs, object: Node}
    - {subject: Axis, type: orders, object: Node}
    - {subject: Label, type: attached_to, object: Node}
    - {subject: Signal, type: highlights, object: Node}
  forbidden:
    - {subject: Lane, type: causes, object: Lane}
assembly_order: [declare actors, order messages, expose wait or retry, mark one dominant signal]
expression_levels: {A: allowed, B: allowed, C: forbidden}
expression_modes: [structural]
content_contract:
  exact: true
  visible_copy: [ДЕ АГЕНТ ЧЕКАЄ, USER, AGENT, TOOL, ЗАПИТ, ВИКЛИК, РЕЗУЛЬТАТ, ВІДПОВІДЬ, ОЧІКУВАННЯ, RETRY]
prompt: prompts/032-interaction-sequence.yaml
specification: recipes/032-interaction-sequence.md
record: recipes/032-interaction-sequence.yaml
```

- [ ] **Step 4: Create the Markdown and prompt contracts**

The Markdown file must reproduce design section 10.1. The prompt file must declare the exact visible copy above, the four canonical reference roles, hard exclusions, and these three material directions:

```yaml
candidate_directions:
  v1: parallel actor Lanes with a vertical time route
  v2: central Agent Lane with mirrored request and response Traces
  v3: compact stepped interaction with one explicit wait interval and retry path
```

- [ ] **Step 5: Implement generic recipe validation**

Validate identity, status, non-empty problem and distinction, at least two scenarios, exact A/B/C keys with C forbidden, allowed components, allowed relations, cardinality bounds, prompt/spec/record paths, exact visible-copy list, and absence of layout keys `layout`, `geometry`, `coordinates`, `card`, `panel`, `container`, and `sidebar`.

- [ ] **Step 6: Run the test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_interaction_sequence_owns_actor_time_messages -q`

Expected: PASS.

- [ ] **Step 7: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/recipes/032-interaction-sequence.* extensions/dynamics-expansion-v0.1/prompts/032-interaction-sequence.yaml tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: define interaction sequence recipe"
```

---

### Task 4: Add Feedback Control

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/recipes/033-feedback-control.yaml`
- Create: `extensions/dynamics-expansion-v0.1/recipes/033-feedback-control.md`
- Create: `extensions/dynamics-expansion-v0.1/prompts/033-feedback-control.yaml`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: `validate_recipe_record()` from Task 3.
- Produces: recipe ID `033` using both `Lane` and `Stock` evidence.

- [ ] **Step 1: Write the failing test**

```python
def test_feedback_control_owns_measured_correction() -> None:
    entry = _load(DYNAMICS / "manifest.yaml")["recipes"][1]
    assert validate_recipe_record(DYNAMICS, entry, _allowed_components(), _allowed_relations()) == []
    recipe = _load(DYNAMICS / entry["record"])
    assert {item["component"] for item in recipe["ingredients"]["required"]} >= {
        "Lane", "Stock", "Loop", "Threshold", "Trace", "Pulse", "Signal", "Label"
    }
    assert {item["type"] for item in recipe["relations"]["allowed"]} >= {"measures", "corrects"}
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_feedback_control_owns_measured_correction -q`

Expected: FAIL because recipe `033` does not exist.

- [ ] **Step 3: Create the recipe record**

Use the exact contract from design section 10.2 with:

```yaml
id: '033'
slug: feedback-control
name: Feedback Control
version: 0.7-candidate
status: candidate
problem: Explain how a system measures deviation from a target and applies a corrective action.
distinguishes_from: Loop owns recurrence, Causal Chain owns one-way consequence, and State Machine owns guarded states; Feedback Control owns target, measurement, deviation, and correction.
allowed_scenarios: [agent autonomy, quality control, reliability, budget control]
expression_levels: {A: allowed, B: allowed, C: forbidden}
expression_modes: [structural, analytical]
content_contract:
  exact: true
  visible_copy: [АВТОНОМНІСТЬ ПОТРЕБУЄ FEEDBACK, TARGET, MEASURE, COMPARE, CORRECT, BACKLOG, ВІДХИЛЕННЯ]
prompt: prompts/033-feedback-control.yaml
specification: recipes/033-feedback-control.md
record: recipes/033-feedback-control.yaml
```

Required ingredient cardinalities and relations must match design section 10.2 exactly.

Use this exact machine-readable block:

```yaml
ingredients:
  required:
    - {component: Lane, min: 2, max: 2, default: 2}
    - {component: Stock, min: 1, max: 1, default: 1}
    - {component: Loop, min: 1, max: 1, default: 1}
    - {component: Threshold, min: 1, max: 2, default: 1}
    - {component: Trace, min: 1, max: 1, default: 1}
    - {component: Pulse, min: 1, max: 2, default: 1}
    - {component: Signal, min: 1, max: 1, default: 1}
    - {component: Label, min: 4, max: 10, default: 7}
  optional: []
relations:
  allowed:
    - {subject: Lane, type: measures, object: Stock}
    - {subject: Lane, type: corrects, object: Stock}
    - {subject: Trace, type: crosses, object: Threshold}
    - {subject: Loop, type: repeats, object: Trace}
    - {subject: Signal, type: highlights, object: Stock}
    - {subject: Label, type: attached_to, object: Stock}
  forbidden:
    - {subject: Lane, type: causes, object: Stock}
assembly_order: [declare target, measure stock, expose deviation, apply correction, close feedback route]
```

- [ ] **Step 4: Create Markdown and prompt contracts**

```yaml
candidate_directions:
  v1: closed control Loop around one measured Stock
  v2: controller and system Lanes with one returning Trace
  v3: target-to-deviation Axis with an explicit corrective return path
```

- [ ] **Step 5: Run the test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_feedback_control_owns_measured_correction -q`

Expected: PASS.

- [ ] **Step 6: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/recipes/033-feedback-control.* extensions/dynamics-expansion-v0.1/prompts/033-feedback-control.yaml tests/test_dynamics_expansion.py
git commit -m "feat: define feedback control recipe"
```

---

### Task 5: Add Stock / Flow

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/recipes/034-stock-flow.yaml`
- Create: `extensions/dynamics-expansion-v0.1/recipes/034-stock-flow.md`
- Create: `extensions/dynamics-expansion-v0.1/prompts/034-stock-flow.yaml`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: `validate_recipe_record()` and `Stock` relation contract.
- Produces: recipe ID `034` and the exact conservation example `24 + 12 - 8 = 28`.

- [ ] **Step 1: Write the failing test**

```python
def test_stock_flow_owns_conservation() -> None:
    entry = _load(DYNAMICS / "manifest.yaml")["recipes"][2]
    assert validate_recipe_record(DYNAMICS, entry, _allowed_components(), _allowed_relations()) == []
    recipe = _load(DYNAMICS / entry["record"])
    assert recipe["quantitative_contract"] == {
        "unit": "tasks",
        "start": 24,
        "inflow": 12,
        "outflow": 8,
        "end": 28,
        "equation": "24 + 12 - 8 = 28",
    }
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_stock_flow_owns_conservation -q`

Expected: FAIL because recipe `034` does not exist.

- [ ] **Step 3: Create the recipe record**

Use design section 10.3 and include:

```yaml
id: '034'
slug: stock-flow
name: Stock / Flow
version: 0.7-candidate
status: candidate
problem: Explain how inflows and outflows change a stored state over a declared interval.
distinguishes_from: Pipeline owns transformation, Sankey owns flow distribution, and Waterfall owns signed reconciliation; Stock / Flow owns persistent accumulated state.
allowed_scenarios: [backlog, technical debt, capacity, cash reserve]
expression_levels: {A: allowed, B: allowed, C: forbidden}
expression_modes: [structural, analytical]
content_contract:
  exact: true
  visible_copy: [BACKLOG ЗМІНЮЄТЬСЯ ПОТОКАМИ, ПОЧАТОК 24, НОВІ ЗАДАЧІ +12, BACKLOG 28, ЗАВЕРШЕНО -8]
quantitative_contract:
  unit: tasks
  start: 24
  inflow: 12
  outflow: 8
  end: 28
  equation: 24 + 12 - 8 = 28
prompt: prompts/034-stock-flow.yaml
specification: recipes/034-stock-flow.md
record: recipes/034-stock-flow.yaml
```

Use this exact ingredient and relation block:

```yaml
ingredients:
  required:
    - {component: Stock, min: 1, max: 1, default: 1}
    - {component: Vector, min: 2, max: 4, default: 2}
    - {component: Pulse, min: 3, max: 6, default: 4}
    - {component: Label, min: 4, max: 10, default: 5}
    - {component: Signal, min: 1, max: 1, default: 1}
  optional:
    - {component: Axis, min: 0, max: 1, default: 0}
    - {component: Band, min: 0, max: 1, default: 0}
    - {component: Threshold, min: 0, max: 1, default: 0}
relations:
  allowed:
    - {subject: Vector, type: flows_into, object: Stock}
    - {subject: Stock, type: flows_out_of, object: Vector}
    - {subject: Label, type: attached_to, object: Stock}
    - {subject: Signal, type: highlights, object: Stock}
    - {subject: Band, type: bounds, object: Stock, condition: when_interval_is_declared}
  forbidden:
    - {subject: Stock, type: produces, object: Stock}
assembly_order: [declare starting stock, declare inflow, declare outflow, reconcile ending stock, mark the dominant value]
```

- [ ] **Step 4: Add conservation validation**

```python
def validate_stock_equation(contract: dict[str, Any]) -> list[str]:
    if contract["start"] + contract["inflow"] - contract["outflow"] != contract["end"]:
        return ["Stock / Flow values must reconcile start + inflow - outflow = end"]
    expected = f'{contract["start"]} + {contract["inflow"]} - {contract["outflow"]} = {contract["end"]}'
    return [] if contract["equation"] == expected else ["Stock / Flow equation must match exact values"]
```

- [ ] **Step 5: Create Markdown and prompt contracts**

```yaml
candidate_directions:
  v1: horizontal inflow-stock-outflow composition
  v2: central Stock with opposed signed Vectors and direct reconciliation
  v3: interval-based change with start and end stock states connected by flows
```

- [ ] **Step 6: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_stock_flow_owns_conservation -q`

Expected: PASS.

- [ ] **Step 7: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/recipes/034-stock-flow.* extensions/dynamics-expansion-v0.1/prompts/034-stock-flow.yaml tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: define stock flow recipe"
```

---

### Task 6: Add Scenario Fan

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/recipes/035-scenario-fan.yaml`
- Create: `extensions/dynamics-expansion-v0.1/recipes/035-scenario-fan.md`
- Create: `extensions/dynamics-expansion-v0.1/prompts/035-scenario-fan.yaml`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: `validate_recipe_record()` and `diverges_to` relation.
- Produces: recipe ID `035` with named paths but no probabilities.

- [ ] **Step 1: Write the failing test**

```python
def test_scenario_fan_owns_uncertain_trajectories_without_invented_probability() -> None:
    entry = _load(DYNAMICS / "manifest.yaml")["recipes"][3]
    assert validate_recipe_record(DYNAMICS, entry, _allowed_components(), _allowed_relations()) == []
    recipe = _load(DYNAMICS / entry["record"])
    assert recipe["scenario_contract"]["probabilities"] == "not_provided"
    assert recipe["scenario_contract"]["paths"] == ["BASELINE", "GUARDED", "AUTONOMOUS"]
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_scenario_fan_owns_uncertain_trajectories_without_invented_probability -q`

Expected: FAIL because recipe `035` does not exist.

- [ ] **Step 3: Create the recipe record**

```yaml
id: '035'
slug: scenario-fan
name: Scenario Fan
version: 0.7-candidate
status: candidate
problem: Explain several plausible future trajectories that share one observed state and diverge under declared assumptions.
distinguishes_from: Decision Tree owns rules, Roadmap owns planned work, and Line owns declared observed or forecast series; Scenario Fan owns named uncertain trajectories.
allowed_scenarios: [forecasting, rollout outcomes, risk, economic scenarios]
expression_levels: {A: allowed, B: allowed, C: forbidden}
expression_modes: [analytical]
content_contract:
  exact: true
  visible_copy: [ОДНЕ РІШЕННЯ. ТРИ ТРАЄКТОРІЇ., NOW, NEXT, LATER, BASELINE, GUARDED, AUTONOMOUS, НЕВИЗНАЧЕНІСТЬ]
scenario_contract:
  shared_origin: NOW
  paths: [BASELINE, GUARDED, AUTONOMOUS]
  probabilities: not_provided
prompt: prompts/035-scenario-fan.yaml
specification: recipes/035-scenario-fan.md
record: recipes/035-scenario-fan.yaml
```

Required ingredients and relations must match design section 10.4.

Use this exact machine-readable block:

```yaml
ingredients:
  required:
    - {component: Axis, min: 1, max: 2, default: 1}
    - {component: Trace, min: 3, max: 5, default: 3}
    - {component: Band, min: 1, max: 3, default: 1}
    - {component: Threshold, min: 0, max: 2, default: 0}
    - {component: Label, min: 5, max: 12, default: 8}
    - {component: Signal, min: 1, max: 1, default: 1}
  optional: []
relations:
  allowed:
    - {subject: Trace, type: diverges_to, object: Trace}
    - {subject: Axis, type: orders, object: Trace}
    - {subject: Band, type: bounds, object: Trace}
    - {subject: Trace, type: crosses, object: Threshold, condition: when_declared_condition_is_crossed}
    - {subject: Signal, type: highlights, object: Trace}
  forbidden:
    - {subject: Trace, type: transitions_to, object: Trace}
assembly_order: [declare shared origin, name trajectories, declare time horizon, expose uncertainty, mark one dominant scenario signal]
```

- [ ] **Step 4: Add scenario validation**

Reject a missing shared origin, fewer than two paths, duplicate path names, and any numeric probability when `probabilities` equals `not_provided`.

- [ ] **Step 5: Create Markdown and prompt contracts**

```yaml
candidate_directions:
  v1: shared origin with three directly labeled Traces and one uncertainty Band
  v2: baseline Axis with guarded and autonomous divergence around it
  v3: three scenario corridors with common NOW state and separated LATER outcomes
```

- [ ] **Step 6: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_scenario_fan_owns_uncertain_trajectories_without_invented_probability -q`

Expected: PASS.

- [ ] **Step 7: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/recipes/035-scenario-fan.* extensions/dynamics-expansion-v0.1/prompts/035-scenario-fan.yaml tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: define scenario fan recipe"
```

---

### Task 7: Enforce repeated component evidence across real recipes

**Files:**
- Modify: `tools/validate_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: all four recipe records.
- Produces: `collect_component_usage(root: Path, manifest: dict[str, Any]) -> dict[str, set[str]]` and `validate_component_usage(root: Path, manifest: dict[str, Any]) -> list[str]`.

- [ ] **Step 1: Write the failing evidence test**

Extend the existing validator import with `collect_component_usage`.

```python
def test_lane_and_stock_have_two_independent_recipe_uses() -> None:
    manifest = _load(DYNAMICS / "manifest.yaml")
    usage = collect_component_usage(DYNAMICS, manifest)
    assert usage["Lane"] == {"Interaction Sequence", "Feedback Control"}
    assert usage["Stock"] == {"Feedback Control", "Stock / Flow"}
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_lane_and_stock_have_two_independent_recipe_uses -q`

Expected: FAIL because `collect_component_usage()` does not exist.

- [ ] **Step 3: Implement actual usage collection**

```python
def collect_component_usage(root: Path, manifest: dict[str, Any]) -> dict[str, set[str]]:
    usage = {name: set() for name in EXPECTED_COMPONENTS}
    for entry in manifest["recipes"]:
        recipe = _read_yaml(root / entry["record"])
        ingredients = recipe["ingredients"]["required"] + recipe["ingredients"]["optional"]
        for ingredient in ingredients:
            if ingredient["component"] in usage:
                usage[ingredient["component"]].add(recipe["name"])
    return usage
```

The full validator must add `component candidate needs repeated semantic evidence: <name>` when any usage set has fewer than two recipe names.

```python
def validate_component_usage(root: Path, manifest: dict[str, Any]) -> list[str]:
    usage = collect_component_usage(root, manifest)
    return [
        f"component candidate needs repeated semantic evidence: {name}"
        for name in EXPECTED_COMPONENTS
        if len(usage[name]) < 2
    ]
```

- [ ] **Step 4: Run the test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_lane_and_stock_have_two_independent_recipe_uses -q`

Expected: PASS.

- [ ] **Step 5: Commit if authorized**

```bash
git add tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "test: enforce dynamics component evidence"
```

---

### Task 8: Add deterministic Control Chart evidence

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/analytics/families.yaml`
- Create: `extensions/dynamics-expansion-v0.1/analytics/datasets/01-controlchart.yaml`
- Create: `tools/build_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: family and dataset YAML.
- Produces: `derive_analytical_proof(family: str, contract: dict[str, Any], dataset_document: dict[str, Any], dataset_path: str) -> dict[str, Any]` with `controlchart` support.

- [ ] **Step 1: Write the failing proof test**

Add `from tools.build_dynamics_expansion import derive_analytical_proof` to the test module.

```python
def test_controlchart_proof_preserves_limits_and_anomaly() -> None:
    families = _load(DYNAMICS / "analytics/families.yaml")["families"]
    dataset = _load(DYNAMICS / "analytics/datasets/01-controlchart.yaml")
    proof = derive_analytical_proof(
        "controlchart", families["controlchart"], dataset,
        "analytics/datasets/01-controlchart.yaml",
    )
    assert proof["derived"]["centerline"] == 20
    assert proof["derived"]["lower_control_limit"] == 14
    assert proof["derived"]["upper_control_limit"] == 26
    assert proof["derived"]["special_cause_ids"] == ["w7"]
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_controlchart_proof_preserves_limits_and_anomaly -q`

Expected: FAIL because the family, dataset, and builder do not exist.

- [ ] **Step 3: Define the family contract and fixed dataset**

```yaml
# analytics/families.yaml
language: CSDL
version: 0.3-candidate
kind: analytical-family-contracts
families:
  controlchart:
    intent: Determine whether an ordered process is stable or contains declared special-cause variation.
    compatible_recipes: ['019', '033']
    candidate_components: [Axis, Band, Threshold, Trace, Label, Signal]
    internal_marks: [observation, centerline, control_limit, special_cause_marker]
    encoding_invariants:
      - preserve ordered observations
      - distinguish control limits from targets
      - expose limit derivation method
      - label special-cause rule
      - preserve missing observations as gaps
```

Add these exact `slopegraph` and `dotplot` contracts in the declared order so later tasks only add datasets and derivation branches:

```yaml
  slopegraph:
    intent: Compare the same entities across exactly two declared states on one shared quantitative domain.
    compatible_recipes: ['019']
    candidate_components: [Axis, Trace, Vector, Pulse, Label, Signal]
    internal_marks: [state_axis, endpoint, entity_connector, direct_label]
    encoding_invariants:
      - bind every connector to one entity across both states
      - keep state ordering explicit and stable
      - use one shared quantitative scale
      - label entities and endpoints directly
      - derive signed delta deterministically
      - declare missing endpoints without connecting incomplete pairs
  dotplot:
    intent: Compare categorical values compactly through position on one declared quantitative domain.
    compatible_recipes: ['019']
    candidate_components: [Axis, Pulse, Threshold, Label, Signal]
    internal_marks: [category_axis, quantitative_axis, point, direct_label]
    encoding_invariants:
      - use position as the primary quantitative encoding
      - declare whether zero is included
      - preserve source order or one declared deterministic sort
      - label selected points directly
      - give multiple series a non-color carrier
      - declare the strategy for overlapping points
```

```yaml
# analytics/datasets/01-controlchart.yaml
language: CSDL
version: 0.3-candidate
dataset:
  id: controlchart-review-time-v1
  version: 1.0.0
  status: synthetic_fixed_data
  unit: minutes
  method: source_declared_limits
  centerline: 20
  lower_control_limit: 14
  upper_control_limit: 26
  special_cause_rule: outside_control_limits
  fields:
    - {name: id, type: string}
    - {name: order, type: integer}
    - {name: value, type: number, unit: minutes}
  records:
    - {id: w1, order: 1, value: 18}
    - {id: w2, order: 2, value: 19}
    - {id: w3, order: 3, value: 20}
    - {id: w4, order: 4, value: 21}
    - {id: w5, order: 5, value: 19}
    - {id: w6, order: 6, value: 22}
    - {id: w7, order: 7, value: 31}
    - {id: w8, order: 8, value: 20}
  provenance:
    source: synthetic fixed data for Dynamics Expansion v0.1
    transformation: none
```

- [ ] **Step 4: Implement the Control Chart derivation branch**

```python
if family == "controlchart":
    values = dataset["records"]
    lower = dataset["lower_control_limit"]
    upper = dataset["upper_control_limit"]
    derived = {
        "centerline": dataset["centerline"],
        "lower_control_limit": lower,
        "upper_control_limit": upper,
        "special_cause_ids": [
            record["id"] for record in values
            if record["value"] < lower or record["value"] > upper
        ],
    }
```

Return the shared proof envelope defined by the design: language, version, family, dataset identity/path/status/source, intent, internal marks, candidate components, encoding invariants, fields, records, derived, and deterministic provenance.

- [ ] **Step 5: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_controlchart_proof_preserves_limits_and_anomaly -q`

Expected: PASS.

- [ ] **Step 6: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/analytics/families.yaml extensions/dynamics-expansion-v0.1/analytics/datasets/01-controlchart.yaml tools/build_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: add control chart proof"
```

---

### Task 9: Add deterministic Slopegraph evidence

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/analytics/datasets/02-slopegraph.yaml`
- Modify: `tools/build_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: shared proof envelope from Task 8.
- Produces: `slopegraph` derivation with exact signed deltas; `dumbbell` remains a rendering form.

- [ ] **Step 1: Write the failing test**

```python
def test_slopegraph_proof_pairs_entities_and_derives_delta() -> None:
    families = _load(DYNAMICS / "analytics/families.yaml")["families"]
    dataset = _load(DYNAMICS / "analytics/datasets/02-slopegraph.yaml")
    proof = derive_analytical_proof(
        "slopegraph", families["slopegraph"], dataset,
        "analytics/datasets/02-slopegraph.yaml",
    )
    assert proof["derived"]["pairs"] == [
        ["MODEL A", 72, 84, 12],
        ["MODEL B", 78, 86, 8],
        ["MODEL C", 82, 81, -1],
    ]
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_slopegraph_proof_pairs_entities_and_derives_delta -q`

Expected: FAIL because the dataset and derivation branch do not exist.

- [ ] **Step 3: Create the fixed paired dataset**

```yaml
language: CSDL
version: 0.3-candidate
dataset:
  id: slopegraph-model-quality-v1
  version: 1.0.0
  status: synthetic_fixed_data
  state_a: BASELINE
  state_b: GUARDED
  unit: percent
  domain: [0, 100]
  fields:
    - {name: entity, type: string}
    - {name: state_a_value, type: number, unit: percent}
    - {name: state_b_value, type: number, unit: percent}
  records:
    - {entity: MODEL A, state_a_value: 72, state_b_value: 84}
    - {entity: MODEL B, state_a_value: 78, state_b_value: 86}
    - {entity: MODEL C, state_a_value: 82, state_b_value: 81}
  provenance:
    source: synthetic fixed data for Dynamics Expansion v0.1
    transformation: signed delta equals state B minus state A
```

- [ ] **Step 4: Implement the Slopegraph derivation branch**

```python
elif family == "slopegraph":
    derived = {
        "state_a": dataset["state_a"],
        "state_b": dataset["state_b"],
        "domain": dataset["domain"],
        "pairs": [
            [
                record["entity"],
                record["state_a_value"],
                record["state_b_value"],
                record["state_b_value"] - record["state_a_value"],
            ]
            for record in dataset["records"]
        ],
    }
```

- [ ] **Step 5: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_slopegraph_proof_pairs_entities_and_derives_delta -q`

Expected: PASS.

- [ ] **Step 6: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/analytics/datasets/02-slopegraph.yaml tools/build_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: add slopegraph proof"
```

---

### Task 10: Add deterministic Dot Plot evidence

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/analytics/datasets/03-dotplot.yaml`
- Modify: `tools/build_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`

**Interfaces:**
- Consumes: shared proof envelope from Task 8.
- Produces: `dotplot` derivation with preserved source order and declared domain.

- [ ] **Step 1: Write the failing test**

```python
def test_dotplot_proof_preserves_declared_category_order() -> None:
    families = _load(DYNAMICS / "analytics/families.yaml")["families"]
    dataset = _load(DYNAMICS / "analytics/datasets/03-dotplot.yaml")
    proof = derive_analytical_proof(
        "dotplot", families["dotplot"], dataset,
        "analytics/datasets/03-dotplot.yaml",
    )
    assert proof["derived"]["ordered_values"] == [
        ["SPEC", 88], ["TESTS", 84], ["DOCS", 76], ["MEMORY", 91]
    ]
    assert proof["derived"]["domain"] == [0, 100]
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_dotplot_proof_preserves_declared_category_order -q`

Expected: FAIL because the dataset and derivation branch do not exist.

- [ ] **Step 3: Create the fixed categorical dataset**

```yaml
language: CSDL
version: 0.3-candidate
dataset:
  id: dotplot-capability-score-v1
  version: 1.0.0
  status: synthetic_fixed_data
  unit: percent
  domain: [0, 100]
  order: source
  zero_included: true
  fields:
    - {name: category, type: string}
    - {name: value, type: number, unit: percent}
  records:
    - {category: SPEC, value: 88}
    - {category: TESTS, value: 84}
    - {category: DOCS, value: 76}
    - {category: MEMORY, value: 91}
  provenance:
    source: synthetic fixed data for Dynamics Expansion v0.1
    transformation: none
```

- [ ] **Step 4: Implement the Dot Plot derivation branch**

```python
elif family == "dotplot":
    derived = {
        "domain": dataset["domain"],
        "zero_included": dataset["zero_included"],
        "order": dataset["order"],
        "ordered_values": [
            [record["category"], record["value"]]
            for record in dataset["records"]
        ],
    }
```

- [ ] **Step 5: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_dotplot_proof_preserves_declared_category_order -q`

Expected: PASS.

- [ ] **Step 6: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/analytics/datasets/03-dotplot.yaml tools/build_dynamics_expansion.py tests/test_dynamics_expansion.py
git commit -m "feat: add dot plot proof"
```

---

### Task 11: Build proofs, indexes, compatibility, and negative fixtures

**Files:**
- Modify: `tools/build_dynamics_expansion.py`
- Modify: `tools/validate_dynamics_expansion.py`
- Modify: `tests/test_dynamics_expansion.py`
- Create: `extensions/dynamics-expansion-v0.1/fixtures/negative/expected-errors.yaml`
- Create: `extensions/dynamics-expansion-v0.1/fixtures/negative/01-message-without-receiver.yaml` through `17-superficial-variant.yaml`
- Generate: `extensions/dynamics-expansion-v0.1/analytics/proofs/*.yaml`
- Generate: `extensions/dynamics-expansion-v0.1/generated/index.yaml`
- Generate: `extensions/dynamics-expansion-v0.1/generated/compatibility.yaml`

**Interfaces:**
- Consumes: all normative records and analytical datasets.
- Produces: `derive_index(root: Path) -> dict[str, Any]`, `derive_compatibility(root: Path) -> dict[str, Any]`, `build_dynamics_expansion(root: Path) -> list[Path]`, and `validate_dynamics_expansion(root: Path) -> list[str]`.

- [ ] **Step 1: Write deterministic rebuild and full-validator tests**

Add `import shutil`, extend the builder import with `build_dynamics_expansion`, extend the validator import with `validate_dynamics_expansion`, and create an isolated repository fixture that preserves every baseline path consumed by the validator:

```python
def _copy_dynamics(tmp_path: Path) -> Path:
    target = tmp_path / "extensions/dynamics-expansion-v0.1"
    shutil.copytree(DYNAMICS, target)
    for source, destination in (
        (
            ROOT / "components/component-library-v0.2/manifest.yaml",
            tmp_path / "components/component-library-v0.2/manifest.yaml",
        ),
        (
            ROOT / "recipes/recipe-library-v0.6/manifest.yaml",
            tmp_path / "recipes/recipe-library-v0.6/manifest.yaml",
        ),
        (
            ROOT / "analytics/analytical-mode-v0.2/manifest.yaml",
            tmp_path / "analytics/analytical-mode-v0.2/manifest.yaml",
        ),
        (
            ROOT / "accessibility/night-mode-v0.1/evaluation/raster-hashes.yaml",
            tmp_path / "accessibility/night-mode-v0.1/evaluation/raster-hashes.yaml",
        ),
    ):
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return target
```

```python
def test_dynamics_outputs_rebuild_deterministically(tmp_path: Path) -> None:
    target = _copy_dynamics(tmp_path)
    first = build_dynamics_expansion(target)
    first_bytes = {path.relative_to(target): path.read_bytes() for path in first}
    second = build_dynamics_expansion(target)
    second_bytes = {path.relative_to(target): path.read_bytes() for path in second}
    assert first_bytes == second_bytes
    assert validate_dynamics_expansion(target) == []


def test_generated_index_has_exact_counts() -> None:
    index = _load(DYNAMICS / "generated/index.yaml")
    assert index["recipe_candidate_count"] == 4
    assert index["component_candidate_count"] == 2
    assert index["relation_candidate_count"] == 6
    assert index["analytical_family_candidate_count"] == 3
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_dynamics_outputs_rebuild_deterministically tests/test_dynamics_expansion.py::test_generated_index_has_exact_counts -q`

Expected: FAIL because generated outputs and full functions are incomplete.

- [ ] **Step 3: Implement deterministic builders**

Follow the `build_arsenal_expansion.py` shape. Write three proof files, then `generated/index.yaml`, then `generated/compatibility.yaml`. Use `yaml.safe_dump(..., allow_unicode=True, sort_keys=False)` and return every written path in deterministic order.

`derive_compatibility()` must include, for every recipe, exact ID, name, distinction, components, sorted relations, and expression modes. For every analytical family include compatible recipes and candidate components.

- [ ] **Step 4: Implement the full validator**

`validate_dynamics_expansion()` must combine:

```python
errors = []
errors.extend(validate_identity(manifest))
errors.extend(validate_baseline(repository, manifest))
vocabulary_errors, components, relations = validate_candidate_vocabulary(root, manifest)
errors.extend(vocabulary_errors)
component_baseline = _load(
    repository / manifest["baseline"]["component_library"],
    errors,
    "baseline component library",
)
allowed_components = set(component_baseline.get("vocabulary", {}).get("components", [])) | set(components)
allowed_relations = set(component_baseline.get("vocabulary", {}).get("relations", [])) | set(relations)
for entry in manifest["recipes"]:
    errors.extend(validate_recipe_record(root, entry, allowed_components, allowed_relations))
errors.extend(validate_component_usage(root, manifest))
errors.extend(validate_analytical_contracts(root, manifest))
errors.extend(validate_protected_inventory(repository, manifest))
errors.extend(validate_generated_outputs(root))
return errors
```

CLI success text must be `dynamics expansion valid`.

- [ ] **Step 5: Add the exact negative-fixture matrix**

Create one YAML mutation per design section 18.3 with these filenames and exact expected messages:

```yaml
01-message-without-receiver.yaml: Interaction Sequence message must declare sender and receiver
02-lane-without-owner.yaml: Lane must declare exactly one owner
03-correction-without-deviation.yaml: Feedback Control correction requires measured deviation
04-stock-without-unit.yaml: Stock must declare a unit
05-unreconciled-stock.yaml: Stock / Flow values must reconcile start + inflow - outflow = end
06-reversed-outflow.yaml: Stock outflow must use flows_out_of
07-scenario-without-origin.yaml: Scenario Fan paths must share one origin
08-invented-probability.yaml: Scenario Fan must not invent probability
09-control-limit-as-target.yaml: Control Chart must distinguish control limits from targets
10-reordered-pair.yaml: Slopegraph entity order must remain declared
11-mismatched-scales.yaml: Slopegraph pairs must share one quantitative domain
12-silent-dot-sort.yaml: Dot Plot category order must remain declared
13-baseline-dsl-candidate-term.yaml: candidate vocabulary must not mutate baseline Prompt DSL
14-level-c-dynamics.yaml: Dynamics recipes must forbid Level C
15-raster-hash-mutation.yaml: protected raster inventory must remain byte-identical
16-duplicate-candidate-hash.yaml: dynamics candidates must have 12 unique SHA-256 values
17-superficial-variant.yaml: candidate directions must declare distinct mechanisms and compositions
```

`expected-errors.yaml` maps each fixture path to exactly one message. The validator test must assert that the intended message appears and that unrelated errors do not replace it.

- [ ] **Step 6: Build outputs twice and run tests**

Run:

```bash
.venv/bin/python tools/build_dynamics_expansion.py extensions/dynamics-expansion-v0.1
.venv/bin/python tools/build_dynamics_expansion.py extensions/dynamics-expansion-v0.1
.venv/bin/python -m pytest tests/test_dynamics_expansion.py -q
.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1
```

Expected: focused tests pass; final command prints `dynamics expansion valid`.

- [ ] **Step 7: Commit if authorized**

```bash
git add tools/build_dynamics_expansion.py tools/validate_dynamics_expansion.py tests/test_dynamics_expansion.py extensions/dynamics-expansion-v0.1/analytics/proofs extensions/dynamics-expansion-v0.1/generated extensions/dynamics-expansion-v0.1/fixtures
git commit -m "feat: validate dynamics expansion proofs"
```

---

### Task 12: Build visual review tooling and candidate validation

**Files:**
- Create: `tools/build_dynamics_review.py`
- Modify: `tests/test_dynamics_expansion.py`
- Create: `extensions/dynamics-expansion-v0.1/selection/README.md`
- Create: `extensions/dynamics-expansion-v0.1/evaluation/rubric.yaml`
- Create: `extensions/dynamics-expansion-v0.1/evaluation/review.md`
- Create: `extensions/dynamics-expansion-v0.1/evaluation/scores.csv`

**Interfaces:**
- Consumes: recipe manifest and `drafts/light/16x9/<id>-<slug>/v1.png` through `v3.png`.
- Produces: `candidate_paths(root: Path, recipe: dict[str, Any]) -> list[Path]`, `validate_recipe_candidates(root: Path, recipe_id: str) -> list[str]`, `validate_dynamics_candidates(root: Path, require_selection: bool = False) -> list[str]`, `build_recipe_board(root: Path, recipe: dict[str, Any], output: Path) -> Path`, and `build_dynamics_review(root: Path) -> list[Path]`.

- [ ] **Step 1: Write failing synthetic-raster tests**

Extend the test imports before adding the fixture:

```python
from PIL import Image

from tools.build_dynamics_review import (
    build_dynamics_review,
    validate_dynamics_candidates,
    validate_recipe_candidates,
)
```

```python
def _write_rgb_png(path: Path, color: tuple[int, int, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    Image.new("RGB", (1920, 1080), color).save(path, format="PNG")


def test_candidate_validator_requires_twelve_unique_pngs(tmp_path: Path) -> None:
    target = _copy_dynamics(tmp_path)
    for recipe_index, entry in enumerate(_load(target / "manifest.yaml")["recipes"]):
        recipe = _load(target / entry["record"])
        for variant in range(1, 4):
            path = target / "drafts/light/16x9" / f'{recipe["id"]}-{recipe["slug"]}' / f"v{variant}.png"
            _write_rgb_png(path, (recipe_index * 40 + variant, variant * 30, 10))
    assert validate_dynamics_candidates(target) == []
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_candidate_validator_requires_twelve_unique_pngs -q`

Expected: FAIL because visual review tooling does not exist.

- [ ] **Step 3: Implement candidate validation**

Require exactly 12 readable PNGs, each `1920x1080`, each RGB or RGBA, with 12 unique SHA-256 digests. Add per-recipe validation so raster tasks can validate one three-candidate group before the full package exists.

- [ ] **Step 4: Implement board and overview builders**

- Recipe board: `1920x480`, three `620x349` previews, title, and `v1/v2/v3` labels.
- Board paths: `selection/boards/<id>-<slug>.png`.
- Overview: `3840x1080`, two boards per row, two rows.
- Hash inventory: extension ID, status `unpromoted`, file count, unique count, relative path, hash, dimensions, and mode.
- CLI validation success text: `dynamics candidates valid`.

- [ ] **Step 5: Write the selection and rubric contracts**

`selection/README.md` must require:

```text
032:v_, 033:v_, 034:v_, 035:v_
```

`rubric.yaml` must preserve Clarity, Presentation readability, Memorability, CSDL identity, Restraint, Text fidelity, and Semantic integrity. `scores.csv` starts with headers only. `review.md` records the package state as unpromoted and lists the required evidence fields for each variant.

- [ ] **Step 6: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_candidate_validator_requires_twelve_unique_pngs -q`

Expected: PASS.

- [ ] **Step 7: Commit if authorized**

```bash
git add tools/build_dynamics_review.py tests/test_dynamics_expansion.py extensions/dynamics-expansion-v0.1/selection/README.md extensions/dynamics-expansion-v0.1/evaluation
git commit -m "feat: add dynamics visual review tooling"
```

---

### Task 13: Generate and review Interaction Sequence candidates

**Files:**
- Create local ignored: `extensions/dynamics-expansion-v0.1/drafts/light/16x9/032-interaction-sequence/v1.png`
- Create local ignored: `extensions/dynamics-expansion-v0.1/drafts/light/16x9/032-interaction-sequence/v2.png`
- Create local ignored: `extensions/dynamics-expansion-v0.1/drafts/light/16x9/032-interaction-sequence/v3.png`
- Generate: `extensions/dynamics-expansion-v0.1/selection/boards/032-interaction-sequence.png`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/review.md`

**Interfaces:**
- Consumes: exact prompt `032`, four canonical references, and `validate_recipe_candidates(root, "032")`.
- Produces: three unique unpromoted candidates and one comparison board.

- [ ] **Step 1: Validate the package and exact prompt before generation**

Run:

```bash
.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1
```

Expected: `dynamics expansion valid`.

- [ ] **Step 2: Generate three independent candidates with built-in Codex image generation**

Attach all four canonical references and state their authority roles. Use the same exact prompt three times, once for each declared direction. Do not ask the model to vary a previous result. Save each source under the exact `v1.png`, `v2.png`, and `v3.png` paths.

- [ ] **Step 3: Normalize only when necessary**

If the generator returns a near-16:9 source size, resize mechanically to `1920x1080` without crop, redraw, recolor, or text edit. Record source dimensions, mode, and hash in `evaluation/review.md`.

- [ ] **Step 4: Validate the three files**

Run:

```bash
.venv/bin/python -c 'from pathlib import Path; from tools.build_dynamics_review import validate_recipe_candidates; errors = validate_recipe_candidates(Path("extensions/dynamics-expansion-v0.1"), "032"); print("\n".join(errors)); raise SystemExit(bool(errors))'
```

Expected: exit zero with no output.

- [ ] **Step 5: Review exact copy and material divergence**

Review all candidates at `1920x1080` and `1280x720`. Record every visible string, the actor-time mechanism, wait/retry visibility, one dominant Signal, prohibited-element scan, and why each composition is materially distinct. Regenerate only a failing variant and preserve rejected-pass evidence.

- [ ] **Step 6: Build the board**

Run the board function for recipe `032` and verify the board shows three independent candidates with readable labels.

- [ ] **Step 7: Commit if authorized**

Commit only persistent review evidence allowed by the repository policy. Do not commit ignored drafts.

Suggested message: `feat: add interaction sequence candidates`.

---

### Task 14: Generate and review Feedback Control candidates

**Files:**
- Create local ignored: `extensions/dynamics-expansion-v0.1/drafts/light/16x9/033-feedback-control/v1.png` through `v3.png`
- Generate: `extensions/dynamics-expansion-v0.1/selection/boards/033-feedback-control.png`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/review.md`

**Interfaces:**
- Consumes: prompt `033` and visual tooling from Task 12.
- Produces: three candidates that visibly distinguish target, measurement, deviation, correction, controller Lane, system Lane, and one Stock.

- [ ] **Step 1: Run pre-generation validation**

Run: `.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1`

Expected: `dynamics expansion valid`.

- [ ] **Step 2: Generate v1, v2, and v3 independently**

Use the three exact direction descriptions from `prompts/033-feedback-control.yaml` and all canonical references.

- [ ] **Step 3: Normalize and validate**

Normalize only by mechanical resize when required. Run `validate_recipe_candidates(..., "033")` and require exit zero.

- [ ] **Step 4: Review semantics and copy**

Reject any variant that reads as a generic Loop, lacks a measured deviation, treats a target as a control limit, omits controller/system ownership, introduces more than one dominant Signal, or mutates visible copy.

- [ ] **Step 5: Build and inspect the board**

Generate `selection/boards/033-feedback-control.png`; inspect full board and each source candidate.

- [ ] **Step 6: Commit if authorized**

Commit only persistent review evidence. Suggested message: `feat: add feedback control candidates`.

---

### Task 15: Generate and review Stock / Flow candidates

**Files:**
- Create local ignored: `extensions/dynamics-expansion-v0.1/drafts/light/16x9/034-stock-flow/v1.png` through `v3.png`
- Generate: `extensions/dynamics-expansion-v0.1/selection/boards/034-stock-flow.png`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/review.md`

**Interfaces:**
- Consumes: prompt `034`, equation `24 + 12 - 8 = 28`, and visual tooling.
- Produces: three exact-copy candidates with explicit inflow, Stock, outflow, unit, and reconciliation.

- [ ] **Step 1: Run pre-generation validation**

Run: `.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1`

Expected: `dynamics expansion valid`.

- [ ] **Step 2: Generate v1, v2, and v3 independently**

Use the exact candidate directions and require every number and sign to appear exactly.

- [ ] **Step 3: Normalize and validate**

Normalize only by mechanical resize when required. Run `validate_recipe_candidates(..., "034")` and require exit zero.

- [ ] **Step 4: Review quantitative fidelity**

Reject any variant with missing unit, reversed flow direction, unsigned outflow, changed value, unreconciled equation, Sankey-like distribution, Pipeline-like stages, decorative container, or extra copy.

- [ ] **Step 5: Build and inspect the board**

Generate `selection/boards/034-stock-flow.png`; inspect the full board and each candidate at full size.

- [ ] **Step 6: Commit if authorized**

Commit only persistent review evidence. Suggested message: `feat: add stock flow candidates`.

---

### Task 16: Generate and review Scenario Fan candidates

**Files:**
- Create local ignored: `extensions/dynamics-expansion-v0.1/drafts/light/16x9/035-scenario-fan/v1.png` through `v3.png`
- Generate: `extensions/dynamics-expansion-v0.1/selection/boards/035-scenario-fan.png`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/review.md`

**Interfaces:**
- Consumes: prompt `035` and scenario contract with no probabilities.
- Produces: three candidates with one shared origin, three named paths, and explicit uncertainty.

- [ ] **Step 1: Run pre-generation validation**

Run: `.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1`

Expected: `dynamics expansion valid`.

- [ ] **Step 2: Generate v1, v2, and v3 independently**

Use the exact directions and prohibit invented percentages, probabilities, confidence levels, or forecasts.

- [ ] **Step 3: Normalize and validate**

Normalize only by mechanical resize when required. Run `validate_recipe_candidates(..., "035")` and require exit zero.

- [ ] **Step 4: Review scenario semantics**

Reject any variant that reads as a Decision Tree or Roadmap, lacks a shared NOW origin, hides scenario identity, invents probability, uses color as the only path carrier, or mutates copy.

- [ ] **Step 5: Build and inspect the board**

Generate `selection/boards/035-scenario-fan.png`; inspect full board and source candidates.

- [ ] **Step 6: Commit if authorized**

Commit only persistent review evidence. Suggested message: `feat: add scenario fan candidates`.

---

### Task 17: Complete the unpromoted candidate package and stop at selection

**Files:**
- Generate: `extensions/dynamics-expansion-v0.1/selection/overview.png`
- Generate: `extensions/dynamics-expansion-v0.1/selection/candidate-hashes.yaml`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/review.md`
- Modify: `DECISIONS.md`
- Modify: `STATUS.md`
- Modify: `CHANGELOG.md`
- Modify: `specs/2026-07-17-csdl-v0.1-design.md`

**Interfaces:**
- Consumes: 12 valid candidates and four valid boards.
- Produces: D-036 candidate-package decision, complete unpromoted overview, exact hash inventory, and user selection syntax.

- [ ] **Step 1: Build the complete review package**

Run:

```bash
.venv/bin/python tools/build_dynamics_review.py extensions/dynamics-expansion-v0.1
.venv/bin/python tools/build_dynamics_review.py extensions/dynamics-expansion-v0.1 --validate
```

Expected: the first command lists four boards, overview, and hash inventory; the second prints `dynamics candidates valid`.

- [ ] **Step 2: Inspect the overview and candidate inventory**

Verify `file_count: 12`, `unique_sha256_count: 12`, exact `1920x1080` dimensions, RGB/RGBA modes, and a visibly distinct mechanism for every variant.

- [ ] **Step 3: Complete review evidence**

For every recipe, record:

- three active filenames;
- rejected-pass filenames when regeneration occurred;
- exact-copy result;
- dimensions and mode;
- mechanism summary;
- divergence summary;
- prohibited-element result;
- remaining risk;
- status `unpromoted`.

- [ ] **Step 4: Record D-036 and status without claiming promotion**

Add a D-036 decision that establishes Dynamics Expansion v0.1 as an additive, evidence-gated candidate package with 4 recipes, 2 components, 6 relations, 3 analytical families, 12 unpromoted candidates, no animation, and no baseline mutation. Update STATUS, CHANGELOG, and the Foundation implementation-status appendix consistently.

- [ ] **Step 5: Run the full regression suite**

Run:

```bash
.venv/bin/python -m pytest -q
.venv/bin/python tools/validate_dynamics_expansion.py extensions/dynamics-expansion-v0.1
.venv/bin/python tools/build_dynamics_review.py extensions/dynamics-expansion-v0.1 --validate
.venv/bin/python tools/validate_component_library.py components/component-library-v0.2/manifest.yaml
.venv/bin/python tools/validate_recipe_library.py recipes/recipe-library-v0.6/manifest.yaml
.venv/bin/python tools/validate_analytical_mode.py analytics/analytical-mode-v0.2
.venv/bin/python tools/validate_accessibility_mode.py accessibility/night-mode-v0.1
.venv/bin/python tools/validate_design_book.py cookbook/design-book-v1.0
git diff --check
```

Expected: every command exits zero; Dynamics commands print their exact success messages; all protected raster hashes remain unchanged.

- [ ] **Step 6: Stop and request user selection**

Present `selection/overview.png` and the four full-size boards. Request exactly:

```text
032:v_, 033:v_, 034:v_, 035:v_
```

Do not score, copy to `selection/selected/`, or promote vocabulary before this response.

- [ ] **Step 7: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/selection extensions/dynamics-expansion-v0.1/evaluation/review.md DECISIONS.md STATUS.md CHANGELOG.md specs/2026-07-17-csdl-v0.1-design.md
git commit -m "feat: add dynamics expansion candidates"
```

---

### Task 18: Persist user selection and accepted rubric evidence

**Files:**
- Create: `extensions/dynamics-expansion-v0.1/selection/selected/032-interaction-sequence.png`
- Create: `extensions/dynamics-expansion-v0.1/selection/selected/033-feedback-control.png`
- Create: `extensions/dynamics-expansion-v0.1/selection/selected/034-stock-flow.png`
- Create: `extensions/dynamics-expansion-v0.1/selection/selected/035-scenario-fan.png`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/review.md`
- Modify: `extensions/dynamics-expansion-v0.1/evaluation/scores.csv`
- Modify: `extensions/dynamics-expansion-v0.1/selection/candidate-hashes.yaml`
- Modify: `tools/build_dynamics_review.py`
- Modify: `tests/test_dynamics_expansion.py`
- Modify: `STATUS.md`
- Modify: `CHANGELOG.md`

**Interfaces:**
- Consumes: explicit user choices for all four IDs.
- Produces: four package-local selected rasters, accepted rubric rows, and `validate_dynamics_candidates(root, require_selection=True) -> []`.

- [ ] **Step 1: Write the failing selection-completeness test**

```python
def test_selected_dynamics_candidates_are_complete_and_identical_to_sources() -> None:
    assert validate_dynamics_candidates(DYNAMICS, require_selection=True) == []
    selection = _load(DYNAMICS / "selection/candidate-hashes.yaml")
    assert selection["status"] == "selected_unpromoted"
    assert len(selection["selected"]) == 4
    for entry in selection["selected"]:
        assert (DYNAMICS / entry["source"]).read_bytes() == (DYNAMICS / entry["selected_path"]).read_bytes()
```

- [ ] **Step 2: Run and confirm failure**

Run: `.venv/bin/python -m pytest tests/test_dynamics_expansion.py::test_selected_dynamics_candidates_are_complete_and_identical_to_sources -q`

Expected: FAIL because selected files and metadata do not exist.

- [ ] **Step 3: Copy exactly the user-selected bytes**

For each chosen variant, copy the source bytes without resize, edit, recolor, metadata rewrite, or re-encoding. Record source path, selected path, source SHA-256, and selected SHA-256.

- [ ] **Step 4: Score accepted candidates**

Add one row per selected recipe. Require:

- Clarity = 5;
- Presentation readability = 5;
- Text fidelity = 5;
- every other criterion at least 4;
- average at least 4.4.

If any threshold fails, return to the affected raster task and regenerate three variants for that recipe. Do not lower thresholds.

- [ ] **Step 5: Extend selection validation**

When `require_selection=True`, require exactly four selected paths, byte identity with the chosen sources, four score rows, exact-copy evidence, accepted thresholds, and status `selected_unpromoted`.

- [ ] **Step 6: Run final package and regression validation**

Run the complete Task 17 command set plus:

```bash
.venv/bin/python -c 'from pathlib import Path; from tools.build_dynamics_review import validate_dynamics_candidates; errors = validate_dynamics_candidates(Path("extensions/dynamics-expansion-v0.1"), require_selection=True); print("\n".join(errors)); raise SystemExit(bool(errors))'
```

Expected: all commands exit zero.

- [ ] **Step 7: Update status without public promotion**

State that four recipe candidates are selected inside the incubation package, while Component Library, Recipe Library, Analytical Mode, Prompt DSL, and accepted baseline rasters remain unchanged. Public promotion requires a separate approved objective and plan.

- [ ] **Step 8: Commit if authorized**

```bash
git add extensions/dynamics-expansion-v0.1/selection extensions/dynamics-expansion-v0.1/evaluation tools/build_dynamics_review.py tests/test_dynamics_expansion.py STATUS.md CHANGELOG.md
git commit -m "feat: select dynamics expansion evidence"
```

## Plan Completion Boundary

This plan ends with a validated, selected, but still unpromoted Dynamics Expansion v0.1 package. It does not create Component Library v0.3, Recipe Library v0.7, Analytical Mode v0.3, or a new public Prompt DSL version. Public promotion requires a separate design review and implementation plan after the selected visual and analytical evidence is accepted.
