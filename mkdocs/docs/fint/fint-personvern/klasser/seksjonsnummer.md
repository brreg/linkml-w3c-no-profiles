

# Slot: seksjonsnummer 


_Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer._





URI: [fint:seksjonsnummer](https://schema.fintlabs.no/seksjonsnummer)
Alias: seksjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Matrikkelnummer](matrikkelnummer.md) |
| Slot URI | [fint:seksjonsnummer](https://schema.fintlabs.no/seksjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:seksjonsnummer |
| native | https://schema.fintlabs.no/personvern/:seksjonsnummer |




## LinkML Source

<details>
```yaml
name: seksjonsnummer
description: Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: fint:seksjonsnummer
alias: seksjonsnummer
domain_of:
- Matrikkelnummer
range: string

```
</details>