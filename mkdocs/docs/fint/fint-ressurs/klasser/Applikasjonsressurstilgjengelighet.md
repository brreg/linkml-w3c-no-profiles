

# Class: Applikasjonsressurstilgjengelighet 


_Kva organisasjonselements brukarar som har tilgang til ein ressurs._





URI: [res:Applikasjonsressurstilgjengelighet](https://schema.fintlabs.no/ressurs/Applikasjonsressurstilgjengelighet)





```mermaid
 classDiagram
    class Applikasjonsressurstilgjengelighet
    click Applikasjonsressurstilgjengelighet href "../Applikasjonsressurstilgjengelighet/"
      Applikasjonsressurstilgjengelighet : gyldighetsperiode
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "1" Periode : gyldighetsperiode
        click Periode href "../Periode/"
    

        
      Applikasjonsressurstilgjengelighet : id
        
      Applikasjonsressurstilgjengelighet : konsument
        
      Applikasjonsressurstilgjengelighet : lisensantall
        
      Applikasjonsressurstilgjengelighet : ressursRef
        
          
    
        
        
        Applikasjonsressurstilgjengelighet --> "1" Applikasjonsressurs : ressursRef
        click Applikasjonsressurs href "../Applikasjonsressurs/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [res:Applikasjonsressurstilgjengelighet](https://schema.fintlabs.no/ressurs/Applikasjonsressurstilgjengelighet) |


## Eigenskapar







  
  

  
  
    
  

  
  

  
  
    
  

  
  
    
  


### Obligatorisk

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [gyldighetsperiode](gyldighetsperiode.md) | 1 <br/> [Periode](periode.md) | Periode ressursen er gyldig for |
| [konsument](konsument.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | Referanse til Organisasjonselement som har tilgang til ressursen |
| [ressursRef](ressursref.md) | 1 <br/> [Applikasjonsressurs](applikasjonsressurs.md) | Ressursen organisasjonselementet har tilgang til |





  
  

  
  

  
  

  
  

  
  





  
  

  
  

  
  
    
  

  
  

  
  


### Valgfri

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [lisensantall](lisensantall.md) | 0..1 <br/> [Integer](integer.md) | Totalt tal på lisensar |






  
  
  
  
    
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  

  
  
  
    
      
    
      
    
      
    
  
  


### Andre

| Namn | Kardinalitet og domene | Beskriving |
| --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](uriorcurie.md) | URI-identifikator for ressursen |








## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RessursContainer](ressurscontainer.md) | [applikasjonsressurstilgjengelegheit](applikasjonsressurstilgjengelegheit.md) | range | [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) |
| [Applikasjonsressurs](applikasjonsressurs.md) | [ressurstilgjengelighet](ressurstilgjengelighet.md) | range | [Applikasjonsressurstilgjengelighet](applikasjonsressurstilgjengelighet.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://data.norge.no/linkml/fint-ressurs




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | res:Applikasjonsressurstilgjengelighet |
| native | https://schema.fintlabs.no/ressurs/:Applikasjonsressurstilgjengelighet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Applikasjonsressurstilgjengelighet
description: Kva organisasjonselements brukarar som har tilgang til ein ressurs.
from_schema: https://data.norge.no/linkml/fint-ressurs
slots:
- id
- gyldighetsperiode
- lisensantall
- konsument
- ressursRef
slot_usage:
  gyldighetsperiode:
    name: gyldighetsperiode
    in_subset:
    - Obligatorisk
    required: true
  lisensantall:
    name: lisensantall
    in_subset:
    - Valgfri
  konsument:
    name: konsument
    in_subset:
    - Obligatorisk
    required: true
  ressursRef:
    name: ressursRef
    in_subset:
    - Obligatorisk
    required: true
class_uri: res:Applikasjonsressurstilgjengelighet

```
</details>

### Induced

<details>
```yaml
name: Applikasjonsressurstilgjengelighet
description: Kva organisasjonselements brukarar som har tilgang til ein ressurs.
from_schema: https://data.norge.no/linkml/fint-ressurs
slot_usage:
  gyldighetsperiode:
    name: gyldighetsperiode
    in_subset:
    - Obligatorisk
    required: true
  lisensantall:
    name: lisensantall
    in_subset:
    - Valgfri
  konsument:
    name: konsument
    in_subset:
    - Obligatorisk
    required: true
  ressursRef:
    name: ressursRef
    in_subset:
    - Obligatorisk
    required: true
attributes:
  id:
    name: id
    description: URI-identifikator for ressursen.
    from_schema: https://data.norge.no/linkml/fint-ressurs
    rank: 1000
    identifier: true
    alias: id
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjon
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    - DigitalEnhet
    - Enhetsgruppe
    - Enhetsgruppemedlemskap
    - Identitet
    - Rettighet
    - Applikasjonskategori
    - Brukertype
    - Enhetstype
    - Handhevingstype
    - Lisensmodell
    - Plattform
    - Produsent
    - Status
    - Begrep
    - Elev
    - Valuta
    - Person
    - Kontaktperson
    - Virksomhet
    range: uriorcurie
    required: true
  gyldighetsperiode:
    name: gyldighetsperiode
    description: Periode ressursen er gyldig for.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-ressurs
    rank: 1000
    slot_uri: fint:gyldighetsperiode
    alias: gyldighetsperiode
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjon
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    - Rettighet
    - Applikasjonskategori
    - Brukertype
    - Enhetstype
    - Handhevingstype
    - Lisensmodell
    - Plattform
    - Produsent
    - Status
    - Begrep
    - Identifikator
    range: Periode
    required: true
    inlined: true
  lisensantall:
    name: lisensantall
    description: Totalt tal på lisensar.
    in_subset:
    - Valgfri
    from_schema: https://data.norge.no/linkml/fint-ressurs
    rank: 1000
    slot_uri: res:lisensantall
    alias: lisensantall
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjonsressurs
    - Applikasjonsressurstilgjengelighet
    range: integer
  konsument:
    name: konsument
    description: Referanse til Organisasjonselement som har tilgang til ressursen.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-ressurs
    rank: 1000
    slot_uri: res:konsument
    alias: konsument
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjonsressurstilgjengelighet
    range: uriorcurie
    required: true
  ressursRef:
    name: ressursRef
    description: Ressursen organisasjonselementet har tilgang til.
    in_subset:
    - Obligatorisk
    from_schema: https://data.norge.no/linkml/fint-ressurs
    rank: 1000
    slot_uri: res:ressursRef
    alias: ressursRef
    owner: Applikasjonsressurstilgjengelighet
    domain_of:
    - Applikasjonsressurstilgjengelighet
    range: Applikasjonsressurs
    required: true
class_uri: res:Applikasjonsressurstilgjengelighet

```
</details>