# WAN edge, QoS, and services

## Table of contents

1. [WAN attachment models](#wan-attachment-models)
2. [FHRP (HSRP, VRRP, GLBP)](#fhrp-hsrp-vrrp-glbp)
3. [SD-WAN adjacency (design level)](#sd-wan-adjacency-design-level)
4. [Enterprise QoS framework](#enterprise-qos-framework)
5. [NAT, DHCP, and common services](#nat-dhcp-and-common-services)
6. [Multicast touchpoints](#multicast-touchpoints)
7. [IPv4/IPv6 at the edge](#ipv4ipv6-at-the-edge)
8. [Operational checklist](#operational-checklist)

## WAN attachment models

| Model | CCNP-level design notes |
|---|---|
| **Single DIA** | Default route; stateful firewall often north of CE |
| **Dual DIA** | BGP or static tracking; asymmetric routing awareness |
| **MPLS L3VPN** | CE peers with PE; hub site may summarize |
| **DMVPN / IPsec** | Hub-spoke crypto overlay; NHRP and routing stability |
| **SD-WAN** | Underlay + overlay; defer template ops to `sd-wan-engineer` |

Document for each site:

- **Circuit IDs**, bandwidth, MTU, and provider NOC
- **Primary/backup** selection mechanism (routing metric, IP SLA, SD-WAN policy)
- **Demarcation** — who owns CPE, firewall, and public IP space

## FHRP (HSRP, VRRP, GLBP)

**Goal:** consistent default gateway for VLANs with sub-second failover when distribution pair fails.

| Protocol | Notes |
|---|---|
| **HSRP** | Cisco default; groups per VLAN/SVI |
| **VRRP** | Standards-based; interoperable |
| **GLBP** | Load-sharing AVG; plan ARP and forwarding tables |

**Design rules:**

- Align **active FHRP** with **STP root** for each VLAN
- Use **preempt** with sensible delay to avoid flapping
- Track **WAN interface** or IP SLA to withdraw priority on uplink loss
- Document **virtual MAC** impact on downstream switches (port-security)

**Authentication:** enable FHRP auth on shared segments in untrusted L2 domains.

## SD-WAN adjacency (design level)

At CCNP depth, specify **handoff points** only:

- Underlay reachability (BGP/OSPF/static) between CE and provider
- **Tunnel endpoints** and **local breakout** policy ownership (`sd-wan-engineer`)
- Application SLA classes mapped to **DSCP** before overlay encapsulation
- **Dual CPE** vs single CPE with diverse last-mile

Avoid duplicating vManage policy lifecycle here.

## Enterprise QoS framework

**End-to-end model (simplified):**

```
[ Classify at access ] → [ Trust boundary ] → [ Queue at WAN edge ] → [ Provider COS ]
```

**Common classes:**

| Class | Applications | Marking (example) |
|---|---|---|
| Voice | RTP telephony | EF / DSCP 46 |
| Video | Real-time video | AF41 or CS4 per policy |
| Critical data | ERP, auth | AF31 |
| Best effort | General user | BE |
| Scavenger | Backup | CS1 |

**Principles:**

- **Mark once** close to source (switch port trust or explicit ACL)
- **Police** guest and scavenger at access or distribution
- **Shape** to WAN CIR at edge — know provider **shaping vs policing**
- **Queue** on egress WAN: priority queue for voice; WFQ/CBWFQ for others

**Meraki:** QoS rules in dashboard; align DSCP with IOS-XE sites for hybrid WAN.

## NAT, DHCP, and common services

| Service | Placement | Notes |
|---|---|---|
| **DHCP** | Centralized server or local relay | Option 43 for APs; document lease time |
| **DNS** | Internal resolvers | Split-horizon for guest |
| **NAT** | Edge firewall or router | PAT for IPv4; document statics for servers |
| **NTP** | Stratum hierarchy | Authentication on management plane |
| **SNMP/syslog** | See assurance reference | Separate management VRF if used |

**NAT64/DNS64** — only with explicit IPv6 program; document app compatibility.

## Multicast touchpoints

Not full multicast engineering — document when present:

- **IGMP snooping** on access VLANs with video
- **PIM** at distribution/core if enterprise IPTV
- **RP placement** and MSDP (if used) — escalate complex designs to backbone peer

## IPv4/IPv6 at the edge

- **Dual-stack:** parallel policies for ACLs, QoS, and routing
- **Default routes:** separate v4/v6 next hops; track object per family
- **Provider delegations:** document **PA vs PI** for IPv6

## Operational checklist

- [ ] FHRP priority/tracking matches STP and WAN primary path
- [ ] QoS policy applied on **correct interface direction** (usually egress WAN)
- [ ] Shaper rate ≤ contracted CIR with overhead accounting
- [ ] ACLs permit established; deny RFC1918 ingress on internet-facing interfaces
- [ ] IP SLA probes for critical SaaS or next-hop validation
- [ ] Runbook for **WAN failover test** quarterly
