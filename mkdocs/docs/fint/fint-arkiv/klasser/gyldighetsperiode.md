

# Slot: gyldighetsperiode 


_Periode ressursen er gyldig for._





URI: [fint:gyldighetsperiode](https://schema.fintlabs.no/gyldighetsperiode)
Alias: gyldighetsperiode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Rolle](rolle.md) | Rolla til ein arkivressurs |  yes  |
| [DokumentType](dokumenttype.md) | Type dokument |  yes  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [JournalpostType](journalposttype.md) | Namn på type journalpost |  yes  |
| [Merknadstype](merknadstype.md) | Namn på type merknad |  yes  |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |  no  |
| [Tilgangsrestriksjon](tilgangsrestriksjon.md) | Angiving av at dokumenta ikkje er offentleg tilgjengelege |  yes  |
| [Skjermingshjemmel](skjermingshjemmel.md) | Tilvising til heimel i offentleglova, tryggingslova eller tryggingsinstruksen |  yes  |
| [PartRolle](partrolle.md) | Rolla til ein part |  yes  |
| [Saksstatus](saksstatus.md) | Status til saksmappa |  yes  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [DokumentStatus](dokumentstatus.md) | Status til eit dokument |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Format](format.md) | Dokumentets filformat |  yes  |
| [Saksmappetype](saksmappetype.md) | Type saksmappe — differensierer innhald og behandlingsrutine |  yes  |
| [KorrespondansepartType](korrespondanseparttype.md) | Type korrespondansepart |  yes  |
| [Tilgangsgruppe](tilgangsgruppe.md) | Tilgangsgruppe for intern skjerming av innhald |  yes  |
| [Variantformat](variantformat.md) | Angiving av kva variant eit dokument førekjem i |  yes  |
| [TilknyttetRegistreringSom](tilknyttetregistreringsom.md) | Kva rolle dokumentet har i høve registreringa (t |  yes  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [JournalStatus](journalstatus.md) | Status til journalposten |  yes  |
| [AdministrativEnhet](administrativenhet.md) | Administrativ eining med ansvar for saksbehandling |  yes  |
| [Klassifikasjonstype](klassifikasjonstype.md) | Type klassifikasjonssystem |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Periode](periode.md) |
| Domain Of | [Begrep](begrep.md), [Identifikator](identifikator.md), [AdministrativEnhet](administrativenhet.md), [DokumentStatus](dokumentstatus.md), [DokumentType](dokumenttype.md), [Format](format.md), [JournalpostType](journalposttype.md), [JournalStatus](journalstatus.md), [Klassifikasjonstype](klassifikasjonstype.md), [KorrespondansepartType](korrespondanseparttype.md), [Merknadstype](merknadstype.md), [PartRolle](partrolle.md), [Rolle](rolle.md), [Saksmappetype](saksmappetype.md), [Saksstatus](saksstatus.md), [Skjermingshjemmel](skjermingshjemmel.md), [Tilgangsgruppe](tilgangsgruppe.md), [Tilgangsrestriksjon](tilgangsrestriksjon.md), [TilknyttetRegistreringSom](tilknyttetregistreringsom.md), [Variantformat](variantformat.md) |
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
- AdministrativEnhet
- DokumentStatus
- DokumentType
- Format
- JournalpostType
- JournalStatus
- Klassifikasjonstype
- KorrespondansepartType
- Merknadstype
- PartRolle
- Rolle
- Saksmappetype
- Saksstatus
- Skjermingshjemmel
- Tilgangsgruppe
- Tilgangsrestriksjon
- TilknyttetRegistreringSom
- Variantformat
range: Periode
inlined: true

```
</details>