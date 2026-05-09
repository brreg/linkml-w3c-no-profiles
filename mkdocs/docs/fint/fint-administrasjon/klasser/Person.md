

# Slot: person 


_Person som er ein personalressurs._





URI: [adm:person](https://schema.fintlabs.no/administrasjon/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](person.md) |
| Domain Of | [Personalressurs](personalressurs.md) |
| Slot URI | [adm:person](https://schema.fintlabs.no/administrasjon/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:person |
| native | https://schema.fintlabs.no/administrasjon/:person |




## LinkML Source

<details>
```yaml
name: person
description: Person som er ein personalressurs.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:person
alias: person
domain_of:
- Personalressurs
range: Person

```
</details>