

# Slot: tidsrom 


_Tidsperiode ressursen dekker._





URI: [dct:temporal](http://purl.org/dc/terms/temporal)
Alias: tidsrom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) | Rotklasse for DCAT-AP-NO-datafiler |  no  |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  yes  |
| [Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Tidsrom](Tidsrom.md) |
| Domain Of | [Container](Container.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Katalog](Katalog.md) |
| Slot URI | [dct:temporal](http://purl.org/dc/terms/temporal) |

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
| self | dct:temporal |
| native | https://data.norge.no/linkml/dcat-ap-no/tidsrom |




## LinkML Source

<details>
```yaml
name: tidsrom
description: Tidsperiode ressursen dekker.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:temporal
alias: tidsrom
domain_of:
- Container
- Datasett
- Datasettserie
- Katalog
range: Tidsrom
multivalued: true

```
</details>