# Observability and SRE

## Table of contents

1. [SLI examples](#sli-examples)
2. [Alerting rules](#alerting-rules)
3. [Dashboards](#dashboards)

## SLI examples

| Service type | SLI | Target example |
|---|---|---|
| HTTP API | Availability, p95 latency | 99.9%, < 300ms |
| Worker | Job success rate | 99.5% |
| Pipeline | Success per schedule | 99% |

## Alerting rules

- Page on user-visible SLO burn (multi-window)
- Ticket on non-urgent threshold breaches
- Suppress alerts during planned maintenance

## Dashboards

- Golden signals per service
- Deploy annotations correlated with error rate
- Cost dashboard for top spenders (optional)
