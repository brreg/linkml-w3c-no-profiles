

# Slot: tittel 


_Navn/tittel på ressursen._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  yes  |
| [Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  yes  |
| [Katalogpost](Katalogpost.md) | En katalogpost som beskriver en ressurs i katalogen |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  yes  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalogpost](Katalogpost.md), [Katalog](Katalog.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

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
| self | dct:title |
| native | https://data.norge.no/linkml/dcat-ap-no/tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Navn/tittel på ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:title
alias: tittel
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Datatjeneste
- Katalogpost
- Katalog
range: LangString
multivalued: true

```
</details>