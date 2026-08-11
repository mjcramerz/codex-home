#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

: "${PYTHONPYCACHEPREFIX:=/tmp/c0d3x-pycache}"
mkdir -p -- "$PYTHONPYCACHEPREFIX" 2>/dev/null || true
export PYTHONPYCACHEPREFIX

# Preflight baseline collector for scoped NetHunter Pixel 9a lab operations.

usage() {
  cat <<'USAGE'
Usage:
  nethunter_pixel9a_preflight.sh \
    --scope-file <path> \
    --device-id <id> \
    --out-dir <path> \
    [--require-adb-device] \
    [--builder-dir <path>] \
    [--installer-dir <path>]
USAGE
}

scope_file=""
device_id=""
out_dir=""
builder_dir="${NH_KERNEL_BUILDER_DIR:-}"
installer_dir="${NH_INSTALLER_DIR:-}"
require_adb_device="0"

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
    --out-dir)
      out_dir="$2"
      shift 2
      ;;
    --require-adb-device)
      require_adb_device="1"
      shift 1
      ;;
    --builder-dir)
      builder_dir="$2"
      shift 2
      ;;
    --installer-dir)
      installer_dir="$2"
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
[[ -n "$out_dir" ]] || { echo "ERROR: --out-dir is required" >&2; exit 2; }

python3 "$CODEX_HOME/plugins/cache/codex-local/security-labs/local/skills/nethunter-pixel9a/scripts/nethunter_scope_guard.py" \
  --scope-file "$scope_file" \
  --operation "rooting-preflight" \
  --device-id "$device_id" >/dev/null

for cmd in adb fastboot git python3 sha256sum; do
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "ERROR: missing required command: $cmd" >&2
    exit 1
  }
done

ts="$(date -u +%Y%m%dT%H%M%SZ)"
report_dir="${out_dir%/}/pixel9a-preflight-${device_id}-${ts}"
mkdir -p "$report_dir"

adb version >"$report_dir/adb-version.txt"
fastboot --version >"$report_dir/fastboot-version.txt"
adb devices -l >"$report_dir/adb-devices.txt"

if timeout 20 adb wait-for-device >/dev/null 2>&1; then
  adb shell getprop ro.product.device >"$report_dir/prop-ro.product.device.txt"
  adb shell getprop ro.build.fingerprint >"$report_dir/prop-ro.build.fingerprint.txt"
  adb shell getprop ro.build.version.release >"$report_dir/prop-ro.build.version.release.txt"
  adb shell getprop ro.build.version.security_patch >"$report_dir/prop-ro.build.version.security_patch.txt"
  adb shell getprop ro.boot.slot_suffix >"$report_dir/prop-ro.boot.slot_suffix.txt"
  adb shell getprop ro.boot.flash.locked >"$report_dir/prop-ro.boot.flash.locked.txt"
  adb shell getprop ro.boot.verifiedbootstate >"$report_dir/prop-ro.boot.verifiedbootstate.txt"
  adb shell getprop ro.boot.vbmeta.device_state >"$report_dir/prop-ro.boot.vbmeta.device_state.txt"
else
  if [[ "$require_adb_device" == "1" ]]; then
    echo "ERROR: no adb device available during preflight window" >&2
    exit 1
  fi
  echo "WARN: no adb device available during preflight window" >"$report_dir/adb-warning.txt"
fi

if fastboot devices >"$report_dir/fastboot-devices.txt" 2>&1; then
  if [[ -s "$report_dir/fastboot-devices.txt" ]]; then
    fastboot getvar current-slot >"$report_dir/fastboot-current-slot.txt" 2>&1 || true
    fastboot getvar is-userspace >"$report_dir/fastboot-is-userspace.txt" 2>&1 || true
    fastboot getvar unlocked >"$report_dir/fastboot-unlocked.txt" 2>&1 || true
  else
    echo "WARN: fastboot command succeeded but no devices were listed" >"$report_dir/fastboot-warning.txt"
  fi
else
  echo "WARN: fastboot device query failed; check cable/mode state" >"$report_dir/fastboot-warning.txt"
fi

for repo in "$builder_dir" "$installer_dir"; do
  [[ -n "$repo" ]] || continue
  if [[ -d "$repo/.git" ]]; then
    name="$(basename "$repo")"
    git -C "$repo" rev-parse HEAD >"$report_dir/${name}.commit.txt"
    git -C "$repo" status --short >"$report_dir/${name}.status.txt"
  fi
done

echo "OK: preflight evidence captured: $report_dir"
