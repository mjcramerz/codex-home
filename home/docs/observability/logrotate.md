# logrotate

Use this guide when you change logging, metrics, tracing, audit collection or retention. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to reliable log rotation and retention.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Rotate by size and/or time; keep retention aligned with policy.
- Compress old logs; keep the most recent uncompressed.
- Use `copytruncate` only when an app cannot reopen logs.
- Enforce ownership/permissions to prevent log tampering.

## Safety notes

- Ensure rotated files are not world‑readable if they contain secrets.
- Add `su` in logrotate configs for services running as non‑root.
- Validate configs with `logrotate -d` (dry run).

## Operational tips

- Use `dateext` for easier log correlation.
- Keep rotations staggered to avoid I/O spikes.

See also:
- `overview.md`
- `$CODEX_HOME/templates/observability/logrotate-skeleton/`
- `$CODEX_HOME/snippets/logrotate/app.logrotate`
- `../workflows/logrotate.md`
- Read the `ops-logrotate` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/logrotate.md`
