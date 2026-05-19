# Platform Kubernetes

## Table of contents

1. [Tenant onboarding](#tenant-onboarding)
2. [Cluster operations](#cluster-operations)
3. [Add-on baseline](#add-on-baseline)

## Tenant onboarding

- Namespace per team or env pattern documented
- RBAC: namespace admin vs read-only
- ResourceQuota and LimitRange defaults
- NetworkPolicy: deny-all + allowlist egress
- Pod Security Standards / admission policies

## Cluster operations

- Upgrade cadence; test on non-prod first
- Node pool separation (system vs workload)
- Backup etcd/stateful workloads per policy
- Incident runbook for control plane degradation

## Add-on baseline

Typical platform-managed add-ons:

- Ingress controller
- cert-manager
- metrics-server + Prometheus agent or managed equivalent
- log collector (DaemonSet or sidecar pattern)
- cluster-autoscaler or Karpenter

Teams consume via abstractions—not raw cluster-admin.
