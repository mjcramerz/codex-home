# Prompts library plan

Use this plan when you following `$CODEX_HOME/docs/workflows/prompts-library.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/prompts-library.md`.

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

- [ ] Review `$CODEX_HOME/docs/workflows/prompts-library.md` and confirm target commands/contracts.
- [ ] Update `$CODEX_HOME/docs/create-prompts.md` if prompt-file structure, names, or catalog entries change.
- [ ] Update linked maintenance assets (docs, index, template, snippet, skill references) when required.

## Testing and validation

- Run a stale-reference sweep for direct prompt-file paths outside `$CODEX_HOME/docs/create-prompts.md`.
- Validate Markdown structure for the changed guidance files.
- Run the narrowest repo checks required by the touched files.

## Security checkpoints

- Confirm trust boundaries and disallow prompt text that bypasses required controls.
- Validate input bounds and expected verification steps before shipping prompt edits.
- Record approved exceptions with owner and expiry.

## Testing checkpoints

- Validate updated prompt listings and command names in `$CODEX_HOME/docs/create-prompts.md`.
- Confirm routing and plan links resolve after any file rename or move.
- Re-run impacted checks after every contract or command change.

## Deployment checkpoints

- Keep prompt assets and prompt guidance aligned before broader pack checks.
- Document user-impacting command changes and rollback instructions.
- Confirm post-sync spot checks of affected commands.

## Multi-agent handoff

- Coordinator shares prompt scope, stop conditions, and required checks.
- When executing, report touched files, command outputs, blockers, and next action.
- Receiving agent confirms workflow scope completeness before continuing.

## Risks and edge cases

- Command contract drift between prompt files and maintenance docs.
- Broken links from renamed commands or moved maintenance assets.
- Runtime/source mismatch when sync happens before validation.

## Examples

- Example objective: "Add a new slash command with explicit `$ARGUMENTS` contract and verification steps."

## Open questions

- None.
