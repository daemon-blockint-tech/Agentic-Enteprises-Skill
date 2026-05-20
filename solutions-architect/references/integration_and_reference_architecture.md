# Integration and reference architecture

## Table of contents

1. [Architecture views](#architecture-views)
2. [Integration patterns](#integration-patterns)
3. [Interface design](#interface-design)
4. [Data and identity](#data-and-identity)
5. [Reference architecture templates](#reference-architecture-templates)
6. [Review checklist](#review-checklist)

## Architecture views

Produce the minimum set stakeholders need:

| View | Audience | Content |
|---|---|---|
| Context | Executives, security | Systems, actors, external deps |
| Container / logical | IT, delivery | Major deployable units, protocols |
| Integration | Integration teams | APIs, events, files, schedules |
| Deployment | Ops, cloud teams | Regions, networks, managed services |
| Sequence (key flows) | Engineering | Auth, order, sync, failure paths |

Label **as-is** vs **to-be**; show **phase boundaries** (PoC vs production).

Platform landing zones and org guardrails → `cloud-architect`, `enterprise-cloud-architect`.
Internal product C4 and ADRs → `senior-system-architecture`.

## Integration patterns

| Pattern | Use when | Watch-outs |
|---|---|---|
| Synchronous API (REST/GraphQL/gRPC) | Real-time UX, query/ command | Coupling, versioning, timeouts |
| Async messaging (queue/topic) | Decouple, burst, fan-out | Ordering, poison messages, DLQ |
| Event streaming | High volume, multiple consumers | Schema evolution, replay |
| Scheduled batch / ETL | Legacy, large volumes, windows | SLAs, partial failure, monitoring |
| File transfer (SFTP, object) | Partner constraints | Encryption, virus scan, idempotency |
| iPaaS / workflow | Low-code orchestration, SaaS glue | Cost, observability, limits |
| Webhooks / callbacks | SaaS integrations | Signature verification, retries |

Prefer **API-first** contracts with explicit error models and idempotency keys for money- or state-changing operations.

## Interface design

For each integration document:

- **Owner system** and counterpart
- **Protocol** — HTTPS, AMQP, SFTP, etc.
- **Auth** — OAuth2, mTLS, API key (prefer short-lived tokens)
- **Payload** — schema reference or sample; versioning rule
- **SLA** — latency, availability, rate limits
- **Failure behavior** — retries, compensation, manual fallback
- **PII / secrets** — what crosses the boundary

Use an **interface catalog** table; link to OpenAPI/AsyncAPI where they exist or will be created in delivery.

## Data and identity

**Data:**

- System of record per entity
- Direction of sync (master → replica, bidirectional)
- Consistency model (strong, eventual)
- Retention and purge requirements

**Identity:**

- Human vs machine identities
- Federation (SAML/OIDC) vs local accounts
- Authorization model (RBAC, ABAC, scopes)
- Service-to-service (workload identity, client credentials)

Call out **cross-border** data flows early for compliance fit.

## Reference architecture templates

Adapt; do not copy blindly.

**SaaS + enterprise integration**

- IdP federation → app → API gateway → core services
- Webhooks to customer SIEM or ticketing
- Admin APIs behind separate auth and rate limits

**Hybrid (on-prem + cloud)**

- Private connectivity (VPN, ExpressRoute, Direct Connect)
- Identity sync (AD → cloud IdP)
- Strangler: new capability in cloud, legacy via API/queue

**Event-driven domain**

- Ingress API → outbox → message bus → consumers
- Schema registry; dead-letter handling

**Analytics / reporting**

- Operational DB → CDC/stream → lake/warehouse → BI
- Separate network path and role for analysts

Detailed cloud service selection → `cloud-architect`. Implementation → `infrastructure-engineer`, `cloud-engineer`.

## Review checklist

- [ ] Every external system on context diagram has an owner and integration owner
- [ ] Critical flows have sequence diagrams including failure/retry
- [ ] No single unnamed “magic” integration box
- [ ] NFRs traced to components (latency, availability, encryption)
- [ ] PoC scope uses subset of interfaces; production gaps listed
- [ ] Versioning and deprecation strategy stated for public APIs
- [ ] Security review scheduled before customer commitment on custom auth
