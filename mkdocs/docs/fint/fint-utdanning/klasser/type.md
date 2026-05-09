

# Slot: type 


_Type._





URI: [utd:type](https://schema.fintlabs.no/utdanning/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Varsel](varsel.md), [OtStatus](otstatus.md), [Kontaktperson](kontaktperson.md) |
| Slot URI | [utd:type](https://schema.fintlabs.no/utdanning/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:type |
| native | https://schema.fintlabs.no/utdanning/:type |




## LinkML Source

<details>
```yaml
name: type
description: Type.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:type
alias: type
domain_of:
- Varsel
- OtStatus
- Kontaktperson
range: string

```
</details>