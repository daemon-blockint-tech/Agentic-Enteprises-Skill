# Hybrid & On-Premise Infrastructure

## Virtualization

### VMware vSphere

| Component | Purpose |
|---|---|
| ESXi | Hypervisor, runs VMs |
| vCenter | Management, orchestration |
| vSAN | Software-defined storage |
| NSX | Software-defined networking |
| vRealize | Automation, monitoring |

### KVM / QEMU
- Open source alternative to VMware
- Proxmox VE: Web UI for KVM + LXC
- oVirt: Enterprise virtualization management

### Hyper-V (Microsoft)
- Integrated with Windows Server
- Hyper-V Replica for DR
- Nested virtualization support

### Container on Bare Metal
| Orchestrator | Use Case |
|---|---|
| Kubernetes (Kubeadm, K3s, RKE2) | Production workloads |
| Nomad | Mixed workloads (containers + binaries) |
| Docker Swarm | Simple container clusters |

## Networking (On-Premise)

### Core Concepts
- **VLANs**: Logical network segmentation (L2)
- **Subnets**: IP range allocation (L3)
- **Routing**: Static vs dynamic (OSPF, BGP)
- **Switching**: Access, trunk, L3 switches

### Network Topology
```
Internet
  └── Firewall (Palo Alto, Fortinet, pfSense)
      └── Core Switch (L3)
          ├── DMZ VLAN
          ├── Production VLAN
          ├── Management VLAN
          └── Storage VLAN (iSCSI/NFS)
```

### SD-WAN
- Replace MPLS with internet + overlay
- Cloud on-ramps for SaaS optimization
- Vendors: Cisco Meraki, Fortinet, VMware VeloCloud

## Storage

### SAN (Storage Area Network)
- **Protocol**: Fibre Channel (FC), iSCSI, FCoE
- **Use case**: Databases, high-performance shared storage
- **Vendors**: Dell EMC, NetApp, HPE, Pure Storage

### NAS (Network Attached Storage)
- **Protocol**: NFS, SMB/CIFS
- **Use case**: File shares, home directories
- **Vendors**: NetApp, QNAP, Synology

### Object Storage (On-Premise)
- **MinIO**: S3-compatible, cloud-native
- **Ceph**: Distributed, unified block/file/object
- **Swift**: OpenStack object storage

### Storage Tiers

| Tier | Media | Use Case | Cost |
|---|---|---|---|
| Hot | NVMe SSD | Active databases | High |
| Warm | SATA SSD | Recent analytics | Medium |
| Cold | HDD | Archival, backups | Low |
| Frozen | Tape / Object | Long-term compliance | Very Low |

## Hybrid Cloud Connectivity

### VPN
- **Site-to-site**: IPsec VPN between on-prem and cloud
- **Client VPN**: Remote access for users
- **Limitation**: Bandwidth and latency constraints

### Direct Connect / ExpressRoute / Cloud Interconnect
- **Dedicated**: Private fiber connection to cloud
- **Benefits**: Lower latency, higher bandwidth, predictable pricing
- **Use case**: Hybrid databases, replication, large data transfers

### Hybrid Patterns

| Pattern | Description | Use Case |
|---|---|---|
| Burst to cloud | On-prem handles baseline, cloud for spikes | Seasonal workloads |
| DR to cloud | Primary on-prem, DR in cloud | Cost-effective DR |
| Data gravity | Data on-prem, compute in cloud | Compliance, latency |
| Cloud on-ramp | SD-WAN to cloud POP | SaaS optimization |

## Physical Data Center

### Design Considerations
- **Power**: UPS, generators, dual feeds, PDU redundancy
- **Cooling**: Hot/cold aisle containment, CRAC/CRAH units
- **Racking**: 42U-52U racks, weight limits, cable management
- **Fire suppression**: FM-200, inert gas (not water)
- **Security**: Biometric access, mantraps, CCTV

### Tier Classification (Uptime Institute)

| Tier | Availability | Redundancy | Downtime/Year |
|---|---|---|---|
| I | 99.671% | None | 28.8 hours |
| II | 99.741% | Partial | 22.7 hours |
| III | 99.982% | N+1 | 1.6 hours |
| IV | 99.995% | 2N+1 | 26.3 minutes |

## Hardware Lifecycle

### Procurement to Decommission
1. **Planning**: Capacity forecast, budget cycle
2. **Procurement**: Vendor selection, lead times
3. **Deployment**: Racking, cabling, imaging
4. **Operation**: Monitoring, maintenance
5. **Refresh**: 3-5 year replacement cycle
6. **Decommission**: Data wipe, disposal, asset recovery

### Asset Management
- Track: serial numbers, warranty, location, owner
- Tools: ServiceNow, Snipe-IT, GLPI
- Audit: Annual physical verification

## Migration Strategies

### Cloud Migration (7 Rs)

| Strategy | Effort | When |
|---|---|---|
| Retire | Low | No longer needed |
| Retain | Low | Not ready to move |
| Rehost (lift-and-shift) | Low | Quick move, optimize later |
| Relocate | Low | VMware to VMware on cloud |
| Repurchase | Medium | SaaS replacement |
| Replatform | Medium | Move + minor changes |
| Refactor | High | Cloud-native redesign |

### Database Migration
1. **Assessment**: Schema compatibility, feature gaps
2. **Replication**: Set up ongoing sync (DMS, Striim, Attunity)
3. **Cutover**: Brief downtime or blue-green switch
4. **Validation**: Data consistency checks, performance
5. **Decommission**: Stop replication, shut down source
