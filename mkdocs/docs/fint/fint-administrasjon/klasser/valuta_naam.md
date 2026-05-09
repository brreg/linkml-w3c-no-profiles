

# Slot: valuta_naam 


_Namn på valuta._





URI: [fint:valutaNavn](https://schema.fintlabs.no/valutaNavn)
Alias: valuta_naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Valuta](valuta.md) |
| Slot URI | [fint:valutaNavn](https://schema.fintlabs.no/valutaNavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:valutaNavn |
| native | https://schema.fintlabs.no/administrasjon/:valuta_naam |




## LinkML Source

<details>
```yaml
name: valuta_naam
description: Namn på valuta.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:valutaNavn
alias: valuta_naam
domain_of:
- Valuta
range: string

```
</details>