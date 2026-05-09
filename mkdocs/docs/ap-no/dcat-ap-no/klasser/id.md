

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/dcat-ap-no/id](https://data.norge.no/linkml/dcat-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tidsinstant](tidsinstant.md) | Eit tidspunkt (OWL Time) |  no  |
| [ProvAttributering](provattributering.md) | Ein kvalifisert PROV-attributering |  no  |
| [Rettighetserklaring](rettighetserklaring.md) | Ei erklæring om rettar til ein ressurs (ODRS) |  no  |
| [Tidsrom](tidsrom.md) | Eit tidsintervall med start- og sluttdato |  no  |
| [OdrlPolicy](odrlpolicy.md) | Ein ODRL-policy |  no  |
| [Relasjon](relasjon.md) | Ein kvalifisert relasjon mellom to ressursar |  no  |
| [Datasett](datasett.md) | Ei samling av data utgjeven eller kuratert av éin aktør |  no  |
| [Sjekksum](sjekksum.md) | Ein sjekksum for ein distribusjon |  no  |
| [Standard](standard.md) | Ein standard som ein ressurs er i samsvar med |  no  |
| [Distribusjon](distribusjon.md) | Ein spesifikk representasjon/nedlastbar form av eit datasett |  no  |
| [KatalogisertRessurs](katalogisertressurs.md) | Basisklasse for ressursar som kan katalogiserast |  no  |
| [ProvAktivitet](provaktivitet.md) | Ein PROV-aktivitet |  no  |
| [Datasettserie](datasettserie.md) | Ei serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Begrepssamling](begrepssamling.md) | Ei SKOS-omgrepssamling (temavokabular) |  no  |
| [Konsept](konsept.md) | Referanse til eit SKOS-omgrep frå eit kontrollert vokabular |  no  |
| [Datatjeneste](datatjeneste.md) | Ei samling operasjonar tilgjengeleg via eit API-grensesnitt |  no  |
| [Frekvens](frekvens.md) | Ein oppdateringsfrekvens |  no  |
| [Identifikator](identifikator.md) | Ein alternativ identifikator for ein ressurs |  no  |
| [Spraak](spraak.md) | Ein språkreferanse (dct:LinguisticSystem) |  no  |
| [Aktor](aktor.md) | Ein aktør (person, organisasjon eller system) med ansvar for ein ressurs |  no  |
| [Katalog](katalog.md) | Ei kuratert samling av metadata om datasett, datatenestar og/eller andre kata... |  no  |
| [Katalogpost](katalogpost.md) | Ein katalogpost som beskriv ein ressurs i katalogen |  no  |
| [ProvenanceStatement](provenancestatement.md) | Ein provenienserklæring |  no  |
| [Kontaktopplysning](kontaktopplysning.md) | Kontaktinformasjon for ein aktør |  no  |
| [Mediatype](mediatype.md) | Ein medietype eller filformat (dct:MediaTypeOrExtent) |  no  |
| [RegulativRessurs](regulativressurs.md) | Ein regulativ ressurs (lov, forskrift o |  no  |
| [Gebyr](gebyr.md) | Eit gebyr knytt til bruk av ein datatjeneste |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Frekvens](frekvens.md), [ProvenanceStatement](provenancestatement.md), [OdrlPolicy](odrlpolicy.md), [ProvAktivitet](provaktivitet.md), [ProvAttributering](provattributering.md), [Tidsinstant](tidsinstant.md), [KatalogisertRessurs](katalogisertressurs.md), [Aktor](aktor.md), [Kontaktopplysning](kontaktopplysning.md), [Tidsrom](tidsrom.md), [Standard](standard.md), [RegulativRessurs](regulativressurs.md), [Identifikator](identifikator.md), [Rettighetserklaring](rettighetserklaring.md), [Sjekksum](sjekksum.md), [Gebyr](gebyr.md), [Relasjon](relasjon.md), [Distribusjon](distribusjon.md), [Katalogpost](katalogpost.md), [Spraak](spraak.md), [Mediatype](mediatype.md), [Konsept](konsept.md), [Begrepssamling](begrepssamling.md) |

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


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://data.norge.no/linkml/dcat-ap-no/id |
| native | https://data.norge.no/linkml/dcat-ap-no/id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
identifier: true
alias: id
domain_of:
- Frekvens
- ProvenanceStatement
- OdrlPolicy
- ProvAktivitet
- ProvAttributering
- Tidsinstant
- KatalogisertRessurs
- Aktor
- Kontaktopplysning
- Tidsrom
- Standard
- RegulativRessurs
- Identifikator
- Rettighetserklaring
- Sjekksum
- Gebyr
- Relasjon
- Distribusjon
- Katalogpost
- Spraak
- Mediatype
- Konsept
- Begrepssamling
range: uriorcurie
required: true

```
</details>