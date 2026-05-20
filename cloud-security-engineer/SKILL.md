---
name: cloud-security-engineer
description: |
  Guides cloud security engineering on AWS, GCP, and Azure—org guardrails (SCPs, org policies),
  cloud IAM and federation, network segmentation and private connectivity, encryption and KMS,
  logging and audit to SIEM, CSPM and native detective controls (Config, Security Hub, GuardDuty,
  SCC, Defender), workload hardening, and secure cloud architecture review with remediation.
  Use when implementing or auditing cloud security controls, fixing misconfigurations, designing
  multi-account guardrails, hardening VPC/VNet and data plane access, or integrating cloud audit
  logs—not for corporate IdP/SIEM/EDR programs broadly (information-security-engineer), CI pipeline
  gates and SBOM only (devsecops), SOC alert triage (defensive-security-analyst), pentest execution
  (penetration-tester, network-pentester, web-pentester for app/API), GRC evidence packaging
  (compliance-engineer), GRC program and audit prep (compliance-specialist), or routine cloud
  provisioning without security ownership (cloud-engineer).
---

# Cloud Security Engineer

## When to Use

- Design and implement **org/account guardrails** — SCPs, policy constraints, landing zone security
- Harden **cloud IAM** — roles, trust policies, permission boundaries, federation, break-glass
- Secure **cloud networking** — segmentation, SG/NSG rules, private endpoints, egress control
- Configure **encryption** — KMS/CMK policies, default encryption, TLS, secrets managers
- Enable **audit and detective** controls — CloudTrail/Audit Logs, Config, GuardDuty, CSPM
- Remediate **misconfigurations** from scans, audits, or Well-Architected security pillar
- Review **workload designs** for cloud threat patterns (IMDS, public buckets, open SGs)
- Integrate cloud findings into **vulnerability and exception** workflows
- Support **incident forensics** with cloud log analysis (with SOC/IR partners)

## When NOT to Use

- Company security strategy, policies, board metrics → `cybersecurity`
- SSO/PAM/SIEM/EDR for corp-wide stack (non-cloud-specific) → `information-security-engineer`
- SAST/SCA/SBOM and GitHub Actions hardening → `devsecops`
- Live SOC alert triage and playbooks → `soc-analyst`
- Cloud telemetry threat hunts and ATT&CK campaigns → `threat-hunter`
- Authorized exploitation and pentest validation → `penetration-tester`
- Network/AD/infra pentest from corp paths → `network-pentester`
- Web/API OWASP testing → `web-pentester`
- GRC program, audit prep, vendor questionnaires → `compliance-specialist`
- SOC 2 control narratives and audit binders → `compliance-engineer`, `cloud-compliance-specialist`
- Build VPC/RDS without security as primary goal → `cloud-engineer`
- Landing zone business architecture and migration → `cloud-architect`
- Cloud program strategy and CCoE investment themes → `vp-of-cloud`
- Product multi-tenant isolation in app layer → `product-infrastructure-security-engineer`
- Cloud access tickets and patching → `cloud-system-administrator`
- Entitlement design, access reviews, federation, PAM → `iam-specialist`
- Customer security questionnaires, deal compliance fit (architecture) → `solutions-architect`

## Related skills

| Need | Skill |
|---|---|
| VP cloud program and risk investment themes | `vp-of-cloud` |
| Corporate security tooling and IdP | `information-security-engineer` |
| Pipeline and supply-chain security | `devsecops` |
| Cloud architecture and WAF reviews | `cloud-architect` |
| Enterprise CCoE and regulated program | `enterprise-cloud-architect` |
| Cloud resource implementation | `cloud-engineer` |
| Terraform platform modules | `infrastructure-engineer` |
| GRC program, gap plans, audit coordination | `compliance-specialist` |
| Compliance evidence (org-wide) | `compliance-engineer` |
| Cloud audit evidence and framework mapping | `cloud-compliance-specialist` |
| SOC triage and playbooks | `soc-analyst` |
| Active security IR, cloud log coordination | `incident-responder` |
| Cloud telemetry threat hunts and hunt campaigns | `threat-hunter` |
| Cloud alert investigation and detection tuning | `defensive-security-analyst` |
| Pentest validation | `penetration-tester` |
| Network/AD/infra pentest | `network-pentester` |
| Web/API OWASP pentest | `web-pentester` |
| Product tenancy | `product-infrastructure-security-engineer` |
| Customer deal security/compliance fit memo | `solutions-architect` |
| CVD and disclosure | `technical-program-manager-security-cvd` |
| Cloud audit log forensics and super-timelines after preservation | `digital-forensics-analyst` |
| Security risk registers and treatment prioritization | `security-risk-analyst` |
| IAM lifecycle, access reviews, federation, PAM | `iam-specialist` |

## Core Workflows

### 1. Scope and shared responsibility

Cloud security boundaries, provider vs customer duties.

**See `references/cloud_security_scope.md`.**

### 2. Cloud IAM and identity

Roles, federation, privilege escalation prevention.

**See `references/identity_iam_cloud.md`.**

### 3. Network security in cloud

Segmentation, private access, logging.

**See `references/network_cloud_security.md`.**

### 4. Data protection and KMS

Encryption, keys, secrets.

**See `references/data_encryption_kms.md`.**

### 5. Logging, CSPM, and detection

Audit logs, posture management, native detectors.

**See `references/detection_cspm_logging.md`.**

### 6. Architecture review and remediation

Threat patterns, review checklist, fix prioritization.

**See `references/secure_cloud_architecture_review.md`.**

## Outputs

- **Guardrail definition** — SCP/policy JSON, exceptions, rollout plan
- **IAM policy set** — least-privilege roles with trust boundaries documented
- **Network security diagram** — zones, flows allowed/denied, private endpoints
- **Remediation backlog** — finding, severity, owner, compensating control
- **Control evidence** — Config rules, scan exports, sample audit log queries
- **Architecture review notes** — risks, required controls before launch

## Principles

- **Deny by default** — explicit allow for network and IAM
- **Security as code** — guardrails versioned and reviewed like application code
- **Detect and prove** — every preventive control has a detective check
- **Break-glass is rare and monitored** — not a bypass for convenience
- **Minimize blast radius** — account segmentation and permission boundaries
