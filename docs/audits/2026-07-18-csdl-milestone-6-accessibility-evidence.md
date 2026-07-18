# Milestone 6 Night Mode and Accessibility — Evidence Audit

**Date:** 2026-07-18  
**Scope:** Night Mode and Accessibility v0.1  
**Repository baseline:** clean `main` at `e079b89d0316724d576815d31c46144a4bd23e55`, equal to `origin/main`

## Audit conclusion

CSDL already has strong accepted evidence for semantic roles, restrained signal area, presentation-scale type, direct labels, exact analytical values, and color-independent meaning. It does not yet have accepted raster evidence for night mode, projector degradation, color-vision differences, or monochrome output. The Foundation night palette is provisional: its semantic intent is useful, but several required adjacent pairs do not meet measurable non-text contrast.

Milestone 6 should therefore be an independent additive contract under `accessibility/night-mode-v0.1/`. It must map existing meanings to accessible light, night, monochrome, and projector profiles without changing Prompt DSL v0.5, the fifteen D-029 components, the 23 D-030 recipes, Analytical Mode v0.1 quantitative invariants, or any accepted raster. Deterministic specification proofs can establish semantic equivalence, contrast, redundant encodings, and output provenance. They cannot claim visual acceptance for a generated night series.

No new raster is required to complete the machine contract. A future visual-calibration packet would need three candidates per selected proof family, full-resolution and `1280×720` review, projector inspection, CVD/monochrome review, exact-copy/data checks, and explicit user approval before generation.

## Audited sources

### Foundation palette and typography

`specs/2026-07-17-csdl-v0.1-design.md` defines:

- the accepted light roles `paper.base`, `paper.raised`, `ink.primary`, `ink.secondary`, `neutral.fill`, `neutral.line`, and four semantic signals;
- provisional night roles for base, raised surface, ink, line, and four signals;
- presentation type roles for display, body, label, metadata/source, and code;
- one dominant Signal, restrained signal area, and a rule that color reinforces rather than replaces form, position, or labels;
- Analytical Mode preference for direct labels and the requirement that color is never the sole carrier.

Independent WCAG 2.2 relative-luminance calculations against the declared backgrounds produced:

| Pair | Ratio | Result |
|---|---:|---|
| `ink.primary` / `paper.base` | 15.8320:1 | text pass |
| `ink.secondary` / `paper.base` | 6.9492:1 | text pass |
| `neutral.line` / `paper.base` | 1.8788:1 | meaningful non-text fail |
| `signal.primary` / `paper.base` | 3.6155:1 | non-text pass; normal text fail |
| `signal.data` / `paper.base` | 5.1591:1 | text and non-text pass |
| `signal.attention` / `paper.base` | 2.2222:1 | meaningful non-text fail |
| `signal.positive` / `paper.base` | 3.4545:1 | non-text pass; normal text fail |
| `night.ink` / `night.base` | 14.8304:1 | text pass |
| `night.ink.secondary` / `night.base` | 8.6161:1 | text pass |
| `night.line` / `night.base` | 2.4021:1 | meaningful non-text fail |
| night signals / `night.base` | 5.5158–8.7833:1 | text and non-text pass |

Ratios are threshold values and are not rounded for conformance decisions. Signal colors that pass graphical contrast but fail 4.5:1 remain valid for non-text emphasis only; informative text must use an ink token or an explicitly valid foreground/background pairing.

### Accessibility standard

The measurable baseline is WCAG 2.2:

- SC 1.4.3: informative text uses at least 4.5:1; large text may use 3:1, but CSDL v0.1 deliberately keeps 4.5:1 for every informative text role;
- SC 1.4.11: meaningful graphical objects and state indicators use at least 3:1 against adjacent colors;
- SC 1.4.1: color is not the only carrier of information, action, response, or distinction;
- SC 2.4.13: focus appearance provides at least the area of a 2 CSS-pixel perimeter and a 3:1 focused/unfocused change.

Canonical references:

- <https://www.w3.org/TR/WCAG22/>
- <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html>
- <https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html>
- <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html>
- <https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html>

Projector behavior is a CSDL delivery profile rather than a WCAG conformance level. It will use a synthetic safety margin of 7:1 for informative text and 4.5:1 for meaningful non-text, thicker critical rules, no low-contrast raised-surface dependency, and direct labels.

### Accepted Pilot 01 and Visual DNA rasters

Audited evidence includes the Pilot 01 style anchor, seven canonical slides, three primary Visual DNA reference boards, seventeen generated Visual DNA canonical files, their previews/contact sheets, scores, and review records.

Accepted evidence establishes:

- exact light-mode copy and full-resolution/`1280×720` readability;
- one dominant semantic Signal with form, weight, position, continuity, direction, or direct text as a redundant carrier;
- sparse neutral rules and open analytical surfaces;
- exact lookup, units, source, ordered values, and direct labels in KPI/Table/Chart/Dashboard;
- no positive Legend requirement in accepted single-series evidence;
- no night, projector, CVD-simulation, or monochrome acceptance claim.

The baseline SHA-256 inventory covers the style anchor, seven Pilot canonical slides, three reference boards, and seventeen Visual DNA canonical rasters. Milestone 6 will re-run the same inventory after implementation and after merge; byte changes are forbidden.

### Component Library v0.1

The fifteen public components already separate meaning from appearance:

- Signal is an attached semantic role, not a color synonym;
- Label has one target and preserves values, units, periods, sources, and punctuation;
- Legend is conditional, subordinate, limited to two–four text-and-form mappings, and requires a recorded direct-label failure;
- Axis owns ordered/quantitative reference structures and honest domains;
- Divider, Vector, Bridge, Node, Frame, Field, and Pulse have distinct semantic ownership.

Missing contract: accessible token eligibility, minimum rule weights, focus/selection states, light/night equivalence, and fallback mappings for each component.

### Recipe Library and Prompt DSL v0.5

All 23 recipes require one dominant signal and state that color is not the only carrier. Prompt DSL v0.5 is closed and layout-free. It has no field for an accessibility profile and must not be changed in place. The additive extension can reference an unchanged v0.5 package/recipe and attach output-mode requirements externally.

### Analytical Mode v0.1

Analytical Mode already preserves data identity, domain, order, values, units, labels, source, transformations, missing states, forecast boundaries, uncertainty, and non-color fallbacks. It supplies deterministic source packages for bars, forecast lines, heatmaps, maps, networks, tables, and dashboards.

Missing contract: measurable token contrast, profile-specific line/interval/region/edge behavior, grayscale Signal survival, and standardized redundant encodings across night/projector/monochrome output. These are additive presentation constraints; they must not rewrite analytical data or encodings.

### Tooling, tests, migrations, decisions, and CI

Milestones 3–5 establish the repository pattern to preserve:

- canonical Markdown plus machine-readable manifests/schemas/contracts;
- strict and tested `require_complete=False` validation;
- deterministic packages, indexes, and compatibility outputs;
- positive indexes and exact-error negative mutation fixtures;
- independent validation against canonical sources;
- additive migration/rollback documentation;
- CI rebuild followed by `git diff --exit-code`.

D-029, D-030, and D-031 remain intact. D-032 records the independent accessibility/night-mode boundary.

## Evidence classification

### Accepted evidence-backed rules

- semantic roles are stable across modes;
- one dominant Signal and existing expression-level area ceilings;
- color never acts alone;
- direct labels precede Legend;
- display/body/label/meta/code hierarchy and horizontal body text;
- sparse meaningful rules, open surfaces, exact analytical labels/units/sources;
- observed/forecast, uncertainty, missing/zero, direction, weight, category, and status remain distinct by semantics;
- no gradients, shadows, 3D, glossy surfaces, UI chrome, decorative coordinates, or random dot fields;
- Prompt DSL v0.5, D-029, D-030, D-031, and accepted rasters are immutable dependencies.

### Standards-backed synthetic rules

- 4.5:1 minimum for every informative text role;
- 3:1 minimum for meaningful non-text and state indicators;
- color-independent redundant form/text/pattern requirements;
- focus indicator area and contrast requirements;
- exact sRGB contrast calculation and adjacent-color evaluation.

### CSDL-specific synthetic proof rules

- 7:1 text and 4.5:1 non-text projector profile;
- minimum critical rule weights per normal and projector output;
- light/night semantic signature equality;
- monochrome patterns/forms and direct labels for semantic roles;
- deterministic CVD review declarations for protanopia, deuteranopia, tritanopia, and achromatopsia;
- token-safe foreground/background combinations and prohibited combinations;
- analytical fallback rules for Axes, Nodes, intervals, maps, heatmaps, and networks;
- deterministic output/provenance digests.

## Raster decision and visual evidence gap

There is a genuine visual evidence gap for night/projector/monochrome/CVD output. It does not block a machine-readable Milestone 6 contract because the required semantics and thresholds can be proved deterministically. No raster will be generated in this milestone without a separate explicit approval.

If visual calibration is later approved, the smallest useful packet is three candidates each for: editorial light/night equivalence, an analytical forecast/uncertainty slide, a heatmap/map/network accessibility composite, and a projector/monochrome stress slide. Each family must use accepted source copy/data, record three-candidate selection and rejection evidence, and pass exact text/data, contrast, CVD, grayscale, projector, full-resolution, and `1280×720` review.

## Risks and controls

- **Token inversion changes meaning.** Compare canonical semantic signatures across light/night profiles; reject any role mutation.
- **Passing hex ratios hides thin-line loss.** Require minimum critical stroke widths and stronger projector rules in addition to contrast.
- **CVD robustness becomes a palette-only claim.** Require label/form/pattern redundancy under every declared CVD profile.
- **Monochrome collapses Signal/status/data.** Require distinct deterministic forms/patterns plus direct text, and validate grayscale contrast.
- **Accessibility terms leak into public vocabulary.** Keep them extension-internal; component and recipe counts remain exact.
- **Analytical presentation rewrites data.** Reload the canonical Analytical Mode package and compare a deterministic semantic digest.
- **Synthetic proofs are mistaken for raster acceptance.** Mark every package `evidence: deterministic_specification`; evaluation notes retain the visual deferral.

## Recommendation

Proceed under D-032 with `accessibility/night-mode-v0.1/` as an independent additive extension. Calibrate accessible semantic token mappings, validate them mathematically, and prove ten required scenarios without changing existing contracts or rasters.
