# Alert triage

## Table of contents

1. [Severity matrix](#severity-matrix)
2. [False positive handling](#false-positive-handling)
3. [Escalation](#escalation)

## Severity matrix

| Level | Indicators | Response |
|---|---|---|
| SEV1 | Active C2, ransomware, mass data exfil | Immediate IR; 24/7 |
| SEV2 | Confirmed account compromise, privilege escalation | < 1 hour; IR engaged |
| SEV3 | Suspicious activity, unconfirmed exploit | Same business day |
| SEV4 | Policy violation, recon | Queue; trend |

## False positive handling

Document:

- Detection ID and logic snippet
- Why benign (maintenance window, known tool, expected admin)
- Tuning change (threshold, allowlist scope, enrichment)
- Review date for allowlist expiry

Never global allowlist critical techniques without expiry and approver.

## Escalation

Escalate when: executive account involved, regulated data, lateral movement, unclear scope >10 hosts, or legal/comms required.
