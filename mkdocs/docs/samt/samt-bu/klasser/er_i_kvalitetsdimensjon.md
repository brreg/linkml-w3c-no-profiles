

# Slot: er_i_kvalitetsdimensjon 


_Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld._

__





URI: [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension)
Alias: er_i_kvalitetsdimensjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  yes  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kvalitetsdimensjon](kvalitetsdimensjon.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md), [Standard](standard.md) |
| Slot URI | [dqv:inDimension](http://www.w3.org/ns/dqv#inDimension) |

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
| self | dqv:inDimension |
| native | samtbuskole:er_i_kvalitetsdimensjon |




## LinkML Source

<details>
```yaml
name: er_i_kvalitetsdimensjon
description: 'Refererer til kvalitetsdimensjon(ar) som kvalitetsmerknaden gjeld.

  '
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dqv:inDimension
alias: er_i_kvalitetsdimensjon
domain_of:
- Kvalitetsmerknad
- Standard
range: Kvalitetsdimensjon
required: false
multivalued: true

```
</details>