# Enterprise security architect scope

## Table of contents

1. [Role boundaries](#role-boundaries)
2. [Operating model](#operating-model)
3. [Stakeholders](#stakeholders)
4. [Deliverable maturity](#deliverable-maturity)

## Role boundaries

| In scope | Out of scope (route to peer skill) |
|---|---|
| Enterprise reference architecture and domain standards | Cloud landing zone vending and CCoE economics → `enterprise-cloud-architect` |
| Zero-trust strategy and segmentation patterns | Cloud SCP/CSPM/terraform remediation → `cloud-security-engineer` |
| Control framework mapping to architecture | GRC program, audit walkthroughs → `compliance-specialist` |
| Security ARB criteria and pattern catalog | Product/service ADRs and C4 → `senior-system-architecture` |
| Board/CISO architecture narrative | Risk register scoring only → `security-risk-analyst` |
| Acquisition security integration standards | SIEM/EDR deployment and tuning → `information-security-engineer` |
| IAM architecture standards (not entitlement ops) | Access reviews and PAM config → `iam-specialist` |

### vs `enterprise-cloud-architect`

`enterprise-cloud-architect` owns **multi-BU cloud programs** — landing zones, CCoE, enterprise agreements, regulated **cloud placement**, and hybrid integration at cloud-EA depth. This skill owns **enterprise-wide security domains** (identity, data, app, network, endpoint) and patterns that apply on-prem, SaaS, and cloud. Coordinate where cloud guardrails express security standards; do not duplicate landing-zone vending or FinOps commit strategy here.

### vs `information-security-engineer`

`information-security-engineer` **implements and operates** controls — SSO connectors, KMS, WAF, SIEM/EDR pipelines, hardening baselines, remediation engineering. This skill defines **what must exist** (reference architecture, mandatory patterns, ARB gates) and hands off build/run to engineering. Do not author terraform modules, connector configs, or SOC playbooks in architecture deliverables.

## Operating model

Define how security architecture governs the enterprise:

| Element | Questions to answer |
|---|---|
| Authority | Who approves mandatory standards? Who grants time-bound exceptions? |
| Federation | Which decisions are central vs BU-owned within guardrails? |
| ARB / SAR | Entry criteria, reviewers, threat modeling depth by tier |
| Standards lifecycle | Draft → pilot → mandatory → deprecated; sunset dates |
| EA alignment | How security blocks attach to business capability maps |
| Risk alignment | How control tiers tie to appetite and risk committee |

**Recommended tiers for systems:**

| Tier | Examples | Review depth |
|---|---|---|
| T0 | Internet-facing, regulated data, crown jewels | Full threat model, mandatory patterns, executive visibility |
| T1 | Internal critical, integration hubs | Standard patterns, documented exceptions |
| T2 | Low sensitivity, isolated | Lightweight checklist |

## Stakeholders

| Stakeholder | Typical ask |
|---|---|
| CISO / VP Security | Posture narrative, investment themes, standards compliance |
| Enterprise architect | Capability alignment, integration standards, technology radar |
| BU technology leads | Approved patterns, exception path, acquisition checklist |
| Risk / GRC | Control mapping, audit-friendly architecture evidence |
| Infrastructure / cloud | Segmentation, logging, identity federation boundaries |
| M&A / integration | Day-1/30/90 security assimilation playbook |

## Deliverable maturity

| Maturity | Characteristics |
|---|---|
| Ad hoc | Point designs, inconsistent terminology |
| Defined | Reference model published, ARB exists |
| Managed | Standards catalog, exception register, metrics |
| Optimizing | Continuous pattern improvement, threat-informed updates |

Track **adoption metrics**: % workloads on mandatory patterns, exception aging, time-to-approve architecture changes.
