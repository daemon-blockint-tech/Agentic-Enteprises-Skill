# Routing IGP, BGP, and policy

## Table of contents

1. [Protocol selection](#protocol-selection)
2. [OSPF design](#ospf-design)
3. [IS-IS design](#is-is-design)
4. [IGP tuning and stability](#igp-tuning-and-stability)
5. [BGP foundations](#bgp-foundations)
6. [BGP policy toolkit](#bgp-policy-toolkit)
7. [Route reflectors and confederations](#route-reflectors-and-confederations)
8. [Filtering and security](#filtering-and-security)
9. [Convergence targets](#convergence-targets)

## Protocol selection

| Factor | Favor OSPF | Favor IS-IS |
|---|---|---|
| Team familiarity | Common in enterprise | Common in SP/large DC |
| TLV extensibility | Adequate | Strong for SR, flex-algo (if used) |
| Multi-area/level design | Areas 0 + non-backbone | Single protocol, wide metrics |
| IPv6 | OSPFv3 parallel or dual-stack | Often single protocol for v4/v6 |
| Vendor DC fabric | Less common as underlay IGP | Common underlay for spine-leaf |

**Default guidance:**

- **Enterprise multi-site** with mixed vendors: OSPF or IS-IS both viable; pick one per domain and avoid redistribution mess
- **MPLS L3VPN underlay**: often IS-IS or OSPF in provider core; customer CE uses static or BGP
- **Internet edge**: always **BGP**; never run IGP with external parties

## OSPF design

### Area design

- **Area 0** connects all ABRs; keep area 0 **small and stable**
- **Stub / totally stubby / NSSA** at remote sites to shrink LSDB
- One **area per site** or per region depending on router count (rule of thumb: avoid >50 routers per area without modeling)

### Types and metrics

- Use **point-to-point** on backbone links (no DR election on /31)
- Reference bandwidth aligned with **fastest link** in area
- **BFD** on all OSPF adjacencies on backbone (see resilience reference)

### Redistribution

- Minimize **static ↔ OSPF** redistribution; use route tags and distribute-lists
- BGP → OSPF only at **controlled borders** with explicit prefix lists

## IS-IS design

### Levels

| Level | Role |
|---|---|
| L2 backbone | Core mesh or hub; carries summarized regional routes |
| L1 access | Site internal; default route to L1/L2 router |
| L1/L2 router | Site border; aggregates L1 into L2 |

### NET addressing

- Consistent **System ID** and **area** plan; document in IPAM adjunct
- Wide metrics for **10G+** links; consider metric-style compatible with TE if Segment Routing deployed

### Multi-topology

- Use only when **IPv4/IPv6** topologies must diverge; otherwise single topology simplifies operations

## IGP tuning and stability

| Knob | Purpose |
|---|---|
| Hello/dead intervals | Faster detection vs stability on lossy links |
| LSA/LSP pacing | Protect CPU during flaps |
| Max-metric router-lsa | **Maintenance** — drain traffic before change |
| Prefix suppression | Hide transit link prefixes if platform supports |

**Graceful restart (NSF/NSR):** document where enabled; verify helper mode on peers during upgrades.

Avoid **IGP in the WAN cloud** unless you own both ends; prefer BGP over MPLS or SD-WAN overlay.

## BGP foundations

### ASN plan

| ASN type | Use |
|---|---|
| Private (64512–65534, 4200000000–4294967294) | Internal iBGP |
| Public | Internet edge, IX peering, some DCI |

**iBGP full mesh** does not scale — use **route reflectors** (RR) or confederations.

### Session types

| Session | Typical use |
|---|---|
| iBGP | Same AS; next-hop unchanged on RR with proper policy |
| eBGP | Internet, transit, IX, carrier MPLS VPN (if applicable) |
| BGP labeled unicast | MPLS VPN or SR transport (carrier-dependent) |

### Address families

- **IPv4 unicast** — default everywhere
- **IPv6 unicast** — parallel policy; separate peer policies if needed
- **VPNv4/VPNv6** — MPLS L3VPN to CE or between PEs
- **EVPN** — DCI or DC fabric (type-2/3/5 routes)

## BGP policy toolkit

Express policy with **route-maps, prefix-lists, AS-path filters, communities**:

| Mechanism | Example use |
|---|---|
| Local preference | Prefer one transit or one DCI path |
| MED | Influence inbound from dual-homed site (same AS only) |
| AS-path prepend | Deprioritize outbound path (limited effect) |
| Communities | Signal regional preference, blackhole, no-export |
| ORF / prefix limit | Cap prefixes accepted from peer |

**Community cookbook** (document organization-specific values):

| Community | Meaning |
|---|---|
| 65000:100 | Prepend once toward internet |
| 65000:666 | Blackhole / RTBH trigger at edge |
| 65000:90 | Do not export to IX peers |

Align **inbound** policy: max-prefix, bogon filter, RPKI ROV where supported.

## Route reflectors and confederations

**Route reflector cluster:**

- Place RR at **distribution** or dedicated RR pair
- **Cluster ID** per RR pair; clients only peer to RR (or local cluster)
- Enable **next-hop-self** on RR only where CE/edge needs it

**Confederation:** split AS into sub-AS for very large networks; use when RR alone insufficient.

**RR on WAN:** avoid reflecting across high-latency links without modeling; regional RR pairs common.

## Filtering and security

| Location | Minimum controls |
|---|---|
| Internet eBGP | Bogon + martian, max-prefix, RPKI invalid drop (if available) |
| IX peering | Prefix limits per LOA; strict inbound filter from peer |
| iBGP | TTL security (GTSM) on loopback sessions where supported |
| VPN PE-CE | CE cannot originate full table; default or limited prefixes |

**RPKI:** document ROA coverage for originated prefixes; monitor INVALID state.

Management plane: BGP sessions from **loopbacks** in MGMT VRF where possible.

## Convergence targets

Document expected behavior:

| Event | Target (example) | Mechanisms |
|---|---|---|
| Link failure | < 1 s | BFD + IGP fast hello; BGP PIC |
| Node failure | < 3 s | ECMP removal; FRR (LFA/RLFA) |
| Peer loss (internet) | < 30 s | BGP hold timer; alternate path |

Validate in **lab** or maintenance window with controlled flap tests.

Pair operational runbooks with `site-reliability-engineer` for application-visible SLOs—not network-only metrics alone.
