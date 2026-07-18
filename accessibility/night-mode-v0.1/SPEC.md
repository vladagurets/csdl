# CSDL Night Mode and Accessibility v0.1

**Status:** complete
**Canonical source:** Markdown  
**Machine contract:** `manifest.yaml`, `token-schema.yaml`, `proof-schema.yaml`, and `contracts/`  
**Version boundary:** independent additive extension; Prompt DSL v0.5 unchanged

## 1. Purpose

Night Mode and Accessibility preserves CSDL meaning, hierarchy, quantitative fidelity, presentation readability, and Constructive Signal identity when an output uses a dark field, a low-contrast projector, color-vision fallback, or monochrome export. It maps semantic roles rather than inverting pixels or recoloring accepted rasters.

## 2. Contract layers

1. An existing CSDL source package remains the semantic and quantitative authority.
2. One Accessibility v0.1 proof source names the output profiles and meaning that must survive.
3. The token contract maps shared semantic roles to light, night, monochrome, and projector values.
4. The contrast contract defines exact sRGB thresholds, eligible pairings, critical stroke weights, and focus appearance.
5. The fallback contract assigns direct text, form, line style, boundary, pattern, direction, and weight redundancy.
6. Compatibility maps the unchanged D-029 components, D-030 recipes, Prompt DSL v0.5, and Analytical Mode v0.1 families.
7. A deterministic builder derives proof packages, contrast matrices, indexes, compatibility output, and provenance digests.

Accessibility roles are extension-internal. They are not public components, recipes, layout vocabulary, or analytical marks.

## 3. Semantic token profiles

### Light

Light preserves warm paper, graphite, mineral signals, and Quiet Modular restraint. Foundation values that already meet their declared use remain recognizable. Meaningful rules use a stronger neutral token; the provisional ochre attention role is darkened enough for non-text use. Signal labels remain neutral unless an explicitly valid text pairing is declared.

### Night

Night uses a warm graphite field, a slightly raised surface, light neutral ink, and lifted mineral signals. It is not a channel inversion. A raised fill never carries a boundary alone: a meaningful surface uses `line.strong` or another redundant boundary.

### Monochrome

Monochrome uses one-channel tonal values plus deterministic direct labels, shapes, line styles, patterns, boundaries, and stroke weights. Tone may support meaning but never acts alone. Random dot fields are forbidden; patterns are named, ordered, and reproducible.

### Projector

Projector is a high-margin dark profile for ambient light and low-contrast display paths. Every informative text pairing meets 7:1, every meaningful graphical pairing meets 4.5:1, critical rules are at least 3 output pixels at `1920×1080`, and raised-surface fill cannot be the only boundary.

## 4. Contrast and readability

- Every informative display, body, label, metadata, code, axis, unit, and source element uses at least 4.5:1 in light, night, and monochrome profiles.
- Projector uses at least 7:1 for every informative text role.
- Meaningful graphical objects and states use at least 3:1 in light, night, and monochrome; projector uses at least 4.5:1.
- Thresholds are exact and are never rounded upward.
- Contrast is measured between declared adjacent sRGB colors, not inferred from a raster preview.
- `line.subtle`, low-contrast fills, and raised-surface differences are non-semantic unless accompanied by a valid boundary.
- Normal critical rules are at least 2 output pixels at `1920×1080`; projector rules are at least 3.
- Interactive focus uses at least the area of a 2 CSS-pixel perimeter and a 3:1 focused/unfocused change.

## 5. Typography

The Foundation type roles remain unchanged. Display, body, label, metadata/source, code, axis, and unit text all use valid ink/background pairs. The v0.1 contract deliberately does not use the relaxed large-text ratio. Thin or unusual strokes cannot compensate for weak contrast. Body copy stays horizontal; direct analytical labels keep values, units, periods, and source association.

## 6. Color-independent meaning

Every semantic encoding names at least one redundant carrier beyond color. Required roles include Signal, focus, selection, error, positive, attention, data, category, missing, uncertainty, observed, and forecast.

- Signal: form/weight/boundary/direct label plus semantic color.
- Focus: visible perimeter or equivalent area plus 3:1 state change.
- Selection: solid or double boundary plus direct label/state text.
- Error: error label and deterministic diagonal hatch or boundary.
- Positive: positive label/check form and horizontal hatch or boundary.
- Attention: attention label/warning form and cross hatch or boundary.
- Data/category: direct labels and shape/line-style/pattern mapping.
- Missing: `N/A`, `MISSING`, or declared status; never zero.
- Uncertainty: visible lower/upper boundaries plus named interval and level.
- Observed/forecast: solid versus dashed line plus direct status/boundary labels.
- Direction: arrowhead and/or direction label; color alone is invalid.
- Weight: numeric label and declared stroke tiers; color alone is invalid.

Color-vision review declares protanopia, deuteranopia, tritanopia, and achromatopsia. Passing does not require hues to remain mutually distinct because every meaning survives without hue.

## 7. Analytical objects

- Thin rules and Axes use `line.strong` when required to understand scale, lookup, zero, direction, or boundary.
- Nodes and Signal states retain direct labels or distinct form/weight.
- Intervals expose boundaries and text; translucent fill alone is invalid.
- Heatmap cells retain exact values or deterministic pattern bins; missing cells retain a text status and unique boundary.
- Map regions retain identifiers/direct labels and deterministic pattern classes; missing regions are explicit.
- Network edges retain arrowheads/direction labels and numeric or tiered weight fallback.
- Source and units remain informative text and use the same contrast threshold as body text.

Analytical Mode v0.1 remains the authority for data identity, values, order, domains, units, sources, transformations, missing states, uncertainty, forecast, geography, and networks. Accessibility packages may add presentation constraints only.

## 8. Direct Labels and Legend

Direct labels are preferred. Legend remains the D-029 conditional exception: one Legend, two–four text-and-form mappings, a recorded direct-label failure, subordinate placement, and no dominant Signal role. A palette strip or color-only key is invalid.

## 9. Light/night equivalence

Light and night representations of one source share an identical semantic-source digest. Component/recipe references, analytical values, relations, states, categories, ordering, missing values, forecast boundary, uncertainty, direction, weight, Signal target, and content cannot change with the profile. Only declared presentation tokens and fallback carriers vary.

## 10. Signal-area behavior

Existing expression and recipe ceilings remain authoritative. A Signal plane or fill cannot carry informative text unless the text uses an allowed foreground/background pair. Large Signal areas still require one semantic target and a redundant form/text mechanism. Accessibility does not authorize an extra color, extra Signal, or larger area.

## 11. Output and provenance

Every deterministic specification declares:

- `1920×1080` landscape output and sRGB color space;
- accessibility contract ID/version and selected profile;
- unchanged source path, source kind, and semantic-source SHA-256;
- exact token roles and allowed adjacent pairings;
- fallback/CVD requirements;
- deterministic builder identity and `deterministic: true`;
- `evidence: deterministic_specification`.

The contract emits YAML specifications, not accepted rasters. A future raster must follow the separate generation/review gate.

## 12. Prohibited behavior

- mechanical inversion or semantic-role swapping;
- color-only meaning;
- normal informative text below 4.5:1 or projector text below 7:1;
- meaningful graphics below 3:1 or projector graphics below 4.5:1;
- semantic use of `line.subtle`, raised fill, or transparent interval fill without a valid boundary;
- red/coral text on dark graphite when the declared pair fails;
- signal-colored normal text without a valid text pairing;
- missing values shown as zero;
- observed/forecast or uncertainty distinguished only by hue/fill;
- hue-only heatmap/map categories or network direction;
- unreadable units/source metadata;
- gradients, shadows, 3D, glossy surfaces, UI chrome, decorative coordinates, random dot fields, or undeclared layout/geometry vocabulary;
- nondeterministic output or missing provenance.

## 13. Evidence status

Accepted light rasters support semantic hierarchy, presentation readability, signal restraint, direct labels, and analytical exactness. WCAG 2.2 supports measurable contrast/color-independent thresholds. Night/projector/CVD/monochrome mappings and ten proofs are deterministic synthetic evidence only. No new raster is generated or visually accepted by this contract.
