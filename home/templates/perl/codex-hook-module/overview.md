# Codex hook module template
Purpose: scaffold a small Perl hook/runtime module with a matching CLI wrapper for local validation for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Inputs
- Module name
- Hook/runtime purpose
- Expected input/output shape

## Outputs
- `lib/Codex/Hook/Example.pm`
- `bin/example-hook.pl`

## Next steps
1. Rename the module/package.
2. Keep hook output schema-first: machine-readable stdout, human-readable stderr, and explicit payload validation.
3. Add repo-local validation such as `perl -c` plus any hook-schema or fixture checks.
4. Wire the module into the hook/runtime entrypoint that will call it.
