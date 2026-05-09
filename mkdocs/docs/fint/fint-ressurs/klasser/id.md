

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/ressurs/:id](https://schema.fintlabs.no/ressurs/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |  no  |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen |  no  |
| [Status](status.md) | Status på ei digital eining i fagsystemet |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Produsent](produsent.md) | Produsent av ei digital eining |  no  |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  no  |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  no  |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md) | Medlemskap mellom ei digital eining og ei einingsgruppe |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på |  no  |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) | Kva organisasjonselements brukarar som har tilgang til ein ressurs |  no  |
| [Identitet](identitet.md) | Identitet som identifiserer innehavaren av rettigheiter i organisasjonen |  no  |
| [Enhetstype](enhetstype.md) | Type digital eining |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  no  |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Applikasjon](applikasjon.md), [Applikasjonsressurs](applikasjonsressurs.md), [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md), [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md), [Enhetsgruppemedlemskap](enhetsgruppemedlemskap.md), [Identitet](identitet.md), [Rettighet](rettighet.md), [Applikasjonskategori](applikasjonskategori.md), [Brukertype](brukertype.md), [Enhetstype](enhetstype.md), [Handhevingstype](handhevingstype.md), [Lisensmodell](lisensmodell.md), [Plattform](plattform.md), [Produsent](produsent.md), [Status](status.md), [Begrep](begrep.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md) |

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


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/ressurs/:id |
| native | https://schema.fintlabs.no/ressurs/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
identifier: true
alias: id
domain_of:
- Applikasjon
- Applikasjonsressurs
- Applikasjonsressurstilgjengelighet
- DigitalEnhet
- Enhetsgruppe
- Enhetsgruppemedlemskap
- Identitet
- Rettighet
- Applikasjonskategori
- Brukertype
- Enhetstype
- Handhevingstype
- Lisensmodell
- Plattform
- Produsent
- Status
- Begrep
- Valuta
- Person
- Kontaktperson
- Virksomhet
range: uriorcurie
required: true

```
</details>