

# Slot: kontaktpunkt 


_Kontaktinformasjon for henvendelser om ressursen._





URI: [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)
Alias: kontaktpunkt

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
| Range | [Kontaktopplysning](Kontaktopplysning.md) |
| Domain Of | [Datasett](Datasett.md), [Datasettserie](Datasettserie.md), [Datatjeneste](Datatjeneste.md), [Katalog](Katalog.md) |
| Slot URI | [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint) |

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
| self | dcat:contactPoint |
| native | https://data.norge.no/linkml/dcat-ap-no/kontaktpunkt |




## LinkML Source

<details>
```yaml
name: kontaktpunkt
description: Kontaktinformasjon for henvendelser om ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:contactPoint
alias: kontaktpunkt
domain_of:
- Datasett
- Datasettserie
- Datatjeneste
- Katalog
range: Kontaktopplysning
multivalued: true

```
</details>