---
name: performance-engineer
description: |
  Guides performance engineering—profiling (CPU, memory, I/O), distributed tracing, latency and
  throughput analysis, load/soak/stress testing, capacity models, performance budgets, database
  query tuning, and regression detection in CI.
  Use when investigating slow endpoints, p99 regressions, memory leaks, saturation, flaky load tests,
  defining latency SLOs, or producing optimization reports with evidence—not for CI/CD pipeline build
  (devops), rollout cutover strategy (deployment-strategist), warehouse dimensional modeling
  (data-warehouse-engineer), React/UI implementation (senior-frontend-software-engineer), facility
  compute utilization (data-center-compute-supply-efficiency), or LLM token/cost research
  (research-engineer-scientist-tokens).
---

# Performance Engineer

## When to Use

- **Profile** services under load — CPU, heap, goroutines, GC, lock contention
- **Trace** requests end-to-end — identify critical path and fan-out
- **Load test** — baseline, soak, stress, spike; interpret saturation and errors
- **Define budgets** — p50/p95/p99 targets, error budget, per-dependency ceilings
- **Tune** databases, caches, queues, and hot code paths with measured before/after
- **Detect regressions** — benchmark suites, CI gates, release comparisons
- **Model capacity** — headroom, scaling triggers, cost vs latency trade-offs
- **Report** findings — reproducible steps, flame graphs, ranked recommendations

## When NOT to Use

- Build or fix Jenkins/GitHub Actions pipelines → `devops`
- Canary/blue-green rollout plans → `deployment-strategist`
- Star schema, dbt layers, warehouse ELT design → `data-warehouse-engineer`, `analytics-data-engineer`
- Implement React components or a11y → `senior-frontend-software-engineer`
- General feature delivery without perf focus → `senior-software-engineer`
- DC power/cooling/rack utilization programs → `data-center-compute-supply-efficiency`
- LLM token benchmarks and compression research → `research-engineer-scientist-tokens`
- Enterprise architecture NFR sign-off only → `senior-system-architecture`

## Related skills

| Need | Skill |
|---|---|
| Implement fixes in application code | `senior-software-engineer` |
| SLO dashboards, alerting, on-call for deploy | `devops` |
| Core Web Vitals in product UI code | `senior-frontend-software-engineer` |
| Warehouse SQL and partition design | `data-warehouse-engineer` |
| Cross-service latency budgets in ADRs | `senior-system-architecture` |
| Data pipeline SLA and batch windows | `data-system-ops-lead` |
| GPU/cluster capacity for training | `data-center-compute-supply-efficiency` |
| Token/cost efficiency experiments | `research-engineer-scientist-tokens` |

## Core Workflows

### 1. Profiling and diagnostics

CPU, memory, I/O, contention.

**See `references/profiling_diagnostics.md`.**

### 2. Load and capacity testing

Scenarios, harness, interpretation.

**See `references/load_capacity_testing.md`.**

### 3. Latency, throughput, and SLOs

Percentiles, budgets, error budget.

**See `references/latency_slo_budgets.md`.**

### 4. Database and data-path tuning

Queries, indexes, caches.

**See `references/database_query_performance.md`.**

### 5. Frontend and client runtime

CWV, network, rendering.

**See `references/frontend_runtime_performance.md`.**

### 6. Regression detection and reporting

Baselines, CI, executive summary.

**See `references/regression_ci_reporting.md`.**

## Outputs

- **Perf investigation brief** — symptom, scope, hypothesis, reproduction
- **Trace + profile pack** — flame graph, span waterfall, top offenders
- **Load test plan and results** — scenario matrix, graphs, bottlenecks
- **Optimization backlog** — ranked by impact × effort with measurements
- **SLO proposal** — targets, measurement points, alert thresholds
- **Regression report** — build-over-build comparison with root cause

## Principles

- **Measure first** — no optimization without baseline and success metric
- **One variable** — isolate changes; document environment (hardware, data size, version)
- **User-centric metrics** — tail latency and error rate over averages
- **Saturation-aware** — distinguish queueing from inefficient work
- **Reproducible** — scripts, seeds, and configs checked in or attached to report
