# Cross-department translation scope

## Table of contents

1. [Definition](#definition)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Quality bar](#quality-bar)
5. [Common failure modes](#common-failure-modes)

## Definition

**Cross-department translation** is reframing the *same underlying facts* so each internal function receives the right **depth**, **vocabulary**, and **actionable asks**—without changing substance, hiding risk, or oversimplifying material constraints.

It is **not** machine translation between human languages unless the user explicitly requests locale/i18n work.

## In scope

| Activity | Examples |
|---|---|
| Audience reframing | RFC → finance one-pager; policy → engineering checklist |
| Dual-audience artifacts | Exec summary + technical appendix on one doc |
| Jargon decoding | Define overloaded terms; surface hidden assumptions |
| Meeting synthesis | Decisions, owner-tagged actions, open questions |
| Handoffs | RACI tables; "what receiving team needs to start" |
| Escalation packs | Situation / impact / options / asks by role |
| Metric translation | How engineering SLAs map to revenue or risk metrics |

## Out of scope

| Activity | Route to |
|---|---|
| Brand voice, external customer copy, launch messaging | `communication-lead` |
| Consulting analysis (issue trees, ROI models) without reframing | `business-consultant` |
| Program RAID, milestones, dependency management | `technical-program-manager` |
| Contract language and legal risk positions | `commercial-counsel` |
| Control design and audit evidence automation | `compliance-engineer` |
| Actuarial opinions, triangles, regulatory filings | `actuarial-consulting`, `actuary` |
| Product locale strings and cultural adaptation | localization/l10n skills if present |

## Quality bar

Good translation:

- Preserves **numbers, dates, owners, and commitments**
- Makes **assumptions explicit** (data, approvals, dependencies)
- States **one primary ask** per audience section
- Separates **must-have** from **nice-to-have**
- Surfaces **risks and trade-offs** each audience cares about

Poor translation:

- Dumbs down technical risk for executives (hides severity)
- Adds commitments the source did not authorize
- Uses buzzwords instead of defined terms
- Mixes recommendation into facts without labeling

## Common failure modes

| Failure | Fix |
|---|---|
| Same doc for everyone | Split by audience or use labeled sections |
| Jargon swap only | Add "so what" and decision impact per audience |
| Missing owner on actions | One accountable owner per action; consult RACI |
| Metric mismatch | Align definitions in a glossary footnote |
| Legal/compliance hand-waving | Quote constraint; tag for specialist review |
