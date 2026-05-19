# Rollout plan

## Table of contents

1. [Phase template](#phase-template)
2. [Rollout patterns](#rollout-patterns)
3. [Rollback](#rollback)
4. [Communication](#communication)

## Phase template

```markdown
## Phase N — [Name]
**Goal:**
**Exit criteria:**
**Initiatives:** [IDs from backlog]
**Owners:**
**Timeline:**
**Budget impact (est.):**
**Eval window:**

### Week-by-week
| Week | Deliverable |
|---|---|
| 1 | |
```

Phase 0 (instrumentation) is mandatory unless attribution already exists.

## Rollout patterns

| Pattern | Use when |
|---|---|
| **Feature flag** | Per-surface optimization |
| **Tenant tier** | Enterprise keeps quality, free tier tighter caps |
| **Model route %** | Gradual router traffic shift |
| **Prompt version** | Registry with instant rollback |
| **Dark launch** | Measure tokens without user-visible change |

Pair with `deployment-strategist` for customer-visible behavior changes.

## Rollback

Per initiative define:

| Trigger | Action |
|---|---|
| Golden eval drop >X% | Revert prompt version / flag off |
| Safety failure | Immediate revert + incident |
| Cost flat but complaints up | Revert; re-analyze traces |

Keep **previous prompt + model pins** for 30 days minimum.

## Communication

| Stakeholder | Message |
|---|---|
| Product | Quality guardrails and UX trade-offs |
| Support | What might look "shorter" or different |
| Finance | $ trajectory vs plan |
| Legal/risk | If retention or logging changes |

After plan delivery, transfer steady-state to `ai-lead-ops` cost review ritual.
