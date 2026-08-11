#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# Time-bounded packet capture helper for security incident triage.

usage() {
  cat <<'USAGE'
Usage:
  incident_wireshark_capture.sh --iface <name> --seconds <duration> --out <pcapng>
USAGE
}

iface=""
seconds=""
out=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --iface)
      iface="$2"
      shift 2
      ;;
    --seconds)
      seconds="$2"
      shift 2
      ;;
    --out)
      out="$2"
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

[[ -n "$iface" ]] || { echo "ERROR: --iface is required" >&2; exit 2; }
[[ -n "$seconds" ]] || { echo "ERROR: --seconds is required" >&2; exit 2; }
[[ "$seconds" =~ ^[0-9]+$ ]] || { echo "ERROR: --seconds must be numeric" >&2; exit 2; }
[[ "$seconds" -gt 0 && "$seconds" -le 3600 ]] || { echo "ERROR: --seconds must be 1..3600" >&2; exit 2; }
[[ -n "$out" ]] || { echo "ERROR: --out is required" >&2; exit 2; }

timeout "$seconds" tshark -i "$iface" -w "$out"
