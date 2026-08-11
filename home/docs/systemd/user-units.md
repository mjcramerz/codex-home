# systemd user services
Purpose: tell the Codex coding agent how to use `docs/systemd/user-units.md` as a runtime-pack surface and when to stop browsing.
User services run under a specific user account and are managed with `systemctl --user`.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/systemd/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## When to use
- Per-user background services (dev tools, personal daemons).
- Services that should not require root privileges.

## Key differences vs system services
- Unit files live in `~/.config/systemd/user/` (per-user) or `/etc/systemd/user/` (system-wide user units).
- Manage with `systemctl --user`.
- For services that should start at boot **without login**, enable lingering:
  - `loginctl enable-linger <user>`

## Minimal user service
```
[Unit]
Description=My User Service

[Service]
Type=simple
ExecStart=%h/bin/my-user-service --serve
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=default.target
```

## Install/enable
- `mkdir -p ~/.config/systemd/user`
- `cp my-user.service ~/.config/systemd/user/`
- `systemctl --user daemon-reload`
- `systemctl --user enable --now my-user.service`

## References
- `overview.md`
- `service-units.md`
- `hardening.md`
- `../workflows/systemd.md`
- `$CODEX_HOME/snippets/systemd/user-service.unit`
- `$CODEX_HOME/templates/systemd/user-service-skeleton/`
- `$CODEX_HOME/index/domains/system/systemd.md`
