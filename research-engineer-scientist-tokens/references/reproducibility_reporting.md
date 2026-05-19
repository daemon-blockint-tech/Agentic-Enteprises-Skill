# Reproducibility and research reporting

## Table of contents

1. [Artifact checklist](#artifact-checklist)
2. [Memo structure](#memo-structure)
3. [Handoff to engineering](#handoff-to-engineering)
4. [Publication hygiene](#publication-hygiene)

## Artifact checklist

- [ ] Git commit or tag for code
- [ ] Config YAML with all arms
- [ ] Eval set version hash
- [ ] Model names and API versions
- [ ] Random seeds listed
- [ ] Raw per-item results CSV
- [ ] Aggregated tables + plots scripts
- [ ] README: how to rerun one command

## Memo structure

1. **Question and hypothesis**
2. **Setup** — models, data, metrics (primary pre-registered)
3. **Results** — tables, CIs, Pareto
4. **Ablations** — what drove effect
5. **Limitations** — data bias, eval gaps, short runs
6. **Recommendation** — ship / iterate / abandon with thresholds
7. **Appendix** — prompts (redacted if needed), failure examples

One-page **executive summary** with tokens saved at fixed quality ε.

## Handoff to engineering

| Research output | Consumer skill |
|---|---|
| Validated compression ratio | `ai-context-engineer` |
| Prompt/token template wins | `prompt-engineer` |
| Program priorities and KPIs | `ai-token-improvement-plan-engineer` |
| Architecture choice | `applied-ai-architect-commercial-enterprise` |
| Production implementation | `ai-engineer` |

Include **guardrail evals** required before prod flag.

## Publication hygiene

- Cite prior art and baselines fairly
- Do not overclaim from synthetic evals only
- Separate **internal** vs **external** communicable results
- No customer data in public artifacts
- Note **assisted-by AI** if company policy requires on internal memos

Negative results worth archiving to prevent duplicate work.
