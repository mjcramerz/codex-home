#!/usr/bin/env bash
# Safe bash script skeleton with strict mode, logging, and cleanup.
# Customize `usage()`, `parse_args()`, and `main()` for your script.
#
# References: snippets/bash/strict.sh, docs/style/bash.md
set -Eeuo pipefail
IFS=$'\n\t'

shopt -s inherit_errexit 2>/dev/null || true

PROG="${0##*/}"
VERSION="0.1.0"
readonly PROG VERSION

LOG_LEVEL="${LOG_LEVEL:-INFO}"
LOG_TS="${LOG_TS:-1}"

dry_run=false
assume_yes=false
verbose=false
arg=""

__on_err() {
  local exit_code=$?
  local line_no="${1:-}"
  printf 'ERROR: %s:%s: command failed (exit=%s)\n' "${BASH_SOURCE[0]}" "${line_no}" "${exit_code}" >&2
  exit "${exit_code}"
}
trap '__on_err ${LINENO}' ERR

usage() {
  cat >&2 <<EOF
Usage:
  ${PROG} [OPTIONS] <arg>

Options:
  --dry-run         Print actions without mutating state
  -y, --yes         Assume yes for prompts (also via ASSUME_YES=1)
  -v, --verbose     Enable debug logging
  --version         Print version and exit
  -h, --help        Show help
EOF
}

__log_ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
__log_level_rank() {
  case "${1^^}" in
    TRACE) echo 0 ;;
    DEBUG) echo 1 ;;
    INFO)  echo 2 ;;
    WARN)  echo 3 ;;
    ERROR) echo 4 ;;
    *)     echo 2 ;;
  esac
}
__log_should_log() {
  local want="${1^^}"
  local have="${LOG_LEVEL^^}"
  [[ "$(__log_level_rank "$want")" -ge "$(__log_level_rank "$have")" ]]
}
__log() {
  local level="${1^^}"; shift || true
  __log_should_log "$level" || return 0
  if [[ "$LOG_TS" == "1" ]]; then
    printf '%s %s: %s\n' "$(__log_ts)" "$level" "$*" >&2
  else
    printf '%s: %s\n' "$level" "$*" >&2
  fi
}
log_debug() { __log DEBUG "$*"; }
log_info()  { __log INFO  "$*"; }
log_warn()  { __log WARN  "$*"; }
log_error() { __log ERROR "$*"; }
die() { log_error "$1"; exit "${2:-1}"; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "missing required command: $1" 127
}

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --dry-run) dry_run=true; shift ;;
      -y|--yes) assume_yes=true; shift ;;
      -v|--verbose) verbose=true; shift ;;
      --version) printf '%s %s\n' "$PROG" "$VERSION"; exit 0 ;;
      -h|--help) usage; exit 0 ;;
      --) shift; break ;;
      -*) die "unknown flag: $1" ;;
      *) break ;;
    esac
  done

  [[ $# -ge 1 ]] || { usage; exit 2; }
  arg="$1"
}

cleanup() {
  if [[ -n "${tmp_dir:-}" && -d "${tmp_dir:-}" ]]; then
    rm -rf -- "${tmp_dir:?}"
  fi
}
trap cleanup EXIT

run() {
  if "$dry_run"; then
    log_info "DRY-RUN: $*"
    return 0
  fi
  "$@"
}

main() {
  parse_args "$@"

  if "$verbose"; then
    LOG_LEVEL="DEBUG"
  fi
  if "$assume_yes"; then
    export ASSUME_YES=1
  fi

  tmp_dir="$(mktemp -d "${TMPDIR:-/tmp}/${PROG}.XXXXXX")"

  log_info "arg=$arg dry_run=$dry_run"

  # require_cmd git
  # run git status --porcelain=v1
  # do work
}

main "$@"
