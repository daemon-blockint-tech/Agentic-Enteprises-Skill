# Edge gateways and protocol bridges

## Table of contents

1. [Gateway roles](#gateway-roles)
2. [Placement and sizing](#placement-and-sizing)
3. [Protocol bridges](#protocol-bridges)
4. [Store-and-forward](#store-and-forward)
5. [Multi-tenant and isolation](#multi-tenant-and-isolation)
6. [Resilience patterns](#resilience-patterns)
7. [Operations checklist](#operations-checklist)

## Gateway roles

| Tier | Examples | Functions |
|---|---|---|
| Field gateway | Industrial PC, LTE router with agent | Southbound protocols, local rules, buffer |
| Home/building hub | Zigbee/Z-Wave coordinator | Pairing, local automation, cloud proxy |
| LoRaWAN gateway | Semtech packet forwarder | RF to UDP/IP; no app logic |
| Edge compute node | K3s, Greengrass, IoT Edge | Containers/modules, ML inference, bridging |

**Separation of concerns:**

- **Radio/PHY** — often vendor or WLAN/OT specialist input.
- **Bridge/translate** — map addresses, scales, and alarms to canonical topics.
- **Edge compute** — filtering, aggregation, OTA proxy, local actuation with safety interlocks.

## Placement and sizing

| Input | Drives |
|---|---|
| Device count per site | CPU, connection table, disk for buffer |
| Message rate and payload size | NIC throughput, serialization cost |
| Southbound protocol count | Bridge containers, serial/USB ports |
| Offline SLA | Disk quota, retention hours |
| Security zone | DMZ vs plant VLAN placement |

**Sizing heuristics:**

- Reserve **2–5× headroom** on connection and msg/s peaks for firmware bugs and burst alarms.
- Disk buffer: `avg_bytes_per_msg × msg_rate × max_outage_hours × safety_factor`.
- Co-locate gateway **one routing hop** from southbound segments when latency-sensitive.

## Protocol bridges

Common southbound → northbound maps:

| Southbound | Northbound | Notes |
|---|---|---|
| Modbus RTU/TCP | MQTT topics per register map | Poll scheduling, exception codes |
| OPC UA | MQTT or cloud SDK | Subscription vs poll; cert trust stores |
| BACnet | MQTT / REST | Object naming; COV vs periodic |
| CAN / J1939 | MQTT (via telematics stack) | Coordinate with `geospatial-telematics-developer` for GPS merge |
| BLE GATT | MQTT | Connection churn; proxy through gateway |
| Zigbee ZCL | MQTT | Cluster/attribute to topic template |

**Bridge design rules:**

1. **Single source of truth** for tag/register → topic mapping (versioned YAML/JSON).
2. **Normalize timestamps** at bridge ingress (gateway UTC + optional device offset).
3. **Alarm vs telemetry** separate topics or severity fields—avoid mixing on same QoS0 firehose.
4. **Command path** authenticated and auditable; reject unsigned writes in plant contexts.
5. **Backpressure** — when northbound down, shed lowest-priority telemetry first.

## Store-and-forward

| Parameter | Recommendation |
|---|---|
| Persistence | Disk-backed queue; survive process restart |
| Ordering | Per-device FIFO; cross-device unordered acceptable |
| Dedupe | Drop duplicates on replay using seq/id |
| Compression | Batch JSON or use columnar/binary for long outages |
| Sync trigger | Backhaul up + broker ACK + disk below high watermark |

**Anti-patterns:**

- Unbounded RAM queues — OOM during multi-hour outage.
- Publishing entire history at QoS2 — broker meltdown on reconnect storm.
- No **timestamp of record** — analytics cannot reconstruct event order.

## Multi-tenant and isolation

| Model | Use when |
|---|---|
| Gateway per tenant | Strong regulatory isolation |
| Shared gateway, separate MQTT credentials | Cost-sensitive multi-tenant SaaS |
| Namespace prefix per tenant | Logical isolation on shared broker |

Enforce:

- Separate **client certs** or username/password per tenant on northbound.
- **Filesystem and container** namespaces for bridge configs.
- **Rate limits** per tenant at gateway export.

## Resilience patterns

| Pattern | Description |
|---|---|
| Active/standby gateway | VIP or DNS failover; shared disk or replicated queue |
| Dual northbound | Primary MQTT broker + secondary cloud; careful dedupe at consumer |
| Split horizon | Local MQTT bus for plant SCADA; cloud only for aggregated metrics |
| Health gate | Stop northbound publish if local safety PLC heartbeat lost |

Document **fail static vs fail safe** for command paths with OT stakeholders.

## Operations checklist

- [ ] Bridge mapping versioned in Git; CI validates topic collisions
- [ ] Gateway clock synced (NTP/PTP); drift alerts
- [ ] Disk and queue depth metrics with paging thresholds
- [ ] Canary site before fleet config push
- [ ] Runbook for broker cert rotation without mass disconnect
- [ ] Integration test: southbound simulator + northbound mock broker
