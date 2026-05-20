# Reporting, governance, and exam readiness

## Table of contents

1. [CFT governance](#cft-governance)
2. [STR/SAR narratives for TF](#strsar-narratives-for-tf)
3. [Internal escalation](#internal-escalation)
4. [Training](#training)
5. [Independent review](#independent-review)
6. [Exam readiness](#exam-readiness)
7. [Board and MLRO reporting](#board-and-mlro-reporting)
8. [Limitations](#limitations)

## CFT governance

| Element | Purpose |
|---|---|
| CFT/PF policy | TF/PF scope, roles, TFS, NPO, MVTS, escalation |
| Risk assessment | Document TF/PF inherent and residual risk |
| Procedures | Playbooks by typology; freeze; NPO tiers |
| Three lines | Business owns customers; compliance oversees; audit assures |
| Sanctions committee | Complex matches, licenses, de-risking (optional) |

Align policy cross-references to **FATF R6–R8** without duplicating full AML program text in `aml-compliance`.

## STR/SAR narratives for TF

Provide **fact packs** and narrative **structure**—not legal filing decisions.

### Suggested narrative sections

1. **Subject** — customer name, type (NPO, MVTS, individual), account IDs, relationship length
2. **Summary** — why TF is suspected in one paragraph (purpose-focused)
3. **Activity** — dates, amounts, channels, counterparties, instruments
4. **TF indicators** — typology match (charitable front, MVTS, self-funding, etc.)
5. **Sanctions** — any TFS matches, freezes, or related designations
6. **Open-source / intel** — vetted only; cite sources; note confidence
7. **Prior filings** — reference earlier SAR/STR if continuing activity
8. **Action taken** — freeze, account closure, law enforcement contact (if any)

### TF-specific facts to include

- Links to **high-risk geographies** or conflict zones
- **NPO** program inconsistency (collections vs distributions)
- **Beneficiary** patterns suggesting network support
- **Donor** anonymity or straw senders
- **Trade** or MVTS path if used for value transfer

**Do not** include privileged legal analysis or speculate on criminal charges.

## Internal escalation

```text
Analyst → Team lead → AML/CFT compliance → MLRO → Counsel (as needed)
                              │
                              └── Freeze / hold (parallel on TFS)
```

| Trigger | Escalation |
|---|---|
| Confirmed sanctions match | Immediate freeze + sanctions team |
| TF typology strong match | Senior compliance within SLA |
| Law enforcement inquiry | MLRO + counsel |
| Media / designation event | Relationship review + rescreen |

Maintain **confidentiality** and tipping-off awareness per jurisdiction.

## Training

| Audience | Topics |
|---|---|
| Front office | TF red flags, NPO basics, sanctions escalation |
| Payments / wire | MVTS, cross-border, incomplete wire data |
| Trade finance | PF dual-use introduction, document red flags |
| Crypto desk | Sanctions, heuristic analytics limits |
| Board / exec | CFT risk appetite, de-risking, major incidents |

Annual refresh plus **triggered** training after exam findings or typology advisories.

## Independent review

Scope examples for second-line or third-line review:

- Sample of **sanctions** true-match dispositions and timeliness
- **NPO** high-risk files for due diligence completeness
- **MVTS** agent oversight files
- **CFT** alert closure quality vs typologies
- **TFS** freeze and unfreeze approvals
- **Training** completion rates

Distinguish **AML independent test** (broad) from **CFT-focused** sample—can be a workstream under `aml-compliance` testing.

## Exam readiness

Prepare **TF/PF-specific** request lists:

| Artifact | Examiner interest |
|---|---|
| CFT/PF risk assessment | Methodology, approvals, refresh |
| TFS policy and procedures | Freeze, rejection, reporting |
| NPO procedure | Tiering, EDD, de-risking |
| MVTS oversight | Agent audits, licensing |
| Sanctions tuning | False positive management |
| Sample cases | TF investigations, freezes |
| Training logs | Role-based completion |
| Independent review | Findings and remediation |

**Walkthrough tips:** show typology-to-scenario mapping; demonstrate freeze hold on test case; explain NPO risk-based approach vs blanket exit.

Coordinate with `auditor` for ITGC and access evidence; with `aml-compliance` for enterprise AML program artifacts.

## Board and MLRO reporting

Periodic pack elements (examples):

- CFT/PF **KRI** trends (sanctions hits, NPO exits, MVTS incidents)
- **Geographic** and product exposure changes
- **Regulatory** and FATF mutual evaluation themes (high level)
- **Remediation** status on CFT findings
- **Resource** asks (staffing, tooling)

No legal conclusions in board materials—state facts and management actions.

## Limitations

- Filing thresholds and formats are jurisdiction-specific—MLRO/counsel decides
- Do not draft law enforcement subpoena responses without counsel
- Exam answers are factual; defer legal interpretations to compliance/legal
- This skill does not replace `aml-compliance` enterprise exam prep
