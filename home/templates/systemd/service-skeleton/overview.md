# systemd service skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/systemd/service-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Template for a hardened `systemd` service (and optional timer).

## Outputs
- `example.service`: service unit template
- `example.timer`: optional timer template
- `example.env`: example environment file

## Quickstart
1) Copy files into your repo or `/etc/systemd/system/`.
2) Rename `example.service` to `<app>.service` and edit:
   - `User`, `Group`, `WorkingDirectory`, `ExecStart`
   - hardening options as needed
3) Put runtime configuration in `example.env` (rename to `<app>.env`).
4) Install:
   - `sudo cp <app>.service /etc/systemd/system/`
   - `sudo systemctl daemon-reload`
   - `sudo systemctl enable --now <app>.service`
5) Verify:
   - `journalctl -u <app>.service`

For scheduled jobs, also install `<app>.timer` and enable it.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/systemd/overview.md`
- `$CODEX_HOME/docs/systemd/service-units.md`
- `$CODEX_HOME/docs/systemd/hardening.md`
