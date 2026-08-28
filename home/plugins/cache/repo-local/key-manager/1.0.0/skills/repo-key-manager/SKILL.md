---
name: repo-key-manager
description: Work securely in the key-manager Go repository across SSH, GPG, post-quantum, TLS, configuration, filesystem, subprocess, UI modules, review, and validation while preserving secret handling, path validation, symlink refusal, and test isolation.
---

# Key Manager repository workflow

## Start

1. Resolve the current Git root; do not assume a machine-local clone path.
2. Confirm the root contains `AGENTS.md`, `go.mod`, `cmd/key-manager/`, `internal/`, and `config/`.
3. Read `AGENTS.md` plus any deeper instruction file governing the touched path.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch`; never print `.env`, key, certificate, or credential contents.

## Security boundary

- Use `internal/executil` for subprocesses; never add `sh -c` or constructed shell commands.
- Use `internal/fs` helpers for atomic writes and symlink refusal.
- Validate domains, SANs, emails, filenames, output roots, permissions, and ownership before mutation.
- Refuse traversal and symlink ambiguity.
- Keep tests on synthetic values such as `example.com`; never use real identities, keys, or certificates.
- Do not run install, uninstall, clean, live key generation, certificate issuance, or privileged TLS flows during ordinary validation.

## Workflow

1. Route from `cmd/key-manager/` into the owning package under `internal/`.
2. Identify trust boundaries for inputs, generated files, subprocesses, ownership, and privilege.
3. Add focused tests beside the changed package for validation, file generation, and error paths.
4. Keep errors short, lowercase, and actionable; preserve standard-library-first Go style.

## Validation

- Run `gofmt` on changed Go files.
- Run `make test`.
- Run `make lint`.
- Confirm tests use temporary directories and synthetic secret material only.
- Do not run `make install`, `make uninstall`, or `make clean`.

## Handoff

Report the owning packages changed, tests and vet results, secret-handling impact, and any privileged validation not run.
