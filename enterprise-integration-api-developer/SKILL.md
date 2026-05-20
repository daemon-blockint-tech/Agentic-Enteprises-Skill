---
name: enterprise-integration-api-developer
description: |
  Guides enterprise integration platforms and APIs—REST/GraphQL versioning, OpenAPI/AsyncAPI,
  event-driven integration (pub/sub, outbox, idempotency, sagas), canonical models and
  anti-corruption layers, iPaaS/ESB orchestration vs choreography, API gateways, OAuth2/OIDC,
  mTLS, B2B partner APIs, transformation, correlation IDs, DLQ patterns, compatibility and
  deprecation. Use for enterprise integration, API developer, integration architect, OpenAPI,
  event-driven integration, API gateway, canonical model, iPaaS, ESB, webhook, idempotent
  consumer, saga pattern, B2B API, API versioning, anti-corruption layer—not EDI X12/EDIFACT
  (edi-engineer), classified air-gapped only (classified-software-devsecops-engineer), OR
  solvers (operations-research-algorithm-developer), generic CRUD (senior-software-engineer).
---

# Enterprise Integration API Developer

## When to Use

- Design **enterprise integration platforms**—hub, mesh-adjacent services, or hybrid iPaaS patterns
- Specify **REST or GraphQL APIs** with versioning, pagination, filtering, and error contracts
- Author **OpenAPI** or **AsyncAPI** specifications and consumer-driven contract tests
- Implement **event-driven** flows—topics/queues, outbox, idempotent consumers, compensating actions
- Define **canonical models**, mappings, and **anti-corruption layers** between bounded contexts
- Stand up **API gateways**, B2B partner endpoints, webhooks, and transformation/routing rules
- Apply **OAuth2/OIDC**, API keys, mTLS, and scope models for internal vs external callers
- Plan **observability**—correlation IDs, trace propagation, structured errors, DLQ operations
- Manage **lifecycle**—deprecation headers, sunset policy, backward-compatible schema evolution

## When NOT to Use

- X12/EDIFACT segment mapping, 997/APERAK, AS2/VAN EDI transport → `edi-engineer`
- Classified air-gapped build, ATO evidence, cleared pipeline promotion only → `classified-software-devsecops-engineer`
- VRP, MIP, scheduling, or solver-based optimization → `operations-research-algorithm-developer`
- Generic application CRUD, UI, or single-service features without integration architecture → `senior-software-engineer`
- CI/CD pipeline YAML, GitOps, and deploy mechanics only → `devops`
- Landing zone, VPC, and managed cloud resource design → `cloud-engineer`
- Enterprise-wide cloud reference architecture and migration roadmap → `cloud-architect`
- Internal developer platform golden paths and portals → `platform-engineer`

## Related skills

| Need | Skill |
|---|---|
| EDI standards, segments, partner certification | `edi-engineer` |
| Application services and code quality | `senior-software-engineer` |
| CI/CD, GitOps, integration service deploy | `devops` |
| Cloud messaging, networking, IAM for integrations | `cloud-engineer` |
| Cloud reference architecture and landing zones | `cloud-architect` |
| IDP, golden paths, paved-road templates | `platform-engineer` |
| Classified DevSecOps and promotion boundaries | `classified-software-devsecops-engineer` |
| OR models, routing, allocation solvers | `operations-research-algorithm-developer` |
| Enterprise architecture ADRs and cross-system review | `senior-system-architecture` |
| Pipeline security and supply chain | `devsecops` |

## Core Workflows

### 1. Scope and integration boundaries

Define systems of record, sync vs async boundaries, partner vs internal surfaces, and non-goals.

**See `references/enterprise_integration_api_scope.md`.**

### 2. API design and contracts

Model resources, errors, versioning, and publish OpenAPI/AsyncAPI with contract tests.

**See `references/api_design_and_contracts.md`.**

### 3. Event-driven reliability

Choose messaging patterns, idempotency keys, outbox, sagas/choreography, and failure handling.

**See `references/event_driven_and_reliability.md`.**

### 4. Canonical models and transformation

Define canonical schemas, ACLs, mapping rules, and validation at ingress/egress.

**See `references/canonical_models_and_transformations.md`.**

### 5. Security, gateways, and governance

Configure gateways, auth, rate limits, partner onboarding, and policy enforcement.

**See `references/security_governance_and_gateways.md`.**

### 6. Operations, observability, and lifecycle

Instrument traces and metrics, operate DLQs, and execute deprecation and compatibility plans.

**See `references/operations_observability_and_lifecycle.md`.**

## Outputs

- **Integration context diagram** — systems, channels, sync/async, trust zones
- **Contract artifacts** — OpenAPI/AsyncAPI, JSON Schema, example payloads, error catalog
- **Mapping spec** — canonical fields, transforms, validation rules, idempotency strategy
- **Runbook** — replay, DLQ drain, partner cutover, rollback, compatibility matrix
- **ADR or decision log** — orchestration vs choreography, versioning, auth model

## Principles

- Prefer **contracts and schemas** over tribal knowledge; test consumers in CI
- Make **idempotency and deduplication** explicit at every external boundary
- Separate **partner (B2B) surfaces** from internal mesh traffic—different auth, SLOs, and change windows
- Design for **observable failures**—correlation ID end-to-end, structured errors, actionable DLQs
- Ship **backward-compatible** changes; document sunsets and give consumers migration time
