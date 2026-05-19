# Eval Dataset Design

## Case anatomy

| Field | Purpose |
|---|---|
| `id` | Stable reference |
| `input` | User message(s) or thread |
| `context` | Optional fixtures (user role, locale, flags) |
| `expected` | Behavior specification (see below) |
| `tags` | domain, risk, tool, difficulty |

## Expected behavior types

| Type | Use when |
|---|---|
| **Exact match** | Structured JSON, enum answers |
| **Contains** | Must mention policy section or value |
| **Tool call** | Must invoke `tool_name` with arg constraints |
| **No tool** | Must answer without tools |
| **Refusal** | Must decline safely |
| **Trajectory** | Ordered steps (tool A → tool B → answer) |

Avoid brittle full-string match on prose unless necessary.

## Coverage matrix

Tag cases across:

| Dimension | Examples |
|---|---|
| **Intent** | FAQ, action, complaint, ambiguous |
| **Tools** | Each tool + never-use paths |
| **Failure** | Tool timeout, empty retrieval, 403 |
| **Safety** | Injection in user text, exfil attempts |
| **Locale** | Language, units, date formats |

Target **50–200** cases for CI; grow with every production failure.

## Building the set

| Source | Notes |
|---|---|
| **Production logs** | Sample and redact PII |
| **SME gold** | Domain Q&A pairs |
| **Synthetic** | Fill gaps; label carefully |
| **Regression** | One case per fixed bug |

Version dataset with prompt (`dataset v3` + `prompt v1.4`).

## Maintenance

- Add case **before** fixing prompt (repro first)
- Retire flaky cases or tighten expected behavior
- Review quarterly for stale product facts
