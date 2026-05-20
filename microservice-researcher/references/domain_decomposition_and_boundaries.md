# Domain decomposition and boundaries

## Table of contents

1. [Discovery inputs](#discovery-inputs)
2. [Bounded context heuristics](#bounded-context-heuristics)
3. [Context mapping](#context-mapping)
4. [Service boundary criteria](#service-boundary-criteria)
5. [Granularity trade-offs](#granularity-trade-offs)
6. [Research checklist](#research-checklist)

## Discovery inputs

Gather before drawing services:

| Source | What to extract |
|---|---|
| Event storm / domain workshop | Domain events, commands, aggregates, hot spots |
| User journeys | Consistency needs, read vs write paths, peak flows |
| Existing monolith modules | Coupling, shared tables, release coupling |
| Org structure | Team boundaries (inform, do not dictate) |
| Compliance | Data residency, retention, segregation |
| NFRs | Latency SLO, availability, audit, cost per capability |

Time-box discovery; record **assumptions** when stakeholders are unavailable.

## Bounded context heuristics

A bounded context has:

- **Ubiquitous language** stable within the boundary
- **Models** that need not match other contexts (e.g., `Customer` in Sales vs Support)
- **Autonomous evolution** of rules without negotiating every change globally

**Signals of a separate context:**

- Different **lifecycle** or definition of core entities
- Different **scaling** or availability targets
- **Regulatory** or trust-zone separation
- **Team** can own outcomes without daily sync to another team

**Signals to keep together:**

- Same aggregate enforces invariants across entities
- Frequent **invariant** changes span proposed split
- Read-your-writes required on a single user action with no acceptable lag

## Context mapping

Document relationships between contexts (DDD context map):

| Pattern | Meaning | Research note |
|---|---|---|
| **Partnership** | Mutual dependency; coordinate releases | High coupling—justify |
| **Customer-Supplier** | Downstream depends on upstream roadmap | Define SLA for API/events |
| **Conformist** | Downstream accepts upstream model | Document risk of model drag |
| **Anti-corruption layer (ACL)** | Translate foreign model at boundary | Prefer for legacy/monolith slices |
| **Open host service (OHS)** | Published language for many consumers | Needs strong versioning policy |
| **Shared kernel** | Shared code/data subset | **Minimize**—hidden distributed monolith risk |

Output: diagram + table of **who translates what** at each edge.

## Service boundary criteria

Score each candidate service (1–5) against weighted criteria:

| Criterion | Questions |
|---|---|
| **Cohesion** | Does one team reason about this capability daily? |
| **Coupling** | How many synchronous calls per user journey? |
| **Data ownership** | Single writer per aggregate? |
| **Deploy independence** | Can ship without coordinated multi-repo deploy? |
| **Failure isolation** | Blast radius acceptable if service down? |
| **Operational load** | On-call, dashboards, runbooks affordable? |
| **Consistency** | Can journeys tolerate eventual consistency here? |

**Split when** high cohesion + clear data ownership + deploy independence outweigh ops overhead.

**Merge when** low cohesion or consistency forces distributed transactions.

## Granularity trade-offs

| Finer services | Coarser services |
|---|---|
| Smaller blast radius | Fewer network hops |
| Team autonomy | Simpler operations |
| Targeted scaling | Easier refactoring inside monolith |
| More contracts to govern | Fewer version skew risks |

**Nano-services warning:** research should flag services with <1 meaningful aggregate or no independent lifecycle.

**Modular monolith option:** always include as **Option A** in comparisons when estate is single-team or maturity is low.

## Research checklist

- [ ] Ubiquitous language glossary per context
- [ ] Aggregates identified with single-writer rule
- [ ] Context map with integration pattern per edge
- [ ] Hot paths counted (sync call depth, fan-out)
- [ ] Shared database tables flagged with migration owner
- [ ] At least two boundary options (including fewer services)
- [ ] Team Topologies hypothesis documented (see `migration_strangler_and_org_alignment.md`)
