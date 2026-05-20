# Red Team Scope

## Purpose

Define what **enterprise adversary simulation** covers in this skill versus adjacent roles.

## In scope

| Activity | Notes |
|---|---|
| Campaign design | Multi-phase objectives, timelines, injects |
| Threat-informed emulation | Actor/TTP selection from intel or frameworks |
| MITRE ATT&CK framing | Technique mapping, coverage heatmaps |
| Purple team | Collaborative or semi-blind detection exercises |
| Detection validation | Was the stage observed? SLA? quality? |
| Executive storytelling | Business risk, attack paths, lessons for leadership |
| Blue-team handoff | Actionable detection and control improvements |

## Out of scope (route elsewhere)

| Activity | Skill |
|---|---|
| LLM jailbreaks, prompt injection, agent tool abuse | `ai-redteam` |
| Primary web/API OWASP testing | `web-pentester` |
| Primary network/AD/infra pentest | `network-pentester` |
| Standard pentest without campaign emulation | `penetration-tester` |
| SOC queue triage | `soc-analyst` |
| Live IR command, containment, regulatory comms | `incident-responder` |
| Security strategy, GRC, policy | `cybersecurity` |
| Building SIEM rules, IAM, guardrails | `information-security-engineer` |

## Engagement types

| Type | Description |
|---|---|
| **Assumed breach** | Start from compromised workstation or creds; test detect/response |
| **Full red team** | Stealth objective-driven campaign; broader scope and OPSEC |
| **Purple team** | Coordinated TTP execution with blue observation |
| **Detection gap assessment** | Repeat known TTPs; score coverage and latency |
| **Tabletop + live inject** | Narrative exercise with optional technical injects |

## Success criteria (examples)

- Demonstrate path to objective (e.g., domain admin, sensitive data access) **within ROE**
- Document **detection coverage** per ATT&CK stage
- Deliver prioritized remediations with owners
- No unauthorized targeting, no out-of-scope systems touched

## Deliverables

- Signed ROE and scope appendix
- Campaign plan and operator log
- ATT&CK technique matrix (executed vs detected)
- Executive summary + technical appendix
- Purple-team / blue-team readout and tracked actions
