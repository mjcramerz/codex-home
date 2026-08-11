# Debian preseed (deep dive)
Purpose: explain the split-file preseed layout and the operational boundaries behind the higher-level Debian preseed workflow for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
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

## You must enforce these guardrails
- Never commit plaintext secrets.
- You must keep destructive disk targets explicit and reviewable.
- You must keep `late_command` minimal and prefer deterministic target-side scripts.
- Test the exact BIOS/UEFI + storage path you intend to ship.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/debian-preseed.md`
- `$CODEX_HOME/templates/virtualization/debian-preseed/`
- `$CODEX_HOME/snippets/preseed/include.preseed.cfg`
