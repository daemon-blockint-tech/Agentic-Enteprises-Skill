# Topology hierarchy and addressing

## Table of contents

1. [Hierarchical reference model](#hierarchical-reference-model)
2. [Core, distribution, and edge roles](#core-distribution-and-edge-roles)
3. [Spine-leaf and EVPN context](#spine-leaf-and-evpn-context)
4. [VRF and multi-tenant segmentation](#vrf-and-multi-tenant-segmentation)
5. [Addressing plan](#addressing-plan)
6. [Summarization strategy](#summarization-strategy)
7. [Loopbacks and anycast](#loopbacks-and-anycast)
8. [Documentation conventions](#documentation-conventions)

## Hierarchical reference model

Classic **three-tier** campus/enterprise hierarchy maps to WAN/backbone as follows:

```
                    [ Internet / IX / Transit ]
                              |
                    +---------+---------+
                    |   Internet Edge     |
                    +---------+---------+
                              |
                    +---------+---------+
                    |   WAN / MPLS Core   |  <- often provider or owned core
                    +---------+---------+
                         /    |    \
            +------------+    |    +------------+
            |  DC / Site A      |         Site B  |
            |  Distribution     |         Distrib. |
            |       |           |              |
            |    Access/Edge    |         Access |
            +-------------------+--------------+
```

**Design intent:**

- **Core** — high-speed transit only; minimal policy; maximum summarization inward
- **Distribution** — policy aggregation, route reflection, firewall insertion, WAN handoff
- **Edge** — access, local default, local summarization toward distribution

Avoid **flat** full-mesh at scale; use hierarchy to bound IGP LSDB and policy complexity.

## Core, distribution, and edge roles

| Layer | Functions | Typical devices | Routing notes |
|---|---|---|---|
| Core | Non-stop forwarding between major hubs | chassis routers, high-density fabrics | IGP on /31 or /30 only; no end-host routes |
| Distribution | Site aggregation, DC border, RR placement | modular switches/routers | Summarize site prefixes; BGP to WAN/core |
| Edge | Access VLANs, WAN CPE, branch | switches, SD-WAN edge, CPE | Default route or partial routes; stub IGP |

**Dual-homing rules:**

- Every distribution node **dual-attaches** to diverse core paths where physically possible
- Edge uses **two upstreams** (distribution pair or active/active SD-WAN) with consistent metrics
- Document **primary/secondary** only when using active/standby; prefer ECMP where protocols allow

## Spine-leaf and EVPN context

For **data center** and large campus, spine-leaf with **EVPN/VXLAN** often replaces classic three-tier inside the DC. Backbone architect scope:

| Inside DC (spine-leaf) | At DC border (backbone attachment) |
|---|---|
| VXLAN VNI, EVPN type-2/3/5 | BGP EVPN to core or route reflectors |
| Anycast gateway on leaves | Summarize tenant prefixes at border leaf pair |
| Clos ECMP east-west | L3 handoff to WAN (no unnecessary L2 stretch) |

**DCI caution:** extending L2 VXLAN between DCs requires explicit design (multi-site EVPN, stretched VLAN). Prefer **L3 DCI** (host routes or summarized prefixes over BGP) unless application mandates L2 adjacency.

Cross-link: application scale patterns → `high-concurrency-scalability` (not a substitute for L3 design).

## VRF and multi-tenant segmentation

Use **VRFs** (or equivalent logical routers) to separate:

| VRF | Typical contents |
|---|---|
| GLOBAL / default | Internet routing, shared services |
| CORP | desktops, internal apps |
| DMZ | public-facing app tiers |
| MGMT | OOB, jump hosts, device management |
| GUEST | captive portal, internet-only |
| PARTNER | extranet B2B |

**Leakage control:**

- Route targets / import-export policies explicit in BGP VPN
- No accidental **full table** leak between VRFs at RR
- Management VRF reachable only via controlled jump paths

Cloud hybrid: map VRF intent to cloud **VPC/VNet** segmentation in joint workshops with `cloud-architect`.

## Addressing plan

### IPv4 private space

Allocate by **region → site → function** with reserved growth:

| Block tier | Example use |
|---|---|
| /16 per region | All sites in geography |
| /20 per site | Loopbacks, links, summaries |
| /24 per function | MGMT, prod, DMZ within site |

Use **consistent loopback** addressing (`/32` per device) for BGP router-id and telemetry source.

### IPv6

If dual-stack:

- **ULA or GUA** per organizational policy
- Parallel summarization at same hierarchy points as v4
- Verify **PMTUD** and extension header handling on WAN

### Link addressing

- Point-to-point `/31` (v4) or `/127` (v6) on backbone links
- Document **interface descriptions** schema: `CORE1-DIST2_lag12_10G`

## Summarization strategy

Summarize **as close to the source as operationally safe**:

| Location | What to summarize |
|---|---|
| Edge | Access subnets → single aggregate per building |
| Distribution | Site aggregate toward core/WAN |
| Core | Regional supernets toward other regions |

**Stability vs agility tradeoff:**

- More specific summary → faster blackhole risk if summary anchor fails
- Less specific → larger tables and suboptimal hot-potato

Use **null route** or discard on summary anchor with **more-specific leak** only for critical /32 exceptions (document each exception).

## Loopbacks and anycast

| Type | Purpose |
|---|---|
| Physical loopback / system IP | Stable BGP RID, SNMP source, SSH target |
| Service anycast | DNS, load balancer VIP, NTP in multiple sites |

Anycast on backbone:

- Same prefix announced from **multiple sites** with consistent **community** or MED policy
- Tie **health** to IGP or BGP withdraw on failure
- Coordinate with `dci_peering_and_internet_edge.md` for internet anycast vs internal anycast

## Documentation conventions

Maintain living artifacts:

- **IPAM spreadsheet or IPAM tool export** — authoritative allocations
- **VRF matrix** — VRF × site × import/export targets
- **Cable / port plan** — only where needed for backbone handoffs (full physical design may sit with `infrastructure-engineer`)
- **Naming** — hostname, interface, and BGP neighbor naming standards

Reconcile quarterly: orphaned subnets, summary drift, and prefix bloat toward internet edge.
