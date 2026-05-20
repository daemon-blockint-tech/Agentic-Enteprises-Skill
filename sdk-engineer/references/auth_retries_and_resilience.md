# Authentication, Retries, and Resilience

## Authentication patterns

### API keys

- Send via header name defined in spec (`Authorization`, `X-Api-Key`)—never query string unless API requires it
- Read from environment variable in examples; never log key values
- Support rotation: allow updating provider without reconstructing entire app graph when possible

### OAuth2 (client credentials, authorization code)

- Encapsulate token fetch + refresh in a **credential provider**
- Refresh proactively before expiry (skew 30–60s)
- Serialize refresh to avoid stampedes; surface `AuthenticationError` on failure
- Document required scopes per operation where server enforces scope

### Request signing (HMAC, AWS SigV4-style)

- Canonicalize method, path, query, body hash per server rules
- Clock skew: document NTP requirement; include signing timestamp in errors on failure
- Unit-test vectors from server docs or golden fixtures

### mTLS

- Expose hooks to supply client cert/key or custom TLS context
- Document certificate rotation for long-running services

## Transport defaults

| Setting | Recommended default | Notes |
|---|---|---|
| Connect timeout | 5–10s | Separate from read timeout |
| Read timeout | 30–120s | Per operation class in docs |
| Total deadline | Optional | gRPC: always set |
| Max connections | Pool per host | Document thread-safety |
| Proxy | Respect env `HTTP(S)_PROXY` | Document explicit override |

## Retry policy

### Retry when

- HTTP **408, 429**, **5xx** (if API does not document otherwise)
- gRPC `UNAVAILABLE`, `RESOURCE_EXHAUSTED` (with backoff)
- Network resets, TLS handshake transient failures

### Do not retry when

- **4xx** except 408/429 (unless API documents retryable code)
- Non-idempotent methods **without** idempotency key support
- Business logic errors encoded as 200 with error envelope (map to non-retryable)

### Backoff

- Exponential backoff with **full jitter**
- Cap max attempts (typically 3–5)
- Honor `Retry-After` on 429 when present

```text
delay = min(cap, base * 2^attempt) * random(0.5, 1.0)
```

### Idempotency keys

- Accept `idempotency_key` on create/charge/payment operations when server supports
- Generate UUID v4 if caller omits; document collision behavior
- Retries must **reuse** same key for same logical operation

## Timeouts and cancellation

- Propagate cancellation (context, AbortSignal, asyncio cancel)
- Document that cancel does not guarantee server-side abort unless API supports it
- On cancel, do not retry unless caller explicitly opts in

## Error taxonomy

Map wire errors to a small hierarchy:

| Type | Retryable | Caller action |
|---|---|---|
| `AuthenticationError` | No | Refresh credentials |
| `PermissionError` | No | Fix scopes |
| `NotFoundError` | No | Fix ID |
| `ValidationError` | No | Fix request |
| `RateLimitError` | Yes (after delay) | Backoff |
| `ServerError` | Yes (bounded) | Retry or escalate |
| `NetworkError` | Often yes | Check connectivity |

Include when available:

- HTTP status / gRPC code
- Server `error_code` string
- `request_id` / trace id
- Raw body attachment for support (redact secrets)

## Circuit breaking (optional)

- Expose optional breaker hook—not mandatory in v1 SDKs
- When integrated: open after error rate threshold; half-open probe
- Document interaction with retries (retry inside breaker only when appropriate)

## Logging and secrets

- Log method, path template, status, latency, request id—**not** bodies with secrets
- Provide debug mode that redacts `Authorization` and signed headers
- Never include tokens in exception messages

## Testing resilience

- Table-driven tests for retry counts and backoff timing (inject clock)
- Simulate 429 with `Retry-After`
- Verify no retry on 400/401/403/404
- Verify idempotency key stable across retries

## Defaults documentation template

Ship a **Defaults** section in README:

```markdown
## Defaults
- Connect timeout: 10s
- Read timeout: 60s
- Retries: 3 attempts on idempotent GET/HEAD and on 429/5xx with jitter
- POST retries: disabled unless `idempotency_key` is set
```
