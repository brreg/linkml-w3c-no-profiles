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

# Optional: andre argument (t.d. ekstra flags)
EXTRA_ARGS="${2:-}"

echo "🔍 Linter LinkML-schema"
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
  linkml lint \
  "$SCHEMA" \
  --validate \
  $EXTRA_ARGS
