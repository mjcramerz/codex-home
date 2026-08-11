# Prompt writing
Purpose: write concise, testable prompts that produce deterministic engineering outputs for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
- you need general prompt-writing advice that is not specific to runtime prompt assets
- you want to improve instruction quality, precision, or validation wording

## Include (high-signal)
- exact behavior to implement
- acceptance criteria (observable, verifiable)
- constraints (no network, target OS, perf budget)
- examples (inputs/outputs) when behavior is subtle
- tests to add or run
- threat model notes when handling untrusted input

## Avoid
- long preambles
- restating generic best practices
- ambiguous scope (“make it better” without a target)

## Tips
- Reference files or modules to anchor the agent.
- You must use absolute paths for critical files and commands.
- You must prefer one clear objective over multi-part requests in a single prompt.
- Call out non-negotiables first (security, data safety, rollout constraints).

## Review checklist
- Is the request concrete and bounded?
- Are acceptance criteria observable?
- Are the critical constraints explicit?
- Does the prompt tell the agent what to verify?

## See also
- `create-prompts.md`
- `workflows/planning.md`
