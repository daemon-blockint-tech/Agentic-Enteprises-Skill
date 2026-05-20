# Security, governance, and API gateways

## Table of contents

1. [Trust zones](#trust-zones)
2. [Authentication patterns](#authentication-patterns)
3. [API gateway capabilities](#api-gateway-capabilities)
4. [B2B vs internal](#b2b-vs-internal)
5. [Governance](#governance)

## Trust zones

| Zone | Typical callers | Controls |
|---|---|---|
| Internet partner | External B2B, webhooks | WAF, mTLS or OAuth, IP allowlists, rate limits |
| DMZ integration | Edge adapters | Mutual TLS, hardened egress, secret rotation |
| Internal mesh | Services, platform jobs | mTLS/service identity, network policies |

Never expose internal admin or debug routes on partner gateways.

## Authentication patterns

| Pattern | Use when |
|---|---|
| **OAuth2 client credentials** | Machine-to-machine partner APIs |
| **OAuth2 authorization code** | User-delegated access to integration admin UIs |
| **OIDC** | Identity claims for human operators |
| **mTLS** | High-trust B2B, fixed partner endpoints |
| **HMAC-signed webhooks** | Inbound partner push with shared secret rotation |
| **API keys** | Low-risk internal tools only; not sole control for partners |

Apply **least-privilege scopes** per partner profile. Rotate credentials on schedule and on incident.

Security program ownership (IdP, KMS, corporate policy) → `information-security-engineer`.

## API gateway capabilities

Configure gateways (Kong, Apigee, AWS API Gateway, Azure APIM, etc.) for:

- **Routing** — path/host-based to upstream clusters
- **Rate limiting** — per client ID, per IP, burst + sustained
- **Quota** — daily/monthly caps for partner tiers
- **Request/response transformation** — headers, URL rewrites (keep complex logic in ACL services)
- **TLS termination** and certificate management
- **Request validation** — OpenAPI validation at edge when appropriate
- **Analytics** — latency, 4xx/5xx, quota exhaustion

Prefer **thin gateway, thick ACL** for business rules.

## B2B vs internal

| Dimension | B2B partner API | Internal service API |
|---|---|---|
| Change velocity | Slow; announced deprecations | Faster with contract tests |
| Auth | OAuth/mTLS, partner onboarding | Service identity, mesh policy |
| Documentation | Public partner portal, SLAs | Internal catalog / Backstage |
| Error detail | Safe, stable codes | Richer diagnostics for owners |
| Testing | Certification environment | Staging with synthetic data |

Run **partner certification** before production: contract tests, negative cases, load smoke.

## Governance

- **API catalog** — register every external surface with owner and lifecycle state
- **Review gate** — security + architecture for new partner integrations
- **Standard headers** — `X-Correlation-Id`, `traceparent`, optional `X-Partner-Id`
- **Data classification** — tag payloads; block PII in logs and DLQ dumps
- **Exception process** — time-boxed waivers with expiry

Classified environments and cleared pipeline boundaries → `classified-software-devsecops-engineer`.

Pipeline security scanning → `devsecops`.
