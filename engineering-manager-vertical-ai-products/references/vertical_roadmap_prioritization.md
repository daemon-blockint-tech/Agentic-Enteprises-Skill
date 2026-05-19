# Vertical Roadmap and Prioritization

## Backlog item template

| Field | Example |
|---|---|
| **Vertical** | Financial services |
| **Outcome** | Cut analyst research time 30% |
| **AI capability** | Document Q&A over customer filings |
| **Platform deps** | New parser plugin; eval harness v2 |
| **Risk tier** | Tier 2 (customer data, human review) |
| **GTM tie** | Q4 enterprise package |

## Prioritization axes

| Axis | Question |
|---|---|
| **Revenue / retention** | Attached to enterprise deal or churn risk? |
| **Platform leverage** | Builds reusable vertical module? |
| **Risk** | Regulated data or customer-facing autonomy? |
| **Feasibility** | Eval baseline already > threshold? |
| **Cost** | Token $ per session within unit economics? |

Balance **vertical wins** with **horizontal platform debt** — negotiate 70/30 or explicit platform OKRs.

## Build vs configure

| Choice | Prefer when |
|---|---|
| **Configure** (prompts, tools, KB) | Same RAG stack; domain content differs |
| **Extend platform** | Missing vertical primitive (e.g. citation format) |
| **Vertical-only code** | Regulated workflow UI; avoid polluting platform |

Escalate extend-vs-fork to `applied-ai-architect-commercial-enterprise`.

## Capacity

- Reserve **25%** for eval debt, incidents, platform upgrades
- Limit **concurrent Tier-1 AI launches** per squad
- Front-load **data + SME time** before engineering sprints

## Escalation

Escalate when: deal-driven date conflicts with eval gate; vertical needs exception to platform security; headcount mismatch to committed vertical OKRs.
