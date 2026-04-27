

# Slot: produsent 


_Aktøren som primært har skapt ressursen._





URI: [dct:creator](http://purl.org/dc/terms/creator)
Alias: produsent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktor](Aktor.md) |
| Domain Of | [Datasett](Datasett.md), [Katalog](Katalog.md) |
| Slot URI | [dct:creator](http://purl.org/dc/terms/creator) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:creator |
| native | https://data.norge.no/linkml/dcat-ap-no/produsent |




## LinkML Source

<details>
```yaml
name: produsent
description: Aktøren som primært har skapt ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:creator
alias: produsent
domain_of:
- Datasett
- Katalog
range: Aktor

```
</details>