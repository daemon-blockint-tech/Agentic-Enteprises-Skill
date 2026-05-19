# UI Accessibility Basics

## Minimum bar (every PR)

- [ ] Interactive elements are **native or roled** correctly (`button`, `link`, `input`)
- [ ] Every input has **visible label** (`<label>` or `aria-label` if icon-only)
- [ ] **Focus order** follows visual order
- [ ] **Focus visible** on keyboard tab
- [ ] **Color contrast** meets WCAG AA for text and controls (use token pairs)
- [ ] Images/icons have **alt** or `aria-hidden` if decorative
- [ ] Modals trap focus and restore on close

## Keyboard

| Control | Expected |
|---|---|
| Button | Enter / Space activates |
| Link | Enter |
| Menu | Arrow keys if composite widget |
| Escape | Closes dialog/popover per spec |

## Do not

- `div onClick` without role and keyboard handler
- `outline: none` without replacement focus style
- Placeholder as sole label
- Disable zoom (`user-scalable=no`)

## When to involve senior FE

- Complex widgets (combobox, datagrid)
- Full page audit or WCAG sign-off
- See `senior-frontend-software-engineer` → `references/a11y_performance.md`

## Quick tests

1. Tab through feature without mouse
2. 200% browser zoom — no clipped controls
3. Screen reader spot-check on primary flow (optional but valuable)
