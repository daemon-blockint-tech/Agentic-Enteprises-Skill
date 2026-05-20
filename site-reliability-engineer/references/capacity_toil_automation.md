# Capacity, toil, and automation

## Table of contents

1. [Capacity planning](#capacity-planning)
2. [Toil definition and measurement](#toil-definition-and-measurement)
3. [Automation priorities](#automation-priorities)
4. [Dependency and blast radius](#dependency-and-blast-radius)

## Capacity planning

Inputs:

- Traffic forecast (seasonal, launch, marketing events)
- Per-request **resource cost** (CPU-ms, DB queries, egress)
- **Headroom target** (e.g., 30% at p99 peak before scale)
- **Failure scenarios** — AZ loss, dependency slow (2× latency)

Outputs:

- Scale triggers (HPA, queue consumers, DB read replicas)
- **Quota** requests before limits block (`cloud-system-administrator`)
- Cost vs reliability trade documented for product

Revisit quarterly or after major architecture change.

## Toil definition and measurement

**Toil** = manual, repetitive, automatable work that scales with service growth.

Track weekly per team:

- Hours on toil vs project work
- Top toil tasks (ticket tags)
- Toil **eliminated** last quarter

Cap: if toil >50% of ops time, pause new features until automation lands.

## Automation priorities

Score candidates:

| Factor | Weight |
|---|---|
| Frequency | High |
| Customer/SLO risk if wrong | High |
| Time saved per month | Medium |
| Implementation cost | Medium |

Prefer: auto-remediation for known failures, self-service dashboards, safe runbook bots with guardrails.

Do not automate untested destructive actions without approval gates.

## Dependency and blast radius

Maintain service graph:

- Sync and async callers/callees
- Shared infrastructure (DB, cache, queue, identity)
- **Critical path** for top user journeys

For each dependency document:

- Timeout and retry policy
- Fallback behavior
- **Failure mode** (fail open vs closed — explicit choice)

Use graph to prioritize incident drills and chaos experiments in `release_reliability_chaos.md`.
