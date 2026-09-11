# fstab guidance

Use this guide when the task concerns fstab guidance. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

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

- Use `UUID=` or `PARTUUID=` from `blkid`.
- Keep a backup before edits.
- Validate with `mount -a` (or `findmnt --verify --verbose` when available).
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
