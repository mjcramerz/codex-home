#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Safe fstab append helper. Default is DRY_RUN=1 (no writes).
# Usage:
#   DRY_RUN=0 fstab_add_uuid "<uuid>" "/mnt/data" "ext4" "defaults,noatime" 0 2

DRY_RUN="${DRY_RUN:-1}"
FSTAB_FILE="${FSTAB_FILE:-/etc/fstab}"

die() { echo "ERROR: $*" >&2; exit 1; }

require_root() {
  [[ "$(id -u)" -eq 0 ]] || die "must run as root"
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "missing command: $1"
}

backup_fstab() {
  local ts
  ts="$(date +%Y%m%d%H%M%S)"
  cp -a "$FSTAB_FILE" "${FSTAB_FILE}.bak.${ts}"
}

valid_uuid() {
  [[ "$1" =~ ^[A-Fa-f0-9-]+$ ]]
}

fstab_add_uuid() {
  local uuid="$1"
  local mountpoint="$2"
  local fstype="$3"
  local options="$4"
  local dump="${5:-0}"
  local pass="${6:-2}"

  [[ -n "$uuid" ]] || die "uuid required"
  valid_uuid "$uuid" || die "invalid UUID: $uuid"
  [[ "$mountpoint" == /* ]] || die "mountpoint must be absolute"
  [[ -n "$fstype" ]] || die "fstype required"
  [[ -n "$options" ]] || die "options required"

  if grep -qsE "^[^#]*\\s+$mountpoint\\s" "$FSTAB_FILE"; then
    die "mountpoint already present in $FSTAB_FILE: $mountpoint"
  fi
  if grep -qsE "^[^#]*UUID=$uuid\\s" "$FSTAB_FILE"; then
    die "UUID already present in $FSTAB_FILE: $uuid"
  fi

  local line="UUID=$uuid  $mountpoint  $fstype  $options  $dump  $pass"
  if [[ "$DRY_RUN" != "0" ]]; then
    echo "DRY_RUN: would append to $FSTAB_FILE:"
    echo "  $line"
    return 0
  fi

  require_root
  backup_fstab
  printf '%s\n' "$line" >>"$FSTAB_FILE"
}

get_uuid() {
  local device="$1"
  require_cmd blkid
  blkid -s UUID -o value "$device"
}
