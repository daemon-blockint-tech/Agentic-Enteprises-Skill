# Microservices developer scope

## Table of contents

1. [Role focus](#role-focus)
2. [Typical deliverables](#typical-deliverables)
3. [Decision boundaries](#decision-boundaries)
4. [Anti-patterns](#anti-patterns)

## Role focus

| In scope | Out of scope (peer skills) |
|---|---|
| Service boundaries, bounded contexts, API design between services | Org SLO program and error-budget policy → `site-reliability-engineer` |
| gRPC/REST/events, sync vs async tradeoffs | K8s cluster ops, Helm platform → `platform-engineer`, `cluster-deployment-engineer` |
| Resilience: timeout, retry, breaker, bulkhead | Enterprise iPaaS, canonical hub, B2B gateway programs → `enterprise-integration-api-developer` |
| DB-per-service, saga/outbox at practical depth | Monolith feature delivery → `senior-software-engineer` |
| Twelve-factor services, health, graceful shutdown | CI/CD YAML and GitOps only → `devops` |
| Trace/log/metric propagation, contract testing | Load-test profiling → `performance-engineer` |
| API versioning behind gateway/mesh | Classified promotion and ATO → `classified-software-devsecops-engineer` |

## Typical deliverables

- Context map and service catalog (name, owner, SLA tier)
- Sequence diagrams for critical cross-service flows
- OpenAPI, protobuf, or event schema with compatibility rules
- Resilience matrix per downstream dependency
- Data ownership matrix (system of record, read models, caches)
- Contract-test plan (provider/consumer, Pact or schema-diff in CI)

## Decision boundaries

**Split a service when:**

- Different scaling or availability profiles (e.g., read-heavy catalog vs write-heavy orders)
- Independent release cadence and team ownership
- Clear bounded context with stable ubiquitous language
- Regulatory or blast-radius isolation

**Keep together when:**

- High-frequency chatty calls with shared transactions
- No stable domain seam; split would only add latency
- Team cannot operate two deployables safely yet

## Anti-patterns

- **Distributed monolith** — many services, one shared database, coordinated deploys
- **Synchronous chains** — A→B→C→D on user-facing path without budgets
- **Leaky ownership** — multiple writers to the same tables
- **Retry storms** — retries without jitter on overloaded dependencies
- **Contractless coupling** — breaking schema changes without consumer notice
