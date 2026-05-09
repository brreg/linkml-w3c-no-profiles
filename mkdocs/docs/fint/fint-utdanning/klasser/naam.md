

# Slot: naam 


_Hovudnamn for ressursen._





URI: [fint:naam](https://schema.fintlabs.no/naam)
Alias: naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Begrep](begrep.md) |
| Slot URI | [fint:naam](https://schema.fintlabs.no/naam) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:naam |
| native | https://schema.fintlabs.no/utdanning/:naam |




## LinkML Source

<details>
```yaml
name: naam
description: Hovudnamn for ressursen.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:naam
alias: naam
domain_of:
- Begrep
range: string

```
</details>