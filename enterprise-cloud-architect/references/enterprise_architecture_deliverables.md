# Enterprise architecture deliverables

## Table of contents

1. [Steering pack](#steering-pack)
2. [Migration portfolio](#migration-portfolio)
3. [Standards publication](#standards-publication)
4. [Relationship to cloud-architect](#relationship-to-cloud-architect)

## Steering pack

Executive summary (5–10 slides max):

1. **Posture** — spend, risk, migration progress vs plan
2. **EA/commit** — utilization, forecast, true-up exposure
3. **Incidents/themes** — security, outages, policy violations
4. **Decisions needed** — funding, exceptions, region expansion
5. **Next quarter** — standards changes, major migrations

Quantify in **dollars and risk**, not service names alone.

## Migration portfolio

Enterprise view across BUs:

| Wave | Apps | Strategy (7R) | Dependency | Risk | Owner |
|---|---|---|---|---|---|

Prioritize by **value, risk, readiness**; capacity in landing zone and network.

Wave execution detail → `cloud-architect` per application; program office → `technical-program-manager`.

## Standards publication

Publish via:

- Internal architecture portal (versioned)
- IaC module registry with compliance badges
- Training for new account owners

**Deprecation:** notice period, automated policy warnings, enforcement date.

## Relationship to cloud-architect

| Scope | Skill |
|---|---|
| Enterprise guardrails, EA, ARB, multi-BU | `enterprise-cloud-architect` |
| Application reference architecture, WAF, single migration | `cloud-architect` |
| Resource configuration | `cloud-engineer` |

When a BU asks for architecture inside approved standards, route to **cloud-architect** with enterprise catalog as constraint.
