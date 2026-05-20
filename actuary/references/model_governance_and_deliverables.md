# Model governance and deliverables

## Table of contents

1. [Model inventory](#model-inventory)
2. [Validation lifecycle](#validation-lifecycle)
3. [Documentation standards](#documentation-standards)
4. [Actuarial memo structure](#actuarial-memo-structure)
5. [Sensitivity and reasonability](#sensitivity-and-reasonability)
6. [Version control and audit trail](#version-control-and-audit-trail)
7. [Model risk escalation](#model-risk-escalation)

## Model inventory

Maintain a register for each production model:

| Field | Example |
|---|---|
| Model ID | RES-GL-001 |
| Purpose | Quarterly GL incurred reserve |
| Owner | Actuarial team lead |
| Users | Reserving, finance, regulatory |
| Inputs | Claim bordereaux, prior factors |
| Output | Ultimate losses, IBNR by AY |
| Tier | 1 / 2 / 3 by materiality |
| Last validation | Date, outcome |

Separate **pricing**, **reserving**, **ALM**, and **capital** models; document dependencies when outputs feed each other.

## Validation lifecycle

```
design → implement → independent review → approval → monitor → change control
```

| Activity | Minimum evidence |
|---|---|
| Conceptual soundness | Method matches problem; literature or ASOP alignment |
| Implementation | Code review, parallel run vs prior tool |
| Outcome testing | Reasonability vs benchmarks, prior period |
| Ongoing monitoring | Backtesting, A/E on ultimates, drift alerts |
| Change | Ticket, impact assessment, re-validation scope |

Tier 1 models require **independent** validation (second actuary or model risk function).

## Documentation standards

Each model should have:

1. **Purpose and scope** — Decisions supported, exclusions
2. **Theory** — Formulas, assumptions, references
3. **Data** — Sources, transforms, quality checks
4. **Parameters** — Tables with version and effective date
5. **Output mapping** — How results post to finance or filings
6. **Limitations** — Known weaknesses and monitoring

Avoid orphan spreadsheets: named ranges, change log tab, locked production tabs.

## Actuarial memo structure

Recommended sections:

1. **Executive summary** — Conclusion, key numbers, recommended action
2. **Scope and data** — Period, entities, exclusions
3. **Methods** — With alternatives considered
4. **Results** — Exhibits, bridges, segment detail
5. **Sensitivities** — Key drivers table
6. **Assumptions** — Cross-reference assumption library
7. **Governance** — Preparer, reviewer, approver, dates
8. **Appendices** — Triangles, tables, technical detail

Write so a **non-actuary executive** understands the decision in page one; specialists use appendices.

## Sensitivity and reasonability

Standard sensitivity pack:

| Driver | Shocks (example) |
|---|---|
| Development factors | ± one age in tail |
| Expected loss ratio (BF) | ± 5% |
| Trend | ± 1 point |
| Large loss threshold | ± cap level |
| Mortality / morbidity | ± table scale |

Reasonability checks:

- Implied **ultimate LR** vs pricing indication
- **Calendar-year** loss vs plan
- **Industry** benchmarks (with caveats)
- **Cash flow** emergence vs paid pattern

## Version control and audit trail

Store:

- Data **cut timestamp** and query definition
- Model **semver** or build ID
- Parameter file hash
- Output file with **read-only** archive

Retention per company policy (often ≥ 7 years for statutory work).

## Model risk escalation

Escalate when:

- Material model change near **filing** deadline
- **Backtest** failure persists two quarters
- **Data quality** break affects key line
- **Undocumented** manual override in production
- **Conflict of interest** (same preparer prices and opines reserves without review)

Route to chief actuary, model risk committee, or audit as defined by policy.
