---
name: product-infrastructure-security-engineer
description: |
  Guides product infrastructure security—securing the runtime, data plane, and control plane that
  ships with the product: multi-tenant isolation, service-to-service auth, customer data boundaries,
  secure defaults in APIs and workers, abuse-resistant rate limits, product-scoped secrets and encryption,
  and security design reviews for product infra changes.
  Use when threat-modeling product features, designing tenant isolation, hardening service mesh or
  internal APIs, reviewing product IaC/modules for data leaks, defining secure baselines for
  microservices the product team owns, or partnering on incidents affecting customer workloads—not
  for corporate IdP/SIEM (information-security-engineer), CI pipeline gates only (devsecops), SOC
  operations (defensive-security-analyst), authorized pentest execution (offensive-security-analyst),
  general IDP golden paths (platform-engineer), company-wide GRC (cybersecurity), or applied AI
  solution architecture for LLM features (applied-ai-architect-commercial-enterprise).
---

# Product Infrastructure Security Engineer

## When to Use

- Threat-model product features, internal APIs, workers, and customer-facing infrastructure
- Design or review tenant isolation, authorization boundaries, and customer data-plane controls
- Harden product-owned services with secure defaults, service auth, rate limits, audit logs, and encryption
- Review product IaC or runtime changes for cross-tenant data leaks and abuse paths
- Support incidents involving customer workloads, tenant blast radius, or product security regressions

## When NOT to Use

- Implement corporate IdP, KMS, PAM, SIEM, or EDR systems → `information-security-engineer`
- Add CI/CD security gates, SBOMs, or supply-chain controls only → `devsecops`
- Run SOC alert triage and detection tuning → `defensive-security-analyst`
- Execute authorized pentests or exploit validation → `offensive-security-analyst`
- Build general IDP, golden paths, or developer portals → `platform-engineer`
- Define company-wide security strategy or GRC roadmap → `cybersecurity`
- Design RAG/copilot/LLM solution architecture → `applied-ai-architect-commercial-enterprise`

## Related skills

| Need | Skill |
|---|---|
| Org-wide IAM, KMS ops, SIEM | `information-security-engineer` |
| Pipeline scans, SBOM, CI OIDC | `devsecops` |
| Product feature code and APIs | `senior-fullstack-developer` |
| Core cloud/K8s provisioning | `infrastructure-engineer` |
| IDP templates and portal | `platform-engineer` |
| Pentest reproduction | `offensive-security-analyst` |
| Customer-impacting incident comms | `cybersecurity` |
| AI copilot/RAG architecture | `applied-ai-architect-commercial-enterprise` |
| K8s namespace isolation and deploy | `cluster-deployment-engineer` |

## Core Workflows

### 1. Product threat modeling

Scope the **product boundary** (what attackers and tenants can reach):

1. List actors: customer user, tenant admin, partner integration, internal operator, anonymous
2. Map assets: customer data, credentials, billing, config, audit logs
3. Draw data flows across services and stores
4. Identify trust boundaries (tenant, region, env)
5. Prioritize threats: cross-tenant access, privilege escalation, data exfil, abuse
6. Record mitigations and residual risk owners

**See `references/product_threat_model.md` for STRIDE-lite worksheet.**

### 2. Multi-tenant isolation

**Isolation goals:**

- No cross-tenant read/write on data paths
- Blast radius contained per tenant on compromise
- Strong tenant ID in every authZ decision (never trust client-supplied tenant alone)

Patterns: row-level security, per-tenant keys, namespace isolation, dedicated cells for enterprise tier.

**See `references/multi_tenant_isolation.md` for patterns and test cases.**

### 3. Service and API security baselines

Every product service should default to:

- Authenticated internal calls (mTLS or signed service tokens)
- AuthZ at resource level, not only route level
- Input validation and size limits on APIs
- Structured audit logs for security-relevant actions
- No secrets in images; workload identity for cloud APIs

**See `references/secure_service_defaults.md` for checklist and anti-patterns.**

### 4. Customer data protection

| Control | Product infra angle |
|---|---|
| Encryption at rest | Per-tenant or per-table keys where required |
| Encryption in transit | TLS everywhere; no TLS termination that exposes plaintext internally without justification |
| Retention | Deletion hooks for account closure |
| Logging | Redact PII in product logs; separate security audit stream |

**See `references/customer_data_protection.md` for key hierarchy and deletion workflow.**

### 5. Abuse and resilience

- Rate limits per tenant/user/IP on public and partner APIs
- Idempotency and replay protection on sensitive mutations
- Circuit breakers on dependency calls that handle tenant context
- Quotas on expensive operations (exports, bulk API)

Align with defensive monitoring for anomaly signals.

### 6. Security design review (product infra)

**Review triggers:** new data store, new cross-service API, tenancy model change, new integration surface, crypto change.

**Review output:**

- Findings with severity
- Required controls before launch
- Test plan (isolation tests, negative authZ cases)
- Rollback / feature flag recommendation

**See `references/security_design_review.md` for review template.**

### 7. Incident support (product scope)

When customer workloads are affected:

1. Confirm blast radius (which tenants, regions)
2. Preserve tenant-scoped logs and configs
3. Coordinate containment without cross-tenant impact
4. Post-incident: add regression test and detection

Hand off enterprise IR/comms to `cybersecurity` when required.

## When to load references

- **Threat modeling** → `references/product_threat_model.md`
- **Tenancy** → `references/multi_tenant_isolation.md`
- **Service baselines** → `references/secure_service_defaults.md`
- **Data and crypto** → `references/customer_data_protection.md`
- **Design reviews** → `references/security_design_review.md`
