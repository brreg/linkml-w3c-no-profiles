

# Slot: datasettdistribusjon 


_Tilgjengelige distribusjoner av datasettet._





URI: [dcat:distribution](http://www.w3.org/ns/dcat#distribution)
Alias: datasettdistribusjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Distribusjon](Distribusjon.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [dcat:distribution](http://www.w3.org/ns/dcat#distribution) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:distribution |
| native | https://data.norge.no/linkml/dcat-ap-no/datasettdistribusjon |




## LinkML Source

<details>
```yaml
name: datasettdistribusjon
description: Tilgjengelige distribusjoner av datasettet.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:distribution
alias: datasettdistribusjon
domain_of:
- Datasett
range: Distribusjon
multivalued: true

```
</details>