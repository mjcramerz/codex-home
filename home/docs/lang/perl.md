# Perl

Use this guide when you implement or review Perl modules, command-line helpers or hook adapters. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Identify the minimum Perl version, module search path, package namespace and entrypoint contract. Enable strict and warnings; keep package initialization free of external side effects.

**2.** Validate JSON shapes, string lengths, paths and encodings before use. Use lexical handles and three-argument open; check open, print, close and rename failures when the operation matters.

**3.** Use list-form system or exec with an explicit executable. Do not construct shell commands from input, use string eval for data, or treat a successful spawn as a successful child exit.

**4.** Keep stdout reserved for the documented machine-readable result. Send bounded, redacted diagnostics to stderr; preserve exit status and distinguish malformed input, tool failure and policy denial.

**5.** Run perl -c with the intended trusted library paths, then the narrow existing tests or fixture calls. Remember that compile-time BEGIN blocks can execute even during syntax checking; inspect unfamiliar modules first.

## Select related guidance

- `$CODEX_HOME/docs/style/perl.md`
- `$CODEX_HOME/templates/perl/codex-hook-module/`
- `$CODEX_HOME/index/domains/lang/perl.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
