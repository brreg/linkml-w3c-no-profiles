

# Slot: kommune 


_Referanse til kommunen OT-eininga dekker._





URI: [utd:kommune](https://schema.fintlabs.no/utdanning/kommune)
Alias: kommune

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  yes  |
| [Person](person.md) | Fysiske private personar |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [OtEnhet](otenhet.md), [Fylke](fylke.md), [Person](person.md) |
| Slot URI | [utd:kommune](https://schema.fintlabs.no/utdanning/kommune) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:kommune |
| native | https://schema.fintlabs.no/utdanning/:kommune |




## LinkML Source

<details>
```yaml
name: kommune
description: Referanse til kommunen OT-eininga dekker.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:kommune
alias: kommune
domain_of:
- OtEnhet
- Fylke
- Person
range: uriorcurie

```
</details>