

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/:id](https://schema.fintlabs.no/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |  no  |
| [Variabellonn](variabellonn.md) | Informasjon om variabel lønn |  no  |
| [Objekt](objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |  no  |
| [Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |  no  |
| [Organisasjonstype](organisasjonstype.md) | Typen til eit organisasjonselement |  no  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  no  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  no  |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |  no  |
| [Uketimetall](uketimetall.md) | Timer per veke i 100 % stilling |  no  |
| [Anlegg](anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |  no  |
| [Art](art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |  no  |
| [Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |  no  |
| [Kontrakt](kontrakt.md) | Kontrakt transaksjonen er knytt til |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  no  |
| [Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |  no  |
| [Lonsart](lonsart.md) | Type ytelse |  no  |
| [Fravaerstype](fravaerstype.md) | Type fråvær |  no  |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |  no  |
| [Diverse](diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |  no  |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |  no  |
| [Formaal](formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |  no  |
| [Fravaersgrunn](fravaersgrunn.md) | Grunn til fråvær |  no  |
| [Ramme](ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |  no  |
| [Personalressurskategori](personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |  no  |
| [Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Aktivitet](aktivitet.md) | Del av kontostrengen og detaljering av funksjon |  no  |
| [Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI) |
| Domain Of | [Begrep](begrep.md), [Elev](elev.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md), [Lonn](lonn.md), [Fravaer](fravaer.md), [Fullmakt](fullmakt.md), [Rolle](rolle.md), [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Personalressurs](personalressurs.md), [Arbeidsforhold](arbeidsforhold.md) |

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


* from schema: https://data.norge.no/linkml/fint-common




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/:id |
| native | https://schema.fintlabs.no/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/fint-common
identifier: true
alias: id
domain_of:
- Begrep
- Elev
- Valuta
- Person
- Kontaktperson
- Virksomhet
- Lonn
- Fravaer
- Fullmakt
- Rolle
- Arbeidslokasjon
- Organisasjonselement
- Personalressurs
- Arbeidsforhold
range: uriorcurie
required: true

```
</details>