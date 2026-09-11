# Virtualization task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [infra-proxmox](skills/infra-proxmox/SKILL.md) | Operate Proxmox VE virtual machines, storage, and networking with cluster-safe procedures |
| [infra-virsh](skills/infra-virsh/SKILL.md) | Manage libvirt and KVM virtual machines directly with virsh commands and XML-based domain control |
| [infra-virtualization](skills/infra-virtualization/SKILL.md) | Design VM-based virtualization using QEMU/KVM/libvirt and Vagrant with reproducible network and storage layout |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
