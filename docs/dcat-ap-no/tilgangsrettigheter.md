

# Slot: tilgangsrettigheter 


_Tilgangsrettigheter for ressursen._





URI: [dct:accessRights](http://purl.org/dc/terms/accessRights)
Alias: tilgangsrettigheter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Rettighetserklaring](Rettighetserklaring.md) |
| Domain Of | [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dct:accessRights](http://purl.org/dc/terms/accessRights) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:accessRights |
| native | https://data.norge.no/linkml/dcat-ap-no/tilgangsrettigheter |




## LinkML Source

<details>
```yaml
name: tilgangsrettigheter
description: Tilgangsrettigheter for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:accessRights
alias: tilgangsrettigheter
domain_of:
- Datasett
- Datatjeneste
range: Rettighetserklaring

```
</details>