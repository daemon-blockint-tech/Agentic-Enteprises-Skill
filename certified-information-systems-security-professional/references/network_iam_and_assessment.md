# Network, IAM, and Security Assessment (Domains 4–6)

## Table of contents

1. [Communication and Network Security (Domain 4)](#communication-and-network-security-domain-4)
2. [Identity and Access Management (Domain 5)](#identity-and-access-management-domain-5)
3. [Security Assessment and Testing (Domain 6)](#security-assessment-and-testing-domain-6)
4. [Cross-domain control patterns](#cross-domain-control-patterns)

## Communication and Network Security (Domain 4)

**OSI and TCP/IP** — map security controls to layers (e.g., switching vs routing, TLS at application layer).

| Control type | Examples |
|---|---|
| Network segmentation | VLANs, micro-segmentation, zero-trust segments |
| Perimeter | Firewalls, WAF, proxies, NAT |
| Remote access | VPN, ZTNA, MFA at edge |
| Wireless | WPA3, guest isolation, rogue AP detection |
| Monitoring | IDS/IPS, NetFlow, NDR (program-level placement) |

**Attack classes** (recognize for governance and assessment scope): spoofing, tampering, repudiation, disclosure, DoS, elevation of privilege (STRIDE complements CBK).

**Secure protocols**: Prefer modern TLS versions; deprecate weak ciphers; understand IPsec modes (transport vs tunnel) at decision level.

**Cloud networking**: Shared responsibility—customer configures security groups, NACLs, private endpoints; provider secures hypervisor and physical layer.

## Identity and Access Management (Domain 5)

**Identity lifecycle**: Provisioning → review → modification → suspension → deprovisioning.

| Concept | Notes |
|---|---|
| Authentication | Something you know/have/are |
| Authorization | What you may do after auth |
| Accounting / auditing | Logging access decisions |
| Federation | SAML, OIDC, trust between domains |
| PAM | Break-glass, session recording, JIT elevation |

**Access control models**:

- MAC — labels enforced by system
- DAC — owner grants permissions
- RBAC — roles aggregate permissions
- ABAC — attributes (context-aware)

**IAM program elements**: SoD, recertification campaigns, privileged access reviews, passwordless/MFA policy. Implementation: `information-security-engineer` and IdP teams.

## Security Assessment and Testing (Domain 6)

| Activity | Purpose |
|---|---|
| Vulnerability assessment | Find weaknesses (scanning) |
| Penetration test | Exploit paths with rules of engagement |
| Audit | Independent compliance/effectiveness review |
| Security assessment | Broader evaluation against criteria |
| Code review / SAST / DAST | Software assurance (ties to Domain 8) |

**Testing program governance**:

- Rules of engagement, scope, production constraints
- Remediation SLAs by severity
- Retest and exception tracking
- Metrics: mean time to remediate, recurring findings

**Audit support** (CISSP lens): define population, sampling, control objective, test procedure, evidence type—`compliance-specialist` owns pack assembly; `compliance-engineer` automates collection.

**False positives / negatives**: Risk to resource allocation; tune processes, not only tools.

## Cross-domain control patterns

| Pattern | Domains |
|---|---|
| MFA everywhere | 4, 5 |
| Encrypted transit | 3, 4 |
| Role-based app access | 5, 8 |
| Annual pen test + continuous scanning | 6, 7 |

Route **active exploitation** and tool-specific runbooks to `penetration-tester`; route **SOC tuning** to `soc-analyst` and `defensive-security-analyst`.
