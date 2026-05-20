# Connectivity protocols and LPWANs

## Table of contents

1. [Protocol selection](#protocol-selection)
2. [MQTT essentials](#mqtt-essentials)
3. [CoAP and HTTP device APIs](#coap-and-http-device-apis)
4. [LoRaWAN](#lorawan)
5. [Mesh and short-range radios](#mesh-and-short-range-radios)
6. [Payload and quality contracts](#payload-and-quality-contracts)
7. [Tradeoffs](#tradeoffs)

## Protocol selection

| Factor | Favor MQTT | Favor CoAP | Favor HTTP/REST |
|---|---|---|---|
| Always-on TCP acceptable | Yes | Often UDP | Yes |
| Constrained MCU / UDP | Possible (lightweight stacks) | Yes | Rare |
| Firewalled corporate HTTP only | Bridge via gateway | Proxy/gateway | Yes |
| Pub/sub fan-out to many consumers | Yes | Observe pattern | Polling/webhooks |
| Command/response with low overhead | Yes (request topics) | Yes | Yes |
| Human debugging with curl | Harder | Moderate | Easy |

**Default pattern:** MQTT from device or gateway to cloud broker; CoAP on constrained UDP links; HTTP for provisioning portals, OTA manifests, and occasional configuration.

## MQTT essentials

| Concept | Guidance |
|---|---|
| QoS 0 | Fire-and-forget telemetry; acceptable loss with periodic full state |
| QoS 1 | At-least-once; dedupe at consumer with message id or sequence |
| QoS 2 | Exactly-once; higher overhead—reserve for billing or safety-adjacent commands |
| Retain | Use for last-known config/state topics only; avoid high-cardinality retained storms |
| Last Will Testament (LWT) | Publish offline status; rate-limit fleet-wide LWT alerts |
| Clean session | Prefer persistent sessions for gateways; ephemeral for disposable sensors |
| Keepalive | Set from worst-case NAT timeout; gateways often 30–120s |

**Session hygiene:** One logical client id per device; reject duplicate connects; document reconnect backoff (exponential cap).

## CoAP and HTTP device APIs

### CoAP

- Use **CON/NON** appropriately; confirmable for commands, non-confirmable for high-rate telemetry when loss is acceptable.
- **Observe** for server-push analog to MQTT subscriptions—watch resource expiry and renewal.
- DTLS mandatory on untrusted networks; pin certs or use EST-like bootstrap aligned with provisioning skill.

### HTTP/REST device APIs

- Idempotent **PUT/PATCH** for desired configuration; **ETags** for conflict detection.
- Short-lived tokens (OAuth client credentials or device certs) rather than long-lived API keys in firmware.
- Prefer **async command** pattern: `POST /commands` → `202` + command id → device polls or uses separate notify channel.

## LoRaWAN

| Layer | Responsibility |
|---|---|
| End device | Class A/B/C trade battery vs downlink latency |
| Join | OTAA preferred over ABP; rotate keys via join server policy |
| Network server | ADR, duty cycle, regional parameters (EU868, US915, etc.) |
| Application server | Decode payloads; map to MQTT/HTTP northbound |

**Architecture notes:**

- Treat LoRaWAN as **high-latency, low-bitrate**—aggregate at gateway/application server before cloud burst.
- Plan for **partial uplinks** and duplicate frames; idempotent ingest keys `(devEUI, fCnt, port)`.
- Backhaul from gateway is often **Ethernet/LTE/Wi-Fi**—coordinate with `wireless-wifi-mobility-specialist` when Wi-Fi is backhaul.

## Mesh and short-range radios

| Radio | Typical role | Edge integration |
|---|---|---|
| Zigbee | Home/building sensors, lighting | Coordinator on gateway → MQTT |
| Z-Wave | Home automation | USB/controller gateway |
| BLE | Wearables, beacons, provisioning | Gateway or phone-assisted onboarding |
| Thread | IPv6 mesh (Matter ecosystem) | Border router on gateway |

**Do not** design full mesh RF plans here when WLAN/OT specialists own the physical layer—define **integration contracts** (pairing, trust center, channel plans) and northbound topic mapping.

## Payload and quality contracts

Standardize envelopes across transports:

```json
{
  "deviceId": "string",
  "ts": "ISO-8601 or unix_ms",
  "seq": 12345,
  "schema": "telemetry.v2",
  "data": { },
  "meta": { "rssi": -90, "fw": "1.2.3" }
}
```

| Quality dimension | Policy |
|---|---|
| Timestamp | Prefer device monotonic + gateway receive time; flag clock skew |
| Ordering | Per-device sequence; consumers tolerate gaps |
| Duplicates | Idempotent upsert on `(deviceId, seq)` or cloud message id |
| Units | Document SI units in schema registry |

## Tradeoffs

| Goal | Technique | Cost |
|---|---|---|
| Battery life | Long sleep, batch uplink, edge aggregate | Stale telemetry |
| Latency | Class B/C LoRa, QoS1 MQTT, persistent TCP | Power and bandwidth |
| Bandwidth | Binary payloads (CBOR/Protobuf), delta encoding | Debuggability |
| Reliability | Store-and-forward at gateway, QoS1 | Disk and ordering complexity |
| Security | mTLS, DTLS, cert pinning | CPU and provisioning friction |

When users ask for **maximum devices per dollar**, optimize payload size and connection schedule before broker SKU upgrades.
