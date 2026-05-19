# Network Mapping

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Network Mapping | Overall topology discovery |
| Logical Link Mapping | Layer 3 connections |
| Active Logical Link Mapping | Scan-based discovery |
| Passive Logical Link Mapping | Flow-based inference |
| Network Traffic Policy Mapping | Firewall/rule mapping |
| Physical Link Mapping | Cabling and physical topology |
| Active Physical Link Mapping | Probing physical paths |
| Direct Physical Link Mapping | Direct connection tracing |

## Mapping Methods

### Logical Topology

```
Discovery: SNMP, LLDP, CDP, routing tables
Visualization: Layer 3 diagram with subnets, VLANs, routers
Update frequency: Weekly or on change
```

### Physical Topology

```
Discovery: Cable tracing, port mapping, DCIM tools
Visualization: Rack elevation, cable runs, power paths
Update frequency: As-built after changes
```

### Traffic Policy Mapping

```
Sources: Firewall configs, cloud security groups, ACLs
Checks: Shadowed rules, overly permissive rules, unused rules
Frequency: Monthly review
```

## Tools
- Nmap, Masscan
- NetBox, phpIPAM
- Cisco Prime, SolarWinds
- CloudMapper, Cartography
