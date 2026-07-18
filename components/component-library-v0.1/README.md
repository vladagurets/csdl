# CSDL Component Library v0.1

Milestone 3 formalizes fifteen reusable CSDL components from accepted Foundation, Pilot 01, and Visual DNA Sprint 1 evidence. Markdown specifications are canonical; `manifest.yaml` exposes the same contracts to validators and later composition tooling.

## Component contract state

All fifteen component records and canonical Markdown specifications are complete. The editorial, structural, and analytical proofs validate using component vocabulary alone, including the fixed Chart quantitative contract. Strict library, proof, and index validation passes, and deterministic `index.yaml` plus `compatibility.yaml` outputs are checked in. Incomplete mode remains available only for historical intermediate-packet review.

## Evidence convention

Every component rule and do/don't example points to an existing repository path and a precise locator such as a Markdown heading, YAML key, family review heading, or named region of a D-028 primary-authority board. Evidence levels mean:

- `strong`: multiple canonical contracts or accepted raster/review records agree;
- `bounded`: accepted evidence is narrow and the component contract must stay within it;
- `constrained`: positive family evidence is absent or limited, so the contract records a strict exception without claiming a canonical raster use.

No new raster is generated for this library. Existing Milestone 2 assets remain the visual evidence.

## Validation

Earlier infrastructure and intermediate packets use programmatic incomplete mode from tests:

```python
validate_component_library(path, require_complete=False)
validate_component_proofs(root, require_complete=False)
validate_component_index(root, require_complete=False)
```

Milestone completion uses strict CLI gates:

```bash
.venv/bin/python tools/validate_component_library.py components/component-library-v0.1/manifest.yaml
.venv/bin/python tools/validate_component_proofs.py components/component-library-v0.1
.venv/bin/python tools/build_component_library.py components/component-library-v0.1
.venv/bin/python tools/validate_component_index.py components/component-library-v0.1
```

`build_component_library.py` writes only deterministic YAML index and compatibility outputs. It does not create or mutate raster evidence.
