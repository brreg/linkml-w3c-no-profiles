# DCAT-AP-NO

Norsk applikasjonsprofil av DCAT-AP, modellert i LinkML med lenking framfor inlining. Basert på https://informasjonsforvaltning.github.io/dcat-ap-no/

URI: https://data.norge.no/linkml/dcat-ap-no

Name: dcat-ap-no



## Classes

| Class | Description |
| --- | --- |
| [Aktor](Aktor.md) | En aktør (person, organisasjon eller system) med ansvar for en ressurs |
| [Begrep](Begrep.md) | Et SKOS-begrep fra et kontrollert vokabular |
| [Begrepssamling](Begrepssamling.md) | En SKOS-begrepssamling (temavokabular) |
| [Container](Container.md) | Rotklasse for DCAT-AP-NO-datafiler |
| [Distribusjon](Distribusjon.md) | En spesifikk representasjon/nedlastbar form av et datasett |
| [Frekvens](Frekvens.md) | En oppdateringsfrekvens |
| [Gebyr](Gebyr.md) | Et gebyr knyttet til bruk av en datatjeneste |
| [Identifikator](Identifikator.md) | En alternativ identifikator for en ressurs |
| [KatalogisertRessurs](KatalogisertRessurs.md) | Basisklasse for ressurser som kan katalogiseres |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datasett](Datasett.md) | En samling av data utgitt eller kuratert av én aktør |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datasettserie](Datasettserie.md) | En serie av relaterte datasett publisert separat men med felles metadata |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Datatjeneste](Datatjeneste.md) | En samling operasjoner tilgjengeliggjort via et API-grensesnitt |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Katalog](Katalog.md) | En kuratert samling av metadata om datasett, datatjenester og/eller andre kat... |
| [Katalogpost](Katalogpost.md) | En katalogpost som beskriver en ressurs i katalogen |
| [Kontaktopplysning](Kontaktopplysning.md) | Kontaktinformasjon for en aktør |
| [Mediatype](Mediatype.md) | En medietype eller filformat |
| [OdrlPolicy](OdrlPolicy.md) | En ODRL-policy |
| [ProvAktivitet](ProvAktivitet.md) | En PROV-aktivitet |
| [ProvAttributering](ProvAttributering.md) | En kvalifisert PROV-attributering |
| [ProvenanceStatement](ProvenanceStatement.md) | En provenienserklæring |
| [RegulativRessurs](RegulativRessurs.md) | En regulativ ressurs (lov, forskrift e |
| [Relasjon](Relasjon.md) | En kvalifisert relasjon mellom to ressurser |
| [Rettighetserklaring](Rettighetserklaring.md) | En erklæring om rettigheter til en ressurs (ODRS) |
| [Sjekksum](Sjekksum.md) | En sjekksum for en distribusjon |
| [Spraak](Spraak.md) | En språkreferanse |
| [Standard](Standard.md) | En standard som en ressurs er i samsvar med |
| [Tidsinstant](Tidsinstant.md) | Et tidspunkt (OWL Time) |
| [Tidsrom](Tidsrom.md) | Et tidsintervall med start- og sluttdato |



## Slots

| Slot | Description |
| --- | --- |
| [aktørar](aktørar.md) |  |
| [algoritme](algoritme.md) | Hashalgoritme brukt for sjekksummen |
| [annen_ansvarlig_aktor](annen_ansvarlig_aktor.md) | Kvalifisert attributering til ansvarlig aktør |
| [annen_identifikator](annen_identifikator.md) | Alternativ identifikator fra et annet system |
| [annen_spesifikk_relasjon](annen_spesifikk_relasjon.md) | Kvalifisert relasjon til en annen ressurs |
| [anvendelsesretningslinjer](anvendelsesretningslinjer.md) | Retningslinjer for gjenbruk av data |
| [begrep](begrep.md) | Fagbegrep som datasettet handler om |
| [begynnelse](begynnelse.md) | Starttidspunkt for et tidsrom |
| [belop](belop.md) | Beløp for gebyret |
| [beskrivelse](beskrivelse.md) | Fritekstbeskrivelse av ressursen |
| [ble_generert_ved](ble_generert_ved.md) | Aktiviteten som genererte datasettet |
| [datasett](datasett.md) | Datasett som er del av katalogen |
| [datasettdistribusjon](datasettdistribusjon.md) | Tilgjengelige distribusjoner av datasettet |
| [datasettprofil](datasettprofil.md) |  |
| [datatenestar](datatenestar.md) |  |
| [datatjeneste](datatjeneste.md) | Datatjeneste som er del av katalogen |
| [dekningsomrade](dekningsomrade.md) | Geografisk dekningsområde |
| [distribusjonar](distribusjonar.md) |  |
| [dokumentasjon](dokumentasjon.md) | Lenke til dokumentasjon om ressursen |
| [eierskapshistorikk](eierskapshistorikk.md) | Opprinnelse og eierskapshistorikk for ressursen |
| [eksempeldata](eksempeldata.md) | Eksempeldata som distribusjon |
| [endepunkts_url](endepunkts_url.md) | URL til datatjenestens endepunkt |
| [endepunktsbeskrivelse](endepunktsbeskrivelse.md) | URL til beskrivelse av endepunktet (f |
| [endringsdato](endringsdato.md) | Dato for siste endring av ressursen |
| [filstorrelse](filstorrelse.md) | Filstørrelse i bytes |
| [format](format.md) | Filformat eller medietype |
| [forste](forste.md) | Første datasett i en datasettserie |
| [frekvens](frekvens.md) | Oppdateringsfrekvens for datasettet |
| [gebyr](gebyr.md) |  |
| [gjeldende_lovgivning](gjeldende_lovgivning.md) | Lovgivning som gjelder for ressursen |
| [har_del](har_del.md) | Delkatalog inkludert i denne katalogen |
| [har_epost](har_epost.md) | E-postadresse til kontaktpunktet |
| [har_gebyr](har_gebyr.md) | Gebyr knyttet til bruk av datatjenesten |
| [har_kontaktside](har_kontaktside.md) | Nettside for kontakt |
| [har_referanse](har_referanse.md) | Referanse til standarden |
| [har_rolle](har_rolle.md) | Rolle en aktør eller ressurs har i en relasjon |
| [hjemmeside](hjemmeside.md) | Katalogenes hjemmeside |
| [i_samsvar_med](i_samsvar_med.md) | Standard ressursen er i samsvar med |
| [i_serie](i_serie.md) | Datasettserie dette datasettet er en del av |
| [id](id.md) | URI-identifikator for ressursen |
| [identifikator_literal](identifikator_literal.md) | Tekstlig identifikator for ressursen |
| [identifikatorar](identifikatorar.md) |  |
| [jurisdiksjon](jurisdiksjon.md) | Jurisdiksjon for rettighetserklæringen |
| [katalogar](katalogar.md) |  |
| [katalogpost](katalogpost.md) | Katalogposter i katalogen |
| [katalogpostar](katalogpostar.md) |  |
| [kilde_datasett](kilde_datasett.md) | Datasett som dette datasettet er avledet fra |
| [kilde_post](kilde_post.md) | Kilde for katalogposten (ekstern oppføring) |
| [komprimeringsformat](komprimeringsformat.md) | Komprimeringsformat brukt i distribusjonen |
| [kontaktopplysningar](kontaktopplysningar.md) |  |
| [kontaktpunkt](kontaktpunkt.md) | Kontaktinformasjon for henvendelser om ressursen |
| [krediteringstekst](krediteringstekst.md) | Tekst som skal brukes ved kreditering |
| [krediteringsurl](krediteringsurl.md) | URL for kreditering av rettighetshaver |
| [landingsside](landingsside.md) | Nettside med informasjon om ressursen |
| [lisens](lisens.md) | Lisens for bruk av ressursen |
| [medietype](medietype.md) | Medietype i henhold til IANA-registeret |
| [navn_aktor](navn_aktor.md) | Navn på aktøren |
| [navn_vcard](navn_vcard.md) | Formatert navn (vCard) |
| [nedlastningslenke](nedlastningslenke.md) | Direkte nedlastningslenke for distribusjonsfilen |
| [nokkelord](nokkelord.md) | Nøkkelord som beskriver ressursen |
| [notasjon](notasjon.md) | Notasjon/kode for identifikatoren |
| [opphavsrettsaar](opphavsrettsaar.md) | Årstall for opphavsrett |
| [opphavsrettserklaring](opphavsrettserklaring.md) | Opphavsrettserklæring |
| [opphavsrettsinnehaver](opphavsrettsinnehaver.md) | Navn på opphavsrettsinnehaver |
| [opphavsrettsnotis](opphavsrettsnotis.md) | Opphavsrettsnotis |
| [pakkeformat](pakkeformat.md) | Pakkeformat brukt i distribusjonen |
| [policy](policy.md) | ODRL-policy som regulerer bruk av ressursen |
| [primaertema](primaertema.md) | Ressursen som katalogposten primært beskriver |
| [produsent](produsent.md) | Aktøren som primært har skapt ressursen |
| [referanse](referanse.md) | Referanse til ekstern ressurs |
| [regulativeRessursar](regulativeRessursar.md) |  |
| [relasjon_til](relasjon_til.md) | Den relaterte ressursen i en kvalifisert relasjon |
| [relasjonar](relasjonar.md) |  |
| [relatert_regulativ_ressurs](relatert_regulativ_ressurs.md) | Relatert regulativ ressurs |
| [relatert_ressurs](relatert_ressurs.md) | Generisk relasjon til en annen ressurs |
| [rettigheitserklaringar](rettigheitserklaringar.md) |  |
| [rettigheter](rettigheter.md) | Rettigheter knyttet til ressursen |
| [siste](siste.md) | Siste datasett i en datasettserie |
| [sjekksum](sjekksum.md) | Sjekksum for distribusjonsfilen |
| [sjekksumar](sjekksumar.md) |  |
| [sjekksumverdi](sjekksumverdi.md) | Sjekksumverdi som heksadesimal streng |
| [slutt](slutt.md) | Sluttidspunkt for et tidsrom |
| [sluttdato](sluttdato.md) | Sluttdato for tidsrommet |
| [sprak](sprak.md) | Språk brukt i ressursen |
| [standardar](standardar.md) |  |
| [startdato](startdato.md) | Startdato for tidsrommet |
| [status](status.md) | Status for ressursen fra et kontrollert vokabular |
| [tema](tema.md) | Tema fra et kontrollert vokabular |
| [temaer](temaer.md) | Temavokabular som brukes i katalogen |
| [tidsopplosning](tidsopplosning.md) | Minste tidsoppløsning i datasettet |
| [tidsrom](tidsrom.md) | Tidsperiode ressursen dekker |
| [tilgangs_url](tilgangs_url.md) | URL for tilgang til distribusjonen |
| [tilgangsrettigheter](tilgangsrettigheter.md) | Tilgangsrettigheter for ressursen |
| [tilgangstjeneste](tilgangstjeneste.md) | Datatjeneste som gir tilgang til distribusjonen |
| [tilgjengeliggjor_datasett](tilgjengeliggjor_datasett.md) | Datasett som datatjenesten tilgjengeliggjør |
| [tilgjengelighet](tilgjengelighet.md) | Planlagt tilgjengelighet for ressursen |
| [tittel](tittel.md) | Navn/tittel på ressursen |
| [tittel_literal](tittel_literal.md) | Navn/tittel uten språktag |
| [type_concept](type_concept.md) | Type ressurs fra et kontrollert vokabular |
| [underkatalog](underkatalog.md) | Katalog som er en del av denne katalogen |
| [utgivelsesdato](utgivelsesdato.md) | Dato ressursen ble første gang publisert |
| [utgiver](utgiver.md) | Aktøren som er ansvarlig for å tilgjengeliggjøre ressursen |
| [valuta](valuta.md) | Valuta for gebyret |
| [versjon](versjon.md) | Versjonsnummer |
| [versjonsmerknad](versjonsmerknad.md) | Merknad om endringer i denne versjonen |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Duration](Duration.md) | ISO 8601-varigheit (xsd:duration), t |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [GYear](GYear.md) | Gregorisk årstal (xsd:gYear), t |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [LangString](LangString.md) | Språktagget streng (rdf:langString) |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [NonNegativeInteger](NonNegativeInteger.md) | Ikke-negativ heltalsverdi (xsd:nonNegativeInteger) |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Anbefalt](Anbefalt.md) | Anbefalte egenskaper i DCAT-AP-NO |
| [Obligatorisk](Obligatorisk.md) | Obligatoriske egenskaper i DCAT-AP-NO |
| [Valgfri](Valgfri.md) | Valgfrie egenskaper i DCAT-AP-NO |
