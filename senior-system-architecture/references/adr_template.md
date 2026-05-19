# ADR template

## Table of contents

1. [When to write an ADR](#when-to-write-an-adr)
2. [Template](#template)
3. [Quality bar](#quality-bar)

## When to write an ADR

Write an ADR when:

- Multiple teams depend on the decision
- Reversal cost is high (data model, public API, vendor, network topology)
- The decision sets a precedent others will copy

Skip ADR for reversible team-local choices; use a short RFC in `senior-software-engineer` instead.

## Template

```markdown
# ADR-NNN: [Short title]

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Date:** YYYY-MM-DD
**Deciders:** [names/roles]

## Context

What forces the decision? Include constraints and prior art.

## Decision

We will [clear statement]. Because [primary reason].

## Consequences

### Positive
- ...

### Negative / trade-offs
- ...

### Risks and mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|

## Alternatives considered

### [Alternative A]
- Pros: ...
- Cons: ...
- Why rejected: ...

## Compliance with principles

Reference org principles (e.g., prefer managed services, event-first for async).

## Follow-up

- [ ] Tasks, owners, dates
- [ ] Metrics to validate decision in production
```

## Quality bar

Reject or send back ADRs that:

- Recommend without comparing alternatives
- Omit operational ownership (who runs it at 3 a.m.)
- Ignore security, cost, or migration
- Use "best practice" without tying to constraints

Supersede; do not silently edit accepted ADRs—link forward to the new record.
