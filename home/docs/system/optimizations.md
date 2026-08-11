# Performance/security optimizations
Purpose: tell the Codex coding agent how to use `docs/system/optimizations.md` as a runtime-pack surface and when to stop browsing.
Guidance for balancing performance and security on hosts.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/system/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- Measure first; avoid blind “tuning packs”.
- Apply one change at a time and record impact.
- You must keep rollback steps for each change.

## Common areas
- **CPU governor**: performance vs powersave (document choice).
- **I/O scheduler**: test per‑device; defaults are often fine.
- **sysctl**: apply minimal deltas and verify behavior.
- **Kernel build flags**: keep to policy‑approved changes.

## Safety notes
- Security‑reducing flags require explicit approval.
- Re‑run benchmarks after each change.

See also:
- `overview.md`
- `kernel.md`
- `sysctl.md`
- `../workflows/optimizations.md`
- You must use skill infra-optimizations.
- `$CODEX_HOME/index/domains/system/optimizations.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
