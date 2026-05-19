# Chargeback and showback

## Table of contents

1. [Showback vs chargeback](#showback-vs-chargeback)
2. [Allocation keys](#allocation-keys)
3. [Rate design](#rate-design)
4. [Governance](#governance)

## Showback vs chargeback

| Mode | GL impact | Purpose |
|---|---|---|
| **Showback** | No internal JE; reporting only | Transparency, behavior change |
| **Chargeback** | Intercompany or management JEs | Full cost recovery to consumers |

Pick mode per company policy and system capability (ERP intercompany modules).

## Allocation keys

For **shared** compute (K8s cluster, shared GPU pool, corporate networking):

| Key | Pros | Cons |
|---|---|---|
| CPU-hours / GPU-hours | Tied to usage | Requires metering |
| % of tagged cloud spend | Uses existing CUR | Tag quality dependent |
| Headcount or revenue | Simple | Weak causality |
| Fixed split by agreement | Stable | Can drift from usage |

Document **hierarchy**: direct tagged spend first → allocate remainder of shared pool.

## Rate design

Internal rates may include:

- **Variable** — per vCPU-hour, per GPU-hour, per GB-month
- **Fixed platform fee** — amortized platform engineering and shared tools
- **Pass-through** — reserved capacity at amortized cost + uplift (policy)

Refresh rates **quarterly** or when unit economics shift materially.

Reconcile **total charged** to **total compute GL expense** ± intentional subsidy (document executive approval).

## Governance

- Publish **dictionary** of cost pools and tags
- **Freeze** allocation rules before month-end close
- Escalate disputes to FinOps + accounting DRI
- Do not use chargeback to bypass capex approval for hardware purchases
