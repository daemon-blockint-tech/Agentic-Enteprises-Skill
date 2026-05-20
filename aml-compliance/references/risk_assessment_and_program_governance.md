# Risk assessment and program governance

## Table of contents

1. [Enterprise AML risk assessment](#enterprise-aml-risk-assessment)
2. [Risk factors](#risk-factors)
3. [Control mapping](#control-mapping)
4. [MLRO and second line](#mlro-and-second-line)
5. [Board reporting](#board-reporting)
6. [Framework orientation](#framework-orientation)
7. [Training and culture](#training-and-culture)
8. [Independent testing](#independent-testing)

## Enterprise AML risk assessment

Purpose: identify **inherent risk**, evaluate **controls**, and document **residual risk** with board-approved appetite.

**Steps:**

1. **Scope** — entities, licenses, products, channels, geographies, customer segments
2. **Inherent risk** — score or rank each cell (customer × product × channel × geography)
3. **Controls** — map preventive/detective controls; rate design and operating effectiveness
4. **Residual risk** — inherent minus control mitigation; flag above appetite
5. **Action plan** — owners, dates, evidence for remediation
6. **Approval** — MLRO and board (or delegated committee) with date
7. **Refresh** — annual minimum; triggers on new product, M&A, exam findings, enforcement trends

Store methodology, data sources, assumptions, and dissenting views.

## Risk factors

| Category | Examples |
|---|---|
| **Customer** | PEPs, MSBs, NGOs, shell companies, VASPs, correspondent banks |
| **Product** | Cash, wires, cross-border, private banking, trade finance, crypto |
| **Channel** | Non-face-to-face, agents, third-party introducers, API onboarding |
| **Geography** | FATF high-risk jurisdictions, sanctions programs, weak AML regimes |
| **Delivery** | Speed, anonymity features, nested relationships, omnibus accounts |

Weight factors per firm strategy; avoid copy-paste scores without business context.

## Control mapping

For each material risk, document:

| Field | Content |
|---|---|
| Control ID | Unique identifier |
| Control type | Preventive / detective / corrective |
| Owner | First-line role |
| Evidence | Reports, logs, approvals |
| Frequency | Continuous / monthly / annual |
| Effectiveness | Design OK? Operating OK? Last test date |

Gaps become **issues** with severity, compensating controls, and target dates.

## MLRO and second line

**Money Laundering Reporting Officer** (or equivalent):

- Owns AML/CFT program oversight and regulatory liaison
- Reviews escalations, SAR/STR decisions (with counsel where required)
- Approves high-risk relationships and policy exceptions
- Reports to board; ensures resources for compliance

**Second line** (AML compliance function):

- Sets standards, monitors first-line execution, challenges risk ratings
- Performs thematic reviews and quality assurance on investigations
- Manages regulatory change horizon scanning (facts to counsel for interpretation)

**First line** — business units own customers and day-to-day CDD/TM execution.

**Third line** — internal audit independent assurance (`auditor`).

## Board reporting

Typical MLRO pack (quarterly or per charter):

| Section | Contents |
|---|---|
| **Risk posture** | Summary of RA, top residual risks, appetite breaches |
| **Metrics** | Alerts per FTE, SAR filings, onboarding times, QC results |
| **Issues** | Open exam findings, independent test gaps, enforcement themes |
| **Emerging risks** | New products, corridors, typologies from FATF/FIU |
| **Resources** | Staffing, tooling, budget asks |

Use trends, not point-in-time vanity metrics; explain **false positive** burden and tuning actions.

## Framework orientation

High-level mapping only—confirm obligations with counsel:

| Framework | Orientation |
|---|---|
| **FATF 40 Recommendations** | International baseline; RBA, DNFBPs, wire transfers, PEPs, reporting |
| **BSA / USA PATRIOT (U.S.)** | CIP, CDD rule, SAR, CTR concepts, OFAC, beneficial ownership (CDD rule) |
| **EU AMLD / AMLA** | Harmonized EU requirements; authority structure evolving under AMLA |
| **UK MLR** | JMLSG guidance context; MLR obligations for relevant firms |

Use `fatf-glossary-reference` for standardized terms—not as legal advice.

## Training and culture

- **Role-based** training: front office, ops, TM analysts, executives, board
- **Frequency** — annual minimum; refresh on material policy change
- **Attestation** — completion tracked; exceptions escalated
- **Speak-up** — escalation paths without retaliation; document referrals to compliance

## Independent testing

Scope second-line or external testers to evaluate:

- RA reasonableness and refresh
- CDD/EDD sample quality
- Screening disposition accuracy
- TM scenario coverage and tuning governance
- SAR decision documentation (redacted samples)
- Training completion and issue management

Findings rated by severity with management responses and retest dates.
