# Logging, CSPM, and detection

## Table of contents

1. [Audit logging](#audit-logging)
2. [Posture management](#posture-management)
3. [Native threat detection](#native-threat-detection)
4. [SIEM integration](#siem-integration)

## Audit logging

Org-wide mandatory:

| Provider | Control |
|---|---|
| AWS | CloudTrail org trail, all regions, log file validation, S3 + KMS |
| GCP | Admin Activity + Data Access (where policy allows), sinks to central bucket |
| Azure | Activity Log to Log Analytics / storage; diagnostic settings on resources |

Protect logs:

- **Immutable** storage; separate audit account
- Alert on trail disable, policy change, root login
- Retention meets legal and `compliance-engineer` requirements

## Posture management

CSPM / native posture tools:

- AWS **Security Hub** + **Config** rules (CIS conformance packs)
- GCP **Security Command Center**
- Azure **Defender for Cloud** + regulatory compliance dashboard

Workflow:

1. Enable org-wide with delegated admin account
2. Baseline rules — fail on critical misconfigs (public S3, open SG, no MFA on root)
3. Route findings to ticketing; SLA by severity
4. Track **mean time to remediate**; exception register with expiry

## Native threat detection

Enable and tune:

- GuardDuty / Defender for Cloud / SCC threat detectors
- VPC Flow–based anomaly where available
- Integrate with SOAR playbooks (`defensive-security-analyst` for alert handling)

Tune suppressions carefully; document false positives.

## SIEM integration

Forward to corporate SIEM (`information-security-engineer`):

- Normalize fields (account, region, principal, resource ARN)
- High-value detections: IAM policy change, SG open to world, KMS disable, snapshot public
- Correlate with IdP sign-in and EDR where available

Cloud-security-engineer owns **cloud log pipeline** quality; SOC owns **detection logic** and response tiers.
