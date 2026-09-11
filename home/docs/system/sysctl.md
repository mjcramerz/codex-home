# sysctl tuning

Use this guide when the task concerns sysctl tuning. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to safe kernel parameter tuning.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/system/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Use drop‑in files under `/etc/sysctl.d/` instead of editing `/etc/sysctl.conf`.
- Keep changes minimal and documented; measure impact.
- Avoid “one‑size‑fits‑all” performance tweaks.

## Safe workflow

1. Draft a config file in `/etc/sysctl.d/`.
2. Apply with `sysctl --system`.
3. Validate current values with `sysctl -a | grep`.
4. Roll back by removing the drop‑in and re‑applying.

## Security vs performance

- Prefer security‑first defaults unless a measured perf regression exists.
- For servers, ensure network hardening flags align with role (router vs host).

See also:
- `overview.md`
- `../workflows/sysctl.md`
- `$CODEX_HOME/templates/system/sysctl-baseline/`
- `$CODEX_HOME/snippets/system/sysctl.conf`
- Read the `infra-sysctl` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/system/hardening.md`
- `$CODEX_HOME/index/domains/system/sysctl.md`
