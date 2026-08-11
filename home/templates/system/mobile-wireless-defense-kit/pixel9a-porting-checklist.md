# Pixel 9a NetHunter porting checklist (controlled)
Purpose: tell the Codex coding agent how to use `templates/system/mobile-wireless-defense-kit/pixel9a-porting-checklist.md` as a runtime-pack surface and when to stop browsing.

## Source control
- [ ] Record Google kernel source revision and manifest.
- [ ] Record NetHunter builder/installer revision IDs.
- [ ] Capture toolchain version and build host metadata.

## Patch and build
- [ ] Apply patch set in reviewable commits.
- [ ] Keep build logs and checksums for each artifact.
- [ ] Produce rollback image for each successful build.

## Validation
- [ ] Boot stability validation in lab.
- [ ] Wi-Fi/Bluetooth/modem smoke tests.
- [ ] USB and HID behavior validation.
- [ ] Security regression checks and segmentation validation.
