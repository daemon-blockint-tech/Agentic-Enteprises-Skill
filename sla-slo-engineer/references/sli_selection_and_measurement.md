# SLI selection and measurement

## Table of contents

1. [Choosing SLIs](#choosing-slis)
2. [Availability SLIs](#availability-slis)
3. [Latency SLIs](#latency-slis)
4. [Freshness and throughput](#freshness-and-throughput)
5. [Measurement implementation](#measurement-implementation)
6. [Data quality and validation](#data-quality-and-validation)
7. [SLO spec schema](#slo-spec-schema)

## Choosing SLIs

Good SLIs are **measurable**, **user-aligned**, and **actionable**.

| Criterion | Question |
|---|---|
| Measurable | Can you query it daily with stable definition? |
| User-aligned | Does a drop mean users were harmed? |
| Actionable | Can the service team change code/infra to improve it? |

| Journey | Example SLI | Notes |
|---|---|---|
| Sync API | Good requests / valid requests | Define valid (exclude 4xx policy) |
| Async job | Jobs completed within deadline / jobs started | Deadline = product SLA |
| Streaming | Connected minutes without gap / total minutes | Harder—often tier T1+ only |
| Mobile app | Successful session start / attempts | Coordinate with client instrumentation |

Avoid primary SLO on **infra-only** signals unless no better proxy exists—and document the mapping risk.

## Availability SLIs

### Request-based (HTTP/gRPC)

```
availability_sli = successful_requests / eligible_requests
```

**Successful** usually: HTTP 2xx/3xx or gRPC OK. **Eligible** excludes:

- Client errors (4xx) — **policy choice**; document in spec
- Requests rejected by WAF for known abuse
- Synthetic probes if mixed with real traffic (prefer separate SLI)

### Time-based (batch, workers)

```
availability_sli = uptime_minutes / total_minutes
```

Use when request counting is meaningless (queue workers, control loops).

### Partial availability

For multi-region: define whether SLO is **global** or **per-region** minimum. Global user journey often needs **weighted** combination, not min of regions.

## Latency SLIs

Common pattern: **proportion under threshold**:

```
latency_sli = count(latency < T) / count(eligible_requests)
```

| Style | Example | When to use |
|---|---|---|
| Threshold % | 99% < 300ms | Simple SLO, easy to explain |
| Percentile cap | p99 < 500ms | Stricter tail control; harder to alert |
| Multi-threshold | 99% < 200ms AND p99 < 1s | Mature services only |

Align threshold **T** with product expectations and capacity plans. Changing T without rebaselining invalidates history.

**Exclusions:** health checks, internal admin routes, prefetch endpoints—list in spec.

## Freshness and throughput

| Type | SLI example | Typical consumer |
|---|---|---|
| Data freshness | % partitions landed within N hours | Analytics, billing |
| Pipeline lag | % messages processed within L seconds | Event-driven systems |
| Throughput | % intervals meeting minimum RPS | Streaming ingress |

Pair freshness SLO with **backfill** and **late data** policies in `data-system-ops-lead` when warehouse-bound.

## Measurement implementation

### Data sources (pick one primary)

| Source | Pros | Cons |
|---|---|---|
| Load balancer / API gateway | Edge truth, simple | Misses internal-only paths |
| Service mesh | Per-route, mTLS context | Ops complexity |
| App metrics (RED) | Business-aware status codes | Instrumentation burden |
| Synthetic probes | Stable baseline | Not full user mix |

**Rule:** one **authoritative** SLI source per SLO; others are debug only.

### Label cardinality

- Slice by `tier`, `region`, `method` sparingly
- Do **not** SLO per customer ID
- Use recording rules or aggregate tables for 30d windows

### Example PromQL-style recording (illustrative)

```promql
# 30d rolling availability - implementation varies by backend
sum(rate(http_requests_total{status=~"2..|3.."}[30d]))
/
sum(rate(http_requests_total{code!~"4.."}[30d]))
```

Document exact query in SLO spec; implementation owned by `devops` / observability owners.

## Data quality and validation

Before committing an SLO:

1. **Compare sources** — LB vs app metrics; reconcile >0.1% gap
2. **Missing data** — treat gaps as bad or exclude? (document)
3. **Deploy markers** — SLI shifts after release? expected?
4. **Seasonality** — Black Friday baseline separate?
5. **Synthetic mix** — keep <5% of eligible requests unless SLO is probe-only

**Validation checklist:**

- [ ] 90 days history plotted
- [ ] Incidents overlay matches intuition
- [ ] Exclusions reviewed by product + legal (if customer-facing)
- [ ] Query reviewed in PR by SRE (`site-reliability-engineer`)

## SLO spec schema

Publish machine-readable specs (YAML example):

```yaml
service: checkout-api
tier: T0
owner: team-checkout
slos:
  - name: availability
    sli:
      type: request_availability
      source: prometheus
      query_ref: recording/checkout_availability_30d
      eligible: "code!~'4..'"
      success: "code=~'2..|3..'"
    objective: 0.999
    window: rolling_30d
    exclusions:
      - maintenance_windows
      - documented_vendor_outages
  - name: latency_p99_under_300ms
    sli:
      type: latency_threshold
      threshold_ms: 300
      percentile: 0.99
      query_ref: recording/checkout_latency_good_30d
    objective: 0.99
    window: rolling_30d
budget_policy_ref: policies/t0_error_budget.yaml
alert_policy_ref: policies/t0_burn_multiwindow.yaml
```

Version spec in Git; link from service catalog or `platform-engineer` portal when available.
