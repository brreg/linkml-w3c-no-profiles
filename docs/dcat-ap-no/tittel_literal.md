

# Slot: tittel_literal 


_Navn/tittel uten språktag._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel_literal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](RegulativRessurs.md) | En regulativ ressurs (lov, forskrift e |  no  |
| [Standard](Standard.md) | En standard som en ressurs er i samsvar med |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Standard](Standard.md), [RegulativRessurs](RegulativRessurs.md) |
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
| native | https://data.norge.no/linkml/dcat-ap-no/tittel_literal |




## LinkML Source

<details>
```yaml
name: tittel_literal
description: Navn/tittel uten språktag.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: dct:title
alias: tittel_literal
domain_of:
- Standard
- RegulativRessurs
range: string
multivalued: true

```
</details>