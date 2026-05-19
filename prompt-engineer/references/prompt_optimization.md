# Prompt Optimization & Testing

## Evaluation Frameworks

### Human Evaluation

| Dimension | Question | Scale |
|---|---|---|
| Accuracy | Is the information correct? | 1-5 |
| Relevance | Does it answer the question? | 1-5 |
| Completeness | Are all aspects covered? | 1-5 |
| Clarity | Is it easy to understand? | 1-5 |
| Format | Does it match the requested format? | Pass/Fail |
| Safety | Is it free of harmful content? | Pass/Fail |

### Automated Evaluation

| Method | Metric | Tool |
|---|---|---|
| Exact match | String comparison | Python `==` |
| Semantic similarity | Cosine similarity of embeddings | sentence-transformers |
| LLM-as-judge | Rubric-based scoring | Same/different model |
| Format validation | Schema compliance | JSON Schema, Pydantic |
| BLEU/ROUGE | N-gram overlap | NLTK, evaluate |

**LLM-as-judge prompt:**
```
Evaluate the following response based on these criteria:
- Accuracy (1-5): Is the information factually correct?
- Helpfulness (1-5): Does it directly address the user's need?

User question: {question}
Response: {response}

Provide scores and a brief justification.
```

## A/B Testing Prompts

### Experiment Design

1. **Hypothesis**: "Adding a role description will improve code review quality by 15%"
2. **Variants**:
   - Control: Baseline prompt
   - Treatment: Baseline + role description
3. **Sample size**: 100 examples per variant (minimum)
4. **Metrics**: Accuracy score, format compliance, token cost
5. **Duration**: Run until statistical significance (p < 0.05)

### Analysis Template

| Variant | N | Mean Score | Std Dev | p-value | Winner |
|---|---|---|---|---|---|
| Control | 100 | 3.2 | 0.8 | — | — |
| Treatment A | 100 | 3.8 | 0.7 | 0.003 | ✅ |
| Treatment B | 100 | 3.3 | 0.9 | 0.42 | — |

## Prompt Versioning

### Version Control Best Practices

```
prompts/
  summarize_v1.0.0.md      # Initial release
  summarize_v1.1.0.md      # Added examples
  summarize_v1.2.0.md      # Switched to JSON output
  summarize_latest.md -> v1.2.0  # Symlink
```

**Semantic versioning for prompts:**
- **Major**: Breaking change in output format or behavior
- **Minor**: New feature, backward compatible
- **Patch**: Bug fix, wording improvement, no behavior change

### Metadata Template
```yaml
---
name: summarize_article
version: 1.2.0
model: gpt-4-turbo
temperature: 0.3
max_tokens: 200
author: @prompt-engineer
last_updated: 2024-01-15
metrics:
  accuracy: 0.87
  latency_p50: 800ms
  cost_per_1k: $0.03
changelog:
  - 1.2.0: Added JSON schema for structured output
  - 1.1.0: Included 3-shot examples for consistency
  - 1.0.0: Initial release
---
```

## Regression Testing

### Test Suite Structure
```
tests/
  prompts/
    test_summarize.py
  fixtures/
    articles/
      short.txt
      long.txt
      technical.txt
  expected/
    summarize_short.json
    summarize_long.json
    summarize_technical.json
```

### Test Categories

| Category | Examples | Frequency |
|---|---|---|
| Happy path | Normal inputs | Every change |
| Edge cases | Empty, very long, unicode | Every change |
| Adversarial | Prompt injection attempts | Weekly |
| Format | JSON compliance, schema validation | Every change |
| Performance | Latency, token count | Weekly |

## Cost Optimization

### Token Reduction Strategies

| Technique | Savings | Implementation |
|---|---|---|
| Shorter prompts | 20-40% | Remove fluff, use abbreviations |
| Fewer examples | 30-50% | Dynamic example selection |
| Smaller model | 50-90% | Use GPT-3.5 for simple tasks |
| Caching | 80-100% (cache hits) | Store common responses |
| Batch processing | 10-20% | Send multiple requests together |

### Model Selection Guide

| Task | Recommended Model | Cost Tier |
|---|---|---|
| Simple classification | GPT-3.5-turbo | Low |
| Complex reasoning | GPT-4-turbo | Medium |
| Code generation | Claude 3.5 Sonnet | Medium |
| Multi-modal | GPT-4o / Claude 3 | High |
| Creative writing | Claude 3 Opus | High |
| Embedding | text-embedding-3-small | Very Low |

### Cost Monitoring

```python
# Track per-request cost
import tiktoken

def estimate_cost(prompt_tokens, completion_tokens, model="gpt-4"):
    pricing = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-3.5-turbo": {"input": 0.0015, "output": 0.002}
    }
    p = pricing.get(model, pricing["gpt-3.5-turbo"])
    return (prompt_tokens * p["input"] + completion_tokens * p["output"]) / 1000
```

## Latency Optimization

| Technique | Impact | Trade-off |
|---|---|---|
| Streaming | Perceived faster | More complex client |
| Lower max_tokens | Faster completion | May truncate |
| Simpler model | Faster inference | Lower quality |
| Caching | Instant (hit) | Stale responses |
| Async processing | Non-blocking | Delayed results |

## Temperature & Sampling

| Temperature | Use Case |
|---|---|
| 0.0 | Deterministic output, coding, data extraction |
| 0.3-0.5 | Balanced: most tasks, Q&A |
| 0.7-0.9 | Creative: marketing, brainstorming |
| 1.0+ | Highly diverse: idea generation, exploration |

**Other sampling parameters:**
- `top_p`: Nucleus sampling (alternative to temperature)
- `frequency_penalty`: Reduce repetition
- `presence_penalty`: Encourage topic diversity
