# Service Inventory and Dependency Analysis

## Inventory template

Capture one row per deployable (service, worker, batch job with HTTP/gRPC surface):

| Field | Notes |
|---|---|
| Service ID | Stable key in catalog |
| Display name | Human label |
| Owner team | On-call rotation or group |
| Tier | 0–3 (customer-critical → internal) |
| Repositories | Mono vs multi-repo |
| Runtime | K8s workload, VM, serverless, mesh sidecar |
| Environments | prod regions, staging parity |
| Public APIs | REST/gRPC/GraphQL routes |
| Events published / subscribed | Topic/stream names |
| Data stores | DB, cache, queue owned or shared |
| Last deploy | Date, version, drift flag |
| SLO defined? | Y/N + link |

## Discovery sources

| Source | Yields |
|---|---|
| Service catalog / Backstage | Owners, tiers, links |
| API gateway / ingress | External routes, rate limits |
| Service mesh (Istio/Linkerd) | mTLS graph, retries, timeouts |
| APM (Datadog, Honeycomb, etc.) | Call edges, latency, error rate |
| Log/trace correlation | De facto dependencies |
| Terraform/K8s manifests | Deployed names, env vars pointing to peers |
| Message broker ACLs | Topic producers/consumers |
| Shared DB connection strings | Shared-fate risks |

## Dependency map rules

1. **Node** = deployable + major data store (if owned).
2. **Edge** = observed traffic (sync) or subscription (async); label protocol and direction.
3. **Weight edges** by RPS, error contribution, or business criticality when data exists.
4. Mark **synthetic** edges (config-only, no recent traffic) separately from **active** edges.

## Dependency graph outputs

- **System context** (1 diagram): actors and top external integrations.
- **Container/service map**: all in-scope services with tier coloring.
- **Critical path overlay**: user-journey services highlighted.
- **Fan-in / fan-out table**: services with >N inbound or outbound deps (coupling smell).

## Sync chain analysis

Document chains longer than 3 hops on tier-0/1 paths:

```
Client → BFF → Order → Inventory → Pricing → Legacy
```

For each chain record: p99 latency budget, timeout cascade risk, partial failure behavior, and idempotency gaps.

## Zombie and orphan detection

| Signal | Interpretation |
|---|---|
| Zero traffic 30+ days | Candidate retire or mis-cataloged |
| Deploy stopped, pods running | Version skew / forgotten service |
| No owner in catalog | Governance gap |
| Duplicate names across envs | Inventory normalization needed |

## Inventory quality checks

- [ ] Every tier-0/1 service has an owner and on-call
- [ ] Every external API has a contract pointer or "missing contract" flag
- [ ] Shared data stores list **all** writers (not just primary)
- [ ] Environments documented; prod-only deps called out

## Handoffs

- Unclear **domain boundaries** for a hotspot → `microservice-researcher`
- Missing **platform golden paths** for standardization → `platform-engineer`
- Mesh/gateway **misconfiguration** remediation → `infrastructure-engineer`, `cloud-engineer`
