# Team Org — Prompt & Eval

## Functions to separate

| Function | Owns |
|---|---|
| **Prompt engineering** | System/developer prompts, tool schemas |
| **Eval engineering** | Harness, golden sets, CI gates |
| **Judge program** | Rubrics, human calibration |
| **Agent platform** | Runtime, tracing — usually `ai-engineer` / platform |

EM may own first three; partner for platform.

## Models

| Model | When |
|---|---|
| **Central prompt+eval guild** | Many agents; shared standards |
| **Embedded in product squads** | Few agents; fast iteration |
| **Hybrid** | Guild sets harness + rubrics; squads own domain goldens |

Avoid: every squad forks harness; no shared pass-rate dashboard.

## Interfaces

| Partner | Cadence | Topics |
|---|---|---|
| Product | Weekly | Agent backlog, launch dates |
| `ai-lead-ops` | Bi-weekly | Incidents, rollout tiers |
| `ai-risk-governance` | Per release | Waivers, tier |
| `applied-ai-architect-commercial-enterprise` | As needed | Tool/prompt architecture |
| `ai-redteam` | Per major agent | Findings → regression cases |

## Staffing

- 1 eval engineer per 2–3 active agents in flight (rule of thumb)
- Dedicated **judge calibration** owner when >1 LLM judge in prod
- Tech lead when golden set >500 cases or multi-repo harness

## Anti-patterns

- PM owns golden set without engineering versioning
- No on-call rotation for prompt-related prod regressions
- Team only reacts to fires — no eval debt budget
