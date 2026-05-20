# Security strategy and program

## Table of contents

1. [Program pillars](#program-pillars)
2. [Roadmap structure](#roadmap-structure)
3. [Investment case](#investment-case)
4. [Operating model](#operating-model)

## Program pillars

Map initiatives to a small set of pillars (example):

| Pillar | Outcomes |
|---|---|
| Identity and access | MFA coverage, privileged access reduction, review discipline |
| Data protection | Classification tiers, encryption coverage, DLP maturity |
| Resilience | IR readiness, backup/immutability, crisis exercises |
| Secure engineering | SSDLC gates, vuln SLA adherence, third-party code |
| Detection and response | MTTD/MTTR trends, coverage, tabletop frequency |
| Third party and supply chain | Critical vendor tiering, assurance cadence |

Avoid pillar sprawl; each pillar needs an owner and 2–3 measurable outcomes.

## Roadmap structure

**Horizon framing:**

- **0–6 months** — quick wins, regulatory deadlines, incident-driven fixes
- **6–18 months** — platform upgrades, org hires, major tool replacements
- **18–36 months** — structural changes (zero trust, segmentation, identity modernization)

Per initiative document: problem, outcome, dependencies, cost, risk if deferred.

## Investment case

Executive investment memo sections:

1. **Risk or compliance driver** — what breaks if we do nothing
2. **Options** — minimum viable vs target vs accelerated
3. **Cost** — capex/opex, FTE, MSSP, license growth
4. **Benefit** — risk reduction, audit finding closure, efficiency
5. **Metrics** — how success is measured in 12 months
6. **Ask** — budget, headcount, policy exception, board awareness

Pair with `enterprise-security-architect` for technical option compare; CISO owns the decision narrative.

## Operating model

| Function | Typical home | CISO sets |
|---|---|---|
| Security engineering | CISO or CIO dotted | Priorities, SLAs, architecture alignment |
| GRC / compliance | CISO or Legal dotted | Appetite, audit themes, framework scope |
| SOC / detection | CISO | Coverage targets, escalation, MSSP model |
| IR / CSIRT | CISO | Severity matrix, crisis linkage |
| IAM program | CISO + `iam-specialist` | Policy, review cadence, PAM mandate |

Review annually: federated vs central model per BU, acquisition integration.
