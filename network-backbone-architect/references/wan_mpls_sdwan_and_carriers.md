# WAN, MPLS, SD-WAN, and carriers

## Table of contents

1. [WAN architecture patterns](#wan-architecture-patterns)
2. [Private line and Ethernet services](#private-line-and-ethernet-services)
3. [MPLS L3VPN](#mpls-l3vpn)
4. [SD-WAN overlay](#sd-wan-overlay)
5. [Hybrid underlay and overlay](#hybrid-underlay-and-overlay)
6. [Carrier selection and SLA](#carrier-selection-and-sla)
7. [MTU and fragmentation](#mtu-and-fragmentation)
8. [Migration and coexistence](#migration-and-coexistence)

## WAN architecture patterns

| Pattern | Topology | Best for | Risks |
|---|---|---|---|
| Hub-and-spoke | Branches → regional hub → core | Cost control, centralized inspection | Hub SPOF, latency hairpin |
| Partial mesh | Meshed hubs, spokes to hub | Balance resiliency and cost | Policy complexity |
| Full mesh | All sites meshed | Lowest latency between all pairs | Cost, table size, operations |
| Regional hub | Continent hubs with inter-hub links | Global enterprises | Inter-hub capacity planning |

Choose based on **traffic matrix**, not diagram aesthetics. Model **hub failure** and **carrier cut** explicitly.

## Private line and Ethernet services

**Dedicated circuits** (TDM legacy, Ethernet EPL/EVPL):

| Attribute | Design note |
|---|---|
| Bandwidth | Committed vs oversubscribed (especially EVPL) |
| Diversity | Diverse POP paths into building; diverse CPE |
| Handoff | Copper vs fiber; single-mode vs multimode |
| SLA | Availability, latency, jitter for voice/video |
| Lead time | Long — plan architecture early |

**Point-to-point Ethernet** between DCs often forms **DCI underlay** before MPLS or IPsec overlay.

Document **demarcation** and who owns CPE vs NID.

## MPLS L3VPN

Carrier provides **VPNv4/VPNv6** with customer VRFs mapped to **route targets (RT)**.

| Role | Device | Function |
|---|---|---|
| PE | Provider edge | Terminates VPN; imposes labels |
| P | Provider core | Label switch only |
| CE | Customer edge | BGP or static to PE |

**Design checklist:**

- Unique **RD** per VRF per site (or per service) per carrier guidance
- **Import/export RT** matrix documented
- **BGP** CE–PE: default route vs full routes vs selective prefixes
- **QoS** marking honored in carrier COS (verify DSCP→EXP mapping)
- **Multicast** rarely supported — confirm before design depends on it

**Inter-provider VPN** (option B/C): only when multi-carrier strategy requires; high operational cost.

## SD-WAN overlay

SD-WAN builds **encrypted overlay** (often IPsec/GRE) across any underlay (broadband, LTE, MPLS).

| Component | Responsibility |
|---|---|
| Orchestrator | Central policy, zero-touch provisioning |
| Edge appliance / vCPE | Local breakout, path selection, DPI (vendor-dependent) |
| Underlay | MPLS, DIA, LTE — diverse paths recommended |

**Path selection policies:**

- **Application-aware** routing based on SLA (latency, loss, jitter)
- **Local internet breakout** for SaaS vs backhaul to hub
- **FEC / packet duplication** for lossy links (bandwidth cost)

**Architectural decisions:**

| Question | Options |
|---|---|
| Hub vs mesh overlay | Meshed edges for DC-like sites; hub for branches |
| Control plane | BGP to LAN, static, or dynamic to DC |
| Integration with MPLS | Hybrid: MPLS primary, DIA backup underlay |
| Security | ZTNA/SWG integration at edge — coordinate with security architecture |

Avoid **double NAT** and asymmetric routing when mixing breakout and hub inspection.

## Hybrid underlay and overlay

Common enterprise pattern:

```
[ Branch SD-WAN ] ---- LTE / DIA ----+
       |                              |
       +---- MPLS VPN (COS gold) -----+----> [ Regional Hub / DC ]
```

**Design rules:**

- **Underlay diversity** — at least two independent paths per site (different carriers or media)
- **Consistent addressing** — overlay uses same corporate VRF semantics as MPLS
- **Routing** — redistribute sparingly between overlay and MPLS; prefer **single control point** at hub
- **QoS** — end-to-end class only if underlay honors DSCP; else application SLA drives path pick only

## Carrier selection and SLA

Evaluate carriers on:

| Criterion | Notes |
|---|---|
| Footprint | On-net sites vs expensive last-mile build |
| SLA credits | Availability %, MTTR, latency guarantees |
| BGP features | Communities, BFD, max-prefix, dual-stack |
| Support | 24×7 NOC, escalation, maintenance notification lead time |
| Security | DDoS scrubbing offering, RTBH support |
| Financial | contract term, burstable vs flat rate |

Maintain **carrier scorecard** and secondary carrier for critical sites.

## MTU and fragmentation

| Layer | Typical MTU | Action |
|---|---|---|
| Internet DIA | 1500 | TCP MSS clamp at edge if tunneling |
| MPLS | 1508–9192 | Confirm end-to-end; jumbo only if full path supports |
| SD-WAN IPsec | 1400–1450 effective | Lower LAN MTU or clamp MSS |
| Overlay inside overlay | Lowest MTU wins | Model in lab |

Document **DF bit** policy and PMTUD black hole detection.

## Migration and coexistence

**MPLS to SD-WAN migration waves:**

1. Pilot sites with parallel run (MPLS + overlay)
2. Shift default route to overlay; keep MPLS for critical classes
3. Decommission MPLS tail after soak period

**Rollback:** retain MPLS VLAN/circuit until overlay stable 30–90 days.

Coordinate cutovers with **maintenance domains** in resilience reference; notify application owners for TCP long-flow resets.

Cloud WAN: hand off cloud-side VPN/Direct Connect attachment design to `cloud-engineer` with backbone BGP parameters documented.
