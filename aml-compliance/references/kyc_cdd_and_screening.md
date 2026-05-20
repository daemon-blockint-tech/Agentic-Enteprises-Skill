# KYC, CDD, and screening

## Table of contents

1. [Definitions](#definitions)
2. [Customer risk tiers](#customer-risk-tiers)
3. [CDD data elements](#cdd-data-elements)
4. [EDD triggers](#edd-triggers)
5. [Screening workflow](#screening-workflow)
6. [Beneficial ownership](#beneficial-ownership)
7. [Ongoing monitoring](#ongoing-monitoring)
8. [Quality and audit](#quality-and-audit)

## Definitions

| Term | Practical meaning |
|---|---|
| **KYC** | Know-your-customer process at onboarding and through lifecycle |
| **CDD** | Standard due diligence for most customers—identity, purpose, expected activity |
| **EDD** | Enhanced measures for higher risk—source of funds/wealth, senior approval, frequency |
| **PEP** | Politically exposed person per firm definition and regulator lists |
| **Sanctions** | Government restricted-party lists; blocking vs reporting regimes vary by license |

## Customer risk tiers

Typical tiering (calibrate to firm risk assessment):

| Tier | Profile examples | CDD depth |
|---|---|---|
| **Low** | Regulated retail, low-value accounts, domestic only | Simplified CDD where permitted |
| **Standard** | SME, payroll, everyday commercial | Full CDD |
| **High** | Cash-intensive, cross-border corridors, complex ownership | EDD |
| **Prohibited** | Sanctions match (true hit), illegal activity, policy exclusions | Do not onboard / exit |

Document **rationale** for tier assignment and **re-rating triggers** (volume spikes, adverse media, STR filing).

## CDD data elements

Collect and verify per policy (not every field for every tier):

- Legal name, aliases, date of birth or incorporation, jurisdiction
- Government ID or corporate registry references (where applicable)
- Address and contact; verify using independent sources where required
- Nature of business and **expected activity** (volume, products, counterparties)
- Source of funds / wealth for higher-risk relationships
- **Purpose** of account and anticipated transaction profile
- Related parties: signers, controllers, UBOs

Record **verification method** (documentary, non-documentary, reliable third party) and **date**.

## EDD triggers

Apply EDD when any trigger fires (examples—firm policy may expand):

- PEP or close associate (domestic or foreign)
- High-risk country or corridor per firm list
- Correspondent banking, nested accounts, payable-through
- Virtual asset service providers and unhosted wallet business models
- Adverse media indicating financial crime, fraud, or regulatory action
- Unusual ownership (shell layers, nominee directors, bearer shares where relevant)
- Prior SAR/STR, law enforcement inquiry, or account restriction history
- Material change in activity vs stated profile

EDD outputs: **source-of-funds/wealth narrative**, senior approval, **enhanced monitoring** frequency, shorter refresh.

## Screening workflow

```
onboarding / periodic / event-driven
  → run lists (sanctions, PEP, adverse media)
  → algorithmic matches + analyst review
  → disposition: false positive | true positive | inconclusive
  → document rationale + approver
  → update risk tier and monitoring
```

**Match disposition rules:**

- **False positive** — different person/entity; document distinguishing factors (DOB, ID, address)
- **True positive** — escalate per sanctions program; do not proceed without compliance/legal path
- **Inconclusive** — obtain additional data; freeze or restrict per policy pending resolution

Maintain **list version**, **screening timestamp**, and **analyst ID** in audit trail.

## Beneficial ownership

For legal entities, identify **ultimate beneficial owners** and control persons per jurisdictional thresholds (e.g., 25% ownership tests—confirm locally with counsel).

- Collect ownership chain for complex structures
- Identify **control** without ownership (directors, POA, trust protectors)
- Refresh on material ownership changes
- Reconcile UBO with screening results

## Ongoing monitoring

CDD is not onboarding-only:

| Activity | Cadence |
|---|---|
| **Periodic refresh** | By tier (e.g., 1–5 years) |
| **Event-driven** | Ownership change, new product, adverse media alert |
| **Transaction profile** | Compare actual vs expected; trigger EDD if divergence |
| **Screening rescreen** | On list updates and schedule per tier |

## Quality and audit

- **QC sample** of onboarding and dispositions with second-line review
- Metrics: time-to-complete, EDD backlog, false positive rate, true positive escalation time
- **Do not** delete screening hits; retain superseded dispositions with reason
- Align retention with `sar_str_reporting_and_records.md` and local law
