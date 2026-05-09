#!/usr/bin/env bash
set -euo pipefail

IMAGE="docker.io/linkml/linkml:latest"
CONTAINER_NAME="linkml-lint"

# -------------------------------
# Les argument
# -------------------------------
SCHEMA="${1:-}"

if [ -z "$SCHEMA" ]; then
  echo "Usage: $0 <schema.yaml>"
  echo "Example: $0 ./source/linkml/samt/samt-bu/samt-bu-schema.yaml"
  exit 1
fi

DATAFILE="${2:-}"

if [ -z "$DATAFILE" ]; then
  echo "Usage: $0 <schema.yaml> <datafile.yaml>"
  echo "Example: $0 ./source/linkml/samt/samt-bu/samt-bu-schema.yaml ./examples/samt/samt-bu-eksempel.yaml"
  exit 1
fi

echo "🔍 Validerer datafil mot LinkML-schema"
echo "Schema: $SCHEMA"
echo

# -------------------------------
# Kjør linkml lint/validate
# -------------------------------
podman run --rm \
  --name "$CONTAINER_NAME" \
  -v "$PWD:/work" \
  -w /work \
  -e PYTHONWARNINGS=ignore \
  "$IMAGE" \
  linkml validate \
  --schema \
  "$SCHEMA" \
  "$DATAFILE" 
 