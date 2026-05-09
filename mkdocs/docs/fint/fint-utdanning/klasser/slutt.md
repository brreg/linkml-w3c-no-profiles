

# Slot: slutt 


_Til tidspunkt._





URI: [fint:slutt](https://schema.fintlabs.no/slutt)
Alias: slutt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datetime](datetime.md) |
| Domain Of | [Periode](periode.md) |
| Slot URI | [fint:slutt](https://schema.fintlabs.no/slutt) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:slutt |
| native | https://schema.fintlabs.no/utdanning/:slutt |




## LinkML Source

<details>
```yaml
name: slutt
description: Til tidspunkt.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:slutt
alias: slutt
domain_of:
- Periode
range: datetime

```
</details>