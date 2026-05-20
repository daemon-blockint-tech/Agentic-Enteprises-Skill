---
name: vendor-cyber-risk-analyst
description: |
  Guides third-party and vendor cyber risk—TPRM intake and tiering, security questionnaire
  analysis and scoring, evidence and attestation review (SOC 2, ISO 27001, pen test summaries),
  continuous vendor monitoring, concentration and fourth-party risk, remediation tracking, and
  executive or procurement risk reporting.
  Use for vendor security assessments, SIG/CAIQ/custom questionnaire review, vendor tiering,
  inherent vendor cyber risk, vendor incident or breach impact, subprocessors and fourth parties,
  vendor risk dashboards, or TPRM program operations—not M&A or investment deal diligence only
  (cyber-diligence-governance), enterprise risk register and FAIR scoring without vendor ops focus
  (security-risk-analyst), GRC audit program and attestation prep (compliance-specialist),
  hands-on IAM or cloud policy implementation (iam-specialist, information-security-engineer),
  physical logistics and OEM supply chain (supply-chain-manager), or broad security program strategy
  (cybersecurity).
---

# Vendor Cyber Risk Analyst

## When to Use

- Run **TPRM intake** — new vendor requests, renewals, scope changes, offboarding risk
- **Tier vendors** by data, access, criticality, substitutability, and concentration
- **Analyze security questionnaires** (SIG, CAIQ, custom) — consistency, gaps, scoring
- Review **evidence and attestations** — SOC 2, ISO 27001, pen test letters, trust centers
- Operate **continuous monitoring** — breach feeds, rating changes, cert expiry, news
- Assess **concentration and fourth-party** (subprocessor) exposure
- Track **remediation** — findings, owners, due dates, re-assessment triggers
- Produce **vendor risk reports** for procurement, security, and executive audiences

## When NOT to Use

- M&A, investment, or deal-team diligence packs → `cyber-diligence-governance`
- Enterprise risk register, FAIR models, or risk appetite without vendor ops → `security-risk-analyst`
- GRC program scope, audit prep, or org-wide compliance attestation → `compliance-specialist`
- Deploy IAM, federation, PAM, or cloud IAM policies → `iam-specialist`, `information-security-engineer`
- Define CISO strategy, board operating model, or crisis exec comms → `chief-information-security-officer`
- Physical supply chain, logistics, inventory, or OEM sourcing → `supply-chain-manager`
- Broad security architecture, IR program, or pentest governance → `cybersecurity`
- Execute pentests or validate exploits → `penetration-tester`
- Negotiate contract redlines or legal interpretation → `commercial-counsel`

## Related skills

| Need | Skill |
|---|---|
| M&A/investment diligence and IC cyber packs | `cyber-diligence-governance` |
| Enterprise risk register, treatment, FAIR framing | `security-risk-analyst` |
| GRC program, audit prep, questionnaire response library | `compliance-specialist` |
| IAM federation, access reviews, PAM implementation | `iam-specialist` |
| SIEM/EDR, guardrails, technical remediation | `information-security-engineer` |
| Executive security strategy and board posture | `chief-information-security-officer` |
| Physical/logistics supply chain and sourcing | `supply-chain-manager` |
| Enterprise security program and IR policy | `cybersecurity` |

## Core Workflows

### 1. Intake and tiering

Capture vendor context, data flows, integrations, and business owner. Assign tier and assessment depth before deep review.

**See `references/tprm_intake_and_tiering.md`.**

### 2. Questionnaire analysis

Map responses to control themes, flag inconsistencies, score gaps, and define evidence asks.

**See `references/questionnaire_scoring.md`.**

### 3. Evidence and attestation review

Validate SOC/ISO scope, bridge letters, pen test coverage, subprocessors, and incident history.

**See `references/evidence_and_attestation_review.md`.**

### 4. Continuous monitoring and incidents

Monitor rating changes, public incidents, cert expiry, and contract events; trigger re-assessment.

**See `references/continuous_monitoring_and_incidents.md`.**

### 5. Reporting and remediation

Track findings to closure; report tier distribution, top risks, concentration, and renewal pipeline.

**See `references/vendor_risk_reporting.md`.**

## Outputs

- **Vendor tier memo** — tier, rationale, assessment depth, cadence
- **Assessment summary** — findings by severity, evidence gaps, residual vendor risk
- **Remediation tracker** — owner, due date, status, re-test trigger
- **Executive / procurement pack** — heat map, concentration, incidents, renewals due
- **Fourth-party / subprocessor register** — inherited risk for T1 vendors

## Principles

- **Tier before depth** — match questionnaire and evidence to inherent risk
- **Evidence over assertions** — require attestations for material claims
- **Separate cyber vendor risk from deal diligence** — use `cyber-diligence-governance` for transaction-only packs
- **Feed the enterprise register** — align with `security-risk-analyst` without duplicating program ownership
- **No legal advice** — provide risk tier and required clause themes; escalate terms to counsel

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries | `references/vendor_cyber_risk_analyst_scope.md` |
| Intake and tiering | `references/tprm_intake_and_tiering.md` |
| Questionnaire scoring | `references/questionnaire_scoring.md` |
| Evidence and attestations | `references/evidence_and_attestation_review.md` |
| Monitoring and incidents | `references/continuous_monitoring_and_incidents.md` |
| Reporting and remediation | `references/vendor_risk_reporting.md` |
