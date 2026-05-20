# Governance, documentation, and change control

## Table of contents

1. [Roles and ownership](#roles-and-ownership)
2. [Approval tiers](#approval-tiers)
3. [Assumption register](#assumption-register)
4. [Change control](#change-control)
5. [Documentation standards](#documentation-standards)
6. [Audit trail and retention](#audit-trail-and-retention)

## Roles and ownership

| Role | Typical responsibilities |
|---|---|
| **Assumption owner** | Maintains driver; proposes updates; sources data |
| **Model owner** | Ensures pack compatibility with model version |
| **Reviewer** | Independent challenge (material packs) |
| **Approver** | Sign-off per tiering policy |
| **Model risk / validation** | Second-line review for critical models |

RACI should be explicit for **material** assumption changes affecting published metrics.

## Approval tiers

Example tiering (adapt to company policy):

| Tier | Criteria | Approval |
|---|---|---|
| 1 | Immaterial; within pre-approved band | Owner only |
| 2 | Material single driver | Owner + reviewer |
| 3 | Pack restructure, new product, regulatory | Approver + model risk |
| 4 | Cross-model economic assumptions | ALM + actuarial committee |

Define **materiality** thresholds (e.g., % impact on reserves, capital, or indicated rate).

## Assumption register

Central register fields (minimum):

```
ID | Name | Category | Value | Unit | Basis | Source | Owner | Effective | Status | Model(s)
```

Statuses: `draft` → `pending approval` → `approved` → `superseded`

Link register rows to:

- Experience study ID
- Assumption paper section
- Model input file / worksheet cell range (if applicable)

## Change control

For each change request:

1. **Description** — Driver, segment, old vs new value
2. **Rationale** — Study, benchmark, judgment memo
3. **Impact** — Quantified where possible (reserve, LR, SCR proxy)
4. **Dependencies** — Other assumptions or models affected
5. **Effective date** — Valuation date or rate filing date
6. **Rollback** — Prior version retained in pack history

Emergency changes (e.g., post-catastrophe) still require **retrospective** documentation within policy SLA.

## Documentation standards

### Assumption paper (outline)

1. Executive summary (what changed, why now)
2. Scope (models, segments, dates)
3. Summary table: prior vs proposed vs approved
4. Evidence (A/E, benchmarks, sensitivities)
5. Judgment sections (if any)
6. Governance sign-offs
7. Appendices (tables, curves, study excerpts)

### Pack manifest

- Pack name and version
- Compatible model versions
- File list with checksums or repo tags
- Known limitations

Align narrative with **model risk** policy language; do not claim regulatory filing adequacy.

## Audit trail and retention

Retain for reproducibility:

- Approved pack snapshot
- Input data cuts (with PII handling per policy)
- Change tickets and approver identity
- Model run logs referencing pack version

Retention period → company records policy; flag **legal hold** when litigation or exam is active.

Coordinate **SOX** or ITGC evidence with `compliance-engineer` only when controls are technical; financial control testing → finance skills.
