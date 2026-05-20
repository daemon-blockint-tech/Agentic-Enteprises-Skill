# Coupling and Data Ownership

## Coupling types (assess existing estate)

| Type | Symptoms | Typical risk |
|---|---|---|
| **Integration** | Chatty sync RPC, no timeouts, retry storms | Latency cascades, incident blast radius |
| **Data** | Multiple services write same tables/schema | Integrity bugs, undeployable changes |
| **Temporal** | Hidden ordering assumptions across events | Race bugs, duplicate processing |
| **Deployment** | Must release A+B+C together | Slow delivery, rollback complexity |
| **Operational** | Shared runbooks, shared secrets, shared queues | Shared fate on outages |

## Shared-database smell checklist

Flag when **two or more** services:

- Write to the same relational schema or collection
- Share ORM models across repos
- Use DB views as integration API
- Bypass service APIs with direct SQL from another team's job

**Document:** which team owns the schema, migration process, and who approves cross-service queries.

## Data ownership matrix

| Aggregate / entity | System of record | Allowed readers | Integration style |
|---|---|---|---|
| Order | order-service | billing (read API), analytics (CDC) | API + outbox |
| Customer profile | identity-service | CRM (event) | async only |

Gaps (no single writer) are **P1 architecture debt** until resolved or explicitly accepted.

## Cyclic dependency detection

Cycles in sync call graphs (A→B→C→A) block independent deployment. Mitigations to recommend (not implement here):

- Introduce async boundary or read model
- Collapse cycle into one deployable temporarily
- Extract shared kernel with strict versioning

## Library and platform coupling

| Pattern | Assessment |
|---|---|
| Shared internal SDK with business logic | Hidden coupling; version skew risk |
| Copy-paste DTOs across services | Contract drift |
| Central "utils" repo imported everywhere | Release bottleneck |

Recommend **contract-first** artifacts (OpenAPI, events) over shared business libraries when drift is observed.

## Change-risk scoring (lightweight)

| Factor | Weight |
|---|---|
| Tier-0/1 on critical path | High |
| Fan-in > 5 services | High |
| Shared DB writer count > 1 | High |
| No contract tests | Medium |
| Deploy frequency < monthly | Medium |

Use scores to order remediation backlog—not as precise math.

## Consolidation vs decomposition signals

**Consolidate candidate** when:

- Services always deploy together, share DB, low independent value
- Operational cost (on-call, pipelines) exceeds benefit of separation

**Decompose candidate** when:

- Single service owns unrelated aggregates with conflicting change rates
- Team cognitive load or incident frequency concentrated in one repo

Hand detailed boundary design to `microservice-researcher` after identifying the candidate.

## Evidence to attach

- Call graph screenshot or export
- Schema ownership doc or migration history
- Incident tickets citing cross-team DB changes
- Deploy correlation (services released in lockstep)
