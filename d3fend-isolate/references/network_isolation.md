# Network Isolation

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Network Isolation | General isolation |
| Broadcast Domain Isolation | VLAN segmentation |
| Directional Network Link | One-way gateways |
| DNS Allowlisting | Permit DNS |
| DNS Denylisting | Block DNS |
| Forward Resolution Domain Denylisting | Block domains |
| Hierarchical Domain Denylisting | Block hierarchies |
| Homoglyph Denylisting | Block homoglyphs |
| Forward Resolution IP Denylisting | Block IPs |
| Reverse Resolution IP Denylisting | Block reverse |
| Encrypted Tunnels | VPN/encryption |
| Network Traffic Filtering | General filtering |
| Inbound Traffic Filtering | Ingress filtering |
| Email Filtering | Mail filtering |
| Outbound Traffic Filtering | Egress filtering |

## Segmentation Strategies

### VLAN Segmentation

```
VLAN 10: Management (restricted access)
VLAN 20: Production servers
VLAN 30: Development
VLAN 40: Guest (internet only)
VLAN 50: IoT (isolated, monitored)
```

### Micro-segmentation

```
Per-workload policies: Allow only required flows
Implementation: Host-based firewall, SDN, service mesh
Example: App A → DB B only, all else denied
```

### DNS Controls

| Control | Implementation |
|---|---|
| Allowlisting | Only resolve approved domains |
| Denylisting | Block known malicious domains |
| Response policy zones | Sinkhole malicious DNS |
| DNSSEC | Validate DNS responses |

### Traffic Filtering

| Direction | Rules |
|---|---|
| Inbound | Deny all, allow specific ports/sources |
| Outbound | Deny unexpected, alert on anomalies |
| Internal | Restrict lateral movement |

### Encrypted Tunnels

| Type | Use Case |
|---|---|
| Site-to-site VPN | Branch office connectivity |
| Client VPN | Remote worker access |
| TLS everywhere | Internal service encryption |
| IPsec | Network layer encryption |
