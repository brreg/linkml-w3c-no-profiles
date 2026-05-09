

# Class: Motivasjon 


_Motivasjonen bak ein kvalitetsmerknad (Web Annotation)._





URI: [oa:Motivation](http://www.w3.org/ns/oa#Motivation)





```mermaid
 classDiagram
    class Motivasjon
    click Motivasjon href "../Motivasjon/"
      Motivasjon : id
        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [oa:Motivation](http://www.w3.org/ns/oa#Motivation) |


## Eigenskapar







  
  





  
  





  
  






  
  
  
  
    
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://example.no/ontology/samt-bu-skole




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oa:Motivation |
| native | samtbuskole:Motivasjon |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Motivasjon
description: Motivasjonen bak ein kvalitetsmerknad (Web Annotation).
from_schema: https://example.no/ontology/samt-bu-skole
slots:
- id
class_uri: oa:Motivation

```
</details>

### Induced

<details>
```yaml
name: Motivasjon
description: Motivasjonen bak ein kvalitetsmerknad (Web Annotation).
from_schema: https://example.no/ontology/samt-bu-skole
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://example.no/ontology/samt-bu-skole
    rank: 1000
    identifier: true
    alias: id
    owner: Motivasjon
    domain_of:
    - Spraak
    - Mediatype
    - Konsept
    - Begrepssamling
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
    - DcatRessurs
    - Kvalitetsdimensjon
    - Kvalitetsmaal
    - Kvalitetsmerknad
    - Kvalitetsmaaling
    - Standard
    - Tekstdel
    - Motivasjon
    range: uriorcurie
    required: true
class_uri: oa:Motivation

```
</details>