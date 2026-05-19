# Continuous monitoring

## Table of contents

1. [CCM metrics](#ccm-metrics)
2. [Drift examples](#drift-examples)
3. [Alert routing](#alert-routing)

## CCM metrics

Track pass rate per control family:

- % users with MFA
- % repos with required branch protection
- % critical vulns within SLA
- % production resources with required tags/encryption

## Drift examples

| Drift | Detection |
|---|---|
| Public S3 bucket | CSPM rule |
| Admin without MFA | IdP report |
| Open security group | Config rule |
| Expired exception | Exception registry job |

## Alert routing

- Engineering owner for technical drift
- Compliance owner for evidence miss
- Escalate repeated failures to security leadership
