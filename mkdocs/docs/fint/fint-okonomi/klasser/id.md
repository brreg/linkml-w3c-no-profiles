

# Slot: id 


_URI-identifikator for ressursen._





URI: [https://schema.fintlabs.no/okonomi/:id](https://schema.fintlabs.no/okonomi/:id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  no  |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |  no  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  no  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  no  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  no  |
| [Transaksjon](transaksjon.md) | Overføring av pengar til eller frå eksterne partar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Fakturagrunnlag](fakturagrunnlag.md) | Grunnlag for fakturering |  no  |
| [Postering](postering.md) | Føring på ein konto i rekneskapet |  no  |
| [Faktura](faktura.md) | Betalingskrav utforma og oversendt frå fakturautstedar til fakturamottakar |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |  no  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  no  |
| [Leverandor](leverandor.md) | Person eller verksemd som leverer produkt eller tenester |  no  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Faktura](faktura.md), [Fakturagrunnlag](fakturagrunnlag.md), [Fakturautsteder](fakturautsteder.md), [Transaksjon](transaksjon.md), [Postering](postering.md), [Leverandor](leverandor.md), [Leverandorgruppe](leverandorgruppe.md), [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md), [Begrep](begrep.md), [Elev](elev.md), [Valuta](valuta.md), [Person](person.md), [Kontaktperson](kontaktperson.md), [Virksomhet](virksomhet.md) |

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


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://schema.fintlabs.no/okonomi/:id |
| native | https://schema.fintlabs.no/okonomi/:id |




## LinkML Source

<details>
```yaml
name: id
description: URI-identifikator for ressursen.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
identifier: true
alias: id
domain_of:
- Faktura
- Fakturagrunnlag
- Fakturautsteder
- Transaksjon
- Postering
- Leverandor
- Leverandorgruppe
- Vare
- Merverdiavgift
- OkonomiValuta
- Begrep
- Elev
- Valuta
- Person
- Kontaktperson
- Virksomhet
range: uriorcurie
required: true

```
</details>