

# Slot: person 


_Referanse til Person (Administrasjon)._





URI: [okn:person](https://schema.fintlabs.no/okonomi/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fakturamottaker](fakturamottaker.md) | Aktør som skal betale faktura (kompleks datatype) |  yes  |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Fakturamottaker](fakturamottaker.md), [Leverandor](leverandor.md) |
| Slot URI | [okn:person](https://schema.fintlabs.no/okonomi/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:person |
| native | https://schema.fintlabs.no/okonomi/:person |




## LinkML Source

<details>
```yaml
name: person
description: Referanse til Person (Administrasjon).
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:person
alias: person
domain_of:
- Fakturamottaker
- Leverandor
range: uriorcurie

```
</details>