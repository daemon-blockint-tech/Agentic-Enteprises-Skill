---
name: platform-engineer
description: |
  Guides platform engineering—internal developer platforms (IDP), golden paths, self-service
  abstractions, developer portals, paved-road templates, multi-tenant Kubernetes platforms, and
  platform-as-product practices (roadmap, adoption, platform SLOs).
  Use when designing or operating a platform for engineering teams, building service scaffolds,
  standardizing deploy/runtime patterns, integrating Backstage or similar portals, defining
  platform APIs and contracts, or measuring developer experience—not for one-off VPC or network
  design (infrastructure-engineer), per-app CI YAML only (devops), release cutover planning
  (deployment-strategist), security control implementation (information-security-engineer), or
  enterprise-wide system integration ADRs (senior-system-architecture). For hands-on cluster
  add-ons, Helm, and namespace layout on shared clusters, use cluster-deployment-engineer.
---

# Platform Engineer

## When to Use

- Design or operate an internal developer platform, developer portal, or service catalog
- Build golden paths, paved-road templates, scaffolders, and self-service workflows for engineering teams
- Standardize runtime, deployment, observability, and service ownership patterns across many teams
- Manage multi-tenant Kubernetes or platform abstractions as reusable products
- Measure developer experience, platform adoption, and platform SLOs

## When NOT to Use

- Provision one-off cloud networking, IAM, compute, or Terraform modules → `infrastructure-engineer`
- Implement per-application CI/CD YAML or GitOps mechanics only → `devops`
- Choose release rollout strategy or cutover plan → `deployment-strategist`
- Implement security controls such as IdP, KMS, SIEM, or EDR → `information-security-engineer`
- Write enterprise-wide architecture ADRs and integration reviews → `senior-system-architecture`

## Related skills

| Need | Skill |
|---|---|
| Cloud networking, core IaC modules | `infrastructure-engineer` |
| Managed cloud services under platform | `cloud-engineer` |
| Shared CI/CD, GitOps, SRE alerting | `devops` |
| Canary/blue-green rollout decisions | `deployment-strategist` |
| Pipeline and supply-chain security | `devsecops` |
| Platform IAM, KMS, SIEM hooks | `information-security-engineer` |
| Security of product runtime and tenant isolation | `product-infrastructure-security-engineer` |
| Enterprise integration ADRs and review | `senior-system-architecture` |
| Cluster deploy and day-2 K8s ops | `cluster-deployment-engineer` |

## Core Workflows

### 1. Platform as product

Treat the platform like a product with internal customers:

1. Identify user journeys (create service, deploy, observe, rotate secrets)
2. Define **thin** platform APIs—hide complexity, expose safe defaults
3. Set platform SLOs (e.g., scaffold time, deploy success rate, portal uptime)
4. Roadmap from developer interviews and toil metrics
5. Deprecate with migration windows—not breaking teams silently

**See `references/platform_product.md` for SLOs and adoption metrics.**

### 2. Golden paths (paved roads)

**Golden path properties:**

- Opinionated defaults (language, observability, auth, CI template)
- Escape hatches documented for edge cases
- Versioned templates with changelog
- Same path for 80% of services; exceptions require review

```
scaffold → build (shared pipeline) → deploy (standard envs) → operate (shared dashboards/alerts)
```

**See `references/golden_paths.md` for template and exception process.**

### 3. Internal developer platform (IDP)

**Layers:**

| Layer | Examples |
|---|---|
| Portal | Backstage, custom UI |
| Orchestration | Argo CD, Terraform/Crossplane, Helm charts |
| Runtime | K8s namespaces, serverless platform |
| Data | Shared RDS patterns, message buses |

Integrate catalog, docs, templates, and deployment in one discoverable flow.

**See `references/idp_architecture.md` for component diagram and contracts.**

### 4. Multi-tenant Kubernetes platform

- Namespace/tenant isolation; RBAC and network policies
- Quotas, priority classes, and cluster autoscaling
- Standard add-ons: ingress, cert-manager, external-dns, metrics, logging
- Cluster upgrades with tenant communication plan
- Policy admission (OPA/Kyverno) owned by platform

**See `references/platform_kubernetes.md` for tenant checklist.**

### 5. Developer portal and service catalog

- Register services: owner, tier, repo, on-call, dependencies
- Link runbooks, APIs, and SLIs from catalog entries
- Software templates (Cookiecutter, Yeoman, internal CLI) generate compliant repos
- Scorecards for maturity (tests, SLOs, security baseline)

**See `references/developer_portal.md` for catalog fields and template standards.**

### 6. Platform interfaces and versioning

- Publish platform contracts: breaking vs additive changes
- Semantic versioning for charts, modules, and templates
- Changelog and migration guides for each major bump
- Support window for N-1 template versions

## When to load references

- **IDP design** → `references/idp_architecture.md`
- **Templates and paved roads** → `references/golden_paths.md`
- **Backstage / catalog** → `references/developer_portal.md`
- **K8s multi-tenancy** → `references/platform_kubernetes.md`
- **SLOs and adoption** → `references/platform_product.md`
