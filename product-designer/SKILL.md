---
name: product-designer
description: |
  Guides product design—problem framing, discovery synthesis, user journeys and flows, wireframes,
  interaction specs, usability evaluation, and engineering handoff for digital products (web and mobile).
  Use when designing a new feature UX, mapping flows, creating wireframe or spec narratives, running
  heuristic reviews, defining states and edge cases for UI, or preparing design-ready acceptance
  criteria—not for writing BRDs or business process docs (business-analyst), front-end implementation
  (senior-frontend-software-engineer, fullstack-software-engineer), or production code review
  (senior-software-engineer).   For UI implementation from specs (tokens, states, Storybook), use ui-software-engineer.
  For interaction specs, coded prototypes, and in-product UX audits, use ux-software-engineer.
  For human data / labeling platform PM (tasks, quality, workforce), use
  product-management-human-data-platform.
  For business model canvas, pricing research, and unit economics, use
  business-model-researcher.
---

# Product Designer

## When to Use

- Frame a user problem and success metrics before UI work
- Map journeys, task flows, and information architecture
- Specify screens, states (empty/error/loading), and interaction behavior
- Prepare handoff for engineering (annotated flows, acceptance notes)
- Critique existing UX with heuristics and prioritized fixes

## When NOT to Use

- Formal requirements documents and workshop facilitation → `business-analyst`
- React/Next implementation or component code → `senior-frontend-software-engineer`
- API/database design → `fullstack-software-engineer`
- Marketing copy or long-form docs → `tech-writer-researcher`
- Business model, TAM, competitor monetization → `business-model-researcher`

## Related skills

| Need | Skill |
|---|---|
| Requirements and user stories | `business-analyst` |
| Build UI from specs | `ui-software-engineer` |
| Flows, prototypes, UX fixes in product | `ux-software-engineer` |
| End-to-end delivery | `fullstack-software-engineer` |
| In-product help text | `tech-writer-researcher` |
| Canvas, market sizing, unit economics | `business-model-researcher` |

## Core Workflows

### 1. Discovery and framing

1. State user, job-to-be-done, and current pain
2. Define success metrics (task time, completion rate, support tickets)
3. List assumptions; note what to validate in research
4. Scope MVP vs later—explicit non-goals

**See `references/discovery_framing.md` for one-pager template.**

### 2. Flows and information architecture

```
entry points → primary path → branches → error recovery → exit/success
```

- One flow per user goal; avoid mixing admin and end-user paths
- Name screens consistently; show decision diamonds
- Call out permissions and role differences

**See `references/user_flows_journeys.md` for flow notation and IA checklist.**

### 3. Wireframes and interaction spec

For each screen document:

| Element | Spec |
|---|---|
| Purpose | What user accomplishes |
| Content | Headings, fields, primary data |
| Actions | Primary/secondary/destructive CTA |
| States | Default, empty, loading, error, partial |
| Responsive | Mobile vs desktop behavior |

Prefer low-fi structure first; visual polish after flow is stable.

**See `references/wireframes_specs.md` for screen spec template.**

### 4. Usability and accessibility (design)

- Apply Nielsen heuristics for review
- Plan keyboard path and focus order on critical flows
- Check contrast and touch targets against WCAG AA targets
- Do not treat design review as legal compliance sign-off

**See `references/usability_heuristics.md` for review worksheet.**

### 5. Engineering handoff

Deliver:

- Linked flows + screen specs
- Edge cases and validation messages
- Analytics events (name, trigger) if product uses them
- Open questions with owner

Align with `business-analyst` on acceptance criteria; with engineering on feasibility spike.

**See `references/design_handoff.md` for handoff checklist.**

### 6. Iteration after build

1. Compare built UI to spec; log gaps by severity
2. Verify states in staging (empty, error, long text)
3. Capture follow-ups as tracked design debt or v2

## When to load references

- **Problem framing** → `references/discovery_framing.md`
- **Flows and IA** → `references/user_flows_journeys.md`
- **Wireframes** → `references/wireframes_specs.md`
- **Heuristic review** → `references/usability_heuristics.md`
- **Handoff** → `references/design_handoff.md`
