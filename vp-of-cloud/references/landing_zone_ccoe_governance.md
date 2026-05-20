# Landing zone and CCoE governance

## Table of contents

1. [CCoE charter](#ccoe-charter)
2. [Landing zone adoption](#landing-zone-adoption)
3. [Standards and exceptions](#standards-and-exceptions)
4. [Federation model](#federation-model)
5. [Enablement and vending](#enablement-and-vending)
6. [Governance cadence](#governance-cadence)

## CCoE charter

Publish a one-page charter:

| Element | Decision |
|---------|----------|
| Mission | Accelerate safe cloud adoption with guardrails |
| Members | Platform, security liaison, FinOps, key BU reps |
| Authority | Mandatory standards; time-boxed exceptions |
| Not authority | App feature delivery, corporate security policy |

VP Cloud **sponsors**; `enterprise-cloud-architect` **runs** ARB and catalog.

## Landing zone adoption

Set org targets:

| Metric | Example target |
|--------|----------------|
| New workloads in vending path | 100% net-new prod |
| Legacy account sunset | Dated per OU |
| Shared services coverage | Central logging, DNS, egress |

Technical blueprint → `enterprise-cloud-architect` (`landing_zone_at_scale.md`).

VP tracks **adoption blockers** (skills, exceptions, funding) not subnet CIDRs.

## Standards and exceptions

| Tier | VP role |
|------|---------|
| Mandatory | Approve additions; sunset with migration budget |
| Recommended | Delegate to CCoE |
| Deprecated | Set firm sunset; escalate non-compliance |
| Prohibited | No VP override without security + legal |

**Exception packet:** risk accepted, owner, expiry, compensating controls.

Cap **open exceptions**; review monthly in SteerCo.

## Federation model

| Central owns | Federated BU owns |
|--------------|-------------------|
| Org root, SCPs, hub network | App workloads in vending accounts |
| EA, central log archive | Team tags and cost accountability |
| Break-glass, security tooling | Release cadence |

Resolve disputes: cost allocation vs risk acceptance — VP decides with CFO/CISO inputs.

## Enablement and vending

Require **self-service vending** with policy checks:

- Account/subscription provisioned in <SLA days
- Guardrails applied at creation (logging, backup, SCP)
- Default tags and cost center enforced

Training plan: role-based paths (developer, architect, finops).

Measure **time-to-productive-account** and **repeat exception rate**.

## Governance cadence

| Forum | Cadence | VP delivers |
|-------|---------|-------------|
| Cloud SteerCo | Monthly | Portfolio, spend, blockers |
| ARB | Biweekly | Escalations only |
| Standards council | Quarterly | Theme approvals |
| BU QBR | Quarterly | Showback and adoption scorecard |

Do not duplicate `vp-of-infrastructure` infra SteerCo — **one combined forum** when same leadership team.
