# AIDE

Use this guide when you change logging, metrics, tracing, audit collection or retention. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to AIDE file‑integrity monitoring.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Build a baseline database after clean install.
- Store the AIDE database offline or on read‑only media when possible.
- Monitor critical paths (`/etc`, `/usr`, bootloader, kernel modules).

## Operations

- Run `aide --init` to generate the initial database.
- Schedule regular checks and alert on diffs.
- Update the baseline after approved changes.

## Safety notes

- Restrict access to AIDE config and database files.
- Avoid monitoring volatile directories (`/var/log`, `/tmp`) unless scoped.

See also:
- `overview.md`
- `$CODEX_HOME/templates/observability/aide-skeleton/`
- `$CODEX_HOME/snippets/aide/aide.conf`
- `../workflows/aide.md`
- Read the `secops-aide` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/aide.md`
