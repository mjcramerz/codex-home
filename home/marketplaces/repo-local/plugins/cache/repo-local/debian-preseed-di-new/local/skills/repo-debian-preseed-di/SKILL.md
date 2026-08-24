---
name: repo-debian-preseed-di
description: Work safely in the Debian Installer preseed repository, including d-i/forky installer policy, class and profile configuration, installer-stage scripts, tracked target mirrors, source-first changes, review, and focused validation.
---

# Debian Preseed DI repository workflow

## Start

1. Resolve the current Git root; do not search for or assume a machine-local workspace path.
2. Confirm the root contains `AGENTS.override.md`, `d-i/forky/`, and `t/`.
3. Read `AGENTS.override.md` plus any deeper instruction file governing the touched path.
4. Require branch `mcr/main` before authored edits.
5. Inspect `git status --short --branch`; preserve all unrelated and untracked user state.

## Source of truth

- Treat `d-i/forky/` as installer source. Start routing at `preseed.cfg`.
- Keep static answers in `common.cfg` and `fragments/*.cfg`.
- Keep class metadata in `classes/install.conf` and `classes/configs/*.cfg`; keep implementations under `class-*`.
- Keep authoritative host policy in `hosts/profiles/**` and shared defaults in `hosts/shared/*.env`.
- Keep stage logic separated under `scripts/{preseed,early,partman,late,firstboot,runtime}/`.
- Treat tracked `hooks/{shared,hardware,role,services}/**/target/**` files as install-path mirrors. Edit the tracked source or template that owns the result; never patch installer runtime output under `/tmp/install-runtime/**`.
- Preserve the fresh-install model. Do not add upgrade or migration behavior that depends on an earlier target state.

## Workflow

1. Trace the requested behavior from preseed or class/profile policy into the exact stage script, hook, template, or tracked mirror that implements it.
2. Make the smallest source-first change and synchronize only directly owned mirrors.
3. Do not use the development host's packages, services, `/etc`, logs, or live installer state as intended-state evidence.
4. Do not add tests under `t/` unless the user requests them. Adapt existing focused tests to the code, never production code to an overly broad verifier.

## Validation

- Run the narrowest existing test that owns the changed contract.
- Use `bash t/<focused-test>.sh` for focused shell tests.
- Use `prove -v t/<focused-test>.t` for focused Perl tests.
- Avoid a broad test sweep unless the touched contract is shared or the repository instructions require it.
- Never write into a real installer target or the development host during validation.

## Handoff

Report the exact source paths changed, focused tests run, fresh-install or security implications, and any validation intentionally not run.
