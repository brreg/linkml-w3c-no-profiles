

# Slot: type 


_Beskriv kva slags type._





URI: [fint:type](https://schema.fintlabs.no/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |  yes  |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |  yes  |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Varsel](varsel.md), [OtStatus](otstatus.md), [Kontaktperson](kontaktperson.md) |
| Slot URI | [fint:type](https://schema.fintlabs.no/type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | fint:type |
| native | https://schema.fintlabs.no/utdanning/:type |




## LinkML Source

<details>
```yaml
name: type
description: Beskriv kva slags type.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: fint:type
alias: type
domain_of:
- Varsel
- OtStatus
- Kontaktperson
range: string

```
</details>