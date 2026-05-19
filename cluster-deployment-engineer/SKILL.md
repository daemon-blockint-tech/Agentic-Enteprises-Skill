---
name: cluster-deployment-engineer
description: |
  Guides Kubernetes cluster deployment and operations—cluster bootstrap and upgrades, node pools,
  add-ons (ingress, CNI, cert-manager), workload delivery with Helm/Kustomize/operators, namespace
  quotas and RBAC, GitOps sync to clusters, multi-cluster patterns, and production troubleshooting
  (scheduling, networking, crash loops).
  Use when deploying or upgrading K8s clusters, installing platform add-ons, rolling out manifests
  or Helm releases, fixing cluster-level failures, or designing namespace and multi-tenant cluster
  layout—not for VPC/IaC foundation (infrastructure-engineer), CI pipeline YAML (devops), app
  rollout strategy canary/blue-green (deployment-strategist), IDP golden paths (platform-engineer),
  or admission policy program design (devsecops). DC facility design: data-center-design-execution-lead.
  DC compute supply/efficiency: data-center-compute-supply-efficiency. Rack-ready delivery:
  senior-data-center-capacity-delivery-manager.
---

# Cluster Deployment Engineer

## When to Use

- Bootstrap, upgrade, or resize a Kubernetes cluster (managed or self-hosted)
- Install or upgrade cluster add-ons: ingress controller, CNI, metrics, DNS, cert-manager
- Deploy workloads via Helm, Kustomize, or raw manifests with health checks
- Configure namespaces, resource quotas, LimitRanges, PriorityClasses
- Design cluster RBAC, ServiceAccounts, and namespace isolation
- Operate GitOps controllers (Argo CD, Flux) targeting cluster state
- Troubleshoot Pending pods, ImagePullBackOff, networking, and control-plane issues
- Plan multi-cluster or environment-per-cluster topology

## When NOT to Use

- Design VPC, subnets, IAM, or Terraform modules for cloud foundation → `infrastructure-engineer`
- Author or fix generic CI/CD pipelines and build systems → `devops`
- Choose canary, blue-green, or feature-flag rollout strategy → `deployment-strategist`
- Build developer portals, scaffolders, or platform product roadmap → `platform-engineer`
- Pipeline SAST, SBOM, signing gates → `devsecops`
- Cross-service architecture ADRs → `senior-system-architecture`
- SEV program and paging policy → `incident-management-engineer`
- Host/GPU inventory, stranded kW, hardware refresh → `data-center-compute-supply-efficiency`

## Related skills

| Need | Skill |
|---|---|
| Cloud networking and cluster IaC | `infrastructure-engineer` |
| CI/CD, GitOps pipelines, delivery SLOs | `devops` |
| Release rollout and rollback planning | `deployment-strategist` |
| Multi-tenant platform product | `platform-engineer` |
| Admission policies, image scan, runtime security | `devsecops` |
| Product tenant isolation on K8s | `product-infrastructure-security-engineer` |
| Launch comms for cluster changes | `communication-lead` |
| Data center / colo facility design | `data-center-design-execution-lead` |
| Compute supply and DC resource efficiency | `data-center-compute-supply-efficiency` |
| Capacity delivery and rack-ready gates | `senior-data-center-capacity-delivery-manager` |
| On-site rack-and-stack, cabling, sign-off | `field-services-engineer` |

## Core Workflows

### 1. Cluster lifecycle

1. **Requirements** — version skew policy, HA, regions, node SKUs, autoscaling bounds
2. **Bootstrap** — control plane, node groups, OIDC for workloads
3. **Add-ons** — ordered install (CNI → DNS → ingress → certs → metrics)
4. **Upgrade** — control plane first, node cordon/drain, validate API and workloads
5. **Decommission** — drain, backup etcd/state if self-managed, destroy order

**See `references/cluster_lifecycle.md`.**

### 2. Workload delivery

1. **Package** — Helm chart or Kustomize overlay per env
2. **Values** — resources, replicas, probes, affinity, topology spread
3. **Apply** — dry-run, diff, apply; watch rollout status
4. **Verify** — readiness, Service endpoints, ingress, smoke test
5. **Rollback** — `helm rollback` or GitOps revert commit

**See `references/workload_delivery.md`.**

### 3. Networking and ingress

- Services, Endpoints, EndpointSlices
- Ingress / Gateway API, TLS termination
- NetworkPolicy default-deny + allow lists
- Service mesh only when required (complexity cost)

**See `references/networking_ingress.md`.**

### 4. Security and tenancy

- Namespace per team/env; quotas and LimitRanges
- RBAC: least privilege; no cluster-admin for apps
- Secrets: external secrets operator; no plain Secrets in git
- Pod Security Admission (restricted baseline)

Pair with `devsecops` for admission controllers and image policy.

**See `references/cluster_security_rbac.md`.**

### 5. GitOps at cluster scope

- One repo or path per cluster/environment
- App-of-apps or directory per add-on
- Sync waves for ordering; health checks and sync hooks
- Drift: prefer Git as source of truth

**See `references/gitops_cluster.md`.**

### 6. Troubleshooting

| Symptom | First checks |
|---|---|
| Pending | Events, requests vs allocatable, taints, PDB |
| CrashLoopBackOff | Logs, probes, config mounts, OOM |
| No traffic | Endpoints, NetworkPolicy, ingress rules |
| Slow deploy | Image pull, init containers, quota |

**See `references/troubleshooting.md`.**

## Output standards

- Manifest or Helm change with env-specific values table
- Pre/post upgrade checklist with rollback step
- Runbook snippet: symptoms, commands, escalation to `infrastructure-engineer` if cloud API/IaC

## When to load references

- **Bootstrap, upgrade, nodes** → `references/cluster_lifecycle.md`
- **Helm, Kustomize, rollouts** → `references/workload_delivery.md`
- **Ingress, CNI, policies** → `references/networking_ingress.md`
- **RBAC, quotas, PSA** → `references/cluster_security_rbac.md`
- **Argo CD / Flux** → `references/gitops_cluster.md`
- **Incidents and debug** → `references/troubleshooting.md`
