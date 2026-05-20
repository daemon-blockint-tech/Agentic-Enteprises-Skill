# Applying CISSP to organizational programs

## Table of contents

1. [From CBK to operating model](#from-cbk-to-operating-model)
2. [Framework alignment](#framework-alignment)
3. [Policy and governance cadence](#policy-and-governance-cadence)
4. [Study and exam prep workflow](#study-and-exam-prep-workflow)
5. [Manager vs technician in practice](#manager-vs-technician-in-practice)
6. [Deliverable templates](#deliverable-templates)

## From CBK to operating model

Map CBK domains to **functions** your organization actually runs:

| CBK domain | Typical organizational home |
|---|---|
| 1 | GRC, risk, executive steering |
| 2 | Data governance, privacy office |
| 3–4 | Architecture, network, cloud platform |
| 5 | IAM / IT |
| 6 | GRC, internal audit, AppSec |
| 7 | SOC, IR, IT operations |
| 8 | Engineering, AppSec, platform |

Produce a **single-page domain RACI** so initiatives do not duplicate ownership.

## Framework alignment

Use frameworks as **structured control sets**, not as substitutes for risk thinking.

| Framework | CISSP-relevant use |
|---|---|
| NIST CSF 2.0 | Govern, Identify, Protect, Detect, Respond, Recover — executive storytelling |
| NIST SP 800-53 | Control catalog for federal/high-assurance systems |
| ISO/IEC 27001 | ISMS, Annex A for certification scope |
| COBIT | IT governance alignment with business goals |
| CIS Controls | Prioritized implementation groups |

**Mapping practice**: For each in-scope control, document objective, implementing control, owner, evidence, and CBK domain(s). Deep GRC execution: `compliance-specialist`.

## Policy and governance cadence

| Cadence | Activities |
|---|---|
| Annual | Policy review, risk assessment refresh, awareness plan |
| Quarterly | KPI/KRI review, exception register, vendor tier reviews |
| Monthly | Vulnerability SLA, incident trends, project security gates |
| Ad hoc | Major change, M&A, new regulation, material incident |

**Exception process**: Requestor, risk assessment, approver authority, expiry, compensating controls—CISSP designs the process; GRC tracks.

## Study and exam prep workflow

Educational workflow only—verify all requirements with official (ISC)² resources.

1. **Baseline** — self-assess each of eight domains (weak / medium / strong)
2. **Schedule** — allocate more time to weak domains; maintain breadth
3. **Study sources** — official outline, authorized materials, legitimate practice questions
4. **Active recall** — explain concepts aloud; teach manager-judgment scenarios
5. **Practice exams** — analyze *why* answers are correct; adjust study plan
6. **Ethics** — review Code of Ethics scenarios
7. **Exam week** — rest, logistics, ID requirements per candidate handbook

**Prohibited**: brain dumps, shared exam items, or any copyright violation—refuse such requests.

## Manager vs technician in practice

| Question type | CISSP skill | Specialist skill |
|---|---|---|
| Which control type reduces this risk? | Here | |
| Write SIEM parser for this log | | `information-security-engineer` |
| Board deck on cyber risk appetite | Complement `chief-information-security-officer` | |
| ISO 27001 audit evidence pack | Frame controls | `compliance-specialist` |
| Run phishing simulation campaign | Define program | Engineering/IT execution |
| Contain ransomware host | Define IR program | `incident-responder` |

## Deliverable templates

**Program alignment brief** (outline):

- Business context and regulatory drivers
- Domain heat map (maturity or gap)
- Top 5 risks and planned treatments
- Initiatives by quarter with owners
- Dependencies on architecture and GRC

**Audit support memo** (outline):

- Control objective and CBK/domain mapping
- Population and sampling approach
- Evidence types and systems of record
- Known exceptions and compensating controls
- Prior finding remediation status

**Study plan** (outline):

- Domain weights from self-assessment
- Weekly topics and practice question targets
- Review dates and accountability partner

Hand technical evidence collection and control deployment to `compliance-engineer` and `information-security-engineer` after CISSP-level framing is agreed.
