# Canonical models and transformations

## Table of contents

1. [Canonical model](#canonical-model)
2. [Anti-corruption layer](#anti-corruption-layer)
3. [Mapping and validation](#mapping-and-validation)
4. [iPaaS and ESB patterns](#ipaas-and-esb-patterns)
5. [Reconciliation](#reconciliation)

## Canonical model

A **canonical model** is the organization’s agreed shape for an entity (e.g., `Order`, `Shipment`, `Party`) independent of any one system’s quirks.

Principles:

- Name fields for **business meaning**, not source column names
- Use **explicit types** (money as amount + currency, address as structured object)
- Version canonical schemas (`order.v2`) separately from API path versions
- Keep **identifiers** stable across systems (`globalCustomerId`, `partnerOrderId`)

Publish canonical schemas (JSON Schema, Avro, Protobuf) in a registry when multiple teams consume them.

## Anti-corruption layer

Place an **ACL** between external/partner models and internal domain models:

```
Partner payload → ACL validate/map → Canonical → Domain service
Domain event    → ACL map          → Partner format → Gateway
```

ACL responsibilities:

- Translate enums and code lists (partner SKU → internal SKU)
- Reject or quarantine invalid payloads before domain logic
- Hide legacy quirks from core services (fixed-width codes, nullable sentinels)

Do not leak partner field names into core domain entities.

## Mapping and validation

| Stage | Checks |
|---|---|
| Syntax | JSON/XML parse, required fields, types |
| Schema | JSON Schema / Avro compatibility |
| Business | Cross-field rules, referential checks |
| Authorization | Scopes, tenant, partner ID |

Implement transforms as **testable units** with golden files per partner profile.

For EDI segment/loop mapping after canonical exists → `edi-engineer`.

## iPaaS and ESB patterns

| Approach | Strengths | Watch-outs |
|---|---|---|
| **Hub (ESB/iPaaS)** | Central visibility, adapter catalog | Bottleneck, team skill concentration |
| **Choreography** | Team autonomy, scalable ownership | Contract drift without governance |
| **Hybrid** | Hub for partners; mesh internal | Clear rules on what flows through hub |

**Orchestration (hub):** visual flows, centralized error queues—good for many SaaS adapters.

**Choreography (events):** domain events between services—good for high-scale internal domains.

Document **which flows must use the hub** (e.g., all B2B ingress) vs **mesh-only** (internal high-volume).

## Reconciliation

When sync and async paths coexist:

- Define **reconciliation jobs** (compare counts, checksums, last-modified)
- Log **discrepancy cases** with correlation ID and payload hash
- Provide operator UI or report for unmatched records

Idempotency and outbox patterns → `references/event_driven_and_reliability.md`.
