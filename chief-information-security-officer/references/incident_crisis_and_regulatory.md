# Incident, crisis, and regulatory

## Table of contents

1. [Escalation matrix](#escalation-matrix)
2. [CISO role in crisis](#ciso-role-in-crisis)
3. [Crisis communications](#crisis-communications)
4. [Regulatory and audit exec](#regulatory-and-audit-exec)

## Escalation matrix

Define severity with **business impact**, not technical detail:

| Severity | Examples | CISO involvement |
|---|---|---|
| SEV-1 | Customer data breach, ransomware production halt, regulatory trigger | Lead exec war room; board notification path |
| SEV-2 | Limited data exposure, major control failure | Approve comms and external counsel; brief CEO |
| SEV-3 | Contained malware, single-system compromise | Monitor; delegate to `incident-responder` |
| SEV-4 | Policy violations, low-impact events | Dashboard only |

Technical execution stays with `incident-responder`, `digital-forensics-analyst`, and SOC partners.

## CISO role in crisis

**First 24 hours:**

1. Confirm facts vs assumptions; single incident commander (often IR lead)
2. Activate crisis roster — Legal, PR/comms, HR, business owner
3. Preserve evidence chain; approve containment that affects customers
4. Start regulatory clock assessment with Legal
5. Brief CEO; prepare board notification if material

**After stabilization:**

- Root cause and systemic fix themes (not blame)
- Control and investment implications for program roadmap
- Lessons for tabletop and appetite review

## Crisis communications

| Audience | Owner | CISO input |
|---|---|---|
| Employees | HR / Comms | Facts, safe behaviors, phishing watch |
| Customers | Comms + Legal | Breach scope, remediation, support channel |
| Regulators | Legal | Notification content, timing |
| Media | Comms | Approved messaging only |
| Board | CISO + CEO | Materiality, timeline, systemic fixes |

Use `communication-lead` for drafts; CISO validates technical accuracy. **No speculative attribution** in external statements.

## Regulatory and audit exec

| Activity | CISO role | Delegate |
|---|---|---|
| Supervisory exam | Exec sponsor; theme prep | `compliance-specialist` packs |
| Audit committee | Present findings and management responses | Internal audit liaison |
| Customer security questionnaires | Policy on tier-1 responses | GRC + engineering SMEs |
| Breach notification | Decision support with Legal | IR evidence |

Track **repeat findings** as program failures—fund systemic fixes in next budget cycle, not point remediations only.
