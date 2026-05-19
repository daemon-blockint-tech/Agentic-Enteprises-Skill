# Research framing (tokens)

## Table of contents

1. [Question types](#question-types)
2. [Hypothesis templates](#hypothesis-templates)
3. [Primary metrics](#primary-metrics)
4. [Scope checklist](#scope-checklist)

## Question types

| Type | Example |
|---|---|
| Efficiency | Does method X cut input tokens 30% at equal task success? |
| Utilization | What fraction of context is attended for task Y? |
| Tokenization | How does delimiter choice change token count across models? |
| Long context | At what depth does retrieval accuracy degrade? |
| Routing | Can a router send 80% of queries to a small model without quality loss? |
| Compression | Does hierarchical summary preserve constraint-following? |

## Hypothesis templates

- **H1:** Under fixed eval set E, strategy S reduces median **tokens-to-success** by ≥δ vs baseline B.
- **H2:** Quality metric Q is non-inferior (ε margin) while input tokens decrease ≥δ.
- **H3:** Failure mode F (e.g., missed needle) increases when compressed context exceeds k tokens.

State **falsification** criteria up front.

## Primary metrics

Pick one primary; others secondary:

| Metric | Definition |
|---|---|
| Tokens-to-success | Total in+out tokens until task pass |
| Tokens per turn | Mean tokens per user turn in multi-turn |
| Effective context | Tokens actually carrying task-relevant signal (proxy via ablation) |
| Cost per success | Tokens × price table + fixed overhead |
| Cache hit rate | Prefix/cache tokens not billed or billed lower |
| Latency per token | Wall time / output tokens (throughput research) |

Always pair with **task quality**: pass@1, win rate, rubric score, human preference.

## Scope checklist

- [ ] Model(s) and snapshot dates fixed
- [ ] Tokenizer/API version documented
- [ ] Eval set frozen and versioned
- [ ] Compute budget cap stated
- [ ] Excluded: safety regressions unless in scope
- [ ] Human eval budget if claiming subjective quality
