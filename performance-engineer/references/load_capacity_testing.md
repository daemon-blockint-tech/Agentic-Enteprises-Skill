# Load and capacity testing

## Table of contents

1. [Test types](#test-types)
2. [Scenario design](#scenario-design)
3. [Harness requirements](#harness-requirements)
4. [Interpreting results](#interpreting-results)
5. [Capacity model](#capacity-model)

## Test types

| Type | Goal | Duration |
|---|---|---|
| Smoke | Script works, SLO not violated at min load | Minutes |
| Load | Steady expected peak + headroom | 30–60 min |
| Soak | Leaks, drift, disk fill | Hours–days |
| Stress | Find breaking point | Until failure |
| Spike | Sudden 2–10× traffic | Short burst |
| Breakpoint | Ramp until errors or SLA breach | One-way ramp |

Always define **success criteria** before running (max error rate, p99 ceiling).

## Scenario design

Model **realistic mix**:

- Read/write ratio, auth vs anonymous, heavy vs light endpoints
- Think time if mimicking users; zero think time for API soak
- **Seed data** size matching prod order of magnitude (not empty DB)
- Idempotent writes or isolated test tenants

Avoid testing only health checks — include business-critical paths.

## Harness requirements

- Distributed workers if single client cannot generate load
- **Warm-up** phase excluded from metrics
- Capture: RPS, latency histogram, errors by class, saturation (CPU, pool wait)
- Store **artifacts**: config, git SHA, env vars (redacted), result files
- Integrate with CI for smoke/load on release candidates

Tools vary by stack — skill is tool-agnostic; document chosen tool and version.

## Interpreting results

| Signal | Likely cause |
|---|---|
| Latency rises, errors flat | Queueing, pool exhaustion |
| Errors rise first | Timeouts, circuit open, DB max connections |
| CPU low, latency high | Blocking I/O, lock, external dependency |
| CPU high, latency high | Inefficient compute, hot loop |
| Recovery slow after spike | Autoscale lag, cache cold, connection rebuild |

Do not extrapolate linearly past knee of curve — document **max sustainable RPS**.

## Capacity model

```
headroom = (max_sustainable_rps - current_peak_rps) / max_sustainable_rps
```

Include:

- Per-service and per-dependency limits
- Autoscale rules and minimum instances
- Cost per 1k requests at target utilization
- Time to scale out vs spike duration

Hand off infra scaling changes to `devops` / `infrastructure-engineer` with evidence.
