# logrotate
Purpose: tell the Codex coding agent how to use `docs/observability/logrotate.md` as a runtime-pack surface and when to stop browsing.
Guidance for reliable log rotation and retention.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- Rotate by size and/or time; keep retention aligned with policy.
- Compress old logs; keep the most recent uncompressed.
- You must use `copytruncate` only when an app cannot reopen logs.
- Enforce ownership/permissions to prevent log tampering.

## Safety notes
- Ensure rotated files are not world‑readable if they contain secrets.
- You must add `su` in logrotate configs for services running as non‑root.
- You must validate configs with `logrotate -d` (dry run).

## Operational tips
- You must use `dateext` for easier log correlation.
- You must keep rotations staggered to avoid I/O spikes.

See also:
- `overview.md`
- `$CODEX_HOME/templates/observability/logrotate-skeleton/`
- `$CODEX_HOME/snippets/logrotate/app.logrotate`
- `../workflows/logrotate.md`
- You must use skill ops-logrotate.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/logrotate.md`
