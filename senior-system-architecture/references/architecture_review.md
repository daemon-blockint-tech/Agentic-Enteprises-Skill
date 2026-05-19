# Architecture review

## Table of contents

1. [Review types](#review-types)
2. [Pre-read package](#pre-read-package)
3. [Checklist](#checklist)
4. [Outcomes](#outcomes)

## Review types

| Type | When | Depth |
|---|---|---|
| **Lightweight** | Two-way door; single team | 30 min; context + one diagram |
| **Standard** | New service or integration | 60 min; context, containers, critical path |
| **Deep** | One-way door, regulated data, multi-region | 90 min + security/finops optional |

## Pre-read package

Send 24h before review:

- Problem statement (≤ 200 words)
- C4 context + container diagrams
- ADR draft or link
- NFR table with targets
- Open questions list

## Checklist

### Scope and fit

- [ ] Solves stated problem; non-goals explicit
- [ ] Fits architecture principles or documents exception
- [ ] Build vs buy justified with TCO, not preference

### Boundaries and contracts

- [ ] Clear ownership per container
- [ ] APIs/events versioned; backward compatibility plan
- [ ] No inappropriate shared databases across teams

### Reliability

- [ ] Single points of failure identified
- [ ] Timeouts, retries, idempotency on external calls
- [ ] Bulkheads / rate limits where needed
- [ ] DR story matches stated RPO/RTO

### Security and privacy

- [ ] Trust zones and authn/authz per boundary
- [ ] Secrets not in app config plaintext
- [ ] PII flow and retention documented
- [ ] Blast radius of compromise bounded

### Operability

- [ ] Logs, metrics, traces per golden signals
- [ ] Runbooks or playbooks for top failure modes
- [ ] Feature flags or safe rollout path

### Data

- [ ] System of record identified
- [ ] Consistency model explicit (sync vs eventual)
- [ ] Migration/reconciliation if dual systems

### Cost and scale

- [ ] Rough capacity model (orders of magnitude)
- [ ] Cost drivers named (egress, storage, licensed seats)

## Outcomes

Record one of:

- **Approved** — proceed; note conditions
- **Approved with actions** — fix listed items before build
- **Revise and resubmit** — major gaps
- **Deferred** — need spike or more data

Assign action owners and dates in the review notes.
