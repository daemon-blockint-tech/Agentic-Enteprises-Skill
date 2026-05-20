# SDK Engineer — Scope and Boundaries

## Purpose

Define what an **SDK engineer** owns when delivering API client libraries: contract fidelity, developer experience, resilience defaults, lifecycle management, and testable documentation—not server implementation or unrelated platform work.

## In scope

| Area | Deliverables |
|---|---|
| Contract alignment | OpenAPI/proto-driven models; drift detection vs server |
| Public API design | Resource names, method signatures, config objects |
| Auth integration | API keys, OAuth2, signing hooks, credential refresh |
| Resilience | Timeouts, retries (idempotent only), circuit-breaker hooks |
| Data access | Pagination iterators, streaming helpers, upload/download |
| Errors | Typed exceptions/status mapping, retryability flags |
| Versioning | Semver, deprecation notices, migration guides |
| Distribution | Package metadata, publishing, minimum runtime versions |
| DX | Quickstart, examples, changelog, breaking-change policy |
| Quality | Contract tests, integration tests, mock/fixture strategy |

## Out of scope (route to peers)

| Request | Route |
|---|---|
| Design REST routes and persistence only | `api-development`, `senior-software-engineer` |
| React/Next product UI | `senior-frontend-software-engineer` |
| Backstage, golden paths, IDP | `platform-engineer` |
| Editorial API docs without code | `tech-writer-researcher` |
| Architecture go/no-go without SDK | `build-validator` |
| EDI, iPaaS canonical models at enterprise scale | `enterprise-integration-api-developer` |

## API styles covered

- **REST/HTTP + JSON** — OpenAPI 3.x primary; hand-crafted ergonomic layer on generated stubs when needed
- **GraphQL** — operations, fragments, persisted queries; avoid leaking raw HTTP unless documented
- **gRPC** — protobuf services, deadlines, metadata, streaming RPCs
- **RPC-style JSON** — JSON-RPC, Solana-style RPC, WebSocket subscriptions where applicable

## Engagement phases

### Discover

- Read official spec (OpenAPI, GraphQL SDL, `.proto`)
- Inventory existing SDKs, codegen tooling, and consumer complaints
- Agree target languages and release cadence

### Design

- Publish **SDK API proposal**: naming, config, error model, pagination pattern
- Review with API owners for breaking vs additive changes
- Decide codegen vs hand-written ratio per language

### Build

- Implement core client, auth, errors, pagination
- Add examples and contract test harness
- Wire CI: lint, unit, contract, optional integration

### Maintain

- Track server deprecations; emit client warnings
- Patch security issues in auth/transport promptly
- Measure adoption (download stats, support tickets, time-to-first-call)

## Success criteria

- New integrator completes **first successful call** in &lt;15 minutes using quickstart alone
- Contract tests pass on every PR against pinned spec revision
- Breaking SDK releases ship with migration doc and codemods when feasible
- Error messages expose **request ID** and stable error codes from server contract

## Anti-patterns

- Exposing raw HTTP response as the only return type for all operations
- Global mutable configuration changed implicitly on each call
- Retrying POST without idempotency key support
- Shipping generated code without a thin ergonomic facade
- Documenting endpoints that are not in the published spec

## Handoff checklist

Before marking an SDK release ready:

- [ ] Spec revision ID recorded in SDK release notes
- [ ] Authentication documented with least-privilege scopes
- [ ] Default timeouts documented; retries documented as idempotent-only
- [ ] Pagination example in README for list operations
- [ ] Deprecation warnings for sunsetting API fields
- [ ] CI green: unit + contract (+ integration if credentials available)
