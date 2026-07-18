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
3. Invoke built-in `$imagegen` three independent times with the same prompt and reference.
4. Save candidates under `pilots/01-agentic-discipline/drafts/light/16x9/<asset>/`.
5. Review all three for exact text, landscape hierarchy, semantic geometry, exclusions, and readability at `1280×720`.
6. Select the strongest passing candidate; never promote the first candidate by default.
7. Normalize only when needed to exact `1920×1080` without changing composition or copy, and record the operation.
8. Copy the selected candidate to `canonical/light/16x9/` (or `references/` for the shared anchor).
9. Persist filenames, rejection reasons, exact-copy evidence, dimensions/mode, selection rationale, and scores in `evaluation/review.md` and `scores.csv`.
10. Re-run the relevant validators.

The accountable Codex reviewer may select candidates when the user has explicitly requested autonomous completion of the whole milestone. Any ambiguous change to the locked visual direction still requires user approval.

## Acceptance thresholds

- clarity = 5;
- presentation readability = 5;
- text fidelity = 5;
- every other criterion ≥ 4;
- average ≥ 4.4.

## Capability blocker

If built-in generation is unavailable, finish the YAML prompt package, report `built-in Codex image generation unavailable`, give the expected filenames and dimensions, and stop. Do not substitute placeholders or treat a missing API key as the blocker.
