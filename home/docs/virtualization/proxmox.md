# Proxmox VE
Purpose: tell the Codex coding agent how to use `docs/virtualization/proxmox.md` as a runtime-pack surface and when to stop browsing.
Guidance for Proxmox virtualization setups.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must treat storage layout as high‑risk; plan before creating pools.
- You must prefer templates and clones for repeatable VM creation.
- You must keep backups and verify restore workflows.

## Storage notes
- Common backends: ZFS, LVM-thin, directory.
- You must keep `storage.cfg` under version control (where safe).

## Networking
- You must use explicit bridges; document VLANs and firewall rules.

See also:
- `overview.md`
- `../filesystems/proxmox.md`
- `$CODEX_HOME/templates/virtualization/proxmox-vm-skeleton/`
- `$CODEX_HOME/snippets/proxmox/storage.cfg`
- You must use skill infra-proxmox.
- `$CODEX_HOME/index/domains/infra/virtualization.md`
- `$CODEX_HOME/index/domains/infra/proxmox.md`
