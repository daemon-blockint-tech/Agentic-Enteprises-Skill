# Secure cloud architecture review

## Table of contents

1. [Review triggers](#review-triggers)
2. [Checklist](#checklist)
3. [Common misconfigurations](#common-misconfigurations)
4. [Remediation prioritization](#remediation-prioritization)

## Review triggers

Run review before:

- New workload landing in prod account
- Internet-exposed service launch
- Cross-account trust or peering
- Handling regulated or PII data
- Major migration wave (`cloud-architect` coordinates)

## Checklist

| Area | Verify |
|---|---|
| Identity | Least privilege; no long-lived keys; federation |
| Network | Segmentation; no public DB; private endpoints |
| Data | Encryption at rest/transit; backup encrypted |
| Logging | Audit on; flows enabled; central retention |
| Resilience | Not a security substitute — align with `site-reliability-engineer` for availability |
| Supply chain | Signed images; private registry (`devsecops`) |
| Admin | No console on prod data plane; break-glass only |

Pair with **Well-Architected Security** pillar and threat model for critical systems.

## Common misconfigurations

| Finding | Typical fix |
|---|---|
| Public S3/GCS/Blob | Block public access org-wide; fix ACLs |
| Open security group | Restrict source; use bastion-less admin |
| Overprivileged role | Split roles; permission boundary |
| Unencrypted volume | Enable default encryption; re-encrypt |
| CloudTrail off | Enable org trail; alert on disable |
| IMDSv1 | Require IMDSv2 |
| Wildcard trust policy | Scope account IDs + external ID |
| Keys in git | Rotate; secrets manager; scan in CI |

Validate fixes with Config rule or rescan — not only console spot check.

## Remediation prioritization

| Priority | Criteria |
|---|---|
| P0 | Exploitable internet exposure of data or admin |
| P1 | Credential risk, broad IAM, missing audit |
| P2 | Encryption gap on non-public data |
| P3 | Hardening drift, low-risk hygiene |

Document **compensating controls** for accepted risk: owner, expiry, detection in place.

Pentest validation of fixes → `offensive-security-analyst`.
