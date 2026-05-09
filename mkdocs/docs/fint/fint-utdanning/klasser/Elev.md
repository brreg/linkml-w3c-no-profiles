

# Slot: elev 


_Eleven dette gjeld._





URI: [utd:elev](https://schema.fintlabs.no/utdanning/elev)
Alias: elev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |  yes  |
| [Person](person.md) | Fysiske private personar |  yes  |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |  yes  |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Elev](elev.md) |
| Domain Of | [Elevforhold](elevforhold.md), [Elevtilrettelegging](elevtilrettelegging.md), [Persongruppe](persongruppe.md), [Person](person.md) |
| Slot URI | [utd:elev](https://schema.fintlabs.no/utdanning/elev) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:elev |
| native | https://schema.fintlabs.no/utdanning/:elev |




## LinkML Source

<details>
```yaml
name: elev
description: Eleven dette gjeld.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:elev
alias: elev
domain_of:
- Elevforhold
- Elevtilrettelegging
- Persongruppe
- Person
range: Elev

```
</details>