# Routing — OSPF, EIGRP, BGP

## Table of contents

1. [Protocol selection](#protocol-selection)
2. [OSPF enterprise design](#ospf-enterprise-design)
3. [EIGRP enterprise design](#eigrp-enterprise-design)
4. [BGP fundamentals at the enterprise edge](#bgp-fundamentals-at-the-enterprise-edge)
5. [Redistribution and loop prevention](#redistribution-and-loop-prevention)
6. [Summarization and filtering](#summarization-and-filtering)
7. [IPv6 routing notes](#ipv6-routing-notes)
8. [Verification and troubleshooting](#verification-and-troubleshooting)

## Protocol selection

| Factor | OSPF | EIGRP | Notes |
|---|---|---|---|
| Multi-vendor campus | Strong default | Cisco-centric | OSPF common in mixed estates |
| Large Cisco-only WAN | Either | Familiar metrics | Document metric manipulation policy |
| Staff skills | Area design literacy | DUAL concepts | Training plan matters |
| IPv6 | Native OSPFv3 | EIGRP for IPv6 (legacy) | Prefer OSPFv3 for dual-stack greenfield |

**Default guidance:** **OSPF** for new enterprise multi-site designs unless EIGRP is mandated by existing core.

Defer **internet-scale BGP policy** to `network-backbone-architect`.

## OSPF enterprise design

**Area types:**

- **Area 0** at core/distribution hub
- **Normal areas** for campuses; **stub/NSSA** at remote sites to limit LSDB size

**Design checklist:**

- [ ] One logical **ABR** layer (distribution) summarizing into area 0
- [ ] **Passive interfaces** on user-facing SVIs; adjacencies only on routed links
- [ ] **BFD** on WAN/core adjacencies where fast failure detection is required
- [ ] **Reference bandwidth** adjusted on high-speed links (`auto-cost reference-bandwidth`)
- [ ] **Authentication** (MD5 or SHA) on all adjacencies in security-sensitive environments

**LSA flooding discipline:**

- Avoid excessive type-7/external in NSSA without summarization
- Filter **default originate** only from documented edge devices

**Timers:** tune only with baseline captures; document hello/dead on WAN links.

## EIGRP enterprise design

**When EIGRP remains:**

- Document **AS number**, **named mode** vs classic, and **stub** sites
- Use **EIGRP stub** on remote spokes to limit query scope
- **Leak maps** and **offset lists** require change control — easy to create loops

**Metrics:**

- Understand **K-values**; avoid arbitrary bandwidth/delay tweaks without traffic matrix
- **Variance** for unequal cost — rare in campus; document if used

## BGP fundamentals at the enterprise edge

Enterprise **BGP** scope here: **single- or dual-homed** internet, MPLS CE, or hub **route reflector** at DC — not full internet table engineering.

**Typical roles:**

| Role | Function |
|---|---|
| CE router | Peers with ISP or MPLS PE; receives default or partial routes |
| DC edge | Originates enterprise aggregates; filters RFC1918 leaks |
| RR (optional) | Hub spokes in large hub-and-spoke VPN designs |

**Checklist:**

- [ ] **ASN** private vs public documented
- [ ] **Prefix filtering** inbound (bogons) and outbound (only owned prefixes)
- [ ] **Maximum-prefix** limits on CE sessions
- [ ] **Local preference / MED** policy documented if multi-homed
- [ ] **BGP TTL security** and GTSM where provider supports

**SD-WAN handoff:** underlay BGP may coexist with overlay; coordinate with `sd-wan-engineer` for path preference.

## Redistribution and loop prevention

Redistribution is a **design event**, not a config shortcut.

**Rules:**

1. Redistribute in **one direction** per routing domain boundary when possible
2. Use **route tags** to identify source protocol
3. Apply **distribute-lists** or route-maps on both protocols at the boundary
4. Never redistribute **BGP into IGP** without filtering defaults at multiple points
5. Prefer **static discard** aggregates over leaking fine-grained externals

**OSPF ↔ EIGRP** (migration):

- Use **seed metrics** consistently (type E1/E2, EIGRP delay/bandwidth)
- Staged migration: mutual redistribution only in maintenance window with loop monitoring

**External routes:** originate summaries at ABR/edge, not from access layer.

## Summarization and filtering

| Location | Summarize | Rationale |
|---|---|---|
| Distribution → Core | Per-building or per-site subnets | Stable LSDB |
| WAN edge | Enterprise supernets to provider | Minimize updates |
| Branch stub | Default route only | Simplicity |

**Filtering:**

- Prefix lists for **exact match** on redistributed nets
- Community tags for **policy** at WAN (coordinate with backbone peer if used)

## IPv6 routing notes

- **OSPFv3** separate process or address-family under single OSPF (platform-dependent)
- Plan **link-local** adjacencies on point-to-point; document global addressing on SVIs
- **ICMPv6 RA** vs DHCPv6 — align with access design
- Filter **fe80::/10** leaks at edge same as IPv4 bogon discipline

## Verification and troubleshooting

**Layered checks:**

1. Interface up/up, correct subnet, MTU match
2. Neighbor state (Full for OSPF; up for EIGRP; Established for BGP)
3. Routing table for prefix — **which protocol, which AD**
4. Forwarding path — `traceroute`, CEF/FIB entry

**Useful show commands:**

```
show ip ospf neighbor
show ip ospf database
show ip eigrp neighbors
show ip route <prefix>
show ip bgp summary
show ip bgp <prefix>
show ip protocols
```

For redistribution bugs, compare **routing table** vs **protocol RIB** and capture **route-map** hit counts during change window.
