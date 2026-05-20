---
name: information-security-engineer
description: |
  Guides information security engineering—implementing and operating security controls, identity and
  access systems, encryption and secrets management, security tool integrations (SIEM, EDR, SOAR),
  cloud guardrails, hardening baselines, and remediation engineering for vulnerabilities.
  Use when building SSO/RBAC/PAM patterns, configuring KMS or certificate lifecycle, deploying WAF/DLP
  or EDR connectors, writing security-as-code policies (OPA, SCPs, CIS benchmarks), integrating
  logging to SIEM, automating security workflows, or validating control fixes—not for SOC triage
  (soc-analyst), pentesting (penetration-tester, network-pentester, web-pentester), red team
  (red-team-specialist), CI gates only (devsecops), platform provisioning without security ownership
  (infrastructure-engineer), CISO/exec program (chief-information-security-officer),
  security program strategy (cybersecurity), GRC program and audit prep (compliance-specialist),
  or product tenancy isolation (product-infrastructure-security-engineer).
---

# Information Security Engineer

## When to Use

- Implement and operate security controls such as SSO, RBAC, PAM, KMS, certificate management, WAF, DLP, EDR, or SIEM integrations
- Translate security architecture, audit findings, or policies into deployable guardrails and validation checks
- Build identity, encryption, secrets, logging, or security automation workflows
- Harden cloud accounts, endpoints, SaaS apps, and baseline configurations with security ownership
- Validate remediation for vulnerabilities and control gaps

## When NOT to Use

- Board briefings, risk appetite, security budget, crisis exec comms → `chief-information-security-officer`
- Define security strategy or enterprise security program → `cybersecurity`
- GRC program, framework scope, audit prep, questionnaires → `compliance-specialist`
- Triage alerts, SOC playbooks, or shift ops → `soc-analyst`
- Deep investigation, hunts, or detection authoring → `defensive-security-analyst`
- Execute authorized pentests or exploit validation → `penetration-tester`, `network-pentester`, `web-pentester`
- Plan adversary simulation or purple-team campaigns → `red-team-specialist`
- Add CI/CD security gates, SBOMs, or artifact signing only → `devsecops`
- Design tenant isolation and product data-plane boundaries → `product-infrastructure-security-engineer`
- Cloud org guardrails, CSPM, multi-account IAM/network security → `cloud-security-engineer`
- IAM program design, access reviews, federation, PAM, SoD (without tool deploy) → `iam-specialist`

## Related skills

| Need | Skill |
|---|---|
| CISO program, board KRIs, appetite, budget | `chief-information-security-officer` |
| AWS/GCP/Azure guardrails, CSPM, cloud IAM/network | `cloud-security-engineer` |
| GRC program, gap plans, audit coordination | `compliance-specialist` |
| Security strategy, policies | `cybersecurity` |
| Audit evidence automation | `compliance-engineer` |
| CI/CD scans, SBOM, pipeline OIDC | `devsecops` |
| VPC, K8s, Terraform platform (general) | `infrastructure-engineer` |
| SOC triage and SOAR playbooks | `soc-analyst` |
| Red team gaps → detection content | `red-team-specialist` |
| Declared security incident response (CSIRT) | `incident-responder` |
| STIX/TAXII feed requirements, intel-driven blocklists | `cti-analyst` |
| Threat hunts and detection engineering | `defensive-security-analyst` |
| Pentest findings to reproduce | `penetration-tester`, `network-pentester`, `web-pentester` |
| Control documentation | `tech-writer-researcher` |
| Product tenancy, customer data plane | `product-infrastructure-security-engineer` |
| CVD program, bounty, disclosure calendar | `technical-program-manager-security-cvd` |
| Post-incident artifact analysis and chain of custody | `digital-forensics-analyst` |
| Risk registers, residual scoring, treatment decisions | `security-risk-analyst` |
| IAM lifecycle, entitlements, reviews, federation, PAM | `iam-specialist` |
| BCM/DRP for security tooling, immutability, restore tests | `bcm-disaster-recovery-specialist` |

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
