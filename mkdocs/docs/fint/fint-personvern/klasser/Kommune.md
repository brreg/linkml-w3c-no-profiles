

# Slot: kommune 


_Kommune._





URI: [fint:kommune](https://schema.fintlabs.no/kommune)
Alias: kommune

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kommune](kommune.md) |
| Domain Of | [Fylke](fylke.md), [Person](person.md) |
| Slot URI | [fint:kommune](https://schema.fintlabs.no/kommune) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kommune |
| native | https://schema.fintlabs.no/personvern/:kommune |




## LinkML Source

<details>
```yaml
name: kommune
description: Kommune.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:kommune
alias: kommune
domain_of:
- Fylke
- Person
range: Kommune

```
</details>