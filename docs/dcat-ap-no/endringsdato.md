

# Slot: endringsdato 


_Dato for siste endring av ressursen._





URI: [dct:modified](http://purl.org/dc/terms/modified)
Alias: endringsdato

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
| Slot URI | [dct:modified](http://purl.org/dc/terms/modified) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:modified |
| native | https://data.norge.no/linkml/dcat-ap-no/endringsdato |




## LinkML Source

<details>
```yaml
name: endringsdato
description: Dato for siste endring av ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:modified
alias: endringsdato
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Katalogpost
- Katalog
range: date

```
</details>