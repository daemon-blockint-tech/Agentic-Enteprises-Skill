---
name: prompt-engineer
description: |
  Design, test, and optimize prompts for LLM interactions.
  Cover prompt patterns (few-shot, chain-of-thought, ReAct), system prompt design,
  output formatting, prompt evaluation, and prompt optimization techniques.
  Triggers on "write prompt", "optimize prompt", "design system prompt",
  "few-shot examples", "chain of thought", "prompt evaluation",
  "LLM output formatting", "prompt testing", or "prompt patterns".
---

# Prompt Engineer

## Overview

Design, test, and optimize prompts for LLM interactions. This skill covers prompt patterns
(few-shot, chain-of-thought, ReAct), system prompt design, output formatting, prompt evaluation,
and prompt optimization techniques.

## Features

- Prompt patterns: few-shot, zero-shot, chain-of-thought, ReAct, self-consistency
- System prompt design: role definition, constraints, output format specification
- Output formatting: JSON, XML, markdown, structured templates
- Prompt evaluation: quality metrics, consistency testing, edge case analysis
- Prompt optimization: token reduction, clarity improvement, robustness testing

## Usage

1. Identify the user's prompt need (pattern selection, system prompt, output format, or optimization)
2. Follow the corresponding workflow below
3. Produce structured outputs: prompt templates, system prompts, output schemas, or evaluation reports

## Examples

- **User**: "Write a prompt for summarization"
  **Agent**: Runs Prompt Design workflow, selects zero-shot pattern, defines role and constraints, produces prompt with output format

- **User**: "Optimize this prompt"
  **Agent**: Runs Prompt Optimization workflow, identifies ambiguity, reduces token count, adds clarity, tests edge cases

- **User**: "Evaluate prompt quality"
  **Agent**: Runs Prompt Evaluation workflow, tests against quality metrics, identifies failure modes, produces improvement recommendations

## When to Use

- Designing, versioning, and evaluating prompts for LLM-powered features
- Building agent workflows (ReAct, tool use, multi-agent coordination)
- Optimizing accuracy, format compliance, latency, and token cost
- Deploying guardrails, observability, and abuse defenses for GenAI in production

## When NOT to Use

- Classical ML model training, feature engineering, or statistical A/B tests → use `data-scientist`
- General technical writing, API reference, or runbooks → use `tech-writer-researcher`
- Cloud infrastructure, CI/CD, or Kubernetes operations → use `infrastructure-engineer`
- Revenue recognition or finance close procedures → use `senior-revenue-accountant`
- Multi-feature token reduction roadmap → use `ai-token-improvement-plan-engineer`
- Rigorous token-efficiency experiments and ablations → use `research-engineer-scientist-tokens`

## Core Workflows

### 1. Prompt Design Workflow

**Step-by-step process:**

1. **Define the task clearly**
   - What input does the user provide?
   - What output format is required?
   - What constraints must be enforced?

2. **Choose the pattern**
   | Pattern | When | Structure |
   |---|---|---|
   | Zero-shot | Simple, well-defined tasks | Instructions + input |
   | Few-shot | Pattern recognition, formatting | Examples + task |
   | Chain-of-thought | Reasoning, math, logic | "Let's think step by step" |
   | Role-based | Domain expertise needed | "You are a senior X..." |
   | Structured | API/programmatic consumption | JSON schema, XML template |

3. **Draft and iterate**
   - Start simple, add complexity only where needed
   - Use clear separators (###, XML tags, markdown)
   - Specify output format explicitly
   - Include constraints and what to avoid

4. **Test with edge cases**
   - Empty input, malformed input, adversarial input
   - Boundary conditions
   - Multiple languages or formats

### 2. Prompt Optimization & Testing

**Evaluation dimensions:**
- **Accuracy**: Does it produce correct results? (human or model judge)
- **Consistency**: Same input → same output? (temperature, seed control)
- **Format compliance**: Does output match the schema? (JSON validator)
- **Latency**: Time to first token, total generation time
- **Cost**: Tokens consumed (input + output)

**Testing workflow:**
1. Build a benchmark dataset (50-200 diverse examples)
2. Establish baseline with current prompt
3. Modify one variable at a time (prompt, model, temperature)
4. Run A/B comparison on benchmark
5. Measure and document improvement

### 3. Agent Orchestration

**Agent patterns:**

| Pattern | When | Components |
|---|---|---|
| ReAct | Tool-using agent | Reasoning + Action + Observation loop |
| Plan-and-Solve | Multi-step tasks | Planner → Executor → Checker |
| Reflexion | Self-improvement | Execute → Evaluate → Revise |
| Multi-agent | Complex workflows | Specialist agents + coordinator |

**Tool use checklist:**
- [ ] Tool schemas are clearly defined (name, description, parameters)
- [ ] Agent can handle tool failure gracefully
- [ ] Tool results are summarized, not passed raw to user
- [ ] Rate limits and costs are monitored

### 4. Production Patterns

**Security checklist:**
- [ ] Input validated and sanitized
- [ ] Prompt injection defenses in place (delimiters, output filtering)
- [ ] No sensitive data in prompts (PII, secrets)
- [ ] Output filtered for harmful content
- [ ] Rate limiting and abuse detection

**Observability:**
- Log all prompts and responses (with PII redaction)
- Track token usage and cost per user/request
- Monitor for drift in output quality
- Alert on error rates and latency spikes
