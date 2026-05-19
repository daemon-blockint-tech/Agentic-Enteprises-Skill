# Metrics and Experiments

## Monetization metric stack

| Layer | Examples |
|-------|----------|
| **Acquisition** | Signup, PQL, trial start |
| **Activation** | First value before paywall |
| **Conversion** | Free→paid, trial→paid, upgrade rate |
| **Expansion** | Seat growth, add-on attach, usage growth |
| **Retention** | Logo churn, revenue churn, downgrade rate |
| **Unit economics** | ARPU, ARPA, LTV:CAC (with finance) |

Define **one north star** per initiative (e.g. paid conversion, expansion ARPU).

## Funnel diagnostics

| Drop-off | Investigate |
|----------|-------------|
| Pricing page bounce | Positioning, anchor price, social proof |
| Checkout abandon | Payment methods, tax, surprise fees |
| Trial no convert | Time-to-value, paywall timing |
| Downgrade spike | Feature gap, competitor, budget season |

Instrument: page views, plan selection, checkout steps, entitlement changes.

## Experiment design

```markdown
## Experiment: [name]

**Hypothesis:** If we [change], then [metric] will [direction] because [reason].
**Segment:** [who]
**Variants:** Control vs treatment
**Primary metric:** …
**Guardrails:** churn, support volume, revenue per user
**Duration / sample:** power assumption
**Stop rules:** harm threshold on guardrail
**Ship criteria:** stat sig + practical significance
```

## Price testing constraints

- Legal: price discrimination rules by region
- Contract: grandfathered customers
- Sales: conflict with quoted enterprise deals
- Brand: public price transparency

Prefer **new cohorts** or **geographies** when full A/B on list price is blocked.

## Packaging experiments

- Add/remove fence on tier
- Bundle vs unbundle feature
- Trial length or credit card upfront
- Annual default vs monthly

## Reporting cadence

| Audience | Content |
|----------|---------|
| Product weekly | Funnel, experiment readouts |
| Leadership monthly | ARR bridges, conversion, expansion |
| Finance sync | Recognition flags, discount leakage |

## Anti-patterns

- Optimizing clicks without revenue outcome
- Ending tests early on novelty effect
- Shipping price change without finance model update
