# Prototypes in Code

## When to prototype in code vs design tool

| Situation | Prefer |
|-----------|--------|
| Validate layout and visual brand | Design tool (`product-designer`) |
| Validate timing, focus, keyboard, real data shapes | Code prototype |
| Stakeholder click-through for exec review | Design tool or low-code |
| Engineer handoff with real components | Code in app repo or Storybook |

## Fidelity levels

| Level | Goal | Timebox |
|-------|------|---------|
| **Lo-fi** | Flow order and labels | Hours |
| **Mid-fi** | Real components, fake data | 1–2 days |
| **Hi-fi** | Production stack, feature flag or branch | Sprint slice |

Do not hi-fi prototype what lo-fi can disprove.

## Stack choices (match the product)

- Reuse design system components when possible—prototypes should feel like shipping UI
- Mock API with fixtures; document which fields are fake
- Route behind feature flag or `/prototype/*` path; never ship prototype routes to prod without guard

## Validation loop

1. Write 3–5 **task scenarios** (no hints in UI copy)
2. Run with 3–5 users or internal proxies; record time and errors
3. Log **severity**: blocker / major / minor / cosmetic
4. Decide: iterate prototype, change spec, or escalate to `product-designer`

## Prototype hygiene

- Label prototype UI (“Preview”) if shown outside eng
- No real PII in fixtures
- Delete or gate dead prototype code after decision
- Link prototype PR to UX spec doc or ticket

## Handoff from prototype

| Artifact | To |
|----------|-----|
| Confirmed flow | `references/ux_engineering_handoff.md` |
| Component gaps | `ui-software-engineer` or design system backlog |
| New patterns | `product-designer` for system update |
