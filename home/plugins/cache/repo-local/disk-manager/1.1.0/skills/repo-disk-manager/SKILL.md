---
name: repo-disk-manager
description: Work safely in the disk-manager Go repository across CLI, internal packages, configuration, installers, storage policy, review, and validation without real disk, filesystem, NVMe, LUKS, mount, or host-install operations.
---

# Disk Manager repository workflow

## Start

1. Resolve the current Git root; do not assume a machine-local clone path.
2. Confirm the root contains `go.mod`, `Makefile`, `cmd/`, `internal/`, and `configs/`.
3. Read all applicable repository instructions before editing.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch` and preserve unrelated user state.

## Safety boundary

- Treat code under `cmd/` and `internal/`, shipped policy under `configs/`, and repository scripts as source.
- Do not run the interactive application as routine validation.
- Do not invoke `mkfs`, `wipefs`, `sgdisk`, `sfdisk`, `cryptsetup`, `nvme`, mount operations, secure erase, or any command against `/dev/**`.
- Do not run install, uninstall, nuke, or host-policy mutation flows during ordinary repository work.
- Use fixtures, command construction tests, and temporary directories instead of real block devices.

## Workflow

1. Trace the requested behavior from the command entrypoint into the owning internal package and configuration.
2. Identify whether the change affects destructive confirmation, device identity, geometry, filesystem policy, LUKS/NVMe handling, or generated host state.
3. Add or update focused Go tests for input validation, command planning, and failure behavior.
4. Keep host-side execution behind existing guardrails and interfaces.

## Validation

- Run `gofmt` on changed Go files.
- Run the repository's safe validation target: `make check`.
- Review the test output for any attempted device, mount, privilege, or host mutation.
- Do not replace `make check` with an installer or interactive smoke run.

## Handoff

Report the code and policy paths changed, `make check` result, destructive-operation risk, and any validation not run.
