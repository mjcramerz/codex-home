#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

: "${PYTHONPYCACHEPREFIX:=/tmp/c0d3x-pycache}"
mkdir -p -- "$PYTHONPYCACHEPREFIX" 2>/dev/null || true
export PYTHONPYCACHEPREFIX

# Guardrails for documented security assessments.
# Usage:
#   source ./security_assessment_guardrails.sh
#   require_scope_file ./scope.json
#   # Add repo-specific scope-mode checks here if your environment needs them.

require_scope_file() {
  local scope_file="${1:-}"
  if [[ -z "$scope_file" || ! -f "$scope_file" ]]; then
    printf '%s\n' "ERROR: missing scope file: $scope_file" >&2
    return 1
  fi
  python3 -m json.tool "$scope_file" >/dev/null
}

validate_scope_operation() {
  local scope_file="$1"
  local target="$2"
  local operation="$3"
  python3 "$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/offsec-defense/scripts/scope_guard.py" \
    --scope-file "$scope_file" \
    --target "$target" \
    --operation "$operation"
}

run_port_scan() {
  local scope_file="$1"
  local target="$2"
  validate_scope_operation "$scope_file" "$target" "port-scan" >/dev/null
  nmap -Pn -sV --top-ports 200 --host-timeout 90s "$target"
}

check_pihole_unbound_health() {
  local dns_host="${1:-127.0.0.1}"
  dig +time=2 +tries=1 @"$dns_host" cloudflare.com A
  dig +time=2 +tries=1 @"$dns_host" dnssec-failed.org A
}

prepare_metasploit_lab_context() {
  local scope_file="$1"
  local target="$2"
  validate_scope_operation "$scope_file" "$target" "metasploit-lab-validation" >/dev/null
  printf '%s\n' "INFO: scope validated for metasploit lab target: $target"
}

prepare_wifi_assessment_context() {
  local scope_file="$1"
  local target="$2"
  validate_scope_operation "$scope_file" "$target" "wifi-security-assessment" >/dev/null
  iw dev
}

prepare_reverse_engineering_context() {
  local sample_path="$1"
  if [[ ! -f "$sample_path" ]]; then
    printf '%s\n' "ERROR: sample not found: $sample_path" >&2
    return 1
  fi
  sha256sum "$sample_path"
  file "$sample_path"
}
