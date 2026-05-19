---
name: d3fend-model
description: |
  Guides cybersecurity asset modeling, inventory, and vulnerability assessment using MITRE D3FEND.
  Covers asset inventory (hardware, software, network, data, containers), network mapping,
  vulnerability enumeration, dependency mapping, and operational risk assessment.
  Use when building CMDBs, running asset discovery, mapping network topology, assessing
  vulnerabilities, or modeling organizational cyber posture—not for hardening controls
  (d3fend-harden), detection engineering (d3fend-detect), or incident response (d3fend-evict).
---

# D3FEND — Model

## When to Use

- Building or auditing asset inventories (hardware, software, network, data)
- Mapping network topology and logical/physical links
- Running vulnerability assessments and enumerating exposures
- Modeling operational dependencies and service mappings
- Assessing organizational cyber risk posture
- Analyzing container images and configurations

## When NOT to Use

- Implementing hardening controls → `d3fend-harden`
- Designing detection rules or monitoring → `d3fend-detect`
- Network segmentation or access mediation → `d3fend-isolate`
- Incident response or eviction actions → `d3fend-evict`
- General enterprise security program design → `cybersecurity`

## Core Workflows

### 1. Asset Inventory

| Asset Type | What to Capture | Tools |
|---|---|---|
| Hardware | Devices, firmware, components | Lansweeper, Nmap, agent-based discovery |
| Software | Installed apps, versions, licenses | SCCM, osquery, SBOM tools |
| Network | Nodes, interfaces, VLANs | Nmap, SNMP, network scanners |
| Data | Databases, file stores, sensitivity | Data classification tools |
| Containers | Images, registries, runtime inventory | Trivy, Docker Scout, Kubernetes APIs |

**See `references/asset_inventory.md`**

### 2. Network Mapping

- **Logical**: Layer 3 topology, routing paths, traffic policies
- **Physical**: Cable runs, rack layouts, wireless coverage
- **Active**: Scanning, probing, traceroute
- **Passive**: NetFlow, ARP tables, DHCP logs

**See `references/network_mapping.md`**

### 3. Vulnerability Assessment

1. Discovery → asset inventory
2. Scanning → Nessus, Qualys, OpenVAS
3. Analysis → CVSS scoring, exploitability, exposure
4. Prioritization → threat intel, asset criticality
5. Reporting → remediation timelines

**See `references/vulnerability_assessment.md`**

### 4. Dependency & Risk Mapping

- Service dependencies: upstream/downstream services
- Operational: business process → IT asset mapping
- Data exchange: flows, interfaces, protocols
- Access modeling: who can access what

**See `references/dependency_risk_mapping.md`**

## When to load references

- **Asset inventory** → `references/asset_inventory.md`
- **Network mapping** → `references/network_mapping.md`
- **Vulnerability assessment** → `references/vulnerability_assessment.md`
- **Dependency & risk mapping** → `references/dependency_risk_mapping.md`
