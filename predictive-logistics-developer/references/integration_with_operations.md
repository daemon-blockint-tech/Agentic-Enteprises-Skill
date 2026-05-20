# Integration with operations

## Integration map

| System | Typical scores consumed | Cadence |
|---|---|---|
| OMS | Demand, promise dates | Intraday to daily |
| TMS | Lane volume, ETA, lead time | Hourly to daily |
| WMS | Replenishment targets, labor drivers | Daily |
| ERP / IBP | S&OP forecast feed | Weekly |
| Inventory optimization | Demand + lead-time distributions | Daily |

## Inference contract template

Document for each score:

| Field | Requirement |
|---|---|
| `entity_keys` | SKU, location, lane, node IDs—stable across systems |
| `as_of` | Forecast origin timestamp (UTC + business TZ) |
| `horizon` | Offset buckets (d+1 … d+n) |
| `point` | Point forecast |
| `p90` / intervals | Optional quantiles |
| `model_version` | Registry ID |
| `quality_flag` | OK, stale features, fallback used |

## Batch vs real-time

| Pattern | When | Risk |
|---|---|---|
| Batch tables | Planning, replenishment | Stale intraday events |
| Streaming features | ETA updates | Complexity, ordering |
| On-demand API | Promise date at cart | Latency SLOs |

Define **idempotent writes** and **partition keys** for backfills.

## Human-in-the-loop

- Expose **override reason codes** in planning UI; log for model feedback
- Never silently overwrite planner buffers without audit
- Provide **explainability snippets** (top drivers) for low-trust segments

## EDI and event alignment

- Use `edi-engineer` for **856/214/990** field semantics; consume status events as features only
- Normalize **status timestamps** to a single event timeline
- Handle **late postings** and **duplicate events** in feature pipelines

## Failure modes and degradation

| Failure | Degraded behavior |
|---|---|
| Feature pipeline delay | Serve last good score + `stale` flag |
| Cold-start SKU | Analog or family rollup forecast |
| Carrier outage | Bump lane variance; alert planning |
| Model version mismatch | Reject write; alert integration owner |

## Security and data boundaries

- No PII in feature stores unless required—aggregate ship-to where possible
- Separate **prod vs sandbox** score tables; prevent test writes to planning prod

## Release checklist

- [ ] Schema contract signed with WMS/TMS consumers
- [ ] Backtest attached for promotion window
- [ ] Monitoring dashboards and paging rules live
- [ ] Rollback version pinned in registry
- [ ] Runbook for fallback and manual override communicated to planning ops
