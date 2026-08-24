---
title: Scoped lab boundary (NetHunter Pixel 9a)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- references
- authorized-lab-boundary-md
- authorized-lab-boundary
- user
- security-labs
updated: '2026-02-20'
---
# Scoped lab boundary (NetHunter Pixel 9a)

Use this reference before any rooting or flashing operation.

## Mandatory controls
- Require a documented `scope_id` for the rooting or flashing run.
- Operate only on organization-owned and allowed lab devices.
- Keep full backup + rollback images before unlock/flash actions.
- Treat rooting as data-destructive until proven otherwise.
- Keep evidence: operator, timestamp, build IDs, hash values, and outcome.

## Required scope schema (minimum)
```json
{
  "scope_id": "MOB-2026-0099",
  "owner": "mobile-security@example.com",
  "lab_only": true,
  "allowed_devices": ["pixel9a-lab-01"],
  "allowed_operations": [
    "rooting-preflight",
    "bootloader-unlock-verification",
    "kernel-source-alignment",
    "nethunter-kernel-build",
    "nethunter-installer-build",
    "boot-image-patch",
    "flash-validation",
    "rollback-validation"
  ],
  "expires_utc": "2026-12-31T23:59:59Z"
}
```

## Stop conditions
- Device is not in the allowed list.
- Scope expired or required scope details are missing.
- No rollback path or no known-good boot image.
- Request asks for access outside scope, bypass, or covert persistence.
