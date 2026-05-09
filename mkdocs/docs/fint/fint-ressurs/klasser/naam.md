

# Slot: naam 


_Namn på ressursen eller kodeverk-elementet._





URI: [res:naam](https://schema.fintlabs.no/ressurs/naam)
Alias: naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Applikasjonskategori](applikasjonskategori.md) | Kategori av applikasjonar |  yes  |
| [Brukertype](brukertype.md) | Dei ulike brukartypane som kan nytte lisensen |  yes  |
| [Status](status.md) | Status på ei digital eining i fagsystemet |  yes  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Produsent](produsent.md) | Produsent av ei digital eining |  yes  |
| [Rettighet](rettighet.md) | Ei namngitt rettighet |  yes  |
| [Lisensmodell](lisensmodell.md) | Lisensmodellar som kan knytast til ein lisens |  yes  |
| [Applikasjon](applikasjon.md) | Ein applikasjon med tilhøyrande ressursar |  yes  |
| [DigitalEnhet](digitalenhet.md) | Ei digital eining som t |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Plattform](plattform.md) | Plattforma tenesta kan leverast på |  yes  |
| [Enhetsgruppe](enhetsgruppe.md) | Ei gruppering av einsarta digitale einingar |  yes  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Enhetstype](enhetstype.md) | Type digital eining |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Applikasjonsressurs](applikasjonsressurs.md) | Informasjon om kor ein applikasjon kan nyttast (lisensressurs) |  yes  |
| [Handhevingstype](handhevingstype.md) | Korleis ulike lisensmodellar kan handhevast |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Applikasjon](applikasjon.md), [Applikasjonsressurs](applikasjonsressurs.md), [DigitalEnhet](digitalenhet.md), [Enhetsgruppe](enhetsgruppe.md), [Rettighet](rettighet.md), [Applikasjonskategori](applikasjonskategori.md), [Brukertype](brukertype.md), [Enhetstype](enhetstype.md), [Handhevingstype](handhevingstype.md), [Lisensmodell](lisensmodell.md), [Plattform](plattform.md), [Produsent](produsent.md), [Status](status.md), [Begrep](begrep.md) |
| Slot URI | [res:naam](https://schema.fintlabs.no/ressurs/naam) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:naam |
| native | https://schema.fintlabs.no/ressurs/:naam |




## LinkML Source

<details>
```yaml
name: naam
description: Namn på ressursen eller kodeverk-elementet.
from_schema: https://data.norge.no/linkml/fint-ressurs
rank: 1000
slot_uri: res:naam
alias: naam
domain_of:
- Applikasjon
- Applikasjonsressurs
- DigitalEnhet
- Enhetsgruppe
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
range: string

```
</details>