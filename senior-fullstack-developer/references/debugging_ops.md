# Production debugging

## Table of contents

1. [Triage order](#triage-order)
2. [Common causes](#common-causes)

## Triage order

1. Correlation ID across logs and traces
2. Deploy timeline vs error spike
3. Feature flags and config changes
4. Dependency health (DB, cache, third-party API)
5. Resource saturation (CPU, connections)

## Common causes

| Symptom | Check |
|---|---|
| 502/503 | Upstream timeout, pod restarts |
| Slow queries | Missing index, N+1 |
| Auth errors | Clock skew, expired keys, wrong env |
