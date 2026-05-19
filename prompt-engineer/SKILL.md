---
name: prompt-engineer
description: |
  Guides prompt engineering and AI agent orchestration for LLM applications.
  Covers prompt design patterns (few-shot, chain-of-thought, role prompting, structured output),
  prompt optimization (A/B testing, evaluation, versioning), agent workflows (ReAct, tool use, planning),
  and production patterns (guardrails, observability, cost optimization).
  Use when designing prompts, building LLM-powered applications, optimizing model outputs,
  creating agentic systems, or deploying prompt-based features to production.
---

# Prompt Engineer

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

**See `references/prompt_design.md` for patterns, templates, and examples.**

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

**See `references/prompt_optimization.md` for evaluation frameworks, regression testing, and cost strategies.**

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

**See `references/agent_orchestration.md` for ReAct implementation, tool definitions, and multi-agent patterns.**

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

**See `references/production_patterns.md` for guardrails, caching strategies, and deployment patterns.**

## When to Load References

- **Prompt design** → `references/prompt_design.md`
- **Optimization & testing** → `references/prompt_optimization.md`
- **Agent orchestration** → `references/agent_orchestration.md`
- **Production patterns** → `references/production_patterns.md`
