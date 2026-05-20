# Operations, observability, and lifecycle

## Table of contents

1. [Observability](#observability)
2. [Correlation and tracing](#correlation-and-tracing)
3. [DLQ and replay](#dlq-and-replay)
4. [Backward compatibility](#backward-compatibility)
5. [Deprecation](#deprecation)
6. [Runbooks](#runbooks)

## Observability

Instrument every integration path:

| Signal | Examples |
|---|---|
| Metrics | Request rate, latency histogram, error rate by partner, queue lag, DLQ depth |
| Logs | Structured JSON; correlation ID; no secrets/PII |
| Traces | HTTP and messaging spans; broker publish/consume spans |

Dashboards per **partner**, **API**, and **flow** (ingress vs egress). Alert on SLO burn (error budget) not only raw 5xx.

Deploy and pipeline mechanics → `devops`. Cloud-native wiring → `cloud-engineer`.

## Correlation and tracing

**Correlation ID:**

- Accept incoming `X-Correlation-Id` or generate UUID at edge
- Propagate through HTTP headers, message attributes, and log fields
- Return correlation ID in error responses for partner support

**Distributed tracing:**

- Use W3C `traceparent` / OpenTelemetry across sync and async
- Link producer publish span to consumer process span via context injection in message headers

## DLQ and replay

| Step | Action |
|---|---|
| Detect | Alert on DLQ depth, age of oldest message, repeated failures |
| Triage | Classify: poison, schema drift, upstream outage, bug |
| Fix | Patch consumer or schema; redeploy |
| Replay | Re-drive from DLQ with rate limit; verify idempotency |
| Communicate | Partner notification if their payloads were rejected |

Never replay to production without **dry-run** or sampled replay when side effects are irreversible.

Document **max replay window** aligned with idempotency TTL.

## Backward compatibility

**Additive changes (safe):**

- New optional JSON fields
- New enum values only if consumers ignore unknowns
- New endpoints or topics

**Breaking changes (require major version or new topic):**

- Removing fields, tightening validation, changing types
- Renaming fields without aliases
- Changing URL paths for partners

Use **schema registries** with compatibility modes (backward/forward) for events.

## Deprecation

1. Announce sunset date in docs and `Sunset` / `Deprecation` HTTP headers
2. Monitor traffic to deprecated version; contact remaining consumers
3. Maintain read-only or dual-publish period as agreed
4. Remove only after **zero critical traffic** and signed partner ack where required

Maintain a **compatibility matrix** (consumer × API version × status).

## Runbooks

Minimum runbook sections:

- **Overview** — flow diagram, owners, dependencies
- **Normal operation** — SLOs, dashboards, key metrics
- **Failure modes** — symptoms, checks, mitigation
- **Partner issues** — how to trace by correlation ID
- **DLQ replay** — prerequisites, commands, rollback
- **Rollback** — previous gateway route or consumer version

For enterprise-wide operational resilience programs → `cyber-resilience-engineer` (when scope is org-wide, not single integration).
