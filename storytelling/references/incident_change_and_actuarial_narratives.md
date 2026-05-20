# Incident, change, and actuarial narratives

## Table of contents

1. [Incident story principles](#incident-story-principles)
2. [Incident timeline arc](#incident-timeline-arc)
3. [Customer and internal incident messages](#customer-and-internal-incident-messages)
4. [Postmortem narrative](#postmortem-narrative)
5. [Change and transformation stories](#change-and-transformation-stories)
6. [Actuarial and insurance risk stories](#actuarial-and-insurance-risk-stories)
7. [Regulatory and sensitive audiences](#regulatory-and-sensitive-audiences)
8. [Handoffs](#handoffs)

## Incident story principles

Separate **process** (`incident-management-engineer`) from **narrative** (this skill):

| Process owns | Story owns |
|---|---|
| Severity, paging, roles | What happened in plain language |
| Status page workflow | Customer-safe wording structure |
| Action item tracking | Blameless timeline arc |
| SLO math | Impact framing (with verified numbers) |

**Rules:**

- No speculation on root cause until confirmed
- No naming individuals as villains
- Timestamp updates; version messages
- Single source of truth for facts

## Incident timeline arc

**In medias res** works well:

1. **Impact now** — who is affected, what is broken, workaround
2. **Timeline** — detection → response → mitigation → recovery (UTC)
3. **Current status** — monitoring, ETA if known (or “investigating”)
4. **Next update** — when and where
5. **Learning preview** — postmortem timing (no premature blame)

```
[TIME] — [Observable event]
[TIME] — [Action taken]
[TIME] — [Customer-visible change]
```

Gap markers: “Unknown between X and Y—under investigation.”

## Customer and internal incident messages

| Audience | Emphasis | Avoid |
|---|---|---|
| **Customer** | Impact, workaround, next update | Internal tool names, blame |
| **Internal** | Technical detail, owners, runbook links | Speculation as fact |
| **Exec** | Business impact, decision needs, reputational risk | Ticket-level noise |

**Holding line pattern:**

```
We are investigating [symptom] affecting [scope].
Impact: [user-visible effect].
Workaround: [if any].
Next update: [time] via [channel].
```

Route legal/security review per severity with `communication-lead`.

## Postmortem narrative

Blameless postmortem **story arc**:

1. **Summary** — impact, duration, customer effect (facts)
2. **Timeline** — detailed, linked to artifacts
3. **Root cause** — technical + contributing factors (systems)
4. **What went well** — detection, collaboration
5. **What went wrong** — gaps without personal attack
6. **Action items** — owner, due date, verification method
7. **Lessons** — durable policy or design change

**Learning story test:** Could a new engineer understand how the system failed and what we changed?

## Change and transformation stories

Organizational change needs **empathy + clarity**:

| Beat | Content |
|---|---|
| Why | External or internal driver (honest) |
| What | New structure, process, or policy |
| Who | Affected groups (specific) |
| When | Phased timeline with milestones |
| How to get help | Channels, FAQ, office hours |
| What stays the same | Reduce anxiety with anchors |

**Manager cascade:** Same spine; managers add team-specific examples.

Pair with `communication-lead` for company-wide rollout wording.

## Actuarial and insurance risk stories

Translate technical actuarial work for **non-technical** listeners without losing integrity:

| Technical concept | Narrative handle |
|---|---|
| Reserve | Money set aside for expected future claims |
| IBNR | Claims incurred but not yet reported |
| Loss ratio | Claims cost per premium dollar |
| Tail risk | Rare large events that drive capital needs |
| Assumption change | Why the estimate moved (driver, not black box) |

**Structure:**

1. **Question** — what decision the audience must make
2. **Answer headline** — central estimate or direction
3. **Drivers** — 2–3 factors in plain language
4. **Uncertainty** — range or sensitivity (“if X, then Y”)
5. **Actions** — pricing, reinsurance, capital, or monitoring

Do **not** simplify away material limitations—state them in one sentence.

Deep modeling stays with `actuary` / `actuarial-consulting`; storyteller shapes **explanation**.

## Regulatory and sensitive audiences

| Trigger | Action |
|---|---|
| Public company disclosure | Counsel + IR review |
| Regulatory filing narrative | Actuarial/consulting owner; legal review |
| Media-facing incident | `communication-lead` + approved spokespeople |
| PHI/PII in examples | Redact; synthetic data only |

Never promise outcomes regulators must approve.

## Handoffs

| Need | Skill |
|---|---|
| Incident severity, paging, SEV program | `incident-management-engineer` |
| Crisis wording approval | `communication-lead` |
| Reserve methodology, opinions | `actuary`, `actuarial-consulting` |
| Cross-dept vocabulary in PMO updates | `cross-department-translation` |
| Compliance control narratives | `compliance-engineer` |
