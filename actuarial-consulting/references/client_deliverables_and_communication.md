# Client deliverables and communication

## Table of contents

1. [Audience mapping](#audience-mapping)
2. [Actuarial memo structure](#actuarial-memo-structure)
3. [Exhibits and workpapers](#exhibits-and-workpapers)
4. [Management presentation](#management-presentation)
5. [Q&A and issue log](#qa-and-issue-log)
6. [Distribution and redaction](#distribution-and-redaction)

## Audience mapping

| Audience | Lead with | Avoid |
|---|---|---|
| CFO / Finance | Reserve movement, margin, capital impact | Excessive factor jargon without summary |
| CRO / Risk | Tail risk, model risk, sensitivity | Unqualified certainty |
| CEO / Board | Materiality, decisions needed, timeline | Raw triangles without headline |
| External audit | Tie-out to GL, change vs prior, controls | Advocacy without documentation |
| Regulators (overview) | Consistency with filings, assumption changes | Legal conclusions |

Match **tone** to role: executives need decision-ready bullets; technical readers need exhibits.

## Actuarial memo structure

Recommended outline:

```markdown
# [Engagement title] — Actuarial Memorandum

**Date | Prepared for | Purpose | Limitations**

## Executive summary
- Scope, conclusion headline, material findings (3–7 bullets)

## Background and scope
- Decision, data period, LOBs, standards referenced (overview)

## Methods summary
- Headline methods; point to exhibits for detail

## Results
- Key metrics, bridges (prior to current), ranges where appropriate

## Findings and recommendations
- Numbered findings; owner; target date

## Limitations and reliance
- Data, scope, non-advice

## Exhibits index
```

Keep the memo **self-contained** for executives; move tables to numbered exhibits.

## Exhibits and workpapers

| Exhibit type | Typical content |
|---|---|
| A | Scope and data summary |
| B | Triangle or development summary (from `actuary`) |
| C | Reserve / pricing bridge |
| D | Sensitivity tables |
| E | Assumption change log |
| F | Model inventory (validation engagements) |

Rules:

- One **message per exhibit**; title states the takeaway
- Footnote **data cutoff** and **definitions**
- Cross-reference memo section ↔ exhibit number

## Management presentation

Target **5–12 slides**:

1. Context and decision
2. Scope and approach (one slide)
3. Headline results
4. Material findings (ranked)
5. Sensitivities or scenarios (if decision-relevant)
6. Recommendations and open items
7. Appendix index (optional backup)

Use **consistent metrics** with memo and prior public disclosures. Prepare **speaker notes** with anticipated challenges.

## Q&A and issue log

Maintain during engagement:

| ID | Question | Owner | Status | Resolution |
|---|---|---|---|---|
| Q1 | … | Client actuary | Open | … |

Use for workshop readouts, board prep, and final memo “open items” section.

## Distribution and redaction

- Define **distribution list** (names, not “management”)
- Redact **policyholder PII** and counterparty terms in external packs
- Version files: `Memo_v1.0_draft`, `Memo_v1.0_final`
- Store final PDF and source workbook paths in engagement index

For transaction work, align with **data room** rules and `commercial-counsel` on what may leave the room.
