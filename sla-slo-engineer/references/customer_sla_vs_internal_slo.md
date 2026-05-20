# Customer SLA vs internal SLO

## Table of contents

1. [Purpose and risk](#purpose-and-risk)
2. [Alignment matrix](#alignment-matrix)
3. [Measurement gaps](#measurement-gaps)
4. [Buffers and carve-outs](#buffers-and-carve-outs)
5. [Credits and remedies](#credits-and-remedies)
6. [Communication](#communication)
7. [Legal handoff](#legal-handoff)

## Purpose and risk

| Artifact | Audience | Engineering role |
|---|---|---|
| **SLA** | Customer, legal, sales | Make measurable; flag impossible terms |
| **SLO** | Engineering, product | Drive prioritization and alerts |

**Risk:** promising SLA metrics you cannot measure or meet with internal SLO + ops maturity.

## Alignment matrix

Maintain per product or per contract tier:

| Customer SLA metric | Internal SLI | Internal SLO | Buffer | Notes |
|---|---|---|---|---|
| 99.9% monthly uptime | `availability` LB metric | 99.95% / 30d | +0.05% | SLA uses calendar month |
| API p95 < 500ms | `latency_threshold` 500ms | 99% good / 30d | Stricter tail via SLO | SLA p95 ≠ SLO % good |
| Support response 1h | N/A (process) | IM SEV policy | — | `incident-management-engineer` |

**Rules:**

1. Every SLA metric maps to **one primary SLI** or explicit “non-SLO process”
2. Internal SLO **stricter** than SLA commitment unless executive risk acceptance
3. Document **measurement endpoint** (region, API version) for both sides

## Measurement gaps

Common mismatches to resolve before signing:

| Gap | SLA text risk | Engineering fix |
|---|---|---|
| SLA counts all HTTP codes | 4xx failures trigger credits | Exclude client errors in contract + SLI |
| SLA uses calendar month, SLO rolling 30d | Surprise breach on dashboard | Dual reporting or align windows |
| Global vs regional | EU-only customer, US incident | Regional SLO slice |
| Third-party status | “Platform up” includes vendor | Carve-out vendor + separate dependency SLO |
| Maintenance | Undefined window | Published maintenance policy + exclusion |

Provide **measurement appendix** to legal (`commercial-counsel`) with query definitions—not legal advice.

## Buffers and carve-outs

### Recommended buffers (starting points)

| SLA availability | Suggested internal SLO (rolling 30d) |
|---|---|
| 99.9% | 99.95% or higher |
| 99.95% | 99.99% |
| 99.5% | 99.9% |

Adjust for measurement error (synthetic vs real traffic, sampling).

### Standard carve-outs (engineering input)

- Scheduled maintenance (notice period per tier)
- Force majeure / provider outage (define provider list)
- Customer-caused issues (misconfiguration, quota)
- Beta/preview SKUs (no SLA or separate doc)
- DDoS / abuse beyond reasonable rate limits

Each carve-out must be **machine-enumerable** or **ticket-linked** for audit.

## Credits and remedies

Engineering supplies:

- **Breach detection** query matching contract definition
- **Monthly SLA report** raw data (redacted)
- **Incident timeline** IDs for disputed periods

Do not promise credit automation unless finance + legal approve.

| Credit tier | Typical trigger | Engineering data needed |
|---|---|---|
| 10% fee credit | <99.9% month | Monthly availability SLI |
| Escalating | Repeated quarters | Trend report |

## Communication

| Audience | Content | Cadence |
|---|---|---|
| Customer success | SLA status vs buffer | Monthly |
| Executives | Tier-0 burn summary | Weekly when >50% |
| Customers (external) | Status page, RCA | Per `incident-management-engineer` + `communication-lead` |

**Never** publish internal SLO targets as customer commitments without legal review.

## Legal handoff

Escalate to `commercial-counsel` when:

- SLA metric not measurable with current telemetry
- Credit triggers on metrics engineering disagrees with
- Unlimited liability or uncapped credits tied to availability
- SLA applies to dependencies outside your control without carve-out

This skill stops at **technical feasibility and measurement spec**; counsel owns contract language.
