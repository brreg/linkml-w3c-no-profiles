

# Slot: etternavn 


_Etternamn til personen._





URI: [fint:etternavn](https://schema.fintlabs.no/etternavn)
Alias: etternavn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Personnavn](personnavn.md) | Namn på ein person |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Personnavn](personnavn.md) |
| Slot URI | [fint:etternavn](https://schema.fintlabs.no/etternavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:etternavn |
| native | https://schema.fintlabs.no/utdanning/:etternavn |




## LinkML Source

<details>
```yaml
name: etternavn
description: Etternamn til personen.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:etternavn
alias: etternavn
domain_of:
- Personnavn
range: string

```
</details>