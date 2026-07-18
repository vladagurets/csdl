---
id: '15'
title_uk: Relations і semantic geometry
editorial_language: uk
terminology_language: en
---
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
