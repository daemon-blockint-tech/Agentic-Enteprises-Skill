---
name: iot-network-edge-engineer
description: |
  This skill should be used when the user asks about IoT network design, edge engineer work,
  MQTT broker and topic design, LoRaWAN, LPWAN, IoT gateway, device provisioning, IoT edge,
  CoAP, Azure IoT Edge, AWS IoT Core, device shadow, OTA updates, Zigbee, protocol bridge,
  IoT fleet, and IoT segmentation. Guides connectivity, edge gateways, store-and-forward,
  broker scale, and cloud IoT handoffs—not enterprise WLAN (wireless-wifi-mobility-specialist),
  OT/ICS plant security (scada-ics-cyber-security-specialist), embedded without connectivity
  (embedded-real-time-software-engineer), carrier backbone (network-backbone-architect),
  cloud landing zones (cloud-architect), or telemetry ML (data-scientist).
---

# IoT Network & Edge Engineer

## When to Use

- Design **device connectivity**—MQTT, CoAP, HTTP/REST device APIs; QoS, retain, and session semantics
- Plan **LPWAN and mesh**—LoRaWAN, Zigbee, Z-Wave, BLE transport roles and gateway backhaul
- Architect **edge gateways and protocol bridges**—northbound cloud, southbound field protocols
- Define **MQTT topics, ACLs, and broker scale**—namespace design, shared subscriptions, clustering
- Implement **device identity, provisioning, and PKI**—bootstrap, cert rotation, revocation
- Design **OTA update architecture**—staged rollouts, bandwidth-aware delivery, rollback at edge
- Engineer **offline tolerance**—store-and-forward, edge buffering, sync after reconnect
- Trade off **bandwidth, latency, and battery**—payload sizing, sleep schedules, edge aggregation
- Integrate **cloud IoT platforms**—AWS IoT Core, Azure IoT Hub, GCP IoT concepts; shadows and rules
- Deploy **edge analytics and rules**—Greengrass, IoT Edge modules, K3s edge workloads
- Segment **IoT networks**—dedicated VLANs/VRFs, zero-trust device access, broker isolation
- Operate **fleet observability**—metrics, last-will, desired/reported state, fleet health dashboards

## When NOT to Use

- Enterprise **Wi-Fi WLAN** design, RF surveys, and 802.11 roaming (unless Wi-Fi is only one IoT transport) → `wireless-wifi-mobility-specialist`
- **OT/ICS** plant networks, Purdue model, and industrial control security → `scada-ics-cyber-security-specialist`
- **Embedded firmware** without connectivity, RTOS drivers, or bare-metal timing → `embedded-real-time-software-engineer`
- **Carrier BGP/MPLS** backbone, IX peering, and internet routing → `network-backbone-architect`
- **SD-WAN** overlay policy and branch breakout as primary deliverable → `sd-wan-engineer`
- **Cloud landing zone**, VPC foundation, and account guardrails → `cloud-architect`
- Implement **cloud networking and managed services** without IoT device plane → `cloud-engineer`
- **Cloud security program**, CSPM, and corporate IdP as primary deliverable → `cloud-security-engineer`
- **Internal developer platform**, golden paths, and portal roadmap → `platform-engineer`
- **Geospatial pipelines**, map matching, and fleet location APIs without connectivity layer → `geospatial-telematics-developer`
- **ML training, feature stores, and model serving** for telemetry analytics → `data-scientist` / `ml-ops-engineer`

## Related skills

| Need | Skill |
|---|---|
| Enterprise Wi-Fi, SSID/VLAN, 802.1X, roaming | `wireless-wifi-mobility-specialist` |
| OT/ICS segmentation, Purdue model, plant wireless | `scada-ics-cyber-security-specialist` |
| RTOS, drivers, MCU timing without network stack | `embedded-real-time-software-engineer` |
| Cloud VPC, landing zone, hybrid connectivity | `cloud-architect` |
| Cloud service implementation and operations | `cloud-engineer` |
| Cloud network security and guardrails | `cloud-security-engineer` |
| BGP/MPLS backbone and DCI | `network-backbone-architect` |
| SD-WAN overlay and branch policy | `sd-wan-engineer` |
| K8s platform, GitOps, cluster lifecycle | `platform-engineer` |
| GPS trajectories, PostGIS, geofencing APIs | `geospatial-telematics-developer` |

## Core Workflows

### 1. Scope and boundaries

Clarify device classes, transports, scale targets, and compliance constraints.

**See `references/iot_network_edge_scope.md`.**

### 2. Connectivity and LPWAN

Select protocols, radio roles, and payload contracts per device class.

**See `references/connectivity_protocols_and_lpwans.md`.**

### 3. Edge gateways and bridges

Place gateways, map protocol translation, and define backhaul resilience.

**See `references/edge_gateways_and_protocol_bridges.md`.**

### 4. Identity, provisioning, and OTA

Bootstrap trust, rotate credentials, and stage firmware delivery safely.

**See `references/device_identity_provisioning_ota.md`.**

### 5. MQTT topics, brokers, and scale

Design namespaces, ACLs, HA brokers, and fleet-scale connection patterns.

**See `references/mqtt_topics_brokers_and_scale.md`.**

### 6. Cloud integration, operations, and security

Wire cloud IoT services, observability, segmentation, and runbooks.

**See `references/cloud_integration_operations_security.md`.**

## Outputs

- **Connectivity architecture** — transports per tier, protocol matrix, QoS and retry policy
- **Gateway and bridge spec** — southbound/northbound maps, buffering, and failover behavior
- **Topic and ACL catalog** — hierarchy, shared subs, retained message policy, tenant isolation
- **Provisioning and PKI runbook** — bootstrap flows, cert templates, rotation and revocation
- **OTA rollout plan** — channels, rings, bandwidth budgets, rollback and attestation hooks
- **Edge deployment model** — modules/containers, offline sync, and cloud command path
- **Fleet observability pack** — metrics, shadows/state, alerts, and last-will semantics
- **Segmentation diagram** — VLANs/VRFs, firewall zones, broker tenancy, and zero-trust device access

## Reference files

| File | Use when |
|---|---|
| `references/iot_network_edge_scope.md` | Scoping, RACI, handoffs, in/out of scope |
| `references/connectivity_protocols_and_lpwans.md` | MQTT/CoAP/HTTP, LoRaWAN, mesh radios |
| `references/edge_gateways_and_protocol_bridges.md` | Gateway placement, bridges, store-and-forward |
| `references/device_identity_provisioning_ota.md` | PKI, bootstrap, OTA rings and rollback |
| `references/mqtt_topics_brokers_and_scale.md` | Topics, ACLs, clustering, millions of devices |
| `references/cloud_integration_operations_security.md` | AWS/Azure/GCP IoT, edge runtimes, segmentation |
