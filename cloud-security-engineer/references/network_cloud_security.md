# Network security in cloud

## Table of contents

1. [Segmentation](#segmentation)
2. [Ingress and egress](#ingress-and-egress)
3. [Private connectivity](#private-connectivity)
4. [Logging and inspection](#logging-and-inspection)

## Segmentation

Design **tiers**:

| Tier | Typical placement |
|---|---|
| Public edge | ALB/Cloud LB only; no admin |
| App | Private subnets; no direct internet |
| Data | Private; SG/NSG allow only app tier |
| Management | Bastion-less preferred; SSM/serial console |

Avoid flat VPCs with wide SG rules (`0.0.0.0/0` on SSH/RDP/DB ports).

## Ingress and egress

**Ingress:**

- WAF on public HTTP(S) where applicable
- Default deny SG/NSG; document each allow rule owner
- No admin ports on `0.0.0.0/0`

**Egress:**

- Restrict outbound to required FQDNs/IPs where possible (egress firewall, NAT with filtering)
- Block metadata abuse — IMDSv2 required on AWS; restrict metadata access on containers

## Private connectivity

Prefer over public internet for service-to-service:

- AWS PrivateLink / GCP Private Service Connect / Azure Private Link
- VPC/VNet peering or Transit Gateway — document routing and NACL/SG at both ends
- Hybrid: VPN or Direct Connect/Interconnect with encryption

## Logging and inspection

Enable and retain:

| Log | Purpose |
|---|---|
| VPC Flow Logs / equivalent | Connection audit |
| DNS query logs | Exfil and C2 patterns |
| LB access logs | HTTP abuse |
| Firewall logs | Allow/deny proof |

Centralize to security log archive; integrate per `detection_cspm_logging.md`.

Optional: IDS/IPS, NGFW appliances — architecture sign-off with `cloud-architect`.
