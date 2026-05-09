# FINT Utdanning

FINT-domenemodell for utdanning. Dekkjer elevar, skular, skoleressursar, elevforhold, undervisningsforhold, klasser, undervisningsgrupper, faggrupper, kontaktlærergrupper, utdanningsprogram, programområde, vurdering, lærling og OT.


URI: https://data.norge.no/linkml/fint-utdanning

Name: fint-utdanning



## Classes

| Class | Description |
| --- | --- |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](person.md) | Fysiske private personar |
| [Anmerkninger](anmerkninger.md) | Åtferds- og ordensanmerkningar for ein elev i eit skoleår |
| [Avbruddsaarsak](avbruddsaarsak.md) | Årsak til avbrot frå opplæring |
| [AvlagtProve](avlagtprove.md) | Ei avlagt prøve for ein lærling |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |
| [Betalingsstatus](betalingsstatus.md) | Betalingsstatus for eksamensavgift |
| [Bevistype](bevistype.md) | Type kompetansebevis for lærling |
| [Brevtype](brevtype.md) | Type brev knytt til lærlingprøve |
| [Eksamen](eksamen.md) | Ein eksamen knytt til ei eksamensgruppe |
| [Eksamensform](eksamensform.md) | Form for gjennomføring av eksamen |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |
| [Elevforhold](elevforhold.md) | Eit elevs tilknyting til ein skule og eit skoleår |
| [Elevfravar](elevfravar.md) | Fråværsregistreringar for ein elev knytt til eit elevforhold |
| [Elevkategori](elevkategori.md) | Kategori for eit elevforhold (t |
| [Elevtilrettelegging](elevtilrettelegging.md) | Tilrettelegging for ein elev i eit elevforhold |
| [Elevvurdering](elevvurdering.md) | Samling av alle vurderingar for ein elev i eit elevforhold |
| [Fagmerknad](fagmerknad.md) | Merknad knytt til eit fag i ei faggruppe |
| [Fagstatus](fagstatus.md) | Status for eit fag i eit faggruppemedlemskap |
| [FagvurderingAbstrakt](fagvurderingabstrakt.md) | Abstrakt basisklasse for fagvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensvurdering](eksamensvurdering.md) | Vurdering gjeven i samband med ein eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsvurdering i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttfagvurdering](sluttfagvurdering.md) | Sluttkarakter i eit fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurdering for ein elev |
| [Fravarsoversikt](fravarsoversikt.md) | Oversikt over fråvær for ein elev i eit fag |
| [Fravarsprosent](fravarsprosent.md) | Kompleks type som representerer fråværsprosent for ein periode |
| [Fravartype](fravartype.md) | Type fråvær (t |
| [Fraversregistrering](fraversregistrering.md) | Ei enkelt fråversregistrering for ein elev |
| [Fullfortkode](fullfortkode.md) | Kode for fullførtresultat av lærling |
| [Gruppe](gruppe.md) | Abstrakt basisklasse for alle gruppetypar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arstrinn](arstrinn.md) | Eit årstrinn i skulen (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppe](eksamensgruppe.md) | Ei gruppe elevar som avlegg same eksamen |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fag](fag.md) | Eit skulefag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppe](faggruppe.md) | Ei gruppe elevar knytt til eit fag på ein skule |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klasse](klasse.md) | Ei fast klasse av elevar ved ein skule (tidlegare kalla Basisgruppe) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppe](kontaktlaerergruppe.md) | Gruppe av elevar med felles kontaktlærar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppe](persongruppe.md) | Ei gruppe elevar definert for personlege føremål |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrade](programomrade.md) | Eit programområde innanfor eit utdanningsprogram (t |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppe](undervisningsgruppe.md) | Ei gruppe elevar som følgjer same undervisning i eit eller fleire fag |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Utdanningsprogram](utdanningsprogram.md) | Eit utdanningsprogram (t |
| [Gruppemedlemskap](gruppemedlemskap.md) | Abstrakt basisklasse for gruppemedlemskapar i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eit elevs deltaking i ei eksamensgruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Faggruppemedlemskap](faggruppemedlemskap.md) | Eit elevs medlemskap i ei faggruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Klassemedlemskap](klassemedlemskap.md) | Eit elevs medlemskap i ei klasse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Eit elevs medlemskap i ei kontaktlærargruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Persongruppemedlemskap](persongruppemedlemskap.md) | Eit elevs medlemskap i ei persongruppe |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Programomrademedlemskap](programomrademedlemskap.md) | Eit elevs tilknyting til eit programområde |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Eit elevs medlemskap i ei undervisningsgruppe |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [Karakterhistorie](karakterhistorie.md) | Historikk over endringar i ein karakter |
| [Karakterskala](karakterskala.md) | Skala for karaktersetjing (t |
| [Karakterstatus](karakterstatus.md) | Status for ein karakter (t |
| [Karakterverdi](karakterverdi.md) | Ein konkret karakterverdi i ei karakterskala |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Laerling](laerling.md) | Ein lærling i yrkesopplæring |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [OrdensvurderingAbstrakt](ordensvurderingabstrakt.md) | Abstrakt basisklasse for ordensvurderingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurdering for ein elev |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurdering for ein elev |
| [OtEnhet](otenhet.md) | Eining i oppfølgingstenesta (OT) |
| [OtStatus](otstatus.md) | Status for ein ungdom i oppfølgingstenesta |
| [OtUngdom](otungdom.md) | Eit ungdomsobjekt i oppfølgingstenesta (OT) |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Provestatus](provestatus.md) | Status for ei lærlingprøve |
| [Rom](rom.md) | Eit rom eller lokale ved ein skule |
| [Sensor](sensor.md) | Ein sensor for ein eksamen |
| [Skole](skole.md) | Ein skule eller opplæringsinstitusjon |
| [Skoleaar](skoleaar.md) | Eit skoleår (t |
| [Skoleeiertype](skoleeiertype.md) | Type skuleeigartilknyting |
| [Skoleressurs](skoleressurs.md) | Ein lærar eller anna tilsett ved ein skule |
| [Termin](termin.md) | Ein skuleterm (t |
| [Tilrettelegging](tilrettelegging.md) | Type tilrettelegging for elevar (t |
| [Time](time.md) | Ein time i timeplanen |
| [UtdanningContainer](utdanningcontainer.md) | Rotcontainer for FINT Utdanning-instansar |
| [Utdanningsforhold](utdanningsforhold.md) | Abstrakt basisklasse for undervisningsforhold i utdanning |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Undervisningsforhold](undervisningsforhold.md) | Eit tilhøve mellom ein skoleressurs og undervisningsaktivitetar |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |
| [Varsel](varsel.md) | Eit varsel knytt til ein elev i ei faggruppe |
| [Varseltype](varseltype.md) | Type varsel knytt til ein elev |
| [Vitnemalsmerknad](vitnemalsmerknad.md) | Merknad på vitnemål |



## Slots

| Slot | Description |
| --- | --- |
| [adresse](adresse.md) | Adresse til matrikkeleining |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [aktiv](aktiv.md) | Angir om sensoren er aktiv |
| [anmerkningar](anmerkningar.md) | Alle anmerkningar i containeren |
| [arbeidsforhold](arbeidsforhold.md) | Referanse til Arbeidsforhold i Administrasjon-domenet |
| [arstrinn](arstrinn.md) | Alle årstrinns-objekt i containeren |
| [atferd](atferd.md) | Åtferdskarakter |
| [avbruddsaarsaker](avbruddsaarsaker.md) | Alle avbruddsårsakar i containeren |
| [avbruddsarsak](avbruddsarsak.md) | Årsak til avbrot frå opplæring |
| [avbruddsdato](avbruddsdato.md) | Dato for avbrot frå opplæring |
| [avlagteprover](avlagteprover.md) | Alle avlagde prøver i containeren |
| [avlagtprove](avlagtprove.md) | Avlagde prøver |
| [bedrift](bedrift.md) | Referanse til bedrifta lærlingen er i |
| [beskrivelse](beskrivelse.md) | Skildring |
| [betalingsstatus](betalingsstatus.md) | Betalingsstatus |
| [bevistypar](bevistypar.md) | Alle bevistypar i containeren |
| [bevistype](bevistype.md) | Type kompetansebevis |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brevtypar](brevtypar.md) | Alle brevtypar i containeren |
| [brevtype](brevtype.md) | Type brev |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [delegert](delegert.md) | Angir om deltakinga er delegert |
| [delegertTil](delegerttil.md) | Referanse til den deltakinga er delegert til |
| [domenenavn](domenenavn.md) | Domenenamn for skulen |
| [eksamen](eksamen.md) | Eksamen |
| [eksamensdato](eksamensdato.md) | Dato for eksamenen |
| [eksamensform](eksamensform.md) | Eksamensform |
| [eksamensformer](eksamensformer.md) | Alle eksamensformer i containeren |
| [eksamensgruppe](eksamensgruppe.md) | Eksamensgruppe |
| [eksamensgruppemedlemskap](eksamensgruppemedlemskap.md) | Eksamensgruppemedlemskap |
| [eksamensgrupper](eksamensgrupper.md) | Alle eksamensgrupper i containeren |
| [eksamensvurdering](eksamensvurdering.md) | Eksamensvurderingar |
| [elev](elev.md) | Eleven dette gjeld |
| [elevar](elevar.md) | Alle elevar i containeren |
| [elevforhold](elevforhold.md) | Elevforholdet dette gjeld |
| [elevfravar](elevfravar.md) | Fråværsobjekt for elev |
| [elevkategoriar](elevkategoriar.md) | Alle elevkategoriar i containeren |
| [elevnummer](elevnummer.md) | Skulens interne elevnummer |
| [elevtilrettelegging](elevtilrettelegging.md) | Alle elevtilretteleggingar i containeren |
| [elevvurdering](elevvurdering.md) | Elevvurderingsobjekt |
| [endretDato](endretdato.md) | Dato og tidspunkt for endringa |
| [enhet](enhet.md) | OT-eining |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [fag](fag.md) | Fag |
| [faggruppe](faggruppe.md) | Faggruppe |
| [faggruppemedlemskap](faggruppemedlemskap.md) | Faggruppemedlemskap |
| [faggrupper](faggrupper.md) | Alle faggrupper i containeren |
| [fagmerknad](fagmerknad.md) | Merknad til faget |
| [fagmerknader](fagmerknader.md) | Alle fagmerknadar i containeren |
| [fagstatus](fagstatus.md) | Fagstatus |
| [feidenavn](feidenavn.md) | Feide-identifikator |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [forersPaaVitnemaal](forerspaavitnemaal.md) | Angir om fråværet vert ført på vitnemålet |
| [foretrukketSensor](foretrukketsensor.md) | Angir om sensor er føretrekt |
| [foretrukketSkole](foretrukketskole.md) | Angir om skulen er føretrekt for eksamenen |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Forretningsadresse |
| [fravaerstimer](fravaerstimer.md) | Antal fråværstimar |
| [fravarsoversikt](fravarsoversikt.md) | Alle fråværsoversikter i containeren |
| [fravarsprosent](fravarsprosent.md) | Fråværsprosent |
| [fravartypar](fravartypar.md) | Alle fråværstypar i containeren |
| [fravartype](fravartype.md) | Type fråvær |
| [fraversregistrering](fraversregistrering.md) | Fråversregistreringar |
| [fraversregistreringer](fraversregistreringer.md) | Fråværsregistreringar knytt til elevforholdet |
| [fullfortkode](fullfortkode.md) | Kode for fullførtresultatet |
| [fullfortkoder](fullfortkoder.md) | Alle fullfortkoder i containeren |
| [fylke](fylke.md) | Fylke |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [grepreferanse](grepreferanse.md) | Referanse til GREP-registeret |
| [gruppemedlemskap](gruppemedlemskap.md) | Gruppemedlemskap |
| [gyldighetsperiode](gyldighetsperiode.md) | Gyldigheitsperiode |
| [halvaar](halvaar.md) | Fråværsprosent for halvåret |
| [halvaarsfagvurdering](halvaarsfagvurdering.md) | Halvårsfagvurderingar |
| [halvaarsordensvurdering](halvaarsordensvurdering.md) | Halvårsordensvurderingar |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [juridiskNavn](juridisknavn.md) | Juridisk namn på skulen |
| [kandidatnummer](kandidatnummer.md) | Kandidatnummer |
| [karakter](karakter.md) | Karakterverdi |
| [karakteransvarlig](karakteransvarlig.md) | Skoleressurs som er ansvarleg for karakteren |
| [karakterhistorie](karakterhistorie.md) | Karakterhistorikk |
| [karakterskalaer](karakterskalaer.md) | Alle karakterskalaer i containeren |
| [karakterstatus](karakterstatus.md) | Karakterstatus |
| [karakterverdi](karakterverdi.md) | Karakterverdi |
| [karakterverdiar](karakterverdiar.md) | Alle karakterverdiar i containeren |
| [kategori](kategori.md) | Kategori for elevforholdet |
| [kjonn](kjonn.md) | Kjønn |
| [klasse](klasse.md) | Klasse |
| [klassemedlemskap](klassemedlemskap.md) | Klassemedlemskap |
| [klasser](klasser.md) | Alle klassar i containeren |
| [kode](kode.md) | Kode |
| [kommentar](kommentar.md) | Kommentar |
| [kommune](kommune.md) | Referanse til kommunen OT-eininga dekker |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktlaerergruppe](kontaktlaerergruppe.md) | Kontaktlærargruppe |
| [kontaktlaerergruppemedlemskap](kontaktlaerergruppemedlemskap.md) | Kontaktlærergruppemedlemskap |
| [kontaktlaerergrupper](kontaktlaerergrupper.md) | Alle kontaktlærargrupper i containeren |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontaktperson_naam](kontaktperson_naam.md) | Namn på kontaktpersonen |
| [kontraktstype](kontraktstype.md) | Type kontrakt for lærlingen |
| [laerling](laerling.md) | Lærling |
| [laerlingar](laerlingar.md) | Alle lærlingar i containeren |
| [land](land.md) | Land der adressa befinn seg |
| [laretid](laretid.md) | Læringstidsperiode for lærlingen |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [naam](naam.md) | Hovudnamn for ressursen |
| [navn](navn.md) | Namn |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [nus](nus.md) | NUS-kode |
| [oppdatertAv](oppdatertav.md) | Skoleressurs som oppdaterte karakteren |
| [oppmoetetidspunkt](oppmoetetidspunkt.md) | Tidspunkt for oppmøte |
| [opprinneligKarakterstatus](opprinneligkarakterstatus.md) | Opphavleg karakterstatus |
| [opprinneligKarakterverdi](opprinneligkarakterverdi.md) | Opphavleg karakterverdi |
| [orden](orden.md) | Ordenskarakter |
| [organisasjon](organisasjon.md) | Referanse til Organisasjonselement i Administrasjon-domenet |
| [organisasjonsnavn](organisasjonsnavn.md) | Organisasjonsnamn |
| [organisasjonsnummer](organisasjonsnummer.md) | Organisasjonsnummer-identifikator |
| [otEnheter](otenheter.md) | Alle OT-einingar i containeren |
| [otStatus](otstatus.md) | Alle OT-statuser i containeren |
| [otUngdom](otungdom.md) | Alle OT-ungdom i containeren |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) | Angir om oppføringen er passiv/inaktiv |
| [periode](periode.md) | Periode |
| [person](person.md) | Referanse til Person i Administrasjon-domenet |
| [person_naam](person_naam.md) | Namn på personen |
| [personalressurs](personalressurs.md) | Referanse til Personalressurs i Administrasjon-domenet |
| [persongruppe](persongruppe.md) | Persongruppe |
| [persongruppemedlemskap](persongruppemedlemskap.md) | Persongruppemedlemskap |
| [persongrupper](persongrupper.md) | Alle persongrupper i containeren |
| [postadresse](postadresse.md) | Postadresse |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [programomrade](programomrade.md) | Programområde |
| [programomrademedlemskap](programomrademedlemskap.md) | Programområdemedlemskap |
| [programomrader](programomrader.md) | Alle programområde i containeren |
| [prosent](prosent.md) | Fråværsprosent (heiltal) |
| [provedato](provedato.md) | Dato prøva vart avlagt |
| [provestatus](provestatus.md) | Status for prøva |
| [provestatuser](provestatuser.md) | Alle prøvestatuser i containeren |
| [registrertAv](registrertav.md) | Skoleressurs som registrerte fråværet |
| [rom](rom.md) | Rom |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sendt](sendt.md) | Dato varselet vart sendt |
| [sensor](sensor.md) | Sensor |
| [sensornummer](sensornummer.md) | Sensornummer |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skala](skala.md) | Karakterskalaen denne verdien tilhøyrer |
| [skolar](skolar.md) | Alle skular i containeren |
| [skole](skole.md) | Skulen dette gjeld |
| [skoleaar](skoleaar.md) | Skoleåret |
| [skoleaarFravar](skoleaarfravar.md) | Fråværsprosent for heile skoleåret |
| [skoleeierType](skoleeiertype.md) | Kategori for skuleeigartilknyting |
| [skoleeijartypar](skoleeijartypar.md) | Alle skuleeigarstypar i containeren |
| [skolenummer](skolenummer.md) | Nasjonal skulenummer-identifikator |
| [skoleressurs](skoleressurs.md) | Skoleressurs |
| [skoleressursar](skoleressursar.md) | Alle skoleressursar i containeren |
| [slutt](slutt.md) | Til tidspunkt |
| [sluttfagvurdering](sluttfagvurdering.md) | Sluttfagvurderingar |
| [sluttordensvurdering](sluttordensvurdering.md) | Sluttordensvurderingar |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [status](status.md) | OT-status for ungdommen |
| [tekst](tekst.md) | Innhald i varselet |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [termin](termin.md) | Termin |
| [terminar](terminar.md) | Alle terminar i containeren |
| [tidsrom](tidsrom.md) | Tidsrom |
| [tilrettelegging](tilrettelegging.md) | Tilretteleggingstype |
| [timar](timar.md) | Alle timar i containeren |
| [time](time.md) | Time |
| [tosprakligFagopplaering](tosprakligfagopplaering.md) | Indikerer om eleven har tospråkleg fagopplæring |
| [trinn](trinn.md) | Årstrinnet |
| [type](type.md) | Type |
| [underveisfagvurdering](underveisfagvurdering.md) | Underveisfagvurderingar |
| [underveisordensvurdering](underveisordensvurdering.md) | Underveisordensvurderingar |
| [undervisningsforhold](undervisningsforhold.md) | Undervisningsforhold |
| [undervisningsgruppe](undervisningsgruppe.md) | Undervisningsgruppe |
| [undervisningsgruppemedlemskap](undervisningsgruppemedlemskap.md) | Undervisningsgruppemedlemskap |
| [undervisningsgrupper](undervisningsgrupper.md) | Alle undervisningsgrupper i containeren |
| [undervisningstimer](undervisningstimer.md) | Totalt antal undervisningstimar |
| [utdanningsprogram](utdanningsprogram.md) | Utdanningsprogram |
| [utsteder](utsteder.md) | Skoleressurs som sende varselet |
| [valuta_naam](valuta_naam.md) | Namn på valuta |
| [varsel](varsel.md) | Varsel |
| [varseltypar](varseltypar.md) | Alle varseltypar i containeren |
| [verdi](verdi.md) | Karakterverdiar i skalaen |
| [vigoreferanse](vigoreferanse.md) | Referanse til Vigo-systemet |
| [virksomhetsId](virksomhetsid.md) | Intern unik identifikator i økonomisystemet |
| [vitnemalsmerknad](vitnemalsmerknad.md) | Vitnemålsmerknad |
| [vurderingsdato](vurderingsdato.md) | Dato og tidspunkt for vurderinga |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](boolean.md) | A binary (true or false) value |
| [Curie](curie.md) | a compact URI |
| [Date](date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](dateordatetime.md) | Either a date or a datetime |
| [Datetime](datetime.md) | The combination of a date and time |
| [Decimal](decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](double.md) | A real number that conforms to the xsd:double specification |
| [Float](float.md) | A real number that conforms to the xsd:float specification |
| [Integer](integer.md) | An integer |
| [Jsonpath](jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](string.md) | A character string |
| [Time](time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](uri.md) | a complete URI |
| [Uriorcurie](uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](anbefalt.md) | Anbefalt eigensskap |
| [Obligatorisk](obligatorisk.md) | Obligatorisk eigensskap |
| [Valgfri](valgfri.md) | Valfri eigensskap |
