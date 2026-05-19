# Control hardening

## Table of contents

1. [Baseline sources](#baseline-sources)
2. [Cloud guardrails](#cloud-guardrails)
3. [Validation](#validation)

## Baseline sources

| Framework | Use for |
|---|---|
| CIS Benchmarks | OS, cloud, K8s hardening |
| NIST 800-53 (selected) | Control mapping for regulated envs |
| Vendor well-architected security pillar | Cloud-native defaults |

Encode baselines in IaC (Terraform, CloudFormation) or policy-as-code (OPA, Kyverno, SCPs).

## Cloud guardrails

Examples (adapt per org):

- Deny public S3 buckets and open security groups by default
- Require encryption on new storage
- Restrict region and instance types via SCP
- Centralize logging to security account
- Enforce IMDSv2, disable legacy auth where possible

## Validation

- Automated compliance scan (e.g., Prowler, Security Hub) on schedule
- Drift detection on IaC
- Sample manual check quarterly for net-new services

Document exceptions: owner, risk acceptance, expiry date.
