# MQTT topics, brokers, and scale

## Table of contents

1. [Topic namespace design](#topic-namespace-design)
2. [ACLs and authorization](#acls-and-authorization)
3. [Broker topology](#broker-topology)
4. [Scale patterns](#scale-patterns)
5. [Performance and tuning](#performance-and-tuning)
6. [Failure modes](#failure-modes)
7. [Observability](#observability)

## Topic namespace design

**Recommended hierarchy:**

```
{tenant}/{env}/{site}/{deviceId}/{stream}/{name}
```

| Segment | Purpose |
|---|---|
| tenant | Multi-tenant isolation |
| env | dev/stage/prod—never share brokers across prod and dev without hard ACL |
| site | Gateway grouping, regional ops |
| deviceId | Stable logical id |
| stream | telemetry | command | config | shadow |
| name | metric or command verb |

**Rules:**

- Avoid **high-cardinality** dynamic segments in shared subscriptions consumers cannot filter.
- Use **single-level wildcards** (`+`) in ACLs; limit `#` to admin tooling.
- Document **retained topic** allow-list (e.g. `.../config/desired` only).
- Command topics: `.../command/{action}` with **response** on `.../command/{action}/response`.

### Anti-patterns

| Pattern | Problem |
|---|---|
| Topic per sensor field | ACL explosion; broker metadata bloat |
| PII in topic path | Leak in logs and metrics |
| Inconsistent deviceId casing | Duplicate logical devices |

## ACLs and authorization

| Principal | Publish | Subscribe |
|---|---|---|
| Device | Own `.../{deviceId}/telemetry/#`, command responses | Own command topics, config desired |
| Gateway | Site prefix | Site prefix + bridge admin |
| Cloud service | Command desired, fleet jobs | Telemetry ingest wildcards (scoped) |
| Operator tooling | None in prod | Read-only telemetry with audit |

**Implementation:**

- Prefer **certificate CN/SAN → ACL template** mapping.
- Use **role templates** per thing group (AWS policy; Azure hub routes).
- Deny by default; explicit allow per topic subtree.

## Broker topology

| Pattern | When |
|---|---|
| Single cluster | <100k connections, single region |
| Active/active cluster | Vendor-supported HA (EMQX, HiveMQ, VerneMQ, cloud managed) |
| Federation/bridge | Cross-region aggregation; watch loop and dedupe |
| Dedicated ingest vs ops | Separate cluster for telemetry firehose vs command path |

**Managed options:** AWS IoT Core (MQTT endpoint), Azure IoT Hub MQTT, GCP (historical patterns via partners). Self-hosted: EMQX, Mosquitto cluster (limited), HiveMQ.

## Scale patterns

| Target | Tactics |
|---|---|
| Millions of devices | Horizontal broker nodes; load balancer TLS termination; shard by tenant/region |
| Connection storms | Exponential reconnect jitter; broker rate limits; onboarding windows |
| Telemetry fan-in | Shared subscriptions on consumer side; partition Kafka/Kinesis from bridge |
| Command fan-out | Job queue + MQTT publish workers; avoid per-device synchronous API |
| Geo distribution | Regional brokers; global control plane; avoid single cross-ocean MQTT hop |

**Sharding dimensions:**

- By **tenant** (SaaS)
- By **region** (data residency)
- By **device class** (telemetry rate profiles)

Document **maximum connections per node** from vendor benchmarks with your payload profile.

## Performance and tuning

| Knob | Guidance |
|---|---|
| Keepalive | Balance NAT timeout vs false offline |
| Inflight window | Tune for QoS1 throughput without memory blowup |
| Message size cap | Enforce at broker; align with LPWAN MTU after gateway |
| TLS session resumption | Reduce handshake CPU on reconnect storms |
| Persistent sessions | Only where needed; monitor orphaned sessions |

**Payload efficiency:** Move to CBOR/Protobuf at scale; keep JSON for debug tenants.

## Failure modes

| Symptom | Likely cause | Mitigation |
|---|---|---|
| Mass LWT offline | Broker restart, cert expiry, DNS change | Staged cert rotation; canary pool |
| Broker CPU spike | Retained message churn, wildcard subs | ACL tighten; remove rogue `#` consumers |
| Disk full | Persistent QoS1/2 backlog | Monitor queue depth; scale storage |
| Duplicate telemetry | QoS1 redelivery | Idempotent consumer keys |
| Command stuck | ACL typo after rollout | Policy simulation in CI |

## Observability

| Metric | Alert on |
|---|---|
| `connections` | Drop >X% in 5m |
| `messages_in/out_rate` | 3σ deviation |
| `auth_failures` | Spike after rotation |
| `publish_errors` | ACL denials cluster |
| `consumer_lag` | Shared sub group behind |

**Tracing:** Correlate `deviceId`, `clientId`, and cloud **messageId** where available.

Pair with cloud IoT metrics (see `cloud_integration_operations_security.md`) for end-to-end SLOs.
