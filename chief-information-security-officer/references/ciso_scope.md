# CISO scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Authority and committees](#authority-and-committees)
3. [Questions CISO answers](#questions-ciso-answers)
4. [Handoffs](#handoffs)

## Role boundary

| chief-information-security-officer | Partner |
|---|---|
| Program strategy, board narrative, appetite | `information-security-engineer` — deploy controls, SIEM, hardening |
| Exec incident escalation, crisis comms | `incident-responder` — CSIRT execution, containment |
| Budget, org design, vendor/insurance posture | `soc-analyst` — alert triage, shift ops |
| Board KRIs and material risk themes | `security-risk-analyst` — registers, scoring, FAIR |
| Regulatory/audit exec relationships | `compliance-specialist` — GRC program, audit prep |
| Control testing workpapers | `compliance-engineer` |
| Reference architecture, zero trust standards | `enterprise-security-architect` |
| Broad security strategy (less exec) | `cybersecurity` |

CISO **sets direction and accountability**; does not own consoles, parsers, or control test scripts.

## Authority and committees

Typical CISO interfaces:

| Forum | CISO role |
|---|---|
| Board / audit committee | Periodic security briefing; material incidents; appetite |
| Executive committee | Digital risk, major investments, crisis decisions |
| Risk committee | Appetite alignment; top risk themes; exception trends |
| Crisis management | Security lead; comms and legal coordination |
| Vendor council | Critical supplier and MSSP posture (exec view) |

Document RACI: who approves exceptions, who signs regulator notices, who owns budget.

## Questions CISO answers

- What is our 18-month security program and what do we stop doing?
- What risk are we willing to accept vs mitigate vs transfer?
- What do we tell the board after a material incident?
- How much should we spend, and on what headcount vs tools?
- Are we exam-ready, and what are the top systemic audit themes?
- Is our cyber insurance adequate for our risk profile?

## Handoffs

| After decision | Owner |
|---|---|
| Deploy controls, integrate SIEM/EDR | `information-security-engineer` |
| Hunt, detect, tune rules | `defensive-security-analyst` |
| IR runbook execution | `incident-responder` |
| Gap plans, audit evidence packs | `compliance-specialist` |
| Architecture standards and ARB | `enterprise-security-architect` |
| Risk register updates | `security-risk-analyst` |
| External statements and media | `communication-lead` (+ Legal) |
