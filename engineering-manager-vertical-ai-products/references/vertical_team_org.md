# Vertical Team Org Design

## Vertical vs horizontal

| Layer | Owns | Example |
|---|---|---|
| **Horizontal AI platform** | Model routing, RAG infra, eval framework, guardrails SDK | Shared by all verticals |
| **Vertical AI product** | Domain prompts, workflows, integrations, vertical UX | Healthcare copilot, legal review assistant |
| **Core product eng** | Non-AI product surface | Settings, billing, admin |

EM role: **vertical pod delivery** while enforcing platform contracts.

## Squad composition (typical)

| Role | Vertical focus |
|---|---|
| **AI / ML engineer** | RAG, agents, evals — `ai-engineer` |
| **Fullstack engineer** | Product UI + APIs — `senior-fullstack-developer` |
| **Tech lead** | Vertical architecture within platform guardrails |
| **PM** | Domain outcomes, not model choice alone |
| **Domain SME** | Part-time: terminology, golden Q&A, acceptance |

## Operating models

| Model | When |
|---|---|
| **Dedicated vertical squad** | Large TAM vertical with sustained roadmap |
| **Vertical + platform rotation** | Smaller vertical; borrow platform engineers |
| **Solutions-led vertical** | Heavy services; engineering caps bespoke % |

Cap **bespoke fork** of platform — track % of vertical code that bypasses shared SDK.

## Interfaces

| Partner | Cadence | Topics |
|---|---|---|
| AI platform lead | Weekly | APIs, quotas, roadmap conflicts |
| `ai-lead-ops` | Bi-weekly | Incidents, rollout tiers |
| `ai-risk-governance` | Per launch | Risk tier, policy |
| Applied architect | As needed | ADR for new data boundary or tenant model |

## Anti-patterns

- Vertical team owns production model hosting without platform SRE
- No domain SME → bad eval sets and customer trust loss
- EM committing to model/vendor without architect + procurement path
