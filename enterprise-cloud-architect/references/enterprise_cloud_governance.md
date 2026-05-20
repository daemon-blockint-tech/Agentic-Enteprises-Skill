# Enterprise cloud governance

## Table of contents

1. [CCoE operating model](#ccoe-operating-model)
2. [Architecture review board](#architecture-review-board)
3. [Standards catalog](#standards-catalog)
4. [Federation vs central IT](#federation-vs-central-it)

## CCoE operating model

Typical functions:

| Function | Deliverable |
|---|---|
| Standards | Approved services, regions, patterns |
| Enablement | Training, sandboxes, templates |
| FinOps | Tag policy, EA management, reports |
| Security liaison | Guardrail requirements with security org |
| Vending | Account/subscription provisioning API |

Define **RACI** with BUs, security, finance, and platform engineering.

## Architecture review board

**ARB triggers:**

- New regulated data class in cloud
- Internet-exposed production workload
- Cross-account trust or org-wide IAM change
- Spend above threshold or new EA commit
- Departure from mandatory standard

**ARB packet:** context, options, NFRs, cost ROM, risks, recommendation.

**Exceptions:** time-bound, named owner, re-review date.

Team-level designs → `cloud-architect` ARB lite; escalate per threshold.

## Standards catalog

| Tier | Meaning |
|---|---|
| Mandatory | Block deploy if non-compliant (policy) |
| Recommended | Default in templates |
| Deprecated | Sunset date; migration required |
| Prohibited | e.g. public S3, long-lived access keys |

Version standards; communicate via portal and IaC modules.

## Federation vs central IT

Balance:

- **Central** — landing zone, network hub, logging, EA, break-glass
- **Federated** — application teams own workloads inside guardrails
- **Escalation** — disputes on cost allocation or risk acceptance

Align with `senior-system-architecture` for enterprise integration principles.
