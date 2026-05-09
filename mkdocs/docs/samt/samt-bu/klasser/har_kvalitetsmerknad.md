

# Slot: har_kvalitetsmerknad 


_Kvalitetsmerknad knytt til datasettet._





URI: [dqv:hasQualityAnnotation](http://www.w3.org/ns/dqv#hasQualityAnnotation)
Alias: har_kvalitetsmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Domain Of | [Datasett](datasett.md) |
| Slot URI | [dqv:hasQualityAnnotation](http://www.w3.org/ns/dqv#hasQualityAnnotation) |

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
| self | dqv:hasQualityAnnotation |
| native | samtbuskole:har_kvalitetsmerknad |




## LinkML Source

<details>
```yaml
name: har_kvalitetsmerknad
description: Kvalitetsmerknad knytt til datasettet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dqv:hasQualityAnnotation
alias: har_kvalitetsmerknad
domain_of:
- Datasett
range: Kvalitetsmerknad
multivalued: true

```
</details>