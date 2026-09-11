# Prompts library plan

Use this plan when you are adding, updating, or removing prompt assets in the pack source tree. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when adding, updating, or removing prompt assets in the pack source tree.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Use `$CODEX_HOME/docs/create-prompts.md` as the source of truth for prompt-file structure and catalog updates.
- Keep command coverage and argument contracts explicit in each prompt file.
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
- Read the `pack-prompts` skill only when its trigger matches this task and the skill is available.

## Action items

- [ ] Define prompt objective, required inputs, and expected outputs before editing.
- [ ] Update `$CODEX_HOME/docs/create-prompts.md` if prompt-file structure, names, or catalog entries change.
- [ ] Keep prompt-maintenance workflow/plan/template/snippet references aligned when contracts change.
- [ ] Validate command naming, argument placeholders, and linked entrypoints.

## Testing and validation

- Validate Markdown structure for changed prompt files and guidance docs.
- Run a stale-reference sweep for direct prompt-file paths outside `$CODEX_HOME/docs/create-prompts.md`.
- Run targeted repo checks after structural changes.

## Security checkpoints

- Ensure prompts do not instruct bypassing auth, validation, or safety constraints.
- Keep network/destructive actions explicit and bounded.
- Avoid embedding secrets or environment dumps in prompt content.

## Testing checkpoints

- Confirm every changed prompt remains discoverable through `$CODEX_HOME/docs/create-prompts.md`.
- Verify no stale references remain after rename/remove operations.
- Re-run prompt checks after any follow-up edits.

## Deployment checkpoints

- Record changed commands and migration notes for users.
- Confirm rollback path (restore prior prompt files) before release.

## Multi-agent handoff

- Coordinator assigns ownership by prompt file set and stop condition.
- When executing, report updated prompt paths, validation output, and unresolved gaps.
- Receiver confirms prompt-file guidance remained centralized in `$CODEX_HOME/docs/create-prompts.md`.

## Risks and edge cases

- Command name drift between filename and overview listing.
- Broken entrypoint links after routing/index refactors.
- Runtime/source divergence if sync is skipped or partial.

## Open questions

- None.
