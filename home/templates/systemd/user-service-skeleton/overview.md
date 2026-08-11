# systemd user service skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/systemd/user-service-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Template for a user-level `systemd` service.

## Outputs
- `example.service`: user service unit template
- `example.env`: example environment file (optional)

## Quickstart
1) Copy files into `~/.config/systemd/user/`.
2) Rename `example.service` to `<app>.service` and edit:
   - `ExecStart`
3) Put runtime configuration in `example.env` (rename to `<app>.env`).
4) Reload and enable:
   - `systemctl --user daemon-reload`
   - `systemctl --user enable --now <app>.service`
5) Verify:
   - `journalctl --user -u <app>.service`

For auto-start at boot without login, enable lingering:
`loginctl enable-linger <user>`

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/systemd/user-units.md`
- `$CODEX_HOME/docs/systemd/overview.md`
