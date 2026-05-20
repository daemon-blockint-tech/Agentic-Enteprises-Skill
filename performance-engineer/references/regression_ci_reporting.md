# Regression detection and reporting

## Table of contents

1. [Baselines](#baselines)
2. [CI performance gates](#ci-performance-gates)
3. [Release comparison](#release-comparison)
4. [Report template](#report-template)

## Baselines

Store per scenario:

- Git SHA, branch, date
- Environment (CPU, memory, region)
- Load profile (RPS, duration, mix)
- Metrics: p50/p95/p99, error rate, CPU, memory

Version baselines when **intentional** perf change ships; annotate in changelog.

## CI performance gates

| Gate type | Typical use |
|---|---|
| Micro-benchmark | Hot function, serializer |
| Integration perf test | API path with test DB |
| Build-size budget | Frontend bundle threshold |
| Smoke load | 5 min at 50% peak on RC |

Policies:

- **Fail PR** on regression > X% vs main (flake budget: rerun N times)
- Store trends in time-series for dashboards
- Separate **noisy** tests; quarantine with owner

Coordinate pipeline wiring with `devops`; own scenario and thresholds here.

## Release comparison

For each release candidate:

1. Run same harness as last green baseline
2. Diff percentiles and errors
3. Attribute to commits via bisect if needed
4. Block or waive with documented risk

Include **statistical caution** — small samples lie; require minimum request count.

## Report template

```markdown
## Summary
- Symptom / ticket:
- Environment:
- Verdict: improved | regressed | inconclusive

## Baseline vs experiment
| Metric | Baseline | Experiment | Δ |
| p99 latency | | | |
| Throughput | | | |
| Error rate | | | |

## Root cause
(Top 3 offenders with evidence — trace id, query, frame)

## Recommendations
1. [impact] …
2. …

## Reproduction
(steps, scripts, links)

## Risks / follow-ups
```

Share with engineering lead; link PRs for fixes. Escalate SLO breach to `incident-management-engineer` if production-impacting.
