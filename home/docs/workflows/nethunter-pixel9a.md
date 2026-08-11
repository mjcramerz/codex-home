# NetHunter Pixel 9a workflow
Purpose: execute NetHunter kernel porting and Android root validation for Google Pixel 9a with a documented device scope for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
You must start with `$CODEX_HOME/plans/workflows/workflow-nethunter-pixel9a.md` before executing this workflow.

## Inputs
- Scope file with allowed device IDs and allowed operation classes.
- Pixel 9a lab device and known-good USB/host tools.
- NetHunter repositories and Google kernel baseline details.
- Platform-Tools version record (`adb`/`fastboot`) captured at run start.

## Workflow steps
1) Validate scope (`scope_id`, documented device, non-expired scope window).
2) Capture device baseline and artifact inventory.
3) Align kernel source + toolchain with exact device build baseline.
4) Implement kernel-port changes in reviewable commits.
5) Build kernel artifacts and installer packages with deterministic logs.
6) Execute root/flash validation on the documented lab device.
7) Run regression checks and rollback drill.
8) Publish evidence, residual risks, and remediation backlog.

## Milestone gates
- Gate A (scope): `nethunter_scope_guard.py` passes for operation + device ID.
- Gate B (baseline): fingerprint, slot, lock state, and stock boot hash are captured.
- Gate C (build): builder/installer commits and artifact hashes are recorded.
- Gate D (flash): selected slot and boot image hash are recorded before flash.
- Gate E (rollback): known-good rollback image restores a bootable state.

## Required artifacts
- Scope manifest and scope summary.
- Device baseline report (pre-unlock and post-flash).
- Build logs, command transcripts, and hash manifest.
- Validation + rollback report.
- Source-mapping note (fingerprint -> Google kernel branch/tag -> NetHunter commits).

## Security checkpoints
- Reject operations without a documented scope or documented device ownership.
- Never bypass locked bootloader controls through exploit techniques.
- You must keep factory images and stock boot images available before flash operations.
- Restrict all activity to lab/staging and avoid production identities.
- Fail closed if slot/mode state cannot be verified (`fastboot getvar current-slot`, `is-userspace`).

## Testing checkpoints
- You must verify host tools (`adb`, `fastboot`, `sha256sum`, `python3`) before device operations.
- You must validate build outputs with deterministic hashes.
- You must re-run functional checks after each flash action.
- You must confirm rollback path with at least one successful drill.
- You must confirm expected Platform-Tools behavior for target commands from current Android docs.

## Deployment checkpoints
- You must treat flashing as change-managed operation with owner acknowledgment.
- You must document blast radius and expected data loss before unlock.
- You must define clear stop conditions and escalation contacts for failed boots.

## Multi-agent handoff
- Scope owner validates scope completeness and stop conditions.
- Build owner manages kernel/installer artifact generation.
- Device owner executes flash/rollback run and captures evidence.
- Final reviewer signs off on risk and residual action items.

See also:
- `../security/nethunter-pixel9a.md`
- `../security/security-labs-index.md`
- `$CODEX_HOME/templates/system/nethunter-pixel9a-kit/overview.md`
- `$CODEX_HOME/snippets/bash/nethunter_pixel9a_preflight.sh`
- `$CODEX_HOME/snippets/bash/nethunter_pixel9a_root_sequence.sh`
- You must use skill `nethunter-pixel9a`.
