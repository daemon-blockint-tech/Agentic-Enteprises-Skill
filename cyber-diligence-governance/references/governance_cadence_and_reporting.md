# Governance cadence and reporting

## Table of contents

1. [Governance forums](#governance-forums)
2. [Standing agenda themes](#standing-agenda-themes)
3. [Metrics and KRIs](#metrics-and-kris)
4. [IC and board packs](#ic-and-board-packs)
5. [Exception and risk acceptance](#exception-and-risk-acceptance)
6. [Coordination with CISO and risk analyst](#coordination-with-ciso-and-risk-analyst)

## Governance forums

| Forum | Typical cadence | Primary audience |
|---|---|---|
| Security steering | Monthly | CISO, IT, engineering leads |
| Risk committee | Quarterly | Risk, legal, business owners |
| Deal / investment committee | Per transaction | Corp dev, finance, exec sponsors |
| Board / audit committee | Quarterly | Directors, audit committee |

This skill drafts **content** for these forums; `chief-information-security-officer` owns executive operating model and board relationship norms.

## Standing agenda themes

Rotate focus to avoid static status slides:

1. **Posture snapshot** — top strengths and gaps vs prior quarter
2. **Diligence pipeline** — active M&A, major vendor assessments, status
3. **Incidents and near-misses** — material events, lessons, open actions
4. **Program progress** — remediation burndown, audit themes (high level)
5. **Third-party risk** — tier changes, concentration, expired certs
6. **Integration** — post-close backlog health (Day 30/90)
7. **Decisions needed** — exceptions, funding, policy exceptions

Keep **compliance attestation** narrative separate from **risk and diligence** narrative to avoid conflating audit readiness with deal risk.

## Metrics and KRIs

Examples (tailor to organization):

| Metric | Use |
|---|---|
| Critical vendor assessments current | % within policy cadence |
| Open critical findings (diligence) | Count and age |
| Mean time to remediate diligence gaps | Post-close or vendor conditions |
| Questionnaire cycle time | Operational efficiency |
| Incidents with third-party root cause | TPRM signal |
| Admin MFA coverage | Integration / hygiene |

Pair activity metrics with **outcome** metrics where possible. Detailed KRI design → `security-risk-analyst` and `chief-information-security-officer`.

## IC and board packs

Structure for deal or standing cyber brief:

1. **Executive summary** (≤1 page) — decision or ask
2. **Context** — deal/vendor/target, scope, access limitations
3. **Top findings** (3–7) — severity, evidence, business impact
4. **Red flags** — show-stoppers vs manageable gaps
5. **Remediation / integration** — cost, timeline, owners
6. **Recommendations** — proceed, conditions, pause, further diligence
7. **Appendix** — request tracker, detailed register (optional)

Use consistent **severity labels** across diligence and governance (see `references/red_flags_and_remediation.md`).

Avoid jargon walls; define acronyms once. Do not include **privileged** legal analysis without counsel review.

## Exception and risk acceptance

For governance-approved exceptions (tooling, architecture, vendor):

| Field | Required |
|---|---|
| Exception ID | Stable identifier |
| Description | What is excepted and why |
| Owner | Business and technical |
| Expiry | Maximum 12 months unless re-approved |
| Compensating controls | Documented |
| Approver | Per policy (CISO, risk committee) |

Expired exceptions surface as **standing agenda** items. Transfer standing risks to `security-risk-analyst` register.

## Coordination with CISO and risk analyst

| Need | Skill |
|---|---|
| Board operating model, risk appetite, crisis comms | `chief-information-security-officer` |
| Risk register rows, scoring methodology, treatment | `security-risk-analyst` |
| Audit program, control attestation | `compliance-specialist` |
| Deal process and timeline | `transaction-manager` |

Cyber diligence lead **feeds** risk analyst and CISO with transaction-specific findings; does not duplicate enterprise-wide register maintenance unless chartered.
