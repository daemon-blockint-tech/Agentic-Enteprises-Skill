# Product threat model

## Table of contents

1. [Actors](#actors)
2. [STRIDE-lite worksheet](#stride-lite-worksheet)
3. [Test ideas](#test-ideas)

## Actors

| Actor | Goal | Trust |
|---|---|---|
| Tenant user | Use product within subscription | Low |
| Tenant admin | Configure tenant, invite users | Medium |
| Partner API | Integrate via scoped credentials | Medium |
| Platform operator | Support, break-glass | High (monitored) |
| Anonymous | Probe public endpoints | None |

## STRIDE-lite worksheet

| Threat | Example in SaaS | Mitigation |
|---|---|---|
| Spoofing | Stolen session | MFA, short-lived tokens |
| Tampering | IDOR on object IDs | AuthZ on every resource |
| Repudiation | Deny admin action | Immutable audit log |
| Info disclosure | Cross-tenant query bug | Tenant guard in data layer |
| DoS | API flood | Rate limits, quotas |
| Elevation | User → admin | Role checks server-side |

## Test ideas

- Two tenants A/B: A cannot read B's IDs (sequential and UUID)
- Token for tenant A rejected on tenant B hostname/header
- Deleted tenant data unreachable after retention job
