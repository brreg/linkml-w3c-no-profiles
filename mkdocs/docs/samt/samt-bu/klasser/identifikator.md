

# Class: Identifikator 


_Ein alternativ identifikator for ein ressurs._





URI: [adms:Identifier](http://www.w3.org/ns/adms#Identifier)





```mermaid
 classDiagram
    class Identifikator
    click Identifikator href "../Identifikator/"
      Identifikator : id
        
      Identifikator : notasjon
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [adms:Identifier](http://www.w3.org/ns/adms#Identifier) |


## Eigenskapar







  
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [notasjon](notasjon.md) | 1 <br/> [String](string.md) | Notasjon/kode for identifikatoren |





  
  

  
  





  
  

  
  






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Datasett](datasett.md) | [annen_identifikator](annen_identifikator.md) | range | [Identifikator](identifikator.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | adms:Identifier |
| native | samtbuskole:Identifikator |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Identifikator
description: Ein alternativ identifikator for ein ressurs.
from_schema: https://example.no/ontology/samt-bu-skole
slots:
- id
- notasjon
slot_usage:
  notasjon:
    name: notasjon
    in_subset:
    - Obligatorisk
    required: true
class_uri: adms:Identifier

```
</details>

### Induced

<details>
```yaml
name: Identifikator
description: Ein alternativ identifikator for ein ressurs.
from_schema: https://example.no/ontology/samt-bu-skole
slot_usage:
  notasjon:
    name: notasjon
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: Identifikator
    domain_of:
    - Containerklasse
    - Skole
    - Skoleeier
    - Basisgruppe
    - Person
    - KatalogisertRessurs
    - Aktor
    - Kontaktopplysning
    - Tidsrom
    - RegulativRessurs
    - Identifikator
    - Rettighetserklaring
    - Sjekksum
    - Gebyr
    - Relasjon
    - Distribusjon
    - Datasett
    - Katalogpost
    - Mediatype
    - Konsept
    - Begrepssamling
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    range: uriorcurie
    required: true
  notasjon:
    name: notasjon
    description: Notasjon/kode for identifikatoren.
    in_subset:
    - Obligatorisk
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    slot_uri: skos:notation
    alias: notasjon
    owner: Identifikator
    domain_of:
    - Identifikator
    range: string
    required: true
class_uri: adms:Identifier

```
</details>