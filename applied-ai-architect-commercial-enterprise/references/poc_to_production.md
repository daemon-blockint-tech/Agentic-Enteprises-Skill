# POC to production

## Table of contents

1. [Stage gates](#stage-gates)
2. [Architecture evolution](#architecture-evolution)
3. [Production checklist](#production-checklist)
4. [Decommission POC](#decommission-poc)

## Stage gates

| Stage | Data | Architecture | Exit criteria |
|---|---|---|---|
| **POC** | Synthetic or anonymized | Single env, manual config | Demo success metric hit |
| **Pilot** | Real subset, named users | Tenant rules, basic audit | Eval pass + security review |
| **Limited GA** | Production classes | SLOs, rate limits, on-call | 2 weeks stable metrics |
| **GA** | Full | DR, cost dashboards, runbooks | Steady state ops handoff |

Never skip pilot with production PII without explicit risk acceptance.

## Architecture evolution

**POC shortcuts to remove:**

- Hardcoded API keys → vault + rotation
- Shared dev index → partitioned prod indexes
- No authz on retrieval → enforce ACL filter
- Console logging → structured audit pipeline
- Single model, no fallback → router + degraded mode

**Add before GA:**

- CI eval regression (`ai-engineer`)
- Canary by tenant or percentage
- Cost alerts per feature (`ai-lead-ops`)
- Customer-facing status for AI outages

## Production checklist

- [ ] Threat model for AI path (prompt injection, tool abuse)
- [ ] Red-team for tier-2+ (`ai-redteam`)
- [ ] Load test retrieval + inference at peak QPS
- [ ] Data deletion and tenant offboarding tested
- [ ] Model/prompt version registry and rollback tested
- [ ] Support playbooks (wrong answer, outage, abuse)
- [ ] Documentation for admins (data scope, limits)

## Decommission POC

- Delete POC indexes and keys
- Revoke POC service principals
- Confirm no prod data copied to dev accounts

Hand off to `ai-lead-ops` for ongoing release and cost governance.
