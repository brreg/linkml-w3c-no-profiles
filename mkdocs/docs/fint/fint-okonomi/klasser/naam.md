

# Slot: naam 


_Namn på eining eller kodeverk-element._





URI: [okn:naam](https://schema.fintlabs.no/okonomi/naam)
Alias: naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Leverandorgruppe](leverandorgruppe.md) | Gruppering av leverandørar |  yes  |
| [Merverdiavgift](merverdiavgift.md) | Kodeverk for merverdiavgifter |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Fakturautsteder](fakturautsteder.md) | Eining som utformar og oversender faktura og mottar betaling |  yes  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Vare](vare.md) | Vare eller teneste som kan leverast og fakturerast |  yes  |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [OkonomiValuta](okonomivaluta.md) | Valuta for transaksjonsbeløp |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Fakturautsteder](fakturautsteder.md), [Leverandorgruppe](leverandorgruppe.md), [Vare](vare.md), [Merverdiavgift](merverdiavgift.md), [OkonomiValuta](okonomivaluta.md), [Begrep](begrep.md) |
| Slot URI | [okn:naam](https://schema.fintlabs.no/okonomi/naam) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-okonomi




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | okn:naam |
| native | https://schema.fintlabs.no/okonomi/:naam |




## LinkML Source

<details>
```yaml
name: naam
description: Namn på eining eller kodeverk-element.
from_schema: https://data.norge.no/linkml/fint-okonomi
rank: 1000
slot_uri: okn:naam
alias: naam
domain_of:
- Fakturautsteder
- Leverandorgruppe
- Vare
- Merverdiavgift
- OkonomiValuta
- Begrep
range: string

```
</details>