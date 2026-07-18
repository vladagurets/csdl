---
id: '25'
title_uk: Analytical Mode v0.1
editorial_language: uk
terminology_language: en
---
# Analytical Mode v0.1

Constructive styling ніколи не змінює те, що кажуть data. `Analytical Mode v0.1` є independent additive extension: він посилається на compatible recipes і 15 public components, але не змінює `Prompt DSL v0.5`.

## Invariants

- dataset identity, field bindings, domain, order, values, units, labels і source зберігаються exactly;
- zero не є missing;
- transformations explicit, deterministic і auditable;
- bar-like encodings починаються від zero;
- log scale і dual axis forbidden by default;
- direct labels precede `Legend`;
- color has a redundant label/form carrier;
- forecast відрізняється від observed, uncertainty показує bounds;
- decorative geometry вимкнена або займає не більше 5% як contextual `Field`.

Internal marks (`bar`, `line`, `cell`, `region`, `network-edge`) не стають public components.
