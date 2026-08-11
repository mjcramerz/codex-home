# systemd overview
Purpose: tell the Codex coding agent how to use `docs/systemd/overview.md` as a runtime-pack surface and when to stop browsing.
This pack treats systemd units as production interfaces. Prefer explicit units, clear ownership, and safe defaults.


## Contents
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/systemd/hardening.md` — systemd hardening options
- `$CODEX_HOME/docs/systemd/service-units.md` — systemd service units
- `$CODEX_HOME/docs/systemd/timers.md` — systemd timers
- `$CODEX_HOME/docs/systemd/user-units.md` — systemd user services
<!-- END:contents -->


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Concepts
- **Units**: `.service`, `.timer`, `.mount`, `.socket`, etc.
- **Drop-ins**: override files in `*.d/` for targeted changes.
- **Targets**: logical groupings (e.g., `multi-user.target`).
- **User units**: per-user services managed by `systemctl --user`.

## Safety baseline
- You must run as non-root when possible (`User=`/`Group=`).
- Set timeouts and restart policies explicitly.
- Avoid running shells; use direct `ExecStart=` arguments.
- You must use hardening options where feasible (see `hardening.md`).

## Common flow
1) Draft a unit file.
2) Validate with `systemd-analyze verify` (if available).
3) Install under `/etc/systemd/system/`.
4) `systemctl daemon-reload`
5) `systemctl enable --now <unit>`
6) Verify logs with `journalctl -u <unit>`.

## References
- `service-units.md`
- `timers.md`
- `hardening.md`
- `user-units.md`
- `../workflows/systemd.md`
- `$CODEX_HOME/templates/systemd/service-skeleton/`
- `$CODEX_HOME/snippets/systemd/service.unit`
- `$CODEX_HOME/index/domains/system/systemd.md`
