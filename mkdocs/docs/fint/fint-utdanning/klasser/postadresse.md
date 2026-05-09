

# Slot: postadresse 


_Postadresse._





URI: [utd:postadresse](https://schema.fintlabs.no/utdanning/postadresse)
Alias: postadresse

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](person.md) | Fysiske private personar |  no  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  no  |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |  yes  |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |  yes  |
| [Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Adresse](adresse.md) |
| Domain Of | [Skole](skole.md), [Aktoer](aktoer.md) |
| Slot URI | [utd:postadresse](https://schema.fintlabs.no/utdanning/postadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:postadresse |
| native | https://schema.fintlabs.no/utdanning/:postadresse |




## LinkML Source

<details>
```yaml
name: postadresse
description: Postadresse.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:postadresse
alias: postadresse
domain_of:
- Skole
- Aktoer
range: Adresse
inlined: true

```
</details>