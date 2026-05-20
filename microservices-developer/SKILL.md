---
name: microservices-developer
description: |
  Guides microservice design and delivery—bounded contexts, service boundaries, REST/gRPC/event APIs,
  sync vs async tradeoffs, resilience (timeouts, retries, circuit breakers, bulkheads), per-service
  data ownership, saga and outbox patterns, twelve-factor containers, observability (logs, metrics,
  trace propagation), API versioning at gateways/meshes, and contract testing.
  Use for microservices developer, service boundary, bounded context, gRPC between services, circuit
  breaker, saga pattern, outbox pattern, twelve-factor, contract testing microservices, service
  decomposition, or event-driven microservice—not K8s platform ops (platform-engineer,
  site-reliability-engineer), enterprise iPaaS (enterprise-integration-api-developer), monolith-first
  apps (senior-software-engineer), or classified pipelines (classified-software-devsecops-engineer).
---

# Microservices Developer

## When to Use

- Decompose a monolith or greenfield system into **bounded contexts** and service boundaries
- Design **REST, gRPC, or event** contracts between services with clear ownership
- Choose **sync vs async** communication and document failure semantics
- Implement **resilience**—timeouts, retries with jitter, circuit breakers, bulkheads, load shedding
- Enforce **database-per-service** (or schema-per-service) and avoid shared mutable stores
- Apply **saga**, **outbox**, or idempotent consumers for cross-service consistency
- Containerize services with **twelve-factor** config, health checks, and graceful shutdown
- Add **observability**—correlation/trace IDs, RED metrics, structured logs, trace propagation
- Plan **API versioning**, deprecation, and backward compatibility at gateway or mesh edge
- Introduce **contract tests** or consumer-driven contract checks between teams

## When NOT to Use

- Operate Kubernetes clusters, Helm platform add-ons, or cluster SRE only → `platform-engineer`, `cluster-deployment-engineer`
- Define org-wide SLO programs, error budgets, and PRR gates → `site-reliability-engineer`
- Design enterprise iPaaS, canonical enterprise models, or B2B integration hubs → `enterprise-integration-api-developer`
- Build monolith features, general RFCs, or stack-agnostic code review without service split → `senior-software-engineer`
- Implement CI/CD pipelines, GitOps, or release automation only → `devops`
- Provision VPC, managed cloud services, or landing zones → `cloud-engineer`, `infrastructure-engineer`
- Gate production builds and artifact promotion policy → `build-validator`
- Profile p99 latency and run load/soak tests as the main task → `performance-engineer`
- Classified air-gapped pipelines, ATO evidence, cleared promotion → `classified-software-devsecops-engineer`

## Related skills

| Need | Skill |
|---|---|
| General service design, RFCs, refactoring | `senior-software-engineer` |
| Internal developer platform, golden paths | `platform-engineer` |
| SLOs, error budgets, reliability program | `site-reliability-engineer` |
| Enterprise integration, OpenAPI hub, iPaaS | `enterprise-integration-api-developer` |
| CI/CD, GitOps, deploy pipelines | `devops` |
| Cloud networking, IAM, managed services | `cloud-engineer` |
| Terraform modules and core IaC | `infrastructure-engineer` |
| Build gates and promotion validation | `build-validator` |
| Profiling, load tests, latency budgets | `performance-engineer` |
| Cross-system ADRs and NFR sign-off | `senior-system-architecture` |
| Rollout cutover and change tiers | `deployment-strategist` |
| Pipeline SAST, SBOM, supply chain | `devsecops` |

## Core Workflows

### 1. Scope and boundaries

Map domains, define service APIs, and document non-goals.

**See `references/microservices_developer_scope.md` and `references/service_boundaries_and_design.md`.**

### 2. Communication and contracts

Pick sync/async patterns; define schemas, errors, and versioning.

**See `references/communication_sync_async.md`.**

### 3. Resilience and reliability

Apply timeouts, retries, breakers, and failure isolation per dependency.

**See `references/resilience_and_reliability.md`.**

### 4. Data, events, and consistency

Own data per service; use outbox/saga where cross-service invariants matter.

**See `references/data_consistency_and_events.md`.**

### 5. Operate, test, and ship

Observability, contract tests, twelve-factor deploy, gateway compatibility.

**See `references/observability_testing_deployment.md`.**

## Outputs

- **Service map** — contexts, APIs, data ownership, sync/async edges
- **Contract draft** — OpenAPI/proto/event schema with error model and versioning note
- **Resilience table** — per-dependency timeout, retry, breaker, fallback
- **Consistency note** — saga/outbox/idempotency choice with failure compensation
- **Runbook snippet** — health checks, dashboards, rollback triggers

## Principles

- Prefer **fewer, cohesive services** over fine-grained chatter; split on change cadence and team boundaries
- **Fail fast** with explicit timeouts; never unbounded blocking across the network
- **Design for partial failure**—degrade features, do not cascade outages
- **Make contracts testable** before production coupling multiplies
