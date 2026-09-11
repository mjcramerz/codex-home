# Cybersecurity Labs task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [c2-defense-ops](skills/c2-defense-ops/SKILL.md) | Run scoped C2 simulation defense operations for Cobalt Strike-like traffic, redirector behavior, reverse-shell telemetry, and SharpKatz-style credential access detection |
| [mobile-wireless-defense](skills/mobile-wireless-defense/SKILL.md) | Run scoped mobile and wireless defense operations covering Wi-Fi assessment controls, NetHunter lab build governance, rooted-device risk management, and BadUSB/Rubber Ducky resilience testing in documented scope. |
| [nethunter-pixel9a](skills/nethunter-pixel9a/SKILL.md) | Run scoped Kali NetHunter Pixel 9a kernel-porting and Android rooting lab operations, including Google kernel alignment, boot-image patch validation, and rollback-safe deployment checks. |
| [offsec-defense](skills/offsec-defense/SKILL.md) | Run scoped offensive-security simulation and cyber-defense operations |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
