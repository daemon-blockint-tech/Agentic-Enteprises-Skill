# Device identity, provisioning, and OTA

## Table of contents

1. [Identity model](#identity-model)
2. [Provisioning flows](#provisioning-flows)
3. [Certificate lifecycle](#certificate-lifecycle)
4. [Secrets and key storage](#secrets-and-key-storage)
5. [OTA architecture](#ota-architecture)
6. [Rollout and rollback](#rollout-and-rollback)
7. [Compliance hooks](#compliance-hooks)

## Identity model

| Identifier | Scope | Notes |
|---|---|---|
| Manufacturing ID | Factory | Immutable; printed label / secure element |
| Logical deviceId | Cloud registry | Stable across cert rotation |
| Client ID (MQTT) | Broker session | Often equals deviceId; document mapping |
| Certificate SAN/CN | TLS | Short-lived preferred |
| Tenant ID | Multi-tenant SaaS | Embedded in topic prefix and ACL |

**Principle:** Separate **immutable hardware identity** from **rotatable operational credentials**.

## Provisioning flows

### Factory provisioning

- Inject initial trust anchor or factory cert in secure element.
- Record device in manufacturing DB; export allow-list to cloud registry.
- Seal debug interfaces per product policy.

### Field bootstrap (claim)

| Step | Action |
|---|---|
| 1 | Device presents factory cert or one-time claim code |
| 2 | Cloud/registry validates allow-list |
| 3 | Issue operational cert + policy (topics, shadow access) |
| 4 | Revoke or narrow factory credentials |

### Zero-touch / bulk

- EST (RFC 7030) or vendor equivalent from gateway.
- CSV allow-list imports for pilots—automate before production scale.

**Wi-Fi onboarding:** BLE SoftAP or DPP may involve phone apps—coordinate UX with mobile teams; network skill owns **resulting MQTT credentials**.

## Certificate lifecycle

| Phase | Practice |
|---|---|
| Issuance | Short TTL (30–90d devices; 24h high-risk) |
| Rotation | Dual cert window; device connects with either until cutover |
| Revocation | CRL/OCSP or broker deny-list; propagate within minutes |
| Algorithm | ECDSA P-256 or Ed25519 on constrained devices; plan PQ migration |

**AWS IoT Core:** Register CA, use JITR/JITP templates, attach policies per thing group.

**Azure IoT Hub:** DPS enrollment groups (symmetric key for dev only), X.509 attestation for production.

## Secrets and key storage

| Storage | Suitable for |
|---|---|
| Secure element / TPM | Private keys, attestation |
| Encrypted flash | Operational certs with anti-rollback counters |
| Gateway vault | Per-site secrets; HSM optional |

Never embed **long-lived cloud API keys** in firmware. Prefer **per-device certs** or **STS-style** short tokens brokered by gateway.

Coordinate with `embedded-real-time-software-engineer` for **where keys live in MCU memory** and boot chain.

## OTA architecture

```
[Build pipeline] → [Signed artifact in object store]
        ↓
[Cloud job / IoT Jobs] → [MQTT command or HTTPS manifest URL]
        ↓
[Device or gateway agent] → verify signature → staged slot → reboot
```

| Component | Responsibility |
|---|---|
| Artifact store | Versioned blobs; CDN for bandwidth |
| Manifest | Version, size, hash, signature, hw compatibility |
| Agent | Download, verify, A/B slots, progress telemetry |
| Policy | Rings, geos, device groups, maintenance windows |

**Edge-assisted OTA:** Gateway caches firmware for **bandwidth-constrained** southbound devices (LoRa, serial).

## Rollout and rollback

| Ring | Population | Promotion criteria |
|---|---|---|
| Canary | 0.1–1% | Error rate, bricked device count, battery impact |
| Early | 10% | 24–72h soak |
| Broad | remainder | Change window approved |

**Rollback triggers:**

- Boot loop detection (failed boots counter)
- Connectivity loss threshold post-update
- Safety interlock trips (plant devices—engage OT)

**Mechanisms:** A/B partitions, signed previous version retained, cloud command to pin version.

## Compliance hooks

- Maintain **SBOM** per firmware line; map CVE response to OTA rings.
- Audit log: who approved ring promotion, artifact hash, device list.
- Data residency: OTA blobs and job APIs in correct region.
- For regulated environments, **dual control** on production ring promotion.

When legal/compliance owns policy interpretation, implement **technical controls** only and document evidence artifacts.
