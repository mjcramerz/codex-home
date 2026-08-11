# /<command>
Purpose: tell the Codex coding agent how to use `templates/prompts/slash-command-maintenance/prompt-template.md` as a runtime-pack surface and when to stop browsing.

## Objective
State exactly what this command should achieve.

## Inputs
- `$ARGUMENTS`: required argument contract and accepted formats.
- Optional context constraints.

## Constraints
- Preserve existing behavior unless explicitly requested.
- You must keep output deterministic and reviewable.
- Avoid unsafe or destructive operations without explicit confirmation.

## You must follow this workflow
1) Confirm the task scope and assumptions.
2) Inspect only the files needed for this command.
3) Apply minimal edits and keep references synchronized.
4) Run focused verification before full pack verification.

## Verification

## Output contract
- Provide changed file paths.
- Provide checks run and outcomes.
- Provide residual risks or next steps.
