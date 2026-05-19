# Platform selection

## Table of contents

1. [Evaluation criteria](#evaluation-criteria)
2. [Deployment models](#deployment-models)
3. [Scoring matrix](#scoring-matrix)
4. [Procurement notes](#procurement-notes)

## Evaluation criteria

| Criterion | Weight | Questions |
|---|---|---|
| Data handling | High | Training opt-out, residency, BAAs |
| Models | High | Needed capabilities (vision, long context, tools) |
| Private access | High | VPC/private link, no public internet |
| Operations | Med | SLAs, quotas, rate limits, support tier |
| Cost | Med | Token $, committed use, egress |
| Lock-in | Med | Portable APIs (OpenAI-compatible?), export |
| Compliance | High | SOC 2, ISO 27001, FedRAMP if needed |

## Deployment models

| Model | Description | When |
|---|---|---|
| **SaaS API** | Vendor-hosted inference | Fastest start; accept data egress |
| **Private endpoint** | Same API in your VPC | Enterprise default |
| **Dedicated / single-tenant** | Isolated capacity | Regulated or large EA |
| **Self-hosted open weights** | You operate GPUs | Extreme residency; high ops burden |

## Scoring matrix

```markdown
| Option | Data | Models | Private | Ops | Cost | Compliance | Total |
|---|---|---|---|---|---|---|
| A | 4 | 5 | 3 | 4 | 3 | 5 | |
| B | 5 | 4 | 5 | 3 | 2 | 5 | |
```

Record **rejected** options and **exit plan** (e.g., abstraction layer, dual-write embeddings).

## Procurement notes

- Separate **inference** from **support** SLAs
- Cap liability and subprocessors in `commercial-counsel` review
- Enterprise Agreement vs pay-as-you-go for forecasting (`ai-lead-ops`)
- Pilot credits and production commit phasing

Do not sign architecture to a single model version without pin and rollback strategy.
