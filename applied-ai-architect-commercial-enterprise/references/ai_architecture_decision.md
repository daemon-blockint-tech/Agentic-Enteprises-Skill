# AI architecture decision

## Table of contents

1. [When to write](#when-to-write)
2. [ADR template](#adr-template)
3. [Review participants](#review-participants)
4. [Common decisions](#common-decisions)

## When to write

AI-specific ADR when decision affects:

- Where customer or corp data is processed
- Model vendor or hosting model
- Autonomy level (agent write tools)
- Shared vs per-tenant indexes
- Logging and retention of prompts

Link to `senior-system-architecture` ADR for broader integration topology.

## ADR template

```markdown
# ADR-NNN: [AI decision title]

**Status:** Proposed | Accepted
**Context:** Use case tier, commercial vs enterprise, data classes
**Decision:** [What we will do]

## Data flow
[Diagram: sources → processing → model → user; trust zones]

## Options considered
### A — [e.g. shared multi-tenant index + metadata filter]
- Pros / cons / cost / security

### B — [e.g. per-tenant dedicated index]
- Pros / cons / cost / security

## NFR impact
| NFR | Target | How this decision supports |

## Risks
| Risk | Mitigation | Owner |

## Eval and rollout
- Eval gates: [golden, safety]
- Rollback: [model pin, feature flag]

## Compliance
- Risk tier: [ai-risk-governance ref]
- DPA/subprocessor impact: [Y/N]
```

## Review participants

| Role | Reviews |
|---|---|
| Engineering | Feasibility, operability |
| Security | Data flow, access, logging |
| Risk/compliance | Tier, policy fit |
| Product | UX and customer promise |
| Procurement | Contract alignment (if new vendor) |

## Common decisions

| Decision | Typical enterprise choice | Typical commercial choice |
|---|---|---|
| RAG vs fine-tune | RAG + ACL | RAG + tenant partition |
| Agent autonomy | Human confirm on writes | Tier-based by plan |
| Model hosting | Private endpoint | SaaS API + optional VPC tier |
| Citation required | Yes external | Yes customer-facing |
