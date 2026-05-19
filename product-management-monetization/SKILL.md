---
name: product-management-monetization
description: |
  Guides product management for monetization—pricing and packaging, plan tiers, usage meters,
  paywalls and upgrade paths, free-to-paid conversion, expansion revenue features, monetization
  experiments, and PRDs for billing-adjacent product surfaces. Covers success metrics (conversion,
  ARPU, NRR drivers) and finance alignment on recognition implications—not GAAP revenue accounting
  (senior-revenue-accountant), billing ops and dunning (customer-ops-specialist), market sizing
  and canvas research (business-model-researcher), deal desk order forms (deal-operations-administrator),
  or payment integration code (fullstack-software-engineer). Paywall UX: product-designer.
---

# Product Management — Monetization

## When to Use

- Define **pricing strategy**, packaging, and plan differentiation
- Write **PRDs** for checkout, upgrades, usage limits, entitlements, or billing settings
- Design **paywall and upgrade** journeys (what to gate, when, and why)
- Plan **monetization experiments** (price tests, packaging, trial length)
- Specify **usage meters** and fair-use policies for usage-based models
- Improve **expansion** paths (seats, add-ons, consumption tiers)
- Set **monetization metrics** and dashboards for product decisions
- Align with **finance/legal** on list price, discounts, and recognition flags

## When NOT to Use

- ASC 606, deferred revenue schedules, audit → `senior-revenue-accountant`
- Support refunds, dunning, subscription ops → `customer-ops-specialist`
- TAM/SAM, competitor monetization research only → `business-model-researcher`
- CPQ, order forms, signature routing → `deal-operations-administrator`
- Stripe/webhook implementation → `fullstack-software-engineer`
- Visual-only paywall mockups → `product-designer`

## Related skills

| Need | Skill |
|---|---|
| Business model and unit economics research | `business-model-researcher` |
| Requirements docs without monetization lens | `business-analyst` |
| Checkout and settings UX | `product-designer` |
| Post-sale billing operations | `customer-ops-specialist` |
| Enterprise order execution | `deal-operations-administrator` |
| Human-data usage pricing | `product-management-human-data-platform` |

## Core Workflows

### 1. Pricing and packaging

Value metrics, tiers, fences.

**See `references/pricing_packaging.md`.**

### 2. Monetization model selection

Subscription, usage, hybrid, marketplace.

**See `references/monetization_models.md`.**

### 3. Metrics and experiments

North star, test design, guardrails.

**See `references/metrics_experiments.md`.**

### 4. Paywalls and conversion

Gating, trials, upgrade triggers.

**See `references/paywall_conversion.md`.**

### 5. Billing platform requirements

Entitlements, meters, proration rules.

**See `references/billing_platform_requirements.md`.**

### 6. Launch and governance

Rollout, comms, price change policy.

**See `references/launch_governance.md`.**

## Output standards

- Every monetization change states **target segment and metric**
- Experiments have **hypothesis, guardrails, and stop rules**
- Packaging maps **features → plans** with clear upgrade path
- Flag **recognition/billing** dependencies for finance before GA
- No list price commitments in PRD without deal desk/finance sign-off

## When to load references

- **Pricing** → `references/pricing_packaging.md`
- **Models** → `references/monetization_models.md`
- **Experiments** → `references/metrics_experiments.md`
- **Paywall** → `references/paywall_conversion.md`
- **Billing** → `references/billing_platform_requirements.md`
- **Launch** → `references/launch_governance.md`
