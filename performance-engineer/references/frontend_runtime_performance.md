# Frontend and client runtime performance

## Table of contents

1. [Core Web Vitals](#core-web-vitals)
2. [Network and assets](#network-and-assets)
3. [Rendering](#rendering)
4. [Measurement](#measurement)
5. [Handoff to FE engineering](#handoff-to-fe-engineering)

## Core Web Vitals

| Metric | Focus |
|---|---|
| LCP | Largest paint — hero image, font, server TTFB |
| INP | Interaction responsiveness — long tasks, handlers |
| CLS | Layout shift — images without dimensions, dynamic inject |

Set **budgets** per template (e.g. LCP < 2.5s p75 field data).

## Network and assets

- Critical path: fewer serial requests, HTTP/2/3, preconnect
- **Bundle size** — code split, tree-shake, defer non-critical JS
- Images: modern formats, responsive `srcset`, lazy below fold
- Third-party scripts: audit cost; load after consent/interaction

Lab tools (Lighthouse) ≠ field RUM — track both.

## Rendering

- Avoid unnecessary re-renders (memoization with measurement)
- Virtualize long lists
- Prefer CSS over JS layout thrashing
- SSR/streaming: balance TTFB vs hydration cost (Next.js patterns)

Deep component implementation → `senior-frontend-software-engineer`.

## Measurement

- RUM: real users by device, region, connection
- Lab: CI Lighthouse or equivalent on representative pages
- **Filmstrip** and long-task attribution for INP fixes
- Compare **before/after** on same throttling profile

## Handoff to FE engineering

Performance engineer delivers:

- Ranked issues with **repro URL** and trace
- Suggested fix class (defer script, resize image, split route)
- Validated improvement in lab or staging

FE engineer owns merge, a11y regression check, and design alignment.
