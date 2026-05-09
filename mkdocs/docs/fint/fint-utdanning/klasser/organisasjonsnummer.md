

# Slot: organisasjonsnummer 


_Organisasjonsnummer-identifikator._





URI: [utd:organisasjonsnummer](https://schema.fintlabs.no/utdanning/organisasjonsnummer)
Alias: organisasjonsnummer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  yes  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Identifikator](identifikator.md) |
| Domain Of | [Skole](skole.md), [Enhet](enhet.md) |
| Slot URI | [utd:organisasjonsnummer](https://schema.fintlabs.no/utdanning/organisasjonsnummer) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:organisasjonsnummer |
| native | https://schema.fintlabs.no/utdanning/:organisasjonsnummer |




## LinkML Source

<details>
```yaml
name: organisasjonsnummer
description: Organisasjonsnummer-identifikator.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:organisasjonsnummer
alias: organisasjonsnummer
domain_of:
- Skole
- Enhet
range: Identifikator
inlined: true

```
</details>