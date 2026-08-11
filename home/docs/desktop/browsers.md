# Browsers overview
Purpose: tell the Codex coding agent how to use `docs/desktop/browsers.md` as a runtime-pack surface and when to stop browsing.
Guidance for hardened desktop browser setup.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must prefer vendor‑signed builds and verify signatures.
- Pin versions in automation and record provenance.
- You must keep browser user-data directories on user‑writable paths with strict permissions.
- Avoid installing browser extensions without review.

## Wayland defaults
- You must prefer native Wayland flags where supported.
- You must use GPU acceleration only after verifying stability.

## Quick map
- LibreWolf: `librewolf.md`
- Mullvad Browser: `mullvad-browser.md`
- Thorium: `thorium.md`

See also:
- `../workflows/browsers.md`
- `../workflows/desktop-entries.md`
- `$CODEX_HOME/index/domains/desktop/stack.md`
- `$CODEX_HOME/index/domains/desktop/browsers.md`
