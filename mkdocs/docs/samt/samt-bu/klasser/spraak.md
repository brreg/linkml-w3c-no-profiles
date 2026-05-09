

# Slot: spraak 


_Språk brukt i ressursen (dct:language)._





URI: [dct:language](http://purl.org/dc/terms/language)
Alias: spraak

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  yes  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [RegulativRessurs](regulativressurs.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Katalogpost](katalogpost.md), [Katalog](katalog.md), [Tekstdel](tekstdel.md) |
| Slot URI | [dct:language](http://purl.org/dc/terms/language) |

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
| self | dct:language |
| native | samtbuskole:spraak |




## LinkML Source

<details>
```yaml
name: spraak
description: Språk brukt i ressursen (dct:language).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
slot_uri: dct:language
alias: spraak
domain_of:
- RegulativRessurs
- Distribusjon
- Datasett
- Katalogpost
- Katalog
- Tekstdel
range: string
multivalued: true

```
</details>