# High-reliability organization principles

## Table of contents

1. [HRO overview](#hro-overview)
2. [Five principles in practice](#five-principles-in-practice)
3. [Behaviors by role](#behaviors-by-role)
4. [Normalization of deviance](#normalization-of-deviance)
5. [Classified and safety-critical overlays](#classified-and-safety-critical-overlays)
6. [Assessment checklist](#assessment-checklist)

## HRO overview

**High-reliability organizations** operate in domains where failures are rare but catastrophic—aviation, nuclear, healthcare, military systems, large-scale cloud control planes.

HRO success depends on **collective mindfulness**, not heroic individuals. This reference translates Weick/Sutcliffe-style HRO ideas into engineering and operations rituals.

## Five principles in practice

| Principle | Meaning | Engineering rituals |
|---|---|---|
| **Preoccupation with failure** | Treat small signals as data | Near-miss reviews; weak-signal dashboards; “almost” postmortems |
| **Reluctance to simplify** | Resist single-story explanations | Multi-cause diagrams; required dissent in design review |
| **Sensitivity to operations** | Frontline context shapes decisions | Ops present in planning; runbook walkthroughs before launch |
| **Commitment to resilience** | Absorb surprise and recover | Graceful degradation specs; rehearsed rollback; pair `cyber-resilience-engineer` |
| **Deference to expertise** | Expertise trumps rank at the boundary | Named technical authority for stop-the-line; no silent override |

## Behaviors by role

| Role | Do | Avoid |
|---|---|---|
| **Executive** | Fund verification; protect reporters; ask “what almost failed?” | Velocity KPIs that punish escalation |
| **Engineering lead** | Staff reviews; gate ownership; pre-mortems on tier-0 | Rubber-stamp “LGTM” on critical paths |
| **Individual contributor** | Report near-miss; halt ambiguous deploy | Quiet fixes that bypass change control |
| **SRE** | Pair prevention metrics with SLOs (`site-reliability-engineer`) | Treat all risk as budgetable without tiering |
| **Incident manager** | Separate learning from command (`incident-management-engineer`) | Blame-focused postmortems |

## Normalization of deviance

**Normalization of deviance** occurs when repeated workaround becomes “how we do it” until an accident exposes the gap.

| Signal | Example | Response |
|---|---|---|
| Drift from standard | Manual prod hotfix weekly | Stop-the-line; fix pipeline |
| Weak alarms | Alert fatigue; muted pages | Tune + fix root cause; don’t delete signal |
| Gate bypass culture | “Emergency” every Friday | Audit bypasses; tighten criteria |
| Hero dependency | One person always saves deploy | Cross-train; automate checks |
| Documentation theater | Runbooks stale since launch | Tie releases to runbook verification |

Run a **norms audit** quarterly: interview operators and reviewers; compare written gates to observed practice.

## Classified and safety-critical overlays

| Overlay | Additional expectation |
|---|---|
| **Classified** | Change boards, inspection windows, two-person integrity—`classified-cyber-security-senior-manager` |
| **Safety-critical OT** | Physical interlocks; provenance; restricted remote access |
| **Regulated finance/health** | Segregation of duties; evidence retention for gate decisions |

Do not substitute HRO language for **legal or accreditation** obligations—coordinate with compliance owners.

## Assessment checklist

- [ ] Near-miss mechanism exists and is used without retaliation
- [ ] Design reviews record dissent and unresolved risks
- [ ] Stop-the-line authority is named and exercised in last 12 months
- [ ] Tier-0 changes have independent verification (not author-only)
- [ ] Repeat incidents trigger system fixes, not repeat training alone
- [ ] Executives receive escape/near-miss trends, not only outage counts

Score **maturity 1–4**: ad hoc → defined gates → measured escapes → continuous norm reinforcement.
