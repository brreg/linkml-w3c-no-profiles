

# Slot: kilde_datasett 


_Datasett som dette datasettet er avledet fra._





URI: [dct:source](http://purl.org/dc/terms/source)
Alias: kilde_datasett

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Datasett](Datasett.md) |
| Domain Of | [Datasett](Datasett.md) |
| Slot URI | [dct:source](http://purl.org/dc/terms/source) |

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
| self | dct:source |
| native | https://data.norge.no/linkml/dcat-ap-no/kilde_datasett |




## LinkML Source

<details>
```yaml
name: kilde_datasett
description: Datasett som dette datasettet er avledet fra.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:source
alias: kilde_datasett
domain_of:
- Datasett
range: Datasett
multivalued: true

```
</details>