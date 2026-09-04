# Codex Image Generation Workflow — 16:9 Canonical

Pilot 01 uses built-in `$imagegen` with GPT Image 2. It does not require `OPENAI_API_KEY`.

## Output contract

- canonical format: PNG, `1920×1080`, RGB or RGBA;
- composition: created directly for landscape 16:9;
- no portrait master, crop-derived adaptation, or mobile preview;
- exact visible copy from `manifest.yaml` only;
- smooth Ukrainian-capable Inter display/body relationship;
- no gradients, shadows, 3D, glossy surfaces, decorative coordinates, random dot fields, UI chrome, logos, or footers.

## Shared reference

Use `pilots/01-agentic-discipline/references/style-anchor-light.png` only after its new 16:9 candidate selection and provenance are complete. The old portrait anchor is superseded and must not be restored from Git history.

## Per-asset procedure

1. Read the matching manifest entry and Prompt DSL file.
2. Run tests and manifest validation; for Cards 01–07 also validate the selected shared anchor.
3. Define `v1`, `v2`, and `v3` direction briefs before generation. Preserve the same approved topic, exact copy/data, evidence, expression level, canvas, references, and exclusions, but make every pair different in concept, dominant visual mechanism, and composition topology.
4. Invoke built-in `$imagegen` once per direction with its direction-specific prompt and the same reference package. Do not repeat one prompt three times.
5. Save candidates under `pilots/01-agentic-discipline/drafts/light/16x9/<asset>/`.
6. Review all three side by side for candidate divergence, exact text, landscape hierarchy, semantic geometry, exclusions, and readability at `1280×720`. Mirroring, repositioning, palette/shape/scale/spacing changes, and decorative substitutions are cosmetic changes, not separate directions.
7. If any pair reads as near-variants of one representation, reject and regenerate the collapsed direction before selection.
8. Select the strongest passing candidate; never promote the first candidate by default.
9. Normalize only when needed to exact `1920×1080` without changing composition or copy, and record the operation.
10. Copy the selected candidate to its unpadded one-based canonical position,
    `canonical/light/16x9/{position}.png` (or `references/` for the shared anchor).
11. Persist direction briefs, filenames, observed concept/mechanism/composition differences, `Candidate-divergence review`, rejection reasons, exact-copy evidence, dimensions/mode, selection rationale, and scores in `evaluation/review.md` and `scores.csv`.
12. Re-run the relevant validators. New or regenerated pilot packages use `--require-divergence` together with `--require-drafts`.

The accountable Codex reviewer may select candidates when the user has explicitly requested autonomous completion of the whole milestone. Any ambiguous change to the locked visual direction still requires user approval.

## Acceptance thresholds

- clarity = 5;
- presentation readability = 5;
- text fidelity = 5;
- every other criterion ≥ 4;
- average ≥ 4.4.
- candidate divergence = pass before rubric selection.

## Capability blocker

If built-in generation is unavailable, finish the YAML prompt package, report `built-in Codex image generation unavailable`, give the expected filenames and dimensions, and stop. Do not substitute placeholders or treat a missing API key as the blocker.
