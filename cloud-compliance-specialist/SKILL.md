---
name: cloud-compliance-specialist
description: |
  Guides cloud compliance—mapping SOC 2, ISO 27001, HIPAA, PCI DSS, FedRAMP, and data-residency
  requirements to cloud controls; collecting audit evidence from AWS, GCP, and Azure APIs;
  shared-responsibility narratives; CSPM/Config continuous monitoring; customer assurance
  questionnaires (CAIQ/SIG); and cloud-specific gap remediation before attestations.
  Use when scoping regulated workloads in cloud, preparing cloud control evidence for auditors,
  interpreting provider compliance artifacts (BAA, PCI AOC, FedRAMP packages), or proving
  residency and logging in multi-account estates—not for org-wide GRC programs and audit coordination
  without cloud evidence (compliance-specialist), non-cloud systems evidence automation
  (compliance-engineer), implementing security guardrails (cloud-security-engineer),
  legal DPAs or contract redlines (commercial-counsel), security strategy (cybersecurity), or
  CI pipeline gates only (devsecops).
---

# Cloud Compliance Specialist

## When to Use

- Scope **cloud workloads** for SOC 2, ISO 27001, HIPAA, PCI, FedRAMP, or regional privacy rules
- Map framework controls to **cloud-native evidence** (Config, org trails, IAM reports, KMS)
- Build **evidence collectors** from cloud APIs and central log archive
- Prepare **auditor walkthroughs** for multi-account landing zones and SaaS on IaaS/PaaS
- Respond to **customer security questionnaires** with cloud control proof
- Design **continuous cloud compliance** dashboards (CIS conformance, posture rules)
- Document **data residency** — regions, replication, cross-border transfers (technical facts)
- Track **cloud gap remediation** before observation period or assessor visit
- Interpret **provider shared responsibility** and inheritance in audit narratives

## When NOT to Use

- Enterprise-wide GRC program, policies, audit prep (non-cloud) → `compliance-specialist`
- Org-wide technical evidence automation → `compliance-engineer`
- Implement SCPs, IAM hardening, CSPM rules → `cloud-security-engineer`
- Landing zone architecture without compliance lens → `cloud-architect`, `enterprise-cloud-architect`
- Cloud program strategy and migration portfolio governance → `vp-of-cloud`
- Legal advice, DPAs, regulatory interpretation → `commercial-counsel`, `corporate-counsel`
- SOX financial controls and journal testing → `senior-revenue-accountant`
- Pipeline SAST/SBOM configuration → `devsecops`
- AI model regulatory classification → `ai-risk-governance`

## Related skills

| Need | Skill |
|---|---|
| VP cloud program and regulated placement themes | `vp-of-cloud` |
| GRC program, scope, gap plans, audit coordination | `compliance-specialist` |
| Cross-domain compliance and evidence automation | `compliance-engineer` |
| Cloud security control implementation | `cloud-security-engineer` |
| Enterprise cloud governance and CCoE | `enterprise-cloud-architect` |
| Cloud reference architecture | `cloud-architect` |
| Security program strategy | `cybersecurity` |
| Pipeline and SSDF evidence | `devsecops` |
| Data governance and privacy architecture | `data-architect` |
| Physical DC compliance evidence | `data-center-design-execution-lead` |
| FinOps spend analysis | `finops-analyst` |
| GL mapping and invoice reconciliation | `compute-accounting-manager` |
| Security risk registers and third-party risk tiers | `security-risk-analyst` |

## Core Workflows

### 1. Scope and shared responsibility

Cloud in-scope boundaries and provider vs customer duties for audits.

**See `references/cloud_compliance_scope.md`.**

### 2. Framework mapping in cloud

SOC 2, ISO, HIPAA, PCI, FedRAMP control patterns on cloud.

**See `references/framework_cloud_mapping.md`.**

### 3. Cloud evidence collection

API sources, samples, retention for assessors.

**See `references/cloud_evidence_collection.md`.**

### 4. Residency and sovereignty

Regions, replication, cross-border technical documentation.

**See `references/residency_sovereignty.md`.**

### 5. Continuous cloud monitoring

CSPM, Config rules, drift and exceptions.

**See `references/continuous_cloud_monitoring.md`.**

### 6. Audit readiness and customer assurance

Walkthroughs, CAIQ/SIG, gap closure.

**See `references/audit_readiness_cloud.md`.**

## Outputs

- **Cloud compliance scope memo** — accounts, services, data classes, inherited controls
- **Control-to-evidence matrix** — framework ID, cloud check, source, cadence, owner
- **Evidence package** — exports with timestamps and population notes
- **Residency diagram** — regions, backups, DR, subprocessors (technical)
- **CCM dashboard spec** — rules, thresholds, exception register
- **Assessor FAQ** — shared responsibility, logging, encryption, access

## Principles

- **Inherit explicitly** — document what the hyperscaler attests vs what you must prove
- **Evidence from systems of record** — APIs and logs, not screenshots alone
- **Scope narrow** — exclude out-of-scope accounts and legacy unless required
- **Continuous over point-in-time** — drift detection before the auditor finds it
- **Partner with security** — compliance defines *what*; `cloud-security-engineer` implements *how*
