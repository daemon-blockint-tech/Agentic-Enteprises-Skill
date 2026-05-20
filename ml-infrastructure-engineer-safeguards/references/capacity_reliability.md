# Capacity and reliability

## Table of contents

1. [Resource planning](#resource-planning)
2. [Degradation modes](#degradation-modes)
3. [Multi-region](#multi-region)
4. [Dependencies](#dependencies)

## Resource planning

Estimate:

```
peak_qps × (tokens_in + tokens_out) × safety_multiplier
```

`safety_multiplier` accounts for extra model calls on pre/post path.

GPU:

- Model size → VRAM per replica
- Concurrent sessions vs batching
- Reserve **headroom** for traffic spikes and deploy surge

CPU classifiers: separate pool from GPU LLM to avoid starvation.

Align long-term GPU supply with `data-center-compute-supply-efficiency` when facility-bound.

## Degradation modes

Ordered fallback (define per product tier):

1. Stricter rate limits
2. Smaller/cheaper model with **same** safeguard stack
3. Queue with timeout message
4. Read-only / cached responses where applicable
5. **No** unguarded LLM shortcut unless explicit break-glass with audit

Break-glass: dual control, time-limited flag, post-incident review.

## Multi-region

- Policy and model versions **consistent** or explicitly documented per region
- Failover: DNS/anycast to healthy region; watch data residency
- Replicate classifier models; avoid cross-border PII for review queues

DR test: safety path included in game days, not model-only.

## Dependencies

| Dependency | Risk |
|---|---|
| Vendor moderation API | Quota, latency, ToS change |
| Vendor LLM | Outage, content policy change |
| Config service | Stale policy, split brain |
| GPU node pool | Preemption, driver, CUDA mismatch |

Maintain **synthetic probes** every minute through full path.

Performance tuning of hot paths → `performance-engineer`; own safeguard-specific SLOs here.
