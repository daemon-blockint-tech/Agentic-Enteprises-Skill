# Business impact and criticality

## Table of contents

1. [BIA objectives](#bia-objectives)
2. [Process and service inventory](#process-and-service-inventory)
3. [Impact dimensions](#impact-dimensions)
4. [Dependency mapping](#dependency-mapping)
5. [Tiering model](#tiering-model)
6. [Workarounds](#workarounds)
7. [BIA outputs](#bia-outputs)

## BIA objectives

Produce a **defensible criticality ranking** for security and IT services that drives RTO/RPO, backup scope, and exercise priority. Focus on:

- **Security outcomes** — authentication, authorization, detection, response, evidence retention
- **Regulatory and contractual** — logging retention, breach investigation capability, access control
- **Operational coupling** — what breaks if IdP, SIEM, or EDR is unavailable for 4h vs 24h

Do not treat all SaaS as tier-0; justify tiers with impact evidence.

## Process and service inventory

Capture each item in a single register:

| Field | Guidance |
|---|---|
| Service name | Product + environment (prod IdP, corp SIEM) |
| Owner | Business + technical |
| Users / consumers | Employees, SOC, apps, regulators |
| Data classes | Credentials, logs, keys, PII in scope |
| Peak usage | Login waves, month-end, release windows |
| RTO/RPO (draft) | From impact interview; refine in RTO doc |

**Security-critical examples:** IdP/MFA, PAM, KMS/HSM, SIEM, log archive, EDR, SOAR, email security gateway, CASB, secrets manager, certificate authority, vulnerability scanner, GRC tool storing control evidence.

## Impact dimensions

Score each service **1–5** per dimension at defined outage durations (e.g., 1h, 4h, 24h, 72h):

| Dimension | Questions |
|---|---|
| Safety / life | Any operational technology or safety system dependency? |
| Financial | Revenue stop, fraud exposure, penalty risk? |
| Legal / regulatory | Inability to investigate, report, or prove controls? |
| Reputational | Customer trust, media, partner churn? |
| Security posture | Blind spots, inability to contain spread, credential risk? |
| Operational | Engineering halt, support paralysis, manual work explosion? |

**Security-specific:** prolonged loss of **logging or IdP** often escalates impact non-linearly—document compound effects (cannot investigate while attackers remain active).

## Dependency mapping

For each tier candidate, diagram:

1. **Upstream** — IdP, DNS, network, hypervisor, SaaS status page
2. **Downstream** — apps, SOC workflows, automation that fails closed or open
3. **Shared fate** — single region, single admin account, single backup controller
4. **External** — identity federation, MSP SOC, cloud control plane

Flag **single points of failure** and **circular dependencies** (e.g., MFA via system that requires MFA to administer).

## Tiering model

| Tier | Typical MTPD | Examples | Recovery priority |
|---|---|---|---|
| 0 | < 1 h | IdP prod, corp MFA, break-glass path | Immediate; pre-staged runbooks |
| 1 | < 4 h | SIEM hot path, EDR management, KMS | Same day; comms to leadership |
| 2 | < 24 h | SOAR, secondary regions, warm log archive | Next business day |
| 3 | < 72 h | GRC, training LMS, non-prod security sandboxes | Scheduled recovery |
| 4 | > 72 h | Dev/test security tools | Best effort |

Assign tier from **highest** impact dimension at MTPD threshold. Document **risk acceptance** when tier and budget disagree.

## Workarounds

Define **manual or degraded modes** before disaster:

| Service | Workaround | Limitations | Max duration |
|---|---|---|---|
| IdP | Break-glass local accounts | Audit burden, no SSO | Hours only |
| SIEM | Store-and-forward / alternate sink | Reduced correlation | Days with risk acceptance |
| EDR | Isolation via network ACL | No central console | Incident-specific |
| MFA | Hardware token backup, SMS (if policy allows) | Weaker factor | Emergency only |

Workarounds require **pre-approval** in policy and **tabletop validation**.

## BIA outputs

Deliver:

1. **Criticality register** (CSV or GRC tool) — all fields above, versioned
2. **Dependency diagram** — tier-0/1 subgraph
3. **Gap list** — missing workarounds, unknown owners, untested dependencies
4. **Recommendations** — RTO/RPO proposals, backup scope changes, exercise priorities

Route tier-0 gaps with **due dates** to `information-security-engineer` or platform owners; track in BCM action register.
