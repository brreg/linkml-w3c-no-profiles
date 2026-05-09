

# Slot: kontaktinformasjon 


_Den føretrekte måten å kome i kontakt med ein aktør._





URI: [fint:kontaktinformasjon](https://schema.fintlabs.no/kontaktinformasjon)
Alias: kontaktinformasjon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  yes  |
| [Part](part.md) | Part til Mappe, Registrering eller Dokumentbeskrivelse |  yes  |
| [Korrespondansepart](korrespondansepart.md) | Verksemd eller person som arkivskapar mottek eller sender arkivdokument til |  yes  |
| [Person](person.md) | Fysiske private personar |  no  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Kontaktinformasjon](kontaktinformasjon.md) |
| Domain Of | [Korrespondansepart](korrespondansepart.md), [Part](part.md), [Aktoer](aktoer.md), [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:kontaktinformasjon](https://schema.fintlabs.no/kontaktinformasjon) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-arkiv




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:kontaktinformasjon |
| native | https://schema.fintlabs.no/arkiv/:kontaktinformasjon |




## LinkML Source

<details>
```yaml
name: kontaktinformasjon
description: Den føretrekte måten å kome i kontakt med ein aktør.
from_schema: https://data.norge.no/linkml/fint-arkiv
rank: 1000
slot_uri: fint:kontaktinformasjon
alias: kontaktinformasjon
domain_of:
- Korrespondansepart
- Part
- Aktoer
- Kontaktperson
range: Kontaktinformasjon
inlined: true

```
</details>