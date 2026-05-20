# Executive economic briefings

## Table of contents

1. [One-pager structure](#one-pager-structure)
2. [ADR economic appendix](#adr-economic-appendix)
3. [CFO questions](#cfo-questions)
4. [Common pitfalls](#common-pitfalls)

## One-pager structure

1. **Decision** — what we are choosing (one sentence)
2. **Recommendation** — option B; NPV or 5y TCO delta vs A
3. **Why now** — trigger (migration, EA renewal, margin pressure)
4. **$ impact** — year 1 run-rate and 5y cumulative (range)
5. **Risks** — usage miss, lock-in, egress surprise, labor
6. **Next steps** — owners, dates, FinOps/eng actions

Use charts: cumulative TCO lines, tornado for top 3 drivers.

## ADR economic appendix

For `cloud-architect` ADRs attach:

| Section | Content |
|---|---|
| Options | 2–4 architectures considered |
| Cost model | 3y TCO table, same assumptions |
| Non-cost | security, latency, skills (qualitative) |
| Recommendation | $ and % difference vs baseline |

Keep technical ADR body with architect; economist appendix is optional attachment.

## CFO questions

Prepare answers:

- What is **run-rate** cloud COGS as % revenue?
- What happens to margin at **2× scale**?
- How much is **committed** vs flexible next 12 months?
- What is **true-up** exposure on EA?
- What is **cash** impact of upfront vs monthly commit?
- How do we **reconcile** model to GL? (`compute-accounting-manager`)

## Common pitfalls

- **Sunk cost fallacy** — past migration spend should not justify bad forward option
- **Ignoring labor** — managed service savings need net of reduced FTE or redeployment
- **Peak pricing** — modeling at max scale without probability
- **Discount double-count** — EA discount plus RI on same usage
- **Egress omission** — largest error in data-heavy migrations

Pair narrative with `business-consultant` only when decision is broader than cloud economics.
