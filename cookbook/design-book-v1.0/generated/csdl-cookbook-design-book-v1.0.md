---
title: CSDL Cookbook and Design Book v1.0
version: 1.0.0
page_count: 32
generated: true
canonical_sources: pages/*.md
---

<!-- page 01 · source pages/01-cover.md -->
# CSDL Cookbook and Design Book v1.0

## Конструктивна мова для складних пояснень

**Constructive Signal Design Language** допомагає перетворювати теми про AI, software engineering та економіку на зрозумілі презентаційні історії.

Одна ідея. Один візуальний механізм. Один домінантний `Signal`.

Українська редакційна мова + стабільна English technical vocabulary.

Milestone 7 · A4 landscape · Markdown canonical · not a public release

<!-- page-break -->

<!-- page 02 · source pages/02-how-to-use.md -->
# Як читати цю книгу

Це не альбом шаблонів. Книга рухається від принципів до рішень: спочатку пояснює, **чому** CSDL працює, потім показує **чим** будувати композицію і завершує процесом **як** перевіряти результат.

## Три шари

1. **Foundations** — Constructive Signal, Quiet Modular, A/B/C, color і typography.
2. **Grammar** — 15 public components, 23 recipes та `Prompt DSL v0.5`.
3. **Practice** — Analytical Mode, accessibility, provenance, authoring і preflight.

English identifiers у `code` є канонічними. Українські пояснення описують їхню роль, але не створюють перекладених API-назв.

Кожна сторінка має source map у `provenance.yaml`. Позначка **accepted raster evidence** означає візуально погоджений файл; **deterministic specification evidence** означає машинну перевірку без нового raster acceptance.

<!-- page-break -->

<!-- page 03 · source pages/03-philosophy.md -->
# Constructive Signal

CSDL починається не з форми, а зі змістовної дії. Масштаб показує вагу, напрямок — перехід, дистанція — зв’язок, вкладеність — scope, а overlap — наслідкову взаємодію.

## Принцип

**Meaning before decoration.** Якщо елемент не показує тезу, статус, напрямок, зв’язок або акцент, він не має роботи.

## Метод, не стилізація

Історична конструктивістська спадщина використовується як метод активного простору, контрольованої асиметрії та geometry-as-narrative. CSDL прямо виключає політичні символи, revolutionary-poster styling, псевдоісторичні шрифти й декоративний «червоний клин».

## Результат

Глядач має за кілька секунд знайти головну думку, сформувати просту ментальну модель і запам’ятати один сильний образ. Впізнаваність виникає з послідовних правил, а не з логотипа чи footer.

<!-- page-break -->

<!-- page 04 · source pages/04-quiet-modular.md -->
# Quiet Modular

Quiet Modular — default expression CSDL. Його сила не в тому, щоб зробити сторінку слабшою, а в тому, щоб залишити тільки форми з чіткою semantic ownership.

## Робоче правило

- один `Anchor` володіє тезою;
- один `Signal` показує найважливіший стан;
- до трьох supporting elements;
- 50–75% negative space залежно від expression level;
- один очевидний entry point і один exit point;
- колір не компенсує нечітку hierarchy.

## Перевірка відніманням

Приберіть кожну лінію, panel, badge і background shape по черзі. Якщо зміст не змінюється, елемент був декоративним. Якщо зв’язок зникає, поверніть елемент і назвіть його роль мовою components.

Quiet Modular — це дисципліна: спочатку ownership і relations, потім мінімальна геометрія, яка робить їх видимими.

<!-- page-break -->

<!-- page 05 · source pages/05-expression-levels.md -->
# Рівні A / B / C

Expression level — не оцінка якості. Це контракт щільності, руху й сили акценту.

## Level A — Quiet

60–75% вільного простору, один домінантний об’єкт, один signal color, до двох допоміжних елементів. Це 60–70% стандартної серії.

## Level B — Constructive

45–65% вільного простору, одна велика semantic form або активний `Vector`, 2–4 information nodes, контрольована асиметрія. Це 20–30% серії.

## Level C — Signal

Короткий текст, велика площина або `Collision`, poster contrast лише для cover, culmination чи share card. Це 5–10% серії.

**Не робіть:** кілька Level C поспіль.  
**Робіть:** використовуйте контраст між тихими й кульмінаційними сторінками як частину meaning.

<!-- page-break -->

<!-- page 06 · source pages/06-canvas-rhythm.md -->
# Canvas, density і rhythm

Presentation master залишається `1920×1080`, 16:9 landscape. A4 landscape цієї книги — окремий publication format і не змінює slide contract.

## Slide geometry

- 12 columns;
- 96 px horizontal margin;
- 72 px vertical safe margin;
- 24 px gutters;
- 8 px baseline unit;
- критичний текст не ближче 72 px до краю.

## Density contract

Одна сторінка не може бути одночасно щільною в text, geometry і color. Якщо один вимір зростає, два інші спрощуються.

## Series rhythm

```text
A → A → B → A → B → A → C
```

Ритм потрібен, щоб серія не перетворювалася на сім конкуруючих posters. Сильний фінальний peak працює лише після тихих сторінок.

<!-- page-break -->

<!-- page 07 · source pages/07-semantic-color.md -->
# Semantic color

Color у CSDL — не тема оформлення, а semantic role. `signal.primary` позначає дію або активну зміну; `signal.data` — дані; `signal.attention` — ризик чи невизначеність; `signal.positive` — стабілізацію або здоровий стан.

| Profile | Background | Ink | Primary signal | Text / non-text |
|---|---|---|---|---|
| `light` | `#F7F5F0` | `#1B1B19` | `#C96157` | 4.5:1 / 3.0:1 |
| `night` | `#171817` | `#EEEAE1` | `#D2756D` | 4.5:1 / 3.0:1 |
| `monochrome` | `#F7F5F0` | `#111111` | `#333332` | 4.5:1 / 3.0:1 |
| `projector` | `#101110` | `#FFFFFF` | `#F08C82` | 7.0:1 / 4.5:1 |

## Контракт

- normal page: background + ink + one dominant signal;
- informative text завжди використовує валідну ink/background pair;
- signal fill не дозволяє слабкий text contrast;
- color ніколи не є єдиним carrier;
- monochrome і projector зберігають meaning через label, form, pattern, boundary, direction або weight.

Light, night, monochrome і projector — mappings спільних roles, а не recoloring accepted rasters.

<!-- page-break -->

<!-- page 08 · source pages/08-typography.md -->
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

<!-- page-break -->

<!-- page 09 · source pages/09-visual-grammar.md -->
# Visual grammar

Components — це слова візуальної мови. Recipes — це синтаксичні конструкції для конкретних explanatory problems. Relations визначають, як roles взаємодіють.

## Nouns і structures

`Anchor`, `Signal`, `Field`, `Frame`, `Cluster`, `Node`, `Pulse`, `Label`.

## Actions і relations

`Vector`, `Divider`, `Loop`, `Collision`, `Bridge`, `Axis`, constrained `Legend`.

## CSDL sentence

```text
One Anchor inside one open Field,
connected to two Clusters by one Vector,
balanced by negative space,
with one primary Signal.
```

Композиція проходить review, коли кожен visible element можна назвати component role, а кожен зв’язок має owning relation. Layout words на кшталт card grid, sidebar або floating panel не є public vocabulary.

<!-- page-break -->

<!-- page 10 · source pages/10-components-01-03.md -->
# Components 01–03

Перші три roles встановлюють semantic priority і контекст. Вони відповідають на питання: що головне, що потребує уваги і в якому середовищі це відбувається?

## 01 · `Anchor`
**Purpose.** Carry the composition's dominant proposition or central concept.
**Meaning.** The first semantic read and ownership root for subordinate content.

## 02 · `Signal`
**Purpose.** Identify the one state, result, transition, value, path, or boundary needing immediate attention.
**Meaning.** A dominant emphasis role attached to another component; never free decoration or a color synonym.

## 03 · `Field`
**Purpose.** Establish context, environment, or state scope without defaulting to a closed panel.
**Meaning.** The space in which components share context or state.

**Do:** прикріплюйте `Signal` до конкретного target.  
**Don’t:** використовуйте coral shape як вільну decoration.  
**Check:** `Anchor` має бути першим semantic read, навіть коли `Signal` сильний візуально.

<!-- page-break -->

<!-- page 11 · source pages/11-components-04-06.md -->
# Components 04–06

Ці roles створюють межу, групу і дію. Їх легко сплутати з generic containers або arrows, тому owning semantics важливіші за appearance.

## 04 · `Frame`
**Purpose.** Create a functional boundary for scope, lookup, or nested ownership depth.
**Meaning.** A visible or implied boundary whose edge improves interpretation.

## 05 · `Cluster`
**Purpose.** Group related concepts, evidence, or measures without automatically implying order.
**Meaning.** A set whose members share one role, model, or review context.

## 06 · `Vector`
**Purpose.** Communicate direction, action, or transformation between declared semantic sources and targets.
**Meaning.** An active route whose direction changes how connected components are read.

`Frame` потрібен лише там, де edge покращує interpretation. `Cluster` групує peer concepts без автоматичного order. `Vector` завжди має source, target і semantic direction.

Retired `Container` не повертається: context належить `Field`, functional scope — `Frame`, related set — `Cluster`.

<!-- page-break -->

<!-- page 12 · source pages/12-components-07-09.md -->
# Components 07–09

Поділ, одиниця і recurrence формують базову process grammar.

## 07 · `Divider`
**Purpose.** Separate peer states, positions, or scopes without establishing scale, direction, or moral priority.
**Meaning.** A subordinate distinction boundary between comparable regions.

## 08 · `Node`
**Purpose.** Represent one stage, actor, option, concept, gate, or data point.
**Meaning.** One discrete semantic unit participating in a larger relation or set.

## 09 · `Loop`
**Purpose.** Represent a closed recurring process whose output changes or feeds the next cycle.
**Meaning.** One directed recurrence over three to five ordered stages.

`Divider` розрізняє peer regions, але не створює scale чи moral priority. `Node` — discrete semantic unit, не автоматична UI card. `Loop` має 3–5 ordered stages, один напрямок і рівно одне closure.

**Diagnostic:** якщо шлях не повертається до початку, це може бути `Workflow` або `Pipeline`, але не `Loop`.

<!-- page-break -->

<!-- page 13 · source pages/13-components-10-12.md -->
# Components 10–12

Ця група пояснює consequence, topology і order.

## 10 · `Collision`
**Purpose.** Show two forces or Anchors producing one consequential intersection, constraint, or synthesis.
**Meaning.** A named result created by one functional overlap between two inputs.

## 11 · `Bridge`
**Purpose.** Connect semantically distant components for topology, ownership, or explicit branching without implying continuous progress.
**Meaning.** A declared relation between separate Nodes, Fields, Frames, or Clusters.

## 12 · `Axis`
**Purpose.** Establish ordered progression, continuous comparison, lookup alignment, support alignment, or quantitative domain.
**Meaning.** An open reference structure that makes order, dimension, lookup, or scale explicit.

`Collision` потребує наслідкового overlap, а не декоративної adjacency. `Bridge` з’єднує distant semantic objects без обіцянки безперервного progress. `Axis` робить explicit sequence, coordinate, lookup, support або quantitative domain.

**Check:** `Axis` не має псевдоточних ticks; `Bridge` не маскується під action arrow; `Collision` називає результат interaction.

<!-- page-break -->

<!-- page 14 · source pages/14-components-13-15.md -->
# Components 13–15

Останні roles відповідають за exact measure і naming.

## 13 · `Pulse`
**Purpose.** Make one exact number or measure the dominant explanatory object.
**Meaning.** A bounded value whose attached label, unit, period, and provenance establish what the number means.

## 14 · `Label`
**Purpose.** Name or qualify one component directly so meaning does not depend on position or color alone.
**Meaning.** A short textual attachment with exactly one semantic target.

## 15 · `Legend`
**Purpose.** Provide a subordinate indirect key for two to four analytical categories only when direct labels cannot fit without collision or ambiguity.
**Meaning.** A conditional mapping from repeated text-and-form keys to analytical categories; never a primary signal, mechanism, or decorative palette strip.

`Pulse` ніколи не відривається від label, unit, period і provenance. `Label` має рівно один target. `Legend` — constrained exception: 2–4 text-and-form mappings лише після записаної причини, чому direct labels створюють collision або ambiguity.

Accepted single-series `Chart` не потребує `Legend`; positive canonical Legend raster не заявляється.

<!-- page-break -->

<!-- page 15 · source pages/15-relations.md -->
# Relations і semantic geometry

Relation має owning component. Це запобігає ситуації, коли одна connector line одночасно означає flow, hierarchy і sequence.

| Relation | Owner | Коли використовувати |
|---|---|---|
| `inside` / `contains` | `Field`, `Frame`, `Cluster` | context, boundary або grouping |
| `attached_to` | `Label`, `Signal` | direct naming або emphasis |
| `connected_to` | `Bridge`, `Vector` | topology або action |
| `orders` | `Axis`, `Loop` | open order або closed recurrence |
| `separates` | `Divider` | peer distinction |
| `overlaps` / `produces` | `Collision` | consequential intersection |
| `maps_to` | `Legend` | exceptional indirect key |

**Do:** оберіть один owner і перевірте source/target.  
**Don’t:** дублюйте той самий meaning двома connector types.

<!-- page-break -->

<!-- page 16 · source pages/16-recipes-001-004.md -->
# Recipes 001–004 · Editorial focus

Ці recipes дають одній тезі, назві, цитаті або величині достатньо простору, щоб стати головним read.

## 001 · `Hero`
Make one proposition immediately understandable and memorable.
**Ingredients.** `Anchor` × 1; `Signal` × 1
**Levels.** A: yes · B: yes · C: yes

## 002 · `Cover`
Name a series or section and establish its single visual premise.
**Ingredients.** `Anchor` × 1; `Field` × 1; `Signal` × 1
**Levels.** A: yes · B: no · C: yes

## 003 · `Quote`
Give one exact statement enough space and hierarchy to be read as an idea, not decoration.
**Ingredients.** `Anchor` × 1; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

## 004 · `Big Number`
Make one exact quantity the dominant explanatory object.
**Ingredients.** `Anchor` × 1; `Pulse` × 1; `Label` × 1–2; `Signal` × 1
**Levels.** A: yes · B: yes · C: yes

Вибір визначає explanatory problem, а не preferred composition. `Hero` не замінює `Cover`; `Big Number` потребує exact quantity, unit і context; `Quote` зберігає exact statement.

<!-- page-break -->

<!-- page 17 · source pages/17-recipes-005-007.md -->
# Recipes 005–007 · Difference and change

Порівняння, зіткнення й трансформація мають різні semantics. Не використовуйте dramatic geometry, якщо content лише зіставляє peer systems.

## 005 · `Comparison`
Compare two systems without implying conflict unless conflict is the content.
**Ingredients.** `Anchor` × 2; `Field` × 2; `Divider` × 1; `Signal` × 1
**Levels.** A: yes · B: yes · C: yes

## 006 · `Collision`
Show two forces producing one consequential intersection or synthesis.
**Ingredients.** `Anchor` × 2; `Collision` × 1; `Signal` × 1; `Label` × 0–3 optional
**Levels.** A: no · B: yes · C: yes

## 007 · `Before / After`
Make a state change legible without reducing it to cosmetic restyling.
**Ingredients.** `Field` × 2; `Divider` × 1; `Vector` × 1; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

`Comparison` лишається complementary за замовчуванням. `Collision` потребує named consequence. `Before / After` показує state change через два `Field`, один `Divider` і semantic `Vector`.

<!-- page-break -->

<!-- page 18 · source pages/18-recipes-008-011.md -->
# Recipes 008–011 · Order, position, ownership, topology

Ці recipes допомагають розрізнити чотири питання: коли, де відносно двох dimensions, хто чим володіє і які boundaries взаємодіють.

## 008 · `Timeline`
Show ordered change over time with one unambiguous reading direction.
**Ingredients.** `Axis` × 1; `Node` × 3–7; `Label` × 3–7; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

## 009 · `Matrix`
Position a small set of options across two independent dimensions.
**Ingredients.** `Axis` × 2; `Field` × 1; `Node` × 2–6; `Label` × 4–10; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

## 010 · `Hierarchy`
Show levels of ownership or decomposition without implying sequence.
**Ingredients.** `Anchor` × 1; `Frame` × 1–4; `Node` × 2–7; `Bridge` × 1–4; `Label` × 2–7
**Levels.** A: yes · B: yes · C: no

## 011 · `Architecture`
Explain stable system boundaries and permitted interactions.
**Ingredients.** `Field` × 1–2; `Node` × 2–7; `Bridge` × 1–4; `Label` × 2–7
**Levels.** A: yes · B: yes · C: no

`Timeline` не є workflow. `Matrix` не є table. `Hierarchy` не обіцяє chronology. `Architecture` пояснює stable boundaries і permitted interactions, а не operational next step.

<!-- page-break -->

<!-- page 19 · source pages/19-recipes-012-016.md -->
# Recipes 012–016 · Process and mental models

Process recipes відрізняються тим, що саме рухається: actor/action, recurring state, material through gates, decision consequence або peer concepts in one model.

## 012 · `Workflow`
Show who or what acts next in a bounded operational sequence.
**Ingredients.** `Node` × 2–7; `Vector` × 1–5; `Label` × 2–7; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

## 013 · `Loop`
Show a repeating process whose output changes the next cycle.
**Ingredients.** `Loop` × 1; `Node` × 3–5; `Label` × 3–5; `Signal` × 1
**Levels.** A: yes · B: yes · C: yes

## 014 · `Pipeline`
Show material or data transformed through fixed stages.
**Ingredients.** `Node` × 3–7; `Vector` × 1–5; `Label` × 3–7; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

## 015 · `Decision Tree`
Make a small branching rule and its consequences explicit.
**Ingredients.** `Node` × 3–7; `Bridge` × 2–4; `Label` × 3–7; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

## 016 · `Framework`
Organize a small set of mutually necessary concepts into one mental model.
**Ingredients.** `Anchor` × 1; `Cluster` × 1; `Node` × 2–6; `Label` × 2–6; `Signal` × 1
**Levels.** A: yes · B: yes · C: no

Швидка діагностика: `Workflow` відповідає “what acts next?”, `Loop` — “what feeds the next cycle?”, `Pipeline` — “what is transformed?”, `Decision Tree` — “what follows this rule?”, `Framework` — “what concepts are jointly necessary?”.

<!-- page-break -->

<!-- page 20 · source pages/20-recipes-017-020.md -->
# Recipes 017–020 · Analytical needs

Ці recipes визначають presentation need, але не замінюють `Analytical Mode v0.1`. Dataset, domain, order, values, units, missing states і transformations належать additive analytical contract.

## 017 · `KPI`
Expose one primary operational measure with only the context needed to interpret it.
**Ingredients.** `Pulse` × 1; `Axis` × 1; `Label` × 2–8; `Signal` × 1
**Levels.** A: yes · B: no · C: no

## 018 · `Table`
Support exact lookup and comparison across a small fixed dataset.
**Ingredients.** `Frame` × 1; `Axis` × 1–2; `Label` × 2–25; `Signal` × 1
**Levels.** A: yes · B: no · C: no

## 019 · `Chart`
Reveal one quantitative trend without distorting its scale or adding decorative geometry.
**Ingredients.** `Axis` × 2; `Node` × 2–7; `Label` × 3–12; `Signal` × 1; `Legend` × 0–1 optional
**Levels.** A: yes · B: no · C: no

## 020 · `Dashboard`
Summarize a small operational state while preserving one clear primary signal.
**Ingredients.** `Pulse` × 1; `Cluster` × 1; `Axis` × 1–2; `Label` × 4–12; `Signal` × 1; `Legend` × 0–1 optional
**Levels.** A: yes · B: no · C: no

`KPI` показує один primary measure. `Table` підтримує exact lookup. `Chart` відкриває один quantitative trend. `Dashboard` збирає small operational state без UI chrome й з одним primary `Signal`.

<!-- page-break -->

<!-- page 21 · source pages/21-recipes-021-023.md -->
# Recipes 021–023 · Pilot-derived extensions

Три recipes зберігають distinct explanatory needs, підтверджені accepted Pilot 01 evidence. Вони не є quota filling.

## 021 · `Breakdown`
Show that an expected recurring system fails to retain continuity and exposes detached consequences.
**Ingredients.** `Loop` × 1; `Node` × 3–5; `Label` × 1–5; `Signal` × 1
**Levels.** A: yes · B: conditional · C: no

## 022 · `Checklist`
Evaluate readiness through a bounded set of required questions with one selected gate.
**Ingredients.** `Anchor` × 1; `Cluster` × 1; `Node` × 3–6; `Signal` × 1; `Label` × 0–6 optional
**Levels.** A: yes · B: conditional · C: no

## 023 · `Formula`
State an exact ordered symbolic relationship and its exact result as one culmination.
**Ingredients.** `Anchor` × 2; `Collision` × 1; `Signal` × 1; `Label` × 0–2 optional
**Levels.** A: no · B: conditional · C: yes

`Breakdown` показує втрату recurrence й detached consequences. `Checklist` оцінює readiness через bounded peer questions. `Formula` завершує серію exact ordered symbolic relationship і result.

Recipe Library навмисно зупиняється на 23 names. Новий recipe потребує нового semantic need і реального usage evidence.

<!-- page-break -->

<!-- page 22 · source pages/22-recipe-selection.md -->
# Як вибирати recipe

Починайте з user question, а не з бажаної форми.

1. Сформулюйте одну main claim.
2. Назвіть task: proposition, comparison, sequence, topology, recurrence, lookup чи quantitative trend.
3. Виберіть recipe, чий `problem` збігається з task.
4. Перевірте allowed scenarios, expression levels і ingredient cardinality.
5. Додайте exact content references.
6. Лише потім збирайте component instances і relations.

## Why / do / don’t

**Why:** recipe стабілізує meaning і review criteria.  
**Do:** обирайте `Architecture` для boundaries, `Workflow` для action sequence.  
**Don’t:** обирайте `Dashboard`, бо хочеться card grid; UI shell не є semantic need.

Якщо жоден із 23 recipes не підходить, зафіксуйте evidence gap. Не винаходьте public name всередині prompt.

<!-- page-break -->

<!-- page 23 · source pages/23-prompt-dsl-anatomy.md -->
# Prompt DSL v0.5 anatomy

`Prompt DSL v0.5` — closed declarative package. Він не описує pixel layout; він відокремлює meaning, exact copy/data, public grammar, generation constraints і provenance.

| Field | Contract |
|---|---|
| `language` | exactly CSDL |
| `version` | exactly 0.5 |
| `kind` | generation-package |
| `id` | stable package identity |
| `recipe` | id, slug, version |
| `semantic_intent` | problem, scenario, main_idea, mechanism |
| `content` | source and exact bindings |
| `component_instances` | D-029 components only |
| `relations` | declared subject, type, object |
| `generation_constraints` | expression through hard exclusions |
| `provenance` | recipe evidence and source outline |

## Ownership

- `semantic_intent` — що треба зрозуміти;
- `content` — що має бути відтворено exact;
- `component_instances` — які public roles беруть участь;
- `relations` — як roles пов’язані;
- `generation_constraints` — expression, canvas, typography, palette, exclusions;
- `provenance` — звідки походять contract і content.

Forbidden layout keys, undeclared components, unsupported relations і placeholders відхиляються. Full analytical data grammar не додається до v0.5; її надає independent `Analytical Mode v0.1`.

<!-- page-break -->

<!-- page 24 · source pages/24-prompt-dsl-example.md -->
# Complete Prompt DSL example

Нижче — complete deterministic generation package з Recipe Library: exact content, grammar і generation constraints.

```yaml
language: CSDL
version: '0.5'
kind: generation-package
id: proof-editorial-big-number
recipe: {id: '004', slug: big-number, version: 0.5.0}
semantic_intent: {main_idea: Three expression levels create one controlled series rhythm., mechanism: big-number-mechanism, problem: Make one exact quantity the dominant explanatory object., scenario: count}
content:
  source: patterns/visual-dna-sprint-01/manifest.yaml#family-04
  bindings: {label: РІВНІ ВИРАЗНОСТІ, supporting_copy: QUIET · CONSTRUCTIVE · SIGNAL, value: '3'}
component_instances:
  - {component: Anchor, content: {binding: value}, id: anchor, role: primary}
  - {attributes: {label: label, value: content.value}, component: Pulse, content: {binding: value}, id: pulse, role: pulse}
  - {attributes: {target: pulse, text: &id001 {binding: value}}, component: Label, content: *id001, id: label, role: label}
  - {attributes: {target: pulse}, component: Signal, content: {binding: value}, id: signal, role: dominant}
relations:
  - {object: pulse, subject: label, type: attached_to}
  - {object: pulse, subject: signal, type: highlights}
generation_constraints:
  expression: A
  density: low
  canvas: {height: 1080, orientation: landscape, ratio: '16:9', safe_margin_horizontal: 96, safe_margin_vertical: 72, width: 1920}
  presentation: {negative_space_percent: {max: 75, min: 50}, one_dominant_signal: true, one_main_idea: true, one_visual_mechanism: true, reading_path: left_to_right}
  typography: {all_text_horizontal: true, body: neutral_sans, code: technical_mono, display: modular_technical, max_typographic_tricks: 1}
  palette: {background: paper.base, ink: ink.primary, mode: light, primary_signal: signal.primary}
  output: {content_accuracy: exact, exact_size: 1920x1080, format: PNG}
  hard_exclusions: [extra text, logos or repeated footers, UI chrome or decorative card shells, decorative coordinates or random dot fields, 'gradients, shadows, glossy surfaces, or 3D', 'political, Soviet, or revolutionary-poster styling', 'pixel, bitmap, dot-matrix, segmented, or retro-computer lettering', extra metric, unsupported statistic, gauge, donut, fake trend, decorative digits, UI chrome, logo, footer, gradients, shadows, 3D, Container or ad hoc layout and geometry primitives]
provenance: {recipe_evidence: specs/004-big-number.md, source_outline: recipes/recipe-library-v0.5/proofs/outlines/01-editorial.yaml}
```

## Review

Перевірте recipe ID, content references, unique component IDs, allowed relations, one dominant `Signal`, exact `1920×1080` output і provenance. No added labels, footer, logo or interface chrome.

<!-- page-break -->

<!-- page 25 · source pages/25-analytical-principles.md -->
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

<!-- page-break -->

<!-- page 26 · source pages/26-analytical-families.md -->
# Analytical families

| Family | Owning precision rule |
|---|---|
| `bar` | preserve declared categorical order |
| `line` | bind x to a temporal or explicitly ordered domain |
| `scatterplot` | bind independent quantitative x and y domains |
| `waterfall` | distinguish start, signed increment, subtotal, and total records |
| `heatmap` | declare matrix identity and fixed row and column order |
| `funnel` | preserve declared stage order |
| `map` | bind every region to a declared geographic identifier |
| `network` | declare unique node and edge identities |
| `table` | preserve exact values and fixed row and column order |
| `dashboard` | require every view to reference one dataset identity and version |

Кожна family має typed source, explicit encoding і deterministic proof. Ten fixed datasets перевіряють positive/negative bars, observed/forecast line with uncertainty, scatterplot, waterfall, heatmap, funnel, normalized map, directed network, exact table і single-dataset dashboard.

Accepted KPI, Table, Chart і Dashboard rasters калібрують presentation restraint. Інші family proofs доводять machine correctness, але не заявляють raster acceptance.

<!-- page-break -->

<!-- page 27 · source pages/27-accessibility-profiles.md -->
# Accessibility profiles

`Night Mode and Accessibility v0.1` maps semantic roles, а не інвертує pixels.

## `light`
Warm-paper accessible mapping; accepted rasters remain unchanged.

## `night`
Warm graphite field with lifted mineral signals; never mechanical inversion.

## `monochrome`
One-channel output with deterministic forms, patterns, and direct labels.

## `projector`
High-margin dark output for ambient-light and low-contrast projection.

## Thresholds

- light / night / monochrome: text ≥ 4.5:1, meaningful non-text ≥ 3:1;
- projector: text ≥ 7:1, meaningful non-text ≥ 4.5:1;
- critical rules: 2 px normally, 3 px for projector at `1920×1080`;
- threshold ratios are exact and never rounded upward.

Night, projector, monochrome і CVD outputs мають deterministic specification evidence. Вони не мають accepted raster calibration без окремого generation/review gate.

<!-- page-break -->

<!-- page 28 · source pages/28-accessibility-meaning.md -->
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

<!-- page-break -->

<!-- page 29 · source pages/29-reference-provenance.md -->
# Reference hierarchy і provenance

Markdown contracts керують meaning; images калібрують visual language. Для Visual DNA діє layered authority:

## Primary visual authority
1. `references/canonical/1.png` — Modular Technical typography, semantic component vocabulary, geometric contrast, and Anchor/Signal construction.
2. `references/canonical/2.png` — Quiet Modular series rhythm, active-space asymmetry, Anchor/Plane/Cluster relationships, and presentation hierarchy.
3. `references/canonical/3.png` — Level A/B/C density, signal scale, palette rhythm, and family continuity.

## Secondary execution reference
- `pilots/01-agentic-discipline/references/style-anchor-light.png` — Direct 16:9 framing, Ukrainian text fidelity, warm paper field, and restrained Quiet spacing.

Якщо quiet execution anchor конфліктує з primary boards у typography, component grammar, asymmetry або expression identity, primary authority перемагає.

## Evidence boundaries

- canonical copy читається з manifests, не з raster text;
- accepted image має provenance, review і SHA-256;
- deterministic proof не стає visual acceptance;
- `provenance.yaml` цієї книги maps every page to owning sources;
- 60 accepted raster hashes перевіряються до й після publication build.

<!-- page-break -->

<!-- page 30 · source pages/30-authoring-workflow.md -->
# Authoring workflow

```text
Content brief
→ Information hierarchy
→ Recipe selection
→ Component sentence
→ Exact content/data
→ Prompt DSL v0.5
→ Approved references
→ Generation or deterministic assembly
→ Text/data/hierarchy review
→ Canonical output or rejected draft
```

## Human + agent parity

Людина визначає claim, evidence і product choice. Agent може deterministic select/build/validate, але не має права розширювати public vocabulary чи вигадувати copy/data.

Для raster work потрібні три candidates, exact-copy review, full-resolution і `1280×720` checks, rubric score та persisted selection evidence. Для цієї книги нові CSDL rasters не генеруються: використовуються canonical examples, deterministic diagrams і clearly labeled comparisons.

<!-- page-break -->

<!-- page 31 · source pages/31-why-do-dont.md -->
# Why / do / don’t

## Why

Semantic ownership робить композицію reviewable. Exact content і provenance роблять її reproducible. Negative space та one-Signal rule роблять її зрозумілою.

## Do

- називайте one main claim до вибору recipe;
- використовуйте component roles для кожного visible element;
- прикріплюйте direct `Label` до exact target;
- зберігайте units, sources, missing states і transformations;
- перевіряйте grayscale, projector і reading order;
- порівнюйте page series як rhythm, а не isolated posters.

## Don’t

- не додавайте decorative geometry, UI chrome, random grids, gradients, shadows або 3D;
- не використовуйте color alone;
- не перекладайте canonical identifiers;
- не маскуйте missing як zero або forecast як observed;
- не називайте synthetic proof accepted raster evidence;
- не робіть license або public-release claims.

<!-- page-break -->

<!-- page 32 · source pages/32-preflight.md -->
# Publishing preflight

Фінальна перевірка з’єднує зміст, visual quality, accessibility, provenance і governance в один release-independent gate.

## Content

- [ ] one main idea, one mechanism, one dominant `Signal` per screen/example;
- [ ] Ukrainian editorial content complete; English identifiers exact;
- [ ] all references resolve and claim class is honest;
- [ ] exact copy/data, units, sources, missing states, forecast and uncertainty preserved.

## Visual and accessibility

- [ ] full-size pages and contact sheet reviewed;
- [ ] no clipping, overflow, missing glyphs or broken reading order;
- [ ] contrast thresholds and color-independent carriers pass;
- [ ] grayscale and projector behavior remain interpretable;
- [ ] accepted rasters embedded without mutation.

## Build and governance

- [ ] page count is 25–40 and order matches manifest;
- [ ] build runs twice with identical hashes;
- [ ] tests, Milestone 1–7 validators and CI pass;
- [ ] generated files are not hand-edited; `git diff --exit-code` passes;
- [ ] license, tags, GitHub Releases, Milestone 8 and public-release claims remain untouched.
