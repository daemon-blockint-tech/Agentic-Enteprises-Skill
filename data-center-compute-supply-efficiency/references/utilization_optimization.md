# Utilization and Optimization

## Identify candidates

| Signal | Typical action |
|---|---|
| Avg CPU < 15% for 30d (non-prod) | Consolidate or power off |
| GPU idle > 50% scheduled window | Reschedule or share pool |
| Single-tenant host, low load | Move to shared cluster |
| Oversized RAM vs working set | Right-size VM or host |
| Powered, no workload | Decommission or reassign |

Always **exclude** hosts with:

- HA pairs where split would violate policy
- Latency-sensitive dedicated inference
- Regulatory isolation requirements

## Consolidation workflow

1. **Inventory** — CMDB + monitoring + owner tag
2. **Classify** — prod / staging / lab / unknown
3. **Model target** — destination host or cluster capacity
4. **Test** — load test or canary migration
5. **Migrate** — maintenance window, rollback plan
6. **Verify** — SLO, power draw, license compliance
7. **Decomm or repurpose** — free kW and U

## Virtualization and containers

- **VM density** — vCPU:pCPU ratios; avoid extreme oversubscription on latency workloads
- **K8s** — requests/limits vs node allocatable; bin-packing efficiency
- **Bare metal** — often lowest utilization; justify with performance or compliance

Coordinate implementation with `cluster-deployment-engineer` or virtualization admins.

## Scheduling for efficiency (DC-aware)

- Batch jobs in off-peak power windows (if tariff or PUE varies)
- GPU time-slicing or MIG where applicable
- Queue training jobs to fill idle accelerators

## Risk controls

| Risk | Mitigation |
|---|---|
| Noisy neighbor after consolidate | Separate pools or quotas |
| Single point of failure | Maintain N+1 at service level |
| Migration failure | Snapshot, rollback runbook |
| License violation | Audit per-socket / per-core terms |

## Success metrics

- kW reclaimed
- Racks deferred (capex avoidance)
- Utilization p50/p95 improved
- No increase in incident rate post-change
