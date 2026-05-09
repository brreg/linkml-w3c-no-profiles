

# Slot: person_naam 


_Namn på personen._





URI: [fint:personNavn](https://schema.fintlabs.no/personNavn)
Alias: person_naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
| Domain Of | [Person](person.md) |
| Slot URI | [fint:personNavn](https://schema.fintlabs.no/personNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:personNavn |
| native | https://schema.fintlabs.no/utdanning/:person_naam |




## LinkML Source

<details>
```yaml
name: person_naam
description: Namn på personen.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:personNavn
alias: person_naam
domain_of:
- Person
range: Personnavn
inlined: true

```
</details>