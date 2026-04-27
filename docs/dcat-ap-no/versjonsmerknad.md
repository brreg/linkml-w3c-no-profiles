

# Slot: versjonsmerknad 


_Merknad om endringer i denne versjonen._





URI: [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes)
Alias: versjonsmerknad

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |  no  |
| [Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LangString](LangString.md) |
| Domain Of | [Datasett](Datasett.md), [Datatjeneste](Datatjeneste.md) |
| Slot URI | [adms:versionNotes](http://www.w3.org/ns/adms#versionNotes) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:versionNotes |
| native | https://data.norge.no/linkml/dcat-ap-no/versjonsmerknad |




## LinkML Source

<details>
```yaml
name: versjonsmerknad
description: Merknad om endringer i denne versjonen.
from_schema: https://data.norge.no/linkml/dcat-ap-no
rank: 1000
slot_uri: adms:versionNotes
alias: versjonsmerknad
domain_of:
- Datasett
- Datatjeneste
range: LangString
multivalued: true

```
</details>