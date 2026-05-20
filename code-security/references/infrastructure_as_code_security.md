# Infrastructure-as-code security

## Table of contents

1. [Terraform (AWS, Azure, GCP)](#terraform-aws-azure-gcp)
2. [Kubernetes](#kubernetes)
3. [Docker](#docker)
4. [GitHub Actions](#github-actions)
5. [IaC review checklist](#iac-review-checklist)

Distilled from upstream rules: `terraform-aws`, `terraform-azure`, `terraform-gcp`, `kubernetes`, `docker`, `github-actions`.

---

## Terraform (AWS, Azure, GCP)

### Common misconfigurations

| Area | Risk | Remediation |
|---|---|---|
| S3 / blob storage | Public buckets, no encryption | Block public access; SSE-KMS; bucket policies least privilege |
| IAM | `Action: *`, `Resource: *`, wildcard principals | Scope actions/resources; restrict `sts:AssumeRole` principals |
| Security groups / NSGs | `0.0.0.0/0` on admin ports | CIDR allowlists; bastion/zero-trust patterns |
| Disks / databases | Unencrypted volumes | Enable encryption at rest; CMK where required |
| Logging | Disabled audit trails | Enable CloudTrail / Activity Log / audit configs |

### AWS patterns

```hcl
# Prefer bucket-level encryption resource (provider v4+)
resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.data.arn
    }
  }
}
```

- Avoid `principal = "*"` in trust policies without tight conditions.
- Use IAM roles for workloads—not long-lived access keys in Terraform outputs.

### Azure / GCP (summary)

- **Azure:** Restrict public network access on storage/SQL; require TLS; managed identities over keys in templates.
- **GCP:** Avoid `allUsers` / `allAuthenticatedUsers` on buckets; enable uniform bucket-level access; least-privilege IAM bindings; VPC SC where required.

**Review heuristics:** `0.0.0.0/0`, `public = true`, `acl = "public-read"`, inline secrets, `ignore_changes` on security attributes.

---

## Kubernetes

### Pod and container security

| Misconfiguration | Secure default |
|---|---|
| `privileged: true` | `privileged: false` |
| `runAsUser: 0` / missing `runAsNonRoot` | `runAsNonRoot: true`, `runAsUser` > 0 |
| `hostNetwork`, `hostPID`, `hostIPC` | Disable unless strictly required |
| Writable root filesystem | `readOnlyRootFilesystem: true` where possible |
| Capabilities | Drop `ALL`, add only needed (`capabilities.drop`) |
| Secrets in env plain text | Use Secret mounts; restrict RBAC to Secret get |

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```

### Cluster hygiene

- Limit **cluster-admin** bindings; namespace-scoped roles.
- NetworkPolicies for east-west segmentation.
- Admission controllers (OPA/Gatekeeper, Kyverno) for policy-as-code.
- Pin images by digest in production; scan images in CI (`devsecops`).

---

## Docker

| Issue | Guidance |
|---|---|
| Run as root | `USER nonroot` after install |
| `--privileged` | Avoid in production |
| Docker socket mount | Never mount `/var/run/docker.sock` into app containers |
| Secrets in layers | Use BuildKit secrets; no `ENV API_KEY=...` |
| Tags | Pin digests or immutable tags—not bare `latest` in prod |
| Attack surface | Minimal base images (distroless/alpine with updates) |

```dockerfile
FROM node:20-bookworm-slim
RUN useradd -r appuser
USER appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
```

---

## GitHub Actions

### Script injection (CWE-78)

**Risk:** `${{ github.event.pull_request.title }}` inside `run: |` executes as shell code.

**Fix:** Pass untrusted context values through `env:` and quote in shell:

```yaml
- name: Check title
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: echo "$PR_TITLE"
```

### `pull_request_target` (CWE-913)

Runs with **base repo secrets**. Checking out PR head and running `npm install` / build can execute attacker code with secret access.

- Avoid checkout + build of untrusted PR code on `pull_request_target`.
- Use `pull_request` for untrusted forks; separate approval for label-gated workflows.

### Supply chain

- Pin actions to **full commit SHA**, not floating `@v4` tags alone.
- Minimize `permissions:` to job needs (`contents: read` default).
- Do not echo secrets to logs; use OIDC to cloud over long-lived cloud keys in secrets.

---

## IaC review checklist

1. **Exposure** — public endpoints, open SGs, anonymous bucket access  
2. **Identity** — wildcard IAM, overbroad AssumeRole, static keys  
3. **Encryption** — at rest and in transit defaults  
4. **Secrets** — literals in HCL/YAML/env  
5. **Workload hardening** — K8s securityContext, non-root containers  
6. **CI trust** — injection surfaces, PR workflows, pinned actions  

For org-wide guardrails (SCPs, OPA, CSPM), coordinate with `information-security-engineer` and `cloud-security-engineer`.
