# System design

## Table of contents

1. [RFC outline](#rfc-outline)
2. [Service boundaries](#service-boundaries)
3. [Consistency](#consistency)

## RFC outline

```markdown
# [Title]
## Context
## Goals / Non-goals
## Options
### Option A — pros/cons
### Option B — pros/cons
## Decision
## Interfaces (API, events, schema)
## Risks and mitigations
## Rollout
## Open questions
```

## Service boundaries

| Signal to split | Signal to keep together |
|---|---|
| Different scaling needs | Same transaction boundary |
| Different release cadence | High chatty coupling |
| Team ownership | Premature microservices |

Prefer modular monolith until proven pain.

## Consistency

| Need | Pattern |
|---|---|
| Strong invariants | Sync API + DB transaction |
| Cross-service | Saga / outbox + idempotent consumers |
| Read scale | CQRS read replicas; accept lag |

Document failure: partial completion, duplicate delivery, ordering.
