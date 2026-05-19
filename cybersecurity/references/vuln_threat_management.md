# Vulnerability and threat management

## Table of contents

1. [Patch SLAs](#patch-slas)
2. [Pentest scope](#pentest-scope)
3. [Threat intel](#threat-intel)

## Patch SLAs

| Severity | Target |
|---|---|
| Critical | 48h |
| High | 7d |
| Medium | 30d |
| Low | 90d |

Adjust for compensating controls and exposure.

## Pentest scope

Include: external attack surface, auth flows, major APIs, admin interfaces.

Exclude without approval: social engineering, destructive tests on prod.

Deliverables: executive summary, finding list, retest window.

## Threat intel

Use feeds for IOC blocking; map TTPs to MITRE ATT&CK for detection gaps.
