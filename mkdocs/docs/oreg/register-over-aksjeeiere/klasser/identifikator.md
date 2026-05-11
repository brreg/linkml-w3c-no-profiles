

# Slot: identifikator 


_Global identifikator for instansen._





URI: [aksje:identifikator](https://example.no/ontology/aksje#identifikator)
Alias: identifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aksjeinnskudd](aksjeinnskudd.md) | Innskot knytt til aksjar i samband med selskapshending |  no  |
| [Aksjeklasse](aksjeklasse.md) | Klasse aksjar høyrer til, med eigne rettigheiter |  no  |
| [Containerklasse](containerklasse.md) | Containerklasse for alle forretningsobjekt i modellen |  no  |
| [Aksje](aksje.md) | Ei enkelt aksje utstedt av eit aksjeselskap |  no  |
| [Utbytte](utbytte.md) | Utbytte knytt til ein eigarposisjon |  no  |
| [Aksjeselskap](aksjeselskap.md) | Selskap som utsteder aksjar og har aksjekapital |  no  |
| [Aksjekapital](aksjekapital.md) | Den registrerte aksjekapitalen i eit aksjeselskap |  no  |
| [Vederlag](vederlag.md) | Vederlag knytt til ei aksjeoverdraging |  no  |
| [Eierposisjon](eierposisjon.md) | Eierens samla posisjon i eit selskap |  no  |
| [Aksjeeierrettighet](aksjeeierrettighet.md) | Rettigheiter knytt til aksjar, til dømes stemmerett |  no  |
| [Aksjeoverdragelse](aksjeoverdragelse.md) | Overdraging av aksjar mellom partar |  no  |
| [Aksjeeier](aksjeeier.md) | Person eller organisasjon som eig aksjar |  no  |
| [Eierskapstransaksjon](eierskapstransaksjon.md) | Transaksjon som påverkar eigarskap i selskapet |  no  |
| [Selskapshendelse](selskapshendelse.md) | Hending som påverkar selskapet sitt eigarskap eller kapital |  no  |
| [Utdeling](utdeling.md) | Konkret utdeling av verdiar til aksjeeigarar |  no  |
| [Aksjepost](aksjepost.md) | Samling aksjar eigd av ein aksjeeigar |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Containerklasse](containerklasse.md), [Aksjeselskap](aksjeselskap.md), [Aksjekapital](aksjekapital.md), [Aksje](aksje.md), [Aksjeklasse](aksjeklasse.md), [Aksjeeierrettighet](aksjeeierrettighet.md), [Aksjeeier](aksjeeier.md), [Eierposisjon](eierposisjon.md), [Aksjepost](aksjepost.md), [Utbytte](utbytte.md), [Utdeling](utdeling.md), [Eierskapstransaksjon](eierskapstransaksjon.md), [Aksjeoverdragelse](aksjeoverdragelse.md), [Vederlag](vederlag.md), [Selskapshendelse](selskapshendelse.md), [Aksjeinnskudd](aksjeinnskudd.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/aksje-eierskap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aksje:identifikator |
| native | aksje:identifikator |




## LinkML Source

<details>
```yaml
name: identifikator
description: Global identifikator for instansen.
from_schema: https://example.no/ontology/aksje-eierskap
rank: 1000
identifier: true
alias: identifikator
domain_of:
- Containerklasse
- Aksjeselskap
- Aksjekapital
- Aksje
- Aksjeklasse
- Aksjeeierrettighet
- Aksjeeier
- Eierposisjon
- Aksjepost
- Utbytte
- Utdeling
- Eierskapstransaksjon
- Aksjeoverdragelse
- Vederlag
- Selskapshendelse
- Aksjeinnskudd
range: uriorcurie
required: true

```
</details>