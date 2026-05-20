# Cloud integration, operations, and security

## Table of contents

1. [Cloud IoT platform map](#cloud-iot-platform-map)
2. [Device registry and shadows](#device-registry-and-shadows)
3. [Rules, jobs, and edge runtimes](#rules-jobs-and-edge-runtimes)
4. [Integration patterns](#integration-patterns)
5. [Network segmentation](#network-segmentation)
6. [Zero-trust device access](#zero-trust-device-access)
7. [Fleet observability](#fleet-observability)
8. [Runbooks](#runbooks)

## Cloud IoT platform map

| Capability | AWS IoT Core | Azure IoT Hub / DPS | GCP (conceptual) |
|---|---|---|---|
| MQTT endpoint | Yes | Yes | Partner / Pub/Sub bridge patterns |
| Device registry | Thing + Thing Group | Device identity + DPS | Device registry APIs |
| Twin/shadow | Device Shadow | Device Twin | Device config / state |
| Rules/routing | IoT Rules → Lambda/Kinesis | Message routing → Event Hub | Dataflow / Cloud Functions |
| OTA | IoT Jobs + S3 | Device Update / ADU | Bucket + custom jobs |
| Edge | Greengrass v2 | IoT Edge modules | GKE/Anthos edge patterns |

**Handoff:** Landing zone, VPC, and private endpoints → `cloud-architect` / `cloud-engineer`. Device-plane policy → this skill.

## Device registry and shadows

| Concept | Usage |
|---|---|
| Desired state | Cloud writes target config/firmware version |
| Reported state | Device acknowledges applied state |
| Delta | Rules trigger on drift between desired/reported |
| Version | Monotonic metadata for optimistic concurrency |

**Design rules:**

- Keep shadow **small** (<4–8 KB); large configs in object storage with URL in shadow.
- Split **telemetry** (high rate) from **shadow** (low rate state).
- Use **named shadows** only when product domains are truly independent.

## Rules, jobs, and edge runtimes

### Cloud rules

- Route telemetry to **time-series DB**, **data lake**, and **alerting** with filtering at ingress.
- Avoid complex business logic in rules—push to stream processors for maintainability.

### Jobs (OTA, reboot, cert rotate)

- Target **thing groups** with rollout configuration.
- Report job progress on dedicated topics; surface failures per device.

### Edge runtimes

| Runtime | Pattern |
|---|---|
| AWS Greengrass | Components as OCI artifacts; local MQTT bridge; IPC auth |
| Azure IoT Edge | Modules with routes; upstream to IoT Hub |
| K3s at edge | Helm releases; GitOps via `platform-engineer`; device plugins for hardware |

**Offline:** Edge rules continue; queue upstream sync; document conflict resolution when cloud desired changes during outage.

## Integration patterns

```
Devices → Gateway/Bridge → MQTT Broker → Cloud IoT → Rules → Stream/TSDB
                              ↓
                         Edge runtime (filter/ML/actuate)
```

| Pattern | Description |
|---|---|
| Ingress bridge | Custom auth → IoT Core with IAM role least privilege |
| Twin command | Mobile/app writes desired; device reports progress |
| Digital twin (Azure) | Model-based simulation—separate from device twin ops |
| Event sourcing | Append-only telemetry bus; shadows for control plane only |

Coordinate downstream **analytics** with `data-scientist` / warehouse teams—define **schema registry** at MQTT boundary.

## Network segmentation

| Zone | Typical contents | Controls |
|---|---|---|
| Device VLAN | Sensors, PLCs via gateways | No direct internet; ACL to gateway only |
| Gateway DMZ | Bridges, edge agents | Outbound 8883/TLS only; no inbound from internet |
| Corporate | Ops tooling | Jump host; read-only MQTT monitors |
| Cloud | PrivateLink/VNet integration | Broker endpoints private; no public shadow APIs |

**IoT segmentation** checklist:

- [ ] Dedicated **VLAN/VRF** per site or per tenant
- [ ] **East-west** denied except required gateway paths
- [ ] **DNS filtering** on gateway egress
- [ ] **No flat /16** with cameras and PLCs shared

For plant floors, align with `scada-ics-cyber-security-specialist` before opening paths.

## Zero-trust device access

| Control | Implementation |
|---|---|
| Identity | Per-device cert; no shared passwords |
| Least privilege | Topic ACLs; cloud IAM per pipeline |
| Continuous validation | Short cert TTL; deny revoked |
| Micro-segmentation | Gateway cannot reach corporate LDAP |
| Admin access | Break-glass bastion with MFA; no shared broker superuser |

**Broker hardening:** Disable anonymous; disable `$SYS` for non-admins; TLS 1.2+; cipher suites reviewed annually.

Engage `cloud-security-engineer` for org-wide KMS, SIEM forwarding, and detective controls.

## Fleet observability

| Signal | Source |
|---|---|
| Connected/disconnected | Broker + cloud lifecycle events |
| Shadow drift | Desired ≠ reported > threshold |
| Message rate anomalies | Per-device baselines |
| OTA job success % | Cloud job API |
| Gateway health | Disk queue, CPU, bridge errors |
| RF metrics (if available) | LoRa SNR, Wi-Fi RSSI via gateway meta |

**SLO examples:**

- 99% devices report telemetry within 2× expected interval
- Command delivery P95 < 30s for online devices
- OTA success > 98% per ring before promotion

## Runbooks

| Incident | Steps |
|---|---|
| Broker cert expiry | Pre-notify; dual trust chain; canary reconnect test |
| ACL mis-deploy | Roll back policy version; read-only mode for tools |
| Telemetry storm | Rate limit at gateway; scale shared subscription consumers |
| Region outage | Failover DNS to secondary broker; document dedupe |
| Compromised device | Revoke cert; quarantine thing group; forensic snapshot |

Maintain **connection simulator** in CI that mirrors production keepalive and payload sizes.

Cross-link: MQTT specifics in `mqtt_topics_brokers_and_scale.md`; provisioning in `device_identity_provisioning_ota.md`.
