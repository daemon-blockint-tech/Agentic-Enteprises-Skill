# Security reference architecture

## Table of contents

1. [Layered model](#layered-model)
2. [Security domains](#security-domains)
3. [Trust zones](#trust-zones)
4. [Pattern catalog](#pattern-catalog)
5. [EA integration](#ea-integration)

## Layered model

Use a consistent stack when describing any system:

```
[ Business context & data classification ]
[ Applications & APIs ]
[ Identity & access ]
[ Data protection & key management ]
[ Network & segmentation ]
[ Endpoint & workload ]
[ Security operations & visibility ]
[ Governance, risk, compliance hooks ]
```

Each layer lists **required controls**, **approved patterns**, and **telemetry** expected downstream.

## Security domains

| Domain | Architecture focus | Example building blocks |
|---|---|---|
| Identity | Workforce, customer, machine identities; federation | SSO, MFA, PAM, workload identity |
| Data | Classification, encryption, DLP, retention | KMS tiers, tokenization, masking |
| Application | Secure SDLC, API security, secrets | WAF, API gateway authZ, vault |
| Network | Segmentation, egress, private connectivity | ZTNA, firewalls, NAC, DNS security |
| Endpoint | Device trust, EDR, mobile | MDM/UEM, device compliance signals |
| Operations | Logging, detection, response interfaces | SIEM, SOAR hooks, immutable audit |

Document **interfaces** between domains (e.g., identity signals feeding network policy).

## Trust zones

| Zone | Description | Default posture |
|---|---|---|
| Internet / DMZ | Public services | Hardened, WAF, minimal exposure |
| Corporate | Users, internal apps | Identity-centric access, monitoring |
| Production | Tiered workloads | Segmented, no flat admin |
| Partner / B2B | Integrations | Dedicated connectivity, contract controls |
| Sensitive / regulated | PCI, PHI, etc. | Enhanced controls, restricted admin |
| Recovery | Backup, DR | Isolated, immutable where required |

Map each workload to **one primary zone**; document cross-zone flows explicitly.

## Pattern catalog

Maintain enterprise patterns with ID, intent, prerequisites, and anti-patterns:

| Pattern ID | Name | When to use |
|---|---|---|
| P-ID-01 | Central IdP federation | All workforce SaaS |
| P-NET-02 | Micro-segmentation by app tier | East-west in production |
| P-DATA-03 | CMK with SoD | Regulated data stores |
| P-APP-04 | OAuth2/OIDC for APIs | Machine and user clients |
| P-OPS-05 | Centralized security logging | All tier T0/T1 |

Each pattern links to **validation tests** (design review questions or automated checks).

## EA integration

Align security architecture to enterprise architecture artifacts:

1. Map patterns to **business capabilities** and **application portfolios**
2. Publish **technology standards** (approved, conditional, prohibited)
3. Feed **technology radar** — emerging controls (ZTNA, SSE, confidential computing)
4. Coordinate **migration waves** — security gates per wave, not bolt-on at cutover
5. Maintain **decision log** — exceptions, expiry, compensating controls

For cloud-specific placement and landing zones, coordinate with `enterprise-cloud-architect`; this reference stays **technology-agnostic** where possible.
