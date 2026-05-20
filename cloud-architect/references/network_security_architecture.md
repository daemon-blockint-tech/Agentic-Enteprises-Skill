# Network and security architecture

## Table of contents

1. [Segmentation](#segmentation)
2. [Connectivity](#connectivity)
3. [Edge and ingress](#edge-and-ingress)
4. [Zero trust hooks](#zero-trust-hooks)

## Segmentation

Layers:

- **Perimeter** — WAF, DDoS, only approved ingress
- **VPC/VNet tiers** — public (ingress/NAT), private (apps), data (DB)
- **Micro-segmentation** — security groups / firewall rules least privilege
- **Service mesh** (optional) — mTLS east-west in Kubernetes

Document **data flows** — who talks to whom, ports, encryption.

## Connectivity

| Pattern | Use |
|---|---|
| Hub-spoke | Central inspection, shared services |
| Mesh peering | Full mesh only at small scale |
| PrivateLink / PSC / Private Endpoint | SaaS without public internet |
| Hybrid VPN / ExpressRoute / Interconnect | On-prem extension |

Align with `data-center-design-execution-lead` for physical paths.

## Edge and ingress

- **TLS termination** — ALB/GLB/API Gateway; cert lifecycle
- **CDN** — static assets, caching rules
- **WAF rules** — OWASP baseline; tune with `devsecops`
- **Rate limiting** — edge and app layers

## Zero trust hooks

Architecture should enable (implementation with security engineering):

- Identity-aware proxy where applicable
- No flat network trust inside VPC
- **Conditional access** for human admin
- Centralized logging of network and identity events

Do not duplicate enterprise GRC catalog — `cybersecurity`.
