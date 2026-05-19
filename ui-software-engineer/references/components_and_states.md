# Components and States

## Presentational vs container

| Type | Responsibility |
|---|---|
| **Presentational** | Props in, markup + styles; no fetch |
| **Container** | Data fetch, maps to presentational |

Keep presentational components in Storybook without API mocks when possible.

## Variants

Use design-system API (`variant`, `size`) — do not fork CSS per screen.

```text
<Button variant="primary" size="md" disabled={isSubmitting} />
```

## State matrix (minimum per interactive surface)

| State | UI |
|---|---|
| Default | Spec styling |
| Hover / active | Per design system |
| Focus | Visible ring (never remove) |
| Disabled | Reduced opacity + no pointer |
| Loading | Spinner or skeleton; disable submit |
| Error | Message + field highlight |
| Empty | Illustration/copy + CTA if spec'd |

## Composition

- Prefer **small composable** pieces over 500-line page files
- Extract when used **twice** or spec defines reusable pattern
- Page = layout + sections; section = heading + content slot

## When to escalate

- New primitive not in design system → `senior-frontend-software-engineer` + design
- Cross-route state architecture → senior FE, not one-off context soup
