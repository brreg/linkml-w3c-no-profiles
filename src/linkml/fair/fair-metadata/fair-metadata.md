# FAIR-etterleving i LinkML-basert metadataarkitektur (Norsk AP + FAIR-overbygning)

## 📌 Oversikt

Denne modellen kombinerer:

- 🇳🇴 Norske applikasjonsprofilar:
  - DCAT-AP-NO
  - ModellDCAT-AP-NO
  - DQV-AP-NO
  - SKOS-AP-NO / XKOS-AP-NO
  - CPSV-AP-NO

- 🧠 FAIR-overbygning:
  - `FAIRMetadata`
  - `Tilgangsmetadata`
  - `Gjenbruksmetadata`
  - `Proveniensmetadata`
  - `Katalogregistrering`

- ⚙️ LinkML som maskinlesbart modellgrunnlag

Målet er å sikre **full FAIR-konformitet (Findable, Accessible, Interoperable, Reusable)** med eksplisitt maskin-aksjonerbar metadata.

---

## 🧠 Arkitekturelt prinsipp

> Norske applikasjonsprofilar definerer *domenedata*  
> FAIR-overbygningen definerer *maskinell brukbarheit*

Dette gir ein to-lags modell:

1. **Domenelag (DCAT / Modell / DQV)**
2. **FAIR-lag (maskinell semantikk + kravlukking)**

---

## 🧩 FAIR-etterleving per prinsipp

### 🔍 Findable (F)

- **F1** → Persistente URIar (PID)
- **F2** → DCAT-AP-NO rike metadata
- **F3** → `beskrivRessurs` i FAIRMetadata
- **F4** → `Katalogregistrering`

---

### 🔓 Accessible (A)

- **A1** → HTTP(S) + resolvable URI
- **A1.2** → `Tilgangsmetadata` (autentisering/autorisasjon)
- **A2** → `metadataPersistens` sikrar at metadata lever vidare

---

### 🔗 Interoperable (I)

- **I1** → RDF + LinkML + ModellDCAT-AP-NO
- **I2** → SKOS/XKOS kontrollerte vokabular
- **I3** → `standardoverensstemming` (conformsTo)

---

### ♻️ Reusable (R)

- **R1.1** → `lisens` (Gjenbruksmetadata)
- **R1.2** → `Proveniensmetadata`
- **R1.3** → ModellDCAT-AP-NO + standardtilknyting
- **DQV** → datakvalitet som støtte for gjenbruk

---

## 🧩 Samla arkitektur

```mermaid
flowchart TB

R["Ressurs<br/>Datasett / Modell / Teneste"]

DCAT["DCAT-AP-NO"]
MODEL["ModellDCAT-AP-NO"]
DQV["DQV-AP-NO"]
SKOS["SKOS / XKOS"]

FAIR["FAIRMetadata"]

TILGANG["Tilgangsmetadata"]
GJENBRUK["Gjenbruksmetadata"]
PROV["Proveniensmetadata"]
KATALOG["Katalogregistrering"]

PID["Persistente URIar"]
HTTP["HTTP-HTTPS"]
CAT["data.norge.no katalog"]

PID -->|F1| R
FAIR -->|F3 beskrivRessurs| R
DCAT -->|F2| FAIR
FAIR -->|F4| CAT

PID -->|A1| HTTP
TILGANG -->|A1.2| HTTP
FAIR -->|A2 metadataPersistens| CAT

MODEL -->|I1| FAIR
DCAT -->|I1| FAIR
SKOS -->|I2| FAIR
FAIR -->|I3| MODEL

GJENBRUK -->|R1.1 lisens| R
PROV -->|R1.2 proveniens| R
DQV -->|R1 kvalitet| FAIR
MODEL -->|R1.3 standard| FAIR

FAIR --> TILGANG
FAIR --> GJENBRUK
FAIR --> PROV
FAIR --> KATALOG