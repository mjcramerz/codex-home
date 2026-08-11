# Debian preseed workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-debian-preseed.md` before executing this workflow.
Purpose: guide unattended Debian installation work, with concrete alignment to the `debian-preseed-di` repository and its staged desktop or service roles, for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Repo anchors
- `d-i/debian/preseed.cfg` and `d-i/debian/common.cfg` for the top-level staged include flow
- `d-i/debian/classes/install.conf` and `d-i/debian/classes/configs/*.cfg` for manifest-driven class metadata
- `d-i/debian/classes/class-select/**`, `class-auto/**`, and `class-addon/**` for role, hardware, network, service, and addon behavior
- `d-i/debian/hosts/profiles/**`, `hosts/shared/**`, and service env fragments for rendered target policy
- `d-i/debian/scripts/preseed/**`, `scripts/early/**`, `scripts/partman/**`, `scripts/late/**`, and `scripts/runtime/**` for staged behavior
- repo-local smoke or functional tests under `t/*.sh`

## Safety first
- Preseed can wipe disks. Always validate in a VM before real hardware.
- Keep preseed files under version control but never store plaintext passwords or deployment secrets.
- Use HTTPS for hosted preseeds when practical and restrict access where possible.

## Core settings checklist
- Locale, keyboard, timezone, and installer source handling
- Class selection (site, role, security, network, service, addon) and any auto-detected classes
- Network behavior (DHCP vs static, optional Wi-Fi addon)
- Partitioning strategy, confirmation flags, and destructive storage targets
- User creation and password hashing or injection flow
- Package selection, upgrades, and addon packages
- Bootloader, reboot behavior, and first-boot runtime helpers

## Repo-specific contract
- Keep storage, class selection, and late-command behavior grounded in the tracked repo contracts.
- Treat kernel command-line inputs as untrusted and validate shape early.
- Keep secrets out of tracked seeds; prefer deployment-time injection for sensitive values.
- Re-test both happy-path and failure-path boot or install behavior after material preseed changes.
- When desktop roles are involved, keep Labwc, Waybar, Wofi, Crystal Dock, Foot, Kitty, lock, and greeter helpers aligned with the staged role helpers and smoke tests.
- When service addons are involved, keep GitLab Runner, Aptly, Bazel, BuildBuddy, Podman, and related env or helper contracts aligned with the staged host service assets and tests.

## Split-file approach (recommended)
- Keep `preseed.cfg` minimal and include split seeds or staged helper entrypoints.
- Separate account, network, apt, and partman settings.
- Review only the seed, class, or helper you change; reduce risk.

## High-risk flags
- Disk target (`partman-auto/disk`) must be explicit.
- Confirmation flags must match the intended destructive actions.
- `late_command` should stage deterministic target-side helpers instead of carrying large inline shell bodies.

## Template
- `$CODEX_HOME/templates/virtualization/debian-preseed/`

## Security checkpoints
- Use hashed credentials only and protect hosted preseed delivery with access controls.
- Pin destructive disk targets explicitly for each hardware or storage class.
- Treat late-command assets as sensitive and rotate bootstrap secrets after install.

## Testing checkpoints
- Run unattended installs in VMs that match BIOS or UEFI modes used in production.
- Verify partition layout, class expansion, account policy, package set, and bootloader state post-install.
- Re-run the narrowest repo-local smoke tests for the changed class, service, or desktop helper path.
- Test failure paths such as unreachable mirrors, missing staged assets, or invalid cmdline answers when the touched surface changes that behavior.

## Deployment checkpoints
- Gate physical rollout on a validated preseed revision and golden image checksum.
- Keep the prior preseed revision and boot params for rollback in provisioning systems.
- Stage rollout by hardware baseline and archive installer or first-boot logs per batch.

## Multi-agent handoff
- Coordinator defines hardware matrix, destructive flags, and required approvals.
- Executor publishes preseed revision, boot parameters, and post-install evidence.
- Receiver tracks field results and opens drift fixes for any baseline mismatch.

## After that, you must check related files
- `overview.md`
- `../virtualization/debian-preseed.md`
- `$CODEX_HOME/docs/workflows/gitlab-runner.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- You must use skill `os-debian-preseed`.
- `$CODEX_HOME/snippets/virtualization/preseed_boot_params.txt`
- `$CODEX_HOME/snippets/preseed/include.preseed.cfg`
- `../virtualization/overview.md`
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/debian-preseed.md`
