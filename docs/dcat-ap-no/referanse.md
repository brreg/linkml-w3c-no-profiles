

# Slot: referanse 


_Referanse til ekstern ressurs._





URI: [rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso)
Alias: referanse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RegulativRessurs](RegulativRessurs.md) | En regulativ ressurs (lov, forskrift e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](Uri.md) |
| Domain Of | [RegulativRessurs](RegulativRessurs.md) |
| Slot URI | [rdfs:seeAlso](http://www.w3.org/2000/01/rdf-schema#seeAlso) |

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
| self | rdfs:seeAlso |
| native | https://data.norge.no/linkml/dcat-ap-no/referanse |




## LinkML Source

<details>
```yaml
name: referanse
description: Referanse til ekstern ressurs.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: rdfs:seeAlso
alias: referanse
domain_of:
- RegulativRessurs
range: uri
multivalued: true

```
</details>