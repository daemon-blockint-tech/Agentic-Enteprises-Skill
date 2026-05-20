---
name: cloud-system-administrator
description: |
  Guides cloud system administration—day-2 operations on AWS, GCP, and Azure: access requests and
  IAM role assignment, key and certificate rotation, OS patching and maintenance windows, backup
  and restore execution, monitoring and alert triage, quota and limit increases, runbooks, change
  records, and on-call troubleshooting of cloud control-plane and managed-service issues.
  Use when operating an existing cloud estate, fulfilling access tickets, running restores,
  responding to cloud infra alerts, or executing hygiene cleanup—not for greenfield VPC/service
  build-out (cloud-engineer), cloud architecture ADRs (cloud-architect), enterprise CCoE programs
  (enterprise-cloud-architect), CI/CD pipelines (devops), Kubernetes cluster admin
  (cluster-deployment-engineer), or designing SEV/on-call programs (incident-management-engineer).
---

# Cloud System Administrator

## When to Use

- Process **access requests** — IAM roles, group membership, break-glass (per policy)
- Execute **credential rotation** — access keys, service account keys, certificates
- Run **patch and maintenance** windows for VMs and managed instance groups
- Operate **backups** — snapshots, retention checks, test restores
- **Triage alerts** — CPU, disk, quota, health checks; escalate per runbook
- Handle **incidents** — connectivity, permission denied, throttling, regional outages
- Request **quota/limit** increases and track vendor cases
- Perform **hygiene** — orphaned volumes, old snapshots, untagged resources, idle compute
- Maintain **runbooks** and execute **change tickets** for routine infra changes
- Support **audit** — access reviews, log exports, evidence for reviewers

## When NOT to Use

- Design landing zones, migration, or reference architecture → `cloud-architect`, `enterprise-cloud-architect`
- Build new VPC, RDS, or serverless stacks from requirements → `cloud-engineer`
- Terraform module libraries and platform IaC → `infrastructure-engineer`
- Pipeline failures and GitOps sync → `devops`
- K8s cluster upgrades and Helm → `cluster-deployment-engineer`
- Define SEV levels, paging policy, postmortem program → `incident-management-engineer`
- Security program, IdP design, SIEM → `information-security-engineer`
- Entitlement design, access review campaigns, federation architecture → `iam-specialist`
- Application bug fixes → `senior-software-engineer`
- GL reconciliation of cloud invoices → `compute-accounting-manager`

## Related skills

| Need | Skill |
|---|---|
| New cloud build and deep service config | `cloud-engineer` |
| Cloud architecture | `cloud-architect` |
| Enterprise cloud governance | `enterprise-cloud-architect` |
| CI/CD and delivery SRE | `devops` |
| Kubernetes operations | `cluster-deployment-engineer` |
| Incident program design | `incident-management-engineer` |
| Security architecture | `information-security-engineer` |
| IAM governance, reviews, PAM policy (not ticket execution) | `iam-specialist` |
| Compliance evidence | `compliance-engineer` |
| BCM program, RTO/RPO, restore-test criteria, cyber recovery sequencing | `bcm-disaster-recovery-specialist` |
| Customer-facing support tickets | `support-engineer` |
| Status/comms for major outages | `communication-lead` |

## Core Workflows

### 1. Scope and operations model

Responsibilities, escalation, change control.

**See `references/cloud_sysadmin_scope.md`.**

### 2. IAM and access operations

Requests, reviews, rotation.

**See `references/iam_access_operations.md`.**

### 3. Compute and OS maintenance

Patching, instances, disks.

**See `references/compute_os_maintenance.md`.**

### 4. Monitoring and incident response

Alerts, triage, runbooks.

**See `references/monitoring_incident_response.md`.**

### 5. Backup and restore operations

Snapshots, drills, recovery steps.

**See `references/backup_restore_operations.md`.**

### 6. Operational hygiene

Quotas, certs, cleanup, DNS ops.

**See `references/operational_hygiene.md`.**

## Outputs

- **Completed change** — ticket ID, steps, rollback noted
- **Access grant record** — who, what role, expiry if temporary
- **Incident timeline** — detection, actions, resolution, follow-ups
- **Restore report** — RPO achieved, data validated
- **Hygiene report** — resources removed, savings estimate
- **Runbook update** — gaps found during incident

## Principles

- **Least privilege** — grant minimum role; time-bound elevation
- **Change control** — no prod change without ticket and rollback
- **Automate repeat work** — scripts over manual clicks where safe
- **Document actions** — audit trail in ticket and logs
- **Escalate architecture** — recurring failures may need `cloud-engineer` or `cloud-architect`
