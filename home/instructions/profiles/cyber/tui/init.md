# Initialize repository guidance

Inspect the current repository's language, build entrypoints, CI commands and
existing `AGENTS.md` files. When the task is to create or update repository guidance,
write concise instructions addressed directly to the coding assistant: scope,
commands verified to exist, conventions, safety boundaries and completion criteria.

Do not invent Makefile targets, deployment paths or tool availability. Do not copy
the global runtime library or configuration schema into repository instructions.
Preserve existing useful guidance and user-owned changes. Create no files unless
the current request authorizes them.
