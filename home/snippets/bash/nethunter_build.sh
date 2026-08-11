#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

: "${PYTHONPYCACHEPREFIX:=/tmp/c0d3x-pycache}"
mkdir -p -- "$PYTHONPYCACHEPREFIX" 2>/dev/null || true
export PYTHONPYCACHEPREFIX

# Deterministic helper for NetHunter build tooling in documented labs.

KERNEL_BUILDER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder.git"
INSTALLER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer.git"

usage() {
  cat <<'USAGE'
Usage:
  nethunter_build.sh [--builder-dir <path>] [--installer-dir <path>] [--clone-missing]

Defaults:
  --builder-dir   $NH_KERNEL_BUILDER_DIR or ./kali-nethunter-kernel-builder
  --installer-dir $NH_INSTALLER_DIR or ./kali-nethunter-installer
USAGE
}

builder_dir="${NH_KERNEL_BUILDER_DIR:-$PWD/kali-nethunter-kernel-builder}"
installer_dir="${NH_INSTALLER_DIR:-$PWD/kali-nethunter-installer}"
clone_missing="0"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --builder-dir)
      builder_dir="$2"
      shift 2
      ;;
    --installer-dir)
      installer_dir="$2"
      shift 2
      ;;
    --clone-missing)
      clone_missing="1"
      shift 1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'ERROR: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

for cmd in git bash python3; do
  command -v "$cmd" >/dev/null 2>&1 || {
    printf 'ERROR: missing required command: %s\n' "$cmd" >&2
    exit 1
  }
done

clone_repo_if_needed() {
  local dst="$1"
  local url="$2"
  [[ -d "$dst" ]] && return 0
  if [[ "$clone_missing" != "1" ]]; then
    printf 'ERROR: missing directory: %s (use --clone-missing to clone from %s)\n' "$dst" "$url" >&2
    return 1
  fi
  git clone "$url" "$dst"
}

clone_repo_if_needed "$builder_dir" "$KERNEL_BUILDER_REPO_URL"
clone_repo_if_needed "$installer_dir" "$INSTALLER_REPO_URL"

[[ -f "$builder_dir/build.sh" ]] || { printf 'ERROR: build.sh not found in %s\n' "$builder_dir" >&2; exit 1; }
[[ -f "$installer_dir/build.py" ]] || { printf 'ERROR: build.py not found in %s\n' "$installer_dir" >&2; exit 1; }

printf '[info] Kernel builder dir: %s\n' "$builder_dir"
printf '[info] Installer dir: %s\n' "$installer_dir"

bash -n "$builder_dir/build.sh"
python3 "$installer_dir/build.py" -h >/dev/null

if [[ -d "$builder_dir/.git" ]]; then
  printf '[info] builder commit: %s\n' "$(git -C "$builder_dir" rev-parse HEAD)"
fi
if [[ -d "$installer_dir/.git" ]]; then
  printf '[info] installer commit: %s\n' "$(git -C "$installer_dir" rev-parse HEAD)"
fi

printf 'OK: NetHunter build tooling precheck complete\n'
