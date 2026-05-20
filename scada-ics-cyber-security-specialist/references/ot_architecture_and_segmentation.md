# OT architecture and segmentation

## Table of contents

1. [Purdue model (practitioner view)](#purdue-model-practitioner-view)
2. [Zones and conduits](#zones-and-conduits)
3. [Crown jewels and data flows](#crown-jewels-and-data-flows)
4. [Secure remote access](#secure-remote-access)
5. [IT/OT convergence risks](#itot-convergence-risks)
6. [Architecture review checklist](#architecture-review-checklist)

## Purdue model (practitioner view)

| Level | Typical assets | Security focus |
|---|---|---|
| L5 | Enterprise ERP, business apps | Keep out of direct OT paths |
| L4 | MES, plant scheduling, lab LIMS | Conduit to L3 only; no flat routing to L1 |
| L3 | SCADA servers, historians, OPC, domain for OT | Patch cadence, jump hosts, AV exceptions documented |
| L2 | HMIs, engineering workstations | Strong auth, removable media policy, gold images |
| L1 | PLCs, RTUs, intelligent devices | No direct internet; minimal protocols; change control |
| L0 | Sensors, actuators, field buses | Physical access; no security tools inline that add latency |

**Goal:** enforce **defense in depth** so compromise at one level does not imply full plant control.

## Zones and conduits

- **Zone** — collection of assets with common security requirements and trust boundary
- **Conduit** — controlled path between zones (firewall rules, data diode, unidirectional gateway, application proxy)

**Patterns:**

| Pattern | Use when |
|---|---|
| OT DMZ | Need to expose historians, OPC, or patch relay without placing servers in L3 core |
| Dual-homed servers | Avoid; prefer explicit conduit with documented rules |
| Industrial firewall | Stateful inspection aware of ICS protocols (vendor-specific) |
| Outbound-only from OT | Reduce C2; allowlist update and time sync paths |

Document for each conduit: **source/dest zones**, **protocols/ports**, **direction**, **business justification**, **owner**.

## Crown jewels and data flows

Prioritize protection for:

- Engineering workstations and project files (logic, recipes)
- PLC/RTU configuration interfaces
- SCADA master and redundancy pairs
- Historians and backup stores (long-term process data)
- Remote access gateways and VPN concentrators into OT
- Protocol translators (Modbus TCP ↔ serial, OPC UA gateways)

Map **northbound** (OT → IT/enterprise) and **southbound** (IT → OT) flows separately; convergence often hides in **OPC**, **SQL replication**, and **RDP jump boxes**.

## Secure remote access

| Control | Intent |
|---|---|
| Jump server in DMZ | No direct VPN to L1/L2 |
| PAM + MFA | Individual accountability; no shared vendor passwords |
| Session recording | Forensics and vendor accountability |
| Time-bound access | Vendor windows aligned with maintenance |
| Split tunnel disabled | Prevent lateral from vendor laptop into OT |
| Allowlist maintenance | Only required IPs and protocols during window |

**Vendor access:** contract clauses for malware-free media, notification of personnel changes, and incident contact.

## IT/OT convergence risks

| Risk | Indicators | Mitigations (high level) |
|---|---|---|
| Shared Active Directory | OT HMIs joined to corp domain | Tiered admin, GPO hardening, separate OU; consider workgroup or OT-specific directory |
| Cloud historians | Process data leaves site | Encryption, private link, data classification, retention |
| IT helpdesk RDP to OT | Ad-hoc support paths | Formal jump architecture only |
| Wireless in plant | Rogue AP, guest bleed | Segmented SSID, monitoring, no bridge to control VLAN |
| USB and removable media | Stuxnet-class spread | Port control, scanning stations, gold images |
| Supply chain | Compromised project files | Hash verification, vendor SBOM where available |

## Architecture review checklist

- [ ] Diagram shows all zones L0–L5 present on site (or explicit exclusions)
- [ ] Every cross-zone path is a named conduit with rules
- [ ] No undocumented dual-homed devices
- [ ] Remote access lands in DMZ/jump, not on PLC subnets
- [ ] Engineering workstations cannot reach internet without proxy controls
- [ ] Backup and patch paths documented and monitored
- [ ] SIS/BPCS separation validated with process safety (no security changes to SIS without safety review)
