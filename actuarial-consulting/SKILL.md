---
name: Actuarial Consulting
description: |
  Guides actuarial consulting engagements—client scoping and SOW design, stakeholder communication
  (CFO, risk, boards, regulators at overview level), due diligence and M&A actuarial support,
  reserving/pricing/capital review programs, model validation and opinion support, regulatory
  interaction prep, and deliverable governance (memos, exhibits, management presentations).
  Use when the user mentions actuarial consulting, actuarial engagement, reserve opinion,
  due diligence actuarial, model validation engagement, actuarial memo, SOW actuarial,
  regulatory actuarial, M&A reserves, or actuarial review—not deep technical modeling execution
  (actuary), P&C line education only (property-casualty-insurance), legal advice
  (commercial-counsel), or generic management consulting without actuarial lens
  (business-consultant).
---

# Actuarial Consulting

## When to Use

- Frame a new **actuarial consulting engagement** (objectives, boundaries, independence)
- Draft or review **SOW**, fees, data access, and deliverable list for actuarial work
- Plan **stakeholder communications** (CFO, CRO, board, audit committee, regulators—overview)
- Support **M&A, divestiture, or reinsurance** due diligence on reserves, pricing, and capital
- Structure **reserve opinion**, pricing review, or capital assessment **engagements** (not sole modeler)
- Scope **model validation**, peer review, or opinion-support workpapers
- Prepare **regulatory meeting** materials (talking points, exhibit index—not legal filings)
- Design **deliverable packages**: actuarial memo, exhibits, management presentation, Q&A log
- Run **project governance**: timeline, quality review, documentation, and sign-off chain

## When NOT to Use

- Execute pricing triangles, IBNR development, or assumption fitting as primary deliverable → `actuary`
- Teach P&C coverages, claims handling, or underwriting mechanics without engagement lens → `property-casualty-insurance`
- Interpret contracts, policy wording, or provide legal/regulatory enforcement advice → `commercial-counsel`
- Corporate FP&A, budgets, or non-insurance investor metrics → `financial-analyst` (if installed)
- Strategy, operating model, or transformation without actuarial workstream → `business-consultant`
- SOC 2 / ISO control mapping and technical audit evidence → `compliance-engineer`
- Cross-team software delivery, RAID, and program milestones only → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| Technical pricing, reserving, triangles, assumptions | `actuary` |
| P&C products, claims, underwriting context | `property-casualty-insurance` |
| Financial statements, variance, non-insurance analytics | `financial-analyst` (if installed) |
| Executive strategy without actuarial deliverables | `business-consultant` |
| Contract, DPA, regulatory interpretation | `commercial-counsel` |
| Control evidence and compliance automation | `compliance-engineer` |
| Multi-team timelines, dependencies, launch governance | `technical-program-manager` |

## Core Workflows

### 1. Engagement framing and independence

1. Clarify **client role** (insurer, reinsurer, investor, regulator-facing company, TPA)
2. Define **decision** the engagement supports (transaction, opinion year, model approval, board review)
3. Document **independence** constraints (prior work, management roles, advocacy vs advisory)
4. Identify **conflicts** (same team pricing and opining; data vendor ties)
5. Set **success criteria** and explicit out-of-scope items

**See `references/actuarial_consulting_scope.md`.**

### 2. Scoping and SOW

1. List **deliverables** with format (memo, workbook, presentation, data request)
2. Specify **data** owners, cutoffs, legal hold, and confidentiality
3. Define **methods** at headline level; defer technical picks to `actuary` workstream
4. Agree **timeline**, review gates, and client point-of-contact
5. Include **fees**, change-control, and reliance limitations

**See `references/engagement_scoping_and_sow.md`.**

### 3. Client deliverables and communication

1. Map **audiences** (CFO, CRO, board, external auditor, regulator—overview)
2. Build **storyline**: issue → analysis → implication → decision or open item
3. Separate **executive summary** from technical appendix and exhibits
4. Prepare **management presentation** and anticipated Q&A
5. Log **version control**, distribution list, and redaction rules

**See `references/client_deliverables_and_communication.md`.**

### 4. Due diligence and M&A support

1. Scope **blocks** (reserves, pricing, capital, reinsurance, run-off, embedded value)
2. Request **data room** index aligned to actuarial questions
3. Define **red-flag** checklist (development spikes, one-time items, model changes)
4. Structure **findings** by materiality and deal impact (not investment advice)
5. Hand off **deep modeling** to `actuary`; legal terms to `commercial-counsel`

**See `references/due_diligence_and_ma_support.md`.**

### 5. Model review and validation engagements

1. Classify engagement type (**validation**, **peer review**, **opinion support**, **use test**)
2. Inventory **models**, owners, version, and intended use
3. Plan **testing** themes (assumions, implementation, governance, output reasonability)
4. Document **findings** severity, remediation, and re-test criteria
5. Coordinate with **appointed actuary** or signatory where applicable

**See `references/model_review_and_validation_engagements.md`.**

### 6. Regulatory, board, and governance

1. Clarify **forum** (examination prep, board risk committee, audit committee)
2. Align **messages** to prior filings and public disclosures
3. Prepare **exhibit index** and backup schedules—not substitute for counsel
4. Track **action items**, responsible owners, and dates
5. Archive **workpapers** per firm policy and professional standards (overview)

**See `references/regulatory_board_and_governance.md`.**

## Engagement kickoff checklist

Copy and track at project start:

```
Engagement kickoff:
- [ ] Signed SOW / engagement letter with limitations
- [ ] Independence and conflict memo on file
- [ ] Data request issued; owners and cutoff agreed
- [ ] Internal team: EM, technical actuary, reviewer, PM (if needed)
- [ ] Client RACI: sponsor, data SME, signatory actuary
- [ ] Deliverable formats and draft review dates
- [ ] Escalation path (client + firm risk/quality)
```

## Engagement type matrix

| Trigger phrase | Primary workflow | Lead reference |
|---|---|---|
| SOW actuarial / actuarial engagement | Scoping and SOW | `engagement_scoping_and_sow.md` |
| actuarial memo / management presentation | Deliverables and comms | `client_deliverables_and_communication.md` |
| due diligence actuarial / M&A reserves | DD framing and findings | `due_diligence_and_ma_support.md` |
| model validation engagement | Validation plan and findings | `model_review_and_validation_engagements.md` |
| reserve opinion / actuarial review | Opinion support + governance | `regulatory_board_and_governance.md` |
| regulatory actuarial | Prep pack (overview) | `regulatory_board_and_governance.md` |

When multiple types apply (e.g., M&A plus validation), **split workstreams** in the SOW with separate timelines and reviewers.

## Quality review and sign-off

Before any client-facing draft:

1. **Technical completeness** — exhibits tie to data cutoff; bridges reconcile
2. **Narrative consistency** — memo, deck, and appendix use same definitions
3. **Audience test** — executive summary understandable without actuarial training
4. **Independence check** — no advocacy language beyond supported analysis
5. **EQ / peer review** — logged comments resolved or documented as exceptions
6. **Versioning** — draft watermark until final; distribution list approved

Coordinate with `technical-program-manager` when actuarial work is one stream in a larger transaction program (shared milestones only).

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Engagement letter / SOW | Scope, deliverables, data, timeline, fees, limitations, reliance |
| Actuarial memo | Purpose, scope, summary conclusion, methods overview, limitations, exhibits list |
| Management deck | 5–12 slides: context, findings, impact, recommendations, open items |
| DD report section | Material issues, evidence pointers, quantified range where supported |
| Validation report | Scope, criteria, findings, management responses, follow-up |
| Board / regulatory pack | Agenda fit, consistent metrics, glossary, appendix index |
| Workshop readout | Decisions, open items, owners, dates |
| Finding register | ID, severity, evidence, management response, re-test status |

State **uncertainty**, **reliance limits**, and **non-advice** boundaries. Do not present consulting output as statutory filing, legal opinion, or appointed-actuary sign-off without qualified human review.

## Common pitfalls

- **Scope creep** without change order when new LOBs or models are added mid-engagement
- **Orphan exhibits** that do not support a stated conclusion in the memo
- **Metric drift** between deck, memo, and public filings
- **Dual role** pressure (consultant validates own prior model build)
- **Missing data** treated as zero rather than flagged as limitation
- **Regulatory meeting** prep that crosses into legal interpretation—escalate to `commercial-counsel`

## When to load references

- **Scope, independence, ethics** → `references/actuarial_consulting_scope.md`
- **SOW and scoping** → `references/engagement_scoping_and_sow.md`
- **Memos, decks, stakeholder comms** → `references/client_deliverables_and_communication.md`
- **M&A and due diligence** → `references/due_diligence_and_ma_support.md`
- **Model validation and review** → `references/model_review_and_validation_engagements.md`
- **Board, regulatory prep, governance** → `references/regulatory_board_and_governance.md`
