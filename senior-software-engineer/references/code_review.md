# Code review

## Table of contents

1. [Severity labels](#severity-labels)
2. [Review checklist](#review-checklist)
3. [Comment patterns](#comment-patterns)

## Severity labels

| Label | Meaning |
|---|---|
| BLOCKER | Must fix before merge |
| SUGGESTION | Better approach; author decides |
| NIT | Style; optional |
| QUESTION | Clarify intent |

## Review checklist

- [ ] Behavior matches ticket and handles errors
- [ ] Authz on every mutating path
- [ ] No secrets or PII in logs
- [ ] Tests cover failure paths
- [ ] Public API backward compatible or versioned
- [ ] Migrations safe (expand-contract)
- [ ] Observability: log fields, metrics for new paths

## Comment patterns

**Good:** "This retry can double-charge on timeout; use idempotency key or mark BLOCKER."

**Weak:** "Consider refactoring this."

Offer alternative when blocking: snippet or link to pattern.
