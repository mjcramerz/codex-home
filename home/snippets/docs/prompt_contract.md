# Prompt contract snippet
Purpose: tell the Codex coding agent how to use `snippets/docs/prompt_contract.md` as a runtime-pack surface and when to stop browsing.
Use this snippet when writing or revising slash-command prompt files.

```markdown
## Objective
<one-line outcome>

## Inputs
- `$ARGUMENTS`: <required shape/constraints>

## Constraints
- Preserve behavior unless explicitly requested.
- Keep changes minimal and reviewable.

## Verification
- <focused check>
- <pack-level check>

## Output contract
- <files changed>
- <tests/checks run>
- <risks/next steps>
```
