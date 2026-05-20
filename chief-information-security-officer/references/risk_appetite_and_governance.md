# Risk appetite and governance

## Table of contents

1. [Appetite statement](#appetite-statement)
2. [Thresholds and metrics](#thresholds-and-metrics)
3. [Exception governance](#exception-governance)
4. [Board risk alignment](#board-risk-alignment)

## Appetite statement

Risk appetite is **how much risk the organization chooses to accept** to pursue objectives—not zero risk.

Draft appetite across domains (tailor to industry):

| Domain | Appetite example (illustrative) |
|---|---|
| Customer data breach | Very low — mandatory controls, no unapproved exceptions |
| Ransomware | Low — immutability, IR tested quarterly |
| Third-party access | Low — tier-1 vendors assessed annually |
| Legacy technical debt | Moderate — time-boxed exceptions with sunset |
| Innovation / shadow IT | Moderate with guardrails — approved sandboxes only |

Link appetite to control tiers in `enterprise-security-architect` standards where applicable.

## Thresholds and metrics

Translate appetite into **measurable thresholds**:

- Critical vulns open > X days on internet-facing assets
- MFA coverage < Y% for workforce
- Privileged accounts without PAM > Z
- Material incidents per year
- Audit findings rated high open > N days

Escalate to CISO when thresholds breach; to board when **material** to financial or reputational statements.

Delegate register maintenance to `security-risk-analyst`; CISO owns appetite breaches and systemic themes.

## Exception governance

Exception record minimum fields:

- Control requirement and compensating controls
- Risk owner (business), approver (CISO or delegate)
- Expiry date (max 12 months unless board-approved)
- Evidence of monitoring

Report **exception volume and aging** to audit committee quarterly—rising exceptions signal appetite drift.

## Board risk alignment

| Input | Source |
|---|---|
| Top enterprise risks including cyber | ERM + `security-risk-analyst` |
| Appetite breaches | Security metrics |
| Incident materiality | IR + Legal |
| Regulatory change | Compliance + Legal |

CISO does not replace ERM; **align cyber narrative** to enterprise risk taxonomy and rating scales.
