

# Slot: tilgangsrettigheter 


_Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang eller ikke-allmenn tilgang til datasettet._





URI: [dct:accessRights](http://purl.org/dc/terms/accessRights)
Alias: tilgangsrettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Datasett](datasett.md), [Datatjeneste](datatjeneste.md) |
| Slot URI | [dct:accessRights](http://purl.org/dc/terms/accessRights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accessRights |
| native | samtbuskole:tilgangsrettigheter |




## LinkML Source

<details>
```yaml
name: tilgangsrettigheter
description: Egenskapen brukes til å angi om det er allmenn tilgang, betinget tilgang
  eller ikke-allmenn tilgang til datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:accessRights
alias: tilgangsrettigheter
domain_of:
- Datasett
- Datatjeneste
range: uri
multivalued: true

```
</details>