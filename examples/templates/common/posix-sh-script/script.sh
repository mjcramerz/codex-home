#!/bin/sh
# shellcheck shell=sh
set -eu
# shellcheck disable=SC3040
(set -o pipefail 2>/dev/null) || true
IFS=$(printf '\n\t')

die(){ printf '%s\n' "$*" >&2; exit 1; }
need(){ command -v "$1" >/dev/null 2>&1 || die "missing dependency: $1"; }

usage(){ printf '%s\n' "usage: $0 [args]" >&2; exit 2; }

main(){
  :
}

main "$@"
