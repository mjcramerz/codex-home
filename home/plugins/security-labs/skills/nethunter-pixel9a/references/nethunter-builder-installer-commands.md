---
title: NetHunter builder and installer command baselines
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- references
- nethunter-builder-installer-commands-md
- nethunter-builder-installer-commands
- user
- security-labs
updated: '2026-02-20'
---
# NetHunter builder and installer command baselines

## Upstream repositories
- Kernel builder:
  - https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder
- Installer builder:
  - https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer

## Clone and prepare
```bash
export NH_KERNEL_BUILDER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder.git"
export NH_INSTALLER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer.git"

git clone "$NH_KERNEL_BUILDER_REPO_URL"
git clone "$NH_INSTALLER_REPO_URL"

cd kali-nethunter-kernel-builder
cp config local.config
# Keep only required, documented overrides in local.config

cd ../kali-nethunter-installer
./bootstrap.sh
./build.py -h
```

## Build and evidence checklist
- Builder commit ID (`git -C <builder> rev-parse HEAD`)
- Installer commit ID (`git -C <installer> rev-parse HEAD`)
- `local.config` hash (`sha256sum`)
- Output artifact hashes (`sha256sum <artifact>`)
- UTC command transcript and non-zero exit checks
