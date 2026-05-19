# Microcopy and Content UX

## Scope

In-product strings UX engineers own or review:

- Buttons and links
- Form labels and hints
- Validation and API errors
- Empty states
- Toasts and banners
- Confirm dialogs
- Onboarding steps

Public marketing and legal copy → `tech-writer-researcher` / legal.

## Principles

| Principle | Practice |
|-----------|----------|
| Specific | "Enter a date after today" not "Invalid input" |
| Action-oriented | Button = verb + object ("Save draft") |
| Human | No internal codes in user-facing text |
| Consistent | Same term for same concept app-wide |
| Calm errors | What happened + what to do next |

## Error message formula

```
[What happened] + [Why if helpful] + [Next step]
```

Examples:

- Bad: `Error 422`
- Good: `That email is already registered. Sign in or reset your password.`

## Empty states

Include:

1. Why it's empty (first use vs filtered out)
2. Primary action to fix
3. Secondary learn-more if complex

## Confirm dialogs

| Destructive? | Pattern |
|--------------|---------|
| Low | Undo toast preferred |
| Medium | Confirm with clear object name |
| High | Type-to-confirm or second step |

Title = consequence; body = what cannot be undone.

## Tone matrix (adjust per brand)

| Context | Tone |
|---------|------|
| Success | Brief, positive |
| Error | Neutral, helpful |
| Billing | Precise, no jokes |
| Security | Serious, no blame |

## Review checklist

- [ ] Jargon and acronyms defined or removed
- [ ] Title case consistent per design system
- [ ] Punctuation consistent (periods in sentences, not in labels)
- [ ] Numbers and units localized if product is i18n
- [ ] Screen reader: errors associated with fields (`aria-describedby`)

## Handoff

- Copy in table: `key | en | context | max length`
- Flag strings that need truncation rules in UI
- Pair with `ui-software-engineer` for overflow in components
