

# Slot: har_definisjon 


_Definisjon av dimensjonen eller målet._





URI: [skos:definition](http://www.w3.org/2004/02/skos/core#definition)
Alias: har_definisjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  yes  |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  yes  |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Kvalitetsdimensjon](kvalitetsdimensjon.md), [Kvalitetsmaal](kvalitetsmaal.md) |
| Slot URI | [skos:definition](http://www.w3.org/2004/02/skos/core#definition) |

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
| self | skos:definition |
| native | samtbuskole:har_definisjon |




## LinkML Source

<details>
```yaml
name: har_definisjon
description: Definisjon av dimensjonen eller målet.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: skos:definition
alias: har_definisjon
domain_of:
- Kvalitetsdimensjon
- Kvalitetsmaal
range: LangString
multivalued: true

```
</details>