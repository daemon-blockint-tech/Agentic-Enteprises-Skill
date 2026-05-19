---
name: devsecops
description: |
  Guides DevSecOps practices that embed security into software delivery—shift-left scanning,
  CI/CD security gates, supply-chain integrity, cloud/container runtime controls, threat modeling,
  and vulnerability management with audit evidence.
  Use when designing or hardening delivery pipelines, adding SAST/SCA/secrets/IaC/container scans,
  implementing SBOMs or artifact signing, configuring OIDC and least-privilege CI/CD, writing OPA/Kyverno
  policies, triaging CVEs, mapping controls to SOC 2/ISO 27001/SSDF, securing GitHub Actions or agentic
  CI workflows, or running pre-release security reviews—not for general cloud provisioning without
  a security lens (use infrastructure-engineer), LLM prompt guardrails (prompt-engineer), or
  cluster Helm/add-on operations without security policy focus (cluster-deployment-engineer).
---

# DevSecOps

## When to Use

- Add or harden SAST, SCA, secrets, IaC, DAST, or container scans in CI/CD
- Configure protected-branch security gates, artifact signing, SBOMs, provenance, or OIDC federation
- Triage pipeline security findings and define remediation SLAs or exception workflows
- Secure GitHub Actions, GitLab CI, build containers, registries, and deployment credentials
- Map delivery artifacts to SOC 2, ISO 27001, SSDF, or supply-chain evidence requirements

## When NOT to Use

- Provision general cloud infrastructure without a security gate focus → `infrastructure-engineer`
- Operate build/deploy pipelines without security requirements → `devops`
- Implement corporate IdP, KMS, PAM, SIEM, or EDR controls → `information-security-engineer`
- Triage live SOC alerts or tune SIEM detections → `defensive-security-analyst`
- Define company-wide security strategy or GRC roadmap → `cybersecurity`
- Bootstrap clusters, Helm releases, ingress, routine pod debug → `cluster-deployment-engineer`

## Related skills

| Need | Skill |
|---|---|
| VPC, K8s platform, IaC provisioning, generic CI/CD | `infrastructure-engineer` |
| AI agent workflows in CI (Codex, Claude Action, prompt injection) | `agentic-actions-auditor` (if installed) |
| Application threat models from repo structure | `security-threat-model` (if installed) |
| Data governance, PII in warehouses | `data-architect` |
| Security runbooks and customer-facing docs | `tech-writer-researcher` |
| Platform IAM, KMS, SIEM/EDR operations | `information-security-engineer` |
| Product tenancy, service authZ, customer data isolation | `product-infrastructure-security-engineer` |
| Audit evidence pipelines and control mapping | `compliance-engineer` |
| K8s workload deploy and cluster day-2 ops | `cluster-deployment-engineer` |
| External researcher disclosure program | `technical-program-manager-security-cvd` |

## Core Workflows

### 1. Shift-left security baseline

**Apply on every repo before merge to default branch:**

1. Inventory languages, build tool, deploy target, and compliance scope
2. Enable secret scanning and push protection on the org/repo
3. Add SAST + SCA in CI on pull requests (fail on new critical/high)
4. Scan IaC on `terraform plan` / manifest changes (Checkov, tfsec, KICS)
5. Scan container images before registry push (Trivy, Grype)
6. Document exceptions with owner, expiry, and compensating control

**Gate policy (default):**

| Finding | PR | Default branch | Production deploy |
|---|---|---|---|
| Secret in code | Block | Block | Block |
| Critical CVE (exploitable) | Block | Block | Block |
| High CVE | Warn or block | Block | Block with exception |
| Medium/low | Warn | Track | Track |

**See `references/shift_left_scanning.md` for tool matrices, baseline configs, and false-positive handling.**

### 2. CI/CD security gates

**Pipeline order (security stages must not be skippable on protected branches):**

```
lint → unit test → SAST/SCA → build → image scan → sign/SBOM → deploy staging → DAST (if applicable) → promote prod
```

**Checklist:**

- [ ] Use OIDC federation to cloud/K8s—no long-lived cloud keys in CI secrets
- [ ] Pin actions/images by digest or immutable version; allowlist third-party actions
- [ ] Separate build (untrusted) from deploy (trusted) jobs with environment protection rules
- [ ] Require code review + passing checks on default branch
- [ ] Store artifacts in immutable registry; verify signatures at deploy
- [ ] Log retention for audit (who deployed what, from which commit)

**See `references/cicd_security_gates.md` for GitHub Actions/GitLab patterns, OIDC, and deployment controls.**

### 3. Supply chain integrity

**Minimum viable supply chain for production services:**

1. Generate SBOM (CycloneDX or SPDX) on each release build
2. Sign container images and/or provenance (Sigstore/cosign, SLSA-oriented attestations where required)
3. Block dependencies with known critical CVEs unless documented exception
4. Prefer pinned lockfiles; review major dependency upgrades in PR
5. Vet new third-party actions, Helm charts, and base images

**See `references/supply_chain.md` for SBOM fields, signing flows, and dependency update policy.**

### 4. Cloud, container, and runtime security

**Pre-production checklist:**

- [ ] Workloads in private subnets; ingress only via LB/WAF
- [ ] Non-root containers, read-only root FS, dropped capabilities, no privileged pods
- [ ] Network policies or service mesh mTLS for east-west traffic
- [ ] Secrets from Vault/Secrets Manager/External Secrets—not in manifests or env in git
- [ ] CSPM/posture alerts wired to on-call for critical misconfigurations
- [ ] Runtime detection (Falco, cloud-native threat detection) for production clusters

**See `references/cloud_runtime_security.md` for K8s admission policies, WAF, and CSPM triage.**

### 5. Threat modeling and security review

**Lightweight review (every feature with auth, payments, PII, or external input):**

1. Draw data flow: actors, trust boundaries, stores, external APIs
2. List assets and STRIDE threats per boundary
3. Map mitigations to existing controls or new tickets
4. Record accepted risks with approver and review date

**Deeper review triggers:** new public API, auth model change, multi-tenant isolation change, crypto design, admin tooling, agent/LLM in production path.

**See `references/threat_modeling.md` for STRIDE prompts, abuse-case templates, and review cadence.**

### 6. Vulnerability management and compliance evidence

**Triage workflow:**

1. Normalize findings (tool, CVE, asset, environment, exploitability)
2. Score with CVSS + business context (internet-facing, data class, compensating controls)
3. Assign owner and remediation SLA (see reference SLAs)
4. Verify fix in CI rescan before closing
5. Aggregate metrics: MTTR, open critical count, recurring classes

**Compliance:** map controls to delivery artifacts (pipeline configs, scan reports, access reviews, change tickets).

**See `references/compliance_evidence.md` for SOC 2 / ISO 27001 / SSDF mapping and audit artifact list.**

## When to load references

- **SAST, SCA, secrets, IaC scans** → `references/shift_left_scanning.md`
- **Pipeline gates, OIDC, GitHub/GitLab hardening** → `references/cicd_security_gates.md`
- **SBOM, signing, dependencies** → `references/supply_chain.md`
- **K8s, CSPM, WAF, runtime** → `references/cloud_runtime_security.md`
- **STRIDE, abuse cases, review templates** → `references/threat_modeling.md`
- **SLAs, SOC 2/ISO evidence** → `references/compliance_evidence.md`
