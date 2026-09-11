# systemd timers

Use this guide when you change systemd units, timers, drop-ins or service integration. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Timers schedule service units (like cron, but first-class systemd).

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/systemd/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Minimal timer

```
[Unit]
Description=Run my job daily

[Timer]
OnCalendar=daily
Persistent=true
Unit=myjob.service

[Install]
WantedBy=timers.target
```

## Common options

- `OnCalendar=`: calendar schedules (`daily`, `Mon..Fri 02:00`, etc.).
- `OnBootSec=` / `OnUnitActiveSec=`: intervals from boot or last run.
- `Persistent=true`: run missed jobs on next boot.

## Validation & install

- `systemctl daemon-reload`
- `systemctl enable --now myjob.timer`
- `systemctl list-timers --all`
For user timers, use `systemctl --user` and `WantedBy=default.target`.

## References

- `overview.md`
- `service-units.md`
- `hardening.md`
- `../workflows/systemd.md`
- `user-units.md`
- `$CODEX_HOME/index/domains/system/systemd.md`
