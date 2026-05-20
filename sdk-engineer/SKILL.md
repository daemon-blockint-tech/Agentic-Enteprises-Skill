---
name: sdk-engineer
description: |
  Designs, builds, and maintains client SDKs for HTTP/REST, GraphQL, gRPC, and RPC-style APIs—
  OpenAPI-first contract alignment, resource modeling, authentication (API keys, OAuth, signing),
  retries/timeouts/idempotency, pagination and streaming, error taxonomy, versioning and deprecation,
  multi-language packaging and naming, developer experience (quickstarts, examples), and SDK testing
  (contract and integration) with documentation aligned to API reference.
  Use when the user says SDK engineer, client SDK, build an SDK, API client library, OpenAPI SDK,
  SDK design, SDK versioning, retry policy SDK, pagination client, SDK authentication, or developer
  SDK—not backend API design only (api-development), end-user app UI (senior-frontend-software-engineer),
  generic integration platform patterns (platform-engineer), technical writing without SDK implementation
  (tech-writer-researcher), or pre-flight architecture go/no-go without SDK work (build-validator).
---

# SDK Engineer

## When to Use

- Design or implement **client SDKs** and API client libraries for public or partner APIs
- Align SDK surface area with **OpenAPI**, GraphQL schema, protobuf, or RPC contracts
- Model resources, operations, pagination, streaming, and error types in client code
- Implement **authentication** flows (API keys, OAuth2, HMAC/signing, mTLS hooks)
- Define **retries, timeouts, idempotency keys**, and resilience defaults for SDK users
- Plan **versioning, deprecation**, and multi-language SDK parity (naming, packaging, semver)
- Author **quickstarts, examples**, and SDK docs that match the API reference
- Build **contract tests** and integration tests against sandboxes or recorded fixtures

## When NOT to Use

- Design the **backend API or service** only without a client library → `api-development`, `senior-software-engineer`, `enterprise-integration-api-developer`
- Build **end-user application UI** or product frontends → `senior-frontend-software-engineer`, `fullstack-software-engineer`
- Stand up **internal developer platforms**, golden paths, or portals without SDK product work → `platform-engineer`
- Write **documentation or tutorials** without implementing or evolving an SDK → `tech-writer-researcher`
- Run **pre-flight architecture or build go/no-go** reviews without SDK delivery → `build-validator`

## Related skills

| Need | Skill |
|---|---|
| Backend REST/GraphQL service implementation | `api-development`, `senior-software-engineer` |
| Enterprise integration APIs, AsyncAPI, gateways | `enterprise-integration-api-developer` |
| Internal platform, IDP, paved-road templates | `platform-engineer` |
| API reference prose, IA, style guides | `tech-writer-researcher` |
| Plan/design validation before execution | `build-validator` |
| OpenAPI lint and API design review | `api-design-reviewer` |
| CI gates and artifact promotion | `devops`, `build-validator` |

## Core Workflows

### 1. Scope and contract intake

1. Identify API style (REST, GraphQL, gRPC, JSON-RPC) and **source of truth** (OpenAPI, proto, schema registry)
2. List target languages/runtimes and distribution (npm, PyPI, Maven, Go module, crates.io)
3. Define non-goals (server implementation, CLI-only wrappers, codegen-only with no hand layer)
4. Capture breaking-change policy and minimum supported API version

**See `references/sdk_engineer_scope.md`.**

### 2. Client modeling and public surface

Map contract operations to **idiomatic client types**: resources, services, request builders, and enums.

1. Prefer stable resource-oriented names over raw URL paths in public API
2. Hide transport details; expose optional raw request escape hatches for power users
3. Keep configuration (base URL, credentials, timeouts) on a single client instance
4. Document thread-safety / async model per language

**See `references/api_contracts_and_client_modeling.md`.**

### 3. Auth, resilience, and errors

1. Implement credential providers and token refresh without surprising global state
2. Apply default timeouts; retry only **idempotent** operations with bounded backoff + jitter
3. Map HTTP/gRPC status and error bodies to a **typed error hierarchy** with request IDs
4. Support idempotency keys where the API documents them

**See `references/auth_retries_and_resilience.md`.**

### 4. Pagination, streaming, and large payloads

1. Implement cursor/page iterators that compose cleanly (`for await`, generators, paginators)
2. Support streaming RPC or SSE where the contract requires partial results
3. Avoid buffering unbounded collections; document memory trade-offs

**See `references/pagination_streaming_and_resources.md`.**

### 5. Versioning and compatibility

1. Ship SDK semver independent of API version where possible; document mapping
2. Add deprecation warnings, sunset dates, and migration snippets in release notes
3. Run compatibility suites against N API versions when feasible

**See `references/versioning_and_compatibility.md`.**

### 6. Testing and documentation

1. **Contract tests**: generated or hand-written against OpenAPI/proto examples
2. **Integration tests**: sandbox credentials, VCR/fixtures, or ephemeral environments
3. Align README, quickstart, and reference docs with the official API catalog
4. Publish runnable examples in CI

**See `references/sdk_testing_and_documentation.md`.**

## When to load references

| Topic | Reference |
|---|---|
| Role boundaries and deliverables | `references/sdk_engineer_scope.md` |
| OpenAPI/proto → client modeling | `references/api_contracts_and_client_modeling.md` |
| Auth, retries, timeouts, errors | `references/auth_retries_and_resilience.md` |
| Pagination, streaming, resources | `references/pagination_streaming_and_resources.md` |
| Semver, deprecation, multi-language | `references/versioning_and_compatibility.md` |
| Contract tests, docs, examples | `references/sdk_testing_and_documentation.md` |
