# API contracts and evolution

## Table of contents

1. [Contract types](#contract-types)
2. [Design-first research outputs](#design-first-research-outputs)
3. [Versioning strategies](#versioning-strategies)
4. [Compatibility matrix](#compatibility-matrix)
5. [Deprecation and sunset](#deprecation-and-sunset)
6. [Governance](#governance)
7. [Research checklist](#research-checklist)

## Contract types

| Contract | Research artifacts | Notes |
|---|---|---|
| **REST/OpenAPI** | Resource model, error model, pagination | Widest tooling; cache semantics |
| **GraphQL** | Schema, federation boundaries if any | BFF vs domain API separation |
| **gRPC/Protobuf** | Package, breaking change rules | Strong typing; mobile/web gateway |
| **AsyncAPI / events** | Event envelope, schema registry policy | Pair with `event-driven-architecture` |
| **CloudEvents** | Metadata fields (type, source, id, time) | Interop across brokers |

Align **public** contracts with bounded context boundaries—no "god API" without explicit aggregation role (BFF).

## Design-first research outputs

Before implementation commitment:

- **Consumer list** — internal, partner, mobile, analytics
- **SLA class** — best-effort vs critical path
- **Error taxonomy** — retryable vs fatal; problem+json or gRPC status mapping
- **Pagination and filtering** — cursor vs offset; max page size
- **AuthZ model** — scopes, claims, service-to-service identity

Produce **contract sketch** (OpenAPI/AsyncAPI fragment) for review—not full implementation.

## Versioning strategies

Compare options in ADR:

| Strategy | Pros | Cons | Fit |
|---|---|---|---|
| **URL path** (`/v1/`) | Obvious | Proliferation of routes | Public partners |
| **Header** (`Accept-Version`) | Clean URLs | Easy to misconfigure | Internal APIs |
| **Media type** | REST purist | Client complexity | Rare |
| **Package/namespace (proto)** | Compile-time checks | Regeneration discipline | gRPC estates |
| **Event schema version** | Decoupled deploy | Consumer lag | Event-driven |

**Research recommendation:** pick **one primary** strategy per surface area; document exceptions.

### Breaking vs non-breaking changes

| Non-breaking (usually) | Breaking (require version bump) |
|---|---|
| Add optional field | Remove or rename field |
| Add endpoint | Change semantics of existing field |
| Add enum value (if clients tolerate unknown) | Tighten validation |
| Add event type | Change partition key |

## Compatibility matrix

Define for APIs and events:

| Direction | Rule | Verification |
|---|---|---|
| **Backward compatible** | New producer, old consumer | Contract tests, schema check |
| **Forward compatible** | Old producer, new consumer | Unknown field tolerance |
| **Full compatible** | Both directions | Rare; version lock |

**Consumer-driven contracts:** research should recommend who runs pact/schema tests and on which cadence.

## Deprecation and sunset

Policy elements:

1. **Announcement** — changelog, portal, email to registered consumers
2. **Dual support window** — minimum duration (e.g., 6–12 months for partners)
3. **Telemetry gate** — zero traffic on old version before removal
4. **Forced migration** — only with executive risk acceptance

Document **sunset criteria** in research memo—not "deprecate when convenient."

## Governance

| Role | Responsibility |
|---|---|
| **Context owner** | Approve breaking changes in their API/event |
| **Architecture forum** | Cross-cutting standards (error model, auth) |
| **Registry** | OpenAPI/AsyncAPI/Proto source of truth |
| **Breaking change board** | Partner-facing changes |

Hand off enterprise-wide API programs to `enterprise-integration-api-developer`.

## Research checklist

- [ ] Public vs internal contract surfaces separated
- [ ] Versioning strategy chosen with examples
- [ ] Compatibility rules stated (backward/forward)
- [ ] Deprecation timeline template attached
- [ ] Error and idempotency conventions referenced
- [ ] Event schemas linked if async boundary exists
- [ ] NFR: rate limits, payload size, timeout documented
