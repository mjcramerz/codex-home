# systemd service units
Purpose: tell the Codex coding agent how to use `docs/systemd/service-units.md` as a runtime-pack surface and when to stop browsing.
Service units define long-running processes or one-shot jobs.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/systemd/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Minimal skeleton
```
[Unit]
Description=My Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=appuser
Group=appgroup
WorkingDirectory=/opt/myapp
EnvironmentFile=/etc/myapp/myapp.env
ExecStart=/opt/myapp/bin/myapp --serve
Restart=on-failure
RestartSec=5s
TimeoutStopSec=30s

[Install]
WantedBy=multi-user.target
```

## Common fields
- `Type=`: `simple` (default), `oneshot`, `notify`, `exec`.
- `User=` / `Group=`: run as non-root when possible.
- `WorkingDirectory=`: keep relative paths predictable.
- `EnvironmentFile=`: keep secrets out of unit files.
- `ExecStart=`: avoid `sh -c`; use direct args.
- `Restart=` / `RestartSec=`: explicit recovery strategy.

## User services
- Place unit files in `~/.config/systemd/user/`.
- Manage with `systemctl --user`.
- You must use `WantedBy=default.target` for user services.
- For boot-time user services, enable lingering (`loginctl enable-linger <user>`).

## Validation & install
- `systemd-analyze verify <unit>`
- `systemctl daemon-reload`
- `systemctl enable --now <unit>`
- `journalctl -u <unit>`

## References
- `overview.md`
- `hardening.md`
- `timers.md`
- `../workflows/systemd.md`
- `user-units.md`
- `$CODEX_HOME/index/domains/system/systemd.md`
