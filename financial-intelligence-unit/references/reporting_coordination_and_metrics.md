# Reporting, coordination, and metrics

## Table of contents

1. [Internal management information](#internal-management-information)
2. [Metrics catalog](#metrics-catalog)
3. [Coordination with transaction monitoring](#coordination-with-transaction-monitoring)
4. [Coordination with compliance and investigations](#coordination-with-compliance-and-investigations)
5. [Regulatory reporting support](#regulatory-reporting-support)
6. [Training and handover](#training-and-handover)
7. [Dashboard cadence](#dashboard-cadence)

## Internal management information

FIU MI supports **MLRO, COO, and risk committees**—not external filing.

| Report | Audience | Typical contents |
|---|---|---|
| **Operations dashboard** | FIU manager | Volumes, backlog, SLA, staffing |
| **Outcome summary** | MLRO | Escalations, closures, STR-path counts |
| **Typology trends** | Risk / TM | Top scenarios, emerging patterns |
| **Quality scorecard** | FIU + QA lead | Defect rates, rework, thematic findings |

State **limitations**: data lag, definition changes, and one-off events affecting trends.

## Metrics catalog

| Metric | Definition notes |
|---|---|
| **Alert / case volume** | By source, entity, product, scenario |
| **Aging** | Days open from triage or assignment; bucketed |
| **SLA adherence** | % closed within tier target |
| **Analyst productivity** | Cases closed per FTE (normalize for complexity) |
| **Escalation rate** | % to MLRO; % STR-path |
| **Rework rate** | QA failures / cases reviewed |
| **False positive feedback** | Closed at triage or post-investigation with TM reason codes |
| **Repeat subjects** | Customers with N cases in rolling window |
| **Typology distribution** | Primary typology tag at closure |

Avoid **single-metric incentives** that encourage premature closure; pair productivity with quality scores.

## Coordination with transaction monitoring

Structured feedback loop:

1. **Tuning requests** — scenario ID, sample case IDs, proposed change, expected impact
2. **False positive reviews** — monthly joint session with documented outcomes
3. **New product / corridor** — FIU input on typologies before go-live (`aml-compliance` owns risk sign-off)
4. **Model validation support** — labeled outcomes for back-testing where governance requires

Log TM changes with **version, approver, and effective date**—FIU references version in cases affected.

## Coordination with compliance and investigations

| Partner | FIU role |
|---|---|
| **Second-line AML compliance** | Policy interpretation requests; thematic reviews; issue tracking |
| **Fraud operations** | Referrals with handoff template; avoid duplicate interviews |
| **Security / cyber** | Account takeover vs ML distinction |
| **Legal / counsel** | Fact packs only; no filing strategy from FIU |
| **CFT specialists** | TF/PF cases → `aml-cft` collaboration on same case ID |

Use **shared case IDs** or links across systems; never parallel undocumented investigations on same subject.

## Regulatory reporting support

FIU may assemble **factual extracts** for MLRO or regulatory requests:

- Aggregate STR counts (internal)
- **Trend narratives** on typologies (non-legal)
- **Population descriptions** for statistical reporting

**Do not**:

- Advise whether a filing is legally required
- Draft final regulator submissions without MLRO/counsel
- Replace `str-report` for narrative assembly

Coordinate **exam requests** with `aml-compliance` and `auditor`—FIU provides case samples and QA evidence.

## Training and handover

| Activity | Purpose |
|---|---|
| **Playbook updates** | Capture QA themes and new typologies |
| **Case studies** | Anonymized closed cases for induction |
| **Shadowing** | New analysts on live queues with reviewer |
| **Shift handover** | Open P1/P2 cases, breaches, LE-sensitive items |
| **Lessons learned** | Post-incident or post-exam findings |

Track training completion in HR/LMS where required; link to **competency matrix** (retail vs corporate vs crypto).

## Dashboard cadence

| Cadence | Forum |
|---|---|
| Daily | Stand-up: backlog, breaches, LE items |
| Weekly | TM feedback; staffing |
| Monthly | MI to MLRO; QA scorecard |
| Quarterly | Thematic review; playbook refresh |

Archive dashboards with **definitions** so period-over-period comparisons remain valid.
