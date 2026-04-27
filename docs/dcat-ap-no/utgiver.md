

# Slot: utgiver 


_Aktøren som er ansvarlig for å tilgjengeliggjøre ressursen._





URI: [dct:publisher](http://purl.org/dc/terms/publisher)
Alias: utgiver

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  yes  |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  yes  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  yes  |
| [Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Aktor](Aktor.md) |
| Domain Of | [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
| Slot URI | [dct:publisher](http://purl.org/dc/terms/publisher) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:publisher |
| native | https://data.norge.no/linkml/dcat-ap-no/utgiver |




## LinkML Source

<details>
```yaml
name: utgiver
description: Aktøren som er ansvarlig for å tilgjengeliggjøre ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:publisher
alias: utgiver
domain_of:
- Datasett
- Datasettserie
- Datatjeneste
- Katalog
range: Aktor

```
</details>