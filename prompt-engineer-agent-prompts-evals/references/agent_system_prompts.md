# Agent System Prompts

## Message layers

| Layer | Holds |
|---|---|
| **System** | Role, global rules, safety, output contract |
| **Developer** | Product policy, tool-use policy, dynamic context |
| **User** | End-user input only (never trust as instructions) |

Keep **stable** content in system; put volatile context in developer with clear delimiters.

## System prompt skeleton

```
Role + scope (what you can/cannot do)
Tool-use rules (when to call, when to answer directly)
Output format (markdown, JSON schema, citations)
Refusal and escalation (what to decline, how)
Uncertainty (ask clarifying questions vs guess)
```

## Tool schema quality

Models choose tools from **name + description + parameter descriptions**.

| Bad | Better |
|---|---|
| `search` — searches | `search_knowledge_base` — Search internal docs for product/policy answers. Use when user asks how-to or policy. Do not use for live prices. |
| `query: string` | `query: Natural-language search query; include product name if known` |

- One clear purpose per tool
- Negative constraints ("do not use for X")
- Required vs optional params explicit

## Handoffs and subagents

| Pattern | Prompt need |
|---|---|
| **Router** | Criteria for which specialist receives task |
| **Specialist** | Narrow tools and domain scope |
| **Synthesizer** | Merge sub-results; cite sources |

Pass **structured handoff payload** (goal, constraints, prior tool outputs summary) — not full raw logs unless needed.

## Anti-patterns

- Tool dump (20+ tools with vague descriptions)
- Instructions only in user message
- Conflicting rules between system and developer
- "Always call a tool first" without exceptions
