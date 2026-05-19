# Flows and Interaction Specs

## Flow diagram minimum

For each journey:

| Element | Document |
|---------|----------|
| Actor | Role (user, admin, guest) |
| Entry | URL, notification, deep link |
| Steps | Screen or modal sequence |
| Decision | Branch conditions |
| Success | Observable outcome |
| Failure | Recoverable vs terminal |
| Exit | Where user lands next |

Use Mermaid `flowchart` or numbered steps—pick one per doc and stay consistent.

## Interaction spec per screen

```markdown
### Screen: Checkout — Payment

**Purpose:** Collect payment without losing cart context.

**Primary action:** Pay now (enabled when card valid + terms checked).

**States:** loading | empty cart redirect | validation error | processing | success | payment declined

**Validation:** Inline on blur for card fields; block submit until terms accepted.

**Focus:** First invalid field on submit failure; trap focus in modal if used.

**Undo:** Back returns to shipping; confirm if payment partially entered.

**Analytics:** checkout_payment_viewed, payment_submitted, payment_failed (reason code)
```

## Transition rules

| Pattern | Specify |
|---------|---------|
| Modal vs page | When each; dismiss behavior |
| Optimistic UI | Rollback on failure |
| Skeleton | Duration threshold before show |
| Sticky CTA | Scroll behavior on mobile |
| Multi-step | Progress indicator; save draft |

## Edge cases checklist

- Session timeout mid-flow
- Double submit
- Back button after partial save
- Permission change mid-flow
- Concurrent edit (another tab)
- Offline / slow network
- Empty search results
- Rate limit / quota exceeded

## Acceptance criteria template

```markdown
Given [context]
When [user action]
Then [system response]
And [focus/announcement if a11y-relevant]
```

## Pair with product-designer

- Wireframes or Figma frames are inputs—not substitutes for interaction rules
- Open UX questions flagged before `ui-software-engineer` builds production UI
