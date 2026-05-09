

# Slot: person 


_Referanse til Person (Administrasjon)._





URI: [pvn:person](https://schema.fintlabs.no/personvern/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Samtykke](samtykke.md) | Tillating til behandling av personopplysning |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Samtykke](samtykke.md) |
| Slot URI | [pvn:person](https://schema.fintlabs.no/personvern/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:person |
| native | https://schema.fintlabs.no/personvern/:person |




## LinkML Source

<details>
```yaml
name: person
description: Referanse til Person (Administrasjon).
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:person
alias: person
domain_of:
- Samtykke
range: uriorcurie

```
</details>