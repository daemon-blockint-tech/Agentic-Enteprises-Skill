# Application and integration security

## Table of contents

1. [Secure SDLC gates](#secure-sdlc-gates)
2. [API and B2B integration](#api-and-b2b-integration)
3. [Secrets and configuration](#secrets-and-configuration)
4. [Third-party and SaaS](#third-party-and-saas)
5. [Architecture review checklist](#architecture-review-checklist)

## Secure SDLC gates

Define **minimum gates** by tier (coordinate implementation with `devsecops`):

| Gate | T0/T1 expectation |
|---|---|
| Threat modeling | STRIDE or PASTA for new external exposure or sensitive data |
| Design review | Security ARB sign-off before build commitment |
| Dependencies | SBOM, vulnerability SLA by severity |
| Static/dynamic test | SAST/DAST in CI for internet-facing apps |
| Secrets | No secrets in repo; vault integration |
| Release | Change record, rollback, monitoring hooks |

Architecture owns **what** must be proven; engineering owns **how** in pipelines.

## API and B2B integration

| Pattern | Standard |
|---|---|
| External APIs | OAuth2/OIDC or mTLS; rate limits; schema validation |
| Internal APIs | Service identity, mesh or gateway authZ, no shared service passwords |
| Webhooks | Signed payloads, replay protection, IP allowlists only as supplement |
| File exchange | Encrypted transport, malware scan, retention limits |
| Event streams | Topic ACLs, encryption, dead-letter monitoring |

Document **trust direction** (inbound vs outbound), **data classes** carried, and **failure modes** (fail closed vs degraded).

## Secrets and configuration

- Central **secrets manager** or vault; no long-lived credentials in config files
- **Environment separation** — prod secrets never in lower environments
- **Rotation** — documented cadence; emergency rotation playbooks
- **Configuration drift** — baseline images and policy-as-code preferred over manual prod edits

## Third-party and SaaS

| Control area | Architecture requirement |
|---|---|
| Identity | Federate via IdP where possible; enforce MFA |
| Data | Classification match; DLP and residency clauses in tier |
| Logging | Export admin and security logs to enterprise SIEM |
| Integration | Dedicated connectivity (no ad hoc VPN exceptions) |
| Exit | Data export and key custody on termination |

Align vendor tiers with `compliance-specialist` questionnaires; technical evidence with `compliance-engineer` where automated.

## Architecture review checklist

Use in security ARB for new or materially changed systems:

1. **Assets and data** — tiers, residency, retention
2. **Trust boundaries** — diagrams with authN/authZ at each crossing
3. **Identity** — human vs machine; admin paths
4. **Network** — zones, ingress/egress, segmentation
5. **Cryptography** — algorithms, key management, TLS versions
6. **Logging & monitoring** — what events, where stored, retention
7. **Availability & DR** — RTO/RPO; security of backups
8. **Dependencies** — third parties, shared platforms
9. **Threats** — top abuse cases and mitigations
10. **Exceptions** — compensating controls, owner, expiry

Record outcomes in the **architecture decision log**; link product ADRs in `senior-system-architecture` when scope is a single product line.
