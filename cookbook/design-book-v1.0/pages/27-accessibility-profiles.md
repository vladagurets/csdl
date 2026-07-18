---
id: '27'
title_uk: Accessibility profiles
editorial_language: uk
terminology_language: en
---
# Accessibility profiles

`Night Mode and Accessibility v0.1` maps semantic roles, а не інвертує pixels.

{{accessibility_profiles}}

## Thresholds

- light / night / monochrome: text ≥ 4.5:1, meaningful non-text ≥ 3:1;
- projector: text ≥ 7:1, meaningful non-text ≥ 4.5:1;
- critical rules: 2 px normally, 3 px for projector at `1920×1080`;
- threshold ratios are exact and never rounded upward.

Night, projector, monochrome і CVD outputs мають deterministic specification evidence. Вони не мають accepted raster calibration без окремого generation/review gate.
