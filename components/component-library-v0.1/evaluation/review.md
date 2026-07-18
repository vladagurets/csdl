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
