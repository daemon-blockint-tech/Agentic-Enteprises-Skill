# Assurance, troubleshooting, and operations

## Table of contents

1. [Network assurance stack](#network-assurance-stack)
2. [Baselines and KPIs](#baselines-and-kpis)
3. [SNMP and polling](#snmp-and-polling)
4. [Flow telemetry (NetFlow, IPFIX)](#flow-telemetry-netflow-ipfix)
5. [Syslog and telemetry basics](#syslog-and-telemetry-basics)
6. [Structured troubleshooting methodology](#structured-troubleshooting-methodology)
7. [Change management and rollback](#change-management-and-rollback)
8. [Evidence capture template](#evidence-capture-template)

## Network assurance stack

| Layer | Tooling (examples) | Purpose |
|---|---|---|
| Synthetic | IP SLA, TWAMP | Path availability and latency |
| Polling | SNMP, gNMI | Device health, interface counters |
| Flows | NetFlow, IPFIX | Who talks to whom, capacity |
| Logs | Syslog, AAA | Config changes, auth failures |
| Dashboards | NMS, Meraki, DNA Center | Operator single pane |

**CCNP depth:** specify **what to collect** and **thresholds**, not vendor SKU selection alone.

## Baselines and KPIs

Establish **7-day normal** before alerting:

| KPI | Typical source | Alert when |
|---|---|---|
| Interface utilization | SNMP ifIn/Out | >70% sustained 15m (tune per link) |
| CPU/memory | SNMP ENTITY | >80% sustained |
| STP topology change | Syslog | TCN storm |
| BGP prefixes | SNMP/CLI | Drop below learned baseline |
| Latency to gateway | IP SLA | Above SLA threshold |
| Error counters | SNMP | CRC/input errors increasing |

Document **business hours** vs **backup window** profiles separately.

## SNMP and polling

**Versions:** prefer **SNMPv3** (authPriv) on production; retire v2c community strings on internet-facing management.

**Polling discipline:**

- Poll interval matched to KPI (60s interface, 300s inventory)
- Limit **OID walks** on large switches during peak
- Use **interface indexes** consistently; re-index after reload

**Useful categories:**

- `ifTable` — status, errors, utilization
- `cpmCPU` / memory OIDs — control plane health
- Entity MIB — temperature, power supplies
- BGP/OSPF MIBs — neighbor state (validate against CLI during incidents)

## Flow telemetry (NetFlow, IPFIX)

**Exporter placement:** distribution or WAN edge — balance visibility vs export volume.

**Design checklist:**

- [ ] **Sampler** rate on high-speed links
- [ ] **Exporter** destination capacity (collector sizing)
- [ ] **Template** refresh for flexible NetFlow v9/IPFIX
- [ ] **Retention** aligned with security investigations (coordinate with security peer)

**Use cases:**

- Top talkers during congestion
- Verify QoS class distribution
- Post-incident **five-tuple** reconstruction (not a substitute for full PCAP on all links)

## Syslog and telemetry basics

**Syslog:**

- Centralize with **NTP-synced** timestamps
- Severity filtering: ERR/CRIT to paging; INFO for config audit
- Separate **management VRF** transport where possible

**Streaming telemetry (awareness):**

- gRPC/gNMI for high-cardinality counters
- Model-driven telemetry complements SNMP for spine-leaf at scale
- Document subscription paths in automation runbooks

**Meraki:** dashboard events and flow logs — map to enterprise SIEM fields for hybrid campuses.

## Structured troubleshooting methodology

Use a **consistent layer model** (adapt to symptom):

```
1. Scope     — Who/what/VLAN/site? When started? Recent change?
2. Physical  — Link up? Errors? PoE? Optics?
3. L2        — VLAN, trunk, MAC, STP blocking?
4. L3        — ARP, FHRP, routing table, ACL?
5. Path      — Traceroute, CEF, PMTU, asymmetric routing?
6. App       — DNS, firewall, proxy (hand off if app-owned)
```

**Divide-and-conquer:**

- Test from **known-good** port or device
- Compare **working vs broken** VLAN or site
- **Isolate** change — rollback if within maintenance window

**Avoid:**

- Random timer tuning without evidence
- Clearing routing tables during peak without capture
- Sharing configs with PII or live credentials in tickets

## Change management and rollback

| Step | Action |
|---|---|
| Plan | Rollback config snippet stored in ticket |
| Pre-check | Baseline show commands archived |
| Window | Notify NOC; freeze parallel changes |
| Execute | One logical change per window when possible |
| Verify | KPI + functional test from user VLAN |
| Post | Update diagram and IPAM if addressing changed |

**Golden config:** Git-backed templates for IOS-XE; Meraki network bind notes for dashboard.

## Evidence capture template

Paste into incident tickets:

```
Device:
Symptom:
Scope (users/VLAN/sites):
Time started (TZ):
Recent changes:
---
show ip interface brief
show vlan brief
show spanning-tree vlan <id>
show standby brief
show ip route <dst>
show ip ospf neighbor
show ip bgp summary
show interfaces <if> counters errors
traceroute <dst> source <src>
---
Resolution:
Root cause category: L1 / L2 / L3 / WAN / Security / External
```

For chronic issues, open **problem record** with trend graphs from NMS.
