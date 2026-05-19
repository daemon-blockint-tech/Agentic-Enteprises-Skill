# Cost and capacity

## Table of contents

1. [Unit economics](#unit-economics)
2. [Optimization levers](#optimization-levers)

## Unit economics

```
cost_per_session = (input_tokens * in_price + output_tokens * out_price) / sessions
```

Segment by feature, model, tenant tier.

## Optimization levers

| Lever | Owner skill |
|---|---|
| Model routing | ai-engineer |
| Prompt caching | ai-context-engineer |
| Memory write less | ai-memory-developer |
| Retrieval top-k | ai-engineer |

Review weekly; target gross margin per product line.
