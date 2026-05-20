# Cloud architecture foundation

## Table of contents

1. [Account structure](#account-structure)
2. [Network topology](#network-topology)
3. [Connectivity patterns](#connectivity-patterns)
4. [Naming and environments](#naming-and-environments)

## Account structure

| Pattern | Use |
|---|---|
| Org per business unit | Blast-radius isolation |
| Env per account (dev/stage/prod) | Clear billing and SCP scope |
| Shared services account | DNS, logging, security tooling |
| Sandbox OU | Experimentation with guardrails |

Apply **SCPs** or org policies: deny public S3, restrict regions, require encryption.

Document **break-glass** admin access and approval.

## Network topology

Standard hub-spoke or multi-VPC:

- **Private subnets** for workloads; **public** only for ingress/NAT
- **Three AZ** minimum for production stateful tiers when available
- **Route tables** explicit; no 0.0.0.0/0 from private without NAT or egress firewall
- **DNS** — private zones for internal names; avoid hard-coded IPs

Provider notes:

| AWS | GCP | Azure |
|---|---|---|
| VPC, subnets, IGW, NAT GW | VPC, subnets, Cloud NAT | VNet, subnets, NAT GW |
| Transit Gateway | VPC peering / NCC | vWAN / peering |
| PrivateLink | Private Service Connect | Private Endpoint |

## Connectivity patterns

- **VPC/VNet peering** — same region, non-transitive; watch CIDR overlap
- **VPN / Direct Connect / ExpressRoute / Interconnect** — hybrid
- **PrivateLink / PSC / Private Endpoint** — SaaS and managed services without public egress
- **Egress filtering** — centralized NAT with inspection where required

## Naming and environments

Convention: `{org}-{env}-{region}-{service}-{resource}`

Environments: `dev`, `staging`, `prod` — separate accounts or subscriptions where possible.

Promotion: infrastructure changes via PR + plan review; align with `devops` for app deploy cadence.

For large Terraform module libraries → `infrastructure-engineer`.
