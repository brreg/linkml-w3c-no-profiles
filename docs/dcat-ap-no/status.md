

# Slot: status 


_Status for ressursen fra et kontrollert vokabular._





URI: [adms:status](http://www.w3.org/ns/adms#status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Katalogpost](Katalogpost.md) | En katalogpost som beskriver en ressurs i katalogen |  yes  |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Begrep](Begrep.md) |
| Domain Of | [Distribusjon](Distribusjon.md), [Datatjeneste](Datatjeneste.md), [Katalogpost](Katalogpost.md) |
| Slot URI | [adms:status](http://www.w3.org/ns/adms#status) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:status |
| native | https://data.norge.no/linkml/dcat-ap-no/status |




## LinkML Source

<details>
```yaml
name: status
description: Status for ressursen fra et kontrollert vokabular.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: adms:status
alias: status
domain_of:
- Distribusjon
- Datatjeneste
- Katalogpost
range: Begrep

```
</details>