# Pricing and Packaging

## Value metric selection

| Value metric | Fits when | Watch |
|--------------|-----------|-------|
| Per seat | Collaboration, admin roles | Seat rot, sharing logins |
| Per usage | Variable consumption | Bill shock, unpredictable revenue |
| Per project/workspace | Isolated teams | Under-monetize power users |
| Per feature module | Clear upsell modules | Fragmentation |
| Flat platform fee | Simple buyer mental model | Leaves money on table |

Pick **one primary** value metric; secondary metrics for add-ons only.

## Packaging principles

| Principle | Application |
|-----------|-------------|
| Good-better-best | Three tiers max for self-serve |
| Fences | Limits that align with willingness to pay (API calls, history, SSO) |
| Land and expand | Low-friction entry; expansion in-product |
| No silent downgrade | Entitlements clear on renewal |

## Tier definition template

```markdown
## Plan: Pro

**Persona:** Team lead, 5–50 users
**Price:** $X / seat / month (annual -Y%)
**Core value:** [one sentence]

**Included:**
- …

**Limits:**
- …

**Not included (upgrade to Enterprise):**
- …

**Upgrade trigger:** Needs SSO, audit logs, >N seats
```

## Discount policy (product input)

| Type | Product role | Approval |
|------|--------------|----------|
| List price change | Propose with elasticity data | Finance + exec |
| Promotional % | Campaign brief | Marketing + finance |
| Enterprise custom | Requirements only | Deal desk |
| Credits / extensions | In-product grace | PM + finance threshold |

Product documents **eligibility rules**; deal desk executes custom deals.

## Competitive positioning

Use `business-model-researcher` for benchmarks; PM decides **position** (premium, parity, penetration).

Document:

- Reference competitors (public list prices only)
- Differentiation worth paying for
- Where you will **not** compete on price

## Price change communication

- Grandfather vs migrate: policy per segment
- Notice period (contract and regulatory minimums)
- In-product messaging and email templates (`communication-lead` if company-wide)

## Anti-patterns

- Feature parity across tiers with price-only difference
- Unlimited usage on usage-priced product without cost model
- Packaging driven by sales one-offs without platform abstraction
