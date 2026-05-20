# Security Operations and Software Development Security (Domains 7–8)

## Table of contents

1. [Security Operations (Domain 7)](#security-operations-domain-7)
2. [Software Development Security (Domain 8)](#software-development-security-domain-8)
3. [Operations vs development handoffs](#operations-vs-development-handoffs)

## Security Operations (Domain 7)

**Foundational capabilities** (program view):

| Capability | CISSP framing |
|---|---|
| Logging and monitoring | What to log, retention, correlation, alerting tiers |
| Incident management | Lifecycle: detection → analysis → containment → eradication → recovery → lessons learned |
| Forensics | Evidence integrity, chain of custody concepts—execution: specialists |
| Change management | Security impact of changes, emergency change controls |
| Configuration management | Baselines, drift detection |
| Patch management | Risk-based prioritization, maintenance windows |
| DR operations | Failover tests, backup verification |

**Investigation types**: Administrative (policy), civil, criminal—different evidence standards; coordinate with Legal.

**Malware response** (program): isolation, analysis decision, eradication, communication—technical steps belong to IR teams.

**Metrics** (examples): MTTD, MTTR, incident volume by category, patch SLA compliance, backup success rate.

**Do not conflate**: CISSP describes **what** the SOC/IR program must achieve; `soc-analyst` and `incident-responder` run shifts and playbooks.

## Software Development Security (Domain 8)

**Secure SDLC phases** (generic):

1. Requirements — security user stories, abuse cases
2. Design — threat modeling, security architecture review
3. Implementation — secure coding standards, secrets management
4. Verification — SAST, DAST, SCA, pen test
5. Release — signing, SBOM, deployment gates
6. Operations — monitoring, vulnerability response, deprecation

**Common vulnerability classes** (awareness level): injection, broken auth, sensitive data exposure, XXE, broken access control, misconfiguration, XSS, insecure deserialization, known vulnerable components, insufficient logging.

**Supply chain**: Third-party libraries, build pipeline integrity, artifact signing, dependency pinning—align with organizational SSDF / SAMM maturity goals.

**API and microservices**: Authentication, rate limiting, schema validation, service mesh identity—architecture detail: `enterprise-security-architect`.

**DevSecOps**: Shift-left testing, pipeline gates, developer training—automation: engineering and `compliance-engineer` for evidence.

## Operations vs development handoffs

| Situation | Lead skill |
|---|---|
| Production incident, containment | `incident-responder` |
| Alert triage and tuning | `soc-analyst`, `defensive-security-analyst` |
| App vuln remediation in sprint | Engineering + security champion |
| SDL policy and gate criteria | CISSP framing → standards → engineers implement |
| Audit of change management | `compliance-specialist` |

**Change advisory board (CAB)**: Security reviews emergency changes and high-risk deployments—CISSP defines criteria; operations enforces.
