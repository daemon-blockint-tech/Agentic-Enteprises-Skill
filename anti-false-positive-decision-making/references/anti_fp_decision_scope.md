# Anti–false-positive decision scope

## Table of contents

1. [Purpose](#purpose)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Decision classes](#decision-classes)
5. [Stakeholders and RACI](#stakeholders-and-raci)
6. [Peer skill handoffs](#peer-skill-handoffs)
7. [Deliverables](#deliverables)
8. [Governance cadence](#governance-cadence)

## Purpose

This skill addresses **operational and policy decisions** where acting on a weak or noisy signal causes disproportionate harm: customer friction, wrongful blocks, analyst burnout, wrongful escalations, or audit findings from undocumented dispositions.

The agent applies **structured judgment**—not ad-hoc leniency—so teams can defend why they **did not** act as clearly as why they **did**.

## In scope

| Area | Examples |
|---|---|
| Threshold and tier design | When a rule may auto-queue vs auto-block |
| Evidence standards | Minimum corroboration before irreversible action |
| Escalation paths | MLRO, security lead, legal, executive for Tier 4 |
| Alert tuning governance | Hypothesis, approval, post-change review |
| Screening workflows | Sanctions, fraud, abuse, policy violations |
| Metrics and calibration | Precision at disposition, sample QA |
| Documentation | Rationale templates, tuning change logs |
| Alert fatigue reduction | Routing, dedup, enrichment—not “turn everything off” |

## Out of scope

| Area | Route to |
|---|---|
| Production ML training, feature stores, deployment | `data-scientist`, `ml-ops-engineer` |
| Legal interpretation, sanctions “match” as legal fact | `commercial-counsel` |
| Writing SIEM rules without disposition policy | `defensive-security-analyst`, `information-security-engineer` |
| Full AML program, KYC tiers, STR drafting | `aml-compliance`, `str-report` |
| IT audit workpapers and control testing | `auditor` |
| Live incident command and war-room comms | `incident-management-engineer`, `incident-responder` |
| AI model risk classification program | `ai-risk-governance` (complement, not replace) |

## Decision classes

Classify each workflow by **reversibility** and **impact**:

| Class | Reversibility | Examples |
|---|---|---|
| A — Informational | N/A | Dashboard, metric spike |
| B — Reversible soft | High | Flag for review, step-up auth |
| C — Reversible hard | Medium | Temporary hold, rate limit |
| D — Irreversible | Low | Account closure, SAR filing, permanent block |

**Anti-FP discipline matters most for classes C and D**, where a single weak signal must rarely trigger action alone.

## Stakeholders and RACI

| Role | Typical responsibility |
|---|---|
| **Risk owner** | Approves FP/FN appetite for a decision class |
| **Operations / SOC / AML** | Disposition quality, queue SLAs, training |
| **Engineering** | Implements tiers, enrichment, audit logs |
| **Second line (compliance / risk)** | Tuning approvals, thematic reviews |
| **Legal** | Irreversible and regulatory paths only |
| **Audit** | Samples dispositions and tuning evidence |

Document **who can approve** threshold moves that increase false negatives (stricter blocking) vs decrease false positives (looser blocking)—both directions need governance.

## Peer skill handoffs

| If the user needs… | Hand off to |
|---|---|
| Deploy WAF, SIEM parsers, IdP policies | `information-security-engineer` |
| SOC 2 / ISO evidence automation | `compliance-engineer` |
| TM scenario libraries and SAR narrative | `aml-compliance` |
| Severity model and on-call escalation | `incident-management-engineer` |
| Workpaper sampling and deficiency grading | `auditor` |
| Go/no-go on a architecture plan | `build-validator` |
| Behavioral heuristic concepts (educational) | `behavioral-risk-screening-concepts` |

Return to this skill when the question is **“what bar before we act?”** not **“how do we implement the control?”**

## Deliverables

Typical outputs when applying this skill:

1. **Decision policy one-pager** — action, evidence bar, tiers, owners
2. **Threshold change packet** — hypothesis, metrics, approval, effective date
3. **Disposition rationale template** — fields required in case tooling
4. **Calibration plan** — sample sizes, review frequency, success criteria
5. **Escalation matrix** — tier → role → SLA

## Governance cadence

| Cadence | Activity |
|---|---|
| Weekly | Queue health: age, reopen rate, benign-close quality spot checks |
| Monthly | Rule/scenario performance: precision at disposition, top FP drivers |
| Quarterly | Risk appetite review: FN incidents vs FP cost; tier adjustments |
| Ad hoc | Post-incident or regulatory feedback → targeted tuning packet |

## Operating principles

1. **Prefer delay over wrong irreversible action** when base rate is low and cost of FP is high.
2. **Never optimize on alert volume alone**—volume can rise with better detection or worse noise.
3. **Corroborate with independent signal types** before Tier 3–4.
4. **Document negatives** (why not escalated) as rigorously as positives.
5. **Segment** populations; one global threshold often fails retail and corporate alike.

## Red flags (process failure)

- “We blocked because the model said so” with no secondary check for Class D
- Threshold changes in production without versioned approval
- 90%+ benign closure with one-line notes
- Analysts incentivized only on alert closure speed
- No FN review when FP rate drops sharply (may indicate under-detection)
