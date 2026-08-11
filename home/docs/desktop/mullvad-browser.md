# Mullvad Browser
Purpose: tell the Codex coding agent how to use `docs/desktop/mullvad-browser.md` as a runtime-pack surface and when to stop browsing.
Guidance for Mullvad Browser setup and integration.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must use official builds and verify signatures.
- You must keep browser user-data storage in a dedicated, locked‑down directory.
- Avoid unnecessary extensions or plugins.

## Wayland notes
- You must prefer Wayland‑native launch flags when supported.
- Test rendering and font settings for readability.

See also:
- `browsers.md`
- `$CODEX_HOME/snippets/desktop/desktop-entry.desktop`
- `../workflows/browsers.md`
- You must use skill desktop-mullvad-browser.
- `$CODEX_HOME/index/domains/desktop/mullvad-browser.md`
