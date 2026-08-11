# Proxmox filesystem guidance
Purpose: tell the Codex coding agent how to use `docs/filesystems/proxmox.md` as a runtime-pack surface and when to stop browsing.
Notes for Proxmox-compatible storage layouts.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/filesystems/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Common backends
- **ZFS**: snapshots, compression, integrity checks.
- **LVM-thin**: efficient thin provisioning for VM disks.
- **Directory storage**: simple, flexible (less snapshot capability).

## Safety baseline
- Plan storage before creating VMs; migrations are disruptive.
- You must keep backups and test restore paths.
- You must document `storage.cfg` changes and keep UUIDs stable.

See also:
- `overview.md`
- `filesystem-types.md`
- `../virtualization/proxmox.md`
- `$CODEX_HOME/snippets/proxmox/storage.cfg`
- `$CODEX_HOME/index/domains/system/filesystems.md`
