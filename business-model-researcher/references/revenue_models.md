# Revenue models

## Table of contents

1. [Model catalog](#model-catalog)
2. [Selection criteria](#selection-criteria)
3. [Packaging patterns](#packaging-patterns)
4. [Hybrid models](#hybrid-models)

## Model catalog

| Model | Mechanism | Fits when | Watch-outs |
|---|---|---|---|
| **Subscription** | Recurring fee for access | Predictable value, ongoing delivery | Churn, expansion needed |
| **Usage / consumption** | Pay per unit (API call, GB) | Value scales with use | Revenue volatility, billing complexity |
| **Freemium → paid** | Free tier + conversion | PLG, viral loops | Free tier cost, conversion rate |
| **License (perpetual)** | One-time + maintenance | On-prem, regulated buyers | Renewal, version pressure |
| **Marketplace take rate** | % of GMV | Network effects, liquidity | Chicken-and-egg, disintermediation |
| **Transaction fee** | Per payment or trade | Fintech, commerce | Regulation, fraud cost |
| **Advertising** | Attention monetization | Scale audience, low CAC content | Privacy, platform risk |
| **Services / professional** | Time and materials | Complex implementation | Margin cap, not scalable |
| **Outcome-based** | Pay for result | Clear measurable ROI | Attribution disputes |

## Selection criteria

Score each option (1–5) against:

- **Willingness to pay** for target segment (interviews, WTP surveys, competitor price)
- **Cost to serve** per unit (support, infra, fraud)
- **Predictability** of revenue (finance and planning)
- **Alignment** with delivery (usage price needs metering)
- **Competitive norm** in category (deviation needs story)

## Packaging patterns

| Pattern | Example |
|---|---|
| Good-better-best tiers | Feature gates + seat limits |
| Seat-based | Per user/month |
| Usage + platform fee | Minimum commit + overage |
| Land-expand | Low entry SKU + expansion SKUs |

Document **expansion path** (what drives NDR).

## Hybrid models

Common combos:

- Sub + usage overage (SaaS infra)
- Take rate + subscription (marketplaces)
- Hardware + subscription (IoT)

Split economics per stream in unit model; avoid double-counting revenue.
