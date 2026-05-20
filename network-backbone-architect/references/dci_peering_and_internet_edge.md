# DCI, peering, and internet edge

## Table of contents

1. [Data center interconnect goals](#data-center-interconnect-goals)
2. [L3 DCI vs stretched L2](#l3-dci-vs-stretched-l2)
3. [DCI transport options](#dci-transport-options)
4. [EVPN multi-site considerations](#evpn-multi-site-considerations)
5. [Internet edge architecture](#internet-edge-architecture)
6. [Peering, transit, and IX](#peering-transit-and-ix)
7. [Multi-homing and traffic engineering](#multi-homing-and-traffic-engineering)
8. [Anycast and CDN adjacency](#anycast-and-cdn-adjacency)
9. [Edge security integration](#edge-security-integration)

## Data center interconnect goals

DCI connects **production DC pairs** or **active/active regions**. Clarify application requirements before choosing technology:

| Requirement | Drives design toward… |
|---|---|
| Active/active L3 apps | BGP between DCs, summarization, ECMP |
| VM mobility / stretched cluster | L2 stretch (higher risk) |
| Sync replication low latency | Dedicated low-latency path, QoS |
| DR only | Asymmetric: backup DC cold/warm; simpler routing |

Document **RPO/RTO** for **network path** separately from storage replication.

## L3 DCI vs stretched L2

| Approach | Pros | Cons |
|---|---|---|
| **L3 DCI** (routed) | Stable flooding domain; clear failure boundaries | App must tolerate routed hops |
| **L2 stretch** (VXLAN/OTV/VPLS) | Legacy apps needing L2 adjacency | Split brain, STP, broadcast storms |
| **L3 with host routing** (anycast GW) | Modern DC pattern | Requires orchestration discipline |

**Default recommendation:** L3 DCI with **BGP** between DC border leaves/routers; advertise **summarized** prefixes plus selective /32 for anycast services.

If L2 stretch required:

- **Stretched VLAN** only for defined VLAN list
- **BUM** handling and ARP suppression in EVPN
- **Split-horizon** and **site-of-origin** tagging
- Run **GFDL** or similar failure detection between sites

## DCI transport options

| Transport | Characteristics |
|---|---|
| Dark fiber / DWDM | Lowest latency, customer-owned mux; capex heavy |
| Carrier Ethernet EPL | Fixed latency, point-to-point |
| MPLS pseudowire / EVPL | Flexible; watch oversubscription |
| IPsec/GRE over internet | Cost-effective; variable latency; encrypt |
| Wave service | Multiple lambdas; long lead times |

**Diversity:** dual paths with **diverse physical routes** (separate conduits, carriers, entrances).

Capacity: size for **replication peak** + **headroom** (see resilience reference); monitor utilization >70% as upgrade trigger.

## EVPN multi-site considerations

When extending **EVPN/VXLAN** across DCs:

| Topic | Guidance |
|---|---|
| Control plane | eBGP EVPN between DC border leaves or route reflectors |
| Route types | Type-2 (MAC/IP), type-3 (IMET), type-5 (IP prefix) interop |
| BUM | Ingress replication vs multicast underlay |
| Multi-homing | ESIs for dual-attached hosts; avoid cross-site vMotion without design |
| Failure | Site isolation — withdraw type-3 routes on partition |

Coordinate with DC fabric team; backbone architect owns **inter-DC BGP policy** and **WAN attachment**, not server vSwitch config.

## Internet edge architecture

Typical **internet edge** layers:

```
 [ Peering / Transit routers ]  <-- eBGP to carriers and IX
            |
 [ Edge firewalls / scrubbing ]  <-- optional inline or divert
            |
 [ Core / DC border ]            <-- iBGP or static to internal
```

**Functions:**

- Originate **company prefixes** with consistent AS_PATH
- **Default route** propagation to internal (full or partial) per policy
- **DDoS** scrubbing diversion (BGP RTBH or flowspec)
- **DNS anycast** and public service anycast if applicable

Place edge in **DMZ VRF** with controlled leaks to corp VRF.

## Peering, transit, and IX

| Relationship | Description | When to use |
|---|---|---|
| **Transit** | Pay provider for full internet table or default | Baseline connectivity, backup |
| **Peering (PNI)** | Private bilateral with another network | High traffic ratio to one AS |
| **IX peering** | Shared L2 fabric at exchange point | Many peers, cost-efficient PNI |
| **Route server** | IX-facilitated BGP on shared fabric | Simplify multilateral peering |

**IX checklist:**

- Cross-connect or reseller port capacity
- **LOA** for MAC if required
- **Prefix filters** inbound/outbound per peer
- **Maximum prefixes** and monitoring
- **Bogon** and **RPKI** on all eBGP sessions

**Peering policy document:** which ASNs to accept, traffic ratios, settlement-free criteria.

## Multi-homing and traffic engineering

**Dual transit providers:**

- Split **prefix announcements** — same NLRI to both with **AS-path** or **prepend** tuning
- Use **communities** received from providers to influence inbound
- **Local-pref** for outbound preference

**Inbound engineering limitations:** you control outbound local-pref; inbound depends on remote policy — use **multiple locations** and **anycast** for strong inbound control.

**Partial routes:** some enterprises take **default only** from transit and **peering routes** from IX — reduces table size on edge.

## Anycast and CDN adjacency

| Service | Network pattern |
|---|---|
| Internal anycast DNS | Same /32 from multiple sites; IGP metric or BGP MED |
| Public anycast | Global announcement from multiple POPs; coordinate RPKI |
| CDN | CNAME to CDN; optional **private interconnect** to CDN (not full internet path) |

Document **withdrawal procedure** on site failure to avoid **blackholing** anycast elsewhere.

## Edge security integration

Coordinate architecture (implementation may involve security engineering):

| Control | Placement |
|---|---|
| Stateful firewall | North-south at edge; avoid hairpin through distant DC |
| DDoS scrubbing | BGP divert to scrubbing center |
| RTBH | Trigger community at edge on attack destination |
| TLS inspection | Often at app layer; avoid breaking latency-sensitive paths |

Do not duplicate full **GRC control catalog** — align with `cloud-security-engineer` for cloud egress and `information-security-engineer` for corporate policy.

**Logging:** flow records (NetFlow/IPFIX) and BGP update logs at edge for peering disputes and incident response.
