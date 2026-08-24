---
title: Latest sources for nethunter-pixel9a
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- references
- latest-sources-md
- latest-sources
- user
- security-labs
updated: '2026-02-20'
---
# Latest sources for nethunter-pixel9a

Retrieved and reviewed on 2026-02-13 (UTC) using Context7 + web lookups.

## Retrieval notes
- Context7 source used: `/websites/source_android_core` (bootloader/fastbootd/GKI topics).
- Web lookup source used for Kali and Android page freshness checks.
- Fetch MCP attempts in this runtime failed with:
  - `Command '['npm', 'version']' died with <Signals.SIGSYS: 31>.`
  - Until resolved, use Context7 + web lookups as fallback.

## Freshness markers captured on 2026-02-13 (UTC)
- Kali NetHunter `building-nethunter` and `porting-nethunter-kernel-builder` pages:
  - Updated on `2025-Jun-18`.
- Android bootloader lock/unlock and fastbootd pages:
  - Last updated `2025-12-02 UTC`.
- Android Platform-Tools page:
  - Last updated `2026-02-10 UTC`.
  - Latest listed release: `35.0.2 (July 2024)`.
- Android GKI releases page:
  - Last updated `2026-01-14 UTC`.

## Kali NetHunter
- https://www.kali.org/docs/nethunter/building-nethunter/
- https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/
- https://www.kali.org/docs/nethunter/porting-nethunter/
- https://www.kali.org/docs/nethunter/nethunter-kernel-1-patching/
- https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder
- https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer

## Android platform
- https://source.android.com/docs/core/architecture/bootloader/locking_unlocking
- https://source.android.com/docs/core/architecture/bootloader/fastbootd
- https://source.android.com/docs/core/architecture/kernel/gki-releases
- https://source.android.com/docs/core/ota/ab
- https://developer.android.com/tools/releases/platform-tools

## Defensive baseline
- https://attack.mitre.org/
- https://csrc.nist.gov/publications/detail/sp/800-115/final
- https://www.cisa.gov/resources-tools/resources/mobile-security-best-practices
