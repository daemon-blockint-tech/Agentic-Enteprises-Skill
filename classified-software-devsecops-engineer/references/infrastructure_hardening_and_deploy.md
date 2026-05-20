# Infrastructure Hardening and Deploy

## Table of contents

1. [Deploy-layer scope](#deploy-layer-scope)
2. [IaC security for classified landing zones](#iac-security-for-classified-landing-zones)
3. [Container and image hardening](#container-and-image-hardening)
4. [Kubernetes admission themes](#kubernetes-admission-themes)
5. [STIG/CIS mapping at deploy](#stigcis-mapping-at-deploy)
6. [Runtime and network](#runtime-and-network)
7. [Pre-production checklist](#pre-production-checklist)

## Deploy-layer scope

DevSecOps owns **security characteristics of what the pipeline deploys**:

- Hardened base images and buildpacks approved for the enclave
- IaC modules scanned before merge
- Manifests enforcing non-root, resource limits, and network policy hooks
- Verification that deploy targets match authorized architecture

Platform teams may own cluster lifecycle; DevSecOps ensures **workload deploy path** meets program baselines.

## IaC security for classified landing zones

| Control theme | Implementation hints |
|---------------|---------------------|
| Encryption | Default encrypt data stores and volumes; keys from program KMS |
| Network | Private subnets, no public IPs on workloads, documented egress |
| Identity | IRSA/workload identity; no static keys in templates |
| Logging | Central audit logs enabled in templates |
| Tagging | Mandatory tags for owner, environment, authorization boundary ID (program schema) |

**Scan on plan:** Terraform/Kubernetes/OpenAPI policies in CI; block critical violations.

**Drift:** Periodic posture scan; pipeline deploy should not disable logging or encryption.

## Container and image hardening

### Base image program

- Maintain **gold images** rebuilt on patch cadence
- Document packages included; remove shells/package managers from minimal runtime where feasible
- Scan gold images before publishing to internal registry

### Dockerfile / build practices

- Run as non-root user
- Read-only root filesystem where application permits
- Drop Linux capabilities; no `privileged`
- No secrets in layers; use runtime secret injection
- Pin base image digest in CI build

## Kubernetes admission themes

Policy-as-code (OPA Gatekeeper, Kyverno, or cloud-native policies) should enforce:

- Allowed registries only (internal mirrors)
- Required labels and annotations
- Block `latest` tag for production namespaces
- Require resource requests/limits
- Deny hostPath, hostNetwork, privileged, escalation
- Require network policies for namespaces in scope
- Verify image signatures where supported

Deploy job fails if admission rejects; do not `--force` without change control.

## STIG/CIS mapping at deploy

| Theme | Deploy-time check |
|-------|-------------------|
| Account management | Service accounts per workload; no default namespace deploy |
| Audit | Audit policy enabled; logs shipped |
| Configuration | Hardened PSP/PSS or equivalent (restricted profile) |
| Identification | Standard naming; no sensitive data in env var names visible cluster-wide |
| System integrity | Immutable infrastructure; config from git + pipeline |

Produce a **mapping spreadsheet** from STIG/CIS items to pipeline checks and cluster policies—ISSO incorporates into SSP evidence.

## Runtime and network

- Network policies default-deny east-west; explicit allow per service
- Ingress only via approved controllers and WAF themes where required
- Secrets via CSI/external secrets; rotation hooks
- Workload identity for cloud API access; scoped IAM policies

## Pre-production checklist

- [ ] IaC scan clean or waivers approved
- [ ] Image scan on exact digest to be deployed
- [ ] Signature verified in deploy job
- [ ] SBOM archived for release
- [ ] STIG/CIS spot checks on sample manifest
- [ ] Network policy applied in staging
- [ ] Logs visible in central SIEM test partition
- [ ] Rollback manifest prepared
- [ ] Change ticket links commit, pipeline run, target environment

## Related workflows

- Supply chain signing → `security_gates_and_supply_chain.md`
- Promotion → `artifact_promotion_and_boundaries.md`
- Evidence → `evidence_ato_and_operations.md`
