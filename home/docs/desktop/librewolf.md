# LibreWolf

Use this guide when the task concerns librewolf. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to LibreWolf installation and hardened defaults.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Use vendor‑signed packages or verified builds.
- Keep browser user data in a dedicated path with `0700` permissions.
- Apply overrides via `librewolf.overrides.cfg` or policies.

## Wayland notes

- Use Wayland flags when supported (`--ozone-platform=wayland`).
- Keep GPU/WebGL flags explicit; disable if unstable.

See also:
- `browsers.md`
- `$CODEX_HOME/snippets/desktop/librewolf.overrides.cfg`
- `../workflows/browsers.md`
- Read the `desktop-librewolf` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/desktop/librewolf.md`
