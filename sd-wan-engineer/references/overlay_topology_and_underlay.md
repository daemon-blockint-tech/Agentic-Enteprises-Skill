# Overlay topology and underlay

## Table of contents

1. [Overlay vs underlay](#overlay-vs-underlay)
2. [Topology patterns](#topology-patterns)
3. [Hub roles and regional design](#hub-roles-and-regional-design)
4. [Underlay types](#underlay-types)
5. [Circuit diversity and carrier handoff](#circuit-diversity-and-carrier-handoff)
6. [Addressing and NAT considerations](#addressing-and-nat-considerations)
7. [CPE and TLOC concepts](#cpe-and-tloc-concepts)
8. [Design checklist](#design-checklist)

## Overlay vs underlay

| Layer | Responsibility | Failure modes to plan |
|---|---|---|
| **Underlay** | Physical/logical transport—MPLS, DIA, LTE, private line | Carrier outage, BGP session down, last-mile cut |
| **Overlay** | Encrypted tunnels, policy, path selection across underlays | Controller reachability, cert expiry, MTU black hole |

SD-WAN **abstracts underlay** so policy applies uniformly; still design underlay **independently**—overlay cannot fix a single-path site if SLA requires diversity.

## Topology patterns

| Pattern | Use when | Tradeoffs |
|---|---|---|
| **Hub-spoke** | Centralized inspection, simple ops, strong control | Hairpin latency; hub scale limits |
| **Full mesh** | Low-latency branch-branch; distributed apps | Control-plane and tunnel count growth |
| **Regional hub** | Global footprint with local breakout | Balance hairpin vs hub count |
| **Dynamic mesh** | Selective branch-branch on demand | Policy complexity; troubleshooting harder |
| **Hybrid** | Mix site classes (mesh for large, spoke for small) | Template discipline required |

**Hub-spoke SD-WAN** remains common for centralized NGFW/SWG. Add **regional hubs** when RTT to a single super-hub exceeds app tolerance.

## Hub roles and regional design

Define explicit roles:

- **Super-hub / DC hub** — data center aggregation, cloud on-ramp, corp apps
- **Regional hub** — inspection and breakout for a geography
- **Transit hub** — optional MPLS internet handoff or partner interconnect

Rules of thumb:

- Place **voice/video** gateways near users or use local breakout to UCaaS PoPs
- Align **cloud on-ramp** with provider region (e.g., AWS Direct Connect location)
- Limit **policy fan-out**—fewer hub tiers reduce asymmetric routing bugs

## Underlay types

| Underlay | Strengths | SD-WAN considerations |
|---|---|---|
| **MPLS L3VPN** | Predictable latency, provider QoS | Often single carrier; combine with DIA for diversity |
| **DIA broadband** | Cost, bandwidth | Asymmetric rates; CGNAT; variable latency |
| **LTE/5G** | Rapid deploy, backup | Data caps; NAT; use as backup or primary for small sites |
| **Private line / EPL** | Deterministic | Expensive; good for DC and large hub |
| **IPsec over internet (legacy)** | Brownfield | Migrate tunnels into SD-WAN overlay gradually |

**Underlay overlay** independence: each transport interface is a **TLOC** (transport location) bound to a circuit; overlay builds across TLOCs.

## Circuit diversity and carrier handoff

| Requirement | Implementation |
|---|---|
| Physical diversity | Separate entrances, paths, and carriers where possible |
| Logical diversity | Different ASNs, separate NNI for MPLS vs DIA |
| Active/active | Two underlays in SLA class with symmetric or weighted load-share |
| Active/standby | Cheaper; document failover timers and stickiness |

**Carrier handoff** documentation per site:

- Handoff type (RJ45, fiber, NNIs)
- Provider VLAN/C-tag, bandwidth, burst
- Support contacts and circuit IDs
- Demarc and smart-hands escalation (`field-services-engineer` for physical work)

## Addressing and NAT considerations

- Use **private addressing** consistently; avoid overlapping site LANs without NAT policy
- Document **NAT modes** on internet underlays (static 1:1 vs PAT) for inbound services
- Set **MTU/MSS** end-to-end—IPsec overhead often requires MSS clamp (1400–1420 common)
- **IPv6** dual-stack: confirm overlay and security services support v6 paths if required

## CPE and TLOC concepts

Vendor-agnostic patterns (Cisco Viptela, VeloCloud, Fortinet, Prisma SD-WAN):

| Concept | Meaning |
|---|---|
| **Edge device / vEdge / appliance** | Branch CPE running overlay data plane |
| **TLOC** | Bind tunnel endpoints to a specific underlay interface |
| **System IP / device ID** | Stable overlay identity independent of underlay |
| **Color / encapsulation** | Tag transport preference (e.g., `mpls`, `biz-internet`, `lte`) |
| **Control connection** | Device to orchestrator (not user traffic) |

**Branch connectivity** templates should declare: number of TLOCs, expected colors, hub preference, and local LAN segments (VRFs/services).

## Design checklist

- [ ] Site class assigned; topology role (spoke, mesh node, hub) documented
- [ ] Minimum two underlays for HA sites; LTE backup defined for small sites
- [ ] No unintended hairpin (SaaS, branch-branch) without policy intent
- [ ] Hub scale validated (tunnel count, throughput, security throughput)
- [ ] MTU tested on each underlay path; MSS clamp configured
- [ ] Carrier handoff and diversity recorded per site
- [ ] Overlap with `network-backbone-architect` for MPLS VPN design at provider edge
