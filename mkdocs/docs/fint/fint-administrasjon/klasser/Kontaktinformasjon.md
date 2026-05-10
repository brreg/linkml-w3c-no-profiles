

# Slot: kontaktinformasjon 


_Den føretrekte måten å kome i kontakt med ein aktør._





URI: [fint:kontaktinformasjon](https://schema.fintlabs.no/kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  yes  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |  yes  |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktinformasjon](kontaktinformasjon.md) |
| Domain Of | [Arbeidslokasjon](arbeidslokasjon.md), [Organisasjonselement](organisasjonselement.md), [Personalressurs](personalressurs.md), [Aktoer](aktoer.md), [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:kontaktinformasjon](https://schema.fintlabs.no/kontaktinformasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktinformasjon |
| native | https://schema.fintlabs.no/administrasjon/:kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
description: Den føretrekte måten å kome i kontakt med ein aktør.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: fint:kontaktinformasjon
alias: kontaktinformasjon
domain_of:
- Arbeidslokasjon
- Organisasjonselement
- Personalressurs
- Aktoer
- Kontaktperson
range: Kontaktinformasjon
inlined: true

```
</details>