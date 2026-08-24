---
name: repo-debian-usb
description: Work safely in the Debian USB repository across Go, Python, shell helpers, configuration, ISO construction, host installation, and removable-media operations while excluding real-media writes and host mutation.
---

# Debian USB repository workflow

## Start

1. Resolve the current Git root; do not assume a machine-local clone path.
2. Confirm the root contains `Makefile`, `go.mod`, `cmd/debian-usb/`, `scripts/`, `src/python/`, and `tests/`.
3. Read all applicable repository instructions before editing.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch` and preserve unrelated user changes, including generated or build-tree state already present.

## Safety boundary

- Treat Go code under `cmd/` and `internal/`, Python code under `src/python/`, helpers under `scripts/`, hooks under `config-hooks/`, and shipped configuration under `configs/` as source.
- Do not run the interactive application, write helpers, ISO write paths, or commands against real `/dev/**` devices.
- Do not run `make install`, `make uninstall`, `make nuke`, or any sudo-backed host mutation.
- Use temporary directories and staged `DESTDIR` behavior only where the repository's safe tests already do so.
- Preserve the repository's explicit root refusal and host-write planning messages.

## Workflow

1. Trace the requested behavior through the owning language and helper boundary.
2. Keep Go, Python, shell, config, and hook changes synchronized only when they implement the same contract.
3. Validate all external paths, media identities, sizes, mount state, and privilege assumptions before any mutation-capable code path.
4. Add focused tests in the existing language-specific test location.

## Validation

- Run `gofmt` on changed Go files.
- Run the repository's safe validation target: `make check`.
- Confirm shell syntax checks and Python unit tests complete without sudo or real media.
- Do not use `make run` as routine validation.

## Handoff

Report the language and helper paths changed, `make check` result, removable-media or privilege risk, and any validation intentionally skipped.
