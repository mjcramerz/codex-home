# LibreWolf
Purpose: tell the Codex coding agent how to use `docs/desktop/librewolf.md` as a runtime-pack surface and when to stop browsing.
Guidance for LibreWolf installation and hardened defaults.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must use vendor‑signed packages or verified builds.
- You must keep browser user data in a dedicated path with `0700` permissions.
- Apply overrides via `librewolf.overrides.cfg` or policies.

## Wayland notes
- You must use Wayland flags when supported (`--ozone-platform=wayland`).
- You must keep GPU/WebGL flags explicit; disable if unstable.

See also:
- `browsers.md`
- `$CODEX_HOME/snippets/desktop/librewolf.overrides.cfg`
- `../workflows/browsers.md`
- You must use skill desktop-librewolf.
- `$CODEX_HOME/index/domains/desktop/librewolf.md`
