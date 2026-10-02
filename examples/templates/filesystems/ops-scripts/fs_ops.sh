#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

usage() {
  cat <<'USAGE'
fs_ops.sh <probe|plan|apply> [options]

Options:
  --device <path>         Stable device path (/dev/disk/by-id/... or /dev/disk/by-path/...)
  --fstype <type>         ext4|xfs|btrfs|f2fs|exfat|vfat|ntfs
  --mountpoint <path>     Absolute mountpoint (e.g., /data)
  --label <label>         Filesystem label (optional)
  --mount-options <opts>  fstab/mount options (default: defaults,noatime)
  --partition <none|single>  Partitioning mode (default: none)
  --partition-table <gpt|mbr> Partition table type (default: gpt)
  --write-fstab           Append UUID-based entry to /etc/fstab
  --fstab <path>          Override fstab path (default: /etc/fstab)
  --danger-erase          Required for partitioning
  --force                 Allow existing partitions/mounts (dangerous)
  --allow-unstable        Allow /dev/sdX style paths (discouraged)
  -h, --help              Show this help

Examples:
  ./fs_ops.sh probe
  ./fs_ops.sh plan --device /dev/disk/by-id/XYZ --fstype ext4 --mountpoint /data
  ./fs_ops.sh apply --device /dev/disk/by-id/XYZ --fstype ext4 --mountpoint /data \
    --partition single --danger-erase --write-fstab
USAGE
}

die() { echo "ERROR: $*" >&2; exit 1; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "missing command: $1"
}

require_root() {
  [[ "$(id -u)" -eq 0 ]] || die "must run as root"
}

cmd="${1:-}"
shift || true

case "$cmd" in
  probe|plan|apply) ;;
  ""|"-h"|"--help") usage; exit 0 ;;
  *) die "unknown command: $cmd" ;;
esac

device=""
fstype=""
mountpoint=""
label=""
mount_opts="defaults,noatime"
partition="none"
partition_table="gpt"
write_fstab=0
fstab_file="/etc/fstab"
danger_erase=0
force=0
allow_unstable=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --device) device="${2:-}"; shift 2 ;;
    --fstype) fstype="${2:-}"; shift 2 ;;
    --mountpoint) mountpoint="${2:-}"; shift 2 ;;
    --label) label="${2:-}"; shift 2 ;;
    --mount-options) mount_opts="${2:-}"; shift 2 ;;
    --partition) partition="${2:-}"; shift 2 ;;
    --partition-table) partition_table="${2:-}"; shift 2 ;;
    --write-fstab) write_fstab=1; shift ;;
    --fstab) fstab_file="${2:-}"; shift 2 ;;
    --danger-erase) danger_erase=1; shift ;;
    --force) force=1; shift ;;
    --allow-unstable) allow_unstable=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "unknown option: $1" ;;
  esac
done

if [[ "$cmd" == "probe" ]]; then
  require_cmd lsblk
  require_cmd blkid
  echo "== lsblk =="
  lsblk -o NAME,PATH,SIZE,TYPE,FSTYPE,FSVER,MOUNTPOINT,UUID,PARTUUID,MODEL
  echo
  echo "== blkid =="
  blkid || true
  exit 0
fi

[[ -n "$device" ]] || die "--device is required"
[[ -n "$fstype" ]] || die "--fstype is required"
[[ -n "$mountpoint" ]] || die "--mountpoint is required"
[[ "$mountpoint" == /* ]] || die "--mountpoint must be absolute"

case "$fstype" in
  ext4|xfs|btrfs|f2fs|exfat|vfat|ntfs) ;;
  zfs) die "zfs is not supported by this script; use zpool/zfs tools" ;;
  *) die "unsupported fstype: $fstype" ;;
esac

case "$partition" in
  none|single) ;;
  *) die "unsupported --partition: $partition" ;;
esac

case "$partition_table" in
  gpt|mbr) ;;
  *) die "unsupported --partition-table: $partition_table" ;;
esac

if [[ "$allow_unstable" -ne 1 ]]; then
  case "$device" in
    /dev/disk/by-id/*|/dev/disk/by-path/*) ;;
    *) die "use a stable device path (/dev/disk/by-id or /dev/disk/by-path), or pass --allow-unstable" ;;
  esac
fi

device_real="$device"
[[ -b "$device_real" ]] || die "not a block device: $device_real"

require_cmd lsblk

dev_type="$(lsblk -no TYPE "$device_real" | head -n1)"
if [[ "$partition" == "none" && "$dev_type" == "disk" ]]; then
  die "device is a disk; pass a partition path or use --partition single"
fi

if [[ "$partition" == "single" ]]; then
  [[ "$danger_erase" -eq 1 ]] || die "--danger-erase required for partitioning"
  [[ "$dev_type" == "disk" ]] || die "partitioning requires a disk device"
fi

if [[ "$cmd" == "apply" ]]; then
  require_root
fi

run() {
  if [[ "$cmd" == "apply" ]]; then
    "$@"
  else
    echo "+ $*"
  fi
}

if [[ "$partition" == "single" ]]; then
  if [[ "$force" -ne 1 ]]; then
    if lsblk -nr -o MOUNTPOINT "$device_real" | grep -q '/'; then
      die "device has mounted partitions; use --force to override"
    fi
  fi

  require_cmd sfdisk
  case "$partition_table" in
    gpt) ;;
    mbr) ;;
  esac
  run sfdisk --wipe always --wipe-partitions always "$device_real" <<EOF
label: $partition_table
, , L
EOF

  if command -v partprobe >/dev/null 2>&1; then
    run partprobe "$device_real"
  fi
  if command -v udevadm >/dev/null 2>&1; then
    run udevadm settle
  fi
fi

target_partition="$device_real"
if [[ "$dev_type" == "disk" ]]; then
  if [[ "$device_real" == *"nvme"* || "$device_real" == *"mmcblk"* ]]; then
    target_partition="${device_real}p1"
  else
    target_partition="${device_real}1"
  fi
fi

case "$fstype" in
  ext4) mkfs_cmd=(mkfs.ext4 -F) ;;
  xfs) mkfs_cmd=(mkfs.xfs -f) ;;
  btrfs) mkfs_cmd=(mkfs.btrfs -f) ;;
  f2fs) mkfs_cmd=(mkfs.f2fs -f) ;;
  exfat) mkfs_cmd=(mkfs.exfat) ;;
  vfat) mkfs_cmd=(mkfs.vfat -F 32) ;;
  ntfs)
    if command -v mkfs.ntfs >/dev/null 2>&1; then
      mkfs_cmd=(mkfs.ntfs -F)
    else
      mkfs_cmd=(mkntfs -F)
    fi
    ;;
esac

if [[ -n "$label" ]]; then
  case "$fstype" in
    ext4|xfs|btrfs|f2fs) mkfs_cmd+=(-L "$label") ;;
    exfat) mkfs_cmd+=(-n "$label") ;;
    vfat) mkfs_cmd+=(-n "$label") ;;
    ntfs) mkfs_cmd+=(-L "$label") ;;
  esac
fi

require_cmd "${mkfs_cmd[0]}"
run "${mkfs_cmd[@]}" "$target_partition"

run mkdir -p "$mountpoint"
run mount -t "$fstype" -o "$mount_opts" "$target_partition" "$mountpoint"

if [[ "$write_fstab" -eq 1 ]]; then
  require_cmd blkid
  uuid="$(blkid -s UUID -o value "$target_partition")"
  [[ -n "$uuid" ]] || die "unable to read UUID for $target_partition"

  line="UUID=$uuid  $mountpoint  $fstype  $mount_opts  0  2"
  if [[ "$cmd" == "apply" ]]; then
    if grep -qsE "^[^#]*\\s+$mountpoint\\s" "$fstab_file"; then
      die "mountpoint already present in $fstab_file: $mountpoint"
    fi
    if grep -qsE "^[^#]*UUID=$uuid\\s" "$fstab_file"; then
      die "UUID already present in $fstab_file: $uuid"
    fi
    cp -a "$fstab_file" "${fstab_file}.bak.$(date +%Y%m%d%H%M%S)"
    printf '%s\n' "$line" >>"$fstab_file"
  else
    echo "+ echo '$line' >> $fstab_file"
  fi
fi

echo "Done."
