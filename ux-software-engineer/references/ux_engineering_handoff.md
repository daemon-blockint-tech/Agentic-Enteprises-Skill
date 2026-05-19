# UX Engineering Handoff

## Handoff chain

```
product-designer (discovery, wireframes)
        ↓
ux-software-engineer (flows, interaction, prototype validation)
        ↓
ui-software-engineer (visual production, tokens, component polish)
        ↓
senior-frontend-software-engineer (perf, a11y depth, arch) when needed
```

## Minimum handoff package

| # | Item |
|---|------|
| 1 | User story + persona |
| 2 | Flow diagram with branches |
| 3 | Per-screen interaction spec (see `flows_interaction_specs.md`) |
| 4 | State matrix (loading, empty, error, success) |
| 5 | Copy doc or inline strings for microcopy |
| 6 | Open questions / assumptions |
| 7 | UX acceptance criteria |
| 8 | Analytics events |
| 9 | Out of scope |
| 10 | Figma or prototype link |

## State matrix template

| State | Trigger | UI | User can |
|-------|---------|-----|----------|
| Initial | Page load | Skeleton | Wait |
| Ready | Data loaded | Form | Edit |
| Submitting | Click save | Disabled + spinner | Wait |
| Success | 200 | Toast + next | Continue |
| Error | 4xx/5xx | Inline + retry | Fix or retry |

## What ui-software-engineer needs from you

- **Behavior** frozen; visual can follow design system
- Component **variants** named (e.g. `destructive`, `compact`)
- **Spacing intent** if not in system (e.g. "dense table")
- Do not assign hex values if tokens exist—reference token names

## What you need from ui-software-engineer

- Storybook links for built states
- Gaps filed when design system cannot express spec

## Review gates

| Gate | Participants | Pass criteria |
|------|--------------|---------------|
| Spec review | PM, design, eng lead | No open P0 questions |
| Prototype | PM, 2 users | Tasks complete without hint |
| Staging UX | UX + QA | Acceptance criteria green |
| Launch | PM | Metrics instrumented |

## Ticket splitting

| Ticket type | Owner skill |
|-------------|-------------|
| Flow / interaction bug | ux-software-engineer spec → eng |
| Visual polish | ui-software-engineer |
| Copy only | ux + tech-writer if public |
| A11y violation | senior-frontend-software-engineer |

## Anti-patterns

- Screenshot-only tickets without expected behavior
- "Make it like [competitor]" without task context
- Mixing UX spec changes into unrelated refactors
