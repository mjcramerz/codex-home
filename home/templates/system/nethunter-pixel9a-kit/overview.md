# NetHunter Pixel 9a kit (overview)
Purpose: tell the Codex coding agent how to use `templates/system/nethunter-pixel9a-kit/overview.md` as a runtime-pack surface and when to stop browsing.
Starter assets for scoped NetHunter kernel-porting and Android root lab operations.

## Outputs
- `scope.example.json`: required scope manifest for Pixel 9a execution
- `local.config.pixel9a.example`: minimal local overrides for NetHunter kernel builder
- `kernel-porting-tracker.md`: phase-by-phase tracking template
- `rooting-checklist.md`: controlled root/flash/rollback checklist

## Usage
1) Copy this directory into an internal security repository.
2) Create an environment-specific scope file from `scope.example.json`.
3) Validate scope with `nethunter-pixel9a/scripts/nethunter_scope_guard.py`.
4) Execute preflight, build, root, validation, and rollback phases.

## Inputs
- Destination repository path for this template.
- Pixel 9a build baseline and Google kernel source mapping.
- Environment-specific values for owner IDs, device IDs, and retention policy.

## Source baseline
- NetHunter build guidance: `https://www.kali.org/docs/nethunter/building-nethunter/`
- NetHunter kernel-builder porting: `https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/`
- Android bootloader model: `https://source.android.com/docs/core/architecture/bootloader/locking_unlocking`
- Android platform-tools notes: `https://developer.android.com/tools/releases/platform-tools`

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders with environment values and operation windows.
3) Pin repo URLs, capture commit IDs, and run narrow preflight checks before any flash operation.

Related:
- `$CODEX_HOME/docs/security/nethunter-pixel9a.md`
- `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md`
- `$CODEX_HOME/snippets/bash/nethunter_pixel9a_preflight.sh`
- `$CODEX_HOME/snippets/bash/nethunter_pixel9a_root_sequence.sh`
