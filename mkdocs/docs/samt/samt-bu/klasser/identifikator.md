

# Slot: identifikator 


_Global identifikator (CURIE/URI)._





URI: [samtbuskole:identifikator](https://example.no/ontology/skole#identifikator)
Alias: identifikator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Containerklasse](containerklasse.md) | Containerklasse for alle klasser som kan inngå i datasettet |  no  |
| [Kontaktlaerer](kontaktlaerer.md) | En lærer med ansvar for ei basisgruppe og er skolens kontaktpunkt for elevane... |  no  |
| [Skole](skole.md) | En skole er en privat eller offentlig institusjon eller et lærested hvor lære... |  no  |
| [PrivatVirksomhet](privatvirksomhet.md) | Virksomhet, eller foretak, er betegnelser for en juridisk person eller en org... |  no  |
| [Skoleeier](skoleeier.md) | Superklasse for alle typer skoleeiere |  no  |
| [Kommune](kommune.md) | En kommune er et geografisk avgrenset område som utgjør en egen politisk og a... |  no  |
| [Basisgruppe](basisgruppe.md) | Skoleklasse som hovedsaklig samler elever i ulike fag |  no  |
| [Fylke](fylke.md) | Fylke (etter norrønt fylki) er en betegnelse på et undernasjonalt, regionalt ... |  no  |
| [Elev](elev.md) | En person som går på skole |  no  |
| [Rektor](rektor.md) | Høgaste akademiske leder av en skole |  no  |
| [Person](person.md) | Eit menneske individ |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](uriorcurie.md) |
| Domain Of | [Containerklasse](containerklasse.md), [Skole](skole.md), [Skoleeier](skoleeier.md), [Basisgruppe](basisgruppe.md), [Person](person.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | samtbuskole:identifikator |
| native | samtbuskole:identifikator |




## LinkML Source

<details>
```yaml
name: identifikator
description: Global identifikator (CURIE/URI).
from_schema: https://example.no/ontology/samt-bu-skole
rank: 1000
identifier: true
alias: identifikator
domain_of:
- Containerklasse
- Skole
- Skoleeier
- Basisgruppe
- Person
range: uriorcurie
required: true

```
</details>