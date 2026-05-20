---
name: ai-researcher
description: |
  Guides AI research work—literature reviews, hypothesis formation, experiment design, benchmarking,
  reproducibility, and synthesis of papers and empirical results for technical decisions.
  Use when surveying state of the art, comparing models or methods, designing ablation studies,
  writing research memos, critiquing methodology, or planning novel experiments—not for shipping
  production LLM features (ai-engineer), enterprise AI policy (ai-risk-governance), or adversarial
  product testing (ai-redteam). Token efficiency experiments and tokens-to-success benchmarks:
  research-engineer-scientist-tokens. Safety classifier and harm-benchmark research:
  ml-research-engineer-safeguards. RL training systems engineering: ml-systems-engineer-rl-engineering.
---

# AI Researcher

## When to Use

- Surveying state-of-the-art models, methods, or benchmarks
- Comparing model families or techniques with fair experimental design
- Designing ablation studies with controlled variables
- Writing research memos or technical reports for stakeholder decisions
- Critiquing methodology in papers or internal experiments
- Planning novel experiments with falsifiable hypotheses
- Reproducing published results and verifying claims

## When NOT to Use

- Shipping production LLM features, RAG, or agent systems → `ai-engineer`
- Enterprise AI policy, regulation, or risk tiering → `ai-risk-governance`
- Adversarial product testing or jailbreak campaigns → `ai-redteam`
- Classical ML pipelines, A/B testing, or statistical analysis → `data-scientist`

## Related skills

| Need | Skill |
|---|---|
| Production RAG, agents, deployment | `ai-engineer` |
| Prompt and agent implementation detail | `prompt-engineer` |
| Classical ML and A/B statistics | `data-scientist` |
| Governance, regulation, risk registers | `ai-risk-governance` |
| Red-team attacks on deployed systems | `ai-redteam` |
| Token/context efficiency research | `research-engineer-scientist-tokens` |
| Safeguard ML benchmarks and classifiers | `ml-research-engineer-safeguards` |
| RL distributed training infrastructure | `ml-systems-engineer-rl-engineering` |

## Core Workflows

### 1. Research question framing

1. Convert vague ask into falsifiable question
2. Define scope: task, data regime, compute budget, timeline
3. List baselines that must be beaten or matched
4. Specify primary and secondary metrics
5. Document assumptions and out-of-scope items

**See `references/research_framing.md` for question templates and hypothesis types.**

### 2. Literature review

**Process:**

1. Search: arXiv, ACL Anthology, OpenReview, major labs' blogs
2. Screen by relevance, recency, citation quality
3. Extract: problem, method, data, metrics, limitations
4. Synthesize themes and open gaps
5. Cite primary sources; avoid over-relying on secondary summaries

**See `references/literature_review.md` for screening matrix and synthesis outline.**

### 3. Experimental design

| Element | Requirement |
|---|---|
| Baselines | Strong and fair (same data, tuning budget) |
| Ablations | One change at a time |
| Seeds | Multiple runs for stochastic methods |
| Stats | Confidence intervals, not single-point luck |
| Reproducibility | Config, data version, code commit logged |

**See `references/experiment_design.md` for power analysis pointers and leakage checks.**

### 4. Benchmarking and analysis

- Use public benchmarks when task-aligned; document train/test contamination risk
- Report compute cost (GPU hours) alongside accuracy
- Separate in-distribution vs stress tests
- Visualize failure modes, not only aggregate scores

**See `references/benchmarking.md` for leaderboard caveats and custom eval sets.**

### 5. Research communication

**Deliverable types:** memo (1–3 pages), technical report, slide deck for decision meeting.

Include: question, method summary, results table, limitations, recommended next step.

**See `references/research_writing.md` for memo structure and peer-review checklist.**

## When to load references

- **Question and hypothesis** → `references/research_framing.md`
- **Literature survey** → `references/literature_review.md`
- **Experiments** → `references/experiment_design.md`
- **Benchmarks** → `references/benchmarking.md`
- **Writing** → `references/research_writing.md`
