# fstab guidance
Purpose: tell the Codex coding agent how to use `docs/filesystems/fstab.md` as a runtime-pack surface and when to stop browsing.
`/etc/fstab` controls persistent mounts. Prefer UUID-based entries and validate before reboot.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/filesystems/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Format (fields)
```
<spec>  <mountpoint>  <fstype>  <options>  <dump>  <pass>
```

## Best practices
- You must use `UUID=` or `PARTUUID=` from `blkid`.
- You must keep a backup before edits.
- You must validate with `mount -a` (or `findmnt --verify --verbose` when available).
- For optional data volumes, consider `nofail` and systemd timeouts:
  - `x-systemd.device-timeout=30s`
  - `x-systemd.automount` for lazy mounts

## Example
```
UUID=1111-2222  /data  ext4  defaults,noatime,nofail,x-systemd.device-timeout=30s  0  2
```

## Notes by filesystem
- **btrfs**: add `subvol=<name>` when mounting subvolumes.
- **vfat/exfat/ntfs**: you may need `uid=`, `gid=`, and `umask=` for permissions.
- **zfs**: typically managed by ZFS tools, not `/etc/fstab`.

## References
- `overview.md`
- `filesystem-types.md`
- `../systemd/overview.md`
- `$CODEX_HOME/index/domains/system/filesystems.md`
