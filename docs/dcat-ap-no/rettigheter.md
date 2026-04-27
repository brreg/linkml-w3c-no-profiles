

# Slot: rettigheter 


_Rettigheter knyttet til ressursen._





URI: [dct:rights](http://purl.org/dc/terms/rights)
Alias: rettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  no  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighetserklaring](Rettighetserklaring.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
| Slot URI | [dct:rights](http://purl.org/dc/terms/rights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:rights |
| native | https://data.norge.no/linkml/dcat-ap-no/rettigheter |




## LinkML Source

<details>
```yaml
name: rettigheter
description: Rettigheter knyttet til ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:rights
alias: rettigheter
domain_of:
- Distribusjon
- Datatjeneste
- Katalog
range: Rettighetserklaring

```
</details>