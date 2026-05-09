

# Slot: laerling 


_Lærling._





URI: [utd:laerling](https://schema.fintlabs.no/utdanning/laerling)
Alias: laerling

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AvlagtProve](avlagtprove.md) | Ei avlagt prøve for ein lærling |  yes  |
| [Person](person.md) | Fysiske private personar |  yes  |
| [Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Laerling](laerling.md) |
| Domain Of | [AvlagtProve](avlagtprove.md), [Person](person.md), [Virksomhet](virksomhet.md) |
| Slot URI | [utd:laerling](https://schema.fintlabs.no/utdanning/laerling) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:laerling |
| native | https://schema.fintlabs.no/utdanning/:laerling |




## LinkML Source

<details>
```yaml
name: laerling
description: Lærling.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:laerling
alias: laerling
domain_of:
- AvlagtProve
- Person
- Virksomhet
range: Laerling

```
</details>