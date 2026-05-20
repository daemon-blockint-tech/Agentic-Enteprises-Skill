# OT detection and incident response

## Table of contents

1. [Detection philosophy](#detection-philosophy)
2. [ICS protocols (high level)](#ics-protocols-high-level)
3. [Monitoring patterns](#monitoring-patterns)
4. [OT threat classes](#ot-threat-classes)
5. [Safety-first incident response](#safety-first-incident-response)
6. [Coordination with IT IR](#coordination-with-it-ir)
7. [Tabletop and exercise hooks](#tabletop-and-exercise-hooks)

## Detection philosophy

- **Prefer passive** collection on OT SPAN/taps; avoid inline devices that add latency or single points of failure
- **Baseline behavior** — normal Modbus/DNP3/OPC patterns per unit; alert on engineering changes and new masters
- **Correlate** OT alerts with IT identity, VPN, and EDR where conduits exist
- **Tune with operations** — reduce false positives that desensitize operators

Corporate SOC (`soc-analyst`) may lack OT context—define **handoff criteria** and **shared runbooks**.

## ICS protocols (high level)

| Protocol | Typical use | Security notes (awareness) |
|---|---|---|
| Modbus TCP/RTU | PLC I/O, simple masters | No auth in classic Modbus; function code abuse; serial gateways |
| DNP3 | Electric utilities, water | Secure authentication exists but often not deployed; unsolicited responses |
| OPC UA / Classic | HMI, historians, MES | UA has security model; classic DCOM risks on legacy Windows |
| BACnet | Building automation crossing into plant | Often flat UDP; check IT/OT boundary |
| EtherNet/IP, PROFINET | Industrial Ethernet | Vendor-specific; CIP objects; time-sensitive |
| IEC 61850 | Substations | MMS/GOOSE; specialized monitoring |

Detection content should reference **function codes**, **new client IPs**, **write operations** to sensitive registers, and **firmware download** sequences—without prescribing unsafe active tests.

## Monitoring patterns

| Use case | Signal (examples) |
|---|---|
| Unauthorized engineering | New project upload, PLC mode change, unexpected EWS login |
| Remote access abuse | Vendor session outside window; concurrent sessions |
| Lateral movement | IT malware beaconing from HMI subnet |
| Historian exfil | Large northbound SQL/OPC export |
| Protocol anomaly | Modbus write from non-master IP |
| Asset drift | New MAC on control VLAN |

Integrate with SIEM where possible; maintain **OT-specific dashboards** for operations liaisons.

## OT threat classes

High-level awareness (not attribution):

| Class | Characteristics | Practitioner response themes |
|---|---|---|
| Ransomware / wiper | IT spread into OT; loss of HMIs | Isolate with operations; restore from gold; see BCM skills |
| Living-off-the-land | Legitimate RDP, VPN, OPC abuse | Session review; conduit tightening |
| ICS-specific malware | TRITON (safety controller targeting), Industroyer (protocol modules) | Vendor advisories; integrity checks on logic; national CERT |
| Supply chain | Trojanized project files, compromised vendor | Hash controls; rebuild EWS; vendor investigation |
| Insider / maintenance | Legitimate credentials misused | PAM, recording, dual control |

Route deep **malware analysis** and **legal** coordination to `incident-responder` and forensics partners.

## Safety-first incident response

**Before cyber actions**, establish:

- **Operations commander** — authority to stop process, safe shutdown state
- **Process safety contact** — SIS not disabled for “cleanup”
- **Communication plan** — control room, field ops, executives

Phased approach:

1. **Detect & confirm** — validate not false positive; preserve SPAN captures
2. **Triage impact** — which zones, safety vs production systems
3. **Contain (approved)** — block conduit, disable remote access, **avoid** abrupt PLC power-off unless ops directs
4. **Eradicate** — reimage EWS/HMI from gold; replace logic only from known-good backup
5. **Recover** — staged restore; functional tests per operations checklist
6. **Learn** — AAR with safety and IT IR; update roadmaps

**Prohibited without ops approval:** mass password changes that lock operators out, antivirus full scans on realtime servers during peak production, active scanning of PLCs.

## Coordination with IT IR

| OT lead owns | IT IR (`incident-responder`) owns |
|---|---|
| Zone isolation plan | Enterprise containment, AD, email |
| PLC/logic integrity checks | Endpoint forensics on corp laptops |
| Control room comms | Legal, regulator notification (with counsel) |
| Vendor OEM engagement | Threat intel enrichment |
| Process restart sequencing | Identity reset, SaaS recovery |

Single **incident timeline**; tag evidence as OT vs IT.

## Tabletop and exercise hooks

Scenarios: ransomware in DMZ, rogue engineering laptop, lost VPN creds into jump host, false positive flood on Modbus alerts.

Inject **safety decisions** (unit trip vs degraded run). Capture gaps for `hardening_roadmaps_and_evidence.md`.

For **threat hunting** on IT-only telemetry, use `threat-hunter`; for **pentest validation**, use `penetration-tester` in lab or agreed test beds—not production OT.
