# API Contracts and Client Modeling

## Source of truth

| Style | Primary artifact | SDK implication |
|---|---|---|
| REST | OpenAPI 3.x | codegen + hand layer; respect `operationId` |
| GraphQL | Schema SDL | typed operations; document nullable vs required |
| gRPC | `.proto` | stubs + wrappers; package versioning |
| RPC JSON | Schema docs / examples | manual models; strict validation |

**Rule:** Server behavior wins over stale specs—file spec bugs upstream; do not encode undocumented server quirks without explicit versioning.

## OpenAPI-first workflow

1. Pin spec URL or commit hash in SDK repo
2. Run codegen (optional) into `generated/` namespace
3. Add **hand-written** public types that hide generated noise
4. Diff spec on CI; fail on breaking changes unless major SDK bump planned
5. Map `components.schemas` to resource classes; avoid anonymous nested objects in public API

### Naming

- Use **stable business names** (`Customer`, `Invoice`) not path segments (`V1CustomersPost`)
- Prefer verbs on client services: `customers.create`, `invoices.list`
- Align enum names with server; document unknown enum handling (`UNSPECIFIED`, string fallback)

### Request builders

Expose optional fields via builders or keyword args—not positional lists of 12 parameters.

```text
client.invoices.create(
  customer_id="cus_123",
  amount=1000,
  currency="usd",
  idempotency_key="idem-uuid",  # when supported
)
```

### Response modeling

- Distinguish **full resource** vs **summary** types when OpenAPI uses different schemas
- Parse dates as language-native instants with explicit timezone policy (UTC default)
- Represent money as integer minor units + currency code unless API uses decimal strings (document parsing)

## GraphQL client modeling

- Colocate operations with types; avoid mega-query strings in consumer apps
- Expose `variables` objects; validate required variables before network call
- Handle `errors[]` + partial `data` per GraphQL spec
- Support persisted query hashes only when server documents them

## gRPC modeling

- Set **deadlines** per call; document default deadline on client
- Map `metadata` for auth tokens and trace propagation
- Wrap streaming iterators with cancellation tied to context/deadline
- Keep proto package version aligned with server deployment matrix

## Configuration object

Single entry point:

| Field | Purpose |
|---|---|
| `base_url` / `endpoint` | Environment override |
| `credentials` | Pluggable provider |
| `timeout` | Per-request or default |
| `retry_policy` | Optional; off by default for mutations |
| `user_agent` | SDK name + version |
| `http_client` | Injectable transport for tests |

## Escape hatches

Provide `raw_request` / low-level access for:

- Beta endpoints not yet in spec
- Custom headers required by support
- Debugging with exact wire format

Document that escape hatches are **not covered** by semver guarantees.

## Multi-language considerations

| Concern | Go | TypeScript | Python | Java |
|---|---|---|---|---|
| Nullability | pointers | `undefined` vs `null` | `Optional` | `Optional` |
| Async | context | Promise | async/await | CompletableFuture |
| Packaging | module path | `exports` field | wheel tags | Maven coordinates |
| Naming | idiomatic Go | camelCase public | snake_case | camelCase |

Parity does not require identical names—require **identical semantics** (auth, retries, error codes).

## Contract drift detection

- CI job: fetch spec, diff against pinned version
- Breaking: removed operation, required field added to request, enum value removed
- Non-breaking: new optional field, new operation, new enum value (if clients tolerate unknowns)

## Review checklist

- [ ] Every public method maps to documented server operation
- [ ] Required auth documented per operation (security schemes in OpenAPI)
- [ ] List operations return iterator/paginator, not opaque next-page token only
- [ ] Unknown JSON fields preserved or ignored per language convention (document which)
