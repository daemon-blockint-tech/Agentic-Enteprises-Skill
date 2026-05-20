# Sizing, cost, and options

## Table of contents

1. [Sizing approach](#sizing-approach)
2. [Cost framing](#cost-framing)
3. [Build vs buy vs partner](#build-vs-buy-vs-partner)
4. [Option comparison template](#option-comparison-template)
5. [Licensing and commercial](#licensing-and-commercial)
6. [Sensitivity and ranges](#sensitivity-and-ranges)

## Sizing approach

Start from **requirements and usage**, not vendor SKUs.

1. **Workload profile** — steady vs bursty; batch windows; geographic distribution
2. **Capacity drivers** — users, transactions/sec, storage GB, API calls, messages
3. **Growth horizon** — 12–36 months; state growth rate assumptions
4. **Redundancy** — HA, DR, multi-region (multiplier on cost and ops)
5. **PoC vs prod** — right-size PoC; list what changes at scale

| Driver | Questions |
|---|---|
| Compute | vCPU/memory per request; concurrency; autoscale bounds |
| Storage | Hot vs archive; retention; replication |
| Network | Egress to partners; CDN; private link count |
| Integrations | API volume; message size and rate |
| Operations | Environments (dev/test/prod); monitoring retention |

Document **formulas or rules of thumb** (e.g., 50 RPS × 200ms × 2 instances headroom).

Hands-on rightsizing and CUR analysis → `finops-analyst`. Deep TCO/NPV → `cloud-economist`.

## Cost framing

Present **ranges**, not false precision.

| Element | Include |
|---|---|
| One-time | Implementation, migration, PoC, professional services |
| Recurring | Subscription, cloud, support, third-party APIs |
| Internal | Customer FTE, change management (qualitative if unknown) |
| Hidden | Egress, premium support, overage, commit shortfall |

**Cost drivers table** — top 5 levers that move the estimate ±20%.

Align currency, term (monthly vs annual), and **who pays** (customer cloud account vs vendor-hosted).

Cloud architecture cost pillar → collaborate with `cloud-architect`. GL and capex → `compute-accounting-manager`.

## Build vs buy vs partner

| Criterion | Build | Buy (SaaS/COTS) | Partner / SI |
|---|---|---|---|
| Time to value | Slower | Faster if fit | Depends on scope |
| Differentiation | High | Low unless extended | Medium |
| Total cost | Dev + maintain | License + config | SOW + license |
| Risk | Delivery, talent | Vendor lock, fit | Integration quality |
| Compliance | You attest | Vendor attest + config | Shared |
| Control | Full | Limited | Shared |

Recommend **one primary option** with explicit **when to reconsider** (e.g., after PoC metrics).

Non-technical portfolio prioritization → `business-consultant`.

## Option comparison template

| Dimension | Option A | Option B | Option C |
|---|---|---|---|
| Summary | One line | | |
| Time to MVP | Weeks | | |
| 3-year TCO range | $X–$Y | | |
| NFR fit | H/M/L per NFR | | |
| Security/compliance | Fit summary | | |
| Ops burden | Customer / vendor | | |
| Lock-in | Low/Med/High | | |
| Risks | Top 3 | | |
| Recommendation | — | | |

Weight dimensions to **customer-stated priorities** (cost vs speed vs risk).

## Licensing and commercial

Clarify for procurement (do not negotiate legal terms):

- Metric (users, cores, transactions, environments)
- Tier breaks and overage
- Dev/test licensing
- HA/DR doubling rules
- Third-party embeds (maps, AI APIs, data providers)

Flag **architecture choices that change license count** (e.g., extra regions, read replicas, sandboxes).

## Sensitivity and ranges

Show **low / expected / high** for:

- Usage growth ±50%
- HA/DR on vs off
- Commit vs on-demand cloud pricing
- Implementation overrun (weeks)

State **break-even** triggers where a more expensive option becomes cheaper (scale, risk reduction).

For deal economics and margin, involve finance/sales; do not invent discount authority.
