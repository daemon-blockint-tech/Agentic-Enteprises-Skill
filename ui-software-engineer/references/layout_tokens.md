# Layout and Tokens

## Token usage

| Category | Use token | Avoid |
|---|---|---|
| Color | `text-primary`, `bg-surface` | Raw `#hex` in components |
| Space | `spacing-4`, gap utilities | Random `margin: 13px` |
| Type | `text-body-sm`, font families | Inline `font-size: 14.5px` |
| Radius | `rounded-md` | Per-component border-radius |

If token missing, add to design system — do not local-patch unless emergency.

## Responsive

| Approach | When |
|---|---|
| Mobile-first CSS | Default stack |
| Breakpoint prefixes | `md:`, `lg:` per spec |
| Container queries | Card grids in variable widths |

Match **Figma frames** to breakpoints explicitly in PR notes.

## Layout patterns

- **Stack**: vertical rhythm with consistent gap token
- **Grid**: columns defined at breakpoint; avoid fixed px widths
- **Sticky header/footer**: test with keyboard scroll and zoom 200%

## Content stress

- Long titles: truncate + `title` tooltip if spec allows
- RTL/i18n: avoid hardcoded `ml-`; use logical properties (`ms-`, `me-`) when project supports

## Visual polish (IC scope)

- Align to **4px or 8px grid** per system
- Icon size paired with text line-height
- Deep CWV work → `senior-frontend-software-engineer`
