

# Slot: kjonn 


_Kjønn._





URI: [fint:kjonn](https://schema.fintlabs.no/kjonn)
Alias: kjonn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |  yes  |
| [Person](person.md) | Fysiske private personar |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kjonn](kjonn.md) |
| Domain Of | [AdministrasjonContainer](administrasjoncontainer.md), [Person](person.md) |
| Slot URI | [fint:kjonn](https://schema.fintlabs.no/kjonn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kjonn |
| native | https://schema.fintlabs.no/administrasjon/:kjonn |




## LinkML Source

<details>
```yaml
name: kjonn
description: Kjønn.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:kjonn
alias: kjonn
domain_of:
- AdministrasjonContainer
- Person
range: Kjonn

```
</details>