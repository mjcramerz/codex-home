#!/bin/sh
# shellcheck shell=sh
set -eu
# shellcheck disable=SC3040
(set -o pipefail 2>/dev/null) || true
IFS=$(printf '\n\t')
