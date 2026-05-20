# Cloud compliance scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Shared responsibility for audits](#shared-responsibility-for-auditors)
3. [Scoping dimensions](#scoping-dimensions)
4. [Provider artifacts](#provider-artifacts)

## Role boundary

| cloud-compliance-specialist | Partner |
|---|---|
| Cloud control mapping and cloud API evidence | `compliance-engineer` — org-wide programs |
| Evidence requirements and assessor packages | `cloud-security-engineer` — control implementation |
| Landing zone design | `cloud-architect` |
| Legal contracts and DPAs | `commercial-counsel` |

Do not provide legal conclusions; document **technical** scope and artifacts.

## Shared responsibility for audits

Prepare a **responsibility matrix** per workload type:

| Area | Typically inherited (verify current provider docs) | Customer must demonstrate |
|---|---|---|
| Physical security | Often provider | — |
| Hypervisor | Often provider | — |
| IAM configuration | — | Yes |
| Network segmentation | — | Yes |
| Encryption key policy | — | Yes |
| Audit logging enablement | — | Yes |
| Application security | — | Yes |

Auditors will ask: *What did you configure vs what does the SOC report cover?* Cite provider **compliance reports** (e.g., SOC 2 Type II for service) plus your **customer responsibility** evidence.

## Scoping dimensions

Define in-scope:

- **Cloud accounts/subscriptions** and OUs
- **Regions** (residency)
- **Services** — EC2/RDS vs Lambda vs SaaS; PCI often excludes unmanaged IaaS unless in scope
- **Data classes** — PHI, PCI CHD, PII
- **Environments** — prod only vs prod+staging
- **Subprocessors** — list with cloud region and contract reference (legal owns contracts)

Document **exclusions** with risk acceptance and approver.

## Provider artifacts

Collect and index (do not substitute for customer evidence):

| Need | Typical artifact |
|---|---|
| SOC 2 for cloud platform | Provider SOC report (under NDA) |
| HIPAA | BAA with provider |
| PCI | Provider AOC / responsibility matrix |
| FedRAMP | Package for authorized services (GovCloud) |
| ISO | Provider certificate scope |

Maintain version and review date; map to services **you actually use**.
