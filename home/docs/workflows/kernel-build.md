# Kernel build workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-kernel-build.md` before executing this workflow.
Purpose: build and deploy a custom kernel safely for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: target hardware, modules, and policy requirements.
2) **Prepare**: pin toolchain, obtain source, verify signatures.
3) **Configure**: start from distro config and apply fragments.
4) **Build**: compile and package with reproducible flags.
5) **Install**: keep previous kernel available for rollback.
6) **Verify**: boot, validate modules, run smoke tests.

## Safety rules
- Never remove the last known‑good kernel.
- Test in a VM before deploying to bare metal.

## Security checkpoints
- You must verify source tarballs/tags and patch provenance before build starts.
- Protect module or kernel signing keys and document signing policy.
- Review config fragments for unintended debug or insecure options.

## Testing checkpoints
- Build in a clean environment and archive config/toolchain metadata.
- Boot-test on VM or canary hardware and validate required module loading.
- You must run smoke and regression benchmarks against the previous known-good kernel.

## Deployment checkpoints
- Install new kernel alongside existing fallback entries; never remove last-known-good.
- Promote through a canary ring before wider rollout.
- You must document rollback steps (`grub-reboot`, package downgrade, rescue path) with owner.

## Multi-agent handoff
- Coordinator sets hardware matrix, mandatory modules, and policy constraints.
- Executor shares config diff, artifact locations, and boot-test logs.
- Receiver owns staged rollout tracking and regression triage.
See also:
- `overview.md`
- `../system/kernel.md`
- `$CODEX_HOME/templates/system/kernel-build-skeleton/`
- `$CODEX_HOME/snippets/system/kernel-config.fragment`
- You must use skill `infra-kernel`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/kernel.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
