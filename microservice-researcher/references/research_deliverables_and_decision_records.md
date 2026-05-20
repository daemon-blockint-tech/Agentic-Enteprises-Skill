# Research deliverables and decision records

## Table of contents

1. [Deliverable templates](#deliverable-templates)
2. [Options matrix](#options-matrix)
3. [NFR impact table](#nfr-impact-table)
4. [ADR structure for microservice research](#adr-structure-for-microservice-research)
5. [Literature and pattern comparison](#literature-and-pattern-comparison)
6. [Review and sign-off](#review-and-sign-off)
7. [Handoff to implementation](#handoff-to-implementation)

## Deliverable templates

### Research brief (1–3 pages)

```markdown
## Question
[Decision to make]

## Constraints
[Time, teams, compliance, budget]

## Method
[Workshops, document review, benchmarks, spikes planned]

## Findings (summary)
[3–5 bullets]

## Recommendation
[Chosen option + confidence]

## Open questions
[Items blocking implementation]
```

### Candidate service catalog

| Service | Bounded context | Owns (data/aggregates) | Publishes | Consumes | Team (proposed) |
|---|---|---|---|---|---|
| Example | Ordering | Order aggregate | `order.*` events | Payment API | Stream-aligned Order |

### Context map summary

Attach diagram + table of edges (pattern, contract type, consistency).

## Options matrix

Always include **at least three** rows:

1. **Status quo / modular monolith** (or fewer services)
2. **Recommended split** (or hybrid)
3. **Maximum decomposition** (stress test)

| Criterion | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Time to first value | | | | |
| Operational complexity | | | | |
| Team autonomy | | | | |
| Consistency fit | | | | |
| Latency (critical path) | | | | |
| Cost (build + run) | | | | |
| Reversibility | | | | |

**Weight criteria** with decision owner; show scored totals only if stakeholders want numbers—avoid false precision.

## NFR impact table

Per recommended boundary:

| Capability | Latency target | Availability | RPO/RTO | Observability | Cost driver |
|---|---|---|---|---|---|
| Checkout | p99 < 500ms | 99.95% | RPO 1h | Golden signals + trace | Sync calls × 3 |

Link to `senior-system-architecture` for estate-wide SLO policy; to `high-concurrency-scalability` for load validation plans.

## ADR structure for microservice research

```markdown
# ADR-NNN: [Title]

## Status
Proposed | Accepted | Deprecated

## Context
[Forces and constraints]

## Decision
[What we will do]

## Options considered
### Option 1 — [name]
- Pros / Cons

### Option 2 — [name]
- Pros / Cons

## Consequences
Positive, negative, risks

## Compliance with principles
[Data ownership, team topology, contract policy]

## Follow-up
[Spikes, ADRs, owners, dates]
```

**One-way doors** (hard-to-reverse splits, public partner contracts): require architecture review with `senior-system-architecture`.

## Literature and pattern comparison

Use citations to inform—not replace—context-specific analysis:

| Source | Use in research |
|---|---|
| **DDD** (Evans) | Bounded context, context map, aggregates |
| **Team Topologies** (Skelton & Pais) | Team–service alignment |
| **Building Microservices** (Newman) | Practical boundaries, migration |
| **Enterprise Integration Patterns** (Hohpe & Woolf) | Messaging, routing metaphors |
| **Monolith to Microservices** (Newman) | Strangler, decomposition |
| **SOA / microservices trade-off essays** | Avoid hype; document downsides |

**Comparison table** when stakeholders cite conflicting patterns:

| Pattern | Problem solved | Cost | Fit for this estate |
|---|---|---|---|
| Strangler | Incremental migration | Dual-run complexity | High / Medium / Low |

## Review and sign-off

| Gate | Participants | Exit criteria |
|---|---|---|
| **Research review** | Domain lead, tech lead, architect | Options matrix complete |
| **Security/compliance** | Security architect if PII/regulated | Data flows classified |
| **Implementation kickoff** | Engineering manager | Backlog owned; open questions ≤ agreed |

## Handoff to implementation

Research package should list:

| Artifact | Owner team | Peer skill if needed |
|---|---|---|
| ADR accepted | Architecture / platform | `senior-system-architecture` |
| OpenAPI/AsyncAPI stubs | Service team | `senior-software-engineer` |
| Event catalog outline | Service team | `event-driven-architecture` |
| Strangler routing rules | Platform/edge | `platform-engineer` |
| Cutover runbook | SRE/release | `deployment-strategist` |
| Load test plan | Performance | `high-concurrency-scalability` |

**Definition of done for research:** decision recorded, constraints documented, boundaries drawn, contracts policy set, migration slice #1 defined, NFR table attached, and implementation backlog created with named owners.
