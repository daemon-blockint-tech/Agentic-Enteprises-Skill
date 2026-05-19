# Investment Prioritization

## Initiative register fields

| Field | Purpose |
|---|---|
| ID | Stable reference |
| Name | Short title |
| Type | Build / expand / refresh / exit / efficiency / network |
| Region | |
| Capex / opex | $ and timing |
| Benefits | Capacity, risk, TCO, sustainability |
| Dependencies | Other initiatives |
| DRI | |
| Stage | Concept / approved / in flight / done |
| RAG | Red / amber / green |

## Scoring dimensions (customize weights)

| Dimension | Questions |
|---|---|
| **Strategic** | Supports core product/regulatory must-haves? |
| **Risk** | Avoids outage, single-site, or contract cliff? |
| **Financial** | NPV, payback, capex deferral value |
| **Time** | Hard deadline (lease end, product launch)? |
| **Unlock** | Enables other initiatives? |
| **Efficiency** | kW or capex avoided via consolidation |

Use weighted score; document **sensitivity** if weights disputed.

## Funding bands

| Band | Meaning |
|---|---|
| **Funded** | In approved capex plan |
| **Conditional** | Funded if dependency clears |
| **Pipeline** | Approved concept, not yet funded |
| **Deferred** | Valid but later year |
| **Rejected** | Kill with reason logged |

## Tradeoff narrative

Steering needs **explicit trades**, e.g.:

- "Defer Site B expansion to fund Site A GPU hall"
- "Accept cloud burst cost for 2 quarters vs early build"

## Business case rollup

Site leads provide TCO assumptions; portfolio lead:

- Normalizes horizon and discount assumptions
- Surfaces inconsistent utilizations across sites
- Totals portfolio capex and run-rate impact

Deep single-site engineering → `data-center-design-execution-lead`.
