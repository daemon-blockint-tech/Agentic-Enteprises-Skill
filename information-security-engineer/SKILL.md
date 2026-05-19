---
name: information-security-engineer
description: |
  Guides information security engineering—implementing and operating security controls, identity and
  access systems, encryption and secrets management, security tool integrations (SIEM, EDR, SOAR),
  cloud guardrails, hardening baselines, and remediation engineering for vulnerabilities.
  Use when building SSO/RBAC/PAM patterns, configuring KMS or certificate lifecycle, deploying WAF/DLP
  or EDR connectors, writing security-as-code policies (OPA, SCPs, CIS benchmarks), integrating
  logging to SIEM, automating security workflows, or validating control fixes—not for SOC alert triage
  (defensive-security-analyst), authorized pentesting (offensive-security-analyst), CI pipeline gates
  only (devsecops), general platform provisioning without security ownership (infrastructure-engineer),
  or security program strategy and GRC (cybersecurity), or multi-tenant product isolation and
  customer-data boundaries in product services (product-infrastructure-security-engineer).
---

# Information Security Engineer

## When to Use

- Implement and operate security controls such as SSO, RBAC, PAM, KMS, certificate management, WAF, DLP, EDR, or SIEM integrations
- Translate security architecture, audit findings, or policies into deployable guardrails and validation checks
- Build identity, encryption, secrets, logging, or security automation workflows
- Harden cloud accounts, endpoints, SaaS apps, and baseline configurations with security ownership
- Validate remediation for vulnerabilities and control gaps

## When NOT to Use

- Define security strategy, policy, or GRC program direction → `cybersecurity`
- Triage alerts, investigate incidents, or write detections → `defensive-security-analyst`
- Execute authorized pentests or exploit validation → `offensive-security-analyst`
- Add CI/CD security gates, SBOMs, or artifact signing only → `devsecops`
- Design tenant isolation and product data-plane boundaries → `product-infrastructure-security-engineer`

## Related skills

| Need | Skill |
|---|---|
| Security strategy, policies, audit evidence | `cybersecurity` |
| CI/CD scans, SBOM, pipeline OIDC | `devsecops` |
| VPC, K8s, Terraform platform (general) | `infrastructure-engineer` |
| Alert triage and detections | `defensive-security-analyst` |
| Pentest findings to reproduce | `offensive-security-analyst` |
| Control documentation | `tech-writer-researcher` |
| Product tenancy, customer data plane | `product-infrastructure-security-engineer` |
| CVD program, bounty, disclosure calendar | `technical-program-manager-security-cvd` |

## Core Workflows

### 1. Control implementation

Translate architecture or policy into deployable controls:

1. Confirm requirement source (policy, threat model, audit finding)
2. Choose control type: preventive, detective, corrective
3. Implement in IaC or managed config (versioned, reviewed)
4. Define validation test (automated where possible)
5. Document owner, exception process, and review cadence

**See `references/control_hardening.md` for baselines and guardrail patterns.**

### 2. Identity and access engineering

```
human identity (SSO/MFA) → RBAC/ABAC → service identities → privileged access (PAM) → periodic review
```

- Federate apps to IdP; enforce MFA and conditional access
- Least-privilege IAM roles; no long-lived access keys on humans
- Break-glass accounts monitored and rare
- Quarterly access reviews with evidence export

**See `references/identity_access_engineering.md` for patterns and anti-patterns.**

### 3. Encryption and secrets

| Layer | Typical implementation |
|---|---|
| Data at rest | KMS, volume encryption, TDE |
| Data in transit | TLS 1.2+, cert automation (ACME/internal CA) |
| Application secrets | Vault, cloud secret manager, rotation |
| Keys | CMK policies, separation of duties, audit logs |

Never commit secrets; scan repos; rotate on incident.

**See `references/encryption_secrets.md` for key lifecycle and TLS checklist.**

### 4. Security tooling integration

**Integration checklist:**

1. Log/agent deployment coverage target (e.g., 95% endpoints)
2. Parser/normalization and field mapping
3. Correlation rules owned by detection team
4. SOAR playbooks for approved auto-actions only
5. Health monitoring on collectors and API quotas

**See `references/security_tooling.md` for SIEM/EDR/SOAR integration notes.**

### 5. Vulnerability remediation engineering

Work with app and platform teams:

1. Ingest findings (scanner, pentest, bug bounty)
2. Prioritize: exploitability × asset criticality × exposure
3. Assign owner and SLA by severity
4. Implement or review fix (patch, config, code)
5. Validate with rescan or analyst sign-off
6. Track exceptions with expiry

**See `references/vulnerability_remediation.md` for SLA table and validation steps.**

### 6. Change and release for security systems

Security changes are production changes:

- Peer review on IaC and policy PRs
- Staged rollout (dev → stage → prod)
- Rollback plan for IdP, WAF, or SIEM parser changes
- Post-change validation within 24h

## When to load references

- **Baselines and guardrails** → `references/control_hardening.md`
- **SSO, IAM, PAM** → `references/identity_access_engineering.md`
- **KMS, TLS, secrets** → `references/encryption_secrets.md`
- **SIEM, EDR, SOAR** → `references/security_tooling.md`
- **Fix tracking and validation** → `references/vulnerability_remediation.md`
