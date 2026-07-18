---
id: '08'
title_uk: Typography roles
editorial_language: uk
terminology_language: en
---
# Typography roles

CSDL розділяє три voices, щоб hierarchy не залежала від випадкового font mixing.

## Modular Technical

Display role для covers, short headlines, key terms і великих чисел. Потрібні квадратні інженерні пропорції, сильні цифри, українська й English підтримка — без sci-fi novelty або ретро-імітації.

## Neutral Sans

Reading role для пояснень, labels і коротких абзаців. Відкриті форми, спокійний rhythm і якісні цифри важливіші за авторський жест.

## Technical Mono

Code role для commands, formula, schema і `Prompt DSL`.

## Licensed-font boundary

Точні global font families лишаються deferred. `Inter Display`, `Inter`, `IBM Plex Sans`, `IBM Plex Mono` та локальні PDF fallbacks є reference/implementation evidence, але не фінальним font lock. Книга не комітить font binaries і записує фактичний build font у provenance.
