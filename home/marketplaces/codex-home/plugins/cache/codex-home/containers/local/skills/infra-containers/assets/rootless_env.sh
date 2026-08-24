#!/usr/bin/env bash
# Populate UID/GID env vars for rootless-friendly compose usage.
set -euo pipefail

format="export"
if [[ "${1:-}" == "--dotenv" ]]; then
  format="dotenv"
fi

uid="$(id -u)"
gid="$(id -g)"

if [[ "${format}" == "dotenv" ]]; then
  cat <<EOF
APP_UID=${uid}
APP_GID=${gid}
DEV_UID=${uid}
DEV_GID=${gid}
ENGINE_UID=${uid}
ENGINE_GID=${gid}
EOF
else
  cat <<EOF
export APP_UID="${uid}"
export APP_GID="${gid}"
export DEV_UID="${uid}"
export DEV_GID="${gid}"
export ENGINE_UID="${uid}"
export ENGINE_GID="${gid}"
EOF
fi
