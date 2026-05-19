# Design Handoff

## Pre-build checklist

- [ ] Figma link + **version** pinned (or export date)
- [ ] Tokens documented (color, font, radius, shadow)
- [ ] Breakpoints listed (mobile, tablet, desktop)
- [ ] All states shown: hover, focus, disabled, error
- [ ] Copy final or flagged TBD
- [ ] Icons/assets export path (SVG preferred)
- [ ] Edge cases: long text, empty, max items

## Questions to resolve before coding

| Gap | Ask |
|---|---|
| Missing empty state | Design or use system pattern? |
| Truncation | Ellipsis vs wrap vs tooltip |
| Modal vs drawer | Breakpoint behavior |
| Form validation | Inline vs summary |

Route UX gaps to `product-designer`; do not invent major flows.

## Implementation order

1. Static layout + tokens (no data)
2. States with mock data
3. API wiring + loading/error/empty
4. A11y pass + keyboard
5. Visual QA vs Figma

## Anti-patterns

- Screenshot-to-code without token mapping
- Hardcoded pixels from inspect tool only
- Shipping without error/empty for lists and forms
