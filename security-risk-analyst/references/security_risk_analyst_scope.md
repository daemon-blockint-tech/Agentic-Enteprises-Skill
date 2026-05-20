# Security risk analyst scope

## Table of contents

1. [Purpose](#purpose)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Framework alignment](#framework-alignment)
5. [Deliverables](#deliverables)
6. [Peer handoffs](#peer-handoffs)

## Purpose

Analyze **information security risk** so leaders can prioritize investment, accept residual risk explicitly, and govern third parties—without operating controls, running audits end-to-end, or executing tests.

## In scope

- Risk registers, scenarios, inherent/residual scores
- Threat–vulnerability–control (TVC) mapping and gap analysis
- Treatment recommendations and risk acceptance records
- Business impact framing for security scenarios (availability, confidentiality, integrity, safety where relevant)
- KRIs and risk committee / board narrative support
- Third-party and supply-chain **risk tiering** and questionnaire scope (not legal contracting)

## Out of scope

| Activity | Route to |
|---|---|
| SOC alert triage | `soc-analyst` |
| Pentest / red team execution | `penetration-tester`, `web-pentester`, `network-pentester`, `red-team-specialist` |
| Control implementation | `information-security-engineer`, `cloud-security-engineer` |
| SOC 2 / ISO evidence automation | `compliance-engineer`, `cloud-compliance-specialist` |
| Enterprise security strategy and IR program | `cybersecurity` |
| AI model risk classification and AI policy | `ai-risk-governance` |

## Framework alignment

Use concepts from **ISO/IEC 27005** (risk management) and **NIST RMF** (categorize → select → implement → assess → authorize → monitor) as **structure**, not as a substitute for organizational risk appetite statements or legal obligations.

- **Do** map scenarios to assets, threats, controls, and residual risk.
- **Do not** claim full ISO 27001 certification readiness—that is `compliance-engineer` with evidence workflows.

## Deliverables

| Artifact | Minimum content |
|---|---|
| Risk register row | Scenario, owner, scores, treatment, review date |
| Risk assessment memo | Scope, methodology, top findings, recommendations |
| Heat map | Likelihood × impact (inherent and residual views) |
| Risk acceptance | Approver, rationale, expiry, compensating controls |
| Committee pack | Top N risks, KRIs, trend, open treatments |

## Peer handoffs

| Input from | Use for |
|---|---|
| Pentest / vuln reports | Threat and vulnerability evidence |
| Audit gaps | Control effectiveness and residual risk |
| Architecture reviews | Asset boundaries and new scenarios |
| Vendor questionnaires | Third-party inherent risk |
| Incidents | Re-score related scenarios; validate KRIs |

| Output to | Action |
|---|---|
| `information-security-engineer` | Mitigation = control implementation backlog |
| `compliance-engineer` | Control gaps that require evidence or policy |
| `cybersecurity` | Program-level appetite and portfolio prioritization |
