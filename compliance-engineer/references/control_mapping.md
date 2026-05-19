# Control mapping

## Table of contents

1. [Mapping template](#mapping-template)
2. [Example mappings](#example-mappings)

## Mapping template

| Control ID | Requirement summary | Policy/process | Technical implementation | Evidence source | Owner | Frequency |
|---|---|---|---|---|---|---|

## Example mappings

| Control theme | Technical implementation | Evidence |
|---|---|---|
| Logical access | SSO + MFA; RBAC in app | IdP config export, sample user list |
| Change management | PR approval + CI deploy log | GitHub audit log, deployment history |
| Encryption | TLS + KMS at rest | Config screenshots, KMS policy |
| Logging | Central SIEM 90d retention | Retention policy, sample alert |
| Vulnerability mgmt | Weekly scan + SLA | Scanner report, closed tickets |

Map one control to multiple evidence items when auditors expect corroboration.
