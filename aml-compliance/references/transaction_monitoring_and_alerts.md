# Transaction monitoring and alerts

## Table of contents

1. [TM program components](#tm-program-components)
2. [Scenario design](#scenario-design)
3. [Thresholds and tuning](#thresholds-and-tuning)
4. [Alert triage](#alert-triage)
5. [Investigation playbook](#investigation-playbook)
6. [Typologies](#typologies)
7. [Metrics and governance](#metrics-and-governance)
8. [Model validation touchpoints](#model-validation-touchpoints)

## TM program components

| Component | Role |
|---|---|
| **Data** | Core banking, payments, cards, crypto ledgers, KYC attributes, watchlists |
| **Rules / models** | Scenarios, aggregation logic, anomaly detection, network analytics |
| **Case management** | Alert queues, notes, attachments, approvals, audit trail |
| **Reporting** | Management MI, regulatory metrics, tuning change log |

Separate **AML TM** from **fraud** or **credit** systems where possible; if shared, tag alert type and route to trained analysts.

## Scenario design

Each scenario should document:

| Field | Description |
|---|---|
| Scenario ID | Stable identifier |
| Typology | Structuring, rapid movement, high-risk geography, etc. |
| Risk linkage | RA reference |
| Data sources | Tables, fields, latency |
| Logic | Plain-language rule; version |
| Thresholds | Parameters with effective dates |
| Disposition codes | Closed: benign / escalated / SAR referral |

Cover **onboarding** (misuse of product), **ongoing** activity, and **exit** (draining accounts).

## Thresholds and tuning

Govern tuning as a **controlled change**:

1. **Hypothesis** — why change (typology shift, false positive burden, new product)
2. **Analysis** — historical alert population, SAR yield, sample review
3. **Approval** — AML compliance + second-line sign-off; MLRO for material shifts
4. **Implementation** — versioned deploy; back-test where feasible
5. **Post-change review** — alert volume, quality, SAR outcomes at 30/90 days

Avoid silent threshold edits in production without documentation.

## Alert triage

Queue design principles:

- **Priority** — high-risk customer, large amount, sanctions proximity, law enforcement flags
- **SLA** — time to first touch and to disposition by severity
- **Skill-based routing** — complex correspondent vs retail
- **Escalation** — team lead → AML compliance → MLRO

Triage checklist (first 15 minutes):

- Confirm customer identity and tier
- Validate alert fired correctly (not data defect)
- Compare to **expected activity** profile
- Check open cases and recent screening hits
- Decide: close with rationale | investigate further | escalate

## Investigation playbook

Deeper investigation steps:

1. **Activity chart** — credits/debits over review window; counterparties
2. **KYC refresh** — still accurate? trigger EDD?
3. **Screening** — rescreen if stale or new names appear
4. **External research** — adverse media (licensed tools); document sources
5. **Customer outreach** — if policy allows; document questions and responses
6. **Conclusion** — reasonable explanation vs unexplained; recommend SAR referral or not
7. **Supervisor review** — mandatory for closures above materiality or SAR paths

Attach **supporting extracts** (redacted) to case; never paste full SAR drafts into general tickets.

## Typologies

Reference typologies (not exhaustive):

| Typology | Indicators |
|---|---|
| **Structuring** | Amounts just below reporting thresholds; smurfing patterns |
| **Rapid movement** | Pass-through; layering across accounts |
| **High-risk geography** | Corridors inconsistent with profile |
| **Trade-based ML** | Invoice anomalies, over/under shipping (if applicable) |
| **Mule activity** | New account, immediate dispersal, many small beneficiaries |
| **Crypto-specific** | Peel chains, mixer proximity, exchange hops (heuristic) |

Pair typologies with **red flags** list in investigation notes; distinguish facts from inference.

## Metrics and governance

| Metric | Use |
|---|---|
| Alerts per analyst / month | Capacity planning |
| False positive rate | Tuning input (define consistently) |
| SAR conversion rate | Scenario effectiveness (interpret carefully) |
| Aging backlog | Operational risk |
| Escalation rate | Training needs |
| Repeat alerts same customer | Profile or scenario gap |

Review metrics in **AML committee** with first-line and MLRO.

## Model validation touchpoints

When TM uses **machine learning or scoring models**:

- Document model purpose, features, training data, and known bias
- Independent validation: conceptual soundness, outcomes analysis, ongoing monitoring
- Define **override** policy and logging
- Align with firm model risk policy; separate from IT change management

Validation is **conceptual structure** here—specialist model risk teams may own execution.
