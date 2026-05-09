

# Slot: organisasjonsnavn 


_Organisasjonsnamn._





URI: [utd:organisasjonsnavn](https://schema.fintlabs.no/utdanning/organisasjonsnavn)
Alias: organisasjonsnavn

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
| Range | [String](string.md) |
| Domain Of | [Skole](skole.md), [Enhet](enhet.md) |
| Slot URI | [utd:organisasjonsnavn](https://schema.fintlabs.no/utdanning/organisasjonsnavn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:organisasjonsnavn |
| native | https://schema.fintlabs.no/utdanning/:organisasjonsnavn |




## LinkML Source

<details>
```yaml
name: organisasjonsnavn
description: Organisasjonsnamn.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:organisasjonsnavn
alias: organisasjonsnavn
domain_of:
- Skole
- Enhet
range: string

```
</details>