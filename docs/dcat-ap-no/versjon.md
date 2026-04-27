

# Slot: versjon 


_Versjonsnummer._





URI: [dcat:version](http://www.w3.org/ns/dcat#version)
Alias: versjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |
| [Standard](Standard.md) | En standard som en ressurs er i samsvar med |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Standard](Standard.md), [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [dcat:version](http://www.w3.org/ns/dcat#version) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:version |
| native | https://data.norge.no/linkml/dcat-ap-no/versjon |




## LinkML Source

<details>
```yaml
name: versjon
description: Versjonsnummer.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dcat:version
alias: versjon
domain_of:
- Standard
- Datasett
- Datatjeneste
range: string

```
</details>