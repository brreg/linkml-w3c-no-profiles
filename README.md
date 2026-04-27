# LINKML-W3C-NO-PROFILES

Dette repoet modellerer alle norske W3C applikasjonsprofiler på LinkML format for gjenbruk.

## Utvikling
>Prosjektet er utstyrt med agents fil CLAUDE.md for å gi instruksjoner til LLM. 


## Krav

- [Podman](https://podman.io/) — alle LinkML-kommandoar køyrer via `docker.io/linkml/linkml:latest`

## Kommandoar

| Kommando | Beskriving |
|---|---|
| `make` | Køyr testar og generer dokumentasjon |
| `make test` | Lint alle skjema og valider alle eksempelfiler |
| `make validate` | Valider skjema mot LinkML-metaskjemaet |
| `make gen-jsonld` | Generer JSON-LD kontekst (`*-context.jsonld`) |
| `make gen-shacl` | Generer SHACL shapes (`*-shapes.ttl`) |
| `make gen-python` | Generer Python-dataklassar (`*-model.py`) |
| `make gen-jsonschema` | Generer JSON Schema (`*-schema.json`) |
| `make gen-owl` | Generer OWL/Turtle-ontologi (`*-ontology.ttl`) |
| `make docs` | Generer HTML-dokumentasjon til `docs/` |
| `make clean` | Slett `generated/` og `docs/` |

Genererte artefakter hamnar i `generated/<profil>/`, t.d. `generated/dcat-ap-no/dcat-ap-no-ontology.ttl`.

### Enkeltskjema direkte

```bash
podman run --rm -v "$(pwd):/work" -w /work docker.io/linkml/linkml:latest \
  linkml validate --schema src/linkml/dcat-ap-no/dcat-ap-no-schema.yaml \
  examples/dcat-ap-no/eksempel-katalog.yaml
```