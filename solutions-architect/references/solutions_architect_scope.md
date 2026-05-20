# Solutions architect scope

## Table of contents

1. [Role definition](#role-definition)
2. [Engagement types](#engagement-types)
3. [Inputs and outputs](#inputs-and-outputs)
4. [Stakeholders](#stakeholders)
5. [Boundaries vs peer skills](#boundaries-vs-peer-skills)
6. [Engagement checklist](#engagement-checklist)

## Role definition

The solutions architect owns **technical solution design** for a defined customer, partner, or internal initiative:

- What problem is being solved and for whom
- How systems integrate and what the target experience is
- Whether the solution fits security, compliance, and budget constraints
- What to prove in a PoC and what delivery needs to build next

You produce **decision-ready artifacts** for executives, procurement, security, and engineering—not production runbooks or legal contracts.

## Engagement types

| Type | Focus | Typical duration |
|---|---|---|
| Discovery | Current state, pain, constraints, success metrics | Days–2 weeks |
| Solution design | Reference architecture, options, recommendation | 1–4 weeks |
| RFP/RFI response | Requirement traceability, compliant narrative | Fixed deadline |
| PoC scoping | Charter, success criteria, technical spike plan | Days–1 week |
| Executive briefing | Storyline, risks, cost framing, decision ask | Hours–days |
| Delivery handoff | Backlog, dependencies, open ADRs | End of design phase |

## Inputs and outputs

**Collect early:**

- Business drivers, timeline, budget envelope (even rough)
- Existing systems inventory, data classifications, regions
- Security/compliance obligations (framework names, questionnaires)
- RFP/SOW language, mandatory requirements, evaluation criteria
- Named stakeholders (business owner, IT, security, procurement)

**Deliver:**

| Artifact | Purpose |
|---|---|
| Discovery summary | Shared understanding of context and gaps |
| Requirements pack | Traceable must/should/could + NFRs |
| Solution architecture | Integration and deployment views |
| Fit memos | Security/compliance and cost framing |
| Option comparison | Build vs buy vs partner with recommendation |
| PoC charter | Bounded experiment with exit criteria |
| Handoff package | Seeds delivery backlog and RAID |

## Stakeholders

| Stakeholder | What they need from you |
|---|---|
| Business sponsor | Outcomes, timeline, cost range, risks |
| IT / platform | Integration feasibility, standards, ops model |
| Security / GRC | Control fit, gaps, evidence path |
| Procurement | RFP compliance, licensing, SLAs |
| Delivery / engineering | Clear scope, interfaces, NFRs, open decisions |
| Sales / account team | Credible story, no over-promise |

Align on **decision owners** for architecture choices before deep design.

## Boundaries vs peer skills

| Topic | Solutions architect | Peer |
|---|---|---|
| Customer deal solution, RFP, PoC scope | **Own** | — |
| Org landing zone, CCoE, EA program | Inform | `enterprise-cloud-architect` |
| Product-internal ADRs, C4, eng standards | Inform | `senior-system-architecture` |
| Cloud WAF, migration waves (platform) | Collaborate | `cloud-architect` |
| Terraform modules, CI/CD build | Hand off | `infrastructure-engineer` |
| Live PoC build, demos, competitive matrix | Collaborate | `sales-engineer` |
| Strategy without technical design | Escalate | `business-consultant` |
| Contract redlines | Do not own | `commercial-counsel` |
| Program RAID and milestones | Collaborate | `technical-program-manager` |

## Engagement checklist

- [ ] Charter signed: objective, scope, out-of-scope, timeline
- [ ] Stakeholder map and interview plan
- [ ] Access to existing diagrams, inventories, RFP, security questionnaires
- [ ] Success criteria agreed (measurable for PoC or phase 1)
- [ ] Escalation path for blockers (security, legal, pricing)
- [ ] Definition of done for design phase and handoff recipient named
