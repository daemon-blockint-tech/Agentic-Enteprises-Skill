# Identity lifecycle and governance

## Table of contents

1. [Lifecycle events](#lifecycle-events)
2. [Provisioning and deprovisioning](#provisioning-and-deprovisioning)
3. [Access reviews](#access-reviews)
4. [Exceptions and emergency access](#exceptions-and-emergency-access)

## Lifecycle events

Map every identity type to HR or authoritative triggers:

| Event | Workforce | Contractor | Service account |
|---|---|---|---|
| Join | HR hire → IdP account → default roles | Start date + sponsor | Ticket + owner approval |
| Move | Role/ dept change → entitlement delta | Extension or scope change | Owner change review |
| Leave | Terminate → disable → revoke within SLA | End date auto-expire | Decommission + key revoke |
| Leave (urgent) | Same-day disable; manager notify | Disable immediately | Rotate secrets |

**SLAs (example targets):**

- Joiner productive access: ≤ 1 business day for standard roles
- Leaver disable: ≤ 4 hours for termination; ≤ 24 hours for voluntary notice end
- Privileged revoke on leave: immediate

## Provisioning and deprovisioning

1. **Source of truth** — HRIS or contractor system drives workforce; CMDB or service catalog for apps
2. **Birthright access** — default groups by job code; no manual “copy user” as standard
3. **Request-based access** — catalog with approval, SoD check, time limit where needed
4. **Provisioning transport** — SCIM to SaaS; group sync to cloud; API for custom apps
5. **Deprovision** — disable IdP first; cascade to apps; revoke tokens and sessions
6. **Orphan detection** — quarterly report: accounts without HR match or inactive > 90 days

Validate with **negative tests**: terminated user cannot SSO; API keys invalidated.

## Access reviews

Run campaigns on a risk-based cadence:

| Entitlement tier | Review frequency | Attestor |
|---|---|---|
| Privileged / admin | Quarterly | Manager + security spot-check |
| Sensitive data apps | Semi-annual | Manager |
| Standard apps | Annual | Manager |
| Service accounts | Semi-annual | Technical owner |

**Campaign steps:**

1. Define scope (app, role, population, point-in-time)
2. Pre-cleanse — remove already-terminated, merge duplicates
3. Present **role + permission detail** (not app name only)
4. Capture attest: retain / revoke / modify with justification
5. Auto-revoke on non-response per policy (with exec exception path)
6. Export evidence for auditors — who attested, when, outcome

Use **risk-based sampling** only when population is huge; document sampling method.

## Exceptions and emergency access

- **Temporary elevation** — max duration, approver, auto-expiry, ticket ID
- **Emergency break-glass** — separate accounts, MFA, session log, post-use review within 24h
- **Exception register** — compensating control, expiry date, executive approver for SoD conflicts

Never leave “permanent exceptions” without expiry and named owner.
