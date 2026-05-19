# Security architecture

## Table of contents

1. [Defense in depth](#defense-in-depth)
2. [Network zones](#network-zones)
3. [Control families](#control-families)

## Defense in depth

| Layer | Examples |
|---|---|
| Identity | MFA, SSO, conditional access |
| Network | Segmentation, WAF, private endpoints |
| Application | Secure SDLC, authz, input validation |
| Data | Encryption, DLP, classification |
| Monitoring | SIEM, EDR, audit logs |

## Network zones

- **Public**: CDN, WAF only
- **DMZ**: Load balancers, ingress
- **Application**: workloads, no inbound from internet
- **Data**: databases, restricted ACLs

## Control families

Map designs to ISO 27001 Annex A or NIST CSF: Identify, Protect, Detect, Respond, Recover.
