# Identity, data, and zero trust

## Table of contents

1. [Zero-trust principles](#zero-trust-principles)
2. [Identity architecture](#identity-architecture)
3. [Data protection tiers](#data-protection-tiers)
4. [Segmentation](#segmentation)
5. [Roadmap phases](#roadmap-phases)

## Zero-trust principles

Apply consistently across corporate, cloud, and partner contexts:

1. **Verify explicitly** — authenticate and authorize every request; no implicit trust by network location
2. **Least privilege** — just-enough access with time bounds for privileged use
3. **Assume breach** — segment, log, detect lateral movement; limit blast radius
4. **Continuous validation** — device posture, session risk, step-up auth when signals change

Zero trust is a **program**, not a single product. Architecture defines required capabilities; `iam-specialist` and `information-security-engineer` implement.

## Identity architecture

```
[ Human identities ] → IdP (SSO/MFA) → RBAC/ABAC → apps & infra
[ Machine identities ] → workload identity / SPIFFE-style → scoped credentials
[ Privileged access ] → PAM/JIT → session monitoring → break-glass (rare, audited)
[ Customer identities ] → separate CIAM stack where applicable
```

| Topic | Architecture standard |
|---|---|
| Federation | SAML/OIDC to central IdP; no local passwords for workforce |
| Admin access | No standing cloud/root; PAM or JIT elevation |
| Service accounts | Named, owned, rotated; prefer workload identity over long-lived keys |
| Guest / contractor | Time-bound, sponsor-attested, restricted entitlements |
| Directory hygiene | Joiner/mover/leaver tied to HRIS; quarterly recertification for sensitive roles |

Coordinate detailed entitlement design with `iam-specialist`; cloud IAM policy patterns with `cloud-security-engineer` where applicable.

## Data protection tiers

| Tier | Examples | Architectural requirements |
|---|---|---|
| Public | Marketing content | Integrity controls; no secret embedding |
| Internal | Most business data | Access via identity; logging |
| Confidential | Strategy, unreleased financials | Encryption, DLP, need-to-know |
| Restricted | Regulated (PCI, PHI, etc.) | Enhanced segmentation, CMK, stricter admin |

For each tier document: **encryption** (at rest/in transit), **key custody**, **retention**, **residency**, and **logging** requirements.

## Segmentation

| Layer | Objective | Patterns |
|---|---|---|
| Perimeter | Reduce internet attack surface | WAF, reverse proxy, DDoS |
| Macro | Separate prod/nonprod, sensitive enclaves | Firewalls, routing, ACLs |
| Micro | Limit east-west | App-tier SGs/NSGs, service mesh policy |
| Identity | Enforce app-level authZ | OAuth scopes, ABAC claims |
| SaaS | Control data exfil | CASB/SSE where standard |

**Avoid** flat networks with shared admin paths. Document **allowed flows** (who talks to whom, on which ports, with which identity).

## Roadmap phases

| Phase | Focus | Outcomes |
|---|---|---|
| 0 — Baseline | Inventory apps, data tiers, flat-network risks | Heat map, quick wins |
| 1 — Identity | SSO coverage, MFA, admin reduction | % apps federated, MFA enforced |
| 2 — Visibility | Central logging, critical asset telemetry | T0/T1 log coverage |
| 3 — Segmentation | Enclaves for crown jewels | Reduced lateral paths |
| 4 — Continuous | Risk-based access, automation | Mean time to revoke, policy-as-code |

Publish **dependencies** (e.g., IdP before app segmentation) and **metrics** per phase for executive tracking.
