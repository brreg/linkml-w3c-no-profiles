

# Slot: utgivelsesdato 


_Dato ressursen ble første gang publisert._





URI: [dct:issued](http://purl.org/dc/terms/issued)
Alias: utgivelsesdato

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  yes  |
| [Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Katalogpost](Katalogpost.md) | En katalogpost som beskriver en ressurs i katalogen |  yes  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Katalogpost](Katalogpost.md), [Katalog](Katalog.md) |
| Slot URI | [dct:issued](http://purl.org/dc/terms/issued) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:issued |
| native | https://data.norge.no/linkml/dcat-ap-no/utgivelsesdato |




## LinkML Source

<details>
```yaml
name: utgivelsesdato
description: Dato ressursen ble første gang publisert.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:issued
alias: utgivelsesdato
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Katalogpost
- Katalog
range: date

```
</details>