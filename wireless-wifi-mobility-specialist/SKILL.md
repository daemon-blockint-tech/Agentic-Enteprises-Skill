---
name: wireless-wifi-mobility-specialist
description: |
  Enterprise WLAN for mobile users—RF/site surveys, AP placement, 802.11 (Wi-Fi 5/6/6E/7), channel/power
  planning, SSID/VLAN segmentation, WPA3/802.1X/RADIUS, guest/captive portal, roaming (802.11k/r/v, band
  steering), high-density and mesh/outdoor, LAN/SD-WAN edge integration, troubleshooting (SNR, DFS, CCI).
  This skill should be used when the user asks about Wi-Fi, wireless mobility, WLAN design, wireless survey,
  AP placement, 802.11, Wi-Fi 6, Wi-Fi 6E, roaming, 802.11k, 802.11r, band steering, WPA3, 802.1X,
  enterprise wireless, high density Wi-Fi, channel planning, RF interference, wireless troubleshooting,
  Aruba, Meraki wireless, or Cisco wireless—not cellular RAN/5G core, MPLS/BGP backbone
  (network-backbone-architect), SD-WAN overlay (sd-wan-engineer), cloud VPC only (cloud-architect), MDM-only,
  or OT ISA wireless (scada-ics-cyber-security-specialist).
---

# Wireless (Wi-Fi) Mobility Specialist

## When NOT to Use

- Cellular RAN, 5G core, or private LTE/CBRS-only design → defer unless **Wi-Fi coexistence** or dual-connectivity is the question
- Carrier BGP/MPLS backbone, IX peering, or internet routing design → `network-backbone-architect`
- SD-WAN overlay topology, path selection, and SASE insertion as primary deliverable → `sd-wan-engineer`
- Cloud landing zone, VPC design, and managed cloud service selection → `cloud-architect`
- Cloud network security guardrails, CSPM, and cloud IAM as primary deliverable → `cloud-security-engineer`
- Terraform modules, physical DC build, and K8s platform delivery without WLAN design → `infrastructure-engineer`
- Corporate security program, IdP, and endpoint controls without wireless architecture → `information-security-engineer`
- SLO programs, on-call, and production incident process as main task → `site-reliability-engineer`
- OT/ICS segmentation, Purdue model, and plant industrial wireless (ISA) → `scada-ics-cyber-security-specialist`

## Related skills

| Need | Skill |
|---|---|
| Routed backbone, BGP/MPLS, DCI, and internet edge | `network-backbone-architect` |
| SD-WAN overlay, underlay, branch breakout, and path policy | `sd-wan-engineer` |
| Cloud reference architecture and hybrid connectivity | `cloud-architect` |
| Implement cloud networking and managed connectivity | `cloud-engineer` |
| Cloud network security controls and posture | `cloud-security-engineer` |
| IaC, physical build, cabling, and platform delivery | `infrastructure-engineer` |
| Enterprise security program and control catalog | `information-security-engineer` |
| Reliability engineering, SLOs, and production incidents | `site-reliability-engineer` |
| OT/ICS plant networks and industrial wireless context | `scada-ics-cyber-security-specialist` |

## Core Workflows

### 1. Scope, constraints, and mobility requirements

Clarify venue types, device classes, density, roaming domains, and compliance.

**See `references/wireless_wifi_mobility_scope.md`.**

### 2. RF survey and AP placement

Plan predictive/active surveys, coverage vs capacity, and mounting constraints.

**See `references/rf_survey_and_ap_planning.md`.**

### 3. Standards, channels, and capacity

Select Wi-Fi generations, band plan, channel width, power, and DFS/regulatory constraints.

**See `references/standards_channels_and_capacity.md`.**

### 4. Security, 802.1X, and segmentation

Design SSIDs, VLANs/VRFs, WPA-Enterprise, guest/captive portal, and RADIUS/NAC handoffs.

**See `references/security_8021x_and_segmentation.md`.**

### 5. Roaming, density, and performance

Optimize 802.11k/r/v, band steering, high-density RF, and sticky-client mitigation.

**See `references/roaming_density_and_performance.md`.**

### 6. Operations, troubleshooting, and integration

Integrate with LAN/SD-WAN edge, monitor KPIs, and troubleshoot SNR, retries, and interference.

**See `references/operations_troubleshooting_integration.md`.**

## Outputs

- **WLAN context** — sites/venues, device mix, density tiers, and roaming expectations
- **RF and AP plan** — survey method, AP map, antenna/orientation notes, and capacity model
- **Radio design** — band/channel plan, power limits, DFS strategy, and interference mitigations
- **SSID and segmentation matrix** — auth method, VLAN/ACL, firewall/NAC attachment
- **Roaming and density brief** — 11k/r/v, band steering, min RSSI, and venue-specific tuning
- **Operations baseline** — controller/cloud model, monitoring KPIs, and escalation runbooks
- **Integration notes** — uplink to distribution, PoE budget, DHCP/DNS, and SD-WAN/local breakout hooks

## Principles

- **Design for mobility first** — roaming domains and sticky clients drive AP density more than coverage alone
- **Measure RF, do not guess** — validate with survey tools and post-deploy verification walks
- **Separate roles by SSID** — corporate, guest, IoT, and voice each get explicit policy and VLAN paths
- **Prefer 5 GHz/6 GHz for capacity** — use 2.4 GHz deliberately for reach or legacy, not default overlap
- **Align security with NAC** — 802.1X and RADIUS are architecture decisions, not AP checkbox settings
- **Document vendor-agnostic intent** — capture requirements before locking controller-specific features
