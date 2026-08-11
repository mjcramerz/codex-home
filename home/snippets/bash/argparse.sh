# shellcheck shell=bash
# Minimal, dependency-free argument parsing pattern for long options.
# Intended to be sourced into a strict-mode script.
#
# Usage:
#   parse_args "$@"
# Then use the globals it sets.
#
# Notes:
# - Keep defaults explicit and validate required options.
# - Adapt `usage()` and globals to your script’s flags.
#
# References: docs/style/bash.md, Use skill shell-bash.
#
# shellcheck disable=SC2034  # globals are consumed by callers after parse_args

usage() {
  cat >&2 <<'EOF'
Usage:
  script.sh [OPTIONS] --name <value>

Options:
  --flag/--no-flag  Example boolean (default: false)
  --name VALUE       Required value (also supports --name=VALUE)
  -v, --verbose      Enable debug logging
  --dry-run          Print actions without mutating state
  -h, --help         Show help
EOF
}

flag=false
name=""
verbose=false
dry_run=false
# Remaining positional args (if any)
extra_args=()

parse_args() {
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --flag) flag=true; shift ;;
      --no-flag) flag=false; shift ;;
      --name=*)
        name="${1#*=}"
        [[ -n "$name" ]] || { echo "ERROR: --name requires a value" >&2; usage; exit 2; }
        shift
        ;;
      --name)
        name="${2:-}"
        [[ -n "$name" ]] || { echo "ERROR: --name requires a value" >&2; usage; exit 2; }
        shift 2
        ;;
      -v|--verbose) verbose=true; shift ;;
      --dry-run) dry_run=true; shift ;;
      -h|--help) usage; exit 0 ;;
      --) shift; break ;;
      -*) echo "ERROR: unknown flag: $1" >&2; usage; exit 2 ;;
      *) break ;;
    esac
  done

  [[ -n "$name" ]] || { echo "ERROR: --name is required" >&2; usage; exit 2; }
  extra_args=("$@")
}
