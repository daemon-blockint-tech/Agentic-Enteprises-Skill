---
name: cloud-engineer
description: |
  Guides cloud engineering on AWS, GCP, and Azure—landing zones and account structure, VPC/VNet
  networking, compute and autoscaling, object/block storage, managed databases and caches,
  serverless and messaging, DNS/CDN, cloud IAM and workload identity, multi-AZ/region reliability,
  backups and DR, tagging, cost controls, and service-level troubleshooting.
  Use when designing or operating cloud resources, wiring private connectivity, rightsizing spend,
  or debugging control-plane and managed-service failures—not for CI/CD and GitOps (devops),
  Kubernetes cluster bootstrap and Helm (cluster-deployment-engineer), internal developer platforms
  (platform-engineer), release cutover strategy (deployment-strategist), security program and
  IdP/KMS ownership (information-security-engineer), enterprise integration ADRs
  (senior-system-architecture), or physical data center facilities (data-center-design-execution-lead).
  Reusable Terraform module libraries: infrastructure-engineer.
---

# Cloud Engineer

## When to Use

- Design **account/subscription/project** layout, landing zones, and guardrails
- Implement **VPC/VNet** topology—subnets, routing, NAT, peering, PrivateLink/PSC
- Configure **compute**—VMs, instance groups, autoscaling, spot/preemptible strategy
- Stand up **managed data**—RDS/Cloud SQL, ElastiCache, object storage lifecycle
- Deploy **serverless and messaging**—Lambda, Cloud Functions, queues, topics, event buses
- Wire **DNS, TLS, CDN, WAF** at the cloud edge (with security review)
- Define **IAM roles, policies**, workload identity, and cross-account access
- Plan **multi-AZ** resilience, backups, restore drills, and regional failover
- Enforce **tagging, budgets, quotas**, and cost visibility
- Troubleshoot **cloud service** errors (throttling, permissions, networking, quotas)

## When NOT to Use

- Build or fix CI/CD pipelines, GitOps controllers, delivery SLOs → `devops`
- Bootstrap K8s clusters, Helm releases, in-cluster RBAC → `cluster-deployment-engineer`
- Golden paths, developer portals, platform roadmap → `platform-engineer`
- Canary/blue-green rollout and change tiers → `deployment-strategist`
- Pipeline SAST, SBOM, admission policies → `devsecops`
- Corporate IdP, KMS program, SIEM integration → `information-security-engineer`
- Entitlement models, access reviews, federation, PAM → `iam-specialist`
- Cloud reference architecture, landing zone, migration roadmap → `cloud-architect`
- Cloud program strategy, CCoE charter, EA commercial frame → `vp-of-cloud`
- Cross-system architecture review and ADRs → `senior-system-architecture`
- Facility power, cooling, rack layout → `data-center-design-execution-lead`
- GPU/compute supply and stranded kW programs → `data-center-compute-supply-efficiency`
- FinOps accounting close and capex controls → `compute-accounting-manager`
- Cloud cost analysis, budgets, rightsizing, commitment recommendations → `finops-analyst`
- Day-2 access tickets, patching, backup restores, alert runbooks → `cloud-system-administrator`
- Customer discovery, RFP technical response, PoC scoping → `solutions-architect`

## Related skills

| Need | Skill |
|---|---|
| VP cloud program and spend envelope | `vp-of-cloud` |
| Day-2 cloud operations and access admin | `cloud-system-administrator` |
| IAM lifecycle, access reviews, cloud IAM policy design | `iam-specialist` |
| Cloud solution architecture and ADRs | `cloud-architect` |
| Terraform modules and IaC patterns | `infrastructure-engineer` |
| CI/CD, GitOps, on-call for deploy | `devops` |
| Kubernetes cluster operations | `cluster-deployment-engineer` |
| Internal developer platform | `platform-engineer` |
| Release strategy and cutover | `deployment-strategist` |
| Cloud security controls and guardrails | `cloud-security-engineer` |
| Corporate security tooling and IdP | `information-security-engineer` |
| Pipeline and artifact security | `devsecops` |
| Product runtime and tenant isolation | `product-infrastructure-security-engineer` |
| ML safeguard serving infra | `ml-infrastructure-engineer-safeguards` |
| RL training on cloud compute | `ml-systems-engineer-rl-engineering` |
| Customer deal solution and handoff | `solutions-architect` |
| FinOps analysis and cost optimization | `finops-analyst` |
| Compute GL and month-end close | `compute-accounting-manager` |

## Core Workflows

### 1. Cloud foundation and networking

Accounts, VPC/VNet, connectivity.

**See `references/cloud_architecture_foundation.md`.**

### 2. Compute and serverless

VMs, scaling groups, functions.

**See `references/compute_and_serverless.md`.**

### 3. Storage and data services

Object, block, managed DB, cache.

**See `references/storage_and_data_services.md`.**

### 4. IAM and identity

Roles, federation, least privilege.

**See `references/cloud_iam_identity.md`.**

### 5. Reliability and DR

Backups, multi-region, runbooks.

**See `references/reliability_dr_multiregion.md`.**

### 6. Cost and operations

Tagging, budgets, troubleshooting.

**See `references/cost_operations_runbooks.md`.**

## Outputs

- **Architecture sketch** — accounts, networks, data flows
- **IaC snippets or console checklist** — resources with naming and tags
- **IAM policy draft** — actions, resources, conditions (security review before apply)
- **Runbook** — failure modes, rollback, restore steps
- **Cost note** — drivers, rightsizing or reservation options

## Principles

- **Least privilege** — scoped roles per workload; no long-lived admin keys in apps
- **Private by default** — public endpoints only with explicit approval
- **Immutable infrastructure** — prefer replace over snowflake SSH fixes
- **Tag everything** — owner, env, cost center, data classification
- **Measure before multi-region** — complexity tax must match RTO/RPO
