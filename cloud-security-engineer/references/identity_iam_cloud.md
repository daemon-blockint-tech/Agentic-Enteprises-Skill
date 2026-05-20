# Cloud IAM and identity

## Table of contents

1. [Human access](#human-access)
2. [Workload identity](#workload-identity)
3. [Privilege escalation paths](#privilege-escalation-paths)
4. [Reviews and break-glass](#reviews-and-break-glass)

## Human access

- **Federate** console/API via corporate IdP (`information-security-engineer` for IdP design)
- **MFA** required for all human principals; no password-only IAM users
- **Permission sets** (AWS SSO) or group-based RBAC — not direct admin on accounts
- **Session duration** limits; no permanent access keys for humans

## Workload identity

| Pattern | Use |
|---|---|
| Instance/pod role | VMs, Lambda, GKE/EKS service accounts |
| OIDC federation | CI/CD from GitHub/GitLab (`devsecops`) |
| Cross-account role | Hub-spoke with external ID and tight trust |

Rules:

- One role per workload function; no shared “super” role
- **Permission boundaries** on roles that can create IAM
- Scope resource ARNs in policies; avoid `*` on `Action` and `Resource` together

## Privilege escalation paths

Audit regularly for:

| Pattern | Risk |
|---|---|
| `iam:PassRole` + `ec2:RunInstances` | Admin instance |
| `lambda:CreateFunction` + pass admin role | Backdoor function |
| `sts:AssumeRole` on `*` in trust | Lateral movement |
| Overly broad `kms:Decrypt` | Data exfil |
| Public AMIs or snapshots | Data leak |

Use **IAM Access Analyzer**, policy simulation, and pentest findings (`offensive-security-analyst`).

## Reviews and break-glass

- Quarterly **access review** with evidence export per account
- **Break-glass** role: MFA, short session, alert on use, post-use review
- Remove unused roles and inline policies; prefer managed policy versions

Operational grants → `cloud-system-administrator`; security standard → this skill.
