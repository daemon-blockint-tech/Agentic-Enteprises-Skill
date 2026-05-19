# AI Feature Launch Governance

## Pre-GA checklist (customer-facing)

| Gate | Owner | Evidence |
|---|---|---|
| Risk tier assigned | `ai-risk-governance` | Tier doc / ticket |
| Eval suite pass | `ai-engineer` | CI + offline report |
| Regression vs prior release | AI eng | No critical metric drop |
| Red-team (if Tier 1–2) | `ai-redteam` | Findings closed or accepted |
| Kill switch / rollback | Platform + vertical | Runbook tested |
| Observability | `ai-lead-ops` patterns | Traces, cost, safety signals |
| Legal / DPA | Counsel | Subprocessor list updated if needed |
| GTM enablement | PM + sales | Demo script, limitations doc |

Coordinate tiers with `applied-ai-architect-commercial-enterprise` ADRs.

## Launch phases

| Phase | Activities |
|---|---|
| **Alpha** | Internal + SME; eval set frozen |
| **Beta** | Limited customers; human-in-loop default |
| **GA** | Eval gate; support trained on limitations |
| **Hypercare (7–14d)** | Daily metric review; fast patch path |

## Rollback triggers

- Safety incident or policy violation
- Eval regression beyond agreed threshold
- Cost overrun >2× forecast without approval
- Critical wrong-answer pattern in production logs

## Post-launch

- Retro: eval gaps, platform asks, SME quality
- Feed **golden set** updates into eval harness
- Ticket horizontal platform improvements with priority label

## Internal / low-tier features

Lighter checklist — still require eval smoke and owner sign-off.
