# Asset Inventory

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Asset Inventory | Central catalog of all assets |
| Asset Vulnerability Enumeration | Map vulnerabilities to assets |
| Container Image Analysis | Inventory and scan container images |
| Configuration Inventory | Track system configurations |
| Data Inventory | Catalog data stores and classifications |
| Hardware Component Inventory | Track physical components |
| Network Node Inventory | Catalog network devices |
| Software Inventory | Track installed applications |

## Implementation

### Discovery Methods

| Method | Coverage | Frequency |
|---|---|---|
| Active scanning | Network devices, open ports | Weekly |
| Agent-based | Endpoints, installed software | Continuous |
| Cloud APIs | IaaS/PaaS resources | Hourly |
| Passive (NetFlow) | Network topology | Continuous |
| Manual entry | Legacy, air-gapped systems | As needed |

### CMDB Structure

```yaml
Asset:
  id: unique_identifier
  type: [hardware|software|network|data|container]
  name: descriptive_name
  owner: team_or_person
  location: physical_or_cloud_region
  criticality: [critical|high|medium|low]
  compliance_scope: [PCI|HIPAA|SOX|etc]
  lifecycle: [active|maintenance|retired]
  vulnerabilities: []  # linked findings
  dependencies: []    # upstream/downstream
```

### Tools
- Lansweeper, ServiceNow CMDB
- Nmap, OpenVAS
- osquery, FleetDM
- Trivy, Docker Scout
- CloudMapper, Prowler

## SBOM Integration

- Generate SBOMs for all software
- Link SBOM components to vulnerabilities
- Track transitive dependencies
- Update on every release
