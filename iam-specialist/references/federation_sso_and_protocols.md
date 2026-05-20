# Federation, SSO, and protocols

## Table of contents

1. [Protocol choice](#protocol-choice)
2. [SAML patterns](#saml-patterns)
3. [OIDC patterns](#oidc-patterns)
4. [SCIM provisioning](#scim-provisioning)
5. [SaaS onboarding checklist](#saas-onboarding-checklist)

## Protocol choice

| Protocol | Typical use | Notes |
|---|---|---|
| SAML 2.0 | Enterprise SaaS, legacy apps | XML signatures; clock skew matters |
| OIDC | Modern apps, mobile, APIs | Prefer for new integrations |
| OAuth 2.0 | API delegation (not SSO alone) | Pair with OIDC for identity |
| SCIM 2.0 | User/group provision to SaaS | Complements SSO; not authentication |

**IdP as hub:** workforce authenticates once; federate to apps; enforce MFA at IdP.

## SAML patterns

1. **Metadata exchange** — sign and encrypt assertions per vendor matrix
2. **NameID** — stable identifier (email or employee ID); avoid display name
3. **Attribute mapping** — least claims; map groups to app roles explicitly
4. **Audience and Recipient** — validate strictly; reject unsolicited responses
5. **Certificate rotation** — dual metadata publish before expiry
6. **Single logout** — implement only if app supports; else document session limits

Test: **IdP-initiated and SP-initiated** flows; invalid signature must fail closed.

## OIDC patterns

1. **Authorization code + PKCE** — required for public clients
2. **Client types** — confidential server apps vs public SPA/mobile
3. **Scopes** — `openid profile email` minimum; add API scopes narrowly
4. **Token lifetimes** — short access tokens; refresh rotation; revoke on logout
5. **Claims** — map groups via `groups` or custom claim with size limits
6. **Multi-tenant SaaS** — issuer per tenant; validate `iss` and `aud`

Integrate **step-up MFA** for sensitive apps via conditional access at IdP.

## SCIM provisioning

1. **Source** — IdP or IAM tool pushes users/groups
2. **Match key** — `userName` / externalId stable across systems
3. **Deactivate** — map `active: false` to suspend; do not delete audit history
4. **Group push** — map entitlement roles to SCIM groups
5. **Error handling** — alert on sync failures; reconcile daily

Run **joiner and leaver** tests in sandbox before production cutover.

## SaaS onboarding checklist

- [ ] SSO protocol (SAML/OIDC) and MFA requirement documented
- [ ] SCIM or manual provisioning with SLA
- [ ] Entitlement roles defined in catalog
- [ ] SoD rules evaluated for app permissions
- [ ] Admin roles limited; break-glass documented
- [ ] Audit logs exported (who accessed, admin actions)
- [ ] Offboarding tested — user cannot authenticate post-disable
- [ ] Data residency and subprocessors recorded for GRC

Hand off ongoing **ticket-based access** to operations runbooks where appropriate (`cloud-system-administrator` for cloud consoles only).
