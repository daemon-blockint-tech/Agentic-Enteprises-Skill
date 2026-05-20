---
name: senior-frontend-software-engineer
description: |
  Guides senior front-end software engineering—TypeScript/React/Next.js architecture, component design,
  client and server rendering, state and data fetching, styling and design systems, accessibility (WCAG),
  performance (Core Web Vitals), testing, and senior-level UI code review.
  Use when building or refactoring complex UIs, designing component APIs, optimizing LCP/INP/CLS,
  implementing accessible interactions, integrating design tokens, or reviewing front-end PRs—not for
  backend APIs or databases (fullstack-software-engineer, senior-fullstack-developer), design-only
  critiques without implementation, CI/CD (devops), or cross-service system RFCs (senior-software-engineer).
  For implementing screens from design specs, component states, and visual QA, use ui-software-engineer.
  Deep perf investigations and load/RUM analysis: performance-engineer.
---

# Senior Front End Software Engineer

## When to Use

- Complex React/Next.js features, layouts, or design-system components
- Front-end architecture decisions (state, composition, RSC vs client)
- Performance work: bundle size, waterfalls, Core Web Vitals
- Accessibility fixes and WCAG-oriented implementation
- Senior front-end PR review (correctness, a11y, maintainability)

## When NOT to Use

- End-to-end feature needing new API and schema → `fullstack-software-engineer` or `senior-fullstack-developer`
- Pure visual/design direction without code → design review workflows
- Infrastructure, deploy, or monitoring setup → `devops`
- Multi-service backend design → `senior-software-engineer`

## Related skills

| Need | Skill |
|---|---|
| Full-stack slice (API + UI) | `fullstack-software-engineer`, `senior-fullstack-developer` |
| Cross-cutting engineering design | `senior-software-engineer` |
| Docs and UI copy in product docs | `tech-writer-researcher` |
| Pipeline and preview deploys | `devops` |
| UX flows and design specs | `product-designer` |
| UI implementation from specs | `ui-software-engineer` |
| RUM/load investigation and perf reports | `performance-engineer` |
| Browser auth, CSRF, CORS, session cookies | `web-application-developer` |
| Authorized web/API security testing context | `web-pentester` |

## Core Workflows

### 1. Component and feature design

1. Map user flows to routes and layout boundaries
2. Split **server** (data fetch, static) vs **client** (interaction) deliberately
3. Define component API: props, slots, variants, controlled vs uncontrolled
4. Plan states: loading, empty, error, partial success
5. Align with design tokens; avoid one-off magic values

**See `references/component_architecture.md` for composition patterns.**

### 2. State and data fetching

| Need | Prefer |
|---|---|
| Server data | RSC fetch, Server Actions for mutations |
| Client cache | TanStack Query or similar with stale times |
| URL state | Search params for shareable filters |
| Global UI | Minimal context; colocate state |

Avoid prop drilling through deep trees—compose or use context at stable boundaries.

**See `references/state_data_fetching.md` for waterfalls and cache invalidation.**

### 3. Styling and design system

- Use design tokens (spacing, color, typography) from system
- Variants via `cva` or equivalent; document in Storybook if present
- Responsive and dark mode from tokens, not duplicated rules
- Do not fork components without team agreement

**See `references/design_system.md` for extension rules.**

### 4. Accessibility and quality

- Semantic HTML first; ARIA only when needed
- Keyboard: focus order, focus visible, escape to close
- Labels on every input; announce dynamic updates thoughtfully
- Target WCAG 2.1 AA for customer-facing flows

**See `references/a11y_performance.md` for checklist and metrics.**

### 5. Performance

- Measure before optimizing (Lighthouse, Web Vitals, bundle analyzer)
- Fix waterfalls: parallelize fetches, hoist server data
- Code-split routes and heavy widgets
- Images: dimensions, modern formats, priority for LCP

**See `references/a11y_performance.md` for INP and CLS tactics.**

### 6. Testing and review

| Layer | Focus |
|---|---|
| Unit | Hooks, formatters, reducers |
| Component | React Testing Library—behavior not implementation |
| E2E | Critical journeys only |

**PR review:** a11y, edge states, unnecessary client boundaries, bundle impact, test gaps.

**See `references/frontend_code_review.md` for review rubric.**

## When to load references

- **Components and composition** → `references/component_architecture.md`
- **State and fetching** → `references/state_data_fetching.md`
- **Design system** → `references/design_system.md`
- **A11y and performance** → `references/a11y_performance.md`
- **Code review** → `references/frontend_code_review.md`
