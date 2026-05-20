# Security, SASE, and ZTNA insertion

## Table of contents

1. [Security services on SD-WAN](#security-services-on-sd-wan)
2. [Traffic breakout models](#traffic-breakout-models)
3. [SASE architecture](#sase-architecture)
4. [Zero trust WAN](#zero-trust-wan)
5. [ZTNA insertion](#ztna-insertion)
6. [Segmentation and zones](#segmentation-and-zones)
7. [Vendor concept mapping](#vendor-concept-mapping)
8. [Operations and compliance](#operations-and-compliance)

## Security services on SD-WAN

Common **security services** chained at edge or hub:

| Service | Function | Typical placement |
|---|---|---|
| **NGFW** | Stateful firewall, IPS, app control | Branch, regional hub, or cloud PoP |
| **SWG** | URL filtering, TLS inspection policy | Hub or SASE PoP |
| **DNS security** | Block malicious domains | Local resolver or cloud |
| **ZTNA** | App access by identity, not network VPN | SASE PoP or connector in DC |
| **CASB** | SaaS API governance | Cloud (paired with SASE) |

SD-WAN **service chaining** forwards selected flows through a **service node** (on-box or at hub) before egress.

## Traffic breakout models

| Model | Description | When to use |
|---|---|---|
| **Local breakout (DIA)** | Internet exit at branch | SaaS, trusted web; reduces hairpin |
| **Centralized breakout** | Backhaul to hub/DC for inspection | Strict compliance, unified logging |
| **Regional SASE PoP** | Breakout near user geography | Global SaaS, consistent policy |
| **Cloud on-ramp** | Private path to IaaS | VPC/VNet workloads |

**Zero trust WAN** reduces implicit trust in MPLS; combine **identity-based access** with **least-privilege segmentation** instead of flat VPN.

## SASE architecture

**SASE** (Secure Access Service Edge) converges WAN edge + security stack in cloud-delivered PoPs:

```
Branch CPE ──overlay──► SASE PoP ──► Internet / SaaS / DC connector
              │              │
              │              ├── SWG, CASB, FWaaS
              │              └── ZTNA broker
              └── optional regional hub for private apps
```

Design decisions:

- **PoP selection** — latency to users vs data residency
- **Connector placement** — DC connector for private apps; HA pairs
- **Policy single pane** — align SD-WAN templates with SASE policy lifecycle
- **Logging** — flow and security logs to SIEM (`information-security-engineer`)

This skill covers **architecture-level SASE integration**, not full corp GRC program.

## Zero trust WAN

Principles for **zero trust WAN** with SD-WAN:

1. **No flat VPN trust** — segment by app and identity
2. **Explicit verification** — device posture, user identity, app entitlement
3. **Micro-segmentation** — VRFs, zones, or service VLANs at branch
4. **Continuous monitoring** — anomaly on flows and DNS

Map legacy **trusted MPLS** apps to **ZTNA or private access** connectors during migration.

## ZTNA insertion

**ZTNA insertion** patterns:

| Pattern | Flow |
|---|---|
| **Client-based ZTNA** | Agent on endpoint → PoP → app |
| **Clientless ZTNA** | Browser access via broker |
| **SD-WAN + ZTNA route** | Specific apps steered to ZTNA PoP via policy |

Coordinate with **DNS** (split horizon), **certificate pinning**, and **private app** publishing.

Do not conflate ZTNA with **site-to-site mesh**—site connectivity remains SD-WAN; user-to-app is ZTNA.

## Segmentation and zones

| Zone | Example controls |
|---|---|
| **Corporate** | Full policy; DC and SaaS via designed breakout |
| **Guest** | Internet only; no RFC1918 access |
| **IoT / OT handoff** | Strict ACL; no routing to corp (`scada-ics-cyber-security-specialist` for OT) |
| **PCI / regulated** | Dedicated VRF; centralized inspection mandatory |

Document **east-west** rules at branch (branch-server to branch-printer) vs **north-south** (branch to internet/DC).

## Vendor concept mapping

Conceptual mapping only—not configuration guides:

| Vendor | SD-WAN / edge | SASE / security |
|---|---|---|
| **Cisco** | Viptela / Catalyst SD-WAN | Umbrella, Secure Access |
| **VMware** | VeloCloud | VMware SASE (partner stack) |
| **Fortinet** | FortiGate SD-WAN | FortiSASE |
| **Palo Alto** | Prisma SD-WAN | Prisma Access (SASE) |

Validate feature parity (TLS inspect, IPv6, multicast) per release notes.

## Operations and compliance

- **Change control** for security policy tied to WAN templates
- **Key management** for certificates on CPE and PoPs
- **Data residency** for inspected traffic in SASE PoPs
- **Incident response** — isolate site (quarantine template) vs kill switch on breakout

Cloud-side controls for breakout targets → `cloud-security-engineer`.
