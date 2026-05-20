---
name: Cisco Certified Network Professional
description: |
  Guides CCNP-level enterprise campus and WAN networking—VLAN/STP/RSTP/MST, EtherChannel, stacking,
  OSPF/EIGRP/BGP fundamentals, redistribution, FHRP (HSRP/VRRP/GLBP), IPv4/IPv6, WAN/SD-WAN design
  adjacency, assurance (SNMP, NetFlow/IPFIX, telemetry), 802.1X/ACLs/device hardening, enterprise QoS,
  and structured troubleshooting on IOS-XE, Catalyst, and Meraki. Use when the user mentions CCNP,
  Cisco Certified Network Professional, OSPF design, EIGRP, BGP enterprise, campus switching, STP
  troubleshooting, HSRP, enterprise routing, Catalyst switch, IOS-XE, network assurance,
  redistribution, VLAN design, or CCNP Enterprise—not carrier-scale BGP alone
  (network-backbone-architect), SD-WAN ops only (sd-wan-engineer), cloud IaC only (cloud-engineer),
  Wi-Fi RF depth (wireless-wifi-mobility-specialist), security audits (information-security-engineer),
  cabling without L3 (infrastructure-engineer), or IoT/OT edge (iot-network-edge-engineer).
---

# Cisco Certified Network Professional

## When to Use

- Design or troubleshoot **enterprise campus** LAN switching (VLANs, STP/RSTP/MST, EtherChannel, stacking)
- Plan **enterprise routing** (OSPF, EIGRP, BGP fundamentals, redistribution, summarization)
- Architect **WAN edge** services (FHRP, DMVPN/SD-WAN handoff points, QoS at branch/DC edge)
- Integrate **wireless** at L2/L3 boundaries (controller/AP attachment, guest segmentation touchpoints)
- Implement **network assurance** (SNMP, NetFlow/IPFIX, syslog, basic telemetry, baseline dashboards)
- Apply **security integration** (802.1X, ACLs, control-plane protection, device hardening) at the network layer
- Follow **structured troubleshooting** methodology on Cisco IOS-XE, Catalyst, and Meraki-managed campuses

## When NOT to Use

- Carrier- or internet-scale backbone BGP policy, peering, IX, and DCI as primary deliverable → `network-backbone-architect`
- SD-WAN controller policy, template lifecycle, and overlay operations as primary task → `sd-wan-engineer`
- Cloud VPC/VNet, landing zone, and cloud-native networking IaC only → `cloud-engineer`
- Wi-Fi RF surveys, channel planning, and mobility protocol depth → `wireless-wifi-mobility-specialist`
- Enterprise security program, SOC 2 evidence, or audit control mapping → `information-security-engineer`
- Physical cabling, rack/power, and DC build without routed campus design → `infrastructure-engineer`
- IoT/OT edge protocols, BACnet/Modbus gateways, and plant segmentation → `iot-network-edge-engineer`

## Related skills

| Need | Skill |
|---|---|
| Backbone BGP, WAN/MPLS, DCI, peering, spine-leaf at scale | `network-backbone-architect` |
| SD-WAN overlay operations, templates, and carrier handoff | `sd-wan-engineer` |
| Cloud networking implementation and hybrid connectivity | `cloud-engineer` |
| RF design, WLAN controllers, and mobility architecture | `wireless-wifi-mobility-specialist` |
| IaC, platform delivery, and DC physical build | `infrastructure-engineer` |
| IoT/OT edge connectivity and industrial protocols | `iot-network-edge-engineer` |
| Security program, IAM evidence, and audit readiness | `information-security-engineer` |

## Core Workflows

### 1. Scope and enterprise architecture

Clarify sites, user/device counts, critical apps, RTO for path loss, and Cisco platform mix (IOS-XE, Catalyst, Meraki).

**See `references/ccnp_scope_and_enterprise_architecture.md`.**

### 2. Campus switching and Layer 2

Design VLANs, STP domain, EtherChannel, stacking/VSS, and L2 security boundaries.

**See `references/campus_switching_and_layer2.md`.**

### 3. Routing (OSPF, EIGRP, BGP)

Select IGP, plan areas/AS, summarization, redistribution, and enterprise BGP at the edge.

**See `references/routing_ospf_eigrp_bgp.md`.**

### 4. WAN edge, QoS, and services

Place FHRP, WAN attachment, marking/queuing, and service modules (NAT, DHCP relay, multicast touchpoints).

**See `references/wan_edge_qos_and_services.md`.**

### 5. Assurance and troubleshooting

Baselines, flow telemetry, structured TSHOOT, and change/rollback discipline.

**See `references/assurance_troubleshooting_and_operations.md`.**

### 6. Security integration and automation basics

802.1X, ACL placement, control-plane hardening, and Git/NETCONF adjacency without replacing security engineering.

**See `references/security_integration_and_automation_basics.md`.**

## Outputs

- **Campus context** — sites, tiers, critical flows, and failure domains
- **L2/L3 design** — VLAN map, STP root plan, routing protocol choice, and summarization boundaries
- **Edge services matrix** — FHRP, QoS classes, WAN/SD-WAN attachment, and ACL inspection points
- **Assurance plan** — SNMP/flow targets, baseline KPIs, and escalation playbooks
- **Troubleshooting runbook** — layered checks (physical → L2 → L3 → app path) with evidence to capture
- **Handoff notes** — what to defer to backbone, SD-WAN, cloud, wireless, or security peers

## Principles

- **Hierarchy and summarization** — aggregate at distribution/core; keep access simple
- **Stability before features** — STP root, FHRP priority, and IGP metrics are operational contracts
- **Document redistribution** — tag, filter, and loop prevention are design requirements, not afterthoughts
- **QoS end-to-end** — classify at access; trust boundaries explicit at WAN edge
- **Measure, then tune** — baselines before micro-optimizing timers or metrics
- **Design guidance, not exam dumps** — teach trade-offs; do not facilitate certification cheating
