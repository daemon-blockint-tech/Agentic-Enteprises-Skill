# Commitment portfolio economics

## Table of contents

1. [Instrument comparison](#instrument-comparison)
2. [Coverage and term](#coverage-and-term)
3. [Break-even math](#break-even-math)
4. [Portfolio view](#portfolio-view)
5. [EA negotiation inputs](#ea-negotiation-inputs)

## Instrument comparison

| Instrument | Flexibility | Typical discount | Risk if usage drops |
|---|---|---|---|
| On-demand | Highest | 0% baseline | None |
| Savings Plan / CUD | Medium (family/region) | Moderate | Unused commit $ |
| Standard RI / reserved | Lower | Higher | Resale/exchange friction |
| All-upfront / 3y | Lowest | Highest | Stranded commit |

Price **option value** of flexibility when usage is volatile.

## Coverage and term

Recommendations:

- Cover **steady baseline** (e.g., 60–80% of min monthly usage), not peak
- Shorter term when product/market uncertain; longer when stable 2+ years
- Mix instruments — do not put 100% in one SKU family
- Reconcile with `finops-analyst` utilization reports monthly

## Break-even math

Simplified:

```
monthly_savings = on_demand_cost × discount_rate
payback_months = upfront_payment / monthly_savings   (if applicable)
```

Include:

- **Amortization** of upfront vs monthly commit fee
- **Exchange/sell** fees if provider allows
- **Opportunity cost** of prepaid cash (discount rate)

If break-even > expected stable life of workload, reject commit.

## Portfolio view

At org level:

- Aggregate by **payer account**, region, instance family
- Avoid **double coverage** (RI + SP on same usage)
- Track **utilization %** of commit pool; target >85% on steady portfolio
- Model **drawdown** of EA commit balance vs on-demand overflow

## EA negotiation inputs

Provide finance and `enterprise-cloud-architect`:

- **Forecast** spend by year (low/base/high)
- **Mix** of services (compute vs data vs SaaS marketplace)
- **Walk-away** — discount at which on-demand + spot is acceptable
- **True-up risk** if under-commit
- **CPI/price increase** clauses sensitivity

Economist does not sign contracts — supplies scenarios.
