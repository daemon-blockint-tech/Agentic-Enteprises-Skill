# Migration, HA, and troubleshooting

## Table of contents

1. [High availability modes](#high-availability-modes)
2. [Brownfield SD-WAN migration](#brownfield-sd-wan-migration)
3. [Migration waves](#migration-waves)
4. [Parallel run and cutover](#parallel-run-and-cutover)
5. [Troubleshooting methodology](#troubleshooting-methodology)
6. [Common failure patterns](#common-failure-patterns)
7. [Acceptance testing](#acceptance-testing)
8. [Post-migration operations](#post-migration-operations)

## High availability modes

| Mode | Description | Considerations |
|---|---|---|
| **Active/standby CPE** | One device forwards | Faster fail to standby; state sync |
| **Active/active CPE** | Both forward; load share | Requires LAN HA (VRRP/HSRP) design |
| **Dual underlay active/active** | Single CPE, multiple TLOCs | Most common branch HA pattern |
| **Geographic hub redundancy** | Dual hubs, priority | Control policy for hub preference |

Align **BFD timers** with app SLA—voice may need sub-3s failover; bulk can wait longer.

Document **split-brain** behavior if control link lost between HA pair.

## Brownfield SD-WAN migration

Typical sources:

- **MPLS hub-spoke** with regional DC
- **DMVPN / IPsec mesh** over internet
- **Dual-MPLS** with static routing
- **WAN optimizers** at branch

**Brownfield SD-WAN migration** principles:

1. **Inventory** circuits, routes, apps, and security dependencies
2. **Pilot** representative site class in each region
3. **Parallel run** MPLS + SD-WAN overlay before removing legacy
4. **Migrate routing** in phases—prefix advertisement, hub preference, default route
5. **Decommission** legacy only after soak period and rollback window closed

Avoid migrating **routing and security** in the same maintenance window without rollback.

## Migration waves

| Wave | Sites | Goal |
|---|---|---|
| 0 | Lab + DC hub | Validate templates, controllers, SASE |
| 1 | Pilot branches (low risk) | Tune SLA and app policies |
| 2 | Regional rollout | Scale ZTP; train NOC |
| 3 | Critical / complex | Custom apps, multicast, OT adjacency |
| 4 | Legacy decommission | Remove MPLS, optimizers |

Each wave includes: **rollback trigger**, **owner**, **communication plan**, **success metrics**.

## Parallel run and cutover

| Technique | Use |
|---|---|
| **Route tagging / preference** | Prefer MPLS until SD-WAN stable |
| **Policy-based forwarding** | Pilot apps over SD-WAN only |
| **Split tunnel** | SaaS on SD-WAN DIA; corp on MPLS temporarily |
| **Supernet advertisement** | Avoid asymmetric routing during dual connect |

**Cutover checklist:**

- [ ] All TLOCs green; certs valid
- [ ] App catalog routes verified
- [ ] Security logs flowing to SIEM
- [ ] NMS maps updated
- [ ] Carrier change requests submitted (if replacing handoff)

## Troubleshooting methodology

Use **overlay vs underlay** isolation first:

```
User report (slow / down)
    │
    ├─ LAN OK? ──no──► LAN/Wi-Fi team
    │
    ├─ Underlay up? (per TLOC, circuit util, errors)
    │       └─no──► carrier / physical
    │
    ├─ Overlay tunnel up? (control, BFD, cert)
    │       └─no──► orchestrator, cert, MTU, NAT
    │
    ├─ Policy / SLA match expected path?
    │       └─no──► app ID, policy group, hub role
    │
    └─ Security service drop? (FW, SWG, ZTNA)
            └─yes──► security policy / SASE PoP
```

Collect: **timestamp**, **site**, **app**, **source/dest**, **underlay colors tried**, **SLA stats**, **recent template push**.

## Common failure patterns

| Symptom | Likely cause | Mitigation |
|---|---|---|
| Intermittent disconnects | MTU / MSS black hole | Clamp MSS; test `ping -s` |
| Works on MPLS not broadband | CGNAT, UDP block, asymmetry | Static IP or provider change |
| SaaS slow after migration | Hairpin to distant hub | Local/regional breakout |
| Flapping paths | Aggressive SLA thresholds | Widen intervals; enable stickiness |
| One app only broken | Misclassified app route | Fix catalog; custom rule |
| Post-template push outage | Bad variable on site | Rollback policy group attach |
| Cert warnings | Expiry or clock skew | NTP; renew cert chain |

**VeloCloud / Viptela / Prisma SD-WAN** each expose different UI labels—map diagnostics to generic steps above.

## Acceptance testing

| Category | Tests |
|---|---|
| **Connectivity** | Ping/traceroute to DC, hub, internet test hosts |
| **Failover** | Pull primary underlay; measure failover time |
| **Apps** | VoIP MOS, VDI login, SaaS load, ERP transaction |
| **Security** | Blocked URL test, allow corporate app |
| **Throughput** | iperf/flex on each underlay at peak window |
| **Operations** | Alarm fires on simulated failure; syslog received |

Store results per wave for audit.

## Post-migration operations

- **Soak** 2–4 weeks before MPLS disconnect
- **Rebaseline** dashboards and alarm thresholds
- **Update** DR runbooks and circuit inventory
- **Train** NOC on overlay vs underlay views
- **Review** cost vs performance (broadband vs MPLS commit)

Backbone or DCI changes after SD-WAN stable → `network-backbone-architect`.
