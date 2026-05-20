# Consolidation, Risk, and Recommendations

## Risk hotspot taxonomy

| Category | Example finding | Typical owner |
|---|---|---|
| **Availability** | Tier-0 without SLO or traces | SRE + service team |
| **Coupling** | 6-hop sync chain on checkout | Architecture + service teams |
| **Data integrity** | Two writers on `orders` table | Data + owning service |
| **Security** | Shared admin SA across 12 deploys | Security + platform |
| **Operability** | Monthly manual failover drill | SRE |
| **Cost** | 40 low-traffic services, shared cluster | Platform + FinOps |
| **Compliance** | PII in logs without retention policy | Security + compliance-engineer |

## Blast-radius analysis

For tier-0/1 paths:

1. Trace **failure propagation** (sync retries, circuit breakers absent?).
2. List **shared infrastructure** (DB, cache, broker cluster, identity provider).
3. Identify **secrets** reused across services.
4. Score **maximum concurrent impact** (users affected, $ at risk if known).

Output: top 5 **shared-fate** nodes with mitigation options (isolate, replicate, degrade gracefully).

## Consolidation candidates

Recommend merge or retire when evidence shows:

| Evidence | Recommendation type |
|---|---|
| Always co-deployed, shared DB, single team | Merge into one service |
| Zero traffic 90d, no compliance hold | Retire with deprecation plan |
| Duplicate capability (two notification services) | Consolidate behind facade |
| BFF + microservice with 1:1 mapping and no autonomy | Collapse or justify split |

Each item needs: **effort** (S/M/L), **risk**, **dependencies**, **rollback**.

## Strangler and decomposition triggers

| Trigger | Suggested next step |
|---|---|
| Monolith module with highest change frequency | Strangler slice research → `microservice-researcher` |
| Team ownership dispute on shared module | Context map workshop |
| Scaling bottleneck isolated to one aggregate | Extract service with clear data ownership |

Analyst defines **where** to cut; researcher defines **how** and options.

## Recommendation record template

```markdown
## REC-001: [Short title]
- **Type:** consolidate | retire | decouple | observability | security
- **Services affected:** ...
- **Evidence:** [metric, graph edge, incident ID, contract diff]
- **Impact if unaddressed:** ...
- **Proposed action:** ...
- **Effort:** S/M/L | **Risk of change:** low/med/high
- **Owner:** team | **Dependencies:** REC-00x
- **Success metric:** ...
```

## Prioritization matrix

|  | Low effort | High effort |
|---|---|---|
| **High impact** | Do now | Plan quarter |
| **Low impact** | Backlog | Defer / reject |

Impact = customer/revenue/availability/security; adjust weights with stakeholders.

## Executive summary (1 page)

1. **Estate snapshot** — service count, tier-0 count, map thumbnail
2. **Top 5 risks** — one line each with evidence pointer
3. **SLO/observability gap** — % tier-0 with full coverage
4. **Contract drift** — count of breaking/unknown consumers
5. **90-day focus** — 3–5 REC items with owners
6. **Explicit non-goals** — what this analysis did not cover

## Program sequencing

Typical order:

1. Inventory + dependency map (facts)
2. Tier-0 SLO and critical-path traces (visibility)
3. Contract drift on external and payment paths (stability)
4. Shared DB and sync-chain remediation (architecture debt)
5. Consolidation/retire quick wins (cost/toil)

## Peer handoffs

| Finding | Skill |
|---|---|
| Boundary options for split/merge | `microservice-researcher` |
| Implement extraction or merge | `senior-software-engineer` |
| SLO/error budget program | `site-reliability-engineer` |
| Load test before/after cutover | `performance-engineer` |
| Cutover planning | `deployment-strategist` |
| Estate-wide ADR approval | `senior-system-architecture` |
