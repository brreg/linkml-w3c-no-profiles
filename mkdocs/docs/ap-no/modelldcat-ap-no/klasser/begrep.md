

# Slot: begrep 


_Fagomgrep ressursen handlar om (dct:subject)._





URI: [dct:subject](http://purl.org/dc/terms/subject)
Alias: begrep

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Kodeelement](kodeelement.md) | Eit element i ei kodeliste (modelldcatno:CodeElement) |  yes  |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |
| [Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |
| [Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Konsept](konsept.md) |
| Domain Of | [Informasjonsmodell](informasjonsmodell.md), [Modellelement](modellelement.md), [Eigenskap](eigenskap.md), [Kodeelement](kodeelement.md) |
| Slot URI | [dct:subject](http://purl.org/dc/terms/subject) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/modelldcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:subject |
| native | https://data.norge.no/linkml/modelldcat-ap-no/begrep |




## LinkML Source

<details>
```yaml
name: begrep
description: Fagomgrep ressursen handlar om (dct:subject).
from_schema: https://data.norge.no/linkml/modelldcat-ap-no
rank: 1000
slot_uri: dct:subject
alias: begrep
domain_of:
- Informasjonsmodell
- Modellelement
- Eigenskap
- Kodeelement
range: Konsept
multivalued: true

```
</details>