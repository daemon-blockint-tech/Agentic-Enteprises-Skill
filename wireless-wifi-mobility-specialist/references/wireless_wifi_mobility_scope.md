# Wireless Wi-Fi mobility scope

## Table of contents

1. [Role and boundaries](#role-and-boundaries)
2. [Stakeholders and inputs](#stakeholders-and-inputs)
3. [Mobility and venue model](#mobility-and-venue-model)
4. [Device and application classes](#device-and-application-classes)
5. [Design constraints](#design-constraints)
6. [Deliverable checklist](#deliverable-checklist)
7. [Handoffs to peer skills](#handoffs-to-peer-skills)

## Role and boundaries

The wireless (Wi-Fi) mobility specialist owns **enterprise WLAN design, deployment, and optimization** for users and devices that move across coverage areas. Scope includes:

- **RF and coverage/capacity** — surveys, AP placement, antenna selection, and interference planning
- **802.11 architecture** — Wi-Fi 5/6/6E/7 feature selection at design level (not chipset driver debugging)
- **SSID and segmentation** — VLAN mapping, firewall/NAC attachment, guest and IoT isolation
- **Enterprise security** — WPA2/WPA3-Enterprise, 802.1X/EAP, RADIUS, and captive portal patterns
- **Mobility** — roaming (802.11k/r/v), band steering, sticky clients, voice/video continuity
- **Platform model** — controller-based, cloud-managed, or distributed (controllerless) WLAN
- **High-density and specialty venues** — stadium, warehouse, healthcare, education, hospitality
- **Outdoor and mesh** — point-to-point bridging, mesh backhaul constraints, and weather-rated gear
- **Integration** — wired LAN distribution, PoE, DHCP/DNS, DNS filtering, and SD-WAN edge breakout
- **Operations** — KPI baselines, troubleshooting (SNR, retries, DFS), and change management

Out of scope (defer to peer skills):

| Topic | Skill |
|---|---|
| Cellular RAN, 5G core, CBRS-only private LTE | Specialist cellular roles; this skill only for **Wi-Fi coexistence** |
| Carrier BGP/MPLS, IX, internet backbone | `network-backbone-architect` |
| SD-WAN overlay, path selection, SASE WAN policy | `sd-wan-engineer` |
| Cloud landing zone, VPC, managed cloud networking | `cloud-architect`, `cloud-engineer` |
| Cloud CSPM, cloud IAM guardrails | `cloud-security-engineer` |
| Endpoint MDM, app delivery, desktop support | Out of scope unless WLAN policy for those devices |
| Terraform/K8s/platform without WLAN design | `infrastructure-engineer` |
| SRE on-call, error budgets, incident process | `site-reliability-engineer` |
| OT/ICS plant wireless, ISA wireless in manufacturing | `scada-ics-cyber-security-specialist` |
| Corporate GRC program without WLAN architecture | `information-security-engineer` |

## Stakeholders and inputs

Gather before locking AP count or SSID matrix:

| Stakeholder | Typical inputs |
|---|---|
| Facilities / real estate | floor plans, ceiling height, construction materials, mounting restrictions |
| Network engineering | VLAN/IP plan, routing, DHCP scopes, DNS, firewall zones |
| Security / IAM | 802.1X methods, certificate strategy, NAC policies, guest compliance |
| Applications (voice, VDI, clinical) | latency, roaming, multicast/broadcast needs |
| Operations / NOC | monitoring tools, change windows, spare AP inventory |
| Vendors / integrators | controller limits, licensing, country regulatory domains |

Minimum discovery artifacts:

- **Floor plans** with scale (CAD/PDF) and marked user density zones
- **Device inventory** — laptops, phones, scanners, VoIP handsets, medical/IoT classes
- **Existing WLAN** — controller model, firmware train, pain points (roaming, drops, density)
- **Uplink and PoE** — switch models, PoE budget per closet, fiber/copper paths to IDF
- **Compliance** — PCI, HIPAA, guest logging, lawful intercept (if applicable)

## Mobility and venue model

Define **mobility domains**—areas where a client should roam without re-auth or with fast transition:

| Venue class | Mobility expectation | Design emphasis |
|---|---|---|
| Open office | Seamless L2 roam within floor | Consistent SSID, 11r if voice, adequate overlap |
| Campus outdoor | Cross-building roam | Cell sizing, min RSSI, controller RF groups |
| Warehouse / DC | Fast roam for scanners | Narrow cells, 5 GHz preferred, low retry rate |
| Healthcare | Voice + location; strict isolation | Separate voice SSID, 11r, medical IoT segmentation |
| Stadium / arena | Extreme density | High AP count, directional antennas, band split |
| Guest / retail | Captive portal, limited east-west | Guest VLAN, DNS filtering, bandwidth limits |

Document **sticky client** risk areas (far corners, legacy devices, printers) and mitigation (min RSSI, disassociation, band steering).

## Device and application classes

Build a **device × application matrix**:

| Class | Examples | WLAN implications |
|---|---|---|
| Corporate BYOD/COPE | laptops, phones | WPA3-Enterprise, 802.1X, device profiling |
| Voice / UC | Wi-Fi handsets, Teams phone | 11r, QoS (WMM), dedicated SSID, low jitter |
| VDI / real-time apps | Citrix, Zoom-heavy sites | 5/6 GHz, adequate SNR, avoid hidden node |
| IoT / building systems | cameras, sensors | Isolated SSID/VLAN, PSK or MPSK, no lateral paths |
| Industrial handheld | barcode scanners | Predictable roam, often 5 GHz-only capable |
| Guest | visitors, contractors | Captive portal, bandwidth cap, internet-only |

## Design constraints

Document non-negotiables early:

- **Regulatory domain** — country code, max EIRP, DFS radar detection requirements
- **Vendor strategy** — single-vendor WLAN vs multi-vendor with standardized features
- **Controller placement** — on-prem HA pair vs cloud-managed (Meraki, Aruba Central, etc.)
- **IPv6** — dual-stack SSIDs, RA guard, and DHCPv6 on wireless VLANs
- **Multicast** — IGMP snooping, multicast-to-unicast conversion for large venues
- **Cable plant** — Cat6A for 2.5/5 Gb uplinks; fiber to IDF; max PoE per switch
- **Change velocity** — template-based config vs per-AP customization

## Deliverable checklist

| Deliverable | Contents |
|---|---|
| WLAN requirements doc | venues, density, devices, NFRs (roam time, availability) |
| RF survey report | heatmaps, AP locations, predicted SNR, interference notes |
| Logical design | SSID matrix, VLANs, ACLs, RADIUS/NAC, guest flow |
| Radio plan | channels, widths, power, DFS, band steering policy |
| Bill of materials | AP models, antennas, licenses, mounting hardware |
| Test plan | coverage walk, roam test, throughput, failover, guest auth |
| Operations pack | monitoring KPIs, config backup, upgrade train, runbooks |

## Handoffs to peer skills

| Handoff | When | Peer |
|---|---|---|
| Default gateway, routing, and firewall between VLANs | After SSID/VLAN design | `network-backbone-architect` (if routed core), LAN team |
| Branch internet breakout and SD-WAN policy | Guest/SaaS hairpin vs local breakout | `sd-wan-engineer` |
| Hybrid cloud connectivity for RADIUS or guest | Auth in cloud, tunnel requirements | `cloud-engineer`, `cloud-architect` |
| Security control mapping (NAC, SIEM) | Posture and logging | `information-security-engineer` |
| Physical install, rack, PoE switches | AP mounting and switch ports | `infrastructure-engineer` |
| Production SLOs and incident process | WLAN as tier-1 service | `site-reliability-engineer` |
| Plant floor OT wireless | ISA, safety, protocol isolation | `scada-ics-cyber-security-specialist` |
