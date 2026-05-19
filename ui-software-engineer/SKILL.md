---
name: ui-software-engineer
description: |
  Guides UI software engineering—implementing screens and components from design specs, design tokens,
  responsive layout, interaction states, forms, and API-boundary loading/error UI in React/Next.js or
  similar stacks. Covers component library usage, basic WCAG implementation, and visual QA—not for
  senior front-end architecture or Core Web Vitals programs (senior-frontend-software-engineer),
  web auth/CORS/session security (web-application-developer), UX discovery without code
  (product-designer), interaction specs and coded prototypes (ux-software-engineer), or backend
  APIs and schemas (fullstack-software-engineer).
---

# UI Software Engineer

## When to Use

- Implement **screens and components** from Figma or design specs
- Apply **design tokens** (color, type, spacing) and design-system primitives
- Build **states**: default, hover, focus, disabled, loading, empty, error
- Wire **read-only or form UI** to existing APIs (loading, success, validation display)
- Fix **layout and responsive** breakpoints per spec
- Add **basic accessibility**: labels, focus order, keyboard activation
- Create **Storybook** (or equivalent) stories for components
- Run **visual QA** against design before PR

## When NOT to Use

- Front-end architecture, RSC strategy, bundle/CWV optimization → `senior-frontend-software-engineer`
- Login, cookies, CSRF, CORS, CSP → `web-application-developer`
- Wireframes, user research, design critique only → `product-designer`
- Flow specs, heuristic audits, prototypes before visual build → `ux-software-engineer`
- New REST API, database, or full vertical feature → `fullstack-software-engineer`
- Deploy pipelines → `devops`

## Related skills

| Need | Skill |
|---|---|
| Senior FE review, performance, complex arch | `senior-frontend-software-engineer` |
| Browser security and session flows | `web-application-developer` |
| Design specs and flows | `product-designer` |
| Interaction specs and UX validation | `ux-software-engineer` |
| API + persistence + UI slice | `fullstack-software-engineer` |

## Core Workflows

### 1. Design handoff to code

Spec checklist, tokens, assets, unknowns.

**See `references/design_handoff.md`.**

### 2. Components and states

Presentational vs container, variants, composition.

**See `references/components_and_states.md`.**

### 3. Layout and tokens

Grid, spacing, typography, responsive rules.

**See `references/layout_tokens.md`.**

### 4. API boundary in UI

Fetch hooks, skeletons, errors, empty states.

**See `references/ui_data_states.md`.**

### 5. Accessibility basics

Labels, contrast, keyboard, focus visible.

**See `references/ui_a11y_basics.md`.**

### 6. Stories and visual QA

Storybook, screenshot compare, PR checklist.

**See `references/stories_visual_qa.md`.**

## Output standards

- Match **design tokens** — no magic hex outside token map
- Every interactive control has **visible focus** and **accessible name**
- **Loading / empty / error** implemented for async views
- PR includes screenshots or Storybook link for changed UI
- Escalate spec gaps to `product-designer` before guessing layout

## When to load references

- **Handoff** → `references/design_handoff.md`
- **Components** → `references/components_and_states.md`
- **Layout** → `references/layout_tokens.md`
- **Data UI** → `references/ui_data_states.md`
- **A11y** → `references/ui_a11y_basics.md`
- **QA** → `references/stories_visual_qa.md`
