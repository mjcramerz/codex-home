# Mobile-wireless kit (overview)

Use this template when you need mobile-wireless kit (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Starter assets for scoped wireless/mobile defense operations.

## Outputs

- `device-scope.example.json`: device/operation scope schema
- `pixel9a-porting-checklist.md`: controlled kernel-porting checklist
- `usb-lab-policy.md`: BadUSB/Rubber Ducky defensive policy baseline

## Usage

1. Copy this directory into an internal security repository.
2. Create an environment-specific scope file from `device-scope.example.json`.
3. Validate scope with `mobile-wireless-defense/scripts/mobile_scope_guard.py`.
4. Run lab validation tracks and capture evidence artifacts.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/security/security-labs-tool-guides.md`
- `$CODEX_HOME/docs/security/security-labs-index.md`
- `$CODEX_HOME/snippets/bash/nethunter_build.sh`
