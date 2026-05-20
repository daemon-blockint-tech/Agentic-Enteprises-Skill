# Crypto, travel rule, and exam readiness

## Table of contents

1. [Virtual asset AML touchpoints](#virtual-asset-aml-touchpoints)
2. [Blockchain analytics](#blockchain-analytics)
3. [Travel rule](#travel-rule)
4. [Correspondent and fiat ramps](#correspondent-and-fiat-ramps)
5. [Exam readiness](#exam-readiness)
6. [Request list preparation](#request-list-preparation)
7. [Common findings](#common-findings)

## Virtual asset AML touchpoints

Map activities to risk assessment:

| Activity | AML considerations |
|---|---|
| **Custody** | Customer identification, wallet ownership, withdrawal controls |
| **Exchange / broker** | KYC tiers, TM on trades and transfers, market manipulation adjacent risks |
| **Transfer** | Travel rule, unhosted wallet policies, address screening |
| **Staking / DeFi exposure** | Counterparty risk, smart contract commingling, disclosure |
| **NFT / high-risk tokens** | Fraud and sanctions exposure; listing policies |

Classify **VASPs** and non-custodial models per license; do not assume one control set fits all products.

## Blockchain analytics

Use on-chain tools as **decision support**, not sole proof:

| Use | Caveats |
|---|---|
| Address screening | Heuristic labels; false labels; freshness |
| Clustering | Attribution confidence varies by chain |
| Path tracing | Does not prove beneficial ownership |
| Risk scores | Vendor-specific; document methodology |

Workflow:

1. Document **why** analytics were pulled (alert, EDD, SAR support)
2. Capture **screenshot or export** with timestamp and tool version
3. State **confidence** and alternative explanations
4. Route law-enforcement-grade investigations to blockint skills

For sanctions checks on addresses, see `chainalysis-sanctions-screening` as engineering pointer; AML owns disposition.

## Travel rule

**FATF Travel Rule** — transmit originator/beneficiary information with virtual asset transfers between obliged entities.

Operational design elements:

| Element | Design question |
|---|---|
| **Counterparty VASP discovery** | How identify beneficiary exchange? |
| **Data elements** | Name, account, address per jurisdiction |
| **IVMS101 / protocols** | Travel Rule Protocol, OpenVASP, etc. |
| **Exceptions** | Unhosted wallets, below thresholds, unable to obtain data |
| **Hold / reject** | When to delay transfer pending data |
| **Recordkeeping** | Proof of send/receive of Travel Rule payload |

Document **sunrise** issues and corridor-specific gaps; escalate legal interpretation to counsel.

## Correspondent and fiat ramps

- **Fiat on/off ramps** — bank partners, MSB relationships, nested flows
- **Correspondent due diligence** — questionnaire, AML attestation, onsite/sampling for high risk
- **Payable-through accounts** — prohibited or heavily restricted in many programs
- **Wire due diligence** — OFAC and AML dual checks; originator/beneficiary fields

Align crypto flows with **traditional TM** where fiat touches the bank.

## Exam readiness

Maintain standing **exam packet** (refresh quarterly):

| Artifact | Notes |
|---|---|
| Board-approved AML policy | Version and approval date |
| Enterprise risk assessment | Latest approved |
| MLRO appointment | Letter or org chart |
| Organization chart | First/second/third line |
| Training logs | Completion by role |
| Independent test report | Issues and remediation status |
| TM scenario catalog | With last tuning summary |
| Sample alert dispositions | Redacted exemplars |
| SAR metrics | Counts, aging—no tipping off in walkthroughs |

Assign **exam coordinator**; single point for requests and legal privilege coordination.

## Request list preparation

When regulators or auditors request samples:

1. **Define population** — date range, business line, alert type
2. **Sample size** — per methodology (statistical or judgmental)
3. **Pull uniformly** — avoid cherry-picking
4. **Index files** — control ID, customer ID, disposition, approver
5. **Redact** — third-party PII; SAR confidentiality rules
6. **Walkthrough script** — who presents, system demo path, known limitations

For IT-dependent controls, involve `compliance-engineer` for log exports and system evidence.

## Common findings

Themes from AML examinations (illustrative):

| Finding | Preventive practice |
|---|---|
| Stale risk assessment | Annual refresh + trigger-based updates |
| Undocumented tuning | Change log with approvals |
| Weak EDD files | Source-of-wealth evidence checklist |
| Screening backlog | SLA monitoring and surge staffing |
| SAR narrative quality | Templates and QC review |
| Travel rule gaps | Exception register with remediation |
| Inadequate crypto policies | Product-specific annexes |
| First-line overrides without approval | Exception workflow with expiry |

Track findings in **issues register** with root cause and retest evidence.
