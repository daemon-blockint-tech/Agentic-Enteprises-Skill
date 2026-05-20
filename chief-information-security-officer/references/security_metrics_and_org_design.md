# Security metrics and org design

## Table of contents

1. [Metrics framework](#metrics-framework)
2. [Sample KRIs](#sample-kris)
3. [Budget envelope](#budget-envelope)
4. [Org design](#org-design)
5. [Vendors and insurance](#vendors-and-insurance)

## Metrics framework

| Layer | Purpose | Audience |
|---|---|---|
| KRIs | Early warning of rising risk | Board, audit committee, CISO |
| Program KPIs | Initiative delivery | CISO, direct reports |
| Operational metrics | SOC/engineering tuning | Security leadership only |

Review quarterly: retire metrics that do not drive decisions; add metrics linked to appetite thresholds.

## Sample KRIs

Tailor to industry and tech stack:

| KRI | Notes |
|---|---|
| % critical assets with EDR coverage | Coverage gaps = appetite breach |
| Mean time to contain (SEV-1/2) | Trend vs prior year |
| Internet-facing critical vulns > SLA | Link to appetite |
| MFA coverage (workforce + privileged) | Split metrics |
| Phishing simulation failure rate | Training effectiveness |
| Third-party critical findings open | Vendor tier 1 only |
| Backup success / restore test pass rate | Resilience |
| Security awareness completion | Supporting, not sufficient alone |

Pair each red KRI with **one accountable owner** and **corrective plan** in board pack.

## Budget envelope

Typical security opex categories:

- Personnel (FTE, contractors)
- Tools (SIEM, EDR, IAM, GRC, scanning)
- MSSP / MDR
- Training and certifications
- Assessments (pentest, red team, audits)
- Insurance premiums

Build **3-year phased plan** aligned to roadmap; show deferral risk for unfunded initiatives.

Coordinate with `vp-of-infrastructure` when security spend sits inside broader infra budget.

## Org design

Sizing considerations:

| Driver | Implication |
|---|---|
| Regulated industry | Higher GRC and audit liaison FTE |
| Global footprint | Follow-the-sun SOC or MSSP |
| Heavy engineering | AppSec and security engineering embedded |
| M&A velocity | Integration and IAM surge capacity |

Define spans: CISO → (Engineering, GRC, SOC/IR, IAM program lead). Avoid combining CISO and CIO without explicit board mandate.

## Vendors and insurance

**Critical vendors:** tier by data access and blast radius; exec review annually for tier 1.

**Cyber insurance:** align limits to scenario modeling (ransomware, notification costs, legal); review annually with broker; document exclusions.

CISO approves **material security contracts**; engineering evaluates technical fit.
