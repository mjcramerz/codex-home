# Perl style guide
Purpose: tell the Codex coding agent how to use `docs/style/perl.md` as a runtime-pack surface and when to stop browsing.
Canonical Perl guidance for this pack. Follow repo-specific conventions first.

## Baseline
- Enable `use strict;` and `use warnings;`.
- You must prefer lexical filehandles, three-arg `open`, and explicit UTF-8 handling when reading text.
- You must keep parsing, normalization, and rendering logic in small pure functions where possible.
- You must use `Path::Tiny`, `File::Spec`, or `File::Basename` patterns instead of hand-rolled path string hacks.

## Input safety
- You must treat hook payloads, env vars, files, and subprocess output as untrusted.
- You must validate key presence, scalar shapes, ranges, and path boundaries before mutating anything.
- Avoid passing untrusted input through a shell; prefer list-form `system` or direct module APIs.

## Data formats
- You must prefer explicit JSON/TOML/YAML parsing libraries instead of regex-only transforms.
- Reparse generated output before finishing the turn.
- You must keep STDERR human-readable and STDOUT machine-readable for CLI helpers.

## Validation
- `perl -c path/to/file.pm`
- `prove -lr t` when the repo ships Perl tests

## After that, you must check related files
- `$CODEX_HOME/docs/lang/perl.md`
- `$CODEX_HOME/templates/perl/codex-hook-module/`
- `$CODEX_HOME/index/style/perl.md`
