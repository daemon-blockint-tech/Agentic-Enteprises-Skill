# IoT network and edge scope

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Roles and RACI](#roles-and-raci)
6. [Handoffs](#handoffs)

## Purpose

Define boundaries for **designing and operating IoT connectivity and edge compute layers**—from field devices and gateways through brokers, edge runtimes, and cloud IoT control planes.

This skill covers **architecture, protocols, provisioning, scale, and operations**—not enterprise WLAN RF design, OT plant control security, or pure firmware development without a network story.

## Terminology

| Term | Meaning |
|---|---|
| Device plane | Field endpoints, radios, and local buses that originate telemetry and accept commands |
| Edge | Gateways and edge runtimes that aggregate, buffer, translate, and enforce policy close to devices |
| Cloud IoT control plane | Managed services for registry, messaging, shadows/state, rules, and fleet jobs |
| Northbound | Traffic from edge/gateway toward cloud or enterprise systems |
| Southbound | Traffic from devices toward gateway or edge runtime |
| Shadow / twin | Desired vs reported state model for fleet command and drift detection |
| LPWAN | Low-power wide-area networks (e.g. LoRaWAN) optimized for battery and range |
| Protocol bridge | Component that maps one field protocol to another (e.g. Modbus → MQTT) |
| Store-and-forward | Buffer telemetry/commands when backhaul is down; sync on reconnect |
| OTA | Over-the-air firmware or config delivery with staged rollout controls |

## In scope

| Area | Examples |
|---|---|
| Application protocols | MQTT (QoS, retain, LWT), CoAP, HTTP/REST device APIs |
| LPWAN and mesh | LoRaWAN architecture, Zigbee/Z-Wave/BLE roles at integration level |
| Gateways and bridges | Protocol translation, edge buffering, multi-tenant gateway isolation |
| Topics and ACLs | Namespace design, shared subscriptions, broker tenancy |
| Identity and PKI | Device certs, EST/bootstrap, rotation, revocation |
| OTA at edge | Rings, bandwidth-aware delivery, rollback, attestation hooks |
| Offline tolerance | Edge queues, disk budgets, dedupe and ordering policy |
| Tradeoffs | Payload size, poll vs push, sleep schedules, edge aggregation |
| Cloud IoT | AWS IoT Core, Azure IoT Hub, GCP IoT patterns; rules and jobs |
| Edge runtimes | Greengrass, IoT Edge modules, K3s edge workloads |
| Segmentation | IoT VLANs/VRFs, broker isolation, zero-trust device access |
| Fleet observability | Connection metrics, shadow drift, LWT storms, broker lag |

## Out of scope

| Topic | Route to |
|---|---|
| Enterprise Wi-Fi design, surveys, 802.11k/r | `wireless-wifi-mobility-specialist` |
| OT Purdue model, ICS protocols as security domain | `scada-ics-cyber-security-specialist` |
| MCU drivers, RTOS scheduling, bare-metal timing | `embedded-real-time-software-engineer` |
| BGP/MPLS backbone, peering, DCI | `network-backbone-architect` |
| SD-WAN overlay and path selection | `sd-wan-engineer` |
| Cloud landing zone and account factory | `cloud-architect` |
| General VPC/IaaS without device plane | `cloud-engineer` |
| Corporate IdP, CSPM program ownership | `cloud-security-engineer` |
| K8s platform roadmap and developer portal | `platform-engineer` |
| PostGIS, map matching, geofence APIs | `geospatial-telematics-developer` |
| ML feature stores and model training | `data-scientist` / `ml-ops-engineer` |

## Roles and RACI

| Activity | IoT network/edge | Embedded | Cloud/platform | Security | Fleet/product |
|---|---|---|---|---|---|
| Protocol and topic architecture | A | C | C | C | I |
| Gateway/bridge placement | A | C | I | C | C |
| Broker HA and scale plan | A | I | C | C | I |
| Device bootstrap and PKI | A | C | C | A | I |
| OTA rollout policy | A | A | C | C | C |
| Cloud IoT service wiring | A | I | C | C | I |
| IoT VLAN/segmentation design | A | I | C | A | I |
| WLAN RF and roaming | C | I | I | C | I |
| ICS zone and safety instrumented systems | C | C | I | A | I |

## Handoffs

| To skill | When |
|---|---|
| `wireless-wifi-mobility-specialist` | IoT uses Wi-Fi as transport—coordinate SSID/VLAN, 802.1X, and density; do not duplicate WLAN design here |
| `scada-ics-cyber-security-specialist` | Devices touch plant networks or safety systems—align zones and change windows |
| `embedded-real-time-software-engineer` | Firmware owns radio stacks and drivers—agree on API contracts and cert storage |
| `cloud-architect` / `cloud-engineer` | Landing zone, private connectivity, and shared services—IoT owns device plane integration |
| `cloud-security-engineer` | Org-wide guardrails, KMS, and SIEM—IoT implements device-centric controls |
| `platform-engineer` | Edge K8s cluster lifecycle, GitOps, and golden paths for edge tenants |
| `geospatial-telematics-developer` | Location pipelines and spatial APIs—consume normalized telemetry after gateway ingest |
| `network-backbone-architect` | Backhaul/MPLS/DCI for sites—IoT defines bandwidth and QoS needs per gateway |
