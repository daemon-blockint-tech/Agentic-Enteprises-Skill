---
name: matrix-environment
description: |
  Guides organizational operating models for cross-functional security and technology teams—matrix
  vs hierarchical structures, RACI and interaction models, chapter/pod/guild patterns, platform vs
  product vs security alignment, interfaces between SOC/IR/AppSec/GRC/Engineering, scaling patterns,
  anti-patterns, and operating rhythm. Use when designing or tuning a matrix org, security/engineering
  interaction models, chapter or guild structure, decision rights between central and embedded teams,
  cross-functional interfaces (SOC, IR, AppSec, GRC, SRE, platform), or org scaling—not cloud
  environment tiers or deployment matrices alone (cloud-engineer), executive security program strategy
  (chief-information-security-officer), enterprise security reference architecture
  (enterprise-security-architect), multi-team program RAID and milestones (technical-program-manager),
  or VP infrastructure portfolio and capex (vp-of-infrastructure).
---

# Matrix Environment

## When to Use

- Design or **tune a matrix operating model** — solid vs dotted lines, decision rights, escalation
- Map **RACI** and **interaction models** between security, platform, product engineering, and ops
- Structure **chapters, pods, guilds, or communities of practice** for security and platform skills
- Align **platform vs product vs security** — embedded vs central, federated vs consolidated
- Define **interfaces** — SOC ↔ IR ↔ AppSec ↔ GRC ↔ Engineering ↔ SRE ↔ TPM
- Plan **operating rhythm** — cadences, forums, intake, prioritization, and governance gates
- Diagnose **scaling problems** — duplication, accountability gaps, slow decisions, shadow teams
- Clarify **environment tiers** (dev/stage/prod) only as an **org handoff** topic—not cloud build-out

## When NOT to Use

- Board briefings, risk appetite, security budget, crisis exec comms → `chief-information-security-officer`
- Enterprise security reference architecture, zero-trust patterns, ARB standards → `enterprise-security-architect`
- Broad security strategy, policies, control architecture → `cybersecurity`
- Deploy SSO, SIEM, EDR, hardening, or remediate vulnerabilities → `information-security-engineer`
- Multi-team milestones, RAID, launch readiness, dependency maps → `technical-program-manager`
- SLI/SLO, error budgets, PRRs, burn-rate alerting → `site-reliability-engineer`
- 3–5 year infra portfolio, capex, hyperscaler EA, board infra narrative → `vp-of-infrastructure`
- VPC, landing zones, Terraform, or environment provisioning → `cloud-engineer`, `infrastructure-engineer`
- Generic strategy issue trees without org design → `business-consultant`

## Related skills

| Need | Skill |
|---|---|
| CISO program, board KRIs, appetite, budget | `chief-information-security-officer` |
| Enterprise security reference architecture | `enterprise-security-architect` |
| Enterprise security strategy and policies | `cybersecurity` |
| Security control implementation and tooling | `information-security-engineer` |
| Multi-team program coordination and RAID | `technical-program-manager` |
| Reliability SLOs, PRRs, incident mitigation | `site-reliability-engineer` |
| VP infrastructure org and portfolio | `vp-of-infrastructure` |
| DACI / decision facilitation workshops | `daci-framework` |
| Company operating system (EOS, OKRs, L10) | `company-os` |
| Process documentation and RACI in SOPs | `process-doc` |

## Core Workflows

### 1. Scope and operating model intent

Clarify why matrix (vs functional or product-only), maturity, and non-goals.

**See `references/matrix_environment_scope.md`.**

### 2. Team topology and chapters

Pods, chapters, guilds, platform teams, and embedded security models.

**See `references/team_topology_and_chapters.md`.**

### 3. RACI and interaction models

Accountability, handoffs, SLAs between functions, and escalation paths.

**See `references/raci_and_interaction_models.md`.**

### 4. Cross-functional interfaces

SOC, IR, AppSec, GRC, Engineering, SRE, platform—intake, triage, and closure.

**See `references/cross_function_interfaces.md`.**

### 5. Scaling and anti-patterns

Growth stages, consolidation triggers, and common failure modes.

**See `references/scaling_and_anti_patterns.md`.**

### 6. Operating rhythm and governance

Cadences, forums, prioritization, and change governance across the matrix.

**See `references/operating_rhythm_and_governance.md`.**

## Outputs

- **Operating model canvas** — structure, decision rights, escalation, forums
- **RACI matrix** — per capability or lifecycle (build, run, respond, assure)
- **Interaction model** — swimlanes or sequence for key flows (vuln, incident, change, audit)
- **Interface catalog** — owners, SLAs, artifacts in/out, tools of record
- **Chapter/guild charter** — mission, membership, standards, backlog intake
- **Scaling roadmap** — when to centralize, federate, or embed; hiring and ratio guidance
- **Anti-pattern assessment** — gaps, duplications, recommended fixes with owners

## Principles

- **Optimize for flow of work** — minimize handoffs and ambiguous ownership
- **One throat to choke per decision** — matrix needs clear A/R, not shared vagueness
- **Embed where friction is** — centralize standards, embed execution at product boundaries
- **Measure interfaces** — SLAs, backlog age, and repeat escalations expose org debt
- **Evolve with scale** — models that work at 50 FTE often break at 500; plan transitions
- **Separate org environment from cloud environment** — tier promotion is a process; matrix is people

## When to load references

- **Role boundary and intent** → `references/matrix_environment_scope.md`
- **Topology and chapters** → `references/team_topology_and_chapters.md`
- **RACI and handoffs** → `references/raci_and_interaction_models.md`
- **SOC/IR/AppSec/GRC/Eng interfaces** → `references/cross_function_interfaces.md`
- **Growth and anti-patterns** → `references/scaling_and_anti_patterns.md`
- **Cadence and governance** → `references/operating_rhythm_and_governance.md`
