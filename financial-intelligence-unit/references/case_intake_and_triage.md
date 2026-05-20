# Case intake and triage

## Table of contents

1. [Sources and queues](#sources-and-queues)
2. [Minimum data checklist](#minimum-data-checklist)
3. [Prioritization](#prioritization)
4. [Routing and assignment](#routing-and-assignment)
5. [Disposition at triage](#disposition-at-triage)
6. [SLA and backlog](#sla-and-backlog)

## Sources and queues

| Source | Typical handling |
|---|---|
| **Transaction monitoring** | Primary volume; tie to scenario ID and threshold breach |
| **Manual referral** | Branch, RM, fraud, security; require referrer ID and reason code |
| **Periodic / event-driven review** | EDD refresh, profile change, geolocation shift |
| **External request** | Law enforcement, regulator, partner bank—escalate per policy immediately |
| **Ad hoc** | Executive or audit sample—document sponsor and scope |

Maintain **separate queues** where regulations or licensing differ (entity, product, corridor). Do not commingle jurisdictions without explicit analyst training.

## Minimum data checklist

Before opening a full investigation, confirm:

- Customer ID, legal entity, and **CDD tier** snapshot
- Alert or referral **reference**, date range, and scenario/rule name
- **Account(s)** and instrument(s) in scope
- **Amounts** and currencies (normalized to reporting currency where used)
- Prior **alerts and dispositions** on same subject (lookback per policy)
- **Sanctions / PEP** status at triage (true match vs false positive disposition)

If gaps exist, set status **Pending data** with owner and due date—do not investigate on incomplete KYC without documented exception approval.

## Prioritization

Use a **scoring model** aligned to policy, for example:

| Factor | Weighting guidance |
|---|---|
| Amount or velocity | Higher notional or rapid movement increases score |
| High-risk geography / corridor | Elevate per risk assessment |
| PEP / sanctions touchpoint | Elevate; may mandate immediate senior review |
| Repeat subject | Prior STR consideration or open case increases score |
| Scenario severity | Critical scenarios (e.g., known typology) override FIFO |
| SLA proximity | Time-to-breach boosts queue position |

Document **priority override** with approver when analysts reprioritize outside the model.

## Routing and assignment

- **Skill-based routing**: complex trade finance, crypto, correspondent, or corporate structures
- **Capacity balancing**: cap WIP per analyst; supervisor rebalances daily
- **Conflict check**: analyst must not investigate own onboarding or overrides they performed
- **Escalation path**: team lead → FIU manager → MLRO for threshold breaches

## Disposition at triage

| Code | When to use |
|---|---|
| **Close – no investigation** | Obvious false positive with documented reason (e.g., payroll pattern explained) |
| **Close – duplicate** | Same underlying activity as open or recently closed case |
| **Investigate** | Minimum data met; typology or risk warrants analysis |
| **Refer – fraud** | Primary loss or account takeover indicators |
| **Refer – security** | Cyber or internal theft indicators |
| **Refer – CFT** | TF/PF-specific indicators without broader ML case |
| **Pending data** | Hold with tracker until KYC/TM data retrieved |

All dispositions require **actor, timestamp, and free-text rationale** retrievable for audit.

## SLA and backlog

- Define **SLA** by priority tier (e.g., P1 24h, P2 72h, P3 10 business days)—adjust to license and risk appetite
- Report **aging buckets** (0–3d, 4–7d, 8–14d, 15+d) in daily stand-up
- Escalate **breaches** with root cause: volume, staffing, data latency, rework
- Cap **reopen rate** tracking—frequent reopens signal triage or QA issues

Feed **false positive** closures back to TM with structured fields (scenario, reason code, sample tx IDs) for tuning governance.
