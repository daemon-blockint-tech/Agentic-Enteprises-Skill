# Classified cyber security senior manager scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Program types](#program-types)
3. [Questions this role answers](#questions-this-role-answers)
4. [Handoffs](#handoffs)

## Role boundary

| classified-cyber-security-senior-manager | Partner |
|---|---|
| Classified program governance, authorization interfaces, inspection readiness | `information-security-engineer` — control implementation, SIEM, hardening |
| Government stakeholder escalation themes, ops interfaces | `incident-responder` — CSIRT execution, containment, forensics |
| Cleared workforce/facility cyber alignment (high level) | `soc-analyst` — alert triage, shift operations |
| Authorization package status, significant changes | `information-systems-security-officer-classified-specialist` — SSP, POA&M, assessor coordination |
| Reference architecture, patterns, ARB exceptions | `enterprise-security-architect` — standards and design authority |
| Classified supply chain and vendor flow-down | `compliance-specialist` — commercial GRC, framework mapping |
| Enterprise board strategy, appetite, insurance | `chief-information-security-officer` — exec program and board narrative |
| Risk registers and quantitative treatment | `security-risk-analyst` — scoring, FAIR, registers |

This role **governs classified cyber programs** and **interfaces with authorizing officials**; it does not operate consoles, write detection rules, or perform assessor-level control testing.

## Program types

Typical environments (generic labels only):

| Environment | Manager focus |
|---|---|
| Classified enclave / high-side network | Boundary, operations interfaces, change governance |
| Defense industrial base program | Contract flow-down, visitor/access themes, subcontractor cyber |
| Multi-level security or compartmented workloads | Data flow policy, cross-domain governance themes |
| Shared services into classified mission systems | Inherited controls, dependency risk, SLA for security services |

Document: system name, classification level (per org policy), authorization status, and owning mission.

## Questions this role answers

- What is in scope for this classified cyber program, and who owns each interface?
- Are we on track for authorization milestones, and what decisions do authorizing officials need?
- What must we tell government stakeholders after a suspected or confirmed incident?
- Are we inspection-ready, and what POA&M items block a clean assessment?
- Is cleared workforce and facility posture aligned with cyber access requirements?
- Is classified IT supply chain controlled (approved products, config baselines, vendor attestations)?

## Handoffs

| After decision | Owner |
|---|---|
| Implement control or remediate finding | `information-security-engineer` |
| Maintain SSP, POA&M, assessor evidence | `information-systems-security-officer-classified-specialist` |
| Execute incident containment and timeline | `incident-responder` |
| Draft commercial audit evidence packs | `compliance-specialist` |
| Board-level enterprise risk narrative | `chief-information-security-officer` |
| Architecture standard or pattern exception | `enterprise-security-architect` |
| Legal classification or export question | Legal/compliance (out of band) |
