---
title: React Native Rules Adapted for Web React
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-react
- references
- react-native-web-adaptations-md
- react-native-web-adaptations
- user
- web
updated: '2026-02-25'
---
# React Native Rules Adapted for Web React

This guide adapts patterns from:

## Mapping table
| React Native rule theme | Web React adaptation |
| --- | --- |
| `list-performance-virtualize` | Use virtualization (`react-window`, `@tanstack/react-virtual`) for long lists |
| `list-performance-item-memo` | Keep row/card props primitive and memo-friendly |
| `list-performance-callbacks` | Hoist list callbacks and keep stable function identities |
| `list-performance-inline-objects` | Avoid inline style/object literals in hot render loops |
| `animation-gpu-properties` | Animate transform/opacity; avoid layout-triggering properties |
| `scroll-position-no-state` | Track scroll in refs/throttled handlers, not high-frequency state |
| `ui-pressable` | Prefer semantic `button`/`a` plus pointer/keyboard parity |
| `ui-expo-image` | Optimize web images (responsive `srcset`, dimensions, lazy loading) |
| `ui-safe-area-scroll` | Respect safe-area insets for mobile-web layouts where relevant |
| `react-state-minimize` | Keep minimal source-of-truth state and derive the rest |
| `state-ground-truth` | Ensure each state value represents user-observable truth |

## Practical application sequence
1. Stabilize list rendering behavior.
2. Reduce animation/layout thrash.
3. Normalize input/press interactions.
4. Remove redundant or derived state.

## Validation hints
- Profile list scrolling and interaction latency.
- Confirm no regressions in keyboard behavior when replacing interactive primitives.
- Record measured wins (fps, interaction latency, rerender counts).
