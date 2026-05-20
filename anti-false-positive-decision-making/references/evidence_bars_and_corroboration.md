# Evidence bars and corroboration

## Table of contents

1. [Evidence tiers](#evidence-tiers)
2. [Corroboration rules](#corroboration-rules)
3. [Independence](#independence)
4. [Disconfirming evidence](#disconfirming-evidence)
5. [Screening-specific patterns](#screening-specific-patterns)
6. [Security alert patterns](#security-alert patterns)
7. [Rationale template](#rationale-template)
8. [Anti-patterns](#anti-patterns)

## Evidence tiers

Define tiers **per decision class** (see `anti_fp_decision_scope.md`):

| Tier | Description | Example sources |
|---|---|---|
| E0 — Context | Background only | Customer tier, tenure |
| E1 — Weak signal | Single heuristic | Velocity spike, one IOC hit |
| E2 — Moderate | Rule + enrichment | TM scenario + KYC match |
| E3 — Strong | Multi-path agreement | Two independent rules + analyst review |
| E4 — Conclusive | Documented proof | Confirmed fraud, law enforcement, confirmed sanctions match per policy |

**Map tiers to response tiers:**

- E0–E1 → observe or soft queue
- E2 → review before customer impact
- E3 → contain pending review
- E4 → irreversible path with approvals

## Corroboration rules

**Corroboration** = at least two pieces of evidence that **jointly** increase confidence before action.

### Minimum rules (examples—adapt per policy)

| Action | Minimum evidence |
|---|---|
| Auto-close benign | E1 + negative enrichment (expected activity) |
| Customer-visible friction | E2 + analyst or E2 + second automated check |
| Funds hold | E3 or E2 + mandatory human within SLA |
| Account termination / SAR | E4 path with legal/compliance gates |

Write rules as **AND** across **independent families**, not duplicate counts of the same data.

## Independence

Evidence families should not share a single failure point:

| Family | Examples |
|---|---|
| **Transactional** | Amount, velocity, counterparties |
| **Identity / KYC** | Tier, occupation, geography |
| **Watchlist / intel** | Sanctions, adverse media (licensed) |
| **Behavioral** | Device, session, graph (where allowed) |
| **Technical security** | EDR, auth anomalies, impossible travel |
| **Human** | Analyst interview, doc request |

**Not independent:** two rules using the same raw field; model score + derived bucket from same score.

## Disconfirming evidence

Before closing or escalating, explicitly check **falsifiers**:

| Hypothesis | Disconfirming checks |
|---|---|
| Account takeover | User confirms activity; known travel; MFA success history |
| Structuring | Payroll pattern; documented business model |
| Sanctions hit | False positive on common name; DOB mismatch per policy |
| Malware beacon | Corporate VPN; known scanner; patched host |

Record **what you looked for** and **what you found** in the case note.

## Screening-specific patterns

Sanctions and PEP screening (operational—not legal advice):

| Stage | Anti-FP practice |
|---|---|
| Hit review | Require identifier match strength (name + DOB + country) per playbook |
| Auto-block | Avoid on name-only weak match; queue for review |
| Rescreen | Do not treat stale hit as new without delta |
| Whitelist | Governed whitelist with expiry and approver |

Pair with `aml-compliance` for program design; this skill sets **bars**, not vendor config alone.

## Security alert patterns

| Pattern | Corroboration before containment |
|---|---|
| Single IOC domain lookup | Pair with host execution, beaconing, or user context |
| One failed login | Rate-based tier only unless privileged account |
| Cloud “public bucket” | Confirm exposure + data class before paging exec |
| DLP single match | Context: test data, known false pattern library |

Use `defensive-security-analyst` for detection content; use this reference for **disposition bar**.

## Rationale template

Required fields for material dispositions:

```
Alert ID / case ID:
Decision: [monitor | soft | hold | escalate | close benign | confirm]
Evidence tier reached: E_
Signals (independent families):
  1.
  2.
Disconfirming checks performed:
Outcome of checks:
Residual uncertainty:
Approver (if Tier 3+):
Next review date (if monitor):
```

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| “Stacking” correlated rules | Inflates confidence artificially |
| Closing with “FP” without checks | Repeats miss on similar cases |
| Auto-block on vendor score alone | Opaque, hard to audit |
| Ignoring population context | New product looks like fraud |
| Permanent whitelist without expiry | Hides true positives later |

## Escalation when evidence is insufficient

If tier required for policy but evidence is only E1:

1. **Do not** downgrade policy silently
2. **Escalate** to risk owner for exception or temporary monitor tier
3. **Time-box** enhanced monitoring
4. **Log** exception with expiry
