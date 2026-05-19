# Threat modeling

## Table of contents

1. [When to model](#when-to-model)
2. [STRIDE cheat sheet](#stride-cheat-sheet)
3. [Lightweight template](#lightweight-template)
4. [Abuse cases](#abuse-cases)
5. [Review cadence](#review-cadence)

## When to model

| Change | Depth |
|---|---|
| New external API or webhook | Lightweight STRIDE |
| AuthN/AuthZ model change | Full data-flow + STRIDE |
| Multi-tenant feature | Isolation + IDOR focus |
| Payment or PII processing | Full + compliance review |
| CI/CD or IaC privilege change | Pipeline abuse cases |
| AI/LLM in user path | Prompt injection + tool abuse |

## STRIDE cheat sheet

| Threat | Question | Example mitigations |
|---|---|---|
| Spoofing | Can an actor pretend to be someone else? | MFA, mTLS, signed tokens |
| Tampering | Can data in transit/at rest be altered? | TLS, signatures, immutable logs |
| Repudiation | Can actions be denied? | Audit logs, WORM storage |
| Information disclosure | Can data leak? | Encryption, RBAC, redaction |
| Denial of service | Can availability be killed? | Rate limits, autoscale, WAF |
| Elevation of privilege | Can a user become admin? | Least privilege, authz tests |

## Lightweight template

```markdown
# Threat model: [Feature]

## Context
- Actors: [user, admin, partner, anonymous]
- Assets: [data stores, keys, revenue]
- Trust boundaries: [browser→API, API→DB, CI→cloud]

## Data flow
[Diagram or numbered steps]

## Threats
| ID | STRIDE | Threat | Mitigation | Status |
|----|--------|--------|------------|--------|
| T1 | I | ... | ... | Open/Done/Waived |

## Accepted risks
| ID | Rationale | Approver | Review date |
```

## Abuse cases

Write as: **Given** [precondition] **When** [action] **Then** [impact].

Examples:

- User A changes `{id}` in URL to access User B's record (IDOR)
- Attacker replays webhook without signature verification
- Compromised CI secret deploys malicious image to production
- LLM tool call exfiltrates env var via crafted user message

Map each abuse case to a test (unit, integration, or security test) or monitoring alert.

## Review cadence

| Artifact | Cadence |
|---|---|
| Lightweight model | Each epic with security touchpoint |
| Full model | Major release or annual for critical systems |
| Waived risks | Revalidate before expiry |
| Post-incident | Update model within 2 weeks of P1/P2 security incident |
