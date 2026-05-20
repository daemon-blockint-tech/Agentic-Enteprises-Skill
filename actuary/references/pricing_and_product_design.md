# Pricing and product design

## Table of contents

1. [Pricing workflow](#pricing-workflow)
2. [Segmentation](#segmentation)
3. [Loss and benefit costs](#loss-and-benefit-costs)
4. [Loadings](#loadings)
5. [Product design tradeoffs](#product-design-tradeoffs)
6. [Metrics and monitoring](#metrics-and-monitoring)
7. [Common pitfalls](#common-pitfalls)

## Pricing workflow

```
define coverage → segment risks → estimate pure premium → add loadings → compare to current → document
```

| Step | Output |
|---|---|
| Coverage definition | Benefit schedule, limits, deductibles, exclusions |
| Cost estimation | Pure premium or tabular cost by segment |
| Loadings | Expense, profit, risk margin, catastrophe |
| Indication | Indicated rate level or premium |
| Implementation | Filing constraints, phase-in, class plan |

## Segmentation

**Credible segments** have enough exposure to estimate frequency and severity (or tabular rates) with acceptable error.

| Technique | When to use |
|---|---|
| GLM / GAM | P&C frequency/severity with rating factors |
| Life tables | Age/gender/smoker bands with volume |
| Manual rates | Thin lines, regulatory filings |
| Pooling | Small segments combined with credibility weights |

Document **minimum volume rules** and off-book segments sent to manual review.

## Loss and benefit costs

### P&C

- **Frequency × severity** on earned exposure (or policy count for some lines)
- Trend selections: loss trend, exposure trend, social inflation where relevant
- **Large loss** caps or separate modeling for property cat

### Life / health

- **Tabular** costs from mortality/morbidity tables adjusted for underwriting class
- **Benefit duration** and utilization for health products
- **Lapse** impact on persistency and unit costs

### Annuity

- **Longevity** and **withdrawal** behavior; guarantee cost via stochastic or scenario set (overview)

## Loadings

| Loading | Typical components |
|---|---|
| Expense | Acquisition, maintenance, overhead allocation |
| Profit | Target underwriting or ROE constraint |
| Risk margin | Parameter risk, model risk, tail |
| Catastrophe | Cat model output or load table by zone |
| Reinsurance | Ceded premium and recoverable economics |

Show **indicated loss ratio** before and after loadings:

```
indicated LR = pure premium / gross premium (excl. reinsurance ceded, per convention)
```

State convention explicitly in the memo.

## Product design tradeoffs

| Lever | Actuarial effect |
|---|---|
| Higher deductible | Lower frequency, adverse selection risk |
| Broader coverage | Higher severity tail |
| Guaranteed renewability | Morbidity anti-selection in health |
| Riders | Marginal cost vs cross-subsidy |
| Index-linked benefits | Inflation and basis risk |

Present **option sets** with expected LR, volume elasticity assumptions (if provided), and capital sensitivity qualitatively.

## Metrics and monitoring

| Metric | Definition (typical) |
|---|---|
| Loss ratio | Incurred losses / earned premium |
| Combined ratio | (Losses + expenses) / earned premium |
| Expense ratio | Underwriting expenses / written or earned premium |
| Rate adequacy | Indicated vs achieved premium |

Set **monitoring triggers** post-launch: A/E by cohort, mix shift, large loss emergence.

## Common pitfalls

- Using **written** premium with **incurred** losses without earning adjustment
- Ignoring **claim reporting lag** in experience picks for pricing
- **Double-counting** reinsurance or subrogation
- **Stale** trend factors after macro shocks
- Pricing to **competitor** without reconciling own experience
