# Troubleshooting

## Table of contents

1. [Quick commands](#quick-commands)
2. [Symptom matrix](#symptom-matrix)
3. [Escalation](#escalation)

## Quick commands

```bash
kubectl get events -A --sort-by='.lastTimestamp' | tail -20
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --previous
kubectl top nodes
kubectl get pods -A -o wide | grep -v Running
```

## Symptom matrix

| Symptom | Likely cause | Fix direction |
|---|---|---|
| Pending | Insufficient CPU/mem, taints, PVC | Scale nodes, fix requests, StorageClass |
| ImagePullBackOff | Bad tag, registry auth | Fix secret, image name |
| CrashLoopBackOff | App error, bad probe | Logs, relax probe, fix config |
| OOMKilled | Limit too low | Raise memory limit or fix leak |
| 502 from ingress | No endpoints | Check Service selector, readiness |
| API timeout | Control plane, network | Provider status, `infrastructure-engineer` |

## Escalation

| Layer | Skill |
|---|---|
| Cloud API, LB, IAM, Terraform | `infrastructure-engineer` |
| CI not promoting manifests | `devops` |
| Release decision to rollback traffic | `deployment-strategist` |
| Security incident on cluster | `cybersecurity`, `defensive-security-analyst` |

Capture: timestamp, cluster, namespace, workload, events snippet, change that preceded failure.
