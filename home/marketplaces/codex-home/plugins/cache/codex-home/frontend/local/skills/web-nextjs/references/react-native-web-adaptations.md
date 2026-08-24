---
title: React Native to Web Adaptations for Next.js
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nextjs
- references
- react-native-web-adaptations-md
- react-native-web-adaptations
- user
- web
updated: '2026-02-25'
---
# React Native to Web Adaptations for Next.js

This guide adapts mobile-focused patterns from:

## High-impact adaptations
| React Native guidance | Web/Next.js adaptation |
| --- | --- |
| Virtualize lists by default | Use list virtualization (`@tanstack/react-virtual`, `react-window`) for long feeds and admin tables |
| Avoid inline objects/functions in item render | Keep stable props for memoized row/card components |
| Animate transform/opacity only | Prefer transform/opacity animations over layout-triggering properties |
| Do not store scroll position in state | Track scroll with refs/throttled handlers to avoid rerender storms |
| Use modern press primitives | Prefer semantic `button`/`a` with explicit pointer and keyboard states |
| Optimize images in lists | Use Next `Image`, fixed dimensions, and responsive sizes |

## Where to apply in Next.js
- Client-heavy dashboards and feeds.
- Infinite-scroll/search-result pages.
- Motion-heavy marketing pages.
- Complex modal/drawer interactions rendered as client components.

## Validation hints
- Check React Profiler for list rerender churn.
- Check Lighthouse/INP regressions after interaction changes.
- Verify keyboard and pointer interactions remain equivalent.
