# Cloud cost to GL mapping

## Table of contents

1. [Data sources](#data-sources)
2. [Mapping dimensions](#mapping-dimensions)
3. [Prepaid and commitments](#prepaid-and-commitments)
4. [Credits and adjustments](#credits-and-adjustments)

## Data sources

| Source | Use |
|---|---|
| Billing invoice (PDF/API) | Cash, AP accrual, vendor subledger |
| Cost and Usage Report (CUR) / cost export | Granular allocation, COGS by product |
| Cost management UI | Sanity check, anomaly detection |
| Internal tag compliance report | Find untagged spend |

Reconcile **invoice total** to **sum of allocated CUR** ± timing (enterprise support, tax lines).

## Mapping dimensions

Build mapping rules in priority order:

1. **Account / subscription** — default GL by payer account
2. **Tag** — `cost_center`, `product`, `environment` (prod vs non-prod)
3. **Service / SKU** — e.g., EC2, GKE, Blob → natural account
4. **Resource group or project** — for committed structure

| Tag state | Fallback |
|---|---|
| Complete tags | Rule-based GL |
| Missing tags | Default “unallocated” + remediation owner |
| Shared platform | Allocation % from chargeback model |

**Prod vs non-prod** — separate R&D vs COGS where policy requires.

## Prepaid and commitments

| Instrument | Accounting pattern |
|---|---|
| All-upfront RI / prepaid | Debit prepaid asset; monthly amort to COGS/expense |
| Partial upfront | Split cash; amortize prepaid portion |
| Savings Plan / CUD benefit | Amortize commitment over term; true-up usage benefit |
| Short-term reservation (<12 mo) | May expense per policy — document |

Track **unamortized balance** monthly; tie to cloud console commitment reports.

## Credits and adjustments

- **Provider credits** — reduce expense or prepaid per nature (promo vs SLA credit)
- **Enterprise Discount Program** — allocate consistently with usage mapping
- **Refunds** — reverse AP and expense or adjust prepaid
- **FX** — invoice currency vs functional currency; document rate source

Log **non-recurring** items separately in flux commentary.
