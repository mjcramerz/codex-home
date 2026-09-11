# systemd hardening options

Use this guide when you change systemd units, timers, drop-ins or service integration. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply these incrementally; test after each change.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/systemd/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Safe defaults (often applicable)

- `NoNewPrivileges=true`
- `PrivateTmp=true`
- `ProtectSystem=strict` (or `full` if strict breaks)
- `ProtectHome=true` (or `read-only`)
- `ProtectControlGroups=true`
- `ProtectKernelModules=true`
- `ProtectKernelTunables=true`
- `LockPersonality=true`
- `RestrictSUIDSGID=true`
- `UMask=0077` (adjust to app needs)

## Network & syscall restrictions (advanced)

- `RestrictAddressFamilies=` (e.g., `AF_INET AF_INET6 AF_UNIX`)
- `SystemCallFilter=` (allowlist or blocklist)
- `CapabilityBoundingSet=` (drop all unless required)

## Filesystem restrictions

- `ReadWritePaths=` and `ReadOnlyPaths=` to narrow access
- `InaccessiblePaths=` to block sensitive directories

## References

- `overview.md`
- `service-units.md`
- `../workflows/systemd.md`
- `$CODEX_HOME/index/domains/system/systemd.md`
