# Improvement backlog

## Table of contents

1. [Initiative card](#initiative-card)
2. [Scoring](#scoring)
3. [Dependencies](#dependencies)
4. [Anti-patterns](#anti-patterns)

## Initiative card

```markdown
### [ID] Title
**Category:** prompt | context | model | RAG | agent | infra
**Owner:**
**Problem:** [which driver from audit]
**Change:** [one paragraph]
**Assumptions:** e.g. 40% of input is duplicate system text
**Est. savings:** X% tokens or $Y/mo (range low–high)
**Effort:** S | M | L
**Quality risk:** Low | Med | High
**Evals required:** [golden-ids], safety subset
**Metrics:** primary KPI + guardrail KPI
**Rollback:** [trigger and action]
**Status:** proposed | in progress | shipped | reverted
```

## Scoring

**Priority score** (higher = do first):

```
score = (impact_1to5 * confidence_1to5) / effort_1to5
```

| impact | guidance |
|---|---|
| 5 | >15% of total spend addressable |
| 3 | 5–15% |
| 1 | <5% |

| confidence | guidance |
|---|---|
| 5 | Measured on traces |
| 3 | Industry benchmark or partial sample |
| 1 | Hypothesis only — spike first |

Cap **in-flight** high-risk (quality med+) initiatives to avoid eval thrash.

## Dependencies

Common chains:

- Instrumentation (phase 0) before attribution-based cuts
- Prompt version registry before A/B cost tests
- Eval harness before model downgrade
- Context compression after golden eval baseline frozen

Draw dependency graph for phase 2+ items.

## Anti-patterns

- Cutting output max_tokens without format eval → broken JSON
- Removing safety instructions to save tokens → `ai-redteam` regression
- Optimizing staging only while prod prompts diverge
- Savings claimed without before/after measurement window
