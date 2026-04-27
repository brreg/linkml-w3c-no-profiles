SCHEMAS    := dcat-ap-no
SCHEMA_DIR := src/linkml
GEN_DIR    := generated
IMAGE      := docker.io/linkml/linkml:latest
PODMAN     := podman run --rm -v "$(CURDIR):/work" -w /work $(IMAGE)

.PHONY: all test validate docs gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl clean

all: test docs

test:
	bash tests/test_schemas.sh

# Valider et skjema mot LinkML-metaskjemaet
validate:
	$(foreach s,$(SCHEMAS),$(PODMAN) gen-linkml --validate $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml;)

# Generer JSON-LD kontekst
gen-jsonld:
	$(foreach s,$(SCHEMAS),mkdir -p $(GEN_DIR)/$(s) && $(PODMAN) gen-jsonld-context $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml > $(GEN_DIR)/$(s)/$(s)-context.jsonld;)

# Generer SHACL shapes
gen-shacl:
	$(foreach s,$(SCHEMAS),mkdir -p $(GEN_DIR)/$(s) && $(PODMAN) gen-shacl $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml > $(GEN_DIR)/$(s)/$(s)-shapes.ttl;)

# Generer Python dataklasser
gen-python:
	$(foreach s,$(SCHEMAS),mkdir -p $(GEN_DIR)/$(s) && $(PODMAN) gen-python $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml > $(GEN_DIR)/$(s)/$(s)-model.py;)

# Generer JSON Schema
gen-jsonschema:
	$(foreach s,$(SCHEMAS),mkdir -p $(GEN_DIR)/$(s) && $(PODMAN) gen-json-schema $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml > $(GEN_DIR)/$(s)/$(s)-schema.json;)

# Generer OWL/Turtle
gen-owl:
	$(foreach s,$(SCHEMAS),mkdir -p $(GEN_DIR)/$(s) && $(PODMAN) gen-owl $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml > $(GEN_DIR)/$(s)/$(s)-ontology.ttl;)

# Generer HTML-dokumentasjon
docs:
	$(foreach s,$(SCHEMAS),$(PODMAN) gen-doc -d docs/$(s) $(SCHEMA_DIR)/$(s)/$(s)-schema.yaml;)

clean:
	rm -rf $(GEN_DIR) docs
