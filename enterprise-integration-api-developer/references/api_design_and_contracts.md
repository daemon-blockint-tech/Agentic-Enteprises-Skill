# API design and contracts

## Table of contents

1. [REST design](#rest-design)
2. [GraphQL boundaries](#graphql-boundaries)
3. [Versioning](#versioning)
4. [OpenAPI and AsyncAPI](#openapi-and-asyncapi)
5. [Errors and pagination](#errors-and-pagination)

## REST design

- Use **nouns** for resources; HTTP methods express intent
- Prefer **stable resource IDs** (UUID, partner-scoped keys)—not auto-increment across partners
- Support **filtering, sorting, sparse fieldsets** for list endpoints; cap page size
- Use **202 Accepted** for async work; return `Location` or job ID for status polling
- Document **idempotency** via `Idempotency-Key` header on unsafe retries

## GraphQL boundaries

Use GraphQL when:

- Many clients need different field shapes on the same aggregate
- A BFF aggregates multiple backends with strict auth per field

Avoid GraphQL when:

- Partner B2B expects simple REST + OpenAPI and long-term stability
- Heavy batch export or file semantics dominate

Enforce **depth limits**, **query cost**, and **persisted queries** for public/partner APIs.

## Versioning

| Strategy | Use when | Notes |
|---|---|---|
| URL path (`/v2/`) | Partner APIs; clear cutover | Easiest for external consumers |
| Header (`Accept-Version`) | Internal services | Keeps URLs clean |
| Schema evolution (events) | Async contracts | Additive fields; compatible readers |

Rules:

- **Additive** changes only in minor versions
- Breaking changes require **new major** + sunset on old major
- Publish **changelog** and consumer notification lead time

## OpenAPI and AsyncAPI

**OpenAPI (REST):**

- Single source of truth in repo; generate server stubs or client SDKs as needed
- Include `examples`, `description`, security schemes, and standard error responses
- Lint with Spectral or equivalent in CI

**AsyncAPI (events):**

- Document channels, payloads, headers (correlation, trace, schema version)
- Bind to actual broker (Kafka, SNS/SQS, etc.) in deployment config—not only prose

**Contract testing:**

- Provider verifies published contract; consumers run pact-style or schema tests in CI
- Fail build on breaking diff without explicit approval label

## Errors and pagination

Standard error body (problem+json or org standard):

```json
{
  "type": "https://api.example.com/errors/validation",
  "title": "Validation failed",
  "status": 400,
  "detail": "shipTo.postalCode is required",
  "instance": "/v1/orders/req-abc",
  "correlationId": "550e8400-e29b-41d4-a716-446655440000"
}
```

Pagination:

- Cursor-based for large, live datasets; offset only for small admin UIs
- Return `next` link or cursor token; document max page size

For enterprise-wide architecture review → `senior-system-architecture`.
