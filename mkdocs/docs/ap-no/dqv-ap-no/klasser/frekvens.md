

# Slot: frekvens 


_Oppdateringsfrekvens for datasettet._





URI: [dct:accrualPeriodicity](http://purl.org/dc/terms/accrualPeriodicity)
Alias: frekvens

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Datasettserie](datasettserie.md) |
| Slot URI | [dct:accrualPeriodicity](http://purl.org/dc/terms/accrualPeriodicity) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | dct:Frequency |




### Schema Source


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accrualPeriodicity |
| native | https://data.norge.no/linkml/dqv-ap-no/frekvens |




## LinkML Source

<details>
```yaml
name: frekvens
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: dct:Frequency
description: Oppdateringsfrekvens for datasettet.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
slot_uri: dct:accrualPeriodicity
alias: frekvens
domain_of:
- Datasettserie
range: string

```
</details>