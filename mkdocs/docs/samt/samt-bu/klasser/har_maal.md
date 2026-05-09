

# Slot: har_maal 


_Ressursen merknaden gjeld._





URI: [oa:hasTarget](http://www.w3.org/ns/oa#hasTarget)
Alias: har_maal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](uri.md) |
| Domain Of | [Kvalitetsmerknad](kvalitetsmerknad.md) |
| Slot URI | [oa:hasTarget](http://www.w3.org/ns/oa#hasTarget) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| gyldige_verdier | dcat:Resource |




### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:hasTarget |
| native | samtbuskole:har_maal |




## LinkML Source

<details>
```yaml
name: har_maal
annotations:
  gyldige_verdier:
    tag: gyldige_verdier
    value: dcat:Resource
description: Ressursen merknaden gjeld.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: oa:hasTarget
alias: har_maal
domain_of:
- Kvalitetsmerknad
range: uri

```
</details>