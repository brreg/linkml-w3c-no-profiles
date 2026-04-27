

# Slot: dokumentasjon 


_Lenke til dokumentasjon om ressursen._





URI: [foaf:page](http://xmlns.com/foaf/0.1/page)
Alias: dokumentasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gebyr](Gebyr.md) | Et gebyr knyttet til bruk av en datatjeneste |  no  |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [Gebyr](Gebyr.md), [Distribusjon](Distribusjon.md), [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [foaf:page](http://xmlns.com/foaf/0.1/page) |

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
| self | foaf:page |
| native | https://data.norge.no/linkml/dcat-ap-no/dokumentasjon |




## LinkML Source

<details>
```yaml
name: dokumentasjon
description: Lenke til dokumentasjon om ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: foaf:page
alias: dokumentasjon
domain_of:
- Gebyr
- Distribusjon
- Datasett
- Datatjeneste
range: uri
multivalued: true

```
</details>