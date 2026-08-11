# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-prompts-library.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/prompts-library.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/prompts-library.md`
- `$CODEX_HOME/plans/prompts-library.md`

## Scope
- In: maintaining prompt guidance files and prompt-maintenance support assets.
- Out: unrelated pack changes outside prompt maintenance.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Review `$CODEX_HOME/docs/workflows/prompts-library.md` and confirm target commands/contracts.
[ ] Update `$CODEX_HOME/docs/create-prompts.md` if prompt-file structure, names, or catalog entries change.
[ ] Update linked maintenance assets (docs, index, template, snippet, skill references) when required.

## Testing and validation
- You must run a stale-reference sweep for direct prompt-file paths outside `$CODEX_HOME/docs/create-prompts.md`.
- You must validate Markdown structure for the changed guidance files.
- You must run the narrowest repo checks required by the touched files.

## Security checkpoints
- You must confirm trust boundaries and disallow prompt text that bypasses required controls.
- You must validate input bounds and expected verification steps before shipping prompt edits.
- You must record approved exceptions with owner and expiry.

## Testing checkpoints
- You must validate updated prompt listings and command names in `$CODEX_HOME/docs/create-prompts.md`.
- You must confirm routing and plan links resolve after any file rename or move.
- You must re-run impacted checks after every contract or command change.

## Deployment checkpoints
- You must keep prompt assets and prompt guidance aligned before broader pack checks.
- You must document user-impacting command changes and rollback instructions.
- You must confirm post-sync spot checks of affected commands.

## Multi-agent handoff
- Coordinator shares prompt scope, stop conditions, and required checks.
- Executor reports touched files, command outputs, blockers, and next action.
- Receiving agent confirms workflow scope completeness before continuing.

## Risks and edge cases
- Command contract drift between prompt files and maintenance docs.
- Broken links from renamed commands or moved maintenance assets.
- Runtime/source mismatch when sync happens before validation.

## Examples

- Example objective: "Add a new slash command with explicit `$ARGUMENTS` contract and verification steps."

## Open questions
- None.
