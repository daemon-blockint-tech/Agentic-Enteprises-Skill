# Optimization and rightsizing

## Table of contents

1. [Waste categories](#waste-categories)
2. [Rightsizing process](#rightsizing-process)
3. [Commitments](#commitments)
4. [Architecture levers](#architecture-levers)

## Waste categories

| Category | Examples | Typical action |
|---|---|---|
| Idle compute | Stopped-but-billed, zero-traffic instances | Stop or terminate |
| Storage | Unattached EBS, old snapshots, incomplete MPU | Delete after snapshot policy |
| Network | Unused EIPs, NAT for dev sandboxes | Release, consolidate |
| Over-SKU | CPU <10% for 14d | Downsize instance family |
| Orphaned | LB with no targets, empty ASG | Remove |
| Non-prod drift | Prod-sized staging | Rightsize or schedule off-hours |

Use native **recommendation engines** (Compute Optimizer, Advisor) as input, not sole truth.

## Rightsizing process

1. **Identify** candidate from metrics (CPU, memory, network, IOPS)
2. **Validate** with owner — batch jobs, peak windows, launch coming
3. **Schedule** change in maintenance window if prod
4. **Measure** 7d post-change for latency/errors
5. **Record** savings in optimization log

Never rightsizing without owner ack on stateful prod.

## Commitments

Decision flow:

1. **30–60 days** stable hourly usage pattern
2. Calculate **on-demand vs RI/SP/CUD** break-even
3. Choose **term** (1y vs 3y) vs flexibility risk
4. Target **coverage** (e.g., 70–80% of steady baseline; not 100% on volatile)
5. Track **utilization** monthly; sell or exchange if provider allows

Enterprise EA and payer-level commits → `enterprise-cloud-architect`.

## Architecture levers

Engage `cloud-architect` / service teams for larger wins:

- Graviton/ARM migration
- Serverless vs always-on
- S3 lifecycle and storage class
- Cross-AZ traffic reduction
- Caching to cut data egress
- Regional consolidation for residency + cost

Document **reliability impact** before architecture-driven cuts.
