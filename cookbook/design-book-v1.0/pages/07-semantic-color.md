---
id: '07'
title_uk: Semantic color
editorial_language: uk
terminology_language: en
---
# Semantic color

Color у CSDL — не тема оформлення, а semantic role. `signal.primary` позначає дію або активну зміну; `signal.data` — дані; `signal.attention` — ризик чи невизначеність; `signal.positive` — стабілізацію або здоровий стан.

{{semantic_tokens}}

## Контракт

- normal page: background + ink + one dominant signal;
- informative text завжди використовує валідну ink/background pair;
- signal fill не дозволяє слабкий text contrast;
- color ніколи не є єдиним carrier;
- monochrome і projector зберігають meaning через label, form, pattern, boundary, direction або weight.

Light, night, monochrome і projector — mappings спільних roles, а не recoloring accepted rasters.
