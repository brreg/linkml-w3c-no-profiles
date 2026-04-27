

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://data.norge.no/linkml/dcat-ap-no/id](https://data.norge.no/linkml/dcat-ap-no/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |  no  |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Katalogpost](Katalogpost.md) | En katalogpost som beskriver en ressurs i katalogen |  no  |
| [Tidsrom](Tidsrom.md) | Et tidsintervall med start- og sluttdato |  no  |
| [Identifikator](Identifikator.md) | En alternativ identifikator for en ressurs |  no  |
| [OdrlPolicy](OdrlPolicy.md) | En ODRL-policy |  no  |
| [Sjekksum](Sjekksum.md) | En sjekksum for en distribusjon |  no  |
| [Standard](Standard.md) | En standard som en ressurs er i samsvar med |  no  |
| [Begrepssamling](Begrepssamling.md) | En SKOS-begrepssamling (temavokabular) |  no  |
| [RegulativRessurs](RegulativRessurs.md) | En regulativ ressurs (lov, forskrift e |  no  |
| [Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |  no  |
| [Gebyr](Gebyr.md) | Et gebyr knyttet til bruk av en datatjeneste |  no  |
| [ProvAktivitet](ProvAktivitet.md) | En PROV-aktivitet |  no  |
| [ProvAttributering](ProvAttributering.md) | En kvalifisert PROV-attributering |  no  |
| [Mediatype](Mediatype.md) | En medietype eller filformat |  no  |
| [Rettighetserklaring](Rettighetserklaring.md) | En erklæring om rettigheter til en ressurs (ODRS) |  no  |
| [Frekvens](Frekvens.md) | En oppdateringsfrekvens |  no  |
| [Aktor](Aktor.md) | En aktør (person, organisasjon eller system) med ansvar for en ressurs |  no  |
| [KatalogisertRessurs](KatalogisertRessurs.md) | Basisklasse for ressurser som kan katalogiseres |  no  |
| [Relasjon](Relasjon.md) | En kvalifisert relasjon mellom to ressurser |  no  |
| [ProvenanceStatement](ProvenanceStatement.md) | En provenienserklæring |  no  |
| [Kontaktopplysning](Kontaktopplysning.md) | Kontaktinformasjon for en aktør |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  no  |
| [Tidsinstant](Tidsinstant.md) | Et tidspunkt (OWL Time) |  no  |
| [Spraak](Spraak.md) | En språkreferanse |  no  |
| [Begrep](Begrep.md) | Et SKOS-begrep fra et kontrollert vokabular |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Begrep](Begrep.md), [Begrepssamling](Begrepssamling.md), [Spraak](Spraak.md), [Mediatype](Mediatype.md), [Frekvens](Frekvens.md), [ProvenanceStatement](ProvenanceStatement.md), [OdrlPolicy](OdrlPolicy.md), [ProvAktivitet](ProvAktivitet.md), [ProvAttributering](ProvAttributering.md), [Tidsinstant](Tidsinstant.md), [KatalogisertRessurs](KatalogisertRessurs.md), [Aktor](Aktor.md), [Kontaktopplysning](Kontaktopplysning.md), [Tidsrom](Tidsrom.md), [Standard](Standard.md), [RegulativRessurs](RegulativRessurs.md), [Identifikator](Identifikator.md), [Rettighetserklaring](Rettighetserklaring.md), [Sjekksum](Sjekksum.md), [Gebyr](Gebyr.md), [Relasjon](Relasjon.md), [Distribusjon](Distribusjon.md), [Katalogpost](Katalogpost.md) |

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
- Begrep
- Begrepssamling
- Spraak
- Mediatype
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
range: uriorcurie
required: true

```
</details>