---
id: '23'
title_uk: Prompt DSL v0.5 anatomy
editorial_language: uk
terminology_language: en
---
# Prompt DSL v0.5 anatomy

`Prompt DSL v0.5` — closed declarative package. Він не описує pixel layout; він відокремлює meaning, exact copy/data, public grammar, generation constraints і provenance.

{{prompt_dsl_fields}}

## Ownership

- `semantic_intent` — що треба зрозуміти;
- `content` — що має бути відтворено exact;
- `component_instances` — які public roles беруть участь;
- `relations` — як roles пов’язані;
- `generation_constraints` — expression, canvas, typography, palette, exclusions;
- `provenance` — звідки походять contract і content.

Forbidden layout keys, undeclared components, unsupported relations і placeholders відхиляються. Full analytical data grammar не додається до v0.5; її надає independent `Analytical Mode v0.1`.
