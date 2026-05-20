# Continuous cloud monitoring

## Table of contents

1. [CCM architecture](#ccm-architecture)
2. [Rule baselines](#rule-baselines)
3. [Exceptions](#exceptions)
4. [Metrics for leadership](#metrics-for-leadership)

## CCM architecture

```
cloud APIs / Config / CSPM → rules engine → findings → ticket → remediate → re-test
```

Integrate with `cloud-security-engineer` for rule implementation and `compliance-engineer` for control ID mapping.

Org-wide:

- **Delegated admin** security account for centralized findings
- **Suppress** only with documented exception
- **Route** critical findings to SLA-based remediation

## Rule baselines

Align rules to frameworks:

| Risk | Example rules |
|---|---|
| Public data | S3/Blob public access, open SG to 0.0.0.0/0 |
| Identity | Root MFA, access key age, overly permissive policies |
| Logging | CloudTrail disabled, flow logs off |
| Encryption | Unencrypted volumes, buckets without SSE |
| Governance | Unauthorized regions, unapproved services |

Map each rule to **SOC/ISO control ID** for auditor traceability.

## Exceptions

Exception register fields:

- Control/rule ID
- Resource ARN and justification
- Compensating control
- Approver and **expiry date**
- Re-review trigger

Expired exceptions fail CCM dashboard; no silent renewals.

## Metrics for leadership

Weekly/monthly:

- % accounts passing critical rules
- Mean time to remediate by severity
- Open exceptions by age
- Trend vs prior observation period

Use for pre-audit readiness—not as sole security KPI (`cybersecurity` program metrics separate).
