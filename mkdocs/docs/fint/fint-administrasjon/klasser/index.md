# FINT Administrasjon

FINT-domenemodell for administrasjon og HR. Dekkjer personalressursar, arbeidsforhold, fullmakter og organisasjonsstruktur.


URI: https://data.norge.no/linkml/fint-administrasjon

Name: fint-administrasjon



## Classes

| Class | Description |
| --- | --- |
| [AdministrasjonContainer](administrasjoncontainer.md) | Rotcontainer for FINT Administrasjon-instansar |
| [Adresse](adresse.md) | Fysisk adresse eller postadresse |
| [Aktoer](aktoer.md) | Abstrakt base for person eller eining vi samhandlar med |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Enhet](enhet.md) | Abstrakt base for alle hovudeiningar, undereiningar og organisasjonsledd iden... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virksomhet](virksomhet.md) | Ein juridisk organisasjon som produserer varer eller tenester |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Person](person.md) | Fysiske private personar |
| [Arbeidsforhold](arbeidsforhold.md) | Eit avtaleforhold mellom personalressurs og arbeidsgjevar |
| [Arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der ein tilsett har sitt arbeidsstad |
| [Begrep](begrep.md) | Abstrakt fellesbase for alle FINT-kodeverk |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Aktivitet](aktivitet.md) | Del av kontostrengen og detaljering av funksjon |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Anlegg](anlegg.md) | Del av kontostrengen; objekt som skal aktiverast eller avskrivast |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ansvar](ansvar.md) | Del av kontostrengen som beskriv kven som har ansvaret for ei utgift eller in... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Arbeidsforholdstype](arbeidsforholdstype.md) | Viser kva behov hos arbeidsgjevar arbeidsforholdet dekkjer |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Art](art.md) | Del av kontostrengen som beskriv kva slags inntekter og utgifter det gjeld |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Diverse](diverse.md) | Del av kontostrengen; supplement til øvrige dimensjonar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Formaal](formaal.md) | Del av kontostrengen som detaljerer inntekter og utgifter ved drift |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fravaersgrunn](fravaersgrunn.md) | Grunn til fråvær |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fravaerstype](fravaerstype.md) | Type fråvær |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Funksjon](funksjon.md) | Del av kontostrengen som beskriv kva som vert produsert |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fylke](fylke.md) | Liste over Norges fylker |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kjonn](kjonn.md) | Verdiar for kjønn basert på ISO/IEC 5218 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kommune](kommune.md) | Liste over Norges kommunar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Kontrakt](kontrakt.md) | Kontrakt transaksjonen er knytt til |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Landkode](landkode.md) | Landskode i ISO 3166-1 alpha-2 format |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lonsart](lonsart.md) | Type ytelse |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Objekt](objekt.md) | Eit bygg, ein veg eller ein mottakar av ei teneste eller eit tilskott |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organisasjonstype](organisasjonstype.md) | Typen til eit organisasjonselement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Personalressurskategori](personalressurskategori.md) | Ansettelsesform til eit arbeidsforhold |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prosjekt](prosjekt.md) | Del av kontostrengen som peikar på løpande prosjekt |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Prosjektart](prosjektart.md) | Element i ei prosjektnedbrytningsstruktur eller arbeidsnedbrytningsstruktur |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Ramme](ramme.md) | Del av kontostrengen som viser kva budsjettramme som skal bere kostnadane |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Spraak](spraak.md) | Verdiar for språk (2 bokstavar) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Stillingskode](stillingskode.md) | Felles kodeverk for stillingar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Uketimetall](uketimetall.md) | Timer per veke i 100 % stilling |
| [Elev](elev.md) | Ein elev registrert i skulesystemet |
| [Fravaer](fravaer.md) | Fråvær frå eit arbeidsforhold |
| [Fullmakt](fullmakt.md) | Fullmakt til å gjere handlingar i høve til ei gjeven Rolle |
| [Identifikator](identifikator.md) | Unik identifikasjon til eit objekt |
| [Kontaktinformasjon](kontaktinformasjon.md) | Informasjon som kan brukast for å oppnå kontakt |
| [Kontaktperson](kontaktperson.md) | Kontaktperson (pårørande) til ein person |
| [Kontostreng](kontostreng.md) | Sammensetning av kontodimensjonar for bokføring |
| [Lonn](lonn.md) | Informasjon om lønn for eit arbeidsforhold (abstrakt base) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fastlonn](fastlonn.md) | Informasjon om fast lønnsbeordring |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fasttillegg](fasttillegg.md) | Faste tillegg til utbetaling |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Variabellonn](variabellonn.md) | Informasjon om variabel lønn |
| [Matrikkelnummer](matrikkelnummer.md) | Eintydleg identifisering av matrikkeleining innanfor kommune |
| [Organisasjonselement](organisasjonselement.md) | Eit element i organisasjonsstrukturen |
| [Periode](periode.md) | Tidsperiode med obligatorisk start og valfri slutt |
| [Personalressurs](personalressurs.md) | Arbeidstakar eller oppdragstakar i organisasjonen |
| [Personnavn](personnavn.md) | Namn på ein person |
| [Rolle](rolle.md) | Rettighet eller type fullmakt |
| [Valuta](valuta.md) | Valutakodar for offisielle valutaer |



## Slots

| Slot | Description |
| --- | --- |
| [aarslonn](aarslonn.md) | Årslønn/grunnlønn i 100 % stilling |
| [adresse](adresse.md) | Adresse til matrikkeleining |
| [adresselinje](adresselinje.md) | Adresseinformasjon |
| [aktivitet](aktivitet.md) | Detaljering av funksjon |
| [aktivitetar](aktivitetar.md) | Alle aktivitetar i containeren |
| [anlegg](anlegg.md) | Objekt som skal aktiverast eller avskrivast |
| [ansattnummer](ansattnummer.md) | Unik identifikator for den tilsette i HR-systemet |
| [ansettelsesperiode](ansettelsesperiode.md) | Perioden personalressursen er i eit tilhøve til organisasjonen |
| [ansettelsesprosent](ansettelsesprosent.md) | Prosenten personalressursen eig i høve til arbeidsavtalen |
| [ansiennitet](ansiennitet.md) | Ansiennitet for personalressurs hos arbeidsgjevar |
| [ansvar](ansvar.md) | Ansvarleg for ei utgift eller inntekt |
| [antall](antall.md) | Mengde som vert beskriven av tillegget, i hundredeler |
| [anviser](anviser.md) | Personalressurs som har anvist lønsmeldinga etter fullmakt |
| [anvist](anvist.md) | Tidspunkt då lønn vart anvist |
| [arbeidsforhold](arbeidsforhold.md) | Arbeidsforhold ressursen er knytt til |
| [arbeidsforholdsperiode](arbeidsforholdsperiode.md) | Periode for ei gjeven stilling |
| [arbeidsforholdstypar](arbeidsforholdstypar.md) | Alle arbeidsforholdstypar i containeren |
| [arbeidsforholdstype](arbeidsforholdstype.md) | Beskriven kode som kategoriserer kva funksjon stillinga er gruppert til |
| [arbeidslokasjon](arbeidslokasjon.md) | Fysisk lokasjon der den tilsette har sitt arbeidsstad |
| [arbeidslokasjoner](arbeidslokasjoner.md) | Alle arbeidslokasjoner i containeren |
| [arbeidssted](arbeidssted.md) | Tilhøyrsle til organisasjonsstrukturen |
| [art](art.md) | Type inntekt eller utgift |
| [artar](artar.md) | Alle artar i containeren |
| [attestant](attestant.md) | Personalressurs som har attestert lønsmeldinga etter fullmakt |
| [attestert](attestert.md) | Tidspunkt då lønn vart attestert |
| [belop](belop.md) | Beløp i øre |
| [beskrivelse](beskrivelse.md) | Beskriven namn eller omtale |
| [bilde](bilde.md) | HTTP(S)-lenkje til eit bilete av personen |
| [bokstavkode](bokstavkode.md) | Bokstavkode for aktuell valuta |
| [bostedsadresse](bostedsadresse.md) | Folkeregistrert adresse til personen |
| [brukernavn](brukernavn.md) | Brukarnamn til den tilsette |
| [bruksnummer](bruksnummer.md) | Fortløpande nummerering av bruk under gårdsnummer |
| [diverse](diverse.md) | Spesifikasjon som ikkje kjem fram i øvrige dimensjonar |
| [elev](elev.md) | Referanse til Elev (Utdanning) |
| [elevnummer](elevnummer.md) | Skulens interne elevnummer |
| [epostadresse](epostadresse.md) | Namngitt elektronisk adresse for mottak av e-post |
| [etternavn](etternavn.md) | Etternamn til personen |
| [fastlonn](fastlonn.md) | Fastlønn for arbeidsforholdet |
| [fasttillegg](fasttillegg.md) | Faste tillegg for arbeidsforholdet |
| [festenummer](festenummer.md) | Fortløpande nummerering av festar under gårdsnummer/bruksnummer |
| [fodselsdato](fodselsdato.md) | Dato for fødsel |
| [fodselsnummer](fodselsnummer.md) | Fødselsnummer eller ein av dei fiktive variantane |
| [forelder](forelder.md) | Foreldreelement i hierarki |
| [foreldre](foreldre.md) | Den/dei som har foreldreansvar til personen |
| [foreldreansvar](foreldreansvar.md) | Personar denne personen har foreldreansvar for |
| [formaal](formaal.md) | Formål viser aktivitet og tenesteproduksjon |
| [fornavn](fornavn.md) | Fornamn til personen |
| [forretningsadresse](forretningsadresse.md) | Besøksadresse til ein organisasjonseining |
| [fortsettelse](fortsettelse.md) | Fortsetjande fråvær |
| [fortsetter](fortsetter.md) | Fråværet dette fråværet er fortsetjing av |
| [fravaer](fravaer.md) | Fråvær knytt til ressursen |
| [fravaersgrunn](fravaersgrunn.md) | Grunn til fråværet |
| [fravaersgrunnar](fravaersgrunnar.md) | Alle fråværsgrunnar i containeren |
| [fravaerstypar](fravaerstypar.md) | Alle fråværstypar i containeren |
| [fravaerstype](fravaerstype.md) | Type fråvær |
| [fullmakt](fullmakt.md) | Fullmakt ressursen er knytt til |
| [fullmakter](fullmakter.md) | Alle fullmakter i containeren |
| [fullmektig](fullmektig.md) | Personalressurs som har fått fullmakt til ei gjeven rolle |
| [funksjon](funksjon.md) | Det som vert produsert eller tenesta som vert levert |
| [funksjonar](funksjonar.md) | Alle funksjonar i containeren |
| [fylke](fylke.md) | Fylke |
| [gaardsnummer](gaardsnummer.md) | Nummerering av gårdseiging i matrikkelen, unik innanfor kommune |
| [godkjenner](godkjenner.md) | Personalressurs som har godkjent fråværsmeldinga |
| [godkjent](godkjent.md) | Tidspunkt då fråværet vart godkjent |
| [gyldighetsperiode](gyldighetsperiode.md) | Periode ressursen er gyldig for |
| [hovedstilling](hovedstilling.md) | Angir kva arbeidsforhold som er hovudarbeidsforhold |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikatorverdi](identifikatorverdi.md) | Ein konkret kombinasjon av teikn og/eller bokstavar som utgjer ein bestemt id... |
| [jobbtittel](jobbtittel.md) | Namn som beskriv jobben eller stillinga |
| [kategori](kategori.md) | Kategori lønnsart |
| [kildesystemId](kildesystemid.md) | Kjeldesystemets unike identifikator |
| [kjonn](kjonn.md) | Kjønn |
| [kode](kode.md) | Verdi som identifiserer omgrepet |
| [kommunar](kommunar.md) | Alle kommuneverdiar i containeren |
| [kommune](kommune.md) | Kommune |
| [kommunenummer](kommunenummer.md) | Nummerering av kommunen i høve til SSB si offisielle liste |
| [kontaktinformasjon](kontaktinformasjon.md) | Den føretrekte måten å kome i kontakt med ein aktør |
| [kontaktperson](kontaktperson.md) | Personar kontaktpersonen er pårørande for |
| [kontaktperson_navn](kontaktperson_navn.md) | Namn på kontaktpersonen |
| [kontaktpersonar](kontaktpersonar.md) | Alle kontaktpersonar i containeren |
| [konterer](konterer.md) | Personalressurs som har kontert lønsmeldinga etter fullmakt |
| [kontert](kontert.md) | Tidspunkt då lønn vart kontert |
| [kontostreng](kontostreng.md) | Kontering av lønn |
| [kontrakt](kontrakt.md) | Kontrakt ressursen er knytt til |
| [kontrakter](kontrakter.md) | Alle kontrakter i containeren |
| [kortnavn](kortnavn.md) | Forkorta namn som beskriv organisasjonselementet |
| [laerling](laerling.md) | Referanse til Laerling (Utdanning) |
| [land](land.md) | Land der adressa befinn seg |
| [landkodar](landkodar.md) | Alle landkodar i containeren |
| [leder](leder.md) | Ansvarleg leiar for organisasjonselementet |
| [lederFor](lederfor.md) | Organisasjonselement personalressursen er leiar for |
| [lokasjonskode](lokasjonskode.md) | Kode som identifiserer ein arbeidslokasjon |
| [lokasjonsnavn](lokasjonsnavn.md) | Namn som beskriv ein arbeidslokasjon |
| [lonnsprosent](lonnsprosent.md) | Prosent av årslønn den tilsette skal ha utbetalt |
| [lonsart](lonsart.md) | Lønnsart |
| [lonsartar](lonsartar.md) | Alle lønnsartar i containeren |
| [lopenummer](lopenummer.md) | Løpenummer i ei nummerserie |
| [maalform](maalform.md) | Målform personen føretrekkjer |
| [mellomnavn](mellomnavn.md) | Mellomnamn |
| [mobiltelefonnummer](mobiltelefonnummer.md) | Mobiltelefonnummer |
| [morsmaal](morsmaal.md) | Morsmål til personen |
| [navn](navn.md) | Hovudnamn for ressursen |
| [nettsted](nettsted.md) | Adresse til eit nettstad |
| [nummerkode](nummerkode.md) | Nummerkode for aktuell valuta |
| [objekt](objekt.md) | Objekt ressursen er knytt til |
| [opptjent](opptjent.md) | Periode der lønn vart opptent |
| [organisasjonselement](organisasjonselement.md) | Organisasjonselement ressursen er knytt til |
| [organisasjonsId](organisasjonsid.md) | Unikt internnummer for organisasjonselementet |
| [organisasjonsKode](organisasjonskode.md) | Beskriven kode for organisasjonselementet |
| [organisasjonsnavn](organisasjonsnavn.md) | Namn på eining registrert i Einingsregisteret |
| [organisasjonsnummer](organisasjonsnummer.md) | Niisifra nummer som eintydleg identifiserer einingar i Einingsregisteret |
| [organisasjonstypar](organisasjonstypar.md) | Alle organisasjonstypar i containeren |
| [organisasjonstype](organisasjonstype.md) | Kva type organisasjonselement dette er |
| [otungdom](otungdom.md) | Referanse til OtUngdom (Utdanning) |
| [overfores](overfores.md) | Angir om fråvær av denne typen skal overførast til HR |
| [overordnet](overordnet.md) | Overordna element i hierarkiet |
| [parorende](parorende.md) | Pårørande kontaktperson til personen |
| [passiv](passiv.md) | Angir at koden er passiv og ikkje kan veljast |
| [periode](periode.md) | Periode for ressursen |
| [person](person.md) | Referanse til Person i Administrasjon-domenet |
| [person_navn](person_navn.md) | Namn på personen |
| [personalansvar](personalansvar.md) | Arbeidsforhold der personalressursen har personalansvar |
| [personalleder](personalleder.md) | Personalleiar til arbeidsforholdet |
| [personalressurs](personalressurs.md) | Personalressurs til arbeidsforholdet |
| [personalressursar](personalressursar.md) | Alle personalressursar i containeren |
| [personalressurskategori](personalressurskategori.md) | Kategori for personalressursen |
| [personalressurskategoriar](personalressurskategoriar.md) | Alle personalressurskategoriar i containeren |
| [personar](personar.md) | Alle personar i containeren |
| [postadresse](postadresse.md) | Informasjon om postadresse til ein aktør |
| [postnummer](postnummer.md) | Postnummer |
| [poststed](poststed.md) | Poststad |
| [prosent](prosent.md) | Prosent |
| [prosjekt](prosjekt.md) | Prosjekt ressursen er knytt til |
| [prosjektart](prosjektart.md) | Deloppgåve eller delprosjekt |
| [prosjektartar](prosjektartar.md) | Alle prosjektartar i containeren |
| [ramme](ramme.md) | Budsjettramme som skal bere kostnadane |
| [rammer](rammer.md) | Alle rammer i containeren |
| [rollar](rollar.md) | Alle rollar i containeren |
| [rolle](rolle.md) | Kva type fullmakt |
| [rolleNavn](rollenavn.md) | Namn på rolla; unik identifikator |
| [seksjonsnummer](seksjonsnummer.md) | Fortløpande nummerering av seksjonar under gårdsnummer/bruksnummer |
| [sip](sip.md) | SIP-protokoll for VoIP (IP-telefoni) |
| [skole](skole.md) | Referanse til Skole (Utdanning) |
| [skoleressurs](skoleressurs.md) | Referanse til Skoleressurs (Utdanning) |
| [slutt](slutt.md) | Til tidspunkt |
| [spraak](spraak.md) | Alle språkverdiar i containeren |
| [start](start.md) | Frå tidspunkt |
| [statsborgerskap](statsborgerskap.md) | Alle statsborgarskap personen har |
| [stedfortreder](stedfortreder.md) | Stedfortredar i fullmaktssamanheng |
| [stillingskode](stillingskode.md) | Firesifra stillingskode frå KS, eventuelt utvida med to siffer |
| [stillingskoder](stillingskoder.md) | Alle stillingskoder i containeren |
| [stillingsnummer](stillingsnummer.md) | Løpenummer for stillinga |
| [stillingstittel](stillingstittel.md) | Arbeidstakarens stillingstittel i gjeldande stilling |
| [telefonnummer](telefonnummer.md) | Telefonnummer |
| [tilstedeprosent](tilstedeprosent.md) | Det personalressursen faktisk jobbar |
| [timerPerUke](timerperuke.md) | Timer per veke i 100 % stilling |
| [type](type.md) | Beskriv kva slags type |
| [uketimetall](uketimetall.md) | Alle uketimetallverdiar i containeren |
| [underordnet](underordnet.md) | Underordna element i hierarkiet |
| [undervisningsforhold](undervisningsforhold.md) | Referanse til Undervisningsforhold (Utdanning) |
| [valuta](valuta.md) | Alle valutaverdiar i containeren |
| [valuta_navn](valuta_navn.md) | Namn på valuta |
| [variabellonn](variabellonn.md) | Variabel lønn for arbeidsforholdet |
| [virksomhetar](virksomhetar.md) | Alle verksemder i containeren |
| [virksomhetsId](virksomhetsid.md) | Intern unik identifikator i økonomisystemet |


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
