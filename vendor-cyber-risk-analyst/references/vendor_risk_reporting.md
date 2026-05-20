# Vendor risk reporting

## Table of contents

1. [Audience views](#audience-views)
2. [Report components](#report-components)
3. [Remediation tracking](#remediation-tracking)
4. [Metrics and KRIs](#metrics-and-kris)
5. [Integration with enterprise risk](#integration-with-enterprise-risk)
6. [Renewal pipeline](#renewal-pipeline)

## Audience views

| Audience | Emphasis |
|---|---|
| Procurement / vendor management | Tier distribution, renewals due, approval blockers |
| Security leadership | Top T1 risks, incidents, concentration, remediation aging |
| Executive / board (via CISO) | Material third-party cyber themes, not every vendor row |
| Audit / GRC | Sample of assessments, evidence retention, cadence adherence |

Align board narrative with `chief-information-security-officer`; this skill supplies **vendor portfolio substance**.

## Report components

Standard periodic pack:

1. **Portfolio summary** — count by tier, new onboardings, offboardings
2. **Heat map** — top vendors by residual cyber risk (not only tier)
3. **Open findings** — by severity, age, owner
4. **Incidents** — vendor-related events in period
5. **Concentration** — thematic exposures (IdP, cloud, email, backup)
6. **Renewals** — next 90 days with assessment status
7. **Exceptions** — time-bound accepts with approver and expiry

Keep **risk analysis** separate from **compliance attestation** status (`compliance-specialist`).

## Remediation tracking

| Field | Purpose |
|---|---|
| Finding ID | Stable reference |
| Vendor / product | Scope |
| Severity | Critical / High / Medium / Low |
| Theme | Control area |
| Remediation type | Vendor fix, internal compensating, contract, exit |
| Owner | Vendor manager + security SME |
| Due date | Contract or policy driven |
| Status | Open / in progress / verified / accepted |
| Re-test | Evidence required to close |

Accepted risks require **approver**, **expiry**, and **compensating controls**; sync material items to `security-risk-analyst` register.

## Metrics and KRIs

Examples (tune to program maturity):

- % T1 vendors with current SOC 2 Type II or ISO
- Mean days to complete T1 assessment from intake
- Open critical findings > 90 days
- Vendor incidents per quarter
- Renewals proceeding without completed assessment (should trend to zero)
- Concentration index (optional): % critical workloads on top N vendors

## Integration with enterprise risk

- Map **material vendor scenarios** to enterprise register rows (single source of truth for treatment)
- Provide **inherent vendor risk** and **residual** after internal compensating controls
- Do not duplicate FAIR quantification unless `security-risk-analyst` leads modeling

## Renewal pipeline

Run renewal queue:

| Horizon | Action |
|---|---|
| 90 days | Schedule assessment, request updated attestations |
| 60 days | Complete questionnaire review |
| 30 days | Remediation closure or exception approval for go/no-go |
| At renewal | Archive prior assessment; attach new evidence package |

Procurement should not sign T1 renewals without security **go** or documented exception per policy.
