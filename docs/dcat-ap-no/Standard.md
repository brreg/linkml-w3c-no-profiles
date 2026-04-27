

# Class: Standard 


_En standard som en ressurs er i samsvar med._





URI: [dct:Standard](http://purl.org/dc/terms/Standard)





```mermaid
 classDiagram
    class Standard
    click Standard href "../Standard/"
      Standard : har_referanse
        
      Standard : id
        
      Standard : tittel_literal
        
      Standard : versjon
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [dct:Standard](http://purl.org/dc/terms/Standard) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | URI-identifikator for ressursen | direct |
| [tittel_literal](tittel_literal.md) | 1..* <br/> [String](String.md) | Navn/tittel uten språktag | direct |
| [har_referanse](har_referanse.md) | * <br/> [Uri](Uri.md) | Referanse til standarden | direct |
| [versjon](versjon.md) | 0..1 <br/> [String](String.md) | Versjonsnummer | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [standardar](standardar.md) | range | [Standard](Standard.md) |
| [Distribusjon](Distribusjon.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](Standard.md) |
| [Datasett](Datasett.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](Standard.md) |
| [Datatjeneste](Datatjeneste.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](Standard.md) |
| [Katalogpost](Katalogpost.md) | [i_samsvar_med](i_samsvar_med.md) | range | [Standard](Standard.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/dcat-ap-no




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dct:Standard |
| native | https://data.norge.no/linkml/dcat-ap-no/Standard |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Standard
description: En standard som en ressurs er i samsvar med.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slots:
- id
- tittel_literal
- har_referanse
- versjon
slot_usage:
  tittel_literal:
    name: tittel_literal
    in_subset:
    - Obligatorisk
    required: true
class_uri: dct:Standard

```
</details>

### Induced

<details>
```yaml
name: Standard
description: En standard som en ressurs er i samsvar med.
from_schema: https://data.norge.no/linkml/dcat-ap-no
slot_usage:
  tittel_literal:
    name: tittel_literal
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    identifier: true
    alias: id
    owner: Standard
    domain_of:
    - Begrep
    - Begrepssamling
    - Spraak
    - Mediatype
    - Frekvens
    - ProvenanceStatement
    - OdrlPolicy
    - ProvAktivitet
    - ProvAttributering
    - Tidsinstant
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - Standard
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Katalogpost
    range: uriorcurie
    required: true
  tittel_literal:
    name: tittel_literal
    description: Navn/tittel uten språktag.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dct:title
    alias: tittel_literal
    owner: Standard
    domain_of:
    - Standard
    - RegulativRessurs
    range: string
    required: true
    multivalued: true
  har_referanse:
    name: har_referanse
    description: Referanse til standarden.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: rdfs:seeAlso
    alias: har_referanse
    owner: Standard
    domain_of:
    - Standard
    range: uri
    multivalued: true
  versjon:
    name: versjon
    description: Versjonsnummer.
    from_schema: https://data.norge.no/linkml/dcat-ap-no
    rank: 1000
    slot_uri: dcat:version
    alias: versjon
    owner: Standard
    domain_of:
    - Standard
    - Datasett
    - Datatjeneste
    range: string
class_uri: dct:Standard

```
</details>