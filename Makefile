IMAGE      := docker.io/linkml/linkml:latest
PODMAN     := podman run --rm -v "$(CURDIR):/work" -w /work -e PYTHONWARNINGS=ignore $(IMAGE)
GEN_DIR    := generated
SCHEMA_DIR := src/linkml
MCP_DIR    := src/mcp-linkml-validator
MCP_IMAGE  := mcp-linkml-validator
DOCS_IMAGE := docker.io/squidfunk/mkdocs-material:9.5
DOCS_RUN   := podman run --rm -v "$(CURDIR)/mkdocs:/docs"

# ---------------------------------------------------------------------------
# Schema discovery – no manual lists needed.
# Leaf schemas follow the pattern: src/linkml/<domain>/<name>/<name>-schema.yaml
# Schemas with 'common' in the path are shared dependencies, not standalone.
# ---------------------------------------------------------------------------
SCHEMAS := $(shell find $(SCHEMA_DIR) -mindepth 3 -maxdepth 3 -name '*-schema.yaml' \
    | grep -v common | sort)

schema_domain = $(word 3,$(subst /, ,$(1)))
schema_name   = $(word 4,$(subst /, ,$(1)))
schema_outdir = $(GEN_DIR)/$(call schema_domain,$(1))/$(call schema_name,$(1))

# Domains are derived automatically from the discovered schemas
DOMAINS := $(sort $(foreach s,$(SCHEMAS),$(call schema_domain,$(s))))

# ---------------------------------------------------------------------------
# Generator macros
# ---------------------------------------------------------------------------
# $1=schemas  $2=generator  $3=output-file suffix (stdout is redirected)
define run_gen
$(foreach s,$(1),mkdir -p $(call schema_outdir,$(s)) && $(PODMAN) $(2) $(s) > $(call schema_outdir,$(s))/$(call schema_name,$(s))-$(3);)
endef

# gen-doc writes to a directory instead of stdout
define run_gen_doc
$(foreach s,$(1),$(PODMAN) gen-doc --template-directory src/templates/docgen -d $(call schema_outdir,$(s))/docs $(s);)
endef

# ---------------------------------------------------------------------------
# Top-level targets
# ---------------------------------------------------------------------------
.PHONY: all test validate gen-jsonld gen-shacl gen-python gen-jsonschema gen-owl gen-rdf convert-rdf docs clean \
        mcp-build mcp-run mcp-test mcp-smoke mcp-validate \
        docs-serve docs-build \
        $(DOMAINS)

all: test

test:
	bash tests/test_schemas.sh

validate:
	$(foreach s,$(SCHEMAS),$(PODMAN) gen-linkml $(s) > /dev/null;)

gen-jsonld:
	$(call run_gen,$(SCHEMAS),gen-jsonld-context,context.jsonld)

gen-shacl:
	$(call run_gen,$(SCHEMAS),gen-shacl,shapes.ttl)

gen-python:
	$(call run_gen,$(SCHEMAS),gen-python,model.py)

gen-jsonschema:
	$(call run_gen,$(SCHEMAS),gen-json-schema,schema.json)

gen-owl:
	$(call run_gen,$(SCHEMAS),gen-owl,ontology.ttl)

gen-rdf:
	$(call run_gen,$(SCHEMAS),gen-rdf,schema.ttl)

docs:
	$(call run_gen_doc,$(SCHEMAS))

# Convert example YAML to RDF/Turtle for all domains.
# AP-NO profiles have no tree_root and use fixture schemas; others use the schema directly.
convert-rdf:
	for domain in $$(ls examples/); do \
		for example in examples/$$domain/*-eksempel.yaml; do \
			[ -f "$$example" ] || continue; \
			name=$$(basename "$$example" .yaml); \
			profil=$$(echo "$$name" | sed 's/-eksempel$$//'); \
			mkdir -p $(GEN_DIR)/$$domain/$$profil; \
			if [ -f tests/fixtures/$$profil-fixture.yaml ]; then \
				schema=tests/fixtures/$$profil-fixture.yaml; \
			else \
				schema=$(SCHEMA_DIR)/$$domain/$$profil/$$profil-schema.yaml; \
			fi; \
			$(PODMAN) linkml-convert \
				--schema $$schema \
				--output-format ttl \
				--no-validate \
				--output $(GEN_DIR)/$$domain/$$profil/$$name.ttl \
				$$example; \
		done; \
	done

clean:
	rm -rf $(GEN_DIR)

# ---------------------------------------------------------------------------
# Per-domain targets – generated automatically for every domain in DOMAINS.
# `make <domain>` (e.g. make oreg) generates all artefacts for that domain.
# New domains appear automatically when schemas are added under src/linkml/.
#
# Escaping guide for the define block used with $(eval $(call ...)):
#   $(1)          – expanded at call time (parameter substitution)
#   $$(VAR)       – becomes $(VAR) after call; expanded at build time
#   $$$$shell_var – becomes $$shell_var after call; shell receives $shell_var
# ---------------------------------------------------------------------------
define domain_target
_schemas_$(1) := $(filter $(SCHEMA_DIR)/$(1)/%,$(SCHEMAS))

.PHONY: $(1)
$(1):
	$$(foreach s,$$(_schemas_$(1)),$$(PODMAN) gen-linkml $$(s) > /dev/null;)
	$$(call run_gen,$$(_schemas_$(1)),gen-jsonld-context,context.jsonld)
	$$(call run_gen,$$(_schemas_$(1)),gen-shacl,shapes.ttl)
	$$(call run_gen,$$(_schemas_$(1)),gen-python,model.py)
	$$(call run_gen,$$(_schemas_$(1)),gen-json-schema,schema.json)
	$$(call run_gen,$$(_schemas_$(1)),gen-owl,ontology.ttl)
	$$(call run_gen,$$(_schemas_$(1)),gen-rdf,schema.ttl)
	for example in examples/$(1)/*-eksempel.yaml; do \
		[ -f "$$$$example" ] || continue; \
		name=$$$$(basename "$$$$example" .yaml); \
		profil=$$$$(echo "$$$$name" | sed 's/-eksempel$$$$//'); \
		mkdir -p $(GEN_DIR)/$(1)/$$$$profil; \
		if [ -f tests/fixtures/$$$$profil-fixture.yaml ]; then \
			schema=tests/fixtures/$$$$profil-fixture.yaml; \
		else \
			schema=$(SCHEMA_DIR)/$(1)/$$$$profil/$$$$profil-schema.yaml; \
		fi; \
		$$(PODMAN) linkml-convert \
			--schema $$$$schema \
			--output-format ttl \
			--no-validate \
			--output $(GEN_DIR)/$(1)/$$$$profil/$$$$name.ttl \
			$$$$example; \
	done
	$$(call run_gen_doc,$$(_schemas_$(1)))
endef

$(foreach d,$(DOMAINS),$(eval $(call domain_target,$(d))))

# ---------------------------------------------------------------------------
# Dokumentasjonsportal (MkDocs Material)
# ---------------------------------------------------------------------------
docs-serve:
	$(DOCS_RUN) -it -p 8000:8000 $(DOCS_IMAGE) serve --dev-addr=0.0.0.0:8000

docs-build:
	$(DOCS_RUN) $(DOCS_IMAGE) build

# ---------------------------------------------------------------------------
# MCP-validator
# ---------------------------------------------------------------------------
MCP_RUN := podman run -i --rm \
  -v "$(CURDIR)/$(MCP_DIR)/server.py:/app/server.py:ro" \
  -v "$(CURDIR)/$(MCP_DIR)/policies:/app/policies:ro"

mcp-build:
	podman build -t $(MCP_IMAGE) $(MCP_DIR)

mcp-run:
	$(MCP_RUN) $(MCP_IMAGE)

mcp-test:
	$(PODMAN) bash -c "pip install pytest --quiet 2>/dev/null && python -m pytest tests/test_mcp_server.py -v"

mcp-smoke: mcp-build
	cat tests/test-mcp-linkml-validator.json | $(MCP_RUN) $(MCP_IMAGE)

# Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=fair]
mcp-validate:
	@test -n "$(SCHEMA)" || (echo "Bruk: make mcp-validate SCHEMA=<sti-til-skjema> [POLICY=fair]"; exit 1)
	@podman image exists $(MCP_IMAGE) 2>/dev/null || $(MAKE) --no-print-directory mcp-build
	bash $(MCP_DIR)/flatten-and-validate.bash $(SCHEMA) $(POLICY)
