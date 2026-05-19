---
name: research-engineer-scientist-tokens
description: |
  Guides research engineering and science on LLM tokens—hypotheses about context use, tokenization,
  compression, and inference efficiency; rigorous benchmarks (tokens per task, quality–cost Pareto);
  ablation design; instrumentation and reproducible logs; and research memos that inform product
  decisions.
  Use when designing token-efficiency experiments, measuring context utilization, comparing
  compression or routing methods, analyzing tokenizer effects, or writing technical reports on
  token/cost trade-offs—not for phased cost roadmaps and owners (ai-token-improvement-plan-engineer),
  production context pipeline implementation (ai-context-engineer), single-prompt edits
  (prompt-engineer), general non-token AI research (ai-researcher), or shipping features (ai-engineer).
---

# Research Engineer / Research Scientist, Tokens

## When to Use

- Frame **research questions** on tokens, context length, or inference cost
- Design **experiments** with baselines, ablations, and statistical rigor
- Build **benchmarks** for tokens-per-successful-task, effective context, cache leverage
- Measure **tokenizer and formatting** effects on length and model behavior
- Evaluate **compression, summarization, routing, or distillation** for token savings
- Analyze **long-context** phenomena (needle, lost-in-middle, attention budget)
- Write **research memos** with reproducible methods and honest limitations
- Translate findings into **actionable thresholds** for engineering and product

## When NOT to Use

- Executive token reduction program with phased rollout → `ai-token-improvement-plan-engineer`
- Implement context packing, compaction code paths → `ai-context-engineer`
- Rewrite one production prompt → `prompt-engineer`
- General literature survey unrelated to tokens → `ai-researcher`
- Production RAG/agent deployment → `ai-engineer`
- Classical ML without LLM token focus → `data-scientist`

## Related skills

| Need | Skill |
|---|---|
| General research methodology | `ai-researcher` |
| Cost improvement program / roadmap | `ai-token-improvement-plan-engineer` |
| Production context assembly | `ai-context-engineer` |
| Prompt wording and eval harness | `prompt-engineer` |
| RAG and agent runtime build | `ai-engineer` |
| Statistical testing and cohort analysis | `data-scientist` |
| Adversarial robustness of compressed context | `ai-redteam` |
| Commercial AI architecture | `applied-ai-architect-commercial-enterprise` |

## Core Workflows

### 1. Research framing (tokens)

Hypothesis, metrics, baselines, budget.

**See `references/research_framing_tokens.md`.**

### 2. Measurement and instrumentation

Token accounting, logging, fair comparison.

**See `references/measurement_instrumentation.md`.**

### 3. Experiment design and ablations

Controls, sweeps, power, stopping rules.

**See `references/experiment_design_ablations.md`.**

### 4. Context, tokenization, and long-context

Tokenizer, placement, window effects.

**See `references/context_tokenization_longcontext.md`.**

### 5. Compression and efficiency methods

Summarization, routing, distillation research.

**See `references/compression_efficiency_methods.md`.**

### 6. Reproducibility and research reporting

Memos, artifacts, handoff to engineering.

**See `references/reproducibility_reporting.md`.**

## Outputs

- **Pre-registration / experiment plan** — hypothesis, metrics, stop criteria
- **Results table** — mean ± CI; tokens and quality side by side
- **Pareto chart narrative** — quality vs tokens at operating points
- **Ablation appendix** — what mattered, what did not
- **Research memo** — conclusion, limits, recommended next build
- **Artifact bundle** — configs, seeds, eval scripts, hashed datasets

## Principles

- **Report tokens and quality together** — never optimize one without the other
- **Match tokenizer and model** — counts from the deployment tokenizer/API
- **Control confounds** — temperature, system prompt, tool schemas held fixed across arms
- **Pre-register primary metric** — avoid p-hacking across slice metrics
- **Separate science from rollout** — research recommends; `ai-token-improvement-plan-engineer` owns program
