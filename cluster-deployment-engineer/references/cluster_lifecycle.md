# Cluster lifecycle

## Table of contents

1. [Bootstrap order](#bootstrap-order)
2. [Upgrades](#upgrades)
3. [Node operations](#node-operations)

## Bootstrap order

Typical managed-cluster sequence:

1. Cluster API available (version pinned)
2. **CNI** — pods must schedule
3. **CoreDNS** — in-cluster DNS
4. **metrics-server** — HPA and kubectl top
5. **Ingress controller** — HTTP(S) entry
6. **cert-manager** — TLS certificates
7. **GitOps controller** — optional if not pipeline-only
8. **Observability agents** — DaemonSets last if they tolerate NotReady nodes

Document versions in a cluster inventory table (component, chart/app version, owner).

## Upgrades

| Step | Action |
|---|---|
| 1 | Read provider release notes; check deprecated APIs |
| 2 | Upgrade control plane |
| 3 | Upgrade add-ons compatible with new version |
| 4 | Cordon → drain nodes → upgrade node pool → uncordon |
| 5 | Run conformance smoke: DNS, ingress, sample deploy |

Maintain **n-1** skew policy between control plane and nodes per vendor guidance.

## Node operations

- **Scale out** — increase pool; verify labels/taints for workload placement
- **Scale in** — drain with `kubectl drain --ignore-daemonsets --delete-emptydir`
- **Taints** — dedicated pools for GPU, system, or batch only when needed

Self-managed: backup etcd before minor upgrades; test restore annually.
