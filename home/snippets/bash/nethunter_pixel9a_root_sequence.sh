#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

: "${PYTHONPYCACHEPREFIX:=/tmp/c0d3x-pycache}"
mkdir -p -- "$PYTHONPYCACHEPREFIX" 2>/dev/null || true
export PYTHONPYCACHEPREFIX

# Root/flash sequence helper for scoped Pixel 9a labs.
# Defaults to preview mode; requires --apply + --confirm for execution.

usage() {
  cat <<'USAGE'
Usage:
  nethunter_pixel9a_root_sequence.sh \
    --scope-file <path> \
    --device-id <id> \
    --stock-boot <img> \
    --patched-boot <img> \
    --slot <a|b> \
    [--out-dir <path>] \
    [--apply --confirm I_UNDERSTAND_DATA_RISK]
USAGE
}

scope_file=""
device_id=""
stock_boot=""
patched_boot=""
slot=""
out_dir="."
apply="0"
confirm=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scope-file)
      scope_file="$2"
      shift 2
      ;;
    --device-id)
      device_id="$2"
      shift 2
      ;;
    --stock-boot)
      stock_boot="$2"
      shift 2
      ;;
    --patched-boot)
      patched_boot="$2"
      shift 2
      ;;
    --slot)
      slot="$2"
      shift 2
      ;;
    --out-dir)
      out_dir="$2"
      shift 2
      ;;
    --apply)
      apply="1"
      shift 1
      ;;
    --confirm)
      confirm="$2"
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
[[ -n "$device_id" ]] || { echo "ERROR: --device-id is required" >&2; exit 2; }
[[ -n "$stock_boot" ]] || { echo "ERROR: --stock-boot is required" >&2; exit 2; }
[[ -n "$patched_boot" ]] || { echo "ERROR: --patched-boot is required" >&2; exit 2; }
[[ -n "$slot" ]] || { echo "ERROR: --slot is required" >&2; exit 2; }
[[ "$slot" == "a" || "$slot" == "b" ]] || { echo "ERROR: --slot must be a or b" >&2; exit 2; }
[[ -f "$stock_boot" ]] || { echo "ERROR: stock boot image not found: $stock_boot" >&2; exit 1; }
[[ -f "$patched_boot" ]] || { echo "ERROR: patched boot image not found: $patched_boot" >&2; exit 1; }

python3 "$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/nethunter-pixel9a/scripts/nethunter_scope_guard.py" \
  --scope-file "$scope_file" \
  --operation "boot-image-patch" \
  --device-id "$device_id" >/dev/null
python3 "$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/nethunter-pixel9a/scripts/nethunter_scope_guard.py" \
  --scope-file "$scope_file" \
  --operation "flash-validation" \
  --device-id "$device_id" >/dev/null

mkdir -p "$out_dir"
manifest="${out_dir%/}/pixel9a-boot-hashes-${device_id}.txt"
{
  echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  sha256sum "$stock_boot"
  sha256sum "$patched_boot"
} >"$manifest"

if [[ "$apply" != "1" ]]; then
  cat <<PREVIEW
INFO: preview mode (no flash commands executed)

adb reboot bootloader
fastboot devices
fastboot getvar current-slot
fastboot flash boot_${slot} "$patched_boot"
fastboot reboot

# Rollback command (run if validation fails)
adb reboot bootloader
fastboot flash boot_${slot} "$stock_boot"
fastboot reboot

Hash manifest: $manifest
PREVIEW
  exit 0
fi

[[ "$confirm" == "I_UNDERSTAND_DATA_RISK" ]] || {
  echo "ERROR: --confirm I_UNDERSTAND_DATA_RISK is required with --apply" >&2
  exit 2
}

for cmd in adb fastboot sha256sum; do
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "ERROR: missing required command: $cmd" >&2
    exit 1
  }
done

adb reboot bootloader
fastboot devices
fastboot getvar current-slot
fastboot flash "boot_${slot}" "$patched_boot"
fastboot reboot

echo "OK: patch flash commands completed. Validate device, then run rollback drill if required."
echo "Hash manifest: $manifest"
