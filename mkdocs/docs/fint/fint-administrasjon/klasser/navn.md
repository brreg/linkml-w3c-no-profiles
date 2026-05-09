

# Slot: navn 


_Namn på organisasjonselementet._





URI: [adm:namn](https://schema.fintlabs.no/administrasjon/namn)
Alias: navn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Organisasjonselement](organisasjonselement.md) |
| Slot URI | [adm:namn](https://schema.fintlabs.no/administrasjon/namn) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-administrasjon




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adm:namn |
| native | https://schema.fintlabs.no/administrasjon/:navn |




## LinkML Source

<details>
```yaml
name: navn
description: Namn på organisasjonselementet.
from_schema: https://data.norge.no/linkml/fint-administrasjon
rank: 1000
slot_uri: adm:namn
alias: navn
domain_of:
- Organisasjonselement
range: string

```
</details>