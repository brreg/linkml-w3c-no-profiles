

# Slot: tittel 


_Namn/tittel på ressursen (dct:title)._





URI: [dct:title](http://purl.org/dc/terms/title)
Alias: tittel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RootObjekttype](rootobjekttype.md) | Ein rotobjekttype — toppnivå-klasse i informasjonsmodellen |  no  |
| [Informasjonsmodell](informasjonsmodell.md) | Ein informasjonsmodell som er katalogisert i ein modelkatalog (modelldcatno:I... |  yes  |
| [Rolle](rolle.md) | Ein rolle — ein eigenskap som knyter ein objekttype til ein assosiasjon |  no  |
| [Modellelement](modellelement.md) | Abstrakt basisklasse for alle modellelement i ein informasjonsmodell |  yes  |
| [Samling](samling.md) | Ein samling — ein eigenskap som representerer ei uordna mengd av modellelemen... |  no  |
| [AlleAv](alleav.md) | Alle av — alle modellelementa i lista må gjelde (logisk OG-mengd) |  no  |
| [Spesialisering](spesialisering.md) | Ein spesialisering — eit arveforhold frå eit spesielt til eit generelt modell... |  no  |
| [Og](og.md) | Og — logisk OG-betingelse; alle deltakande modellelement må gjelde |  no  |
| [Ikke](ikke.md) | Ikkje — negasjon; modellelementet det refererer til må ikkje gjelde |  no  |
| [NoenAv](noenav.md) | Nokon av — minst eitt modellelement i lista må gjelde (logisk ELLER-mengd) |  no  |
| [Betingelsesregel](betingelsesregel.md) | Ein betingelsesregel — ei formell avgrensing på modellelement eller eigenskap... |  no  |
| [EnkelType](enkeltype.md) | Ein enkel type med restriksjonar (xsd-fasettar) |  no  |
| [Eigenskap](eigenskap.md) | Abstrakt basisklasse for eigenskapar knytt til eit modellelement |  yes  |
| [Attributt](attributt.md) | Ein attributt — ein eigenskap med ein datatype eller enkel type som verdi |  no  |
| [Avhengighet](avhengighet.md) | Ein avhengighet — ein relasjon der det eine modellelementet avheng av det and... |  no  |
| [Realisering](realisering.md) | Ein realisering — ein implementasjonsrelasjon mellom modellelement |  no  |
| [Modul](modul.md) | Ein modul som grupperer modellelement i informasjonsmodellen |  no  |
| [Merknad](merknad.md) | Ei merknad knytt til eit modellelement eller eigenskap |  yes  |
| [Dokument](dokument.md) | Eit dokument (foaf:Document) |  no  |
| [Eller](eller.md) | Eller — logisk ELLER-betingelse; minst eitt modellelement må gjelde |  no  |
| [Datatype](datatype.md) | Ein datatype — ein strukturert samansett type |  no  |
| [Standard](standard.md) | Ein standard (dct:Standard) |  yes  |
| [Modelkatalog](modelkatalog.md) | Ei kuratert samling av metadata om informasjonsmodellar (dcat:Catalog) |  yes  |
| [XEllerY](xellery.md) | Xor — eksklusiv ELLER-betingelse; nøyaktig eitt modellelement må gjelde |  no  |
| [Objekttype](objekttype.md) | Ein objekttype — ein klasse med eigenskapar i informasjonsmodellen |  no  |
| [Assosiasjon](assosiasjon.md) | Ein assosiasjon — ein eigenskap som refererer til eit anna modellelement |  no  |
| [Kodeliste](kodeliste.md) | Ei kodeliste — eit kontrollert vokabular av tillate verdiar |  no  |
| [Abstraksjon](abstraksjon.md) | Ein abstraksjon — ein forenkling som representerer eit modellelement |  no  |
| [Sammensetning](sammensetning.md) | Ein sammensetning — ein sterk eigarelskapsrelasjon mellom modellelement |  no  |
| [Valg](valg.md) | Eit val — ein eigenskap som representerer eit val mellom modellelement |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](langstring.md) |
| Domain Of | [Standard](standard.md), [Dokument](dokument.md), [Modelkatalog](modelkatalog.md), [Informasjonsmodell](informasjonsmodell.md), [Modellelement](modellelement.md), [Eigenskap](eigenskap.md), [Merknad](merknad.md) |
| Slot URI | [dct:title](http://purl.org/dc/terms/title) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/common-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:title |
| native | https://data.norge.no/linkml/common-ap-no/tittel |




## LinkML Source

<details>
```yaml
name: tittel
description: Namn/tittel på ressursen (dct:title).
from_schema: https://data.norge.no/linkml/common-ap-no
slot_uri: dct:title
alias: tittel
domain_of:
- Standard
- Dokument
- Modelkatalog
- Informasjonsmodell
- Modellelement
- Eigenskap
- Merknad
range: LangString
multivalued: true

```
</details>