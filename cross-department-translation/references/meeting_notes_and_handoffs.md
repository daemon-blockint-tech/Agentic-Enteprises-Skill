# Meeting notes and handoffs

## Table of contents

1. [Meeting notes structure](#meeting-notes-structure)
2. [Action item rules](#action-item-rules)
3. [RACI handoffs](#raci-handoffs)
4. [Handoff checklist](#handoff-checklist)
5. [Anti-patterns](#anti-patterns)

## Meeting notes structure

```markdown
# [Meeting title] — YYYY-MM-DD

**Attendees:** [roles or names]
**Purpose:** [one line]

## Decisions
- D1: [decision] — **Owner:** [name/role]

## Actions
| ID | Action | Owner | Due | Status |
|---|---|---|---|---|
| A1 | [verb + deliverable] | [one person] | [date] | Open |

## FYI
- [facts without required response]

## Open questions
| Question | Owner to resolve | By |
|---|---|---|
| Q1 | | |

## Parking lot
- [deferred topics]
```

**Decisions** are outcomes, not topics discussed. If no decision, write "No decision — escalated to [forum]."

## Action item rules

Each action must be:

- **Verb-led** — "Draft," "Approve," "Ship," "Validate"
- **Single owner** — one accountable person (RACI **A**)
- **Deliverable-specific** — artifact or measurable state change
- **Dated** — due date or event trigger ("before launch")

Convert vague notes:

| Weak | Strong |
|---|---|
| "Follow up on API" | **A1:** Engineering publishes OpenAPI diff by Fri — Owner: [name] |
| "Legal to review" | **A2:** Legal returns redlines on DPA v3 — Owner: [counsel] — Due: [date] |

## RACI handoffs

Use when multiple teams touch the same workstream:

| Work item | R | A | C | I |
|---|---|---|---|---|
| [item] | [does work] | [accountable] | [consulted] | [informed] |

**R** = responsible (does the work)  
**A** = accountable (one person; approves completion)  
**C** = consulted (input required before proceed)  
**I** = informed (kept in loop)

Handoff email/doc must include:

1. **Context** — why this handoff now
2. **Artifacts** — links to specs, tickets, data
3. **State** — what's done vs remaining
4. **Risks** — known blockers
5. **First action** for receiver — unambiguous next step

## Handoff checklist

Receiving team should be able to answer without a meeting:

- [ ] What is the **goal** and **definition of done**?
- [ ] What **constraints** are non-negotiable?
- [ ] What **decisions** are already made vs open?
- [ ] Who is **accountable** for each workstream?
- [ ] What **systems/access** are required?
- [ ] What **dates** are committed externally?
- [ ] Where is the **source of truth** doc?

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Team will handle" | Name one owner per action |
| Decisions buried in narrative | Pull into **Decisions** section |
| Duplicate actions across teams | Merge; clarify RACI |
| Handoff without links | Minimum: ticket ID + doc URL |
| Actions without due dates | Default to next business milestone |

For program-level tracking across many teams, pair output with `technical-program-manager` after translation is complete.
