# Prompt writing

Use this guide when the task concerns prompt writing. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when

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
- Use absolute paths for critical files and commands.
- Prefer one clear objective over multi-part requests in a single prompt.
- Call out non-negotiables first (security, data safety, rollout constraints).

## Review checklist

- Is the request concrete and bounded?
- Are acceptance criteria observable?
- Are the critical constraints explicit?
- Does the prompt tell the agent what to verify?

## See also

- `create-prompts.md`
- `workflows/planning.md`
