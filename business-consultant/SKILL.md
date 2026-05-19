---
name: business-consultant
description: |
  Guides management consulting-style work—engagement framing, hypothesis-driven problem structuring,
  issue trees, business cases, operating model and capability design, strategic options analysis,
  workshop facilitation, and executive recommendations (not legal advice).
  Use when diagnosing a business problem, structuring a strategy or transformation initiative,
  building a business case for leadership, designing target operating models, preparing steerCo or
  board recommendations, or advising on build-vs-buy and portfolio priorities—not for detailed
  requirements/BRDs (business-analyst), multi-team delivery tracking (technical-program-manager),
  contract negotiation (commercial-counsel), revenue accounting (senior-revenue-accountant),
  applied AI architecture (applied-ai-architect-commercial-enterprise), or system ADRs
  (senior-system-architecture). Canvas/TAM: business-model-researcher. Comms: communication-lead.
  M&A closing: transaction-manager. M&A principal/IC: transaction-principal.
---

# Business Consultant

## When to Use

- Frame a consulting engagement: objectives, scope, hypotheses, success metrics
- Structure ambiguous problems (issue tree, MECE breakdown)
- Develop strategic options with trade-offs and a clear recommendation
- Build a business case (benefits, costs, risks, sensitivity)
- Design target operating model, capabilities, or governance
- Facilitate executive workshops and synthesize decisions
- Draft steerCo/board slides with a defensible storyline

## When NOT to Use

- User stories, BRDs, process maps for build teams → `business-analyst`
- Cross-team milestones, RAID, program status → `technical-program-manager`
- MSA/SaaS redlines or legal risk → `commercial-counsel`
- Quote-to-cash, CPQ, order form assembly → `deal-operations-administrator`
- GL, ASC 606, close calendars → `senior-revenue-accountant`
- Dashboards, SQL, metric definitions → `bi-analyst`
- C4 diagrams, integration ADRs, NFR targets → `senior-system-architecture`
- UX research and wireframes → `product-designer`
- Business model canvas, market sizing, unit economics research → `business-model-researcher`
- M&A closing matrix, signing, funds flow → `transaction-manager`
- Live M&A thesis, valuation, negotiation → `transaction-principal`

## Related skills

| Need | Skill |
|---|---|
| Requirements and FRDs for delivery | `business-analyst` |
| Program execution and launch readiness | `technical-program-manager` |
| Technical architecture decisions | `senior-system-architecture` |
| Contract and commercial terms | `commercial-counsel` |
| Deal desk and order processing | `deal-operations-administrator` |
| Research synthesis and long-form docs | `tech-writer-researcher` |
| Product UX and journeys | `product-designer` |
| Canvas, TAM, competitor pricing research | `business-model-researcher` |
| Applied AI solution architecture | `applied-ai-architect-commercial-enterprise` |
| Company-wide messaging and comms cadence | `communication-lead` |
| M&A deal execution and closing | `transaction-manager` |
| M&A deal principal and IC | `transaction-principal` |

## Core Workflows

### 1. Engagement framing

Before analysis:

1. **Sponsor and decision** — Who decides? By when? What happens if we do nothing?
2. **Success criteria** — Measurable outcomes (revenue, cost, risk, time)
3. **Scope** — In / out / assumptions; phase 1 vs later
4. **Hypotheses** — 3–5 testable statements (not solutions yet)
5. **Workplan** — Analyses, interviews, data pulls, milestones

**See `references/engagement_framing.md`.**

### 2. Problem structuring

1. Start from the **decision** or outcome, not symptoms
2. Build an **issue tree** (MECE branches)
3. Prioritize branches by impact and ease of analysis
4. Assign fact base: interviews, benchmarks, internal data
5. Kill branches early when evidence disproves hypothesis

**See `references/problem_structuring.md`.**

### 3. Options and recommendation

For each viable option document:

| Dimension | Content |
|---|---|
| Description | What changes for customers, employees, systems |
| Benefits | Quantified where possible; ranges if uncertain |
| Costs | One-time + run rate; implementation risk |
| Risks | Top 3 with mitigations |
| Dependencies | Org, tech, vendor, regulatory |

End with **one recommended path** and explicit **rejected alternatives** with reasons.

**See `references/business_case.md`.**

### 4. Operating model (when relevant)

Define how the organization will run after change:

- **Capabilities** — What must we be great at?
- **Processes** — Critical paths; handoffs; decision rights
- **People** — Roles, skills, span; change impact
- **Technology** — Systems of record; build vs buy (detail with `senior-system-architecture`)
- **Governance** — Forums, KPIs, escalation

**See `references/operating_model.md`.**

### 5. Executive communication

Storyline order:

1. **Answer first** — Recommendation in one sentence
2. **So what** — Why it matters now (burning platform or opportunity)
3. **Evidence** — 3–5 supporting facts, not appendix dumps
4. **How** — Roadmap phases, owners, investment
5. **Risks and asks** — Decisions needed from the room

Use appendix for methodology and backup analyses.

**See `references/executive_communication.md`.**

### 6. Handoff to delivery

When recommendation is approved:

| Output | Owner skill |
|---|---|
| BRD / user stories / process specs | `business-analyst` |
| Program plan and RAID | `technical-program-manager` |
| Architecture ADR | `senior-system-architecture` |
| Commercial contracting | `commercial-counsel` |

Document open assumptions delivery teams must validate.

## When to load references

- **Scope and hypotheses** → `references/engagement_framing.md`
- **Issue trees and MECE** → `references/problem_structuring.md`
- **ROI and options** → `references/business_case.md`
- **Capabilities and governance** → `references/operating_model.md`
- **SteerCo and board packs** → `references/executive_communication.md`
