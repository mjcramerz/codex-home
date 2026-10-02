# Pixel 9a NetHunter porting checklist (controlled)

Use this template when you need pixel 9a nethunter porting checklist (controlled) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

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
