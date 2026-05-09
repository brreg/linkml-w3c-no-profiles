

# Slot: organisasjonsnummer 


_Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret._





URI: [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  yes  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Enhet](enhet.md) |
| Slot URI | [fint:organisasjonsnummer](https://schema.fintlabs.no/organisasjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:organisasjonsnummer |
| native | https://schema.fintlabs.no/administrasjon/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:organisasjonsnummer
alias: organisasjonsnummer
domain_of:
- Arbeidslokasjon
- Organisasjonselement
- Enhet
range: Identifikator
inlined: true

```
</details>