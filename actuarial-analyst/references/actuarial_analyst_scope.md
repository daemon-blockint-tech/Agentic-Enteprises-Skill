# Actuarial analyst scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Relationship to actuary and consulting](#relationship-to-actuary-and-consulting)
3. [Typical assignments](#typical-assignments)
4. [Lines of business (analyst lens)](#lines-of-business-analyst-lens)
5. [Professional standards (analyst)](#professional-standards-analyst)
6. [Escalation triggers](#escalation-triggers)

## Role boundary

The **actuarial analyst** executes technical preparation, calculation support, reconciliation, and exhibit production under **actuarial direction**. The analyst does **not** own:

| Out of analyst scope | Route to |
|---|---|
| Statement of actuarial opinion / appointed actuary sign-off | `actuary` |
| Engagement letter, SOW, client strategy | `actuarial-consulting` |
| Enterprise assumption approval and governance | `assumption-setting` |
| ALM policy and strategic asset allocation | `asset-liability-management` |
| Legal interpretation of policy or filing requirements | `commercial-counsel` / `corporate-counsel` |

| In scope (analyst) | Examples |
|---|---|
| Triangle build and factor tables | Paid/incurred by AY and lag |
| IBNR support schedules | Ultimates, diagnostics, PYD bridge |
| Pricing experience tables | Segment pure premium, trend, credibility application |
| Data validation | Bordereaux tie-out, key integrity, cutoff checks |
| Model run support | Input prep, output reasonability, run documentation |
| Reporting tie-outs | Statutory schedule ↔ workpaper mapping |
| Workpaper packaging | Exhibit index, QA checklist, version control |

## Relationship to actuary and consulting

```
Client / management question
        ↓
actuarial-consulting (engagement framing) — optional
        ↓
actuary (methods, assumptions, sign-off)
        ↓
actuarial-analyst (data, exhibits, reconciliations, runs)
```

Analysts **implement** methods the actuary selects; they **propose** diagnostics and alternatives in a support memo, not as final professional judgment.

## Typical assignments

| Assignment | Analyst primary outputs | Actuary decision |
|---|---|---|
| Quarterly reserve update | Triangles, factor picks draft, IBNR table | Method, tail, final ultimates |
| Rate filing support | Experience, trend, indication tables | Implemented rate, constraints |
| Model production run | Inputs, outputs, diffs | Assumption version, acceptance |
| Statutory tie-out | Line-by-line reconciliation | Materiality, adjustments |
| Experience study prep | A/E tables, outliers flagged | Assumption updates → `assumption-setting` |
| Pension valuation data | Census roll-forward, check totals | Assumptions and certification |

## Lines of business (analyst lens)

| LOB | Analyst emphasis | Common data issues |
|---|---|---|
| P&C | Development triangles; class/territory splits | Case reserve adequacy shifts; cat years |
| Life | In-force reconciliations; claim experience cuts | Lapse spikes; partial records |
| Health | Monthly seasonality; benefit change flags | Provider grouping changes |
| Reinsurance | Ceded gross/net alignment | Treaty mapping errors |
| Pension | Census vs liability roll-forward | Missing termination reasons |

Coordinate **line context** with `property-casualty-insurance`, `life-health-insurance`, or `pension-retirement-funds` when the user needs product or plan mechanics beyond exhibit production.

## Professional standards (analyst)

Align workpapers so a **qualified actuary** can evaluate:

- **Traceability** — Source → transformation → exhibit cell
- **Definitions** — Every metric footnoted (basis, cutoff, net/gross)
- **Versioning** — Data cut date, model build, assumption memo reference
- **Transparency** — Hard-coded adjustments explained; no hidden plugs
- **Confidentiality** — Redact policyholder fields per firm policy

Do not misrepresent analyst tables as **signed actuarial opinion**.

## Escalation triggers

Escalate to `actuary` (and document in open-items log) when:

- Triangle diagnostics imply **method change** (e.g., shift from chain ladder to BF)
- **Tail factor** or cat treatment is material and undocumented
- **Credibility** or trend differs materially from approved assumptions
- **Model output** diverges from plan or prior quarter beyond tolerance
- **Regulatory** or **legal** interpretation is requested
- **Assumption change** is needed → also involve `assumption-setting` for governance
