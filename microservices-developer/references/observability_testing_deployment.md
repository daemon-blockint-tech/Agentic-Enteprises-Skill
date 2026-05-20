# Observability, testing, and deployment

## Table of contents

1. [Observability](#observability)
2. [Testing strategy](#testing-strategy)
3. [Twelve-factor deployment](#twelve-factor-deployment)
4. [API versioning and rollout](#api-versioning-and-rollout)

## Observability

**Three pillars per service:**

| Signal | Minimum |
|---|---|
| Logs | Structured JSON; `trace_id`, `span_id`, `service`, `level`; no secrets |
| Metrics | RED: rate, errors, duration; saturation (pool, queue) |
| Traces | W3C `traceparent` propagated on HTTP/gRPC and message headers |

**Dashboards:** one row per service SLO; dependency health; breaker state if exposed.

**Alerts:** user-journey burn rate, not only CPU; page on missing heartbeats for critical workers.

Trace and SLO program design → `site-reliability-engineer`. Pipeline metrics → `devops`.

## Testing strategy

| Layer | Focus |
|---|---|
| Unit | Domain logic, adapters mocked |
| Integration | DB, broker testcontainers; outbox relay |
| Contract | Provider verifies published schema; consumer expectations in CI |
| E2E | Few critical journeys; environment-specific |

**Contract testing (conceptual):**

- **Consumer-driven contracts** — consumer defines expected interactions; provider verifies before release
- **Schema registry** — Avro/Protobuf/JSON Schema compatibility checks (`BACKWARD`, `FULL`)
- **Breaking change gate** — diff OpenAPI/proto in PR; fail on incompatible without major version

**Test doubles for dependencies:** use wire mocks or test containers; avoid shared staging for unit-level contracts.

## Twelve-factor deployment

| Factor | Microservice practice |
|---|---|
| Codebase | One repo per service (or mono-repo with clear module boundaries) |
| Dependencies | Lockfiles; reproducible images |
| Config | Env vars / secret store; no config in image |
| Backing services | Attach DB, cache, broker via URLs from config |
| Build, release, run | Immutable image digest; separate build and deploy |
| Processes | Stateless workers; scale horizontally |
| Port binding | Export health on `/healthz` (liveness) and `/readyz` (readiness) |
| Concurrency | Scale process count; respect bulkheads |
| Disposability | Graceful shutdown: drain in-flight, stop consumers |
| Dev/prod parity | Same container locally and in prod |
| Logs | stdout; aggregate centrally |
| Admin processes | One-off jobs as separate Job/Cron, not SSH |

Container build and promotion gates → `devops`, `build-validator`.

## API versioning and rollout

| Strategy | Guidance |
|---|---|
| URL path (`/v1/`) | Obvious; easy routing at gateway |
| Header negotiation | Cleaner URLs; requires discipline |
| Parallel deploy | Run v1 and v2; route by gateway rule |
| Deprecation | `Sunset` header + metrics on v1 traffic; remove when near zero |

**Backward compatible changes:** add optional fields, new endpoints; never rename or change type in place.

**Rollout:** blue/green or canary at gateway/mesh; feature flags inside service for risky logic.

Cutover planning and change tiers → `deployment-strategist`.
