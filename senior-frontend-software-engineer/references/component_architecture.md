# Component architecture

## Table of contents

1. [Composition](#composition)
2. [Server vs client](#server-vs-client)
3. [Anti-patterns](#anti-patterns)

## Composition

- Prefer compound components (`Tabs`, `Tabs.List`, `Tabs.Panel`) for flexible UIs
- Container/presentational split when data loading differs from display
- Extract after second duplication, not before

## Server vs client

| Use Server Component | Use Client Component |
|---|---|
| Read data, static layout | Clicks, forms, browser APIs |
| SEO-critical content | Charts, maps, rich editors |

Mark client files with `"use client"` at top; keep boundary as low as possible.

## Anti-patterns

- God components >300 lines without extraction plan
- `useEffect` for data that could load on server
- Copy-paste variants instead of props/variants
- Inline styles for design-system-covered tokens
