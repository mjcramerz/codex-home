# Codex hook module template

Use this template when you need codex hook module in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

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
