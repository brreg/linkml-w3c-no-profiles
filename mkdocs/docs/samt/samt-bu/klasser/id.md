

# Slot: id 


_URI-identifikator for ressursen._





URI: [samtbuskole:id](https://example.no/ontology/skole#id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  no  |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  no  |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  no  |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |  no  |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  no  |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  no  |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Spraak](spraak.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md), [KatalogisertRessurs](katalogisertressurs.md), [Aktor](aktor.md), [Kontaktopplysning](kontaktopplysning.md), [Tidsrom](tidsrom.md), [RegulativRessurs](regulativressurs.md), [Identifikator](identifikator.md), [Rettighetserklaring](rettighetserklaring.md), [Sjekksum](sjekksum.md), [Gebyr](gebyr.md), [Relasjon](relasjon.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Katalogpost](katalogpost.md), [Kvalitetsdimensjon](kvalitetsdimensjon.md), [Kvalitetsmaal](kvalitetsmaal.md), [Kvalitetsmerknad](kvalitetsmerknad.md), [Kvalitetsmaaling](kvalitetsmaaling.md), [Standard](standard.md), [Tekstdel](tekstdel.md) |

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


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:id |
| native | samtbuskole:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
identifier: true
alias: id
domain_of:
- Spraak
- Mediatype
- Konsept
- Begrepssamling
- KatalogisertRessurs
- Aktor
- Kontaktopplysning
- Tidsrom
- RegulativRessurs
- Identifikator
- Rettighetserklaring
- Sjekksum
- Gebyr
- Relasjon
- Distribusjon
- Datasett
- Katalogpost
- Kvalitetsdimensjon
- Kvalitetsmaal
- Kvalitetsmerknad
- Kvalitetsmaaling
- Standard
- Tekstdel
range: uriorcurie
required: true

```
</details>