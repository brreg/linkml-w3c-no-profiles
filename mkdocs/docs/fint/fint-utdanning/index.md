# fint-utdanning

```mermaid
erDiagram
Adresse {
    stringList adresselinje  
    string postnummer  
    string poststed  
}
Anmerkninger {
    uriorcurie id  
    integer atferd  
    integer orden  
}
Arstrinn {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Avbruddsaarsak {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
AvlagtProve {
    uriorcurie id  
    uriorcurieList laerling  
    date provedato  
}
Betalingsstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Bevistype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Brevtype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Eksamen {
    uriorcurie id  
    string beskrivelse  
    string navn  
    datetime oppmoetetidspunkt  
}
Eksamensform {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Eksamensgruppe {
    datetime eksamensdato  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Eksamensgruppemedlemskap {
    boolean delegert  
    uriorcurie delegertTil  
    boolean foretrukketSensor  
    boolean foretrukketSkole  
    string kandidatnummer  
    uriorcurie id  
}
Eksamensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Elev {
    uriorcurie id  
}
Elevforhold {
    uriorcurie id  
    date avbruddsdato  
    string beskrivelse  
    boolean tosprakligFagopplaering  
}
Elevfravar {
    uriorcurie id  
}
Elevkategori {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Elevtilrettelegging {
    uriorcurie id  
}
Elevvurdering {
    uriorcurie id  
}
Fag {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Faggruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Faggruppemedlemskap {
    uriorcurie id  
}
Fagmerknad {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fagstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fravarsoversikt {
    uriorcurie id  
}
Fravarsprosent {
    integer fravaerstimer  
    integer prosent  
    integer undervisningstimer  
}
Fravartype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fraversregistrering {
    uriorcurie id  
    boolean forersPaaVitnemaal  
    string kommentar  
}
Fullfortkode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Fylke {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Halvaarsfagvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Halvaarsordensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Identifikator {
    string identifikatorverdi  
}
Karakterhistorie {
    uriorcurie id  
    datetime endretDato  
}
Karakterskala {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
    uriorcurie vigoreferanse  
}
Karakterstatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Karakterverdi {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Kjonn {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Klasse {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Klassemedlemskap {
    uriorcurie id  
}
Kommune {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Kontaktinformasjon {
    string epostadresse  
    string mobiltelefonnummer  
    string nettsted  
    string sip  
    string telefonnummer  
}
Kontaktlaerergruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Kontaktlaerergruppemedlemskap {
    uriorcurie id  
}
Kontaktperson {
    uriorcurie id  
    string type  
}
Laerling {
    uriorcurie id  
    uriorcurie bedrift  
    string kontraktstype  
}
Landkode {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
OtEnhet {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
OtStatus {
    uriorcurie id  
    string beskrivelse  
    string kode  
    string navn  
    boolean passiv  
    string type  
}
OtUngdom {
    uriorcurie id  
}
Periode {
    string beskrivelse  
    datetime slutt  
    datetime start  
}
Person {
    uriorcurie id  
    string bilde  
    date fodselsdato  
    uriorcurieList laerling  
    uriorcurie otungdom  
    uriorcurie personalressurs  
}
Persongruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Persongruppemedlemskap {
    uriorcurie id  
}
Personnavn {
    string etternavn  
    string fornavn  
    string mellomnavn  
}
Programomrade {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Programomrademedlemskap {
    uriorcurie id  
}
Provestatus {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Rom {
    uriorcurie id  
    string navn  
}
Sensor {
    uriorcurie id  
    boolean aktiv  
    integer sensornummer  
}
Skole {
    uriorcurie id  
    string domenenavn  
    string juridiskNavn  
    string navn  
    uriorcurie organisasjon  
    string organisasjonsnavn  
    uriorcurie vigoreferanse  
}
Skoleaar {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Skoleeiertype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Skoleressurs {
    uriorcurie id  
    uriorcurie personalressurs  
}
Sluttfagvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Sluttordensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Spraak {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Termin {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Tilrettelegging {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Time {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Underveisfagvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Underveisordensvurdering {
    uriorcurie id  
    string kommentar  
    datetime vurderingsdato  
}
Undervisningsforhold {
    uriorcurie arbeidsforhold  
    uriorcurie id  
    string beskrivelse  
}
Undervisningsgruppe {
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Undervisningsgruppemedlemskap {
    uriorcurie id  
}
Utdanningsprogram {
    uriorcurie grepreferanse  
    uriorcurie vigoreferanse  
    uriorcurie id  
    string beskrivelse  
    string navn  
}
Varsel {
    uriorcurie id  
    integer fravarsprosent  
    date sendt  
    string tekst  
}
Varseltype {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}
Vitnemalsmerknad {
    uriorcurie id  
    string kode  
    string navn  
    boolean passiv  
}

Adresse ||--|o Landkode : "land"
Anmerkninger ||--|o Skoleaar : "skoleaar"
Arstrinn ||--}o Klasse : "klasse"
Arstrinn ||--}o Programomrade : "programomrade"
Avbruddsaarsak ||--|o Periode : "gyldighetsperiode"
AvlagtProve ||--|o Bevistype : "bevistype"
AvlagtProve ||--|o Brevtype : "brevtype"
AvlagtProve ||--|o Fullfortkode : "fullfortkode"
AvlagtProve ||--|o Provestatus : "provestatus"
Betalingsstatus ||--|o Periode : "gyldighetsperiode"
Bevistype ||--|o Periode : "gyldighetsperiode"
Brevtype ||--|o Periode : "gyldighetsperiode"
Eksamen ||--|o Eksamensgruppe : "eksamensgruppe"
Eksamen ||--|o Periode : "tidsrom"
Eksamen ||--}o Rom : "rom"
Eksamensform ||--|o Periode : "gyldighetsperiode"
Eksamensgruppe ||--|o Eksamen : "eksamen"
Eksamensgruppe ||--|o Eksamensform : "eksamensform"
Eksamensgruppe ||--|o Skoleaar : "skoleaar"
Eksamensgruppe ||--|| Fag : "fag"
Eksamensgruppe ||--|| Skole : "skole"
Eksamensgruppe ||--|| Termin : "termin"
Eksamensgruppe ||--}o Eksamensgruppemedlemskap : "gruppemedlemskap"
Eksamensgruppe ||--}o Sensor : "sensor"
Eksamensgruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Eksamensgruppemedlemskap ||--|o Betalingsstatus : "betalingsstatus"
Eksamensgruppemedlemskap ||--|o Karakterstatus : "nus"
Eksamensgruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Eksamensgruppemedlemskap ||--|| Eksamensgruppe : "eksamensgruppe"
Eksamensgruppemedlemskap ||--|| Elevforhold : "elevforhold"
Eksamensvurdering ||--|o Fag : "fag"
Eksamensvurdering ||--|o Karakterverdi : "karakter"
Eksamensvurdering ||--|o Skoleaar : "skoleaar"
Eksamensvurdering ||--|| Eksamensgruppe : "eksamensgruppe"
Eksamensvurdering ||--|| Elevvurdering : "elevvurdering"
Eksamensvurdering ||--}o Karakterhistorie : "karakterhistorie"
Elev ||--|o Identifikator : "elevnummer"
Elev ||--|o Person : "person"
Elevforhold ||--|o Avbruddsaarsak : "avbruddsarsak"
Elevforhold ||--|o Elevkategori : "kategori"
Elevforhold ||--|o Elevvurdering : "elevvurdering"
Elevforhold ||--|o Fravarsoversikt : "elevfravar"
Elevforhold ||--|o Skoleaar : "skoleaar"
Elevforhold ||--|| Elev : "elev"
Elevforhold ||--|| Skole : "skole"
Elevforhold ||--}o Eksamensgruppemedlemskap : "eksamensgruppemedlemskap"
Elevforhold ||--}o Elevfravar : "fraversregistreringer"
Elevforhold ||--}o Elevtilrettelegging : "tilrettelegging"
Elevforhold ||--}o Faggruppemedlemskap : "faggruppemedlemskap"
Elevforhold ||--}o Klassemedlemskap : "klassemedlemskap"
Elevforhold ||--}o Kontaktlaerergruppemedlemskap : "kontaktlaerergruppemedlemskap"
Elevforhold ||--}o Persongruppemedlemskap : "persongruppemedlemskap"
Elevforhold ||--}o Programomrademedlemskap : "programomrademedlemskap"
Elevforhold ||--}o Undervisningsgruppemedlemskap : "undervisningsgruppemedlemskap"
Elevfravar ||--|| Elevforhold : "elevforhold"
Elevfravar ||--}o Fraversregistrering : "fraversregistrering"
Elevkategori ||--|o Periode : "gyldighetsperiode"
Elevtilrettelegging ||--|o Eksamensform : "eksamensform"
Elevtilrettelegging ||--|o Elevforhold : "elev"
Elevtilrettelegging ||--|o Tilrettelegging : "tilrettelegging"
Elevvurdering ||--|o Vitnemalsmerknad : "vitnemalsmerknad"
Elevvurdering ||--|| Elevforhold : "elevforhold"
Elevvurdering ||--}o Eksamensvurdering : "eksamensvurdering"
Elevvurdering ||--}o Halvaarsfagvurdering : "halvaarsfagvurdering"
Elevvurdering ||--}o Halvaarsordensvurdering : "halvaarsordensvurdering"
Elevvurdering ||--}o Sluttfagvurdering : "sluttfagvurdering"
Elevvurdering ||--}o Sluttordensvurdering : "sluttordensvurdering"
Elevvurdering ||--}o Underveisfagvurdering : "underveisfagvurdering"
Elevvurdering ||--}o Underveisordensvurdering : "underveisordensvurdering"
Fag ||--}o Eksamensgruppe : "eksamensgruppe"
Fag ||--}o Faggruppe : "faggruppe"
Fag ||--}o Programomrade : "programomrade"
Fag ||--}o Skole : "skole"
Fag ||--}o Tilrettelegging : "tilrettelegging"
Fag ||--}o Undervisningsgruppe : "undervisningsgruppe"
Faggruppe ||--|o Skole : "skole"
Faggruppe ||--|o Skoleaar : "skoleaar"
Faggruppe ||--|| Fag : "fag"
Faggruppe ||--}o Faggruppemedlemskap : "faggruppemedlemskap"
Faggruppemedlemskap ||--|o Elevforhold : "elevforhold"
Faggruppemedlemskap ||--|o Faggruppe : "faggruppe"
Faggruppemedlemskap ||--|o Fagmerknad : "fagmerknad"
Faggruppemedlemskap ||--|o Fagstatus : "fagstatus"
Faggruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Faggruppemedlemskap ||--}o Varsel : "varsel"
Fagmerknad ||--|o Periode : "gyldighetsperiode"
Fagstatus ||--|o Periode : "gyldighetsperiode"
Fravarsoversikt ||--|| Elevforhold : "elevforhold"
Fravarsoversikt ||--|| Fag : "fag"
Fravarsoversikt ||--|| Fravarsprosent : "halvaar, skoleaarFravar"
Fravartype ||--|o Periode : "gyldighetsperiode"
Fraversregistrering ||--|o Elevfravar : "elevfravar"
Fraversregistrering ||--|o Faggruppe : "faggruppe"
Fraversregistrering ||--|o Skoleressurs : "registrertAv"
Fraversregistrering ||--|| Fravartype : "fravartype"
Fraversregistrering ||--|| Periode : "periode"
Fraversregistrering ||--|| Undervisningsgruppe : "undervisningsgruppe"
Fullfortkode ||--|o Periode : "gyldighetsperiode"
Fylke ||--|o Periode : "gyldighetsperiode"
Fylke ||--}o Kommune : "kommune"
Halvaarsfagvurdering ||--|o Fag : "fag"
Halvaarsfagvurdering ||--|o Karakterverdi : "karakter"
Halvaarsfagvurdering ||--|o Skoleaar : "skoleaar"
Halvaarsfagvurdering ||--|| Elevvurdering : "elevvurdering"
Halvaarsordensvurdering ||--|o Karakterverdi : "atferd, orden"
Halvaarsordensvurdering ||--|o Skoleaar : "skoleaar"
Halvaarsordensvurdering ||--|| Elevvurdering : "elevvurdering"
Identifikator ||--|o Periode : "gyldighetsperiode"
Karakterhistorie ||--|o Karakterstatus : "karakterstatus, opprinneligKarakterstatus"
Karakterhistorie ||--|o Karakterverdi : "karakterverdi, opprinneligKarakterverdi"
Karakterhistorie ||--|o Skoleressurs : "oppdatertAv"
Karakterskala ||--|o Periode : "gyldighetsperiode"
Karakterskala ||--}o Karakterverdi : "verdi"
Karakterstatus ||--|o Periode : "gyldighetsperiode"
Karakterverdi ||--|o Periode : "gyldighetsperiode"
Karakterverdi ||--|| Karakterskala : "skala"
Kjonn ||--|o Periode : "gyldighetsperiode"
Klasse ||--|o Skole : "skole"
Klasse ||--|o Skoleaar : "skoleaar"
Klasse ||--}o Arstrinn : "trinn"
Klasse ||--}o Klassemedlemskap : "klassemedlemskap"
Klasse ||--}o Kontaktlaerergruppe : "kontaktlaerergruppe"
Klasse ||--}o Termin : "termin"
Klasse ||--}o Undervisningsforhold : "undervisningsforhold"
Klassemedlemskap ||--|o Elevforhold : "elevforhold"
Klassemedlemskap ||--|o Klasse : "klasse"
Klassemedlemskap ||--|o Periode : "gyldighetsperiode"
Kommune ||--|o Periode : "gyldighetsperiode"
Kommune ||--|| Fylke : "fylke"
Kontaktlaerergruppe ||--|o Skole : "skole"
Kontaktlaerergruppe ||--|o Skoleaar : "skoleaar"
Kontaktlaerergruppe ||--}o Kontaktlaerergruppemedlemskap : "gruppemedlemskap"
Kontaktlaerergruppe ||--}o Termin : "termin"
Kontaktlaerergruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Kontaktlaerergruppe ||--}| Klasse : "klasse"
Kontaktlaerergruppemedlemskap ||--|o Elevforhold : "elevforhold"
Kontaktlaerergruppemedlemskap ||--|o Kontaktlaerergruppe : "kontaktlaerergruppe"
Kontaktlaerergruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Kontaktperson ||--|o Kontaktinformasjon : "kontaktinformasjon"
Kontaktperson ||--|o Personnavn : "kontaktperson_navn"
Kontaktperson ||--}o Person : "kontaktperson"
Laerling ||--|o Periode : "laretid"
Laerling ||--|o Programomrade : "programomrade"
Laerling ||--|| Person : "person"
Laerling ||--}o AvlagtProve : "avlagtprove"
Landkode ||--|o Periode : "gyldighetsperiode"
OtEnhet ||--|o Periode : "gyldighetsperiode"
OtEnhet ||--|| Kommune : "kommune"
OtStatus ||--|o Periode : "gyldighetsperiode"
OtUngdom ||--|o OtEnhet : "enhet"
OtUngdom ||--|o OtStatus : "status"
OtUngdom ||--|o Programomrade : "programomrade"
OtUngdom ||--|| Person : "person"
Person ||--|o Adresse : "bostedsadresse, postadresse"
Person ||--|o Elev : "elev"
Person ||--|o Kjonn : "kjonn"
Person ||--|o Kommune : "kommune"
Person ||--|o Kontaktinformasjon : "kontaktinformasjon"
Person ||--|o Spraak : "maalform, morsmaal"
Person ||--|| Identifikator : "fodselsnummer"
Person ||--|| Personnavn : "person_navn"
Person ||--}o Kontaktperson : "parorende"
Person ||--}o Landkode : "statsborgerskap"
Person ||--}o Person : "foreldre, foreldreansvar"
Persongruppe ||--|o Skole : "skole"
Persongruppe ||--|o Skoleaar : "skoleaar"
Persongruppe ||--}o Elevforhold : "elev"
Persongruppe ||--}o Persongruppemedlemskap : "persongruppemedlemskap"
Persongruppe ||--}o Skoleressurs : "skoleressurs"
Persongruppe ||--}o Termin : "termin"
Persongruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Persongruppemedlemskap ||--|o Elevforhold : "elevforhold"
Persongruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Persongruppemedlemskap ||--|o Persongruppe : "persongruppe"
Programomrade ||--}o Arstrinn : "trinn"
Programomrade ||--}o Programomrademedlemskap : "gruppemedlemskap"
Programomrademedlemskap ||--|o Elevforhold : "elevforhold"
Programomrademedlemskap ||--|o Periode : "gyldighetsperiode"
Programomrademedlemskap ||--|o Programomrade : "programomrade"
Provestatus ||--|o Periode : "gyldighetsperiode"
Rom ||--}o Eksamen : "eksamen"
Rom ||--}o Time : "skuletime"
Sensor ||--|| Eksamensgruppe : "eksamensgruppe"
Sensor ||--|| Skoleressurs : "skoleressurs"
Skole ||--|o Adresse : "forretningsadresse, postadresse"
Skole ||--|o Identifikator : "organisasjonsnummer, skolenummer"
Skole ||--|o Skoleeiertype : "skoleeierType"
Skole ||--}o Eksamensgruppe : "eksamensgruppe"
Skole ||--}o Fag : "fag"
Skole ||--}o Faggruppe : "faggruppe"
Skole ||--}o Klasse : "klasse"
Skole ||--}o Kontaktlaerergruppe : "kontaktlaerergruppe"
Skole ||--}o Skoleressurs : "skoleressurs"
Skole ||--}o Utdanningsprogram : "utdanningsprogram"
Skoleaar ||--|o Periode : "gyldighetsperiode"
Skoleeiertype ||--|o Periode : "gyldighetsperiode"
Skoleressurs ||--|o Identifikator : "feidenavn"
Skoleressurs ||--|o Person : "person"
Skoleressurs ||--}o Sensor : "sensor"
Skoleressurs ||--}o Skole : "skole"
Sluttfagvurdering ||--|o Eksamensgruppe : "eksamensgruppe"
Sluttfagvurdering ||--|o Fag : "fag"
Sluttfagvurdering ||--|o Karakterverdi : "karakter"
Sluttfagvurdering ||--|o Skoleaar : "skoleaar"
Sluttfagvurdering ||--|| Elevvurdering : "elevvurdering"
Sluttfagvurdering ||--}o Karakterhistorie : "karakterhistorie"
Sluttordensvurdering ||--|o Karakterverdi : "atferd, orden"
Sluttordensvurdering ||--|o Skoleaar : "skoleaar"
Sluttordensvurdering ||--|| Elevvurdering : "elevvurdering"
Spraak ||--|o Periode : "gyldighetsperiode"
Termin ||--|o Periode : "gyldighetsperiode"
Tilrettelegging ||--|o Periode : "gyldighetsperiode"
Time ||--|o Periode : "tidsrom"
Time ||--}o Rom : "rom"
Time ||--}| Undervisningsforhold : "undervisningsforhold"
Time ||--}| Undervisningsgruppe : "undervisningsgruppe"
Underveisfagvurdering ||--|o Fag : "fag"
Underveisfagvurdering ||--|o Karakterverdi : "karakter"
Underveisfagvurdering ||--|o Skoleaar : "skoleaar"
Underveisfagvurdering ||--|| Elevvurdering : "elevvurdering"
Underveisordensvurdering ||--|o Karakterverdi : "atferd, orden"
Underveisordensvurdering ||--|o Skoleaar : "skoleaar"
Underveisordensvurdering ||--|| Elevvurdering : "elevvurdering"
Undervisningsforhold ||--|o Skoleressurs : "skoleressurs"
Undervisningsforhold ||--}o Eksamensgruppe : "eksamensgruppe"
Undervisningsforhold ||--}o Klasse : "klasse"
Undervisningsforhold ||--}o Kontaktlaerergruppe : "kontaktlaerergruppe"
Undervisningsforhold ||--}o Time : "skuletime"
Undervisningsgruppe ||--|o Skole : "skole"
Undervisningsgruppe ||--|o Skoleaar : "skoleaar"
Undervisningsgruppe ||--}o Termin : "termin"
Undervisningsgruppe ||--}o Time : "skuletime"
Undervisningsgruppe ||--}o Undervisningsforhold : "undervisningsforhold"
Undervisningsgruppe ||--}o Undervisningsgruppemedlemskap : "gruppemedlemskap"
Undervisningsgruppe ||--}| Fag : "fag"
Undervisningsgruppemedlemskap ||--|o Elevforhold : "elevforhold"
Undervisningsgruppemedlemskap ||--|o Periode : "gyldighetsperiode"
Undervisningsgruppemedlemskap ||--|o Undervisningsgruppe : "undervisningsgruppe"
Utdanningsprogram ||--}o Programomrade : "programomrade"
Utdanningsprogram ||--}o Skole : "skole"
Varsel ||--|o Skoleressurs : "karakteransvarlig, utsteder"
Varsel ||--|o Varseltype : "type"
Varsel ||--}o Faggruppemedlemskap : "faggruppemedlemskap"
Varseltype ||--|o Periode : "gyldighetsperiode"
Vitnemalsmerknad ||--|o Periode : "gyldighetsperiode"

```



FINT-domenemodell for utdanning. Dekkjer elevar, skular, skoleressursar, elevforhold, undervisningsforhold, klasser, undervisningsgrupper, faggrupper, kontaktlærergrupper, utdanningsprogram, programområde, vurdering, lærling og OT.


URI: https://data.norge.no/linkml/fint-utdanning

Name: fint-utdanning



## Classes

| Class | Description |
| --- | --- |
| [Adresse](klasser/adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](klasser/aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](klasser/enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](klasser/virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](klasser/person.md) | Fysiske private personar |
| [Anmerkninger](klasser/anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |
| [Avbruddsaarsak](klasser/avbruddsaarsak.md) | Årsak til avbrot frå opplæring |
| [AvlagtProve](klasser/avlagtprove.md) | Ei avlagt prøve for ein lærling |
| [Begrep](klasser/begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](klasser/fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](klasser/kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](klasser/kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](klasser/landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](klasser/spraak.md) | Verdiar for språk (2 bokstavar) |
| [Betalingsstatus](klasser/betalingsstatus.md) | Betalingsstatus for eksamensavgift |
| [Bevistype](klasser/bevistype.md) | Type kompetansebevis for lærling |
| [Brevtype](klasser/brevtype.md) | Type brev knytt til lærlingprøve |
| [Eksamen](klasser/eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |
| [Eksamensform](klasser/eksamensform.md) | Form for gjennomføring av eksamen |
| [Elev](klasser/elev.md) | Ein elev registrert i skulesystemet |
| [Elevforhold](klasser/elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |
| [Elevfravar](klasser/elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |
| [Elevkategori](klasser/elevkategori.md) | Kategori for eit elevforhold (t |
| [Elevtilrettelegging](klasser/elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |
| [Elevvurdering](klasser/elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |
| [Fagmerknad](klasser/fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |
| [Fagstatus](klasser/fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |
| [FagvurderingAbstrakt](klasser/fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensvurdering](klasser/eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsfagvurdering](klasser/halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttfagvurdering](klasser/sluttfagvurdering.md) | Sluttkarakter i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisfagvurdering](klasser/underveisfagvurdering.md) | Underveisfagvurdering for ein elev |
| [Fravarsoversikt](klasser/fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |
| [Fravarsprosent](klasser/fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |
| [Fravartype](klasser/fravartype.md) | Type fråvær (t |
| [Fraversregistrering](klasser/fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |
| [Fullfortkode](klasser/fullfortkode.md) | Kode for fullførtresultat av lærling |
| [Gruppe](klasser/gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arstrinn](klasser/arstrinn.md) | Eit årstrinn i skulen (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppe](klasser/eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fag](klasser/fag.md) | Eit skulefag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppe](klasser/faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klasse](klasser/klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppe](klasser/kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppe](klasser/persongruppe.md) | Ei gruppe elevar definert for personlege føremål |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrade](klasser/programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppe](klasser/undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Utdanningsprogram](klasser/utdanningsprogram.md) | Eit utdanningsprogram (t |
| [Gruppemedlemskap](klasser/gruppemedlemskap.md) | Abstrakt basisklasse for gruppemedlemskapar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppemedlemskap](klasser/eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppemedlemskap](klasser/faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klassemedlemskap](klasser/klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppemedlemskap](klasser/kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppemedlemskap](klasser/persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrademedlemskap](klasser/programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppemedlemskap](klasser/undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |
| [Identifikator](klasser/identifikator.md) | Unik identifikasjon til eit objekt |
| [Karakterhistorie](klasser/karakterhistorie.md) | Historikk over endringar i ein karakter |
| [Karakterskala](klasser/karakterskala.md) | Skala for karaktersetjing (t |
| [Karakterstatus](klasser/karakterstatus.md) | Status for ein karakter (t |
| [Karakterverdi](klasser/karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |
| [Kontaktinformasjon](klasser/kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](klasser/kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Laerling](klasser/laerling.md) | Ein lærling i yrkesopplæring |
| [Matrikkelnummer](klasser/matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [OrdensvurderingAbstrakt](klasser/ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsordensvurdering](klasser/halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttordensvurdering](klasser/sluttordensvurdering.md) | Sluttordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisordensvurdering](klasser/underveisordensvurdering.md) | Underveisordensvurdering for ein elev |
| [OtEnhet](klasser/otenhet.md) | Eining i oppfølgingstenesta (OT) |
| [OtStatus](klasser/otstatus.md) | Status for ein ungdom i oppfølgingstenesta |
| [OtUngdom](klasser/otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |
| [Periode](klasser/periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](klasser/personnavn.md) | Namn på ein person |
| [Provestatus](klasser/provestatus.md) | Status for ei lærlingprøve |
| [Rom](klasser/rom.md) | Eit rom eller lokale ved ein skule |
| [Sensor](klasser/sensor.md) | Ein sensor for ein eksamen |
| [Skole](klasser/skole.md) | Ein skule eller opplæringsinstitusjon |
| [Skoleaar](klasser/skoleaar.md) | Eit skoleår (t |
| [Skoleeiertype](klasser/skoleeiertype.md) | Type skuleeigartilknyting |
| [Skoleressurs](klasser/skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |
| [Termin](klasser/termin.md) | Ein skuleterm (t |
| [Tilrettelegging](klasser/tilrettelegging.md) | Type tilrettelegging for elevar (t |
| [Time](klasser/time.md) | Ein time i timeplanen |
| [UtdanningContainer](klasser/utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |
| [Utdanningsforhold](klasser/utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsforhold](klasser/undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |
| [Valuta](klasser/valuta.md) | Valutakodar for offisielle valutaer |
| [Varsel](klasser/varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |
| [Varseltype](klasser/varseltype.md) | Type varsel knytt til ein elev |
| [Vitnemalsmerknad](klasser/vitnemalsmerknad.md) | Merknad på vitnemål |



## Slots

| Slot | Description |
| --- | --- |
| [adresse](klasser/adresse.md) | Adresse til matrikkeleining |
| [adresselinje](klasser/adresselinje.md) | Adresseinformasjon |
| [aktiv](klasser/aktiv.md) | Angir om sensoren er aktiv |
| [anmerkningar](klasser/anmerkningar.md) | Alle anmerkningar i containeren |
| [arbeidsforhold](klasser/arbeidsforhold.md) | Referanse til Arbeidsforhold i Administrasjon-domenet |
| [arstrinn](klasser/arstrinn.md) | Alle årstrinns-objekt i containeren |
| [atferd](klasser/atferd.md) | Åtferdskarakter |
| [avbruddsaarsaker](klasser/avbruddsaarsaker.md) | Alle avbruddsårsakar i containeren |
| [avbruddsarsak](klasser/avbruddsarsak.md) | Årsak til avbrot frå opplæring |
| [avbruddsdato](klasser/avbruddsdato.md) | Dato for avbrot frå opplæring |
| [avlagteprover](klasser/avlagteprover.md) | Alle avlagde prøver i containeren |
| [avlagtprove](klasser/avlagtprove.md) | Avlagde prøver |
| [bedrift](klasser/bedrift.md) | Referanse til bedrifta lærlingen er i |
| [beskrivelse](klasser/beskrivelse.md) | Beskriven namn eller omtale |
| [betalingsstatus](klasser/betalingsstatus.md) | Betalingsstatus |
| [bevistypar](klasser/bevistypar.md) | Alle bevistypar i containeren |
| [bevistype](klasser/bevistype.md) | Type kompetansebevis |
| [bilde](klasser/bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](klasser/bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](klasser/bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brevtypar](klasser/brevtypar.md) | Alle brevtypar i containeren |
| [brevtype](klasser/brevtype.md) | Type brev |
| [bruksnummer](klasser/bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [delegert](klasser/delegert.md) | Angir om deltakinga er delegert |
| [delegertTil](klasser/delegerttil.md) | Referanse til den deltakinga er delegert til |
| [domenenavn](klasser/domenenavn.md) | Domenenamn for skulen |
| [eksamen](klasser/eksamen.md) | Eksamen |
| [eksamensdato](klasser/eksamensdato.md) | Dato for eksamenen |
| [eksamensform](klasser/eksamensform.md) | Eksamensform |
| [eksamensformer](klasser/eksamensformer.md) | Alle eksamensformer i containeren |
| [eksamensgruppe](klasser/eksamensgruppe.md) | Eksamensgruppe |
| [eksamensgruppemedlemskap](klasser/eksamensgruppemedlemskap.md) | Eksamensgruppemedlemskap |
| [eksamensgrupper](klasser/eksamensgrupper.md) | Alle eksamensgrupper i containeren |
| [eksamensvurdering](klasser/eksamensvurdering.md) | Eksamensvurderingar |
| [elev](klasser/elev.md) | Referanse til Elev (Utdanning) |
| [elevar](klasser/elevar.md) | Alle elevar i containeren |
| [elevforhold](klasser/elevforhold.md) | Elevforholdet dette gjeld |
| [elevfravar](klasser/elevfravar.md) | Fråværsobjekt for elev |
| [elevkategoriar](klasser/elevkategoriar.md) | Alle elevkategoriar i containeren |
| [elevnummer](klasser/elevnummer.md) | Skulens interne elevnummer |
| [elevtilrettelegging](klasser/elevtilrettelegging.md) | Alle elevtilretteleggingar i containeren |
| [elevvurdering](klasser/elevvurdering.md) | Elevvurderingsobjekt |
| [endretDato](klasser/endretdato.md) | Dato og tidspunkt for endringa |
| [enhet](klasser/enhet.md) | OT-eining |
| [epostadresse](klasser/epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](klasser/etternavn.md) | Etternamn til personen |
| [fag](klasser/fag.md) | Fag |
| [faggruppe](klasser/faggruppe.md) | Faggruppe |
| [faggruppemedlemskap](klasser/faggruppemedlemskap.md) | Faggruppemedlemskap |
| [faggrupper](klasser/faggrupper.md) | Alle faggrupper i containeren |
| [fagmerknad](klasser/fagmerknad.md) | Merknad til faget |
| [fagmerknader](klasser/fagmerknader.md) | Alle fagmerknadar i containeren |
| [fagstatus](klasser/fagstatus.md) | Fagstatus |
| [feidenavn](klasser/feidenavn.md) | Feide-identifikator |
| [festenummer](klasser/festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](klasser/fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](klasser/fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](klasser/foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](klasser/foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forersPaaVitnemaal](klasser/forerspaavitnemaal.md) | Angir om fråværet vert ført på vitnemålet |
| [foretrukketSensor](klasser/foretrukketsensor.md) | Angir om sensor er føretrekt |
| [foretrukketSkole](klasser/foretrukketskole.md) | Angir om skulen er føretrekt for eksamenen |
| [fornavn](klasser/fornavn.md) | Fornamn til personen |
| [forretningsadresse](klasser/forretningsadresse.md) | Besøksadresse til ein organisasjonseining |
| [fravaerstimer](klasser/fravaerstimer.md) | Antal fråværstimar |
| [fravarsoversikt](klasser/fravarsoversikt.md) | Alle fråværsoversikter i containeren |
| [fravarsprosent](klasser/fravarsprosent.md) | Fråværsprosent |
| [fravartypar](klasser/fravartypar.md) | Alle fråværstypar i containeren |
| [fravartype](klasser/fravartype.md) | Type fråvær |
| [fraversregistrering](klasser/fraversregistrering.md) | Fråversregistreringar |
| [fraversregistreringer](klasser/fraversregistreringer.md) | Fråværsregistreringar knytt til elevforholdet |
| [fullfortkode](klasser/fullfortkode.md) | Kode for fullførtresultatet |
| [fullfortkoder](klasser/fullfortkoder.md) | Alle fullfortkoder i containeren |
| [fylke](klasser/fylke.md) | Fylke |
| [gaardsnummer](klasser/gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [grepreferanse](klasser/grepreferanse.md) | Referanse til GREP-registeret |
| [gruppemedlemskap](klasser/gruppemedlemskap.md) | Gruppemedlemskap |
| [gyldighetsperiode](klasser/gyldighetsperiode.md) | Periode ressursen er gyldig for |
| [halvaar](klasser/halvaar.md) | Fråværsprosent for halvåret |
| [halvaarsfagvurdering](klasser/halvaarsfagvurdering.md) | Halvårsfagvurderingar |
| [halvaarsordensvurdering](klasser/halvaarsordensvurdering.md) | Halvårsordensvurderingar |
| [id](klasser/id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](klasser/identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [juridiskNavn](klasser/juridisknavn.md) | Juridisk namn på skulen |
| [kandidatnummer](klasser/kandidatnummer.md) | Kandidatnummer |
| [karakter](klasser/karakter.md) | Karakterverdi |
| [karakteransvarlig](klasser/karakteransvarlig.md) | Skoleressurs som er ansvarleg for karakteren |
| [karakterhistorie](klasser/karakterhistorie.md) | Karakterhistorikk |
| [karakterskalaer](klasser/karakterskalaer.md) | Alle karakterskalaer i containeren |
| [karakterstatus](klasser/karakterstatus.md) | Karakterstatus |
| [karakterverdi](klasser/karakterverdi.md) | Karakterverdi |
| [karakterverdiar](klasser/karakterverdiar.md) | Alle karakterverdiar i containeren |
| [kategori](klasser/kategori.md) | Kategori for elevforholdet |
| [kjonn](klasser/kjonn.md) | Kjønn |
| [klasse](klasser/klasse.md) | Klasse |
| [klassemedlemskap](klasser/klassemedlemskap.md) | Klassemedlemskap |
| [klasser](klasser/klasser.md) | Alle klassar i containeren |
| [kode](klasser/kode.md) | Verdi som identifiserer omgrepet |
| [kommentar](klasser/kommentar.md) | Kommentar |
| [kommune](klasser/kommune.md) | Kommune |
| [kommunenummer](klasser/kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](klasser/kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktlaerergruppe](klasser/kontaktlaerergruppe.md) | Kontaktlærargruppe |
| [kontaktlaerergruppemedlemskap](klasser/kontaktlaerergruppemedlemskap.md) | Kontaktlærergruppemedlemskap |
| [kontaktlaerergrupper](klasser/kontaktlaerergrupper.md) | Alle kontaktlærargrupper i containeren |
| [kontaktperson](klasser/kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontaktperson_navn](klasser/kontaktperson_navn.md) | Namn på kontaktpersonen |
| [kontraktstype](klasser/kontraktstype.md) | Type kontrakt for lærlingen |
| [laerling](klasser/laerling.md) | Referanse til Laerling (Utdanning) |
| [laerlingar](klasser/laerlingar.md) | Alle lærlingar i containeren |
| [land](klasser/land.md) | Land der adressa befinn seg |
| [laretid](klasser/laretid.md) | Læringstidsperiode for lærlingen |
| [maalform](klasser/maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](klasser/mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](klasser/mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](klasser/morsmaal.md) | Morsmål til personen |
| [navn](klasser/navn.md) | Hovudnamn for ressursen |
| [nettsted](klasser/nettsted.md) | Adresse til eit nettstad |
| [nummerkode](klasser/nummerkode.md) | Nummerkode for aktuell valuta |
| [nus](klasser/nus.md) | NUS-kode |
| [oppdatertAv](klasser/oppdatertav.md) | Skoleressurs som oppdaterte karakteren |
| [oppmoetetidspunkt](klasser/oppmoetetidspunkt.md) | Tidspunkt for oppmøte |
| [opprinneligKarakterstatus](klasser/opprinneligkarakterstatus.md) | Opphavleg karakterstatus |
| [opprinneligKarakterverdi](klasser/opprinneligkarakterverdi.md) | Opphavleg karakterverdi |
| [orden](klasser/orden.md) | Ordenskarakter |
| [organisasjon](klasser/organisasjon.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [organisasjonsnavn](klasser/organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](klasser/organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [otEnheter](klasser/otenheter.md) | Alle OT-einingar i containeren |
| [otStatus](klasser/otstatus.md) | Alle OT-statuser i containeren |
| [otUngdom](klasser/otungdom.md) | Alle OT-ungdom i containeren |
| [otungdom](klasser/otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](klasser/parorende.md) | Pårørande kontaktperson til personen |
| [passiv](klasser/passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [periode](klasser/periode.md) | Periode |
| [person](klasser/person.md) | Referanse til Person i Administrasjon-domenet |
| [person_navn](klasser/person_navn.md) | Namn på personen |
| [personalressurs](klasser/personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [persongruppe](klasser/persongruppe.md) | Persongruppe |
| [persongruppemedlemskap](klasser/persongruppemedlemskap.md) | Persongruppemedlemskap |
| [persongrupper](klasser/persongrupper.md) | Alle persongrupper i containeren |
| [postadresse](klasser/postadresse.md) | Informasjon om postadresse til ein aktør |
| [postnummer](klasser/postnummer.md) | Postnummer |
| [poststed](klasser/poststed.md) | Poststad |
| [programomrade](klasser/programomrade.md) | Programområde |
| [programomrademedlemskap](klasser/programomrademedlemskap.md) | Programområdemedlemskap |
| [programomrader](klasser/programomrader.md) | Alle programområde i containeren |
| [prosent](klasser/prosent.md) | Fråværsprosent (heiltal) |
| [provedato](klasser/provedato.md) | Dato prøva vart avlagt |
| [provestatus](klasser/provestatus.md) | Status for prøva |
| [provestatuser](klasser/provestatuser.md) | Alle prøvestatuser i containeren |
| [registrertAv](klasser/registrertav.md) | Skoleressurs som registrerte fråværet |
| [rom](klasser/rom.md) | Rom |
| [seksjonsnummer](klasser/seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sendt](klasser/sendt.md) | Dato varselet vart sendt |
| [sensor](klasser/sensor.md) | Sensor |
| [sensornummer](klasser/sensornummer.md) | Sensornummer |
| [sip](klasser/sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skala](klasser/skala.md) | Karakterskalaen denne verdien tilhøyrer |
| [skolar](klasser/skolar.md) | Alle skular i containeren |
| [skole](klasser/skole.md) | Skulen dette gjeld |
| [skoleaar](klasser/skoleaar.md) | Skoleåret |
| [skoleaarFravar](klasser/skoleaarfravar.md) | Fråværsprosent for heile skoleåret |
| [skoleeierType](klasser/skoleeiertype.md) | Kategori for skuleeigartilknyting |
| [skoleeijartypar](klasser/skoleeijartypar.md) | Alle skuleeigarstypar i containeren |
| [skolenummer](klasser/skolenummer.md) | Nasjonal skulenummer-identifikator |
| [skoleressurs](klasser/skoleressurs.md) | Skoleressurs |
| [skoleressursar](klasser/skoleressursar.md) | Alle skoleressursar i containeren |
| [skuletime](klasser/skuletime.md) | Ein skuletime i timeplanen |
| [slutt](klasser/slutt.md) | Til tidspunkt |
| [sluttfagvurdering](klasser/sluttfagvurdering.md) | Sluttfagvurderingar |
| [sluttordensvurdering](klasser/sluttordensvurdering.md) | Sluttordensvurderingar |
| [start](klasser/start.md) | Frå tidspunkt |
| [statsborgerskap](klasser/statsborgerskap.md) | Alle statsborgarskap personen har |
| [status](klasser/status.md) | OT-status for ungdommen |
| [tekst](klasser/tekst.md) | Innhald i varselet |
| [telefonnummer](klasser/telefonnummer.md) | Telefonnummer |
| [termin](klasser/termin.md) | Termin |
| [terminar](klasser/terminar.md) | Alle terminar i containeren |
| [tidsrom](klasser/tidsrom.md) | Tidsrom |
| [tilrettelegging](klasser/tilrettelegging.md) | Tilretteleggingstype |
| [timar](klasser/timar.md) | Alle timar i containeren |
| [tosprakligFagopplaering](klasser/tosprakligfagopplaering.md) | Indikerer om eleven har tospråkleg fagopplæring |
| [trinn](klasser/trinn.md) | Årstrinnet |
| [type](klasser/type.md) | Beskriv kva slags type |
| [underveisfagvurdering](klasser/underveisfagvurdering.md) | Underveisfagvurderingar |
| [underveisordensvurdering](klasser/underveisordensvurdering.md) | Underveisordensvurderingar |
| [undervisningsforhold](klasser/undervisningsforhold.md) | Undervisningsforhold |
| [undervisningsgruppe](klasser/undervisningsgruppe.md) | Undervisningsgruppe |
| [undervisningsgruppemedlemskap](klasser/undervisningsgruppemedlemskap.md) | Undervisningsgruppemedlemskap |
| [undervisningsgrupper](klasser/undervisningsgrupper.md) | Alle undervisningsgrupper i containeren |
| [undervisningstimer](klasser/undervisningstimer.md) | Totalt antal undervisningstimar |
| [utdanningsprogram](klasser/utdanningsprogram.md) | Utdanningsprogram |
| [utsteder](klasser/utsteder.md) | Skoleressurs som sende varselet |
| [valuta_navn](klasser/valuta_navn.md) | Namn på valuta |
| [varsel](klasser/varsel.md) | Varsel |
| [varseltypar](klasser/varseltypar.md) | Alle varseltypar i containeren |
| [verdi](klasser/verdi.md) | Karakterverdiar i skalaen |
| [vigoreferanse](klasser/vigoreferanse.md) | Referanse til Vigo-systemet |
| [virksomhetsId](klasser/virksomhetsid.md) | Intern unik identifikator i økonomisystemet |
| [vitnemalsmerknad](klasser/vitnemalsmerknad.md) | Vitnemålsmerknad |
| [vurderingsdato](klasser/vurderingsdato.md) | Dato og tidspunkt for vurderinga |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](klasser/boolean.md) | A binary (true or false) value |
| [Curie](klasser/curie.md) | a compact URI |
| [Date](klasser/date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](klasser/dateordatetime.md) | Either a date or a datetime |
| [Datetime](klasser/datetime.md) | The combination of a date and time |
| [Decimal](klasser/decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](klasser/double.md) | A real number that conforms to the xsd:double specification |
| [Float](klasser/float.md) | A real number that conforms to the xsd:float specification |
| [Integer](klasser/integer.md) | An integer |
| [Jsonpath](klasser/jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](klasser/jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](klasser/ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](klasser/nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](klasser/objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](klasser/sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](klasser/string.md) | A character string |
| [Time](klasser/time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](klasser/uri.md) | a complete URI |
| [Uriorcurie](klasser/uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](klasser/anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](klasser/obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](klasser/valgfri.md) | Valfri eigensskap |


## Generated artifacts

| Artefakt | Fil |
|----------|-----|
| SHACL shapes | [fint-utdanning-shapes.ttl](fint-utdanning-shapes.ttl) |
| JSON-LD kontekst | [fint-utdanning-context.jsonld](fint-utdanning-context.jsonld) |
| JSON Schema | [fint-utdanning-schema.json](fint-utdanning-schema.json) |
| OWL ontologi | [fint-utdanning-ontology.ttl](fint-utdanning-ontology.ttl) |
| RDF/Turtle skjema | [fint-utdanning-schema.ttl](fint-utdanning-schema.ttl) |
| Python-klasser | [fint-utdanning-model.py](fint-utdanning-model.py) |
| ER-diagram (Mermaid) | [fint-utdanning-erdiagram.md](fint-utdanning-erdiagram.md) |
| Eksempeldata (Turtle) | [fint-utdanning-eksempel.ttl](fint-utdanning-eksempel.ttl) |
