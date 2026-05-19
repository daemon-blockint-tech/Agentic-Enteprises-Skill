# Reconnaissance and enumeration

## Table of contents

1. [Phases](#phases)
2. [Asset inventory](#asset-inventory)
3. [Enumeration targets](#enumeration-targets)

## Phases

| Phase | Activities |
|---|---|
| Passive | DNS, CT logs, public repos, job posts, metadata |
| Active (scoped) | Port scan, service banners, virtual host discovery |
| Application | Routes, APIs, auth flows, tech stack fingerprint |
| Cloud | Public buckets, misconfigured storage, IAM metadata (if in scope) |

Stay within ROE rate limits and scope lists.

## Asset inventory

Track per asset:

- Hostname / URL
- IP or endpoint
- Owner (if known)
- Environment (prod/stage/dev)
- Auth required (Y/N)
- Notes

## Enumeration targets

- Default credentials on admin panels
- Exposed admin interfaces and debug endpoints
- API versioning and undocumented routes
- TLS/certificate transparency for shadow IT
- Subdomain takeover candidates (dangling DNS)
