

# Slot: forretningsadresse 


_Forretningsadresse._





URI: [utd:forretningsadresse](https://schema.fintlabs.no/utdanning/forretningsadresse)
Alias: forretningsadresse

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
| Range | [Adresse](adresse.md) |
| Domain Of | [Skole](skole.md), [Enhet](enhet.md) |
| Slot URI | [utd:forretningsadresse](https://schema.fintlabs.no/utdanning/forretningsadresse) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:forretningsadresse |
| native | https://schema.fintlabs.no/utdanning/:forretningsadresse |




## LinkML Source

<details>
```yaml
name: forretningsadresse
description: Forretningsadresse.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:forretningsadresse
alias: forretningsadresse
domain_of:
- Skole
- Enhet
range: Adresse
inlined: true

```
</details>