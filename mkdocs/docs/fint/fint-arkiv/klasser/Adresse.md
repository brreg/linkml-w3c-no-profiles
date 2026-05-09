

# Slot: adresse 


_Adresse til matrikkeleining._





URI: [fint:adresse](https://schema.fintlabs.no/adresse)
Alias: adresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |  no  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md), [Matrikkelnummer](matrikkelnummer.md) |
| Slot URI | [fint:adresse](https://schema.fintlabs.no/adresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:adresse |
| native | https://schema.fintlabs.no/arkiv/:adresse |




## LinkML Source

<details>
```yaml
name: adresse
description: Adresse til matrikkeleining.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:adresse
alias: adresse
domain_of:
- Korrespondansepart
- Part
- Matrikkelnummer
range: Adresse
inlined: true

```
</details>