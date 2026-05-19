# Network and connectivity

## Table of contents

1. [Demarc and carriers](#demarc-and-carriers)
2. [Fabric roles](#fabric-roles)
3. [Hybrid to cloud](#hybrid-to-cloud)

## Demarc and carriers

- **MMR:** carrier handoff; diverse entry paths where tier requires
- **Cross-connects:** colo order lead time; label both ends
- **Diverse paths:** separate conduits/building entries; document shared risk (single bridge, etc.)

Contract: SLA for repair, LOA/CFA process, demarc extension standards.

## Fabric roles

| Layer | Facility scope |
|---|---|
| Core | Inter-row, exit to WAN |
| Distribution | Aggregation to top-of-rack |
| ToR | Server and storage NICs |

Out-of-band management network: separate switches/VLAN; no shared fate with production under failure.

Software-defined overlays and cloud networking → `infrastructure-engineer`.

## Hybrid to cloud

Document for each site:

- Primary cloud region and dedicated link (DX, ExpressRoute, Partner Interconnect, etc.)
- Bandwidth, latency RTT, failover path
- Encryption (MACsec, IPsec) and ownership

Latency-sensitive apps: place in region or site within RTT budget.
