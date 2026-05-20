# Enterprise integration and API scope

## Table of contents

1. [Role boundaries](#role-boundaries)
2. [Integration styles](#integration-styles)
3. [Scoping checklist](#scoping-checklist)
4. [Deliverable boundaries](#deliverable-boundaries)

## Role boundaries

| In scope | Out of scope (route elsewhere) |
|---|---|
| REST/GraphQL API design, OpenAPI/AsyncAPI | X12/EDIFACT segments and VAN/AS2 EDI → `edi-engineer` |
| Event buses, webhooks, outbox, idempotency | Pure OR solver / VRP math → `operations-research-algorithm-developer` |
| Canonical models, ACL, transformation | Generic app features without integration → `senior-software-engineer` |
| API gateway, B2B partner APIs, OAuth/mTLS | Classified pipeline-only promotion → `classified-software-devsecops-engineer` |
| Correlation, tracing hooks, DLQ patterns | CI/CD YAML and GitOps mechanics → `devops` |
| Versioning, deprecation, compatibility | Cloud landing zone / VPC design → `cloud-engineer` |

Revalidate scope when a request is **only** deploy scripts, **only** EDI segments, or **only** solver formulation.

## Integration styles

| Style | When to use | Risks |
|---|---|---|
| **Synchronous API** | Query/command with immediate feedback; low fan-out | Coupling, cascading latency, retry storms |
| **Async messaging** | Decouple teams; absorb spikes; audit trail | Ordering, duplicates, operational complexity |
| **Webhook / callback** | Partner pushes events; SaaS integrations | Signature verification, replay, timeout handling |
| **Batch / file drop** | Large payloads; legacy ERP; scheduled sync | Late data, partial files, reconciliation |
| **iPaaS / ESB hub** | Many adapters; visual ops; centralized governance | Bottleneck, single team dependency |
| **Choreographed events** | Autonomous services; domain events | Distributed debugging without standards |

Document the **system of record** per entity (order, customer, inventory) and whether integration is **read**, **write**, or **bidirectional**.

## Scoping checklist

1. **Stakeholders** — product owners, partner ops, security, SRE, data governance
2. **Trust zones** — internet partner, corporate DMZ, internal mesh, batch zone
3. **Channels** — REST, GraphQL, Kafka/SQS/SNS, webhook, SFTP (hand off file semantics to owning team)
4. **Volume** — peak TPS, payload size, burst vs steady, retention
5. **Latency SLO** — sync p99, async max delivery delay, partner SLA
6. **Consistency** — strong vs eventual; acceptable duplicate handling
7. **Compliance** — PII fields, residency, audit log requirements
8. **Lifecycle** — MVP cutover, dual-write period, deprecation horizon

## Deliverable boundaries

Produce artifacts appropriate to phase:

| Phase | Typical outputs |
|---|---|
| Discover | Context diagram, interface inventory, risk list |
| Design | ADR, OpenAPI/AsyncAPI draft, canonical model sketch |
| Build | Mappers, gateway config, contract tests, idempotency store |
| Operate | Runbooks, dashboards, DLQ playbooks, partner comms templates |

Do not embed secrets, production URLs, or partner credentials in skill outputs or reference examples.
