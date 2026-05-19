# Enterprise NFR and integration

## Table of contents

1. [Identity and access](#identity-and-access)
2. [Data and residency](#data-and-residency)
3. [Observability and audit](#observability-and-audit)
4. [Safety and human oversight](#safety-and-human-oversight)
5. [Integration checklist](#integration-checklist)

## Identity and access

| Requirement | Commercial | Enterprise |
|---|---|---|
| Authentication | Product session + tenant | SSO (SAML/OIDC) |
| Authorization | Tenant RBAC + feature flags | IdP groups → doc ACLs |
| Service accounts | Per-tenant or pooled | Dedicated SP with least privilege |

**Never** trust model to enforce permissions—enforce at retrieval and tool layers.

## Data and residency

Document:

- Regions for inference, embedding, and storage
- Whether data is used for provider training (contractual opt-out)
- Subprocessors list for customer DPA
- Retention: conversation, vectors, logs (TTL and delete API)

Cross-border: default deny; explicit approval for transfer mechanisms.

## Observability and audit

| Event | Log fields (minimize PII) |
|---|---|
| Request | tenant_id, user_id hash, feature, model, latency |
| Retrieval | doc ids, scores, not full text if sensitive |
| Tool call | tool name, status, correlation_id |
| Outcome | success, escalation, feedback |

Export for SIEM; align with `cybersecurity` retention policy.

## Safety and human oversight

Tier use cases (`ai-risk-governance`):

| Tier | Examples | Controls |
|---|---|---|
| Low | Draft rewrite internal | Standard guardrails |
| Med | Customer support suggest | Human review option |
| High | Legal/medical/financial advice | Block or expert-only |
| Critical | Autonomous write to prod systems | Prohibit or dual control |

## Integration checklist

- [ ] SSO and group mapping tested on real directory
- [ ] DLP scan on upload and optionally on outbound
- [ ] Rate limits per tenant and global circuit breaker
- [ ] Secrets in vault; no keys in prompts
- [ ] DR: model fallback and degraded read-only mode
- [ ] Eval suite in CI; red-team for tier-2+ (`ai-redteam`)
- [ ] Runbook for model outage and index lag
