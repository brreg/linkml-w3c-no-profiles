

# Slot: type_concept 


_Type ressurs fra et kontrollert vokabular._





URI: [dct:type](http://purl.org/dc/terms/type)
Alias: type_concept

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |
| [RegulativRessurs](RegulativRessurs.md) | En regulativ ressurs (lov, forskrift e |  no  |
| [Aktor](Aktor.md) | En aktør (person, organisasjon eller system) med ansvar for en ressurs |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Aktor](Aktor.md), [RegulativRessurs](RegulativRessurs.md), [Datasett](Datasett.md) |
| Slot URI | [dct:type](http://purl.org/dc/terms/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:type |
| native | https://data.norge.no/linkml/dcat-ap-no/type_concept |




## LinkML Source

<details>
```yaml
name: type_concept
description: Type ressurs fra et kontrollert vokabular.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:type
alias: type_concept
domain_of:
- Aktor
- RegulativRessurs
- Datasett
range: Begrep

```
</details>