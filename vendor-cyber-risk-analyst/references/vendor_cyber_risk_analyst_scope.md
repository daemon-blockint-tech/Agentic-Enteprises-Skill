# Vendor cyber risk analyst scope

## Table of contents

1. [Role boundaries](#role-boundaries)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Stakeholders](#stakeholders)
5. [Deliverables](#deliverables)

## Role boundaries

The vendor cyber risk analyst owns **operational third-party cyber risk** for the vendor portfolio: tiering, assessment execution, evidence review, monitoring, remediation tracking, and vendor-facing risk reporting.

| Adjacent role | Division of labor |
|---|---|
| `cyber-diligence-governance` | Transaction and investment diligence, deal IC packs, post-close integration themes |
| `security-risk-analyst` | Enterprise risk register, inherent/residual scoring, treatment, FAIR-style loss framing |
| `compliance-specialist` | Org-wide GRC program, audit prep, **outbound** customer questionnaire library |
| `compliance-engineer` | Automated evidence collection from IdP, CI/CD, CSPM |
| `iam-specialist` | IAM architecture, federation, access reviews, PAM—without vendor portfolio ops |
| `information-security-engineer` | Implement controls when vendor findings require internal remediation |
| `chief-information-security-officer` | Executive strategy, board operating model, risk appetite |
| `supply-chain-manager` | Physical goods, logistics, inventory, OEM sourcing—not SaaS TPRM |
| `cybersecurity` | Enterprise security program, IR policy, pentest governance |

## In scope

- TPRM intake workflows (onboarding, renewal, change, offboarding)
- Vendor **cyber tiering** and assessment depth selection
- **Questionnaire** analysis (SIG, CAIQ, custom portals)
- **Attestation** review (SOC 2 Type II, ISO 27001, pen test summaries, trust centers)
- **Continuous monitoring** triggers (breach, cert lapse, rating change)
- **Concentration** and **fourth-party** (subprocessor) analysis
- **Remediation** tracking and re-assessment criteria
- **Procurement and security** risk reporting

## Out of scope

- M&A target diligence without ongoing vendor portfolio ownership
- Legal contract negotiation, DPA redlines, indemnity → `commercial-counsel`
- Hands-on IAM, CSPM, or SIEM configuration
- Pentest execution or exploit validation
- Physical supply chain disruption modeling
- Full SOC 2 / ISO audit program management (inbound assessor prep)

## Stakeholders

| Stakeholder | Typical ask |
|---|---|
| Procurement / vendor management | Tier, approval to contract, renewal gate |
| Business owner | Integration scope, data shared, outage impact |
| Security leadership | Top vendor risks, concentration, incident exposure |
| Legal / privacy | Subprocessors, residency (risk tier input only) |
| Internal GRC | Align vendor list to audit scope |

## Deliverables

- Tier assignment with documented rationale
- Assessment summary with severity-rated findings
- Evidence gap list and attestation review notes
- Remediation tracker with owners and dates
- Periodic portfolio report (tiers, incidents, renewals, concentration)
