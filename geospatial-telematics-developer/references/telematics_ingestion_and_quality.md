# Telematics ingestion and quality

## Table of contents

1. [Ingestion channels](#ingestion-channels)
2. [NMEA and device payloads](#nmea-and-device-payloads)
3. [Timestamps](#timestamps)
4. [Quality dimensions](#quality-dimensions)
5. [Stream and batch patterns](#stream-and-batch-patterns)
6. [CAN-linked metadata](#can-linked-metadata)
7. [Idempotency and replay](#idempotency-and-replay)

## Ingestion channels

| Channel | Typical pattern | Notes |
|---|---|---|
| MQTT / device gateway | Per-device topics, QoS1 | Auth per device; payload size limits |
| HTTPS batch upload | Mobile SDK backoff | Signed uploads; gzip JSON |
| Kafka / Kinesis | Partition by `asset_id` | Preserve per-asset ordering |
| SFTP / object files | Nightly vendor drops | Schema registry; quarantine bad files |

## NMEA and device payloads

Common sentences (conceptual—validate against device spec):

| Sentence | Fields of interest |
|---|---|
| GGA | Fix quality, lat/lon, HDOP, altitude |
| RMC | Speed over ground, course, date/time |
| GSA / GSV | Satellite visibility (quality diagnostics) |

**Proprietary JSON** often includes: `lat`, `lon`, `speed`, `heading`, `accuracy`, `ignition`, `odometer`, `event_code`.

Parse in a **dedicated ingest worker**; emit normalized canonical fix records to the spatial store.

## Timestamps

| Clock | Use |
|---|---|
| Device GNSS time | Preferred for kinematics when trustworthy |
| Device wall clock | Fallback; detect skew vs server |
| Server ingest time | Latency monitoring; not for trip logic |

Policies:

- Reject or flag fixes **> N minutes** in the future
- Define **late arrival** window (e.g. 24–72h) for stream processing
- Store all three when available: `ts_device`, `ts_gnss`, `ts_ingest`

## Quality dimensions

| Flag | Detection | Downstream |
|---|---|---|
| No fix | Missing lat/lon or fix quality invalid | Drop or dead-letter |
| Low accuracy | HDOP/accuracy meters above threshold | Weight down in analytics |
| Duplicate | Same asset + timestamp + rounded coords | Idempotent upsert |
| Teleport | Speed implied > physical max | Split trip; quarantine |
| Jitter | Stationary spread | Snap only after stop detection |
| Time gap | Δt > threshold | End trip; new segment |

Expose quality as **columns or sidecar table**—do not silently discard without audit.

## Stream and batch patterns

```
device → ingest → validate → enrich (tenant, asset) → publish fix event → spatial writer
```

- **Watermark** on event time for windowed aggregations
- **Dead-letter queue** for schema violations
- **Batch backfill** replays with same idempotency keys as live path

## CAN-linked metadata

Conceptual linkage only—implementation varies by OEM:

| Signal | Geo use |
|---|---|
| Odometer | Distance reconciliation vs GPS |
| Ignition | Stop detection corroboration |
| Fuel / engine hours | Utilization analytics (not spatial core) |
| DTC codes | Correlate breakdown events with last known position |

Do not claim **safety-critical** CAN semantics unless under automotive safety process.

## Idempotency and replay

| Key component | Recommendation |
|---|---|
| Natural key | `(tenant_id, asset_id, ts_device, source_seq)` |
| Upsert | `ON CONFLICT DO UPDATE` with monotonic `source_seq` |
| Replay | Same keys; versioned derived tables for map match |
| Audit | Count raw vs accepted vs rejected per batch |

Monitor **ingest lag** (p50/p99), **reject rate**, and **duplicate rate** per device firmware version.
