# System Infra task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [aptly](skills/aptly/SKILL.md) | Manage Aptly repositories with deterministic snapshot promotion, signing, cleanup, and publication contracts |
| [debian-preseed](skills/debian-preseed/SKILL.md) | Plan and review Debian preseed repositories with class manifests, destructive-storage safeguards, and staged installer hooks |
| [infra-grub](skills/infra-grub/SKILL.md) | Modify GRUB bootloader configuration and kernel parameters with rollback-aware safety checks |
| [infra-kernel](skills/infra-kernel/SKILL.md) | Build and validate custom Linux kernel configurations with reproducible compile and boot validation steps |
| [infra-optimizations](skills/infra-optimizations/SKILL.md) | Use this skill for tune host performance and security settings with measurement-first baselines and rollback controls |
| [infra-sysctl](skills/infra-sysctl/SKILL.md) | Apply kernel sysctl parameter changes with safe rollout, verification, and rollback guidance |
| [infra-systemd](skills/infra-systemd/SKILL.md) | Use this skill for design, harden, and validate systemd services and timers including unit files, restart behavior, and sandbox directives |
| [ops-logrotate](skills/ops-logrotate/SKILL.md) | Design logrotate policies for predictable retention, rotation cadence, and service-safe log handling |
| [os-debian-preseed](skills/os-debian-preseed/SKILL.md) | Create and review Debian preseed automation files for unattended installations with deterministic installer behavior, class-driven profiles, and staged runtime helpers |
| [perf-profiling](skills/perf-profiling/SKILL.md) | Profile and optimize application or system performance using benchmarking, hot-path analysis, and regression guards |
| [storage-filesystems](skills/storage-filesystems/SKILL.md) | Design safe filesystem provisioning including partitioning, mkfs, mounts, and fstab entries with rollback notes |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
