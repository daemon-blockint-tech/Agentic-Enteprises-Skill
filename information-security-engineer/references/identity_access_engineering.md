# Identity and access engineering

## Table of contents

1. [Human access](#human-access)
2. [Service accounts](#service-accounts)
3. [Privileged access](#privileged-access)
4. [Anti-patterns](#anti-patterns)

## Human access

- Single IdP (OIDC/SAML) for workforce apps
- MFA required; phishing-resistant methods for admins
- Group-based RBAC; avoid direct user-to-resource bindings at scale
- Joiner/mover/leaver automation from HR source of truth

## Service accounts

- One workload = one identity (no shared “app user”)
- Short-lived credentials via IAM roles / workload identity
- API keys only when unavoidable; stored in secret manager with rotation

## Privileged access

- PAM or just-in-time elevation for production admin
- Session recording where required by policy
- Separate admin accounts; no daily-driver admin

## Anti-patterns

- Long-lived root/cloud owner keys
- Shared break-glass without monitoring
- Role sprawl with `*:*` permissions
- SAML/OIDC misconfiguration allowing assertion replay or weak signature validation
