---
id: '28'
title_uk: Meaning без залежності від color
editorial_language: uk
terminology_language: en
---
# Meaning без залежності від color

Кожен semantic state має щонайменше один carrier поза hue.

| Meaning | Redundant carriers |
|---|---|
| `Signal` | form, weight, boundary, direct label |
| selection | solid/double boundary + state text |
| error | label + diagonal hatch або boundary |
| positive | label/check + horizontal hatch |
| missing | `N/A` / `MISSING` + unique boundary |
| uncertainty | lower/upper boundaries + interval name |
| observed / forecast | solid/dashed + status label |
| direction | arrowhead або direction label |
| weight | numeric label або declared stroke tier |

Informative source, unit, axis і metadata мають ті самі text thresholds, що body copy. Raised fill або subtle line не можуть самі нести boundary meaning.
