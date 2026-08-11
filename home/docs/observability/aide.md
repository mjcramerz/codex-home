# AIDE
Purpose: tell the Codex coding agent how to use `docs/observability/aide.md` as a runtime-pack surface and when to stop browsing.
Guidance for AIDE file‑integrity monitoring.


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
- You must run `aide --init` to generate the initial database.
- Schedule regular checks and alert on diffs.
- You must update the baseline after approved changes.

## Safety notes
- Restrict access to AIDE config and database files.
- Avoid monitoring volatile directories (`/var/log`, `/tmp`) unless scoped.

See also:
- `overview.md`
- `$CODEX_HOME/templates/observability/aide-skeleton/`
- `$CODEX_HOME/snippets/aide/aide.conf`
- `../workflows/aide.md`
- You must use skill secops-aide.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/aide.md`
