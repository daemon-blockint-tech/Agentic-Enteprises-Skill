# Microservice researcher scope

## Table of contents

1. [Role focus](#role-focus)
2. [Research vs delivery](#research-vs-delivery)
3. [Typical deliverables](#typical-deliverables)
4. [Decision boundaries](#decision-boundaries)
5. [Anti-patterns](#anti-patterns)

## Role focus

| In scope | Out of scope (peer skills) |
|---|---|
| Domain decomposition, bounded contexts, context maps | Production service implementation → `senior-software-engineer`, `microservices-developer` |
| Service boundary options and trade-off analysis | Broker/outbox implementation, stream ops → `event-driven-architecture` |
| Sync vs async, data ownership, consistency at research level | K8s platform, GitOps, cluster lifecycle → `platform-engineer` |
| API/event contract evolution strategy | Cloud landing zone, VPC, IaC modules → `cloud-architect`, `infrastructure-engineer` |
| Strangler migration research, parity criteria, cutover gates | Physical/carrier network design → `network-backbone-architect` |
| Team Topologies alignment with boundaries | Portfolio strategy, operating model → `enterprise-strategist` |
| Build vs buy vs managed for capabilities | Load-test execution and cache tuning → `high-concurrency-scalability` |
| ADRs, options matrices, literature comparison | Estate-wide architecture sign-off only → `senior-system-architecture` |

## Research vs delivery

| Activity | Microservice Researcher | Peer handoff |
|---|---|---|
| Context map and candidate services | ✓ | `senior-system-architecture` for estate ADR |
| Options matrix with NFR columns | ✓ | — |
| Saga/outbox **pattern** choice | ✓ | `event-driven-architecture` for broker/schema/DLQ design |
| OpenAPI/AsyncAPI **policy** | ✓ | `enterprise-integration-api-developer` for enterprise hub |
| Strangler slice definition | ✓ | `deployment-strategist` for cutover runbooks |
| Team topology recommendation | ✓ | `enterprise-strategist` for org redesign |
| PoC or spike to validate boundary | Advisory scope only | Engineering team executes |

**Stop research** when: decision owner accepts recommendation, constraints are stable, and implementation backlog is owned by engineering—with explicit open questions logged.

## Typical deliverables

- **Research brief** — question, constraints, method, sources, recommendation
- **Context map** — bounded contexts, relationships (customer/supplier, ACL, OHS, shared kernel risks)
- **Candidate service catalog** — name, owner team hypothesis, data owned, APIs/events published
- **Integration/consistency note** — per flow: sync/async, consistency, idempotency, failure UX
- **Contract evolution policy** — versioning, compatibility, sunset rules
- **Migration roadmap** — strangler slices, parity checklist, telemetry gates
- **ADR** — options, criteria weights, decision, consequences (see `references/research_deliverables_and_decision_records.md`)

## Decision boundaries

**Favor microservices (or finer boundaries) when research shows:**

- Independent **release cadence** per capability with acceptable contract discipline
- Teams can **own data** end-to-end without constant cross-team transactions
- NFRs differ materially (scale, availability, compliance zone) per capability
- Organizational alignment supports **stream-aligned** ownership

**Favor modular monolith or fewer services when research shows:**

- Domain is still **volatile**—boundaries would churn monthly
- Consistency needs dominate user journeys (**strong consistency** on critical path)
- Operational maturity cannot absorb **distributed failure modes** yet
- Team size cannot support **on-call per service**

**Default stance:** microservices are a **means** (autonomy, scale, isolation)—not an end state. Document why split beats a well-modularized monolith.

## Anti-patterns

- **Org-chart services** — one service per manager without domain cohesion
- **Research without owners** — options matrix with no decision maker or date
- **Distributed monolith research** — many boxes, shared database, coupled deploys labeled "microservices"
- **Skipping NFR column** — boundary choice without latency, ops, or cost estimate
- **Implementation smuggled into research** — framework and broker selection before boundary agreement
- **Infinite discovery** — no time-box; recommend "decide and revisit" when evidence plateaus
