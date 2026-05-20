# Requirements and decision briefs

## Table of contents

1. [Brief types](#brief-types)
2. [Dual-audience layout](#dual-audience-layout)
3. [Technical → business template](#technical--business-template)
4. [Business → engineering template](#business--engineering-template)
5. [Decision record](#decision-record)

## Brief types

| Type | When | Primary reader |
|---|---|---|
| **Translation brief** | Existing doc needs reframing only | Target audience |
| **Decision brief** | Leadership must choose among options | Executive + sponsors |
| **Handoff brief** | Work moves between teams | Receiving team lead |
| **Constraint brief** | Policy/finance/legal limits implementation | Engineering + product |

## Dual-audience layout

Use labeled sections on one page when leaders and implementers share a single artifact:

```markdown
## Executive (≤200 words)
- Decision needed by [date]
- Recommendation
- Impact if delayed

## [Target function] detail
- Context, constraints, dependencies
- Acceptance criteria / evidence
- Appendix: links, diagrams, data
```

Rules:

- Executive section contains **no unexplained acronyms**
- Detail section may reference RFCs, tickets, control IDs
- **Single source of truth** for numbers (no conflicting figures across sections)

## Technical → business template

```markdown
# [Initiative] — business summary

## Outcome
What changes for customers or the business (1–2 sentences).

## Why now
Burning platform or opportunity; link to OKR/metric.

## Scope
In / out / phase 2.

## Cost and timeline
Effort band (S/M/L), major dependencies, key dates.

## Risks
Top 3 with mitigations (availability, security, compliance, revenue).

## Decision / ask
What you need from this audience (approve, fund, prioritize, accept risk).

## Technical appendix (optional)
Architecture sketch, SLIs, link to RFC.
```

Translate **implementation choices** into **business consequences** (revenue, cost, risk, time-to-market).

## Business → engineering template

```markdown
# [Initiative] — engineering brief

## Problem statement
User or business problem in testable terms.

## Success criteria
Measurable outcomes; definition of done.

## Constraints (must / must not)
Policy, budget, date, regions, data residency, accessibility, etc.

## Non-goals
Explicit exclusions to prevent scope creep.

## Dependencies
Teams, vendors, data, approvals required before build.

## Open questions
Owner per question; deadline for resolution.

## Context links
PRD, designs, legal/compliance refs, finance case ID.
```

Avoid solution prescription unless the business decision **already** selected an approach.

## Decision record

For cross-functional decisions, capture:

| Field | Content |
|---|---|
| Decision | What was chosen |
| Date / forum | When and where decided |
| Options considered | Brief list with reject reasons |
| Owners | Accountable for execution |
| Assumptions | What must remain true |
| Review trigger | When to revisit |

Pair with `business-consultant` when the brief is primarily analytical; stay in this skill when the core task is **audience-appropriate framing**.
