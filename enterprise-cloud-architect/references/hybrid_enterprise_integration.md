# Hybrid enterprise integration

## Table of contents

1. [Identity federation](#identity-federation)
2. [ERP and core systems](#erp-and-core-systems)
3. [Data center portfolio](#data-center-portfolio)
4. [Network diversity](#network-diversity)

## Identity federation

Enterprise standard:

- **Entra ID / AD** as IdP for cloud SSO
- **Conditional access** — MFA, device compliance, location
- **Privileged access** — PIM/JIT; break-glass monitored
- **Workload identity** — no static keys in applications

Map legacy apps on **LDAP sync** vs **SAML/OIDC** migration waves.

## ERP and core systems

Common integrations:

- SAP on cloud or RISE — latency and private connectivity
- Mainframe batch — scheduled transfer, not synchronous coupling
- Message buses — enterprise Kafka/Event Hub between on-prem and cloud

Architecture defines **integration zones** — DMZ, API gateway, ESB vs event mesh.

Detailed integration ADRs may involve `senior-system-architecture`.

## Data center portfolio

Align cloud burst and steady-state with **on-prem capacity**:

- Portfolio roadmap → `data-center-portfolio-planning-execution-lead`
- Utilization and GPU supply → `data-center-compute-supply-efficiency`
- New MW delivery → `senior-data-center-capacity-delivery-manager`

**Hybrid placement rule:** default cloud for elastic; on-prem for fixed high-utilization or license-bound unless strategy says otherwise.

## Network diversity

Enterprise hybrid requires:

- **Dual carriers** on ExpressRoute/Direct Connect/Interconnect
- **BGP** and failover testing
- **DNS** split-horizon and global load balancing strategy
- **Egress** inspection policy consistent cloud and on-prem

Document **single points of failure** in steering reviews.
