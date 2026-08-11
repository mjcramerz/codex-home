#!/usr/bin/env bash
# Strict-mode baseline for production scripts.
# References: docs/style/bash.md, Use skill shell-bash.
# -E: inherit ERR trap in functions/subshells
set -Eeuo pipefail
IFS=$'\n\t'

# Optional (bash >=4.4): propagate errexit through command substitutions.
shopt -s inherit_errexit 2>/dev/null || true

__on_err() {
  local exit_code=$?
  local line_no="${1:-}"

  # Avoid leaking secrets: do not print full command lines by default.
  printf 'ERROR: %s:%s: command failed (exit=%s)\n' "${BASH_SOURCE[0]}" "${line_no}" "${exit_code}" >&2

  if [[ "${LOG_COMMAND_ON_ERROR:-}" == "1" ]]; then
    printf '  command: %s\n' "${BASH_COMMAND}" >&2
  fi

  exit "${exit_code}"
}
trap '__on_err ${LINENO}' ERR
