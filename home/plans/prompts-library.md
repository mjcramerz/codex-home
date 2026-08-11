# Plan
Purpose: tell the Codex coding agent how to use `plans/prompts-library.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when adding, updating, or removing prompt assets in the pack source tree.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Requirements
- You must use `$CODEX_HOME/docs/create-prompts.md` as the source of truth for prompt-file structure and catalog updates.
- You must keep command coverage and argument contracts explicit in each prompt file.
- Preserve deterministic verification and routing behavior after edits.

## Scope
- In: prompt-file guidance, prompt catalog maintenance, and prompt-related routing/index content.
- Out: unrelated skill/template/doc implementation changes.

## Files and entry points
- `$CODEX_HOME/docs/prompts-maintenance.md`
- `$CODEX_HOME/docs/workflows/prompts-library.md`
- `$CODEX_HOME/plans/workflows/workflow-prompts-library.md`
- `$CODEX_HOME/docs/create-prompts.md`
- `$CODEX_HOME/templates/prompts/slash-command-maintenance/`
- `$CODEX_HOME/snippets/docs/prompt_contract.md`
- You must use skill `pack-prompts`.

## Action items
[ ] Define prompt objective, required inputs, and expected outputs before editing.
[ ] Update `$CODEX_HOME/docs/create-prompts.md` if prompt-file structure, names, or catalog entries change.
[ ] Keep prompt-maintenance workflow/plan/template/snippet references aligned when contracts change.
[ ] Validate command naming, argument placeholders, and linked entrypoints.

## Testing and validation
- You must validate Markdown structure for changed prompt files and guidance docs.
- You must run a stale-reference sweep for direct prompt-file paths outside `$CODEX_HOME/docs/create-prompts.md`.
- You must run targeted repo checks after structural changes.

## Security checkpoints
- Ensure prompts do not instruct bypassing auth, validation, or safety constraints.
- You must keep network/destructive actions explicit and bounded.
- Avoid embedding secrets or environment dumps in prompt content.

## Testing checkpoints
- You must confirm every changed prompt remains discoverable through `$CODEX_HOME/docs/create-prompts.md`.
- You must verify no stale references remain after rename/remove operations.
- You must re-run prompt checks after any follow-up edits.

## Deployment checkpoints
- You must record changed commands and migration notes for users.
- You must confirm rollback path (restore prior prompt files) before release.

## Multi-agent handoff
- Coordinator assigns ownership by prompt file set and stop condition.
- Executor reports updated prompt paths, validation output, and unresolved gaps.
- Receiver confirms prompt-file guidance remained centralized in `$CODEX_HOME/docs/create-prompts.md`.

## Risks and edge cases
- Command name drift between filename and overview listing.
- Broken entrypoint links after routing/index refactors.
- Runtime/source divergence if sync is skipped or partial.

## Open questions
- None.
