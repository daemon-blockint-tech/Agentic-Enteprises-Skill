# Questionnaire scoring

## Table of contents

1. [Questionnaire types](#questionnaire-types)
2. [Analysis workflow](#analysis-workflow)
3. [Control themes](#control-themes)
4. [Scoring model](#scoring-model)
5. [Consistency checks](#consistency-checks)
6. [Outbound vs inbound](#outbound-vs-inbound)

## Questionnaire types

| Type | Notes |
|---|---|
| SIG / SIG Lite | Standardized; map to shared control library |
| CAIQ (CSA) | Cloud-centric; align to shared responsibility |
| Custom Excel / portal | Define internal mapping before scoring |
| Customer-issued (inbound to you) | Coordinate via `compliance-specialist` response library |
| Vendor-completed (outbound from them) | Primary focus of this skill |

## Analysis workflow

1. **Triage** — due date, tier, net-new vs renewal, repeating vendor
2. **Map** — each section to control themes (see below)
3. **Score** — per theme and overall gap severity
4. **Evidence ask** — list attestations required for "yes" answers
5. **Interview** — optional for T1 when answers are vague or conflicting
6. **Summarize** — findings, residual vendor risk, remediation asks
7. **Archive** — version, date, assessor for renewal comparison

## Control themes

Group responses under:

- Governance and risk management
- Asset and data inventory
- Access control and identity (federation, MFA, privileged access)
- Secure development and change management
- Vulnerability and patch management
- Logging, monitoring, and incident response
- Business continuity and disaster recovery
- Encryption and key management
- Subprocessors and data residency
- Physical and personnel security (when relevant)

Technical assertions → validate with `information-security-engineer` or `cloud-security-engineer` before accepting "implemented."

## Scoring model

Use a simple, explainable scale per theme:

| Score | Meaning |
|---|---|
| 0 — Met | Answer supported by evidence on file |
| 1 — Partial | Control exists with documented gaps |
| 2 — Gap | Missing or contradictory vs tier expectations |
| 3 — Critical gap | Unacceptable for tier (e.g., no MFA for T1 admin access) |

**Overall vendor posture**: derive from highest theme scores and T1-critical gaps, not arithmetic average alone.

Document **compensating controls** (internal) separately from vendor gaps.

## Consistency checks

Flag:

- "Yes" without matching evidence type (e.g., claims SOC 2 but no report date)
- Conflicting answers across sections (encryption at rest vs backup narrative)
- Copy-paste or outdated policy dates
- Subprocessor list missing regions claimed in data-flow answers
- Pen test scope excluding the service you consume

Compare to **prior assessment** on renewal; escalate regressions.

## Outbound vs inbound

| Direction | Owner |
|---|---|
| You assess **vendor** questionnaires | `vendor-cyber-risk-analyst` |
| **Customer** asks you to complete SIG/CAIQ | `compliance-specialist` (response library) |
| **Deal** questionnaire for target company | `cyber-diligence-governance` |

Do not reuse inbound customer answers as vendor assessment evidence without verification.
