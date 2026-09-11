# Debian preseed (deep dive)

Use this guide when you change Debian packaging, APT configuration, installation or host integration. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when

- you already chose the Debian preseed route and need the split-file structure
- you are reviewing what belongs in top-level vs included seed files
- you are validating late-command scope before changing the installer repo

## Current split-file pattern

- `preseed.cfg`
- `preseed/account.preseed.cfg`
- `preseed/network.preseed.cfg`
- `preseed/apt.preseed.cfg`
- `preseed/partman.preseed.cfg`
- `preseed/packages.preseed.cfg`
- `preseed/finish.preseed.cfg`

## Enforce these guardrails

- Never commit plaintext secrets.
- Keep destructive disk targets explicit and reviewable.
- Keep `late_command` minimal and prefer deterministic target-side scripts.
- Test the exact BIOS/UEFI + storage path you intend to ship.

## After that, check related files

- `$CODEX_HOME/docs/workflows/debian-preseed.md`
- `$CODEX_HOME/templates/virtualization/debian-preseed/`
- `$CODEX_HOME/snippets/preseed/include.preseed.cfg`
