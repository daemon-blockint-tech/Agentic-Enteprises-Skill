# CCNP scope and enterprise architecture

## Table of contents

1. [Role and boundaries](#role-and-boundaries)
2. [CCNP Enterprise alignment](#ccnp-enterprise-alignment)
3. [Campus hierarchy model](#campus-hierarchy-model)
4. [Discovery checklist](#discovery-checklist)
5. [Addressing and naming](#addressing-and-naming)
6. [Platform context (IOS-XE, Catalyst, Meraki)](#platform-context-ios-xe-catalyst-meraki)
7. [Deliverable checklist](#deliverable-checklist)
8. [Peer handoffs](#peer-handoffs)

## Role and boundaries

This skill covers **CCNP-level enterprise networking**: multi-site campuses, branch WAN attachment, and integrated security/assurance at the **network engineering** layer. Depth is **design and operational workflow**, not CCIE lab scripting or certification item memorization.

**In scope:**

- Three-tier and collapsed-core campus designs
- L2/L3 integration for wired and wireless attachment
- Enterprise IGP (OSPF, EIGRP) and **BGP fundamentals** at WAN/DC edge
- FHRP, redistribution, IPv4/IPv6 dual-stack planning
- Enterprise QoS, ACLs, 802.1X at access/distribution
- SNMP, NetFlow/IPFIX, syslog, and basic telemetry for assurance
- Structured troubleshooting on Cisco platforms

**Out of scope (use peer skills):**

| Topic | Skill |
|---|---|
| Internet/peering/DCI BGP policy at carrier scale | `network-backbone-architect` |
| SD-WAN template/overlay day-two ops | `sd-wan-engineer` |
| AWS/Azure/GCP VPC and cloud IaC | `cloud-engineer` |
| RF planning, RRM, and WLAN mobility depth | `wireless-wifi-mobility-specialist` |
| SOC 2 / ISO audit programs | `information-security-engineer` |
| Rack/cable plant without routing design | `infrastructure-engineer` |
| IoT/OT protocols and plant gateways | `iot-network-edge-engineer` |

## CCNP Enterprise alignment

Map work to common **CCNP Enterprise** themes without treating the skill as an exam guide:

| Domain (conceptual) | This skill emphasizes |
|---|---|
| Architecture | Hierarchy, modularity, failure domains, dual-stack |
| Virtualization | VLANs, VRF-lite at enterprise edge, overlay handoff to SD-WAN |
| Infrastructure | Switching, routing, FHRP, WAN attachment |
| Network assurance | Baselines, flows, SNMP, structured TSHOOT |
| Security | 802.1X, ACLs, CPP, device hardening at network layer |
| Automation | NETCONF/RESTCONF awareness; Git-backed config discipline |

**Do not** reproduce exam item banks, brain-dump answers, or unauthorized certification content.

## Campus hierarchy model

Typical **enterprise campus** roles:

```
[ Access ] ──► [ Distribution ] ──► [ Core ] ──► [ WAN / DC edge ]
     │                  │                │
  User VLANs      L3 + FHRP         High-speed
  802.1X          Summarization      routing
  PoE             ACL inspection     BGP (if edge)
```

**Collapsed core** (distribution + core combined) is valid for smaller sites when:

- East-west traffic stays local or hairpins acceptably
- STP domain and FHRP ownership remain documented
- Growth path to three-tier is captured in the design record

Label **failure domains**: one access switch failure vs distribution pair vs WAN path.

## Discovery checklist

Gather before locking VLAN or routing design:

| Input | Why it matters |
|---|---|
| Site count and criticality tier | Hub vs spoke, FHRP placement |
| User/device counts per VLAN | Subnet sizing, DHCP scope |
| Application latency/jitter needs | QoS classes, local vs central services |
| Wireless controller model | L2 adjacency, guest segmentation |
| Existing IGP and pain points | Migration vs greenfield |
| WAN type (MPLS, DIA, SD-WAN) | Handoff to `sd-wan-engineer` or backbone peer |
| Security zones (PCI, guest, IoT) | VRF/VLAN map; defer OT depth to IoT peer |
| Operations tooling | SNMP, NetFlow, syslog, ticketing integration |
| Change windows and rollback | Maintenance discipline |

Minimum artifacts:

- **Traffic matrix** (site × site × app × peak Mbps) — simplified is acceptable
- **RTO** for single-link and single-node failure at distribution
- **Address plan** with summarization boundaries documented

## Addressing and naming

**IPv4:**

- Use **RFC1918** with deliberate summarization at distribution/core
- Reserve point-to-point `/30` or `/31` (where supported) for routed links
- Document **DHCP relay** placement (distribution vs centralized)

**IPv6:**

- Plan **dual-stack** or IPv6-only islands with documented DNS/NTP reachability
- Unique Local (ULA) vs global — align with WAN and cloud peers early

**Naming:**

- Consistent hostname scheme (`site-role-id`)
- Interface descriptions: remote device, circuit ID, VLAN purpose
- Document **VRF** names if used (guest, voice, management)

## Platform context (IOS-XE, Catalyst, Meraki)

| Platform | Typical use in this skill |
|---|---|
| **Catalyst** (access/distribution) | STP, EtherChannel, stacking, 802.1X |
| **IOS-XE** (routers, L3 switches) | OSPF/EIGRP/BGP, FHRP, QoS, WAN interfaces |
| **Meraki** (cloud-managed) | Simplified campus/branch; document API/dashboard limits vs CLI designs |

When Meraki and traditional IOS-XE coexist:

- Document **automation boundary** (dashboard templates vs CLI/Git)
- Align **VLAN and subnet** plans across both worlds
- Escalate **advanced routing policy** to backbone or SD-WAN peers

## Deliverable checklist

- [ ] Site inventory with tier and platform list
- [ ] Logical topology (L2/L3 boundaries, FHRP, summarization points)
- [ ] VLAN/VRF matrix with security zone labels
- [ ] Routing protocol selection with area/AS rationale
- [ ] WAN/SD-WAN attachment diagram with peer ownership
- [ ] QoS policy summary (classes, markings, queue roles)
- [ ] Assurance targets (SNMP OIDs/polls, flow exporters, syslog)
- [ ] TSHOOT playbook outline for top three failure scenarios

## Peer handoffs

| Trigger | Hand off to |
|---|---|
| Full-mesh BGP, IX/peering, anycast, DCI L3 | `network-backbone-architect` |
| vManage templates, ZTP, overlay path selection | `sd-wan-engineer` |
| VPC, TGW, Direct Connect, cloud VPN | `cloud-engineer` |
| Survey, channel width, 802.11k/v/r design | `wireless-wifi-mobility-specialist` |
| Audit control mapping and evidence | `information-security-engineer` |
| Smart building sensors, BACnet, edge gateways | `iot-network-edge-engineer` |
