# Night Mode and Accessibility v0.1 — Proof Review

**Evidence class:** deterministic specification over accepted light and analytical sources  
**Visual calibration:** accepted Pilot 01 and Visual DNA light rasters  
**Raster generation, recoloring, or mutation:** none

## Review method

Each proof was reviewed through independent paths:

1. the builder loaded the unchanged canonical Recipe or Analytical package, calculated a semantic-source SHA-256, applied the selected profile tokens, and derived exact text/non-text checks;
2. the validator reloaded the canonical source and token contracts independently, recomputed source/semantic digests, sRGB luminance, every adjacent contrast ratio, stroke threshold, fallback carrier, scenario invariant, compatibility rule, and deterministic output.

Synthetic packages establish contract correctness only. They do not claim that a night, projector, CVD, or monochrome raster has been visually accepted.

## Proof decisions

| Proof | Canonical source | Mechanical acceptance |
|---|---|---|
| Editorial equivalence | Recipe proof `01-editorial` | light/night source and semantic signatures are identical; display/label/meta and Signal pairs pass |
| Structural Signal | Recipe proof `02-structural` | light/night/monochrome route, Signal, focus, selection, and direction use form/label/boundary redundancy |
| Exact table | Analytical proof `09-table` | exact lookup, labels, units, source, missing/zero distinction, Frame/Axis contrast |
| Positive/negative bar | Analytical proof `01-bar` | signed values share a visible zero Axis and retain position/numeric/direct labels |
| Forecast/uncertainty | Analytical proof `02-line` | observed solid, forecast dashed with direct labels and boundary; 80% interval has visible lower/upper boundaries |
| Heatmap | Analytical proof `05-heatmap` | exact numeric labels plus deterministic pattern scale; unavailable cell remains `N/A`, not zero |
| Normalized map | Analytical proof `07-map` | normalized denominator/unit preserved; regions use pattern/direct labels; missing region uses open frame and `N/A` |
| Directed network | Analytical proof `08-network` | arrowheads/direct labels preserve direction; numeric labels/stroke tiers preserve weight |
| Monochrome export | Recipe proof `02-structural` | Signal, focus, selection, error, positive, attention, data, missing, uncertainty, observed, and forecast survive without hue |
| Projector fallback | Analytical proof `10-dashboard` | all text ≥7:1, meaningful graphics ≥4.5:1, critical rules ≥3 px, source/units retained |

## Negative review

Seventeen indexed fixtures reject all objective-listed failures plus two explicit contract risks: insufficient text contrast; insufficient non-text contrast; color-only meaning; indistinguishable observed/forecast values; invisible uncertainty; missing confused with zero; inaccessible heatmap scale; hue-only map regions; color-only network direction; Signal lost in grayscale; unreadable source; light/night role mutation; unsupported token/component combination; undeclared layout; nondeterministic output; prohibited color pairing; and inaccessible Signal area.

Every fixture is a deterministic mutation over one accepted proof package. Strict validation requires its exact indexed error.

## Evidence-backed versus synthetic rules

Accepted evidence supports hierarchy, direct labels, one Signal, expression-level area ceilings, exact analytical values/units/source, open structures, and color-independent meaning. WCAG 2.2 supports 4.5:1 text, 3:1 meaningful non-text, use-of-color, and focus requirements. Projector thresholds, calibrated accessible token values, pattern assignments, CVD declarations, monochrome forms, and all new night proofs are deterministic synthetic rules.

## Compatibility

- Prompt DSL v0.5 unchanged.
- Exactly fifteen D-029 public components; no accessibility role is promoted to a component.
- Exactly 23 D-030 recipes; no output profile becomes a recipe.
- All ten Analytical Mode families mapped without changing data, domains, order, units, missing states, uncertainty, forecast, geography, networks, or transformations.
- Legend remains conditional and absent from the ten proofs because direct labels remain viable.

## Remaining visual risk and deferral

No accepted raster demonstrates the calibrated night tokens, projector degradation, pattern density, CVD simulations, or monochrome hierarchy. A future visual calibration requires explicit approval before generation and three-candidate review for the bounded packet documented in the Milestone 6 evidence audit. Milestone 6 does not substitute placeholders or schema proofs for visual acceptance.

## Local release-candidate validation

The complete pre-integration matrix passed on 2026-07-18:

- `153` pytest cases;
- Pilot manifest, style anchor, canonical assets, and scores;
- Visual DNA catalog, fixed data, assets, scores, review, deterministic rebuild, and index;
- Component Library contract, proofs, deterministic rebuild, and index;
- Recipe Library, proof rebuild, Prompt DSL v0.5, deterministic library rebuild, and index;
- Analytical Mode deterministic rebuild and strict validation;
- Night Mode and Accessibility deterministic rebuild and strict validation.

The accessibility raster inventory contains exactly sixty tracked accepted PNGs and excludes ignored drafts. Every recorded SHA-256 matches the current bytes. Final clean-commit repeated-builder/no-diff validation and GitHub integration remain separate gates before the milestone state changes to complete.
