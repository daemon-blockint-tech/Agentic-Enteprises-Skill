# Secure service defaults

## Table of contents

1. [Launch checklist](#launch-checklist)
2. [Anti-patterns](#anti-patterns)

## Launch checklist

- [ ] No default credentials; bootstrap via sealed secrets
- [ ] Health endpoints do not leak internal state
- [ ] Admin/debug endpoints disabled in prod or behind break-glass
- [ ] CORS and cookie flags correct for product domains
- [ ] SSRF protections on outbound fetch from user URLs
- [ ] Dependency pins; no critical CVEs on release branch
- [ ] Security headers on customer-facing HTTP

## Anti-patterns

- Global admin API key shared across services
- Trusting `X-Tenant-Id` header without signature
- Logging full request bodies with PII
- Shared cache keys without tenant prefix
- Background jobs without tenant scoping
