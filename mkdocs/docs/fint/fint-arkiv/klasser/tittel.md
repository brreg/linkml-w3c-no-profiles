

# Slot: tittel 


_Tittel eller namn på arkivenheten._





URI: [ark:tittel](https://schema.fintlabs.no/arkiv/tittel)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TilskuddFartoy](tilskuddfartoy.md) | Sak om søknad om tilskudd til freda fartøy |  no  |
| [Mappe](mappe.md) | Abstrakt basisklasse for alle mappetypar |  yes  |
| [Sak](sak.md) | Generisk saksmappe (konkret Sak i Noark) |  no  |
| [Arkivdel](arkivdel.md) | Ein vilkårleg definert del av eit arkiv |  yes  |
| [Klassifikasjonssystem](klassifikasjonssystem.md) | Overordna struktur for mappene i ein eller fleire arkivdelar |  yes  |
| [SoeknadDrosjeloeyve](soeknaddrosjeloeyve.md) | Sak om søknad om løyve til å køyre drosje |  no  |
| [DispensasjonAutomatiskFredaKulturminne](dispensasjonautomatiskfredakulturminne.md) | Sak om søknad om dispensasjon for tiltak på automatisk freda kulturminne |  no  |
| [TilskuddFredaBygningPrivatEie](tilskuddfredabygningprivateie.md) | Sak om søknad om tilskudd til freda bygningar i privat eige (FRIP) |  no  |
| [Dokumentbeskrivelse](dokumentbeskrivelse.md) | Skildring av eit dokument tilknytt ein journalpost |  yes  |
| [Registrering](registrering.md) | Abstrakt basisklasse — arkivets primære byggeklossar |  yes  |
| [Journalpost](journalpost.md) | Ein journalpost (inn- eller utgåande dokument, notat o |  no  |
| [Saksmappe](saksmappe.md) | Abstrakt spesialisering av Mappe som svarar til ei "sak" i Noark |  no  |
| [Klasse](klasse.md) | Ein klasse i eit klassifikasjonssystem |  yes  |
| [Tilgang](tilgang.md) | Styring av kven som har tilgang til kva opplysningar |  yes  |
| [Personalmappe](personalmappe.md) | Saksmappe med opplysningar om ein arbeidstakars arbeidsforhold |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Mappe](mappe.md), [Registrering](registrering.md), [Arkivdel](arkivdel.md), [Klassifikasjonssystem](klassifikasjonssystem.md), [Tilgang](tilgang.md), [Dokumentbeskrivelse](dokumentbeskrivelse.md), [Klasse](klasse.md) |
| Slot URI | [ark:tittel](https://schema.fintlabs.no/arkiv/tittel) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ark:tittel |
| native | https://schema.fintlabs.no/arkiv/:tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Tittel eller namn på arkivenheten.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: ark:tittel
alias: tittel
domain_of:
- Mappe
- Registrering
- Arkivdel
- Klassifikasjonssystem
- Tilgang
- Dokumentbeskrivelse
- Klasse
range: string

```
</details>