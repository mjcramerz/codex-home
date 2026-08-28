#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

: "${PYTHONPYCACHEPREFIX:=/tmp/c0d3x-pycache}"
mkdir -p -- "$PYTHONPYCACHEPREFIX" 2>/dev/null || true
export PYTHONPYCACHEPREFIX

# Scope-validated inventory scan helper (defensive baseline).
# Requires scope validation before running nmap.

usage() {
  cat <<'USAGE'
Usage:
  scoped_nmap_inventory.sh --scope-file <path> --target <ip-or-cidr>
USAGE
}

scope_file=""
target=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope-file)
      scope_file="$2"
      shift 2
      ;;
    --target)
      target="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[[ -n "$scope_file" ]] || { echo "ERROR: --scope-file is required" >&2; exit 2; }
[[ -n "$target" ]] || { echo "ERROR: --target is required" >&2; exit 2; }

python3 "$CODEX_HOME/plugins/cache/codex-home/security-labs/1.0.0/skills/offsec-defense/scripts/scope_guard.py" \
  --scope-file "$scope_file" \
  --target "$target" \
  --operation "port-scan" >/dev/null

nmap -sn "$target"
