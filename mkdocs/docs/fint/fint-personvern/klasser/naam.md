

# Slot: naam 


_Namn på ressursen._





URI: [pvn:naam](https://schema.fintlabs.no/personvern/naam)
Alias: naam

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |  no  |
| [Kommune](kommune.md) | Liste over Norges kommunar |  no  |
| [Behandlingsgrunnlag](behandlingsgrunnlag.md) | Rettsleg grunnlag for behandling av personopplysningar |  yes  |
| [Fylke](fylke.md) | Liste over Norges fylker |  no  |
| [Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |  no  |
| [Tjeneste](tjeneste.md) | Teneste eller system som behandlar personopplysningar |  yes  |
| [Personopplysning](personopplysning.md) | Opplysningar og vurderingar som kan knytast til enkeltpersonar |  yes  |
| [Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |  no  |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](string.md) |
| Domain Of | [Tjeneste](tjeneste.md), [Behandlingsgrunnlag](behandlingsgrunnlag.md), [Personopplysning](personopplysning.md), [Begrep](begrep.md) |
| Slot URI | [pvn:naam](https://schema.fintlabs.no/personvern/naam) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-personvern




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pvn:naam |
| native | https://schema.fintlabs.no/personvern/:naam |




## LinkML Source

<details>
```yaml
name: naam
description: Namn på ressursen.
from_schema: https://data.norge.no/linkml/fint-personvern
rank: 1000
slot_uri: pvn:naam
alias: naam
domain_of:
- Tjeneste
- Behandlingsgrunnlag
- Personopplysning
- Begrep
range: string

```
</details>