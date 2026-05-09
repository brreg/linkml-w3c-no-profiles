

# Slot: kontaktperson_naam 


_Namn på kontaktpersonen._





URI: [fint:kontaktpersonNavn](https://schema.fintlabs.no/kontaktpersonNavn)
Alias: kontaktperson_naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Personnavn](personnavn.md) |
| Domain Of | [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:kontaktpersonNavn](https://schema.fintlabs.no/kontaktpersonNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktpersonNavn |
| native | https://schema.fintlabs.no/arkiv/:kontaktperson_naam |




## LinkML Source

<details>
```yaml
name: kontaktperson_naam
description: Namn på kontaktpersonen.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:kontaktpersonNavn
alias: kontaktperson_naam
domain_of:
- Kontaktperson
range: Personnavn
inlined: true

```
</details>