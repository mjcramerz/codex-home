#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Read-only filesystem probe for planning.
# Usage: ./fs_probe.sh

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || echo "WARN: missing command: $1" >&2
}

require_cmd lsblk
require_cmd blkid

echo "== lsblk =="
lsblk -o NAME,PATH,SIZE,TYPE,FSTYPE,FSVER,MOUNTPOINT,UUID,PARTUUID,MODEL

echo
echo "== blkid =="
blkid || true
