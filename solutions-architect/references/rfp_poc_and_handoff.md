# RFP, PoC, and handoff

## Table of contents

1. [RFP and RFI response](#rfp-and-rfi-response)
2. [PoC charter](#poc-charter)
3. [PoC vs production gap list](#poc-vs-production-gap-list)
4. [Delivery handoff](#delivery-handoff)
5. [Handoff package contents](#handoff-package-contents)
6. [Post-handoff support model](#post-handoff-support-model)

## RFP and RFI response

**Process:**

1. Parse RFP into requirement IDs (mirror customer numbering where possible)
2. Assign **owner** per section (architecture, security, ops, commercial)
3. Draft **compliant** answers; mark **partial** or **future** explicitly
4. Cross-check traceability matrix (requirement → response → evidence)
5. Red-team for over-commitment; security and legal review per policy
6. Final consistency pass (terminology, diagrams, pricing alignment)

**Structure per requirement:**

```
Ref: RFP 4.3.2
Requirement: [quote or paraphrase]
Response: Compliant | Partial | Non-compliant | Alternative
Solution approach: [how]
Evidence: [diagram, cert, PoC plan]
Dependencies: [customer action, third party]
```

Differentiate **standard product** vs **custom** scope; custom items need effort estimate and risk flag.

Executive summary: outcomes, differentiators, implementation approach, risks, assumptions.

## PoC charter

A PoC proves **specific hypotheses**, not full production.

| Field | Content |
|---|---|
| Objective | What decision the PoC unlocks |
| In scope | Features, integrations, environments |
| Out of scope | Explicit exclusions |
| Success criteria | Measurable (latency, throughput, user tasks) |
| Duration | Start/end; decision date |
| Team | Customer + vendor roles |
| Environment | Cloud account owner, data (synthetic vs prod-like) |
| Exit | Go / no-go / extend with conditions |

**Technical spikes** — list experiments (e.g., IdP federation, 10k TPS load, CMK).

Live build and demo execution → collaborate with `sales-engineer`. Infra for PoC only → `infrastructure-engineer` if non-trivial.

## PoC vs production gap list

Maintain a visible **gap register**:

| Gap | PoC state | Production need | Effort | Risk |
|---|---|---|---|---|
| HA multi-AZ | Single AZ | Active-passive | M | Medium |
| CMK | Platform keys | Customer KMS | L | High contractual |
| Monitoring | Basic logs | SIEM integration | M | Low |

Use gaps to **right-size** statements in RFP and contracts.

## Delivery handoff

Hand off when:

- Requirements baseline approved (or change process agreed)
- Target architecture accepted with logged open ADRs
- PoC outcome documented (if applicable)
- Security gaps have owners and target dates
- Backlog seed and milestone sketch accepted by delivery lead

**Handoff meeting agenda:**

1. Walk context and success criteria
2. Review architecture and interface catalog
3. Review requirements and traceability
4. Review gap register and RAID
5. Agree first sprint / wave scope and environments
6. Confirm escalation and change control

Program-scale coordination → `technical-program-manager`.

## Handoff package contents

| Artifact | Location / format |
|---|---|
| Discovery summary | Markdown / wiki |
| Requirements pack + matrix | Spreadsheet or doc |
| Architecture diagrams | Source files + exported PNG/PDF |
| Interface catalog | Table + OpenAPI links |
| Security/compliance fit memo | With gap register |
| Sizing and cost assumptions | Spreadsheet with formulas |
| PoC report | Results vs success criteria |
| ADR log | Open and decided |
| Backlog seed | Epics/stories linked to REQ IDs |
| RAID | Risks, actions, issues, decisions |

## Post-handoff support model

Define **architecture owner** during build:

- Office hours for clarification (not day-to-day PM)
- ADR decisions for scope changes
- Review of material integration or security changes
- Customer-facing review before major milestones

Avoid becoming the delivery PM—escalate schedule and dependency tracking to `technical-program-manager`.

Return to solutions architect for **phase 2** design, expansion regions, or new RFP modules.
