# sysctl tuning
Purpose: tell the Codex coding agent how to use `docs/system/sysctl.md` as a runtime-pack surface and when to stop browsing.
Guidance for safe kernel parameter tuning.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/system/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must use drop‑in files under `/etc/sysctl.d/` instead of editing `/etc/sysctl.conf`.
- You must keep changes minimal and documented; measure impact.
- Avoid “one‑size‑fits‑all” performance tweaks.

## Safe workflow
1) Draft a config file in `/etc/sysctl.d/`.
2) Apply with `sysctl --system`.
3) Validate current values with `sysctl -a | grep`.
4) Roll back by removing the drop‑in and re‑applying.

## Security vs performance
- You must prefer security‑first defaults unless a measured perf regression exists.
- For servers, ensure network hardening flags align with role (router vs host).

See also:
- `overview.md`
- `../workflows/sysctl.md`
- `$CODEX_HOME/templates/system/sysctl-baseline/`
- `$CODEX_HOME/snippets/system/sysctl.conf`
- You must use skill infra-sysctl.
- `$CODEX_HOME/index/domains/system/hardening.md`
- `$CODEX_HOME/index/domains/system/sysctl.md`
