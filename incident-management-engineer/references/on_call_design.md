# On-call design

## Table of contents

1. [Rotation patterns](#rotation-patterns)
2. [Handoff template](#handoff-template)

## Rotation patterns

| Pattern | Pros | Cons |
|---|---|---|
| Weekly primary + secondary | Predictable; deep context | Long week for primary |
| Follow-the-sun | Global coverage | Handoff complexity |
| Team pool | Spreads load | Weaker service ownership |

Rules:

- Secondary must be able to page primary’s manager if no ack
- Limit pages from non-production environments
- Comp time or rotation fairness reviews monthly

## Handoff template

```markdown
## On-call handoff — [date]
### Open incidents (ID, SEV, owner, next step)
### Deploys / changes last 24h
### Flapping or noisy alerts
### Known risks this week
```
