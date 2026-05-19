# Commercial vs enterprise

## Table of contents

1. [Decision guide](#decision-guide)
2. [Commercial product AI](#commercial-product-ai)
3. [Enterprise internal AI](#enterprise-internal-ai)
4. [Hybrid (common)](#hybrid-common)

## Decision guide

| Question | Lean commercial | Lean enterprise |
|---|---|---|
| Who pays? | Customer subscription | IT budget / chargeback |
| Whose data? | Customer tenant data | Employer corp data |
| Blast radius of leak | Cross-customer | Regulatory + IP |
| Release cadence | Product sprint | Change advisory board |
| Identity | App user + tenant | Corporate IdP groups |

Many vendors ship **both**: same stack, different control planes and contracts.

## Commercial product AI

**Architecture must-haves:**

- **Tenant isolation** at every layer (index, cache, object store, logs)
- **No cross-tenant retrieval** — partition keys, separate indexes, or metadata filters enforced in code
- **Configurable retention** per tenant; deletion on churn
- **Usage metering** — tokens, seats, or feature flags for billing
- **Customer-visible** behavior changes → versioning, release notes, opt-out where required

**Typical patterns:**

- Embedded copilot in SaaS app (RAG on tenant docs)
- API-accessible AI features with rate limits
- Optional BYOK or customer-managed keys (enterprise tier)

Route security depth to `product-infrastructure-security-engineer`.

## Enterprise internal AI

**Architecture must-haves:**

- **Private connectivity** to model APIs (VPC endpoint, no public egress)
- **Source system ACLs** respected at retrieval (SharePoint, Confluence, tickets)
- **Group-aware** answers — user A must not see HR docs
- **Audit** for compliance: who asked, what retrieved, model version
- **Human oversight** for high-impact actions (write-back to systems)

**Typical patterns:**

- Microsoft 365 / Google Workspace copilot integrations
- Service desk and policy Q&A
- Code and runbook assistants on private repos

Coordinate with `information-security-engineer` and `ai-risk-governance` early.

## Hybrid (common)

| Pattern | Note |
|---|---|
| Same RAG stack, dual deployment | Prod multi-tenant + single-tenant VPC for regulated customers |
| Enterprise SSO into commercial product | SAML + tenant provisioning |
| Customer brings own model endpoint | Proxy in customer cloud; you run orchestration only |

Document **data flow diagram** showing where prompts and retrieved text cross trust boundaries.
