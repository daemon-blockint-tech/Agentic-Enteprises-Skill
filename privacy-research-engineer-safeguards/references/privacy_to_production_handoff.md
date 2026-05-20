# Privacy handoff to production

## Table of contents

1. [Promotion criteria](#promotion-criteria)
2. [Deliverables](#deliverables)
3. [Monitoring in prod](#monitoring-in-prod)
4. [Incident triggers](#incident-triggers)

## Promotion criteria

Minimum before enabling new PII/redaction stack:

| Gate | Example |
|---|---|
| Benchmark | No regression on critical PII types at FP budget |
| Utility | Harm classifier delta within agreed bound |
| Leakage study | No canary regurgitation over threshold |
| Logging | Only approved fields enabled |
| Access | RBAC and encryption verified by infra |

Sign-off: privacy research + `ml-research-engineer-safeguards` if shared model + governance for high-risk tiers.

## Deliverables

Package for `ml-infrastructure-engineer-safeguards`:

- Detector version, threshold table per locale/type
- Redaction mode configuration
- **Prohibited** logging flags
- Runbook: false negative PII escalation
- Eval report JSON attached to release ticket

## Monitoring in prod

Ongoing metrics (aggregated):

- PII detector score distribution drift
- Manual sample audit rate (reviewer findings)
- Privacy-related tickets / escalations
- Failed redaction jobs

Alert on spike in **raw text** log volume — config regression.

## Incident triggers

Immediate review if:

- Suspected cross-tenant data in safety queue
- Bulk export of reviewer data
- Model outputs repeating unique user strings
- Public dataset release containing prompts

Route to `ai-lead-ops` incident process; preserve forensics per legal hold guidance.
