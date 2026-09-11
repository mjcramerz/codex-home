# Create prompts

Use this guide when the task concerns create prompts. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Scope

- This is the only documentation file under `$CODEX_HOME/*` that should directly reference prompt files in `$CODEX_HOME/.prompt/`.
- Use it when creating, revising, or reviewing reusable prompt assets intended for Codex requests.

## Current prompt files

- `$CODEX_HOME/.prompt/codex-general.md`
- `$CODEX_HOME/.prompt/bugfix.md`
- `$CODEX_HOME/.prompt/feature-implementation.md`
- `$CODEX_HOME/.prompt/code-review.md`
- `$CODEX_HOME/.prompt/docs-refresh.md`
- `$CODEX_HOME/.prompt/shell-runtime.md`
- `$CODEX_HOME/.prompt/windows-manager.md`

## File contract

- Every prompt file must be Markdown.
- The first line must be a short HTML comment that describes the prompt in one sentence.
- The body should be ready to paste into a Codex request with minimal editing.
- Keep the wording concrete, directive, and operational rather than conversational.

## Design rules

- Start with the role and domain depth that the task actually needs.
- State the task objective early.
- Require read-first behavior before edits.
- Call out critical constraints explicitly: correctness, security, compatibility, rollout, or testing.
- Prefer deterministic instructions over vague requests such as “improve this” or “make it better”.
- Keep prompts concise enough to scan quickly, but detailed enough to drive the full task without extra interpretation.

## Maintenance notes

- Keep prompt file names lower-case and hyphenated.
- When adding a new prompt file, update this document and nowhere else in `$CODEX_HOME/*`.
- Do not reference transient local state or machine-specific secrets from prompt assets.
