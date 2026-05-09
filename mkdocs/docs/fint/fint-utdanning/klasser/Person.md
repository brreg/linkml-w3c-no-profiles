

# Slot: person 


_Referanse til Person i Administrasjon-domenet._





URI: [utd:person](https://schema.fintlabs.no/utdanning/person)
Alias: person

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |  yes  |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |  yes  |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |  yes  |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Elev](elev.md), [Skoleressurs](skoleressurs.md), [Laerling](laerling.md), [OtUngdom](otungdom.md) |
| Slot URI | [utd:person](https://schema.fintlabs.no/utdanning/person) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:person |
| native | https://schema.fintlabs.no/utdanning/:person |




## LinkML Source

<details>
```yaml
name: person
description: Referanse til Person i Administrasjon-domenet.
from_schema: https://data.norge.no/linkml/fint-utdanning
rank: 1000
slot_uri: utd:person
alias: person
domain_of:
- Elev
- Skoleressurs
- Laerling
- OtUngdom
range: uriorcurie

```
</details>