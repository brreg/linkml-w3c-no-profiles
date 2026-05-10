

# Class: Utdanningsforhold 


_Abstrakt basisklasse for undervisningsforhold i utdanning._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [utd:Utdanningsforhold](https://schema.fintlabs.no/utdanning/Utdanningsforhold)





```mermaid
 classDiagram
    class Utdanningsforhold
    click Utdanningsforhold href "../Utdanningsforhold/"
      Utdanningsforhold <|-- Undervisningsforhold
        click Undervisningsforhold href "../Undervisningsforhold/"
      
      Utdanningsforhold : beskrivelse
        
      Utdanningsforhold : id
        
      
```





## Inheritance
* **Utdanningsforhold**
    * [Undervisningsforhold](undervisningsforhold.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [utd:Utdanningsforhold](https://schema.fintlabs.no/utdanning/Utdanningsforhold) |


## Eigenskapar







  
  

  
  





  
  

  
  





  
  

  
  
    
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [beskrivelse](beskrivelse.md) | 0..1 <br/> [String](string.md) | Beskriven namn eller omtale |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |


















## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-utdanning




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | utd:Utdanningsforhold |
| native | https://schema.fintlabs.no/utdanning/:Utdanningsforhold |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Utdanningsforhold
description: Abstrakt basisklasse for undervisningsforhold i utdanning.
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
slots:
- id
- beskrivelse
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
class_uri: utd:Utdanningsforhold

```
</details>

### Induced

<details>
```yaml
name: Utdanningsforhold
description: Abstrakt basisklasse for undervisningsforhold i utdanning.
from_schema: https://data.norge.no/linkml/fint-utdanning
abstract: true
slot_usage:
  beskrivelse:
    name: beskrivelse
    in_subset:
    - Valgfri
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    identifier: true
    alias: id
    owner: Utdanningsforhold
    domain_of:
    - Gruppe
    - Gruppemedlemskap
    - Utdanningsforhold
    - Elevforhold
    - Elevtilrettelegging
    - Skole
    - Skoleressurs
    - Varsel
    - Eksamen
    - Rom
    - Time
    - FagvurderingAbstrakt
    - OrdensvurderingAbstrakt
    - Anmerkninger
    - Elevfravar
    - Elevvurdering
    - Fravarsoversikt
    - Fraversregistrering
    - Karakterhistorie
    - Sensor
    - AvlagtProve
    - Laerling
    - OtUngdom
    - Avbruddsaarsak
    - Betalingsstatus
    - Bevistype
    - Brevtype
    - Eksamensform
    - Elevkategori
    - Fagmerknad
    - Fagstatus
    - Fravartype
    - Fullfortkode
    - Karakterskala
    - Karakterstatus
    - Karakterverdi
    - OtEnhet
    - OtStatus
    - Provestatus
    - Skoleaar
    - Skoleeiertype
    - Termin
    - Tilrettelegging
    - Varseltype
    - Vitnemalsmerknad
    - Begrep
    - Elev
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    range: uriorcurie
    required: true
  beskrivelse:
    name: beskrivelse
    description: Beskriven namn eller omtale.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-utdanning
    rank: 1000
    slot_uri: fint:beskrivelse
    alias: beskrivelse
    owner: Utdanningsforhold
    domain_of:
    - Gruppe
    - Utdanningsforhold
    - Elevforhold
    - Eksamen
    - Time
    - OtStatus
    - Periode
    range: string
class_uri: utd:Utdanningsforhold

```
</details>