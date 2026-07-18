# CSDL Visual DNA Sprint 1

This catalog formalizes the first 20 CSDL pattern families on the canonical `1920×1080` landscape canvas.

Hero, Comparison, and Loop resolve to approved Pilot 01 evidence. The remaining 17 families receive one new canonical example each, selected from three built-in GPT Image 2 candidates using the approved Pilot 01 style anchor.

The catalog is not a fixed template library. `manifest.yaml` provides machine-readable contracts, `specs/` explains semantics, `prompts/` contains generation packages, and `evaluation/` records evidence. KPI, Table, Chart, and Dashboard are bounded Visual DNA prototypes over fixed demo data; full Analytical Mode remains deferred to Milestone 5.

## Validation

```bash
.venv/bin/python -m pytest -q
.venv/bin/python tools/validate_pattern_catalog.py patterns/visual-dna-sprint-01/manifest.yaml
.venv/bin/python tools/validate_pattern_data.py patterns/visual-dna-sprint-01/data/agent-reliability-demo.yaml
.venv/bin/python tools/validate_pattern_assets.py patterns/visual-dna-sprint-01
.venv/bin/python tools/validate_pattern_scores.py patterns/visual-dna-sprint-01/evaluation/scores.csv
```

Asset and score validation are milestone-level completion gates. During infrastructure and family-by-family branches, use their programmatic `require_complete=False` mode through tests; command-line validation remains strict.
