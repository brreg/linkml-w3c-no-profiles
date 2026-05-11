

# Slot: gyldighetsperiode 


_Periode ressursen er gyldig for._





URI: [fint:gyldighetsperiode](https://schema.fintlabs.no/gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |  yes  |
| [Gruppemedlemskap](gruppemedlemskap.md) | Abstrakt basisklasse for gruppemedlemskapar i utdanning |  yes  |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |  yes  |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |  yes  |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |  yes  |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |  yes  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |
| [Fullfortkode](fullfortkode.md) | Kode for fullførtresultat av lærling |  yes  |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |  yes  |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |  yes  |
| [Vitnemalsmerknad](vitnemalsmerknad.md) | Merknad på vitnemål |  yes  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |  yes  |
| [Fravartype](fravartype.md) | Type fråvær (t |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Karakterstatus](karakterstatus.md) | Status for ein karakter (t |  yes  |
| [Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |  no  |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |  yes  |
| [Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |  no  |
| [Varseltype](varseltype.md) | Type varsel knytt til ein elev |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Brevtype](brevtype.md) | Type brev knytt til lærlingprøve |  yes  |
| [Eksamensform](eksamensform.md) | Form for gjennomføring av eksamen |  yes  |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |  yes  |
| [Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |  no  |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |  yes  |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |  yes  |
| [Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |  no  |
| [Termin](termin.md) | Ein skuleterm (t |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |  no  |
| [Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |  yes  |
| [Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Begrep](begrep.md), [Identifikator](identifikator.md), [Gruppemedlemskap](gruppemedlemskap.md), [Avbruddsaarsak](avbruddsaarsak.md), [Betalingsstatus](betalingsstatus.md), [Bevistype](bevistype.md), [Brevtype](brevtype.md), [Eksamensform](eksamensform.md), [Elevkategori](elevkategori.md), [Fagmerknad](fagmerknad.md), [Fagstatus](fagstatus.md), [Fravartype](fravartype.md), [Fullfortkode](fullfortkode.md), [Karakterskala](karakterskala.md), [Karakterstatus](karakterstatus.md), [Karakterverdi](karakterverdi.md), [OtEnhet](otenhet.md), [OtStatus](otstatus.md), [Provestatus](provestatus.md), [Skoleaar](skoleaar.md), [Skoleeiertype](skoleeiertype.md), [Termin](termin.md), [Tilrettelegging](tilrettelegging.md), [Varseltype](varseltype.md), [Vitnemalsmerknad](vitnemalsmerknad.md) |
| Slot URI | [fint:gyldighetsperiode](https://schema.fintlabs.no/gyldighetsperiode) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:gyldighetsperiode |
| native | https://schema.fintlabs.no/:gyldighetsperiode |




## LinkML Source

<details>
```yaml
name: gyldighetsperiode
description: Periode ressursen er gyldig for.
from_schema: https://data.norge.no/linkml/fint-common
slot_uri: fint:gyldighetsperiode
alias: gyldighetsperiode
domain_of:
- Begrep
- Identifikator
- Gruppemedlemskap
- Avbruddsaarsak
- Betalingsstatus
- Bevistype
- Brevtype
- Eksamensform
- Elevkategori
- Fagmerknad
- Fagstatus
- Fravartype
- Fullfortkode
- Karakterskala
- Karakterstatus
- Karakterverdi
- OtEnhet
- OtStatus
- Provestatus
- Skoleaar
- Skoleeiertype
- Termin
- Tilrettelegging
- Varseltype
- Vitnemalsmerknad
range: Periode
inlined: true

```
</details>