# Browsers workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-browsers.md` before executing this workflow.
Purpose: install and harden desktop browsers safely for the Codex coding agent.
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
1) **Scope**: threat model, user-data location, extension policy.
2) **Install**: use vendor‑signed builds; verify provenance.
3) **Configure**: apply overrides or policies.
4) **Integrate**: add `.desktop` entries and Wayland flags.
5) **Verify**: test user-data directory permissions and updates.

## Safety rules
- You must keep browser user-data directories in `0700` directories.
- Avoid running browsers as root.

## Security checkpoints
- You must verify package signatures/checksums and trusted update channels for each browser build.
- Apply extension and policy allowlists; disable risky debug or unmanaged user-data paths.
- You must keep user-data directories at `0700` and system policy files root-owned.

## Testing checkpoints
- Launch with hardened browser state and confirm policies are applied as expected.
- You must validate required internal sites, SSO flows, and certificate trust behavior.
- Test Wayland and `.desktop` integration paths used by target users.

## Deployment checkpoints
- Pilot one browser/user-data combination before expanding to wider user groups.
- You must keep prior browser package and policy snapshots for fast rollback.
- You must define update cadence, ownership, and post-update compatibility checks.

## Multi-agent handoff
- Coordinator shares target browser versions, user-data paths, and extension policy scope.
- Executor records installed builds, policy files changed, and user-impact findings.
- Receiver drives broad rollout communication and tracks post-update regressions.
See also:
- `overview.md`
- `../desktop/browsers.md`
- `../desktop/librewolf.md`
- `../desktop/mullvad-browser.md`
- `../desktop/thorium.md`
- You must use skill `desktop-browser-hardening`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/desktop/browsers.md`
