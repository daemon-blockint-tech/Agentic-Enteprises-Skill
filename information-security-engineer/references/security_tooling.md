# Security tooling integration

## Table of contents

1. [Logging pipeline](#logging-pipeline)
2. [EDR](#edr)
3. [SOAR](#soar)

## Logging pipeline

```
source → collector/agent → normalize → SIEM index → detections → ticket/SOAR
```

- Standardize timestamps (UTC), host, user, action, outcome
- Retention per compliance tier (hot/warm/cold)
- Integrity: restrict who can delete indexes; separate admin roles

## EDR

- Deploy to servers and workstations per policy
- Tamper protection enabled
- Test isolation API in non-prod before IR use
- Export telemetry to SIEM for correlation

## SOAR

- Automate only low-risk actions (enrichment, ticketing)
- Human approval for containment in production
- Version playbooks; test against recorded alerts
- Rate-limit API calls to avoid vendor lockout
