# Monetization Models

## Model comparison

| Model | Revenue profile | Product demands |
|-------|-----------------|-----------------|
| **Subscription** | Predictable MRR | Renewal value, churn fight |
| **Usage / consumption** | Scales with adoption | Meters, dashboards, alerts |
| **One-time / license** | Lumpy | Version upgrades, support entitlements |
| **Marketplace / take rate** | Network effects | Trust, payouts, dispute flows |
| **Freemium** | Conversion funnel | Clear free limits, upgrade hooks |
| **Hybrid** | Common in B2B SaaS | Base + metered overage |

## Hybrid pattern (common B2B)

```
Platform fee (seats or flat) + included quota + overage per unit
```

Specify in PRD:

- What resets monthly vs annual
- Overage price and caps
- Grace period before hard block

## Freemium design

| Element | Decision |
|---------|----------|
| Free limit | Usage, time, or feature cap |
| Upgrade CTA | In-context at limit hit |
| Watermark / branding | Optional viral tradeoff |
| Sales assist | When free user hits PQL threshold |

## Usage-based specifics

- **Meter definition**: billable event schema (idempotent, auditable)
- **Rating**: tiered blocks vs linear
- **Preview**: estimated bill in product UI
- **Alerts**: 50/80/100% thresholds

Pair with `product-management-human-data-platform` for labeling-volume pricing.

## Enterprise vs self-serve

| Dimension | Self-serve | Enterprise |
|-----------|------------|------------|
| Price | Public list | Custom quote |
| Contract | Click-through | MSA + order form |
| Provisioning | Instant | Manual or SCIM |
| Invoicing | Card | PO / invoice |

Product defines **entitlement parity** between channels where possible.

## Marketplace (if applicable)

- Take rate and payout timing
- Seller onboarding and KYC product requirements
- Dispute and refund split rules
- Search ranking and monetization conflict policies

## Model migration

When changing models (e.g. seat → usage):

- Customer impact segments
- Parallel run period
- Legacy plan sunset timeline
- Finance recognition impact → `senior-revenue-accountant`
