# IAM access operations

## Table of contents

1. [Access request workflow](#access-request-workflow)
2. [Role assignment](#role-assignment)
3. [Reviews and offboarding](#reviews-and-offboarding)
4. [Credential rotation](#credential-rotation)

## Access request workflow

1. Validate **ticket** — requester, manager approval, justification, duration
2. Map need to **predefined role** — avoid inline custom policies in prod
3. Apply in correct **account/subscription** — verify environment tag
4. Confirm **MFA** and SSO path for human access
5. Notify requester; log in access register

Deny if: no approval, excessive permissions, prod break-glass without incident.

## Role assignment

Prefer:

- **Group-based** roles over user-attached policies
- **Assumed roles** with session duration limits
- **Workload roles** for apps — no long-lived keys

Cross-account: verify **trust policy** and external ID match standard.

Architecture changes to roles → `cloud-engineer` with security review.

## Reviews and offboarding

Quarterly **access review**:

- List users/roles per account
- Owners attest or revoke
- Remove stale **SSO assignments** and cloud bindings same day as HR term

Emergency revoke: disable SSO session + detach policies + rotate shared secrets if any.

## Credential rotation

| Asset | Cadence | Procedure |
|---|---|---|
| Access keys | 90d or policy | Create new, deploy, delete old |
| Service account keys | Per policy | Prefer workload identity instead |
| TLS certs | Before expiry | ACM/Let's Encrypt automation; manual fallback runbook |
| DB passwords | Per policy | Secrets Manager rotation window |

Never paste secrets in tickets or chat — use vault references.
