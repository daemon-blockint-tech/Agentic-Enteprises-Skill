# Cloud and runtime security

## Table of contents

1. [Kubernetes admission](#kubernetes-admission)
2. [Network segmentation](#network-segmentation)
3. [Secrets and identity](#secrets-and-identity)
4. [CSPM triage](#cspm-triage)
5. [WAF and edge](#waf-and-edge)
6. [Runtime detection](#runtime-detection)

## Kubernetes admission

Enforce with **Kyverno** or **OPA Gatekeeper** (pick one per cluster).

| Policy | Example deny |
|---|---|
| Privileged pods | `securityContext.privileged: true` |
| Root user | `runAsNonRoot` required |
| Latest tag | `image: :latest` in prod namespaces |
| Host path mounts | `hostPath` volumes |
| Missing labels | `app`, `owner`, `environment` required |

**Sample Kyverno (concept):** require `runAsNonRoot: true` on Deployments in namespace `production`.

## Network segmentation

- Default-deny network policies; allowlist by label
- Ingress only through ingress controller + WAF
- Egress allowlist for workloads that do not need open internet
- Private endpoints for managed databases and object storage

## Secrets and identity

| Anti-pattern | Fix |
|---|---|
| Secrets in ConfigMaps | External Secrets Operator + vault |
| Shared cluster-admin for apps | Namespace-scoped RBAC |
| Long-lived kubeconfig in CI | OIDC + short-lived tokens |
| IAM user keys on nodes | Instance/workload identity |

Rotate secrets on compromise, role change, or quarterly for high-risk systems.

## CSPM triage

When posture tool flags a finding:

1. Confirm resource ID, account, environment (prod vs dev)
2. Classify: misconfiguration vs intended exception
3. Check blast radius (public exposure, data class)
4. Remediate via IaC PR or automated auto-remediation where safe
5. Document exception with expiry if not fixing immediately

**High-priority CSPM categories:** public storage, open security groups on admin ports, disabled encryption, overly permissive IAM, logging disabled.

## WAF and edge

- OWASP CRS or managed rule sets on public HTTP APIs
- Rate limiting and geo blocks where appropriate
- TLS termination at edge; HSTS for browser clients
- Block common probes; alert on rule spikes

## Runtime detection

| Signal | Tool examples |
|---|---|
| Syscall anomalies | Falco |
| K8s audit abuse | Falco, cloud audit logs |
| Malware in container | Runtime AV where required |
| Anomalous IAM | CloudTrail / Cloud Logging alerts |

**Response:** isolate workload (network policy, scale to zero), capture forensics snapshot, rotate credentials, open incident per severity matrix in `compliance_evidence.md`.
