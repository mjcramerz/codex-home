# shellcheck shell=bash
# Logging helpers (stderr).
#
# Environment variables:
#   LOG_LEVEL  One of: TRACE|DEBUG|INFO|WARN|ERROR (default: INFO)
#   LOG_TS     "1" to prefix UTC timestamps (default: 1)
#
# Notes:
# - Keep logs free of secrets and large payloads.
# - Prefer structured logs for automation; this stays human-readable.
#
# References: docs/style/bash.md, Use skill shell-bash.

LOG_LEVEL="${LOG_LEVEL:-INFO}"
LOG_TS="${LOG_TS:-1}"
LOG_PREFIX="${LOG_PREFIX:-}"

__log_ts() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

__log_level_rank() {
  case "${1^^}" in
    TRACE) echo 0 ;;
    DEBUG) echo 1 ;;
    INFO)  echo 2 ;;
    WARN)  echo 3 ;;
    ERROR) echo 4 ;;
    *)     echo 2 ;; # default INFO
  esac
}

__log_should_log() {
  local want_level="${1^^}"
  local have_level="${LOG_LEVEL^^}"
  [[ "$(__log_level_rank "$want_level")" -ge "$(__log_level_rank "$have_level")" ]]
}

__log() {
  local level="${1^^}"; shift || true
  __log_should_log "$level" || return 0
  local prefix=""
  if [[ -n "$LOG_PREFIX" ]]; then
    prefix="${LOG_PREFIX} "
  fi

  if [[ "$LOG_TS" == "1" ]]; then
    printf '%s %s%s: %s\n' "$(__log_ts)" "$prefix" "$level" "$*" >&2
  else
    printf '%s%s: %s\n' "$prefix" "$level" "$*" >&2
  fi
}

log_trace() { __log TRACE "$*"; }
log_debug() { __log DEBUG "$*"; }
log_info()  { __log INFO  "$*"; }
log_warn()  { __log WARN  "$*"; }
log_error() { __log ERROR "$*"; }

die() {
  local msg="${1:-}"
  local code="${2:-1}"
  log_error "$msg"
  exit "$code"
}
