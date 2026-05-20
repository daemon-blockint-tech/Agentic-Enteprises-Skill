# Landing zone at scale

## Table of contents

1. [Hierarchy patterns](#hierarchy-patterns)
2. [Account vending](#account-vending)
3. [Guardrails at scale](#guardrails-at-scale)
4. [Shared services hub](#shared-services-hub)

## Hierarchy patterns

Example AWS-style (adapt for Azure MG / GCP folders):

```
Organization
├── Security (log archive, audit, tooling)
├── Infrastructure (network hub, DNS, egress)
├── Sandbox OU (SCP-limited, auto-suspend)
├── NonProd OU (per BU or per product)
└── Prod OU (stricter SCPs, change windows)
```

**Per BU** vs **per environment** account model — document in ADR with cost and blast-radius trade-offs.

## Account vending

Self-service flow:

1. Request via portal/ticket with owner, cost center, data class, region
2. Automated create — OU placement, baseline SCPs, tags, networking attachment
3. Handoff — break-glass roles, FinOps tags, security contacts
4. **Lifecycle** — suspend sandbox idle; decommission with data retention rules

Integrate with `infrastructure-engineer` module pipeline for baseline config.

## Guardrails at scale

| Layer | Examples |
|---|---|
| Org SCP / policy | Region deny, encryption required |
| Tag policy | Mandatory cost center, owner, data class |
| Service control | Allowed instance types, no public DB |
| Detective | Config rules, Security Hub, org trails |

**Drift:** central dashboard; BU remediation SLAs.

## Shared services hub

Centralize:

- Egress and inspection
- Private DNS and certificate authorities
- Central logging and SIEM feed
- Backup vaults for regulated tiers

Document **data flows** from spoke to hub — `cloud-architect` network detail for spokes.
