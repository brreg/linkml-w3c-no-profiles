#!/usr/bin/env python3
"""MCP-server for LinkML-skjemavalidering med konfigurerbar policy."""

import json
import sys
import tempfile
import yaml
from pathlib import Path


# ---------------------------------------------------------------------------
# Hjelpefunksjonar
# ---------------------------------------------------------------------------

def issue(severity: str, code: str, target: str, message: str) -> dict:
    return {"severity": severity, "code": code, "target": target, "message": message}


_POLICY_DIR = Path(__file__).parent / "policies"


def load_policy(name: str = "default") -> dict:
    try:
        with open(_POLICY_DIR / f"{name}.yaml", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}


def send(obj: dict) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# FAIR-sjekkar
# ---------------------------------------------------------------------------

# Kjende URI-ar for lisensinformasjon (CURIE og full URI)
_LICENSE_URIS = {
    "dct:license",
    "http://purl.org/dc/terms/license",
}

# Kjende URI-ar for proveniensinformasjon (CURIE og full URI)
_PROVENANCE_URIS = {
    "prov:wasAttributedTo", "http://www.w3.org/ns/prov#wasAttributedTo",
    "prov:wasGeneratedBy",  "http://www.w3.org/ns/prov#wasGeneratedBy",
    "dct:creator",          "http://purl.org/dc/terms/creator",
    "dct:publisher",        "http://purl.org/dc/terms/publisher",
    "dct:contributor",      "http://purl.org/dc/terms/contributor",
}

_STANDARD_PREFIXES = {"dct", "dcat", "skos", "prov", "rdf", "rdfs", "owl", "foaf", "xsd"}


def _all_slot_uris(schema) -> set:
    """Samlar alle slot_uri-verdiar frå globale slots og class-attributtar."""
    uris = set()
    for slot in (schema.slots or {}).values():
        if slot.slot_uri:
            uris.add(str(slot.slot_uri))
    for cls in (schema.classes or {}).values():
        for attr in (cls.attributes or {}).values():
            uri = getattr(attr, "slot_uri", None)
            if uri:
                uris.add(str(uri))
    return uris


def _fair_f1_persistent_id(sv, schema, issues):
    """F1: Schema-id skal vere ein HTTP(S)-URI (persistent identifikator)."""
    sid = str(schema.id or "")
    if not (sid.startswith("http://") or sid.startswith("https://")):
        issues.append(issue(
            "error", "fair_f1", "schema",
            "FAIR F1: schema.id er ikkje ein HTTP(S)-URI — persistent identifikator manglar",
        ))


def _fair_f2_title(sv, schema, issues):
    """F2: Schema skal ha title (rike metadata)."""
    if not schema.title:
        issues.append(issue(
            "warning", "fair_f2", "schema",
            "FAIR F2: schema.title manglar — rike metadata krev ein tittel",
        ))


def _fair_f3_class_uris(sv, schema, issues):
    """F3/I1: Alle klasser bør ha class_uri for formal ressursbeskrivelse.
    tree_root-klasser er friteke (dei er strukturelle hjelpeklasser)."""
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            continue
        if not cls.class_uri:
            issues.append(issue(
                "warning", "fair_f3", f"class:{cname}",
                f"FAIR F3/I1: Klasse '{cname}' manglar class_uri (formal ressursbeskrivelse)",
            ))


def _fair_f4_version(sv, schema, issues):
    """F4: Schema bør ha version for katalogregistrering og sporbarheit."""
    if not schema.version:
        issues.append(issue(
            "warning", "fair_f4", "schema",
            "FAIR F4: schema.version manglar — versjonering støttar katalogregistrering",
        ))


def _fair_i1_slot_uris(sv, schema, issues):
    """I1: Alle globale slots bør ha slot_uri (formal semantikk via RDF)."""
    for sname, slot in (schema.slots or {}).items():
        if not slot.slot_uri:
            issues.append(issue(
                "warning", "fair_i1", f"slot:{sname}",
                f"FAIR I1: Slot '{sname}' manglar slot_uri — formell RDF-semantikk er ikkje definert",
            ))


def _fair_i2_standard_prefixes(sv, schema, issues):
    """I2: Schema bør deklarere standard vokabularprefiks (dct, dcat, skos, prov …)."""
    declared = set(schema.prefixes.keys()) if schema.prefixes else set()
    if not (declared & _STANDARD_PREFIXES):
        issues.append(issue(
            "warning", "fair_i2", "schema",
            "FAIR I2: Ingen standard vokabularprefiks deklarert (dct, dcat, skos, prov m.fl.)",
        ))


def _fair_r11_license(sv, schema, issues):
    """R1.1: Schema bør ha ein slot med dct:license (lisensinformasjon)."""
    if not (_all_slot_uris(schema) & _LICENSE_URIS):
        issues.append(issue(
            "warning", "fair_r11", "schema",
            "FAIR R1.1: Ingen slot med dct:license funnen — lisensinformasjon manglar",
        ))


def _fair_r12_provenance(sv, schema, issues):
    """R1.2: Schema bør ha proveniens-slot (prov:wasAttributedTo, dct:creator m.fl.)."""
    if not (_all_slot_uris(schema) & _PROVENANCE_URIS):
        issues.append(issue(
            "warning", "fair_r12", "schema",
            "FAIR R1.2: Ingen proveniens-slot funnen (prov:wasAttributedTo, dct:creator m.fl.)",
        ))


_FAIR_CHECKS = {
    "f1_persistent_id":   _fair_f1_persistent_id,
    "f2_title":           _fair_f2_title,
    "f3_class_uris":      _fair_f3_class_uris,
    "f4_version":         _fair_f4_version,
    "i1_slot_uris":       _fair_i1_slot_uris,
    "i2_standard_prefixes": _fair_i2_standard_prefixes,
    "r11_license":        _fair_r11_license,
    "r12_provenance":     _fair_r12_provenance,
}


def _check_class_slots(sv, schema, policy: dict, issues: list) -> None:
    """Sjekkar at spesifiserte klasser har slots med kravde slot_uri-ar."""
    must_include = policy.get("class_slots", {}).get("must_include", [])
    if not must_include:
        return

    own_class_names = set(schema.classes.keys()) if schema.classes else set()

    for entry in must_include:
        cname = entry.get("class")
        required_uri = entry.get("slot_uri")
        label = entry.get("label", required_uri)

        if cname not in own_class_names:
            continue

        slot_uris = set()
        visited: set = set()
        queue = [cname]
        while queue:
            name = queue.pop()
            if name in visited:
                continue
            visited.add(name)
            cls = sv.get_class(name)
            if cls is None:
                continue
            for sname in (cls.slots or []):
                slot = sv.get_slot(sname)
                if slot and slot.slot_uri:
                    slot_uris.add(str(slot.slot_uri))
            for attr in (cls.attributes or {}).values():
                if attr.slot_uri:
                    slot_uris.add(str(attr.slot_uri))
            if cls.is_a:
                queue.append(cls.is_a)
            for mixin in (cls.mixins or []):
                queue.append(mixin)

        if required_uri not in slot_uris:
            issues.append(issue(
                "error", "class_missing_required_slot", f"class:{cname}",
                f"Klasse '{cname}' manglar obligatorisk slot '{label}' ({required_uri})",
            ))


def _check_container_classes(schema, policy: dict, issues: list) -> None:
    """Sjekkar at tree_root-klassen har attributtar med range for spesifiserte klasser.

    Policy-nøklar:
      container_classes.must_include   – manglar → error
      container_classes.should_include – manglar → warning
    """
    must_include   = policy.get("container_classes", {}).get("must_include", [])
    should_include = policy.get("container_classes", {}).get("should_include", [])
    if not must_include and not should_include:
        return

    # Finn tree_root-klassen i dette skjemaet (ikkje importerte klasser)
    container_cls  = None
    container_name = None
    for cname, cls in (schema.classes or {}).items():
        if cls.tree_root:
            container_cls  = cls
            container_name = cname
            break

    if container_cls is None:
        issues.append(issue(
            "error", "no_container_class", "schema",
            "Ingen tree_root-klasse funnen — kan ikkje sjekke container-klasse-krav",
        ))
        return

    # Samle range-verdiar frå attributtane til container-klassen
    container_ranges = {
        str(attr.range)
        for attr in (container_cls.attributes or {}).values()
        if attr.range
    }

    for cls_name in must_include:
        if cls_name not in container_ranges:
            issues.append(issue(
                "error", "container_missing_required_class",
                f"class:{container_name}",
                f"Container '{container_name}' manglar obligatorisk attributt med range '{cls_name}'",
            ))

    for cls_name in should_include:
        if cls_name not in container_ranges:
            issues.append(issue(
                "warning", "container_missing_recommended_class",
                f"class:{container_name}",
                f"Container '{container_name}' manglar anbefalt attributt med range '{cls_name}'",
            ))


def _run_fair_checks(sv, schema, policy: dict, issues: list) -> None:
    for check_name in policy.get("fair_checks", []):
        fn = _FAIR_CHECKS.get(check_name)
        if fn:
            fn(sv, schema, issues)


# ---------------------------------------------------------------------------
# Validering
# ---------------------------------------------------------------------------

def validate_schema(schema_text: str, policy_name: str = "default") -> dict:
    policy = load_policy(policy_name)
    issues = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        schema_path = str(Path(tmp_dir) / "schema.yaml")
        Path(schema_path).write_text(schema_text, encoding="utf-8")

        # 1) Parse — gir parse-feil som error
        try:
            from linkml_runtime.utils.schemaview import SchemaView
            sv = SchemaView(schema_path)
        except Exception as exc:
            return {
                "valid": False,
                "errorCount": 1,
                "warningCount": 0,
                "issues": [issue("error", "parse_error", "schema", str(exc))],
            }

        # 2) LinkML linter — sender filstien (str), ikkje SchemaView
        try:
            from linkml.linter.linter import Linter
            linter = Linter()
            for problem in linter.lint(schema_path):
                level = getattr(problem.level, "value", str(problem.level)).lower()
                rule = getattr(problem, "rule_name", None) or "linkml_lint"
                target = str(getattr(problem, "source", None) or "schema")
                issues.append(issue(level, rule, target, str(problem.message)))
        except Exception as exc:
            issues.append(issue("error", "linter_error", "schema", str(exc)))

        schema = sv.schema

        # 3) Policy-felt-sjekkar
        def _check(obj, obj_label: str, required_fields: list, recommended_fields: list):
            for field in required_fields:
                if not getattr(obj, field, None):
                    issues.append(issue(
                        "error", "missing_required_metadata", obj_label,
                        f"Manglar obligatorisk metadata: {field}",
                    ))
            for field in recommended_fields:
                if not getattr(obj, field, None):
                    issues.append(issue(
                        "warning", "missing_recommended_metadata", obj_label,
                        f"Manglar anbefalt metadata: {field}",
                    ))

        _check(
            schema,
            f"schema:{schema.name or 'ukjent'}",
            policy.get("required", {}).get("schema", []),
            policy.get("recommended", {}).get("schema", []),
        )
        for cname, cls in (schema.classes or {}).items():
            _check(
                cls, f"class:{cname}",
                policy.get("required", {}).get("class", []),
                policy.get("recommended", {}).get("class", []),
            )
        for sname, slot in (schema.slots or {}).items():
            _check(
                slot, f"slot:{sname}",
                policy.get("required", {}).get("slot", []),
                policy.get("recommended", {}).get("slot", []),
            )

        # Påkravde fellesklasser
        must_use = policy.get("common_classes", {}).get("must_use", [])
        all_class_names = set(sv.all_classes().keys())
        for cc in must_use:
            if cc not in all_class_names:
                issues.append(issue(
                    "error", "missing_common_class", f"class:{cc}",
                    f"Påkravd fellesklasse manglar: {cc}",
                ))

        # Container-klasse-sjekkar
        _check_container_classes(schema, policy, issues)

        # AP-NO obligatoriske slot-sjekkar
        _check_class_slots(sv, schema, policy, issues)

        # 4) FAIR-strukturelle sjekkar (berre for policyer som definerer fair_checks)
        _run_fair_checks(sv, schema, policy, issues)

    errors = [i for i in issues if i["severity"] == "error"]
    warnings = [i for i in issues if i["severity"] == "warning"]
    return {
        "valid": len(errors) == 0,
        "errorCount": len(errors),
        "warningCount": len(warnings),
        "issues": issues,
    }


# ---------------------------------------------------------------------------
# MCP-protokoll
# ---------------------------------------------------------------------------

TOOL_DEF = {
    "name": "validate_linkml_schema",
    "description": (
        "Validerer eit LinkML-skjema med standard LinkML-linting og "
        "konfigurerbare policy-reglar. Støttar fleire policyer: "
        "'default' (basis) og 'fair' (FAIR-prinsippa F1–R1.3)."
    ),
    "inputSchema": {
        "type": "object",
        "required": ["schemaText"],
        "properties": {
            "schemaText": {
                "type": "string",
                "description": "LinkML-skjema i YAML-format.",
            },
            "policy": {
                "type": "string",
                "description": "Policy-namn (default: 'default'). Tilgjengelege: 'default', 'fair'.",
                "default": "default",
            },
        },
    },
}


def handle(msg: dict) -> dict | None:
    method = msg.get("method", "")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "mcp-linkml-validator", "version": "1.0.0"},
            },
        }

    if method == "initialized":
        return None  # notifikasjon — ingen respons

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": [TOOL_DEF]},
        }

    if method == "tools/call":
        tool_name = msg.get("params", {}).get("name")
        arguments = msg.get("params", {}).get("arguments", {})

        if tool_name == "validate_linkml_schema":
            policy_name = arguments.get("policy", "default")
            result = validate_schema(arguments.get("schemaText", ""), policy_name)
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}
                    ]
                },
            }

        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32602, "message": f"Ukjent verktøy: {tool_name}"},
        }

    return {
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Metode ikkje funnen: {method}"},
    }


def main():
    for raw in sys.stdin:
        raw = raw.strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError as exc:
            send({"jsonrpc": "2.0", "id": None,
                  "error": {"code": -32700, "message": f"Parse-feil: {exc}"}})
            continue

        response = handle(msg)
        if response is not None:
            send(response)


if __name__ == "__main__":
    main()
