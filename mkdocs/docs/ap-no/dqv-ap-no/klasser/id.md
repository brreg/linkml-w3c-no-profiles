

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/dqv-ap-no/id](https://data.norge.no/linkml/dqv-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [Kvalitetsmaaling](kvalitetsmaaling.md) | Ei konkret måling av eit kvalitetsmål for eit datasett |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Standard](standard.md) | Ein standard eller spesifikasjon som eit datasett er i samsvar med |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Kvalitetsdeldimensjon](kvalitetsdeldimensjon.md) | Ein deldimensjon av ein kvalitetsdimensjon |  no  |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Kvalitetsmaal](kvalitetsmaal.md) | Eit kvalitetsmål som operasjonaliserer ein kvalitetsdeldimensjon |  no  |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [Brukartilbakemelding](brukartilbakemelding.md) | Tilbakemelding frå ein brukar om kvaliteten til eit datasett |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Kvalitetssertifikat](kvalitetssertifikat.md) | Eit sertifikat som stadfester kvaliteten til eit datasett |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Kvalitetsmerknad](kvalitetsmerknad.md) | Ein merknad om kvaliteten til eit datasett |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |  no  |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |  no  |
| [Tekstdel](tekstdel.md) | Ein tekstleg del av ein kvalitetsmerknad (Web Annotation) |  no  |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Kvalitetsdimensjon](kvalitetsdimensjon.md) | Ein kvalitetsdimensjon som grupperer relaterte kvalitetsmål |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Kvalitetsdimensjon](kvalitetsdimensjon.md), [Kvalitetsmaal](kvalitetsmaal.md), [Kvalitetsmerknad](kvalitetsmerknad.md), [Kvalitetsmaaling](kvalitetsmaaling.md), [Standard](standard.md), [Tekstdel](tekstdel.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md), [KatalogisertRessurs](katalogisertressurs.md), [Aktor](aktor.md), [Kontaktopplysning](kontaktopplysning.md), [Tidsrom](tidsrom.md), [RegulativRessurs](regulativressurs.md), [Identifikator](identifikator.md), [Rettighetserklaring](rettighetserklaring.md), [Sjekksum](sjekksum.md), [Gebyr](gebyr.md), [Relasjon](relasjon.md), [Distribusjon](distribusjon.md), [Datasett](datasett.md), [Katalogpost](katalogpost.md) |

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


* from schema: https://data.norge.no/linkml/dqv-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/dqv-ap-no/id |
| native | https://data.norge.no/linkml/dqv-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/dqv-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- Kvalitetsdimensjon
- Kvalitetsmaal
- Kvalitetsmerknad
- Kvalitetsmaaling
- Standard
- Tekstdel
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
range: uriorcurie
required: true

```
</details>