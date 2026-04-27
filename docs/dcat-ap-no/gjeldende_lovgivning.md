

# Slot: gjeldende_lovgivning 


_Lovgivning som gjelder for ressursen._





URI: [dcatap:applicableLegislation](http://data.europa.eu/r5r/applicableLegislation)
Alias: gjeldende_lovgivning

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  no  |
| [Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |  yes  |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  yes  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  yes  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulativRessurs](RegulativRessurs.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
| Slot URI | [dcatap:applicableLegislation](http://data.europa.eu/r5r/applicableLegislation) |

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
| self | dcatap:applicableLegislation |
| native | https://data.norge.no/linkml/dcat-ap-no/gjeldende_lovgivning |




## LinkML Source

<details>
```yaml
name: gjeldende_lovgivning
description: Lovgivning som gjelder for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcatap:applicableLegislation
alias: gjeldende_lovgivning
domain_of:
- Distribusjon
- Datasett
- Datasettserie
- Datatjeneste
- Katalog
range: RegulativRessurs
multivalued: true

```
</details>