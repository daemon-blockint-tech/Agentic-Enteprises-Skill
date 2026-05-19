# Encryption and secrets

## Table of contents

1. [Key management](#key-management)
2. [TLS](#tls)
3. [Secrets handling](#secrets-handling)

## Key management

- Customer-managed keys (CMK) for regulated data when required
- Key policies: least privilege; separate admin vs usage roles
- Enable key rotation and CloudTrail/KMS audit logs
- Document data classification → key tier mapping

## TLS

- TLS 1.2 minimum; prefer 1.3
- Automate cert renewal (ACME or internal CA)
- HSTS on public web; strong cipher suites
- Monitor cert expiry 30/14/7 days before

## Secrets handling

- Central secret store; no secrets in git or images
- Rotation on schedule and on compromise
- Pre-commit and CI secret scanning
- Inject at runtime via sidecar or platform secret mount
