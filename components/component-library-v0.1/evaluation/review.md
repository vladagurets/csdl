# Component Library v0.1 Review

## Review protocol

Each component packet records complete specification paths, machine-readable records, evidence strength, relation and expression checks, family compatibility, targeted tests, Milestone 2 regressions, and remaining risk. A record is accepted only when incomplete-mode validation sees the whole record and its Markdown specification; partial records are never accepted.

## Infrastructure packet

- Branch: `codex/m3-component-infrastructure`
- Manifest state: zero accepted component records; exact fifteen-name vocabulary declared
- Schema: complete component, relation, expression, evidence, proof, and path contract
- Markdown: canonical component template and evidence convention
- Tooling: library, proof, builder, and index validators with strict and incomplete modes
- Raster generation: none
- Canonical raster mutation: none

### TDD evidence

Initial focused run failed during collection with four expected `ModuleNotFoundError` results for the not-yet-created library, proof, builder, and index modules.

After implementation:

```text
.venv/bin/python -m pytest -q \
  tests/test_validate_component_library.py \
  tests/test_validate_component_proofs.py \
  tests/test_build_component_library.py \
  tests/test_validate_component_index.py
13 passed

programmatic incomplete-mode library/proof validation
component infrastructure partial contracts valid
```

Strict-mode stop signals are intentional at this packet boundary:

- library validator: exact fifteen records missing and all active `Container` alias locations reported;
- proof validator: editorial, structural, and analytical proofs missing;
- builder: `component library is incomplete`.

### Regression validation

```text
.venv/bin/python -m pytest -q
62 passed

Pilot manifest/style-anchor/assets/scores validators
pass

Milestone 2 catalog/data/assets/scores/review/index validators
pass

git diff --check
pass
```

Remaining risk: relation permission is structurally validated, but proof-level relation compatibility cannot receive positive real-library coverage until component records exist. The component packets add that coverage before strict proof validation can pass.

## Foundation component packet

- Branch: `codex/m3-components-foundation`
- Accepted records: `01 Anchor`, `02 Signal`, `03 Field`, `04 Frame`, `14 Label`
- Canonical specs: `specs/01-anchor.md`, `02-signal.md`, `03-field.md`, `04-frame.md`, `14-label.md`
- Evidence levels: Anchor strong, Signal strong, Field strong, Frame bounded, Label strong
- Raster generation: none
- Canonical raster mutation: none

### Vocabulary decision and migration

D-029 records the user-approved fifteen-name public vocabulary. The earlier Container alias is retired without visual change:

- Hierarchy: nested ownership scope is `Frame`;
- Architecture: system context is `Field`; actors remain `Node`s;
- Pipeline: stages are `Node`s on one `Vector`; no wrapper is present in the accepted evidence.

The Foundation component table, three Milestone 2 family component arrays, three Prompt DSL arrays, and three canonical family specs now agree. The component validator's active-vocabulary gate reports no undeclared name.

### TDD and validation evidence

The packet began with two expected failing assertions: the five component slugs were absent and the active-vocabulary gate had no accepted records to exercise.

```text
focused component infrastructure tests
15 passed

programmatic incomplete-mode library validation
component foundation packet valid

strict library validation
expected stop: exactly 15 components and canonical full order are not complete

.venv/bin/python -m pytest -q
64 passed

Pilot manifest/style-anchor/assets/scores validators
pass

Milestone 2 catalog/data/assets/scores/review/index validators
pass

git diff --check
pass
```

Remaining risk: Frame's Hierarchy compatibility is a lossless vocabulary mapping from accepted open-bracket evidence rather than a new raster. The strict proof gate will independently exercise Frame relations in a later packet; no current raster semantics changed.

## Structural unit component packet

- Branch: `codex/m3-components-units`
- Accepted records: `05 Cluster`, `07 Divider`, `08 Node`, `12 Axis`
- Canonical specs: `specs/05-cluster.md`, `07-divider.md`, `08-node.md`, `12-axis.md`
- Evidence levels: all strong
- Raster generation: none
- Canonical raster mutation: none

### Owning distinctions

- Cluster owns non-sequential grouping through proximity, alignment, and repetition.
- Divider owns one subordinate distinction between two peer scopes and cannot establish order or direction.
- Node owns one discrete stage, actor, option, concept, gate, or data point; repeated Nodes remain comparable.
- Axis owns open sequence, coordinate, lookup, support, or quantitative reference structure; every mode declares direction, and quantitative mode requires a domain.

These contracts preserve the accepted differences between Framework, Comparison, Timeline, Matrix, Table, and Chart rather than collapsing them into generic rows or boxes.

### TDD and validation evidence

The packet began with the expected failure that the canonical nine-record subsequence still contained only the five foundation records.

```text
focused component infrastructure tests
16 passed

programmatic incomplete-mode library validation
component units packet valid

.venv/bin/python -m pytest -q
65 passed

Pilot manifest/style-anchor/assets/scores validators
pass

Milestone 2 catalog/data/assets/scores/review/index validators
pass

git diff --check
pass
```

Remaining risk: Axis intentionally unifies five evidenced modes. Mode-specific proof validation currently enforces the fixed quantitative contract only for analytical proofs; the structural and analytical proof packet will exercise both open topology and honest scale before milestone completion.

## Relation component packet

- Branch: `codex/m3-components-relations`
- Accepted records: `06 Vector`, `09 Loop`, `10 Collision`, `11 Bridge`
- Canonical specs: `specs/06-vector.md`, `09-loop.md`, `10-collision.md`, `11-bridge.md`
- Evidence levels: all strong
- Raster generation: none
- Canonical raster mutation: none

### Owning distinctions

- Vector owns a source-to-target action, state change, or continuous transformation carrier.
- Loop owns one closed recurrence over three to five ordered Nodes.
- Collision owns exactly two inputs producing one named intrinsic overlap/result.
- Bridge owns topology, ownership, or explicit branching between two endpoints, not continuous progress.

The contracts explicitly reject substitution across Vector/Axis, Vector/Bridge, Loop/Axis, Collision/Cluster, and Bridge/Workflow semantics.

### TDD and validation evidence

The packet began with the expected failure that the canonical thirteen-record sequence still contained only nine accepted records.

```text
focused component infrastructure tests
17 passed

programmatic incomplete-mode library validation
component relations packet valid

.venv/bin/python -m pytest -q
66 passed

Pilot manifest/style-anchor/assets/scores validators
pass

Milestone 2 catalog/data/assets/scores/review/index validators
pass

git diff --check
pass
```

Remaining risk: real proof instances do not yet exercise relation-direction permission across two component records. The composition-proof packet must demonstrate at least one allowed Field/Node/Bridge topology and reject one incompatible relation before the primary signal can pass.

## Analytical and annotation component packet

- Branch: `codex/m3-components-analytical`
- Accepted records: `13 Pulse`, `15 Legend`
- Canonical specs: `specs/13-pulse.md`, `15-legend.md`
- Evidence levels: Pulse strong, Legend constrained
- Raster generation: none
- Canonical raster mutation: none

### Evidence boundary

Pulse is directly supported by accepted Big Number, KPI, and Dashboard evidence. Its contract permits one exact value, preserves label/unit/period/source context, and rejects invented targets, deltas, trends, gauges, and peer metrics.

Legend is intentionally constrained rather than promoted from vocabulary to unsupported canonical use. Foundation Analytical Mode prefers direct Labels, and the accepted single-series Chart explicitly contains no Legend. Legend is therefore conditional only for Level A Chart or Dashboard compositions with two to four analytical categories, text-and-form keys, and a recorded reason direct Labels collide or remain ambiguous. The Foundation primary-authority palette strip supports construction calibration only; it is not claimed as family-use evidence.

### TDD and validation evidence

The packet began with the expected strict-order failure: Pulse and Legend were absent from the thirteen-record manifest. After both contracts were added, the new strict test passed. The wider focused run then exposed and corrected two obsolete test fixtures: one still expected strict mode to fail at thirteen records, and one omitted the primary-authority PNG from a temporary evidence tree.

```text
focused component infrastructure tests
18 passed

.venv/bin/python tools/validate_component_library.py components/component-library-v0.1/manifest.yaml
component library valid

.venv/bin/python -m pytest -q
67 passed

Pilot manifest/style-anchor/assets/scores validators
pass

Milestone 2 catalog/data/assets/scores/review/index validators
pass

git diff --check
pass
```

Remaining risk: the strict component-record gate is complete, but the composition-proof gate remains red until editorial, structural, and analytical proof documents exercise real instances and relations. No accepted raster currently demonstrates Legend use, so its compatibility remains conditional by design.

## Composition proof and index packet

- Branch: `codex/m3-composition-proofs`
- Proofs: `proofs/01-editorial.yaml`, `02-structural.yaml`, `03-analytical.yaml`
- Generated outputs: `index.yaml`, `compatibility.yaml`
- Compatibility coverage: 15 components × 20 families; every family has at least one declared component
- Raster generation: none
- Canonical raster mutation: none

### Proof review

- Editorial / Big Number: Anchor owns the proposition, Pulse owns exact `3`, direct Label retains `QUIET · CONSTRUCTIVE · SIGNAL`, and one Signal highlights the value.
- Structural / Architecture: one open Field contains AGENT, TOOLS, and MEMORY Nodes; USER stays outside; three Bridges encode the exact directed/bidirectional topology without layout primitives.
- Analytical / Chart: two Axes order four directly labeled Nodes at exact W1–W4 values `[72, 78, 84, 90]` on `[0, 100]`; one Signal highlights W4; `DEMO DATA` remains attached; Legend is absent.

Each proof points to its accepted Milestone 2 raster, declares semantic content separately from instances, and uses only public component and relation vocabulary. The proof validator rejects an injected ad hoc `layout` key, a relation forbidden by the two component contracts, and an altered W4 quantitative value.

### TDD and validation evidence

The first focused run produced the expected six failures: the three proofs and two generated outputs did not exist, strict proof/index validation remained red, and mutation fixtures had no analytical proof to edit. After the proofs and deterministic outputs were added:

```text
focused proof, builder, and index tests
10 passed

.venv/bin/python tools/validate_component_proofs.py components/component-library-v0.1
component proofs valid

.venv/bin/python tools/build_component_library.py components/component-library-v0.1
component library built: index.yaml, compatibility.yaml

.venv/bin/python tools/validate_component_index.py components/component-library-v0.1
component index valid

.venv/bin/python -m pytest -q
71 passed

Pilot manifest/style-anchor/assets/scores validators
pass

Milestone 2 catalog/data/assets/scores/review/build/index validators
pass

git diff --check
pass
```

Remaining risk: Legend remains a deliberately uninstantiated conditional exception because no accepted raster supports positive use. The proof and generated-output gates are met; final documentation consistency, clean-tree reproducibility, GitHub CI, and integration remain for the release packet.
