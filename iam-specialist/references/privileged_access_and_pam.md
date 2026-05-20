# Privileged access and PAM

## Table of contents

1. [Privileged account types](#privileged-account-types)
2. [PAM capabilities](#pam-capabilities)
3. [JIT elevation](#jit-elevation)
4. [Break-glass](#break-glass)
5. [Monitoring and review](#monitoring-and-review)

## Privileged account types

| Type | Examples | Controls |
|---|---|---|
| Tier 0 | Domain admin, cloud org admin, IdP super-admin | PAM vault; no daily use |
| Tier 1 | Server admin, namespace admin, DB admin | JIT + session log |
| Tier 2 | Operator, deployer to non-prod | Time-bound roles |
| Break-glass | Emergency root | Sealed credentials; heavy audit |

**Separate** privileged accounts from standard workforce accounts — no shared mailbox admins.

## PAM capabilities

Implement in priority order:

1. **Credential vaulting** — rotate passwords/keys; checkout/check-in
2. **Session management** — proxy RDP/SSH/SQL; record where regulated
3. **Approval workflows** — manager or peer for production access
4. **Just-in-time** — Azure PIM, AWS IAM Identity Center, GCP PAM, or third-party
5. **Discovery** — scan for local admins, orphaned keys, shadow SaaS admins

Align vault coverage with **risk tier** — Tier 0 first, then production paths.

## JIT elevation

Workflow:

1. User requests role or resource scope with ticket reference
2. SoD and approval checks (automated where possible)
3. Grant **time-bound** assignment (e.g., 1–8 hours)
4. Notify security; log activation event
5. Auto-revoke at expiry; confirm revocation in audit

**Deny** standing permanent admin in production unless exception registered.

For **CI/CD and automation**, use workload identity — not vaulted human passwords.

## Break-glass

1. **Dedicated accounts** — not personal users; strong MFA hardware
2. **Storage** — split knowledge or sealed envelope; vault checkout
3. **Trigger** — incident commander approval; major outage criteria
4. **Usage** — single purpose; time box; parallel notification to security
5. **Post-incident** — credential rotation; session review; incident record

Cloud: prefer **break-glass roles** in separate account with SCP guardrails (`cloud-security-engineer` for SCP design).

## Monitoring and review

- Alert on: vault checkout, JIT activation, break-glass login, new admin group member
- Correlate IdP, PAM, and cloud **CloudTrail/Audit Logs**
- Weekly sample of privileged sessions; quarterly full access review
- Metric: % admin access that is JIT vs standing; mean time to revoke on leave

Remediation of **misused break-glass** is incident-driven — partner with `incident-responder` when abuse suspected.
