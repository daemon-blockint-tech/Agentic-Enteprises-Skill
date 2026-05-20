# Matrix Environment Scope

## Purpose

Define how **people and teams** collaborate across security, platform, and product engineering—not how cloud accounts or deployment pipelines are named.

## In scope

| Topic | Examples |
|---|---|
| Operating model | Matrix vs functional vs product-led; solid/dotted lines |
| Decision rights | Who sets standards vs who ships; exception paths |
| Team topology | Chapters, pods, guilds, platform squads, embedded security |
| Interfaces | SOC, IR, AppSec, GRC, SRE, TPM, product engineering |
| Governance rhythm | SteerCo, ARB, change advisory, security council |
| Scaling | Ratios, consolidation, federated vs central |
| Environment tiers (org lens) | Who owns promotion gates, approvals, and accountability across dev/stage/prod |

## Out of scope (hand off)

| Topic | Skill |
|---|---|
| Board security narrative, appetite, budget | `chief-information-security-officer` |
| Reference architecture, zero-trust patterns | `enterprise-security-architect` |
| Security program strategy and policies | `cybersecurity` |
| SIEM/EDR/SSO implementation | `information-security-engineer` |
| Program RAID, milestones, launch gates | `technical-program-manager` |
| SLO/error budget operations | `site-reliability-engineer` |
| Infra portfolio, capex, hyperscaler EA | `vp-of-infrastructure` |
| Landing zones, Terraform, account vending | `cloud-engineer`, `infrastructure-engineer` |

## Clarifying questions (ask first)

1. **Company stage** — startup, scale-up, enterprise; regulated or not
2. **Primary pain** — slow decisions, duplicated work, unclear ownership, security friction, incident chaos
3. **Current shape** — central security vs embedded; platform team maturity; SOC in-house vs MSSP
4. **Constraints** — union rules, geo distribution, M&A integration, outsourcing
5. **Success metric** — cycle time, audit findings, incident MTTR, developer satisfaction, cost per engineer

## Environment tiers (secondary)

When the user says "environment matrix," confirm intent:

| If they mean… | Primary skill | This skill covers… |
|---|---|---|
| Dev/stage/prod promotion, approvals, segregation of duties | `cloud-engineer`, `devops`, `deployment-strategist` | **Org ownership** of tier gates, CAB membership, who signs off |
| Account/subscription layout per env | `cloud-architect`, `enterprise-cloud-architect` | **Interface** between platform team and product teams for env requests |
| Org structure for security + engineering | **matrix-environment** | Full operating model |

## Deliverable checklist

- [ ] Stated operating model choice and rationale
- [ ] Decision rights table (standards, build, run, respond, assure)
- [ ] Named forums and cadence
- [ ] Explicit handoffs to peer skills for execution work
