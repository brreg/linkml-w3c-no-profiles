

# Slot: fravaerstimer 


_Antal fråværstimar._





URI: [utd:fravaerstimer](https://schema.fintlabs.no/utdanning/fravaerstimer)
Alias: fravaerstimer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fravarsprosent](fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](integer.md) |
| Domain Of | [Fravarsprosent](fravarsprosent.md) |
| Slot URI | [utd:fravaerstimer](https://schema.fintlabs.no/utdanning/fravaerstimer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:fravaerstimer |
| native | https://schema.fintlabs.no/utdanning/:fravaerstimer |




## LinkML Source

<details>
```yaml
name: fravaerstimer
description: Antal fråværstimar.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:fravaerstimer
alias: fravaerstimer
domain_of:
- Fravarsprosent
range: integer

```
</details>