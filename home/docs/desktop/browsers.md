# Browsers overview

Use this guide when the task concerns browsers. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to hardened desktop browser setup.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Prefer vendor‑signed builds and verify signatures.
- Pin versions in automation and record provenance.
- Keep browser user-data directories on user‑writable paths with strict permissions.
- Avoid installing browser extensions without review.

## Wayland defaults

- Prefer native Wayland flags where supported.
- Use GPU acceleration only after verifying stability.

## Quick map

- LibreWolf: `librewolf.md`
- Mullvad Browser: `mullvad-browser.md`
- Thorium: `thorium.md`

See also:
- `../workflows/browsers.md`
- `../workflows/desktop-entries.md`
- `$CODEX_HOME/index/domains/desktop/stack.md`
- `$CODEX_HOME/index/domains/desktop/browsers.md`
